# v16.0.0 → v16.0.1 · 最優先の変更候補 (68)

[一覧の目次](README.md)

<a id="compare-93faf0d3c8053fa35e2894971838e34c"></a>

### [`00b0f5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f5f0.md) → [`00b0fa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0fa18.md) FUN_00b0fa18

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008609ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00860/008609ac.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`007de5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007de5bc.md)
- 新版 呼出元 1件 [`008609ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00860/008609ec.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`007de5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de5fc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.55% / 新版 73.55%

CFGの説明率　旧版 56.43% / 新版 56.20%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 52件, `unresolved_call_alignment` 17件, `unresolved_store_alignment` 63件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f74c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f75c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0fb30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0f720"
      ]
    ],
    [
      "unmatched:00b0f710",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0f740"
      ]
    ],
    [
      "unmatched:00b0f71c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0f740"
      ]
    ]
  ],
  "added": [
    [
      "00b0fb30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0fb48"
      ]
    ],
    [
      "00b0fb38",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0fb68"
      ]
    ],
    [
      "00b0fb44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0fb68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0f74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f5f0.md#insn-00b0f74c) · [`00b0f754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f5f0.md#insn-00b0f754) · [`00b0f75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f5f0.md#insn-00b0f75c)

~~~diff
- 00b0f74c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:38:8"]]
- 00b0f74c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b0f74c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b0f74c bytes 1f1c00f9
- 00b0f754 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b0f754 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b0f754 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:30:8"]]
- 00b0f754 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 00b0f754 bytes 1f0d03f8
- 00b0f75c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:28:8"]]
- 00b0f75c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b0f75c bytes 081400f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbe22abcf526191f68d20b4703cfef65"></a>

### [`00b1090c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b1090c.md) → [`00b10d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d34.md) FUN_00b10d34

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b0efe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0efe4.md) [`00b0f48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f48c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`00b0f40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f40c.md) [`00b0f8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f8b4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b10d40",
      "incomplete_value": false,
      "site": "00b10d44",
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
      "definition_site": "00b10918",
      "incomplete_value": false,
      "site": "00b1091c",
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
      "00b10d40",
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
      "00b10d40",
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

- 旧版 [`00b1091c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b1090c.md#insn-00b1091c) · [`00b10918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b1090c.md#insn-00b10918)
- 新版 [`00b10d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d34.md#insn-00b10d44) · [`00b10d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d34.md#insn-00b10d40)

~~~diff
- 00b1091c ["INT_ADD", "register:40f0:8", ["const:b1091c:8", "const:4:8"]]
- 00b1091c ["CALL", null, ["callee:0043b778:8"]]
+ 00b10d44 ["INT_ADD", "register:40f0:8", ["const:b10d44:8", "const:4:8"]]
+ 00b10d44 ["CALL", null, ["callee:0043b778:8"]]
- 00b1091c bytes 87abe497
+ 00b10d44 bytes 8daae497
- 00b10918 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b10918 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b10918 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b10918 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b10d40 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b10d40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b10d40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b10d40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b10918 bytes 00303c91
+ 00b10d40 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-618c53a32490c2092e124f3dd55ae815"></a>

### [`00b10920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10920.md) → [`00b10d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d48.md) FUN_00b10d48

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b0f5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f5f0.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`00b0fa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0fa18.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "00b10d54",
      "incomplete_value": false,
      "site": "00b10d58",
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
      "definition_site": "00b1092c",
      "incomplete_value": false,
      "site": "00b10930",
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
      "00b10d54",
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
      "00b10d54",
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

- 旧版 [`00b10930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10920.md#insn-00b10930) · [`00b1092c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10920.md#insn-00b1092c)
- 新版 [`00b10d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d48.md#insn-00b10d58) · [`00b10d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d48.md#insn-00b10d54)

~~~diff
- 00b10930 ["INT_ADD", "register:40f0:8", ["const:b10930:8", "const:4:8"]]
- 00b10930 ["CALL", null, ["callee:00442930:8"]]
+ 00b10d58 ["INT_ADD", "register:40f0:8", ["const:b10d58:8", "const:4:8"]]
+ 00b10d58 ["CALL", null, ["callee:00442930:8"]]
- 00b10930 bytes f0c7e497
+ 00b10d58 bytes f6c6e497
- 00b1092c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b1092c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b1092c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b1092c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b10d54 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b10d54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b10d54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b10d54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b1092c bytes 00303c91
+ 00b10d54 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ba29aca5470d88d3db2324332ac0139"></a>

### [`00b10934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10934.md) → [`00b10d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d5c.md) _INIT_257

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 68.36% / 新版 68.36%

CFGの説明率　旧版 87.50% / 新版 93.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 29件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b10964"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1098c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b109b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b10964",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b10970",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b1098c",
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
      "00b10d8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b10d98",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b10db4",
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

- 旧版 [`00b10964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10934.md#insn-00b10964) · [`00b1098c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10934.md#insn-00b1098c) · [`00b109b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10934.md#insn-00b109b0)

~~~diff
- 00b10964 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b10964 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b10964 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b10964 bytes a9831ff8
- 00b1098c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00b1098c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b1098c bytes e013813c
- 00b109b0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00b109b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b109b0 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf99a2fe80e3c18acd2ad5bf1e240b76"></a>

### [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md) → [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md) FUN_00b110ec

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 147件 [`0046d0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) [`0047aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md) [`00489184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md) · 呼出先 20件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00470e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470e14.md) [`004716e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004716e4.md) [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) [`004813f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md)
- 新版 呼出元 147件 [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) [`004891c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md) · 呼出先 20件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00470e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470e54.md) [`00471724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471724.md) [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) [`00481430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481430.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.53% / 新版 95.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b11270",
      "incomplete_value": true,
      "site": "00b11270",
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
                "const:5dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b10e48",
      "incomplete_value": true,
      "site": "00b10e48",
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
                "const:500:8"
              ]
            ]
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
      "definition_site": "00b11420",
      "incomplete_value": false,
      "site": "00b11424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b10ff8",
      "incomplete_value": false,
      "site": "00b10ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b11458",
      "incomplete_value": true,
      "site": "00b11458",
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
                "const:5dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b11030",
      "incomplete_value": true,
      "site": "00b11030",
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b11130",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e14"
      ]
    ],
    [
      "00b111cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e14"
      ]
    ],
    [
      "00b11250",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "00b11130",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e54"
      ]
    ],
    [
      "00b111cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e54"
      ]
    ],
    [
      "00b11250",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b10d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md#insn-00b10d08) · [`00b10da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md#insn-00b10da4) · [`00b10e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md#insn-00b10e28)
- 新版 [`00b11130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md#insn-00b11130) · [`00b111cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md#insn-00b111cc) · [`00b11250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md#insn-00b11250)

~~~diff
- 00b10d08 ["INT_ADD", "register:40f0:8", ["const:b10d08:8", "const:4:8"]]
- 00b10d08 ["CALL", null, ["ram:470e14:8"]]
+ 00b11130 ["INT_ADD", "register:40f0:8", ["const:b11130:8", "const:4:8"]]
+ 00b11130 ["CALL", null, ["ram:470e54:8"]]
- 00b10d08 bytes 4380e597
+ 00b11130 bytes 497fe597
- 00b10da4 ["INT_ADD", "register:40f0:8", ["const:b10da4:8", "const:4:8"]]
- 00b10da4 ["CALL", null, ["ram:470e14:8"]]
+ 00b111cc ["INT_ADD", "register:40f0:8", ["const:b111cc:8", "const:4:8"]]
+ 00b111cc ["CALL", null, ["ram:470e54:8"]]
- 00b10da4 bytes 1c80e597
+ 00b111cc bytes 227fe597
- 00b10e28 ["INT_ADD", "register:40f0:8", ["const:b10e28:8", "const:4:8"]]
- 00b10e28 ["CALL", null, ["ram:48ccb8:8"]]
+ 00b11250 ["INT_ADD", "register:40f0:8", ["const:b11250:8", "const:4:8"]]
+ 00b11250 ["CALL", null, ["ram:48ccf8:8"]]
- 00b10e28 bytes a4efe597
+ 00b11250 bytes aaeee597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee11b7a105b1c443d6d4c176c6021724"></a>

### [`00b11460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b11460.md) → [`00b11888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11888.md) _INIT_258

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00b118c4",
      "incomplete_value": true,
      "site": "00b118e0",
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
      "definition_site": "00b1149c",
      "incomplete_value": true,
      "site": "00b114b8",
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
      "definition_site": "00b118e8",
      "incomplete_value": true,
      "site": "00b11904",
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
      "definition_site": "00b114c0",
      "incomplete_value": true,
      "site": "00b114dc",
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
      "definition_site": "00b11908",
      "incomplete_value": true,
      "site": "00b11924",
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
      "definition_site": "00b114e0",
      "incomplete_value": true,
      "site": "00b114fc",
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
      "00b118c4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00b118e8",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00b11908",
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
      "00b118c4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b118e8",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b11908",
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

- 旧版 [`00b115c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b11460.md#insn-00b115c0) · [`00b11694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b11460.md#insn-00b11694) · [`00b1148c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b11460.md#insn-00b1148c)
- 新版 [`00b119e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11888.md#insn-00b119e8) · [`00b11abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11888.md#insn-00b11abc) · [`00b118b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11888.md#insn-00b118b4)

~~~diff
- 00b115c0 ["INT_ADD", "register:40f0:8", ["const:b115c0:8", "const:4:8"]]
- 00b115c0 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00b119e8 ["INT_ADD", "register:40f0:8", ["const:b119e8:8", "const:4:8"]]
+ 00b119e8 ["CALL", null, ["callee:0043b7f8:8"]]
- 00b115c0 bytes 7ea8e497
+ 00b119e8 bytes 84a7e497
- 00b11694 ["INT_ADD", "register:40f0:8", ["const:b11694:8", "const:4:8"]]
- 00b11694 ["CALL", null, ["callee:00c57e30:8"]]
+ 00b11abc ["INT_ADD", "register:40f0:8", ["const:b11abc:8", "const:4:8"]]
+ 00b11abc ["CALL", null, ["callee:00c57e30:8"]]
- 00b11694 bytes e7180594
+ 00b11abc bytes dd180594
- 00b1148c ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00b1148c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00b1148c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00b1148c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00b118b4 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 00b118b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00b118b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00b118b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00b1148c bytes 73e22791
+ 00b118b4 bytes 73e23791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db663a320200db3f760dac0c21ea5bf1"></a>

### [`00b11858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b11858.md) → [`00b11c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11c80.md) FUN_00b11c80

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005ba758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md) · 呼出先 7件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00470e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470e14.md) [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) [`00a359a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a359a0.md)
- 新版 呼出元 1件 [`005ba798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba798.md) · 呼出先 7件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00470e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470e54.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00a35b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35b98.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

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
      "site": "00b11cf8",
      "value": [
        "leaf",
        "ram:470e54:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b118d0",
      "value": [
        "leaf",
        "ram:470e14:8"
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
      "00b11cd0",
      "READ",
      [
        "storage",
        "00c9b210",
        null,
        "pointer"
      ]
    ],
    [
      "00b11cf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e14"
      ]
    ],
    [
      "00b11cfc",
      "PARAM",
      [
        "storage",
        "011214d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b11cd0",
      "READ",
      [
        "storage",
        "00c9b610",
        null,
        "pointer"
      ]
    ],
    [
      "00b11cf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e54"
      ]
    ],
    [
      "00b11cfc",
      "PARAM",
      [
        "storage",
        "011218d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b118d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b11858.md#insn-00b118d0) · [`00b11878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b11858.md#insn-00b11878) · [`00b1187c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b11858.md#insn-00b1187c)
- 新版 [`00b11cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11c80.md#insn-00b11cf8) · [`00b11ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11c80.md#insn-00b11ca0) · [`00b11ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11c80.md#insn-00b11ca4)

~~~diff
- 00b118d0 ["INT_ADD", "register:40f0:8", ["const:b118d0:8", "const:4:8"]]
- 00b118d0 ["CALL", null, ["ram:470e14:8"]]
+ 00b11cf8 ["INT_ADD", "register:40f0:8", ["const:b11cf8:8", "const:4:8"]]
+ 00b11cf8 ["CALL", null, ["ram:470e54:8"]]
- 00b118d0 bytes 517de597
+ 00b11cf8 bytes 577ce597
- 00b11878 ["INT_ADD", "register:40f0:8", ["const:b11878:8", "const:4:8"]]
- 00b11878 ["CALL", null, ["callee:00a380fc:8"]]
+ 00b11ca0 ["INT_ADD", "register:40f0:8", ["const:b11ca0:8", "const:4:8"]]
+ 00b11ca0 ["CALL", null, ["callee:00a380fc:8"]]
- 00b11878 bytes a399fc97
+ 00b11ca0 bytes 1799fc97
- 00b1187c ["INT_ADD", "register:40f0:8", ["const:b1187c:8", "const:4:8"]]
- 00b1187c ["CALL", null, ["callee:00a35b98:8"]]
+ 00b11ca4 ["INT_ADD", "register:40f0:8", ["const:b11ca4:8", "const:4:8"]]
+ 00b11ca4 ["CALL", null, ["callee:00a35b98:8"]]
- 00b1187c bytes 4990fc97
+ 00b11ca4 bytes bd8ffc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df7bdfea767c90c98b39b5121bd809e1"></a>

### [`00b12c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12c08.md) → [`00b13030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b13030.md) FUN_00b13030

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1195c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b1195c.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)
- 新版 呼出元 1件 [`00b11d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11d84.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.87% / 新版 89.87%

CFGの説明率　旧版 92.11% / 新版 94.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b13070",
      "incomplete_value": false,
      "site": "00b1307c",
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
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b12c48",
      "incomplete_value": false,
      "site": "00b12c54",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b13090",
      "incomplete_value": true,
      "site": "00b130a8",
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
                "const:4de:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b12c68",
      "incomplete_value": true,
      "site": "00b12c80",
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
                "const:49e:8"
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
      "definition_site": "00b130ac",
      "incomplete_value": true,
      "site": "00b130ac",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b12c84",
      "incomplete_value": true,
      "site": "00b12c84",
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
                "const:e:8"
              ]
            ]
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
      "00b1307c",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00b13090",
      "READ",
      [
        "storage",
        "002b149e",
        null,
        "string"
      ]
    ],
    [
      "00b13098",
      "READ",
      [
        "storage",
        "002b14ac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1307c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00b13090",
      "READ",
      [
        "storage",
        "002b14de",
        null,
        "string"
      ]
    ],
    [
      "00b13098",
      "READ",
      [
        "storage",
        "002b14ec",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b12dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12c08.md#insn-00b12dd8) · [`00b12ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12c08.md#insn-00b12ddc) · [`00b12de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12c08.md#insn-00b12de8)

~~~diff
- 00b12dd8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b12dd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b12dd8 bytes e80f00f9
- 00b12ddc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b12ddc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b12ddc bytes e93300f9
- 00b12de8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b12de8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b12de8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b12de8 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00b12de8 bytes 696a28f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4248d7a96ed6a8f14cc2fd96aff294e"></a>

### [`00b1cef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1c/00b1cef4.md) → [`00b1d31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1d/00b1d31c.md) FUN_00b1d31c

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 13件 [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`0048822c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/0048822c.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 13件 [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`0048826c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/0048826c.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.32% / 新版 69.32%

CFGの説明率　旧版 18.22% / 新版 17.99%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 26件, `unresolved_call_alignment` 31件, `unresolved_store_alignment` 44件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1cf2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1cf40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1cf5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1cf2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1cf30",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487e20"
      ]
    ],
    [
      "unmatched:00b1cf40",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b1d354",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b1d358",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487e20"
      ]
    ],
    [
      "00b1d368",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1cf2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1c/00b1cef4.md#insn-00b1cf2c) · [`00b1cf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1c/00b1cef4.md#insn-00b1cf40) · [`00b1cf5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1c/00b1cef4.md#insn-00b1cf5c)

~~~diff
- 00b1cf2c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b1cf2c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b1cf2c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b1cf2c bytes a8831ff8
- 00b1cf40 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:f0:8"]]
- 00b1cf40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b1cf40 bytes e87b00f9
- 00b1cf5c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:c8:8"]]
- 00b1cf5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b1cf5c bytes e9cb00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2205de1c622724793bd0743f7aea3161"></a>

### [`00b1dc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1d/00b1dc60.md) → [`00b1e088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1e088.md) FUN_00b1e088

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 25件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 25件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 38.06% / 新版 37.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_condition` 1件, `store_value` 1件, `unresolved_branch_alignment` 16件, `unresolved_call_alignment` 13件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 28件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1dc70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1dc70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1dc74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1dc70",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1dc74",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1dc8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x3c8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b1e098",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b1e09c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b1e0b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x3c8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1dc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1d/00b1dc60.md#insn-00b1dc70) · [`00b1dc74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1d/00b1dc60.md#insn-00b1dc74) · [`00b1dc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1d/00b1dc60.md#insn-00b1dc8c)

~~~diff
- 00b1dc70 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b1dc70 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b1dc70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b1dc70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1dc70 bytes f65704a9
- 00b1dc74 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b1dc74 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b1dc74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b1dc74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1dc74 bytes f44f05a9
- 00b1dc8c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b1dc8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b1dc8c bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fed480380fcecec438239b65e3f96a11"></a>

### [`00b1ea5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1e/00b1ea5c.md) → [`00b1ee84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ee84.md) FUN_00b1ee84

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00b1dc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1d/00b1dc60.md) · 呼出先 3件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b1e088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1e088.md) · 呼出先 3件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 85.00% / 新版 89.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1ea84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1e/00b1ea5c.md#insn-00b1ea84) · [`00b1ea90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1e/00b1ea5c.md#insn-00b1ea90) · [`00b1eab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1e/00b1ea5c.md#insn-00b1eab4)
- 新版 [`00b1eeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ee84.md#insn-00b1eeac) · [`00b1eeb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ee84.md#insn-00b1eeb8) · [`00b1eedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ee84.md#insn-00b1eedc)

~~~diff
- 00b1ea84 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b1ea84 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b1ea84 ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
+ 00b1eeac ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b1eeac ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00b1eeac ["CBRANCH", null, ["local:b14:8", "tmp:1:1"]]
- 00b1ea84 bytes a9060054
+ 00b1eeac bytes a9060054
- 00b1ea90 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 00b1eeb8 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00b1ea90 bytes a0040054
+ 00b1eeb8 bytes a0040054
- 00b1eab4 ["CBRANCH", null, ["local:b14:8", "register:102:1"]]
+ 00b1eedc ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
- 00b1eab4 bytes c2040054
+ 00b1eedc bytes c2040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf77d92ab648558140f927d020d9c77a"></a>

### [`00b1eb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1e/00b1eb70.md) → [`00b1ef98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ef98.md) FUN_00b1ef98

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005ba758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md) · 呼出先 14件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f74c.md) [`0056081c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056081c.md) [`00597e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e7c.md) [`00880cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md)
- 新版 呼出元 1件 [`005ba798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba798.md) · 呼出先 14件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f78c.md) [`0056085c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056085c.md) [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.57% / 新版 80.57%

CFGの説明率　旧版 57.38% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1ebec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1ec3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1ec40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1efe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b1ebcc"
      ]
    ],
    [
      "unmatched:00b1ebd8",
      "READ",
      [
        "storage",
        "002aff9a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b1ebec",
      "WRITE",
      [
        "storage",
        "Stack[-0x7f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b1efe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1eff4"
      ]
    ],
    [
      "00b1f000",
      "READ",
      [
        "storage",
        "002affda",
        null,
        "string"
      ]
    ],
    [
      "00b1f014",
      "WRITE",
      [
        "storage",
        "Stack[-0x7f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1ebec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1e/00b1eb70.md#insn-00b1ebec) · [`00b1ec3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1e/00b1eb70.md#insn-00b1ec3c) · [`00b1ec40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1e/00b1eb70.md#insn-00b1ec40)

~~~diff
- 00b1ebec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00b1ebec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b1ebec bytes e013833c
- 00b1ec3c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b1ec3c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:30:8"]]
- 00b1ec3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b1ec3c bytes e8c30039
- 00b1ec40 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b1ec40 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:31:8"]]
- 00b1ec40 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b1ec40 bytes ea1303f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f2f78dbe98156cdbcd77affa2f3fa02"></a>

### [`00b296ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b296ec.md) → [`00b29b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29b14.md) FUN_00b29b14

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b2989c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b2989c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b29cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cc4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 80.56% / 新版 80.56%

CFGの説明率　旧版 64.71% / 新版 55.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b29728"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b29b50"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b29c58",
      "incomplete_value": true,
      "site": "00b29c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_MULT",
            "8",
            [
              [
                "live",
                "register:40b0:8"
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
    "old": {
      "definition_site": "00b29830",
      "incomplete_value": true,
      "site": "00b2983c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_MULT",
            "8",
            [
              [
                "live",
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:320:8"
              ]
            ]
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
      "unmatched:00b29728",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b29bd4"
      ]
    ]
  ],
  "added": [
    [
      "00b29b50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b29bd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b29728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b296ec.md#insn-00b29728) · [`00b2983c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b296ec.md#insn-00b2983c)
- 新版 [`00b29c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29b14.md#insn-00b29c64) · [`00b29b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29b14.md#insn-00b29b50)

~~~diff
- 00b29728 ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
- 00b29728 bytes 22040054
- 00b2983c ["INT_ADD", "register:40f0:8", ["const:b2983c:8", "const:4:8"]]
- 00b2983c ["CALL", null, ["callee:00c58090:8"]]
+ 00b29c64 ["INT_ADD", "register:40f0:8", ["const:b29c64:8", "const:4:8"]]
+ 00b29c64 ["CALL", null, ["callee:00c58090:8"]]
- 00b2983c bytes 15b90494
+ 00b29c64 bytes 0bb90494
+ 00b29b50 ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
+ 00b29b50 bytes 22040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c243165491b742752dce1df42fb744d5"></a>

### [`00b2989c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b2989c.md) → [`00b29cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cc4.md) FUN_00b29cc4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b296ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b296ec.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00b29b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29b14.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b29cd0",
      "incomplete_value": false,
      "site": "00b29cd4",
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
      "definition_site": "00b298a8",
      "incomplete_value": false,
      "site": "00b298ac",
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
      "00b29cd0",
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
      "00b29cd0",
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

- 旧版 [`00b298ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b2989c.md#insn-00b298ac) · [`00b298a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b2989c.md#insn-00b298a8)
- 新版 [`00b29cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cc4.md#insn-00b29cd4) · [`00b29cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cc4.md#insn-00b29cd0)

~~~diff
- 00b298ac ["INT_ADD", "register:40f0:8", ["const:b298ac:8", "const:4:8"]]
- 00b298ac ["CALL", null, ["callee:0043b778:8"]]
+ 00b29cd4 ["INT_ADD", "register:40f0:8", ["const:b29cd4:8", "const:4:8"]]
+ 00b29cd4 ["CALL", null, ["callee:0043b778:8"]]
- 00b298ac bytes a347e497
+ 00b29cd4 bytes a946e497
- 00b298a8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b298a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b298a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b298a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b29cd0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b29cd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b29cd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b29cd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b298a8 bytes 00303c91
+ 00b29cd0 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5758fe4a76ac541093ef98ff049dcf30"></a>

### [`00b298b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b298b0.md) → [`00b29cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cd8.md) FUN_00b29cd8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b29a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29a44.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b29e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.08% / 新版 92.08%

CFGの説明率　旧版 40.00% / 新版 47.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2993c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b29d64"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b29df4",
      "incomplete_value": true,
      "site": "00b29e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_MULT",
            "8",
            [
              [
                "live",
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b299cc",
      "incomplete_value": true,
      "site": "00b299dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_MULT",
            "8",
            [
              [
                "live",
                "register:40b0:8"
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
    "ordinal": 2,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b2993c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b298b0.md#insn-00b2993c) · [`00b299dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b298b0.md#insn-00b299dc) · [`00b29a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b298b0.md#insn-00b29a3c)
- 新版 [`00b29e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cd8.md#insn-00b29e04) · [`00b29e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cd8.md#insn-00b29e64)

~~~diff
- 00b2993c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b2993c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b2993c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b2993c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b2993c bytes 5831899a
- 00b299dc ["INT_ADD", "register:40f0:8", ["const:b299dc:8", "const:4:8"]]
- 00b299dc ["CALL", null, ["callee:00c58090:8"]]
+ 00b29e04 ["INT_ADD", "register:40f0:8", ["const:b29e04:8", "const:4:8"]]
+ 00b29e04 ["CALL", null, ["callee:00c58090:8"]]
- 00b299dc bytes adb80494
+ 00b29e04 bytes a3b80494
- 00b29a3c ["INT_ADD", "register:40f0:8", ["const:b29a3c:8", "const:4:8"]]
- 00b29a3c ["CALL", null, ["callee:00b29e6c:8"]]
+ 00b29e64 ["INT_ADD", "register:40f0:8", ["const:b29e64:8", "const:4:8"]]
+ 00b29e64 ["CALL", null, ["callee:00b29e6c:8"]]
- 00b29a3c bytes 02000094
+ 00b29e64 bytes 02000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ef20d3ccf201dc2aa212d43efa1df9a"></a>

### [`00b29a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29a44.md) → [`00b29e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e6c.md) FUN_00b29e6c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b298b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b298b0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00b29cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cd8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b29e78",
      "incomplete_value": false,
      "site": "00b29e7c",
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
      "definition_site": "00b29a50",
      "incomplete_value": false,
      "site": "00b29a54",
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
      "00b29e78",
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
      "00b29e78",
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

- 旧版 [`00b29a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29a44.md#insn-00b29a54) · [`00b29a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29a44.md#insn-00b29a50)
- 新版 [`00b29e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e6c.md#insn-00b29e7c) · [`00b29e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e6c.md#insn-00b29e78)

~~~diff
- 00b29a54 ["INT_ADD", "register:40f0:8", ["const:b29a54:8", "const:4:8"]]
- 00b29a54 ["CALL", null, ["callee:0043b778:8"]]
+ 00b29e7c ["INT_ADD", "register:40f0:8", ["const:b29e7c:8", "const:4:8"]]
+ 00b29e7c ["CALL", null, ["callee:0043b778:8"]]
- 00b29a54 bytes 3947e497
+ 00b29e7c bytes 3f46e497
- 00b29a50 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b29a50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b29a50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b29a50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b29e78 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b29e78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b29e78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b29e78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b29a50 bytes 00303c91
+ 00b29e78 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c951229e937e57baa7e8a4f42149b64"></a>

### [`00b29be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29be8.md) → [`00b2a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a010.md) FUN_00b2a010

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b29a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29a58.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00b29e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e80.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b2a01c",
      "incomplete_value": false,
      "site": "00b2a020",
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
      "definition_site": "00b29bf4",
      "incomplete_value": false,
      "site": "00b29bf8",
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
      "00b2a01c",
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
      "00b2a01c",
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

- 旧版 [`00b29bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29be8.md#insn-00b29bf8) · [`00b29bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29be8.md#insn-00b29bf4)
- 新版 [`00b2a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a010.md#insn-00b2a020) · [`00b2a01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a010.md#insn-00b2a01c)

~~~diff
- 00b29bf8 ["INT_ADD", "register:40f0:8", ["const:b29bf8:8", "const:4:8"]]
- 00b29bf8 ["CALL", null, ["callee:0043b778:8"]]
+ 00b2a020 ["INT_ADD", "register:40f0:8", ["const:b2a020:8", "const:4:8"]]
+ 00b2a020 ["CALL", null, ["callee:0043b778:8"]]
- 00b29bf8 bytes d046e497
+ 00b2a020 bytes d645e497
- 00b29bf4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b29bf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b29bf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b29bf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a01c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b2a01c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a01c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a01c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b29bf4 bytes 00303c91
+ 00b2a01c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d66d95d4e83498e5da6407c5d6c8032"></a>

### [`00b29d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d28.md) → [`00b2a150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a150.md) FUN_00b2a150

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b29bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29bfc.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00b2a024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a024.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b2a15c",
      "incomplete_value": false,
      "site": "00b2a160",
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
      "definition_site": "00b29d34",
      "incomplete_value": false,
      "site": "00b29d38",
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
      "00b2a15c",
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
      "00b2a15c",
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

- 旧版 [`00b29d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d28.md#insn-00b29d38) · [`00b29d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d28.md#insn-00b29d34)
- 新版 [`00b2a160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a150.md#insn-00b2a160) · [`00b2a15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a150.md#insn-00b2a15c)

~~~diff
- 00b29d38 ["INT_ADD", "register:40f0:8", ["const:b29d38:8", "const:4:8"]]
- 00b29d38 ["CALL", null, ["callee:0043b778:8"]]
+ 00b2a160 ["INT_ADD", "register:40f0:8", ["const:b2a160:8", "const:4:8"]]
+ 00b2a160 ["CALL", null, ["callee:0043b778:8"]]
- 00b29d38 bytes 8046e497
+ 00b2a160 bytes 8645e497
- 00b29d34 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b29d34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b29d34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b29d34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a15c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b2a15c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a15c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a15c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b29d34 bytes 00303c91
+ 00b2a15c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-781aa0437e82e7867256e157371e5194"></a>

### [`00b29ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ed0.md) → [`00b2a2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a2f8.md) FUN_00b2a2f8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b29d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d3c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00b2a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a164.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b2a304",
      "incomplete_value": false,
      "site": "00b2a308",
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
      "definition_site": "00b29edc",
      "incomplete_value": false,
      "site": "00b29ee0",
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
      "00b2a304",
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
      "00b2a304",
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

- 旧版 [`00b29ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ed0.md#insn-00b29ee0) · [`00b29edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ed0.md#insn-00b29edc)
- 新版 [`00b2a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a2f8.md#insn-00b2a308) · [`00b2a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a2f8.md#insn-00b2a304)

~~~diff
- 00b29ee0 ["INT_ADD", "register:40f0:8", ["const:b29ee0:8", "const:4:8"]]
- 00b29ee0 ["CALL", null, ["callee:0043b778:8"]]
+ 00b2a308 ["INT_ADD", "register:40f0:8", ["const:b2a308:8", "const:4:8"]]
+ 00b2a308 ["CALL", null, ["callee:0043b778:8"]]
- 00b29ee0 bytes 1646e497
+ 00b2a308 bytes 1c45e497
- 00b29edc ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b29edc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b29edc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b29edc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a304 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b2a304 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a304 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a304 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b29edc bytes 00303c91
+ 00b2a304 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3d7a11712f63550eac602ea9a76eb1f"></a>

### [`00b2a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a074.md) → [`00b2a49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a49c.md) FUN_00b2a49c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b29ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ee4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00b2a30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a30c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b2a4a8",
      "incomplete_value": false,
      "site": "00b2a4ac",
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
      "definition_site": "00b2a080",
      "incomplete_value": false,
      "site": "00b2a084",
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
      "00b2a4a8",
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
      "00b2a4a8",
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

- 旧版 [`00b2a084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a074.md#insn-00b2a084) · [`00b2a080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a074.md#insn-00b2a080)
- 新版 [`00b2a4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a49c.md#insn-00b2a4ac) · [`00b2a4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a49c.md#insn-00b2a4a8)

~~~diff
- 00b2a084 ["INT_ADD", "register:40f0:8", ["const:b2a084:8", "const:4:8"]]
- 00b2a084 ["CALL", null, ["callee:0043b778:8"]]
+ 00b2a4ac ["INT_ADD", "register:40f0:8", ["const:b2a4ac:8", "const:4:8"]]
+ 00b2a4ac ["CALL", null, ["callee:0043b778:8"]]
- 00b2a084 bytes ad45e497
+ 00b2a4ac bytes b344e497
- 00b2a080 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b2a080 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a080 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a080 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a4a8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b2a4a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a4a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a4a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2a080 bytes 00303c91
+ 00b2a4a8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3cfba67a1fc06f0f49bc7acce64b690"></a>

### [`00b2a088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a088.md) → [`00b2a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a4b0.md) FUN_00b2a4b0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b2a4bc",
      "incomplete_value": false,
      "site": "00b2a4c0",
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
      "definition_site": "00b2a094",
      "incomplete_value": false,
      "site": "00b2a098",
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
      "00b2a4bc",
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
      "00b2a4bc",
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

- 旧版 [`00b2a098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a088.md#insn-00b2a098) · [`00b2a094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a088.md#insn-00b2a094)
- 新版 [`00b2a4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a4b0.md#insn-00b2a4c0) · [`00b2a4bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a4b0.md#insn-00b2a4bc)

~~~diff
- 00b2a098 ["INT_ADD", "register:40f0:8", ["const:b2a098:8", "const:4:8"]]
- 00b2a098 ["CALL", null, ["callee:0043b778:8"]]
+ 00b2a4c0 ["INT_ADD", "register:40f0:8", ["const:b2a4c0:8", "const:4:8"]]
+ 00b2a4c0 ["CALL", null, ["callee:0043b778:8"]]
- 00b2a098 bytes a845e497
+ 00b2a4c0 bytes ae44e497
- 00b2a094 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b2a094 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a094 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a094 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a4bc ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b2a4bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a4bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a4bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2a094 bytes 00303c91
+ 00b2a4bc bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cba9476f1707189960e8362c074f40d"></a>

### [`00b2a1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a1c8.md) → [`00b2a5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a5f0.md) FUN_00b2a5f0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2a09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a09c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00b2a4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a4c4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b2a5fc",
      "incomplete_value": false,
      "site": "00b2a600",
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
      "definition_site": "00b2a1d4",
      "incomplete_value": false,
      "site": "00b2a1d8",
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
      "00b2a5fc",
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
      "00b2a5fc",
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

- 旧版 [`00b2a1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a1c8.md#insn-00b2a1d8) · [`00b2a1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a1c8.md#insn-00b2a1d4)
- 新版 [`00b2a600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a5f0.md#insn-00b2a600) · [`00b2a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a5f0.md#insn-00b2a5fc)

~~~diff
- 00b2a1d8 ["INT_ADD", "register:40f0:8", ["const:b2a1d8:8", "const:4:8"]]
- 00b2a1d8 ["CALL", null, ["callee:0043b778:8"]]
+ 00b2a600 ["INT_ADD", "register:40f0:8", ["const:b2a600:8", "const:4:8"]]
+ 00b2a600 ["CALL", null, ["callee:0043b778:8"]]
- 00b2a1d8 bytes 5845e497
+ 00b2a600 bytes 5e44e497
- 00b2a1d4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b2a1d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a1d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a1d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a5fc ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b2a5fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a5fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a5fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2a1d4 bytes 00303c91
+ 00b2a5fc bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-298e976caf19c9d54f90ab5fcfeef52a"></a>

### [`00b2a1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a1dc.md) → [`00b2a604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a604.md) FUN_00b2a604

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b2a394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a394.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2a7bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a7bc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 70.59% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b2a388",
      "incomplete_value": true,
      "site": "00b2a38c",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b2a38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a1dc.md#insn-00b2a38c) · [`00b2a244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a1dc.md#insn-00b2a244) · [`00b2a280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a1dc.md#insn-00b2a280)
- 新版 [`00b2a7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a604.md#insn-00b2a7b4) · [`00b2a66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a604.md#insn-00b2a66c) · [`00b2a6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a604.md#insn-00b2a6a8)

~~~diff
- 00b2a38c ["INT_ADD", "register:40f0:8", ["const:b2a38c:8", "const:4:8"]]
- 00b2a38c ["CALL", null, ["callee:00b2a7bc:8"]]
+ 00b2a7b4 ["INT_ADD", "register:40f0:8", ["const:b2a7b4:8", "const:4:8"]]
+ 00b2a7b4 ["CALL", null, ["callee:00b2a7bc:8"]]
- 00b2a38c bytes 02000094
+ 00b2a7b4 bytes 02000094
- 00b2a244 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b2a244 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b2a244 ["CBRANCH", null, ["local:b12:8", "tmp:1:1"]]
+ 00b2a66c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b2a66c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b2a66c ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
- 00b2a244 bytes 280a0054
+ 00b2a66c bytes 280a0054
- 00b2a280 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b2a280 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b2a280 ["CBRANCH", null, ["local:b13:8", "tmp:1:1"]]
+ 00b2a6a8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b2a6a8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b2a6a8 ["CBRANCH", null, ["local:b17:8", "tmp:1:1"]]
- 00b2a280 bytes 88080054
+ 00b2a6a8 bytes 88080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98b8a1ed680d680f708a5d722338c9eb"></a>

### [`00b2a394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a394.md) → [`00b2a7bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a7bc.md) FUN_00b2a7bc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2a1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a1dc.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00b2a604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a604.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b2a7c8",
      "incomplete_value": false,
      "site": "00b2a7cc",
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
      "definition_site": "00b2a3a0",
      "incomplete_value": false,
      "site": "00b2a3a4",
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
      "00b2a7c8",
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
      "00b2a7c8",
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

- 旧版 [`00b2a3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a394.md#insn-00b2a3a4) · [`00b2a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a394.md#insn-00b2a3a0)
- 新版 [`00b2a7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a7bc.md#insn-00b2a7cc) · [`00b2a7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a7bc.md#insn-00b2a7c8)

~~~diff
- 00b2a3a4 ["INT_ADD", "register:40f0:8", ["const:b2a3a4:8", "const:4:8"]]
- 00b2a3a4 ["CALL", null, ["callee:0043b778:8"]]
+ 00b2a7cc ["INT_ADD", "register:40f0:8", ["const:b2a7cc:8", "const:4:8"]]
+ 00b2a7cc ["CALL", null, ["callee:0043b778:8"]]
- 00b2a3a4 bytes e544e497
+ 00b2a7cc bytes eb43e497
- 00b2a3a0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b2a3a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a3a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a3a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a7c8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b2a7c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a7c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a7c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2a3a0 bytes 00303c91
+ 00b2a7c8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba8cd076be5778f78186026c5d2a8e8c"></a>

### [`00b2a414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a414.md) → [`00b2a83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a83c.md) FUN_00b2a83c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b2a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a688.md) [`00b2a69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a69c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2aab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aab0.md) [`00b2aac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aac4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.15% / 新版 98.15%

CFGの説明率　旧版 66.67% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2a5a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b2a9c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2a9cc",
      "incomplete_value": true,
      "site": "00b2a9d0",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
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
      "unmatched:00b2a5a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2aa0c"
      ]
    ]
  ],
  "added": [
    [
      "00b2a9c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2aa0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2a5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a414.md#insn-00b2a5a0) · [`00b2a5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a414.md#insn-00b2a5a8)
- 新版 [`00b2a9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a83c.md#insn-00b2a9d0) · [`00b2a9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a83c.md#insn-00b2a9c8)

~~~diff
- 00b2a5a0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b2a5a0 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00b2a5a0 bytes 21020054
- 00b2a5a8 ["INT_ADD", "register:40f0:8", ["const:b2a5a8:8", "const:4:8"]]
- 00b2a5a8 ["CALL", null, ["callee:00b2aab0:8"]]
+ 00b2a9d0 ["INT_ADD", "register:40f0:8", ["const:b2a9d0:8", "const:4:8"]]
+ 00b2a9d0 ["CALL", null, ["callee:00b2aab0:8"]]
- 00b2a5a8 bytes 38000094
+ 00b2a9d0 bytes 38000094
+ 00b2a9c8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b2a9c8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00b2a9c8 bytes 21020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af132d7391619638f92eb8282967b033"></a>

### [`00b2a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a688.md) → [`00b2aab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aab0.md) FUN_00b2aab0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2a414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a414.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00b2a83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a83c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b2aabc",
      "incomplete_value": false,
      "site": "00b2aac0",
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
      "definition_site": "00b2a694",
      "incomplete_value": false,
      "site": "00b2a698",
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
      "00b2aabc",
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
      "00b2aabc",
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

- 旧版 [`00b2a698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a688.md#insn-00b2a698) · [`00b2a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a688.md#insn-00b2a694)
- 新版 [`00b2aac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aab0.md#insn-00b2aac0) · [`00b2aabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aab0.md#insn-00b2aabc)

~~~diff
- 00b2a698 ["INT_ADD", "register:40f0:8", ["const:b2a698:8", "const:4:8"]]
- 00b2a698 ["CALL", null, ["callee:0043b778:8"]]
+ 00b2aac0 ["INT_ADD", "register:40f0:8", ["const:b2aac0:8", "const:4:8"]]
+ 00b2aac0 ["CALL", null, ["callee:0043b778:8"]]
- 00b2a698 bytes 2844e497
+ 00b2aac0 bytes 2e43e497
- 00b2a694 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b2a694 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a694 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a694 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2aabc ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b2aabc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2aabc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2aabc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2a694 bytes 00303c91
+ 00b2aabc bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77336ccc6fd93de4a62c1bfbc0b4bfe7"></a>

### [`00b2a790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a790.md) → [`00b2abb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abb8.md) FUN_00b2abb8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b2abc4",
      "incomplete_value": false,
      "site": "00b2abc8",
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
      "definition_site": "00b2a79c",
      "incomplete_value": false,
      "site": "00b2a7a0",
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
      "00b2abc4",
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
      "00b2abc4",
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

- 旧版 [`00b2a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a790.md#insn-00b2a7a0) · [`00b2a79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a790.md#insn-00b2a79c)
- 新版 [`00b2abc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abb8.md#insn-00b2abc8) · [`00b2abc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abb8.md#insn-00b2abc4)

~~~diff
- 00b2a7a0 ["INT_ADD", "register:40f0:8", ["const:b2a7a0:8", "const:4:8"]]
- 00b2a7a0 ["CALL", null, ["callee:0043b778:8"]]
+ 00b2abc8 ["INT_ADD", "register:40f0:8", ["const:b2abc8:8", "const:4:8"]]
+ 00b2abc8 ["CALL", null, ["callee:0043b778:8"]]
- 00b2a7a0 bytes e643e497
+ 00b2abc8 bytes ec42e497
- 00b2a79c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b2a79c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a79c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a79c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2abc4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b2abc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2abc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2abc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2a79c bytes 00303c91
+ 00b2abc4 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d473e73323f93c8001817478472ba147"></a>

### [`00b2b0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b0a4.md) → [`00b2b4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b4cc.md) FUN_00b2b4cc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2ac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ac48.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00b2b070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b070.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b2b4d8",
      "incomplete_value": false,
      "site": "00b2b4dc",
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
      "definition_site": "00b2b0b0",
      "incomplete_value": false,
      "site": "00b2b0b4",
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
      "00b2b4d8",
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
      "00b2b4d8",
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

- 旧版 [`00b2b0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b0a4.md#insn-00b2b0b4) · [`00b2b0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b0a4.md#insn-00b2b0b0)
- 新版 [`00b2b4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b4cc.md#insn-00b2b4dc) · [`00b2b4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b4cc.md#insn-00b2b4d8)

~~~diff
- 00b2b0b4 ["INT_ADD", "register:40f0:8", ["const:b2b0b4:8", "const:4:8"]]
- 00b2b0b4 ["CALL", null, ["callee:0043b778:8"]]
+ 00b2b4dc ["INT_ADD", "register:40f0:8", ["const:b2b4dc:8", "const:4:8"]]
+ 00b2b4dc ["CALL", null, ["callee:0043b778:8"]]
- 00b2b0b4 bytes a141e497
+ 00b2b4dc bytes a740e497
- 00b2b0b0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b2b0b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2b0b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2b0b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2b4d8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b2b4d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2b4d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2b4d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2b0b0 bytes 00303c91
+ 00b2b4d8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab2e5cb4bc41e60ee46aa27fa36aff75"></a>

### [`00b2b0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b0b8.md) → [`00b2b4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b4e0.md) _INIT_259

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.48% / 新版 50.48%

CFGの説明率　旧版 90.32% / 新版 93.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 8件, `store_value` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 39件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2b0e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2b0fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2b100"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2b0e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2b0f4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b2b0fc",
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
      "00b2b510",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b2b51c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b2b524",
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

- 旧版 [`00b2b0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b0b8.md#insn-00b2b0e8) · [`00b2b0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b0b8.md#insn-00b2b0fc) · [`00b2b100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b0b8.md#insn-00b2b100)

~~~diff
- 00b2b0e8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b2b0e8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b2b0e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b2b0e8 bytes a9831ff8
- 00b2b0fc ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b2b0fc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00b2b0fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b2b0fc bytes ea130278
- 00b2b100 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b2b100 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b2b100 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb3a546b08a9cb8fc33c5442a9252e24"></a>

### [`00b2b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4cc.md) → [`00b2b8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b8f4.md) FUN_00b2b8f4

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043afbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043afbc.md) · 呼出先 20件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f4e0.md) [`0046ca50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca50.md) [`0046ca7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca7c.md) [`00495240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495240.md)
- 新版 呼出元 1件 [`0043affc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043affc.md) · 呼出先 20件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f520.md) [`0046ca90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca90.md) [`0046cabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cabc.md) [`00495280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495280.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.08% / 新版 91.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2b9a8",
      "incomplete_value": false,
      "site": "00b2b9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2b580",
      "incomplete_value": false,
      "site": "00b2b590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2bad8",
      "incomplete_value": false,
      "site": "00b2bae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2b6b0",
      "incomplete_value": false,
      "site": "00b2b6c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00b2b9d4",
      "incomplete_value": true,
      "site": "00b2b9d4",
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
              "LOAD",
              [
                "leaf",
                "const:e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2b5ac",
      "incomplete_value": true,
      "site": "00b2b5ac",
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
              "LOAD",
              [
                "leaf",
                "const:e8:8"
              ]
            ]
          ]
        ]
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
      "00b2b9ac",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b2b9b8",
      "DATA",
      [
        "storage",
        "00c8eee8",
        null,
        "undefined *"
      ]
    ],
    [
      "00b2b9bc",
      "READ",
      [
        "storage",
        "00ca6110",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b2b9ac",
      "READ",
      [
        "storage",
        "00c9b240",
        null,
        "pointer"
      ]
    ],
    [
      "00b2b9b8",
      "DATA",
      [
        "storage",
        "00c8f2e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00b2b9bc",
      "READ",
      [
        "storage",
        "00ca6510",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2b5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4cc.md#insn-00b2b5ac) · [`00b2b6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4cc.md#insn-00b2b6dc) · [`00b2b4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4cc.md#insn-00b2b4f0)
- 新版 [`00b2b9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b8f4.md#insn-00b2b9d4) · [`00b2bb04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b8f4.md#insn-00b2bb04) · [`00b2b918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b8f4.md#insn-00b2b918)

~~~diff
- 00b2b5ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2b5ac ["INT_ADD", "register:40f0:8", ["const:b2b5ac:8", "const:4:8"]]
- 00b2b5ac ["CALLIND", null, ["register:0:8"]]
+ 00b2b9d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b2b9d4 ["INT_ADD", "register:40f0:8", ["const:b2b9d4:8", "const:4:8"]]
+ 00b2b9d4 ["CALLIND", null, ["register:0:8"]]
- 00b2b5ac bytes 00013fd6
+ 00b2b9d4 bytes 00013fd6
- 00b2b6dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2b6dc ["INT_ADD", "register:40f0:8", ["const:b2b6dc:8", "const:4:8"]]
- 00b2b6dc ["CALLIND", null, ["register:0:8"]]
+ 00b2bb04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b2bb04 ["INT_ADD", "register:40f0:8", ["const:b2bb04:8", "const:4:8"]]
+ 00b2bb04 ["CALLIND", null, ["register:0:8"]]
- 00b2b6dc bytes 00013fd6
+ 00b2bb04 bytes 00013fd6
- 00b2b4f0 ["INT_ADD", "register:40f0:8", ["const:b2b4f0:8", "const:4:8"]]
- 00b2b4f0 ["CALL", null, ["callee:008514f8:8"]]
+ 00b2b918 ["INT_ADD", "register:40f0:8", ["const:b2b918:8", "const:4:8"]]
+ 00b2b918 ["CALL", null, ["callee:008514f8:8"]]
- 00b2b4f0 bytes f297f497
+ 00b2b918 bytes f896f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93777d69bedfe17e34b2be684780a749"></a>

### [`00b2b834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b834.md) → [`00b2bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bc5c.md) FUN_00b2bc5c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b2ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md) · 呼出先 8件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00b2ce48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md) · 呼出先 8件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.42% / 新版 93.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2bca4",
      "incomplete_value": true,
      "site": "00b2bca4",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:f9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2b87c",
      "incomplete_value": true,
      "site": "00b2b87c",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:ebe:8"
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
      "definition_site": "00b2bc9c",
      "incomplete_value": true,
      "site": "00b2bca8",
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
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2b874",
      "incomplete_value": true,
      "site": "00b2b880",
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
                "const:7:8"
              ]
            ]
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
      "00b2bc94",
      "READ",
      [
        "storage",
        "002a5ebe",
        null,
        "string"
      ]
    ],
    [
      "00b2bc9c",
      "READ",
      [
        "storage",
        "002a5ec5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2bc94",
      "READ",
      [
        "storage",
        "002a5f9a",
        null,
        "string"
      ]
    ],
    [
      "00b2bc9c",
      "READ",
      [
        "storage",
        "002a5fa1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2b854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b834.md#insn-00b2b854) · [`00b2b85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b834.md#insn-00b2b85c) · [`00b2b868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b834.md#insn-00b2b868)
- 新版 [`00b2bc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bc5c.md#insn-00b2bc7c) · [`00b2bc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bc5c.md#insn-00b2bc84) · [`00b2bc90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bc5c.md#insn-00b2bc90)

~~~diff
- 00b2b854 ["INT_ADD", "register:40f0:8", ["const:b2b854:8", "const:4:8"]]
- 00b2b854 ["CALL", null, ["callee:00588e6c:8"]]
+ 00b2bc7c ["INT_ADD", "register:40f0:8", ["const:b2bc7c:8", "const:4:8"]]
+ 00b2bc7c ["CALL", null, ["callee:00588e6c:8"]]
- 00b2b854 bytes 7675e997
+ 00b2bc7c bytes 7c74e997
- 00b2b85c ["INT_ADD", "register:40f0:8", ["const:b2b85c:8", "const:4:8"]]
- 00b2b85c ["CALL", null, ["callee:0058915c:8"]]
+ 00b2bc84 ["INT_ADD", "register:40f0:8", ["const:b2bc84:8", "const:4:8"]]
+ 00b2bc84 ["CALL", null, ["callee:0058915c:8"]]
- 00b2b85c bytes 3076e997
+ 00b2bc84 bytes 3675e997
- 00b2b868 ["COPY", "tmp:0:8", ["const:ebe:8"]]
- 00b2b868 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b2b868 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b2b868 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b2bc90 ["COPY", "tmp:0:8", ["const:f9a:8"]]
+ 00b2bc90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b2bc90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b2bc90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b2b868 bytes 29f93a91
+ 00b2bc90 bytes 29693e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b83e649ad834230ed7c451622fd2ecd6"></a>

### [`00b2b9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b9a0.md) → [`00b2bdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bdc8.md) FUN_00b2bdc8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b2ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md) · 呼出先 8件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00b2ce48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md) · 呼出先 8件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2be08",
      "incomplete_value": true,
      "site": "00b2be20",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:f07:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2b9e0",
      "incomplete_value": true,
      "site": "00b2b9f8",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:ec7:8"
              ]
            ]
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
      "00b2be08",
      "READ",
      [
        "storage",
        "002abec7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2be08",
      "READ",
      [
        "storage",
        "002abf07",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2b9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b9a0.md#insn-00b2b9c0) · [`00b2b9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b9a0.md#insn-00b2b9c8) · [`00b2b9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b9a0.md#insn-00b2b9d4)
- 新版 [`00b2bde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bdc8.md#insn-00b2bde8) · [`00b2bdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bdc8.md#insn-00b2bdf0) · [`00b2bdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bdc8.md#insn-00b2bdfc)

~~~diff
- 00b2b9c0 ["INT_ADD", "register:40f0:8", ["const:b2b9c0:8", "const:4:8"]]
- 00b2b9c0 ["CALL", null, ["callee:00588e6c:8"]]
+ 00b2bde8 ["INT_ADD", "register:40f0:8", ["const:b2bde8:8", "const:4:8"]]
+ 00b2bde8 ["CALL", null, ["callee:00588e6c:8"]]
- 00b2b9c0 bytes 1b75e997
+ 00b2bde8 bytes 2174e997
- 00b2b9c8 ["INT_ADD", "register:40f0:8", ["const:b2b9c8:8", "const:4:8"]]
- 00b2b9c8 ["CALL", null, ["callee:0058915c:8"]]
+ 00b2bdf0 ["INT_ADD", "register:40f0:8", ["const:b2bdf0:8", "const:4:8"]]
+ 00b2bdf0 ["CALL", null, ["callee:0058915c:8"]]
- 00b2b9c8 bytes d575e997
+ 00b2bdf0 bytes db74e997
- 00b2b9d4 ["COPY", "tmp:0:8", ["const:ec7:8"]]
- 00b2b9d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b2b9d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b2b9d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b2bdfc ["COPY", "tmp:0:8", ["const:f07:8"]]
+ 00b2bdfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b2bdfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b2bdfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b2b9d4 bytes 291d3b91
+ 00b2bdfc bytes 291d3c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e767a6a0c688eff910096e53cac883df"></a>

### [`00b2bc74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bc74.md) → [`00b2c09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c09c.md) FUN_00b2c09c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md) · 呼出先 8件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00b2ce48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md) · 呼出先 8件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.54% / 新版 90.54%

CFGの説明率　旧版 73.68% / 新版 82.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2c0dc",
      "incomplete_value": true,
      "site": "00b2c0f0",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:8e7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2bcb4",
      "incomplete_value": true,
      "site": "00b2bcc8",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:8a7:8"
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2bd44"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b2c16c"
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
      "00b2c0dc",
      "READ",
      [
        "storage",
        "002b98a7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b2bd44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2c190"
      ]
    ],
    [
      "unmatched:00b2bd3c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b2c0dc",
      "READ",
      [
        "storage",
        "002b98e7",
        null,
        "string"
      ]
    ],
    [
      "00b2c16c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2c190"
      ]
    ],
    [
      "00b2c164",
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

- 旧版 [`00b2bd3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bc74.md#insn-00b2bd3c) · [`00b2bd44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bc74.md#insn-00b2bd44)
- 新版 [`00b2c164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c09c.md#insn-00b2c164)

~~~diff
- 00b2bd3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2bd3c ["INT_ADD", "register:40f0:8", ["const:b2bd3c:8", "const:4:8"]]
- 00b2bd3c ["CALLIND", null, ["register:0:8"]]
- 00b2bd3c bytes 00013fd6
- 00b2bd44 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00b2bd44 bytes 20010054
+ 00b2c164 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b2c164 ["INT_ADD", "register:40f0:8", ["const:b2c164:8", "const:4:8"]]
+ 00b2c164 ["CALLIND", null, ["register:0:8"]]
+ 00b2c164 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96a71e75f131d071cff8a827941950b1"></a>

### [`00b2bdd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bdd8.md) → [`00b2c200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c200.md) FUN_00b2c200

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0043aeec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043aeec.md) · 呼出先 19件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`0046792c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md) [`0046d928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d928.md) [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`0048b350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b350.md)
- 新版 呼出元 1件 [`0043af2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043af2c.md) · 呼出先 19件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`0046796c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046796c.md) [`0046d968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d968.md) [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`0048b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b390.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.50% / 新版 88.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2c24c",
      "incomplete_value": true,
      "site": "00b2c24c",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:e1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2be24",
      "incomplete_value": true,
      "site": "00b2be24",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:ddd:8"
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
      "definition_site": "00b2c2b4",
      "incomplete_value": true,
      "site": "00b2c2b8",
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
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:148:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2be8c",
      "incomplete_value": true,
      "site": "00b2be90",
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
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:108:8"
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
      "definition_site": "00b2c310",
      "incomplete_value": true,
      "site": "00b2c310",
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
                "const:5dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2bee8",
      "incomplete_value": true,
      "site": "00b2bee8",
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b2c238",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "00b2c2b4",
      "READ",
      [
        "storage",
        "002c4108",
        null,
        "undefined8"
      ]
    ],
    [
      "00b2c2c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ],
  "added": [
    [
      "00b2c238",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "00b2c2b4",
      "READ",
      [
        "storage",
        "002c4148",
        null,
        "undefined8"
      ]
    ],
    [
      "00b2c2c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2bea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bdd8.md#insn-00b2bea0) · [`00b2bf50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bdd8.md#insn-00b2bf50) · [`00b2be00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bdd8.md#insn-00b2be00)
- 新版 [`00b2c2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c200.md#insn-00b2c2c8) · [`00b2c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c200.md#insn-00b2c378) · [`00b2c228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c200.md#insn-00b2c228)

~~~diff
- 00b2bea0 ["INT_ADD", "register:40f0:8", ["const:b2bea0:8", "const:4:8"]]
- 00b2bea0 ["CALL", null, ["ram:46dac0:8"]]
+ 00b2c2c8 ["INT_ADD", "register:40f0:8", ["const:b2c2c8:8", "const:4:8"]]
+ 00b2c2c8 ["CALL", null, ["ram:46db00:8"]]
- 00b2bea0 bytes 0807e597
+ 00b2c2c8 bytes 0e06e597
- 00b2bf50 ["INT_ADD", "register:40f0:8", ["const:b2bf50:8", "const:4:8"]]
- 00b2bf50 ["CALL", null, ["ram:66d050:8"]]
+ 00b2c378 ["INT_ADD", "register:40f0:8", ["const:b2c378:8", "const:4:8"]]
+ 00b2c378 ["CALL", null, ["ram:66d090:8"]]
- 00b2bf50 bytes 4004ed97
+ 00b2c378 bytes 4603ed97
- 00b2be00 ["INT_ADD", "register:40f0:8", ["const:b2be00:8", "const:4:8"]]
- 00b2be00 ["CALL", null, ["callee:00c5ab70:8"]]
+ 00b2c228 ["INT_ADD", "register:40f0:8", ["const:b2c228:8", "const:4:8"]]
+ 00b2c228 ["CALL", null, ["callee:00c5ab70:8"]]
- 00b2be00 bytes 5cba0494
+ 00b2c228 bytes 52ba0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fce8402ab59a3fa2d6cd989ece756895"></a>

### [`00b2bffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bffc.md) → [`00b2c424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c424.md) FUN_00b2c424

採用 · 移動量 `+0x428` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043b618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b618.md) · 呼出先 5件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f4f4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047b78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b78c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`0043b658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b658.md) · 呼出先 5件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f534.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047b7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7cc.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

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
      "site": "00b2c43c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b2c014",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00b2c43c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00b2c43c",
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

- 旧版 [`00b2c014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bffc.md#insn-00b2c014) · [`00b2c004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bffc.md#insn-00b2c004) · [`00b2c010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bffc.md#insn-00b2c010)
- 新版 [`00b2c43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c424.md#insn-00b2c43c) · [`00b2c42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c424.md#insn-00b2c42c) · [`00b2c438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c424.md#insn-00b2c438)

~~~diff
- 00b2c014 ["INT_ADD", "register:40f0:8", ["const:b2c014:8", "const:4:8"]]
- 00b2c014 ["CALL", null, ["ram:47acb4:8"]]
+ 00b2c43c ["INT_ADD", "register:40f0:8", ["const:b2c43c:8", "const:4:8"]]
+ 00b2c43c ["CALL", null, ["ram:47acf4:8"]]
- 00b2c014 bytes 283be597
+ 00b2c43c bytes 2e3ae597
- 00b2c004 ["INT_ADD", "register:40f0:8", ["const:b2c004:8", "const:4:8"]]
- 00b2c004 ["CALL", null, ["callee:008514f8:8"]]
+ 00b2c42c ["INT_ADD", "register:40f0:8", ["const:b2c42c:8", "const:4:8"]]
+ 00b2c42c ["CALL", null, ["callee:008514f8:8"]]
- 00b2c004 bytes 2d95f497
+ 00b2c42c bytes 3394f497
- 00b2c010 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2c010 ["INT_ADD", "register:40f0:8", ["const:b2c010:8", "const:4:8"]]
- 00b2c010 ["CALLIND", null, ["register:0:8"]]
+ 00b2c438 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b2c438 ["INT_ADD", "register:40f0:8", ["const:b2c438:8", "const:4:8"]]
+ 00b2c438 ["CALLIND", null, ["register:0:8"]]
- 00b2c010 bytes 00013fd6
+ 00b2c438 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9803b08396d6ea793e873271c61093b2"></a>

### [`00b2c028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2c028.md) → [`00b2c450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md) FUN_00b2c450

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0043b57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b57c.md) [`00b2d430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d430.md) · 呼出先 24件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md)
- 新版 呼出元 2件 [`0043b5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b5bc.md) [`00b2d858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d858.md) · 呼出先 24件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.12% / 新版 98.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2c64c",
      "incomplete_value": false,
      "site": "00b2c64c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2c224",
      "incomplete_value": false,
      "site": "00b2c224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2c728",
      "incomplete_value": true,
      "site": "00b2c734",
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
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:454:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2c300",
      "incomplete_value": true,
      "site": "00b2c30c",
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
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:414:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2ca5c",
      "incomplete_value": true,
      "site": "00b2ca6c",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:faa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2c634",
      "incomplete_value": true,
      "site": "00b2c644",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:ece:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 75,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b2c64c",
      "DATA",
      [
        "storage",
        "00c8ef68",
        null,
        "undefined *"
      ]
    ],
    [
      "00b2c728",
      "READ",
      [
        "storage",
        "002b0414",
        null,
        "string"
      ]
    ],
    [
      "00b2c7c4",
      "READ",
      [
        "storage",
        "00c8ef90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2c64c",
      "DATA",
      [
        "storage",
        "00c8f368",
        null,
        "undefined *"
      ]
    ],
    [
      "00b2c728",
      "READ",
      [
        "storage",
        "002b0454",
        null,
        "string"
      ]
    ],
    [
      "00b2c7c4",
      "READ",
      [
        "storage",
        "00c8f390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2c21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2c028.md#insn-00b2c21c) · [`00b2c6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2c028.md#insn-00b2c6cc) · [`00b2c734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2c028.md#insn-00b2c734)
- 新版 [`00b2c644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md#insn-00b2c644) · [`00b2caf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md#insn-00b2caf4) · [`00b2cb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md#insn-00b2cb5c)

~~~diff
- 00b2c21c ["COPY", "register:4050:8", ["const:c8e000:8"]]
+ 00b2c644 ["COPY", "register:4050:8", ["const:c8f000:8"]]
- 00b2c21c bytes 0a0b00d0
+ 00b2c644 bytes 0a0b00f0
- 00b2c6cc ["INT_ADD", "register:40f0:8", ["const:b2c6cc:8", "const:4:8"]]
- 00b2c6cc ["CALL", null, ["ram:48ccb8:8"]]
+ 00b2caf4 ["INT_ADD", "register:40f0:8", ["const:b2caf4:8", "const:4:8"]]
+ 00b2caf4 ["CALL", null, ["ram:48ccf8:8"]]
- 00b2c6cc bytes 7b81e597
+ 00b2caf4 bytes 8180e597
- 00b2c734 ["INT_ADD", "register:40f0:8", ["const:b2c734:8", "const:4:8"]]
- 00b2c734 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b2cb5c ["INT_ADD", "register:40f0:8", ["const:b2cb5c:8", "const:4:8"]]
+ 00b2cb5c ["CALL", null, ["callee:00c57eb0:8"]]
- 00b2c734 bytes dfac0494
+ 00b2cb5c bytes d5ac0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05858f53446ffb123379417b9c6d4ee0"></a>

### [`00b2ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md) → [`00b2ce48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md) FUN_00b2ce48

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0043aeec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043aeec.md) [`0043b26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b26c.md) · 呼出先 23件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3e4.md) [`0043f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3ec.md) [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) [`0046ca14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca14.md)
- 新版 呼出元 2件 [`0043af2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043af2c.md) [`0043b2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b2ac.md) · 呼出先 23件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f424.md) [`0043f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f42c.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`0046ca54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca54.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.69% / 新版 94.69%

CFGの説明率　旧版 88.64% / 新版 92.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2ce90",
      "incomplete_value": true,
      "site": "00b2ceac",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:4ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2ca68",
      "incomplete_value": true,
      "site": "00b2ca84",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:420:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b2cf54",
      "incomplete_value": true,
      "site": "00b2cf54",
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
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2cb2c",
      "incomplete_value": true,
      "site": "00b2cb2c",
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
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b2cf58",
      "incomplete_value": true,
      "site": "00b2cf58",
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
            "const:24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2cb30",
      "incomplete_value": true,
      "site": "00b2cb30",
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
            "const:24:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b2ce90",
      "READ",
      [
        "storage",
        "002a9420",
        null,
        "string"
      ]
    ],
    [
      "00b2cf50",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ],
    [
      "00b2cf54",
      "WRITE",
      [
        "storage",
        "00ca4898",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b2ce90",
      "READ",
      [
        "storage",
        "002a94ed",
        null,
        "string"
      ]
    ],
    [
      "00b2cf50",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ],
    [
      "00b2cf54",
      "WRITE",
      [
        "storage",
        "00ca4c98",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2cdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md#insn-00b2cdc0) · [`00b2ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md#insn-00b2ca44) · [`00b2ca4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md#insn-00b2ca4c)
- 新版 [`00b2d1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md#insn-00b2d1e8) · [`00b2ce6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md#insn-00b2ce6c) · [`00b2ce74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md#insn-00b2ce74)

~~~diff
- 00b2cdc0 ["INT_ADD", "register:40f0:8", ["const:b2cdc0:8", "const:4:8"]]
- 00b2cdc0 ["CALL", null, ["ram:48ccb8:8"]]
+ 00b2d1e8 ["INT_ADD", "register:40f0:8", ["const:b2d1e8:8", "const:4:8"]]
+ 00b2d1e8 ["CALL", null, ["ram:48ccf8:8"]]
- 00b2cdc0 bytes be7fe597
+ 00b2d1e8 bytes c47ee597
- 00b2ca44 ["INT_ADD", "register:40f0:8", ["const:b2ca44:8", "const:4:8"]]
- 00b2ca44 ["CALL", null, ["callee:00588e6c:8"]]
+ 00b2ce6c ["INT_ADD", "register:40f0:8", ["const:b2ce6c:8", "const:4:8"]]
+ 00b2ce6c ["CALL", null, ["callee:00588e6c:8"]]
- 00b2ca44 bytes fa70e997
+ 00b2ce6c bytes 0070e997
- 00b2ca4c ["INT_ADD", "register:40f0:8", ["const:b2ca4c:8", "const:4:8"]]
- 00b2ca4c ["CALL", null, ["callee:0058915c:8"]]
+ 00b2ce74 ["INT_ADD", "register:40f0:8", ["const:b2ce74:8", "const:4:8"]]
+ 00b2ce74 ["CALL", null, ["callee:0058915c:8"]]
- 00b2ca4c bytes b471e997
+ 00b2ce74 bytes ba70e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fab207ece86d4a70d516f1df70a56e84"></a>

### [`00b2cf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cf10.md) → [`00b2d338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d338.md) FUN_00b2d338

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0043b554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b554.md) · 呼出先 8件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3ec.md) [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) [`004440a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004440a0.md) [`004466b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004466b8.md)
- 新版 呼出元 1件 [`0043b594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b594.md) · 呼出先 8件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f42c.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`004440e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/004440e0.md) [`004466f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/004466f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 87.50% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2cf20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cf10.md#insn-00b2cf20) · [`00b2cf24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cf10.md#insn-00b2cf24) · [`00b2cf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cf10.md#insn-00b2cf30)
- 新版 [`00b2d348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d338.md#insn-00b2d348) · [`00b2d34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d338.md#insn-00b2d34c) · [`00b2d358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d338.md#insn-00b2d358)

~~~diff
- 00b2cf20 ["INT_ADD", "register:40f0:8", ["const:b2cf20:8", "const:4:8"]]
- 00b2cf20 ["CALL", null, ["callee:0066d0dc:8"]]
+ 00b2d348 ["INT_ADD", "register:40f0:8", ["const:b2d348:8", "const:4:8"]]
+ 00b2d348 ["CALL", null, ["callee:0066d0dc:8"]]
- 00b2cf20 bytes 5f00ed97
+ 00b2d348 bytes 65ffec97
- 00b2cf24 ["INT_ADD", "register:40f0:8", ["const:b2cf24:8", "const:4:8"]]
- 00b2cf24 ["CALL", null, ["callee:008514f8:8"]]
+ 00b2d34c ["INT_ADD", "register:40f0:8", ["const:b2d34c:8", "const:4:8"]]
+ 00b2d34c ["CALL", null, ["callee:008514f8:8"]]
- 00b2cf24 bytes 6591f497
+ 00b2d34c bytes 6b90f497
- 00b2cf30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2cf30 ["INT_ADD", "register:40f0:8", ["const:b2cf30:8", "const:4:8"]]
- 00b2cf30 ["CALLIND", null, ["register:0:8"]]
+ 00b2d358 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b2d358 ["INT_ADD", "register:40f0:8", ["const:b2d358:8", "const:4:8"]]
+ 00b2d358 ["CALLIND", null, ["register:0:8"]]
- 00b2cf30 bytes 00013fd6
+ 00b2d358 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94f6a1e2fda17db6889f1ed28b121ca7"></a>

### [`00b2cfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cfb0.md) → [`00b2d3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d3d8.md) FUN_00b2d3d8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b2d3ec",
      "incomplete_value": false,
      "site": "00b2d3f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2cfc4",
      "incomplete_value": false,
      "site": "00b2cfc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "00b2d3f0",
      "DATA",
      [
        "storage",
        "00c8ee68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2d3f0",
      "DATA",
      [
        "storage",
        "00c8f268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2cfbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cfb0.md#insn-00b2cfbc) · [`00b2cfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cfb0.md#insn-00b2cfc0) · [`00b2cfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cfb0.md#insn-00b2cfc4)
- 新版 [`00b2d3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d3d8.md#insn-00b2d3e4) · [`00b2d3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d3d8.md#insn-00b2d3e8) · [`00b2d3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d3d8.md#insn-00b2d3ec)

~~~diff
- 00b2cfbc ["INT_ADD", "register:40f0:8", ["const:b2cfbc:8", "const:4:8"]]
- 00b2cfbc ["CALL", null, ["callee:00c57e90:8"]]
+ 00b2d3e4 ["INT_ADD", "register:40f0:8", ["const:b2d3e4:8", "const:4:8"]]
+ 00b2d3e4 ["CALL", null, ["callee:00c57e90:8"]]
- 00b2cfbc bytes b5aa0494
+ 00b2d3e4 bytes abaa0494
- 00b2cfc0 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00b2d3e8 ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00b2cfc0 bytes 080b00d0
+ 00b2d3e8 bytes 080b00d0
- 00b2cfc4 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 00b2cfc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b2cfc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b2cfc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b2d3ec ["COPY", "tmp:0:8", ["const:268:8"]]
+ 00b2d3ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b2d3ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b2d3ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b2cfc4 bytes 08a13991
+ 00b2d3ec bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-374b871ae28ada34241d231db3dc4530"></a>

### [`00b2d034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d034.md) → [`00b2d45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d45c.md) FUN_00b2d45c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b2d470",
      "incomplete_value": false,
      "site": "00b2d474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2d048",
      "incomplete_value": false,
      "site": "00b2d04c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "00b2d474",
      "DATA",
      [
        "storage",
        "00c8eee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2d474",
      "DATA",
      [
        "storage",
        "00c8f2e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2d040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d034.md#insn-00b2d040) · [`00b2d044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d034.md#insn-00b2d044) · [`00b2d048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d034.md#insn-00b2d048)
- 新版 [`00b2d468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d45c.md#insn-00b2d468) · [`00b2d46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d45c.md#insn-00b2d46c) · [`00b2d470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d45c.md#insn-00b2d470)

~~~diff
- 00b2d040 ["INT_ADD", "register:40f0:8", ["const:b2d040:8", "const:4:8"]]
- 00b2d040 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b2d468 ["INT_ADD", "register:40f0:8", ["const:b2d468:8", "const:4:8"]]
+ 00b2d468 ["CALL", null, ["callee:00c57e90:8"]]
- 00b2d040 bytes 94aa0494
+ 00b2d468 bytes 8aaa0494
- 00b2d044 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00b2d46c ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00b2d044 bytes 080b00b0
+ 00b2d46c bytes 080b00d0
- 00b2d048 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 00b2d048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b2d048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b2d048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b2d470 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00b2d470 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b2d470 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b2d470 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b2d048 bytes 08a13b91
+ 00b2d470 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29d547e1c0565136a0e51efb9df2d596"></a>

### [`00b2d058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d058.md) → [`00b2d480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d480.md) FUN_00b2d480

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b2d484",
      "incomplete_value": false,
      "site": "00b2d488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2d05c",
      "incomplete_value": false,
      "site": "00b2d060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "00b2d488",
      "DATA",
      [
        "storage",
        "00c8eee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2d488",
      "DATA",
      [
        "storage",
        "00c8f2e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2d058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d058.md#insn-00b2d058) · [`00b2d05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d058.md#insn-00b2d05c)
- 新版 [`00b2d480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d480.md#insn-00b2d480) · [`00b2d484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d480.md#insn-00b2d484)

~~~diff
- 00b2d058 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00b2d480 ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00b2d058 bytes 080b00b0
+ 00b2d480 bytes 080b00d0
- 00b2d05c ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 00b2d05c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b2d05c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b2d05c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b2d484 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00b2d484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b2d484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b2d484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b2d05c bytes 08a13b91
+ 00b2d484 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d83a0e03b367a534544c88407fb512b5"></a>

### [`00b2d0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d0b4.md) → [`00b2d4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d4dc.md) FUN_00b2d4dc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2c028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2c028.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b2d2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d2b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b2c450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2d6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d6e0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 65.22% / 新版 68.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2d278"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b2d6a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2d1b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2d1b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2d68c"
      ]
    ],
    [
      "unmatched:00b2d248",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2d68c"
      ]
    ],
    [
      "unmatched:00b2d27c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2d6ac"
      ]
    ]
  ],
  "added": [
    [
      "00b2d5d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2d68c"
      ]
    ],
    [
      "00b2d670",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2d68c"
      ]
    ],
    [
      "00b2d6a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2d6ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2d1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d0b4.md#insn-00b2d1a0) · [`00b2d1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d0b4.md#insn-00b2d1b0) · [`00b2d224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d0b4.md#insn-00b2d224)
- 新版 [`00b2d64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d4dc.md#insn-00b2d64c)

~~~diff
- 00b2d1a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2d1a0 ["INT_ADD", "register:40f0:8", ["const:b2d1a0:8", "const:4:8"]]
- 00b2d1a0 ["CALLIND", null, ["register:0:8"]]
- 00b2d1a0 bytes 00013fd6
- 00b2d1b0 ["CBRANCH", null, ["local:b29:8", "register:101:1"]]
- 00b2d1b0 bytes a0050054
- 00b2d224 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2d224 ["INT_ADD", "register:40f0:8", ["const:b2d224:8", "const:4:8"]]
- 00b2d224 ["CALLIND", null, ["register:0:8"]]
+ 00b2d64c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b2d64c ["INT_ADD", "register:40f0:8", ["const:b2d64c:8", "const:4:8"]]
+ 00b2d64c ["CALLIND", null, ["register:0:8"]]
- 00b2d224 bytes 00013fd6
+ 00b2d64c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d57154afbea99b3d1bcbc95168c8408f"></a>

### [`00b2d2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d2b8.md) → [`00b2d6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d6e0.md) FUN_00b2d6e0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2d0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d0b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00b2d4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d4dc.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b2d6ec",
      "incomplete_value": false,
      "site": "00b2d6f0",
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
      "definition_site": "00b2d2c4",
      "incomplete_value": false,
      "site": "00b2d2c8",
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
      "00b2d6ec",
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
      "00b2d6ec",
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

- 旧版 [`00b2d2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d2b8.md#insn-00b2d2c8) · [`00b2d2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d2b8.md#insn-00b2d2c4)
- 新版 [`00b2d6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d6e0.md#insn-00b2d6f0) · [`00b2d6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d6e0.md#insn-00b2d6ec)

~~~diff
- 00b2d2c8 ["INT_ADD", "register:40f0:8", ["const:b2d2c8:8", "const:4:8"]]
- 00b2d2c8 ["CALL", null, ["callee:0043b778:8"]]
+ 00b2d6f0 ["INT_ADD", "register:40f0:8", ["const:b2d6f0:8", "const:4:8"]]
+ 00b2d6f0 ["CALL", null, ["callee:0043b778:8"]]
- 00b2d2c8 bytes 1c39e497
+ 00b2d6f0 bytes 2238e497
- 00b2d2c4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b2d2c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2d2c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2d2c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2d6ec ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b2d6ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2d6ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2d6ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2d2c4 bytes 00303c91
+ 00b2d6ec bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-133412ceadaf8d6296b03e2d0d806ca8"></a>

### [`00b2d32c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d32c.md) → [`00b2d754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d754.md) FUN_00b2d754

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2d784",
      "incomplete_value": false,
      "site": "00b2d784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2d35c",
      "incomplete_value": false,
      "site": "00b2d35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "00b2d784",
      "DATA",
      [
        "storage",
        "00c8ef68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2d784",
      "DATA",
      [
        "storage",
        "00c8f368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2d340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d32c.md#insn-00b2d340) · [`00b2d34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d32c.md#insn-00b2d34c) · [`00b2d350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d32c.md#insn-00b2d350)
- 新版 [`00b2d768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d754.md#insn-00b2d768) · [`00b2d774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d754.md#insn-00b2d774) · [`00b2d778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d754.md#insn-00b2d778)

~~~diff
- 00b2d340 ["INT_ADD", "register:40f0:8", ["const:b2d340:8", "const:4:8"]]
- 00b2d340 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b2d768 ["INT_ADD", "register:40f0:8", ["const:b2d768:8", "const:4:8"]]
+ 00b2d768 ["CALL", null, ["callee:00c57e90:8"]]
- 00b2d340 bytes d4a90494
+ 00b2d768 bytes caa90494
- 00b2d34c ["COPY", "register:4058:8", ["const:c8e000:8"]]
+ 00b2d774 ["COPY", "register:4058:8", ["const:c8f000:8"]]
- 00b2d34c bytes 0b0b00b0
+ 00b2d774 bytes 0b0b00d0
- 00b2d350 ["COPY", "tmp:0:8", ["const:f68:8"]]
- 00b2d350 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00b2d350 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00b2d350 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00b2d778 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 00b2d778 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00b2d778 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00b2d778 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00b2d350 bytes 6ba13d91
+ 00b2d778 bytes 6ba10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52f61f660e5a3785f75cfd5a61b64a9f"></a>

### [`00b2d3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d3a8.md) → [`00b2d7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d7d0.md) FUN_00b2d7d0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

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
      "definition_site": "00b2d7dc",
      "incomplete_value": false,
      "site": "00b2d7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2d3b4",
      "incomplete_value": false,
      "site": "00b2d3b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "00b2d7dc",
      "DATA",
      [
        "storage",
        "00c8ef68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2d7dc",
      "DATA",
      [
        "storage",
        "00c8f368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2d3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d3a8.md#insn-00b2d3ac) · [`00b2d3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d3a8.md#insn-00b2d3b0)
- 新版 [`00b2d7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d7d0.md#insn-00b2d7d4) · [`00b2d7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d7d0.md#insn-00b2d7d8)

~~~diff
- 00b2d3ac ["COPY", "register:4048:8", ["const:c8e000:8"]]
+ 00b2d7d4 ["COPY", "register:4048:8", ["const:c8f000:8"]]
- 00b2d3ac bytes 090b00b0
+ 00b2d7d4 bytes 090b00d0
- 00b2d3b0 ["COPY", "tmp:0:8", ["const:f68:8"]]
- 00b2d3b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b2d3b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b2d3b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b2d7d8 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 00b2d7d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b2d7d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b2d7d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b2d3b0 bytes 29a13d91
+ 00b2d7d8 bytes 29a10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b85e5c2c9d4f828650055c6625a2b91d"></a>

### [`00b2d874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d874.md) → [`00b2dc9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2dc9c.md) FUN_00b2dc9c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0067e15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e15c.md) · 呼出先 2件 [`00b3c6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c6b0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`0067e19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e19c.md) · 呼出先 2件 [`00b3cad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3cad8.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2d89c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b2dcc4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b2d890",
      "incomplete_value": true,
      "site": "00b2d8a0",
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
            "const:a8:8"
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
      "unmatched:00b2d89c",
      "DATA",
      [
        "storage",
        "00c74430",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b2dcc4",
      "DATA",
      [
        "storage",
        "00c74830",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2d89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d874.md#insn-00b2d89c) · [`00b2d8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d874.md#insn-00b2d8a0)
- 新版 [`00b2dcc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2dc9c.md#insn-00b2dcc8) · [`00b2dcc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2dc9c.md#insn-00b2dcc4)

~~~diff
- 00b2d89c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b2d89c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b2d89c bytes 680200f9
- 00b2d8a0 ["INT_ADD", "register:40f0:8", ["const:b2d8a0:8", "const:4:8"]]
- 00b2d8a0 ["CALL", null, ["callee:00c58090:8"]]
+ 00b2dcc8 ["INT_ADD", "register:40f0:8", ["const:b2dcc8:8", "const:4:8"]]
+ 00b2dcc8 ["CALL", null, ["callee:00c58090:8"]]
- 00b2d8a0 bytes fca80494
+ 00b2dcc8 bytes f2a80494
+ 00b2dcc4 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 00b2dcc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b2dcc4 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-601f077f188628fec6460c6cc814b538"></a>

### [`00b2d8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d8b8.md) → [`00b2dce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2dce0.md) FUN_00b2dce0

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) [`00ac52f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac5/00ac52f4.md) [`00ac6a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac6/00ac6a98.md) [`00ac7008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7008.md) · 呼出先 11件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00864120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00864/00864120.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 4件 [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) [`00ac54f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac5/00ac54f0.md) [`00ac6c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac6/00ac6c94.md) [`00ac7204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac7/00ac7204.md) · 呼出先 11件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00864160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864160.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 26.40% / 新版 26.40%

CFGの説明率　旧版 34.68% / 新版 39.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 26件, `unresolved_store_alignment` 112件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2d8bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2d8bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2d8c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2d8bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2d8c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2d8c4",
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
      "00b2dce4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b2dce8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b2dcec",
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

- 旧版 [`00b2d8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d8b8.md#insn-00b2d8bc) · [`00b2d8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d8b8.md#insn-00b2d8c0) · [`00b2d8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d8b8.md#insn-00b2d8c4)

~~~diff
- 00b2d8bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b2d8bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b2d8bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b2d8bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b2d8bc bytes fd7b06a9
- 00b2d8c0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b2d8c0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b2d8c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b2d8c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b2d8c0 bytes f65707a9
- 00b2d8c4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b2d8c4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b2d8c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b2d8c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b2d8c4 bytes f44f08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-005fa3ea2798b2a112cda8acec8f27c3"></a>

### [`00b2e090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2e/00b2e090.md) → [`00b2e4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2e/00b2e4b8.md) FUN_00b2e4b8

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`0090da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090da6c.md) [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) [`00ac52f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac5/00ac52f4.md) [`00ac6a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac6/00ac6a98.md) [`00ac7008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7008.md) · 呼出先 24件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046e4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e4f8.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md)
- 新版 呼出元 5件 [`0090dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090dc08.md) [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) [`00ac54f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac5/00ac54f0.md) [`00ac6c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac6/00ac6c94.md) [`00ac7204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac7/00ac7204.md) · 呼出先 24件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046e538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e538.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 61.23% / 新版 61.23%

CFGの説明率　旧版 44.94% / 新版 44.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 1件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 26件, `unresolved_store_alignment` 78件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2e114"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2e118"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2e128"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b2e52c",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b2e530",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b2eb48"
      ]
    ],
    [
      "unmatched:00b2e114",
      "WRITE",
      [
        "storage",
        "Stack[-0x55]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b2e52c",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b2e530",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2ef70"
      ]
    ],
    [
      "00b2e53c",
      "WRITE",
      [
        "storage",
        "Stack[-0x55]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2e114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2e/00b2e090.md#insn-00b2e114) · [`00b2e118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2e/00b2e090.md#insn-00b2e118) · [`00b2e128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2e/00b2e090.md#insn-00b2e128)

~~~diff
- 00b2e114 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b2e114 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b2e114 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffeb:8"]]
- 00b2e114 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b2e114 bytes bfb31e38
- 00b2e118 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b2e118 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe0:8"]]
- 00b2e118 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b2e118 bytes a8031e38
- 00b2e128 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b2e128 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:21:8"]]
- 00b2e128 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b2e128 bytes a9120278
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b036c13d67c0a7edbb0d4eb9570ad9f0"></a>

### [`00b2ef24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2e/00b2ef24.md) → [`00b2f34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f34c.md) FUN_00b2f34c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) [`0097df28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097df28.md) · 呼出先 2件 [`00695b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695b6c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) [`0097e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097e/0097e0c4.md) · 呼出先 2件 [`00695bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695bac.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2f364",
      "incomplete_value": false,
      "site": "00b2f38c",
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
      "definition_site": "00b2ef3c",
      "incomplete_value": false,
      "site": "00b2ef64",
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
      "00b2f364",
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
      "00b2f364",
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

- 旧版 [`00b2ef64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2e/00b2ef24.md#insn-00b2ef64) · [`00b2ef3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2e/00b2ef24.md#insn-00b2ef3c) · [`00b2ef8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2e/00b2ef24.md#insn-00b2ef8c)
- 新版 [`00b2f38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f34c.md#insn-00b2f38c) · [`00b2f364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f34c.md#insn-00b2f364) · [`00b2f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f34c.md#insn-00b2f3b4)

~~~diff
- 00b2ef64 ["INT_ADD", "register:40f0:8", ["const:b2ef64:8", "const:4:8"]]
- 00b2ef64 ["CALL", null, ["callee:00695bac:8"]]
+ 00b2f38c ["INT_ADD", "register:40f0:8", ["const:b2f38c:8", "const:4:8"]]
+ 00b2f38c ["CALL", null, ["callee:00695bac:8"]]
- 00b2ef64 bytes 029bed97
+ 00b2f38c bytes 089aed97
- 00b2ef3c ["COPY", "tmp:0:8", ["const:6b5:8"]]
- 00b2ef3c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b2ef3c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b2ef3c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b2f364 ["COPY", "tmp:0:8", ["const:6f5:8"]]
+ 00b2f364 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b2f364 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b2f364 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b2ef3c bytes 42d41a91
+ 00b2f364 bytes 42d41b91
- 00b2ef8c ["INT_ADD", "register:40f0:8", ["const:b2ef8c:8", "const:4:8"]]
- 00b2ef8c ["CALL", null, ["callee:00c57ee0:8"]]
+ 00b2f3b4 ["INT_ADD", "register:40f0:8", ["const:b2f3b4:8", "const:4:8"]]
+ 00b2f3b4 ["CALL", null, ["callee:00c57ee0:8"]]
- 00b2ef8c bytes d5a20494
+ 00b2f3b4 bytes cba20494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fba5e5a4061c17631fddd99b43696d8"></a>

### [`00b2ef90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2e/00b2ef90.md) → [`00b2f3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f3b8.md) _INIT_261

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 64.97% / 新版 64.97%

CFGの説明率　旧版 71.88% / 新版 67.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2efc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2efd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2efd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2efc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2efcc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b2efd4",
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
      "00b2f3e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b2f3f4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b2f3fc",
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

- 旧版 [`00b2efc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2e/00b2ef90.md#insn-00b2efc0) · [`00b2efd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2e/00b2ef90.md#insn-00b2efd4) · [`00b2efd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2e/00b2ef90.md#insn-00b2efd8)

~~~diff
- 00b2efc0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b2efc0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b2efc0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b2efc0 bytes a9831ff8
- 00b2efd4 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b2efd4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00b2efd4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b2efd4 bytes ea130278
- 00b2efd8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b2efd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b2efd8 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1d1efc7f0d5c192235aa7a297558a19"></a>

### [`00b2f368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f368.md) → [`00b2f790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f790.md) FUN_00b2f790

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0075d548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d548.md) · 呼出先 2件 [`00b3ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba38.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md)
- 新版 呼出元 1件 [`0075d588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d588.md) · 呼出先 2件 [`00b3be60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be60.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b2f7e0",
      "incomplete_value": false,
      "site": "00b2f7e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2f3b8",
      "incomplete_value": false,
      "site": "00b2f3b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a9c:8"
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
      "00b2f7e0",
      "WRITE",
      [
        "storage",
        "00ca3a9c",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b2f7e0",
      "WRITE",
      [
        "storage",
        "00ca3e9c",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2f3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f368.md#insn-00b2f3b8) · [`00b2f37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f368.md#insn-00b2f37c) · [`00b2f3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f368.md#insn-00b2f3ac)
- 新版 [`00b2f7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f790.md#insn-00b2f7e0) · [`00b2f7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f790.md#insn-00b2f7a4) · [`00b2f7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f790.md#insn-00b2f7d4)

~~~diff
- 00b2f3b8 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b2f3b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:a9c:8"]]
- 00b2f3b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b2f7e0 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00b2f7e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:e9c:8"]]
+ 00b2f7e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b2f3b8 bytes 09712a39
+ 00b2f7e0 bytes 09713a39
- 00b2f37c ["INT_ADD", "register:40f0:8", ["const:b2f37c:8", "const:4:8"]]
- 00b2f37c ["CALL", null, ["callee:00b3be94:8"]]
+ 00b2f7a4 ["INT_ADD", "register:40f0:8", ["const:b2f7a4:8", "const:4:8"]]
+ 00b2f7a4 ["CALL", null, ["callee:00b3be94:8"]]
- 00b2f37c bytes bc310094
+ 00b2f7a4 bytes bc310094
- 00b2f3ac ["INT_ADD", "register:40f0:8", ["const:b2f3ac:8", "const:4:8"]]
- 00b2f3ac ["CALL", null, ["callee:00b3be60:8"]]
+ 00b2f7d4 ["INT_ADD", "register:40f0:8", ["const:b2f7d4:8", "const:4:8"]]
+ 00b2f7d4 ["CALL", null, ["callee:00b3be60:8"]]
- 00b2f3ac bytes a3310094
+ 00b2f7d4 bytes a3310094
~~~


<a id="compare-5a1a1d2c0bd12ac23311884db7e88761"></a>

### [`00b2f5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f5e4.md) → [`00b2fa0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2fa0c.md) FUN_00b2fa0c

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) · 呼出先 15件 [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`00597dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597dc8.md) [`00597e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md) [`00752240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/00752240.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md)
- 新版 呼出元 1件 [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) · 呼出先 15件 [`0046dabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dabc.md) [`00597e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e08.md) [`00597e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e48.md) [`00752280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00752/00752280.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md)

変更の種類 branch_condition_or_target, call, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 55.41% / 新版 55.41%

CFGの説明率　旧版 24.24% / 新版 27.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f604"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f608"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f640"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2f604",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2f60c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "unmatched:00b2f610",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768398"
      ]
    ]
  ],
  "added": [
    [
      "00b2fa2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b2fa34",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "00b2fa38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2f604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f5e4.md#insn-00b2f604) · [`00b2f608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f5e4.md#insn-00b2f608) · [`00b2f614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f5e4.md#insn-00b2f614)

~~~diff
- 00b2f604 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b2f604 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b2f604 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b2f604 bytes a8831ff8
- 00b2f608 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b2f608 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00b2f608 ["COPY", "tmp:2:4", ["tmp:1:4"]]
- 00b2f608 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:2:2"]]
- 00b2f608 bytes 7f020079
- 00b2f614 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b2f614 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b2f614 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b2f614 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b2f614 bytes 00040036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e318f68f56f7e23c0d8972af41cbf68"></a>

### [`00b2f918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f918.md) → [`00b2fd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2fd40.md) FUN_00b2fd40

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2f5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f5e4.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00b303f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b303f0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00b2fa0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2fa0c.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00b30818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b30/00b30818.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 50.00% / 新版 38.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f95c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f960"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2f948",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2f95c",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2f960",
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
      "00b2fd70",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b2fd84",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "00b2fd88",
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

- 旧版 [`00b2f948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f918.md#insn-00b2f948) · [`00b2f95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f918.md#insn-00b2f95c) · [`00b2f960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f918.md#insn-00b2f960)

~~~diff
- 00b2f948 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b2f948 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b2f948 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b2f948 bytes a9831ff8
- 00b2f95c ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b2f95c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b2f95c bytes e003803d
- 00b2f960 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b2f960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b2f960 bytes e80b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-143c1bbbb178421e377635c87a84bb9a"></a>

### [`00b2fa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2fa50.md) → [`00b2fe78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2fe78.md) FUN_00b2fe78

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2f5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f5e4.md) · 呼出先 12件 [`00560418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560418.md) [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`005975dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975dc.md) [`005975e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975e4.md) [`00597e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e84.md)
- 新版 呼出元 1件 [`00b2fa0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2fa0c.md) · 呼出先 12件 [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`0059761c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059761c.md) [`00597624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597624.md) [`00597ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 47.73% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2fa70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2fa7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2faa0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2fa70",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2fa74",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "unmatched:00b2fa7c",
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
      "00b2fe98",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b2fe9c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "00b2fea4",
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

- 旧版 [`00b2fa70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2fa50.md#insn-00b2fa70) · [`00b2fa74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2fa50.md#insn-00b2fa74) · [`00b2fa7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2fa50.md#insn-00b2fa7c)

~~~diff
- 00b2fa70 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b2fa70 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b2fa70 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b2fa70 bytes a8831ff8
- 00b2fa74 ["INT_ADD", "register:40f0:8", ["const:b2fa74:8", "const:4:8"]]
- 00b2fa74 ["CALL", null, ["callee:00c57e90:8"]]
- 00b2fa74 bytes 07a00494
- 00b2fa7c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b2fa7c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 00b2fa7c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b2fa7c bytes a0031cf8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2efefd42bcccc5a6c83607bbd30d873d"></a>

### [`00b2fd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2fd18.md) → [`00b30140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b30/00b30140.md) FUN_00b30140

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`00457838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md) [`004581f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/004581f0.md) · 呼出先 11件 [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00459a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459a90.md) [`0045bdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdb8.md) [`005975dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975dc.md) [`005975e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975e4.md)
- 新版 呼出元 3件 [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`00457878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md) [`00458230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458230.md) · 呼出先 11件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md) [`0045bdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md) [`0059761c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059761c.md) [`00597624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597624.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.10% / 新版 55.10%

CFGの説明率　旧版 1.56% / 新版 1.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 18件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2fd2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2fd2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2fd44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2fd2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2fd44",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2fd88",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b30154",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b3016c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b301b0",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2fd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2fd18.md#insn-00b2fd2c) · [`00b2fd44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2fd18.md#insn-00b2fd44) · [`00b2fd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2fd18.md#insn-00b2fd88)

~~~diff
- 00b2fd2c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b2fd2c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b2fd2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b2fd2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b2fd2c bytes f44f08a9
- 00b2fd44 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b2fd44 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b2fd44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b2fd44 bytes a8831ff8
- 00b2fd88 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b2fd88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:8"]]
- 00b2fd88 bytes 180000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e47630c9759f9da057afe82c02d6d4e"></a>

### [`00b301b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b301b4.md) → [`00b305dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b30/00b305dc.md) FUN_00b305dc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2fa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2fa50.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00b314f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b31/00b314f0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00b2fe78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2fe78.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00b31918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b31/00b31918.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.10% / 新版 90.10%

CFGの説明率　旧版 48.72% / 新版 46.34%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b301b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b301b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b301bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b301b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b301bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b301c0",
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
      "00b305e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b305e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b305e8",
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

- 旧版 [`00b301b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b301b4.md#insn-00b301b8) · [`00b301bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b301b4.md#insn-00b301bc) · [`00b301c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b301b4.md#insn-00b301c0)

~~~diff
- 00b301b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b301b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b301b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b301b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b301b8 bytes fd7b08a9
- 00b301bc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b301bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b301bc bytes f94b00f9
- 00b301c0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b301c0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b301c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b301c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b301c0 bytes f85f0aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdbf6724a64dfcf0b2e6b34a2ca031d3"></a>

### [`00b303f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b303f0.md) → [`00b30818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b30/00b30818.md) FUN_00b30818

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b2f918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f918.md) [`00b303f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b303f0.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00b2fd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2fd40.md) [`00b30818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b30/00b30818.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.30% / 新版 83.30%

CFGの説明率　旧版 37.85% / 新版 40.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `store_condition` 2件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b30418"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b30420"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b30428"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b30418",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b30420",
      "WRITE",
      [
        "storage",
        "Stack[-0xf8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b30428",
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
      "00b30840",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ],
    [
      "00b30848",
      "WRITE",
      [
        "storage",
        "Stack[-0xf8]",
        null,
        null
      ]
    ],
    [
      "00b30850",
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

- 旧版 [`00b30418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b303f0.md#insn-00b30418) · [`00b30420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b303f0.md#insn-00b30420) · [`00b30428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b303f0.md#insn-00b30428)

~~~diff
- 00b30418 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b30418 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4018:8"]]
- 00b30418 bytes e31300f9
- 00b30420 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b30420 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b30420 bytes e91f00f9
- 00b30428 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b30428 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00b30428 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b30428 bytes a9031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ec8677ef13877d028be49ab9cf89364"></a>

### [`00b30cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b30cf0.md) → [`00b31118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b31/00b31118.md) FUN_00b31118

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b303f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b303f0.md) [`00b30cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b30cf0.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00b30818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b30/00b30818.md) [`00b31118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b31/00b31118.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 40.54% / 新版 41.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_condition` 2件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b30cf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b30cf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b30cf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b30cf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b30cf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b30cfc",
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
      "00b3111c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b31120",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b31124",
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

- 旧版 [`00b30cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b30cf0.md#insn-00b30cf4) · [`00b30cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b30cf0.md#insn-00b30cf8) · [`00b30cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b30cf0.md#insn-00b30cfc)

~~~diff
- 00b30cf4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b30cf4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b30cf4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b30cf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b30cf4 bytes fd7b08a9
- 00b30cf8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b30cf8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b30cf8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b30cf8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b30cf8 bytes fc6f09a9
- 00b30cfc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b30cfc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b30cfc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b30cfc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b30cfc bytes fa670aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cf4df091bdb6acea1aaedfa61c0b3ee"></a>

### [`00b314f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b31/00b314f0.md) → [`00b31918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b31/00b31918.md) FUN_00b31918

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b301b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b301b4.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00b31730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b31/00b31730.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00b305dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b30/00b305dc.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00b31b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b31/00b31b58.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.10% / 新版 95.10%

CFGの説明率　旧版 34.21% / 新版 27.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31540"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3156c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31570"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b31540",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3156c",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b31570",
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
      "00b31968",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b31994",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "00b31998",
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

- 旧版 [`00b31540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b31/00b314f0.md#insn-00b31540) · [`00b3156c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b31/00b314f0.md#insn-00b3156c) · [`00b31570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b31/00b314f0.md#insn-00b31570)

~~~diff
- 00b31540 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffe0:8"]]
- 00b31540 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b31540 bytes a0039e3c
- 00b3156c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b3156c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b3156c bytes e00b803d
- 00b31570 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00b31570 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b31570 bytes e81b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef174db96079756ed399a155774cd1aa"></a>

### [`00b31730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b31/00b31730.md) → [`00b31b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b31/00b31b58.md) FUN_00b31b58

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b314f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b31/00b314f0.md) [`00b31730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b31/00b31730.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00b31918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b31/00b31918.md) [`00b31b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b31/00b31b58.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.82% / 新版 93.82%

CFGの説明率　旧版 66.18% / 新版 68.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_branch_alignment` 11件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b317ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31d00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31e70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b31788",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b31d8c"
      ]
    ],
    [
      "unmatched:00b317a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b31d8c"
      ]
    ],
    [
      "unmatched:00b317ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x2f8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b31bb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b31d8c"
      ]
    ],
    [
      "00b31bc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b31d8c"
      ]
    ],
    [
      "00b31bd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x2f8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3177c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b31/00b31730.md#insn-00b3177c) · [`00b31780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b31/00b31730.md#insn-00b31780) · [`00b31788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b31/00b31730.md#insn-00b31788)

~~~diff
- 00b3177c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b3177c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b3177c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b3177c ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00b3177c bytes bc16809a
- 00b31780 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b31780 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b31780 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b31780 ["COPY", "register:40d8:8", ["tmp:0:8"]]
- 00b31780 bytes 3b01949a
- 00b31788 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b31788 ["CBRANCH", null, ["local:b39:8", "tmp:0:1"]]
- 00b31788 bytes e30e0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f704dd3eb98df1edd4048878139aa662"></a>

### [`00b32608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32608.md) → [`00b32a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b32/00b32a30.md) _INIT_262

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00b32a6c",
      "incomplete_value": true,
      "site": "00b32a88",
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
      "definition_site": "00b32644",
      "incomplete_value": true,
      "site": "00b32660",
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
      "definition_site": "00b32a90",
      "incomplete_value": true,
      "site": "00b32aac",
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
      "definition_site": "00b32668",
      "incomplete_value": true,
      "site": "00b32684",
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
      "definition_site": "00b32ab0",
      "incomplete_value": true,
      "site": "00b32acc",
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
      "definition_site": "00b32688",
      "incomplete_value": true,
      "site": "00b326a4",
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
      "00b32a6c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00b32a90",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00b32ab0",
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
      "00b32a6c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b32a90",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b32ab0",
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

- 旧版 [`00b32768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32608.md#insn-00b32768) · [`00b3283c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32608.md#insn-00b3283c) · [`00b32634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32608.md#insn-00b32634)
- 新版 [`00b32b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b32/00b32a30.md#insn-00b32b90) · [`00b32c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b32/00b32a30.md#insn-00b32c64) · [`00b32a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b32/00b32a30.md#insn-00b32a5c)

~~~diff
- 00b32768 ["INT_ADD", "register:40f0:8", ["const:b32768:8", "const:4:8"]]
- 00b32768 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00b32b90 ["INT_ADD", "register:40f0:8", ["const:b32b90:8", "const:4:8"]]
+ 00b32b90 ["CALL", null, ["callee:0043b7f8:8"]]
- 00b32768 bytes 1424e497
+ 00b32b90 bytes 1a23e497
- 00b3283c ["INT_ADD", "register:40f0:8", ["const:b3283c:8", "const:4:8"]]
- 00b3283c ["CALL", null, ["callee:00c57e30:8"]]
+ 00b32c64 ["INT_ADD", "register:40f0:8", ["const:b32c64:8", "const:4:8"]]
+ 00b32c64 ["CALL", null, ["callee:00c57e30:8"]]
- 00b3283c bytes 7d940494
+ 00b32c64 bytes 73940494
- 00b32634 ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 00b32634 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00b32634 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00b32634 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00b32a5c ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 00b32a5c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00b32a5c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00b32a5c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00b32634 bytes 73e22a91
+ 00b32a5c bytes 73e23a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a67607f2ccd18d8972c99a3f1021f6f"></a>

### [`00b32998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32998.md) → [`00b32dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b32/00b32dc0.md) _INIT_263

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00b32dfc",
      "incomplete_value": true,
      "site": "00b32e18",
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
      "definition_site": "00b329d4",
      "incomplete_value": true,
      "site": "00b329f0",
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
      "definition_site": "00b32e20",
      "incomplete_value": true,
      "site": "00b32e3c",
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
      "definition_site": "00b329f8",
      "incomplete_value": true,
      "site": "00b32a14",
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
      "definition_site": "00b32e40",
      "incomplete_value": true,
      "site": "00b32e5c",
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
      "definition_site": "00b32a18",
      "incomplete_value": true,
      "site": "00b32a34",
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
      "00b32dfc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00b32e20",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00b32e40",
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
      "00b32dfc",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b32e20",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b32e40",
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

- 旧版 [`00b32af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32998.md#insn-00b32af8) · [`00b32bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32998.md#insn-00b32bcc) · [`00b329c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32998.md#insn-00b329c4)
- 新版 [`00b32f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b32/00b32dc0.md#insn-00b32f20) · [`00b32ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b32/00b32dc0.md#insn-00b32ff4) · [`00b32dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b32/00b32dc0.md#insn-00b32dec)

~~~diff
- 00b32af8 ["INT_ADD", "register:40f0:8", ["const:b32af8:8", "const:4:8"]]
- 00b32af8 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00b32f20 ["INT_ADD", "register:40f0:8", ["const:b32f20:8", "const:4:8"]]
+ 00b32f20 ["CALL", null, ["callee:0043b7f8:8"]]
- 00b32af8 bytes 3023e497
+ 00b32f20 bytes 3622e497
- 00b32bcc ["INT_ADD", "register:40f0:8", ["const:b32bcc:8", "const:4:8"]]
- 00b32bcc ["CALL", null, ["callee:00c57e30:8"]]
+ 00b32ff4 ["INT_ADD", "register:40f0:8", ["const:b32ff4:8", "const:4:8"]]
+ 00b32ff4 ["CALL", null, ["callee:00c57e30:8"]]
- 00b32bcc bytes 99930494
+ 00b32ff4 bytes 8f930494
- 00b329c4 ["COPY", "tmp:0:8", ["const:ad0:8"]]
- 00b329c4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00b329c4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00b329c4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00b32dec ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 00b32dec ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00b32dec ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00b32dec ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00b329c4 bytes 73422b91
+ 00b32dec bytes 73423b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cf0848eb50b96e1bf5742ae03026cb4"></a>

### [`00b32d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32d2c.md) → [`00b33154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33154.md) FUN_00b33154

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00aa572c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa5/00aa572c.md) [`00aa5ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa5/00aa5ee4.md) [`00aa7190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa7/00aa7190.md) [`00aa9230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa9/00aa9230.md) [`00aadd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadd90.md) · 呼出先 12件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 5件 [`00aa5928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa5/00aa5928.md) [`00aa60e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa6/00aa60e0.md) [`00aa738c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa7/00aa738c.md) [`00aa942c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa9/00aa942c.md) [`00aadf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aad/00aadf8c.md) · 呼出先 12件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b33198",
      "incomplete_value": true,
      "site": "00b331a8",
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
                "const:c81:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b32d70",
      "incomplete_value": true,
      "site": "00b32d80",
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
                "const:ba5:8"
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
      "definition_site": "00b331c4",
      "incomplete_value": true,
      "site": "00b331d0",
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
                "const:360:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b32d9c",
      "incomplete_value": true,
      "site": "00b32da8",
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
                "const:320:8"
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
      "definition_site": "00b331c0",
      "incomplete_value": true,
      "site": "00b331d4",
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
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:72d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b32d98",
      "incomplete_value": true,
      "site": "00b32dac",
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
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:6ed:8"
              ]
            ]
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
      "00b33198",
      "READ",
      [
        "storage",
        "002a4ba5",
        null,
        "string"
      ]
    ],
    [
      "00b331c0",
      "READ",
      [
        "storage",
        "002bc6ed",
        null,
        "string"
      ]
    ],
    [
      "00b331c0",
      "READ",
      [
        "storage",
        "002bc6fd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b33198",
      "READ",
      [
        "storage",
        "002a4c81",
        null,
        "string"
      ]
    ],
    [
      "00b331c0",
      "READ",
      [
        "storage",
        "002bc72d",
        null,
        "string"
      ]
    ],
    [
      "00b331c0",
      "READ",
      [
        "storage",
        "002bc73d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b32d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32d2c.md#insn-00b32d58) · [`00b32d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32d2c.md#insn-00b32d60) · [`00b32d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32d2c.md#insn-00b32d68)
- 新版 [`00b33180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33154.md#insn-00b33180) · [`00b33188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33154.md#insn-00b33188) · [`00b33190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33154.md#insn-00b33190)

~~~diff
- 00b32d58 ["INT_ADD", "register:40f0:8", ["const:b32d58:8", "const:4:8"]]
- 00b32d58 ["CALL", null, ["callee:00588e6c:8"]]
+ 00b33180 ["INT_ADD", "register:40f0:8", ["const:b33180:8", "const:4:8"]]
+ 00b33180 ["CALL", null, ["callee:00588e6c:8"]]
- 00b32d58 bytes 3558e997
+ 00b33180 bytes 3b57e997
- 00b32d60 ["INT_ADD", "register:40f0:8", ["const:b32d60:8", "const:4:8"]]
- 00b32d60 ["CALL", null, ["callee:0058915c:8"]]
+ 00b33188 ["INT_ADD", "register:40f0:8", ["const:b33188:8", "const:4:8"]]
+ 00b33188 ["CALL", null, ["callee:0058915c:8"]]
- 00b32d60 bytes ef58e997
+ 00b33188 bytes f557e997
- 00b32d68 ["COPY", "tmp:0:8", ["const:ba5:8"]]
- 00b32d68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b32d68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b32d68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b33190 ["COPY", "tmp:0:8", ["const:c81:8"]]
+ 00b33190 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b33190 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b33190 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b32d68 bytes 29952e91
+ 00b33190 bytes 29053291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d2b3d9680778868383ed4263ec9487f"></a>

### [`00b32ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32ef8.md) → [`00b33320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33320.md) FUN_00b33320

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00aad4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aad4a0.md) [`00aadd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadd7c.md) · 呼出先 12件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 2件 [`00aad69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aad/00aad69c.md) [`00aadf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aad/00aadf78.md) · 呼出先 12件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.33% / 新版 88.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b33378",
      "incomplete_value": true,
      "site": "00b33388",
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
                "const:c81:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b32f50",
      "incomplete_value": true,
      "site": "00b32f60",
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
                "const:ba5:8"
              ]
            ]
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
      "definition_site": "00b333a4",
      "incomplete_value": true,
      "site": "00b333ac",
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
                "const:120:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b32f7c",
      "incomplete_value": true,
      "site": "00b32f84",
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
                "const:e0:8"
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
      "definition_site": "00b333a0",
      "incomplete_value": true,
      "site": "00b333b0",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b32f78",
      "incomplete_value": true,
      "site": "00b32f88",
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
                "const:20:8"
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
      "00b33378",
      "READ",
      [
        "storage",
        "002a4ba5",
        null,
        "string"
      ]
    ],
    [
      "00b333a0",
      "READ",
      [
        "storage",
        "002b3400",
        null,
        "string"
      ]
    ],
    [
      "00b333a0",
      "READ",
      [
        "storage",
        "002b3410",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b33378",
      "READ",
      [
        "storage",
        "002a4c81",
        null,
        "string"
      ]
    ],
    [
      "00b333a0",
      "READ",
      [
        "storage",
        "002b3440",
        null,
        "string"
      ]
    ],
    [
      "00b333a0",
      "READ",
      [
        "storage",
        "002b3450",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b32f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32ef8.md#insn-00b32f38) · [`00b32f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32ef8.md#insn-00b32f40) · [`00b32f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b32/00b32ef8.md#insn-00b32f48)
- 新版 [`00b33360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33320.md#insn-00b33360) · [`00b33368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33320.md#insn-00b33368) · [`00b33370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33320.md#insn-00b33370)

~~~diff
- 00b32f38 ["INT_ADD", "register:40f0:8", ["const:b32f38:8", "const:4:8"]]
- 00b32f38 ["CALL", null, ["callee:00588e6c:8"]]
+ 00b33360 ["INT_ADD", "register:40f0:8", ["const:b33360:8", "const:4:8"]]
+ 00b33360 ["CALL", null, ["callee:00588e6c:8"]]
- 00b32f38 bytes bd57e997
+ 00b33360 bytes c356e997
- 00b32f40 ["INT_ADD", "register:40f0:8", ["const:b32f40:8", "const:4:8"]]
- 00b32f40 ["CALL", null, ["callee:0058915c:8"]]
+ 00b33368 ["INT_ADD", "register:40f0:8", ["const:b33368:8", "const:4:8"]]
+ 00b33368 ["CALL", null, ["callee:0058915c:8"]]
- 00b32f40 bytes 7758e997
+ 00b33368 bytes 7d57e997
- 00b32f48 ["COPY", "tmp:0:8", ["const:ba5:8"]]
- 00b32f48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b32f48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b32f48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b33370 ["COPY", "tmp:0:8", ["const:c81:8"]]
+ 00b33370 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b33370 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b33370 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b32f48 bytes 29952e91
+ 00b33370 bytes 29053291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-282b64b145671fe6abb5215061936a7d"></a>

### [`00b3315c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b3315c.md) → [`00b33584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33584.md) FUN_00b33584

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) · 呼出先 9件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) · 呼出先 9件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.06% / 新版 88.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b335cc",
      "incomplete_value": true,
      "site": "00b335dc",
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
                "const:d79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b331a4",
      "incomplete_value": true,
      "site": "00b331b4",
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
                "const:d39:8"
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
      "definition_site": "00b335d0",
      "incomplete_value": true,
      "site": "00b335f4",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b331a8",
      "incomplete_value": true,
      "site": "00b331cc",
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
                "const:a:8"
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
      "definition_site": "00b335e0",
      "incomplete_value": true,
      "site": "00b335f8",
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
                "const:a90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b331b8",
      "incomplete_value": true,
      "site": "00b331d0",
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
                "const:a50:8"
              ]
            ]
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
      "00b335cc",
      "READ",
      [
        "storage",
        "002bbd39",
        null,
        "string"
      ]
    ],
    [
      "00b335d0",
      "READ",
      [
        "storage",
        "002bbd43",
        null,
        "string"
      ]
    ],
    [
      "00b335e0",
      "READ",
      [
        "storage",
        "002c2a50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b335cc",
      "READ",
      [
        "storage",
        "002bbd79",
        null,
        "string"
      ]
    ],
    [
      "00b335d0",
      "READ",
      [
        "storage",
        "002bbd83",
        null,
        "string"
      ]
    ],
    [
      "00b335e0",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b33180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b3315c.md#insn-00b33180) · [`00b33188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b3315c.md#insn-00b33188) · [`00b33194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b3315c.md#insn-00b33194)
- 新版 [`00b335a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33584.md#insn-00b335a8) · [`00b335b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33584.md#insn-00b335b0) · [`00b335bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33584.md#insn-00b335bc)

~~~diff
- 00b33180 ["INT_ADD", "register:40f0:8", ["const:b33180:8", "const:4:8"]]
- 00b33180 ["CALL", null, ["callee:00588e6c:8"]]
+ 00b335a8 ["INT_ADD", "register:40f0:8", ["const:b335a8:8", "const:4:8"]]
+ 00b335a8 ["CALL", null, ["callee:00588e6c:8"]]
- 00b33180 bytes 2b57e997
+ 00b335a8 bytes 3156e997
- 00b33188 ["INT_ADD", "register:40f0:8", ["const:b33188:8", "const:4:8"]]
- 00b33188 ["CALL", null, ["callee:0058915c:8"]]
+ 00b335b0 ["INT_ADD", "register:40f0:8", ["const:b335b0:8", "const:4:8"]]
+ 00b335b0 ["CALL", null, ["callee:0058915c:8"]]
- 00b33188 bytes e557e997
+ 00b335b0 bytes eb56e997
- 00b33194 ["INT_ADD", "register:40f0:8", ["const:b33194:8", "const:4:8"]]
- 00b33194 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b335bc ["INT_ADD", "register:40f0:8", ["const:b335bc:8", "const:4:8"]]
+ 00b335bc ["CALL", null, ["callee:00c57e90:8"]]
- 00b33194 bytes 3f920494
+ 00b335bc bytes 35920494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db55a6afacdbd5871fd9c6b573f38381"></a>

### [`00b332a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b332a4.md) → [`00b336cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b336cc.md) _INIT_264

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 48.08% / 新版 48.08%

CFGの説明率　旧版 55.88% / 新版 48.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 45件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b332d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b332e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b332ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b332d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b332e0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b332e8",
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
      "00b336fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b33708",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b33710",
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

- 旧版 [`00b332d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b332a4.md#insn-00b332d4) · [`00b332e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b332a4.md#insn-00b332e8) · [`00b332ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b332a4.md#insn-00b332ec)

~~~diff
- 00b332d4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b332d4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b332d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b332d4 bytes a9831ff8
- 00b332e8 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b332e8 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00b332e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b332e8 bytes ea130278
- 00b332ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b332ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b332ec bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4599db21cacc9a9855dfa96a29171ed5"></a>

### [`00b336b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b336b4.md) → [`00b33adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33adc.md) FUN_00b33adc

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0043f5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f5d8.md) · 呼出先 10件 [`0046ca14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca14.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 1件 [`0043f618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f618.md) · 呼出先 10件 [`0046ca54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca54.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.86% / 新版 64.86%

CFGの説明率　旧版 37.93% / 新版 40.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33730"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33738"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33760"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b33708",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b3370c",
      "PARAM",
      [
        "storage",
        "00ca4870",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b33728",
      "READ",
      [
        "storage",
        "002b24fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b33b30",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ],
    [
      "00b33b34",
      "PARAM",
      [
        "storage",
        "00ca4c70",
        null,
        "undefined8"
      ]
    ],
    [
      "00b33b50",
      "READ",
      [
        "storage",
        "002b253c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b33730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b336b4.md#insn-00b33730) · [`00b33738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b336b4.md#insn-00b33738) · [`00b33760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b336b4.md#insn-00b33760)

~~~diff
- 00b33730 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b33730 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:18:8"]]
- 00b33730 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b33730 bytes e8630039
- 00b33738 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b33738 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:19:8"]]
- 00b33738 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b33738 bytes e99301f8
- 00b33760 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b33760 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b33760 bytes e00b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d573a93eca966176f1aa5a44a1c0d74"></a>

### [`00b33950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33950.md) → [`00b33d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33d78.md) FUN_00b33d78

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) [`0043f4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f4f4.md) · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 2件 [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`0043f534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f534.md) · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

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
      "definition_site": "00b33dcc",
      "incomplete_value": true,
      "site": "00b33dcc",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:90b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b339a4",
      "incomplete_value": true,
      "site": "00b339a4",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:83e:8"
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
      "00b33db4",
      "READ",
      [
        "storage",
        "002a283e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b33db4",
      "READ",
      [
        "storage",
        "002a290b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3396c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33950.md#insn-00b3396c) · [`00b33974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33950.md#insn-00b33974) · [`00b33980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33950.md#insn-00b33980)
- 新版 [`00b33d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33d78.md#insn-00b33d94) · [`00b33d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33d78.md#insn-00b33d9c) · [`00b33da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33d78.md#insn-00b33da8)

~~~diff
- 00b3396c ["INT_ADD", "register:40f0:8", ["const:b3396c:8", "const:4:8"]]
- 00b3396c ["CALL", null, ["callee:00588e6c:8"]]
+ 00b33d94 ["INT_ADD", "register:40f0:8", ["const:b33d94:8", "const:4:8"]]
+ 00b33d94 ["CALL", null, ["callee:00588e6c:8"]]
- 00b3396c bytes 3055e997
+ 00b33d94 bytes 3654e997
- 00b33974 ["INT_ADD", "register:40f0:8", ["const:b33974:8", "const:4:8"]]
- 00b33974 ["CALL", null, ["callee:0058915c:8"]]
+ 00b33d9c ["INT_ADD", "register:40f0:8", ["const:b33d9c:8", "const:4:8"]]
+ 00b33d9c ["CALL", null, ["callee:0058915c:8"]]
- 00b33974 bytes ea55e997
+ 00b33d9c bytes f054e997
- 00b33980 ["COPY", "tmp:0:8", ["const:83e:8"]]
- 00b33980 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b33980 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b33980 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b33da8 ["COPY", "tmp:0:8", ["const:90b:8"]]
+ 00b33da8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b33da8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b33da8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b33980 bytes 29f92091
+ 00b33da8 bytes 292d2491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b80de6b3c1454fd9543660fdee2b728f"></a>

### [`00b33a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33a68.md) → [`00b33e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33e90.md) _INIT_265

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00b33ecc",
      "incomplete_value": true,
      "site": "00b33ee8",
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
      "definition_site": "00b33aa4",
      "incomplete_value": true,
      "site": "00b33ac0",
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
      "definition_site": "00b33ef0",
      "incomplete_value": true,
      "site": "00b33f0c",
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
      "definition_site": "00b33ac8",
      "incomplete_value": true,
      "site": "00b33ae4",
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
      "definition_site": "00b33f10",
      "incomplete_value": true,
      "site": "00b33f2c",
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
      "definition_site": "00b33ae8",
      "incomplete_value": true,
      "site": "00b33b04",
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
      "00b33ecc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00b33ef0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00b33f10",
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
      "00b33ecc",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b33ef0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b33f10",
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

- 旧版 [`00b33bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33a68.md#insn-00b33bc8) · [`00b33c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33a68.md#insn-00b33c9c) · [`00b33a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33a68.md#insn-00b33a94)
- 新版 [`00b33ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33e90.md#insn-00b33ff0) · [`00b340c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33e90.md#insn-00b340c4) · [`00b33ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b33/00b33e90.md#insn-00b33ebc)

~~~diff
- 00b33bc8 ["INT_ADD", "register:40f0:8", ["const:b33bc8:8", "const:4:8"]]
- 00b33bc8 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00b33ff0 ["INT_ADD", "register:40f0:8", ["const:b33ff0:8", "const:4:8"]]
+ 00b33ff0 ["CALL", null, ["callee:0043b7f8:8"]]
- 00b33bc8 bytes fc1ee497
+ 00b33ff0 bytes 021ee497
- 00b33c9c ["INT_ADD", "register:40f0:8", ["const:b33c9c:8", "const:4:8"]]
- 00b33c9c ["CALL", null, ["callee:00c57e30:8"]]
+ 00b340c4 ["INT_ADD", "register:40f0:8", ["const:b340c4:8", "const:4:8"]]
+ 00b340c4 ["CALL", null, ["callee:00c57e30:8"]]
- 00b33c9c bytes 658f0494
+ 00b340c4 bytes 5b8f0494
- 00b33a94 ["COPY", "tmp:0:8", ["const:b30:8"]]
- 00b33a94 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00b33a94 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00b33a94 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00b33ebc ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 00b33ebc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00b33ebc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00b33ebc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00b33a94 bytes 73c22c91
+ 00b33ebc bytes 73c23c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5666539fd8dd2290f3d17ca056453be"></a>

### [`00b33e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33e58.md) → [`00b34280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34280.md) FUN_00b34280

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b1610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1610.md) · 呼出先 2件 [`00b34370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34370.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005b1650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1650.md) · 呼出先 2件 [`00b34798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34798.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b342e8",
      "incomplete_value": false,
      "site": "00b342f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1124000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b33ec0",
      "incomplete_value": false,
      "site": "00b33ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1124000:8"
          ],
          [
            "leaf",
            "const:b50:8"
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
      "00b342e8",
      "PARAM",
      [
        "storage",
        "01124b50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b342e8",
      "PARAM",
      [
        "storage",
        "01124f50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b33ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33e58.md#insn-00b33ecc) · [`00b33e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33e58.md#insn-00b33e90) · [`00b33eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33e58.md#insn-00b33eb8)
- 新版 [`00b342f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34280.md#insn-00b342f4) · [`00b342b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34280.md#insn-00b342b8) · [`00b342e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34280.md#insn-00b342e0)

~~~diff
- 00b33ecc ["INT_ADD", "register:40f0:8", ["const:b33ecc:8", "const:4:8"]]
- 00b33ecc ["CALL", null, ["callee:00b34798:8"]]
+ 00b342f4 ["INT_ADD", "register:40f0:8", ["const:b342f4:8", "const:4:8"]]
+ 00b342f4 ["CALL", null, ["callee:00b34798:8"]]
- 00b33ecc bytes 29010094
+ 00b342f4 bytes 29010094
- 00b33e90 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b33e90 ["INT_ADD", "register:40f0:8", ["const:b33e90:8", "const:4:8"]]
- 00b33e90 ["CALLIND", null, ["register:0:8"]]
+ 00b342b8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b342b8 ["INT_ADD", "register:40f0:8", ["const:b342b8:8", "const:4:8"]]
+ 00b342b8 ["CALLIND", null, ["register:0:8"]]
- 00b33e90 bytes 20013fd6
+ 00b342b8 bytes 20013fd6
- 00b33eb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b33eb8 ["INT_ADD", "register:40f0:8", ["const:b33eb8:8", "const:4:8"]]
- 00b33eb8 ["CALLIND", null, ["register:0:8"]]
+ 00b342e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b342e0 ["INT_ADD", "register:40f0:8", ["const:b342e0:8", "const:4:8"]]
+ 00b342e0 ["CALLIND", null, ["register:0:8"]]
- 00b33eb8 bytes 00013fd6
+ 00b342e0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d279ea1761f6f4cb4e4bebfbe4d35bf"></a>

### [`00b33f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33f20.md) → [`00b34348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34348.md) FUN_00b34348

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b1610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1610.md) · 呼出先 2件 [`00b344d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b344d8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005b1650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1650.md) · 呼出先 2件 [`00b34900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34900.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b343b0",
      "incomplete_value": false,
      "site": "00b343bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1124000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b33f88",
      "incomplete_value": false,
      "site": "00b33f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1124000:8"
          ],
          [
            "leaf",
            "const:b80:8"
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
      "00b343b0",
      "PARAM",
      [
        "storage",
        "01124b80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b343b0",
      "PARAM",
      [
        "storage",
        "01124f80",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b33f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33f20.md#insn-00b33f94) · [`00b33f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33f20.md#insn-00b33f58) · [`00b33f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33f20.md#insn-00b33f80)
- 新版 [`00b343bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34348.md#insn-00b343bc) · [`00b34380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34348.md#insn-00b34380) · [`00b343a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34348.md#insn-00b343a8)

~~~diff
- 00b33f94 ["INT_ADD", "register:40f0:8", ["const:b33f94:8", "const:4:8"]]
- 00b33f94 ["CALL", null, ["callee:00b34900:8"]]
+ 00b343bc ["INT_ADD", "register:40f0:8", ["const:b343bc:8", "const:4:8"]]
+ 00b343bc ["CALL", null, ["callee:00b34900:8"]]
- 00b33f94 bytes 51010094
+ 00b343bc bytes 51010094
- 00b33f58 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b33f58 ["INT_ADD", "register:40f0:8", ["const:b33f58:8", "const:4:8"]]
- 00b33f58 ["CALLIND", null, ["register:0:8"]]
+ 00b34380 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b34380 ["INT_ADD", "register:40f0:8", ["const:b34380:8", "const:4:8"]]
+ 00b34380 ["CALLIND", null, ["register:0:8"]]
- 00b33f58 bytes 20013fd6
+ 00b34380 bytes 20013fd6
- 00b33f80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b33f80 ["INT_ADD", "register:40f0:8", ["const:b33f80:8", "const:4:8"]]
- 00b33f80 ["CALLIND", null, ["register:0:8"]]
+ 00b343a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b343a8 ["INT_ADD", "register:40f0:8", ["const:b343a8:8", "const:4:8"]]
+ 00b343a8 ["CALLIND", null, ["register:0:8"]]
- 00b33f80 bytes 00013fd6
+ 00b343a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efc55e543d9b1d478a0e6b6812834acc"></a>

### [`00b33fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33fe8.md) → [`00b34410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34410.md) FUN_00b34410

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b1610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1610.md) · 呼出先 13件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0087a2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a2c8.md) [`0087b37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b37c.md) [`00b34640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34640.md) [`00b3483c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b3483c.md)
- 新版 呼出元 1件 [`005b1650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1650.md) · 呼出先 13件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0087a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a308.md) [`0087b3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md) [`00b34a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34a68.md) [`00b34c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34c64.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.89% / 新版 94.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b34458",
      "incomplete_value": true,
      "site": "00b34458",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:686:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b34030",
      "incomplete_value": true,
      "site": "00b34030",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:5b9:8"
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
      "definition_site": "00b34544",
      "incomplete_value": false,
      "site": "00b3454c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b3411c",
      "incomplete_value": false,
      "site": "00b34124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b344c8",
      "incomplete_value": false,
      "site": "00b344d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:d94:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b340a0",
      "incomplete_value": false,
      "site": "00b340a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:d54:8"
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
      "00b34448",
      "READ",
      [
        "storage",
        "002a05b9",
        null,
        "string"
      ]
    ],
    [
      "00b344c8",
      "PARAM",
      [
        "storage",
        "002bbd54",
        null,
        "string"
      ]
    ],
    [
      "00b34508",
      "PARAM",
      [
        "storage",
        "002b95aa",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b34448",
      "READ",
      [
        "storage",
        "002a0686",
        null,
        "string"
      ]
    ],
    [
      "00b344c8",
      "PARAM",
      [
        "storage",
        "002bbd94",
        null,
        "string"
      ]
    ],
    [
      "00b34508",
      "PARAM",
      [
        "storage",
        "002b95ea",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b340a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33fe8.md#insn-00b340a8) · [`00b340e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33fe8.md#insn-00b340e8) · [`00b3401c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33fe8.md#insn-00b3401c)
- 新版 [`00b344d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34410.md#insn-00b344d0) · [`00b34510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34410.md#insn-00b34510) · [`00b34444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34410.md#insn-00b34444)

~~~diff
- 00b340a8 ["INT_ADD", "register:40f0:8", ["const:b340a8:8", "const:4:8"]]
- 00b340a8 ["CALL", null, ["callee:00b34a68:8"]]
+ 00b344d0 ["INT_ADD", "register:40f0:8", ["const:b344d0:8", "const:4:8"]]
+ 00b344d0 ["CALL", null, ["callee:00b34a68:8"]]
- 00b340a8 bytes 66010094
+ 00b344d0 bytes 66010094
- 00b340e8 ["INT_ADD", "register:40f0:8", ["const:b340e8:8", "const:4:8"]]
- 00b340e8 ["CALL", null, ["callee:00b34c64:8"]]
+ 00b34510 ["INT_ADD", "register:40f0:8", ["const:b34510:8", "const:4:8"]]
+ 00b34510 ["CALL", null, ["callee:00b34c64:8"]]
- 00b340e8 bytes d5010094
+ 00b34510 bytes d5010094
- 00b3401c ["COPY", "tmp:0:8", ["const:5b9:8"]]
- 00b3401c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b3401c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b3401c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b34444 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 00b34444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b34444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b34444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b3401c bytes 08e51691
+ 00b34444 bytes 08191a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a876eb528583faf449844bba60bcfe6c"></a>

### [`00b34a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34a40.md) → [`00b34e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34e68.md) FUN_00b34e68

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b34e7c",
      "incomplete_value": false,
      "site": "00b34e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b34a54",
      "incomplete_value": false,
      "site": "00b34a58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "00b34e80",
      "DATA",
      [
        "storage",
        "00c8efe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b34e80",
      "DATA",
      [
        "storage",
        "00c8f3e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b34a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34a40.md#insn-00b34a4c) · [`00b34a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34a40.md#insn-00b34a50) · [`00b34a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34a40.md#insn-00b34a54)
- 新版 [`00b34e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34e68.md#insn-00b34e74) · [`00b34e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34e68.md#insn-00b34e78) · [`00b34e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34e68.md#insn-00b34e7c)

~~~diff
- 00b34a4c ["INT_ADD", "register:40f0:8", ["const:b34a4c:8", "const:4:8"]]
- 00b34a4c ["CALL", null, ["callee:00c57e90:8"]]
+ 00b34e74 ["INT_ADD", "register:40f0:8", ["const:b34e74:8", "const:4:8"]]
+ 00b34e74 ["CALL", null, ["callee:00c57e90:8"]]
- 00b34a4c bytes 118c0494
+ 00b34e74 bytes 078c0494
- 00b34a50 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00b34e78 ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00b34a50 bytes c80a00d0
+ 00b34e78 bytes c80a00f0
- 00b34a54 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00b34a54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b34a54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b34a54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b34e7c ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 00b34e7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b34e7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b34e7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b34a54 bytes 08a13f91
+ 00b34e7c bytes 08a10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a9d03f4b3973cdbe7c45e95ddbf4a38"></a>

### [`00b34a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34a64.md) → [`00b34e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34e8c.md) FUN_00b34e8c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b34e90",
      "incomplete_value": false,
      "site": "00b34e94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b34a68",
      "incomplete_value": false,
      "site": "00b34a6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "00b34e94",
      "DATA",
      [
        "storage",
        "00c8efe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b34e94",
      "DATA",
      [
        "storage",
        "00c8f3e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b34a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34a64.md#insn-00b34a64) · [`00b34a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34a64.md#insn-00b34a68)
- 新版 [`00b34e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34e8c.md#insn-00b34e8c) · [`00b34e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34e8c.md#insn-00b34e90)

~~~diff
- 00b34a64 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00b34e8c ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00b34a64 bytes c80a00d0
+ 00b34e8c bytes c80a00f0
- 00b34a68 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00b34a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b34a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b34a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b34e90 ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 00b34e90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b34e90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b34e90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b34a68 bytes 08a13f91
+ 00b34e90 bytes 08a10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85108d911ce84265b485a6db283fd4ba"></a>

### [`00b34f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34f58.md) → [`00b35380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35380.md) FUN_00b35380

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b35394",
      "incomplete_value": false,
      "site": "00b35398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b34f6c",
      "incomplete_value": false,
      "site": "00b34f70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00b35398",
      "DATA",
      [
        "storage",
        "00c8f058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b35398",
      "DATA",
      [
        "storage",
        "00c8f458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b34f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34f58.md#insn-00b34f64) · [`00b34f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34f58.md#insn-00b34f6c)
- 新版 [`00b3538c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35380.md#insn-00b3538c) · [`00b35394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35380.md#insn-00b35394)

~~~diff
- 00b34f64 ["INT_ADD", "register:40f0:8", ["const:b34f64:8", "const:4:8"]]
- 00b34f64 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b3538c ["INT_ADD", "register:40f0:8", ["const:b3538c:8", "const:4:8"]]
+ 00b3538c ["CALL", null, ["callee:00c57e90:8"]]
- 00b34f64 bytes cb8a0494
+ 00b3538c bytes c18a0494
- 00b34f6c ["COPY", "tmp:0:8", ["const:58:8"]]
- 00b34f6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b34f6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b34f6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b35394 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 00b35394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b35394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b35394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b34f6c bytes 08610191
+ 00b35394 bytes 08611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e5a5190dcb5cff81b8ef25a15e03d92"></a>

### [`00b34f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34f94.md) → [`00b353bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b353bc.md) FUN_00b353bc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 98.13% / 新版 98.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b354b0",
      "incomplete_value": true,
      "site": "00b354b0",
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
      "definition_site": "00b35088",
      "incomplete_value": true,
      "site": "00b35088",
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
      "00b354a4",
      "READ",
      [
        "storage",
        "01124b70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b354a4",
      "READ",
      [
        "storage",
        "01124f70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b34fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34f94.md#insn-00b34fc0) · [`00b34fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34f94.md#insn-00b34fd8) · [`00b34fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34f94.md#insn-00b34fec)
- 新版 [`00b353e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b353bc.md#insn-00b353e8) · [`00b35400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b353bc.md#insn-00b35400) · [`00b35414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b353bc.md#insn-00b35414)

~~~diff
- 00b34fc0 ["INT_ADD", "register:40f0:8", ["const:b34fc0:8", "const:4:8"]]
- 00b34fc0 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b353e8 ["INT_ADD", "register:40f0:8", ["const:b353e8:8", "const:4:8"]]
+ 00b353e8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b34fc0 bytes 90950494
+ 00b353e8 bytes 86950494
- 00b34fd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b34fd8 ["INT_ADD", "register:40f0:8", ["const:b34fd8:8", "const:4:8"]]
- 00b34fd8 ["CALLIND", null, ["register:0:8"]]
+ 00b35400 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b35400 ["INT_ADD", "register:40f0:8", ["const:b35400:8", "const:4:8"]]
+ 00b35400 ["CALLIND", null, ["register:0:8"]]
- 00b34fd8 bytes 00013fd6
+ 00b35400 bytes 00013fd6
- 00b34fec ["INT_ADD", "register:40f0:8", ["const:b34fec:8", "const:4:8"]]
- 00b34fec ["CALL", null, ["callee:00c5aa10:8"]]
+ 00b35414 ["INT_ADD", "register:40f0:8", ["const:b35414:8", "const:4:8"]]
+ 00b35414 ["CALL", null, ["callee:00c5aa10:8"]]
- 00b34fec bytes 89950494
+ 00b35414 bytes 7f950494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f63e62c23787f836d069bf32f44c382f"></a>

### [`00b351e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b351e0.md) → [`00b35608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35608.md) _INIT_266

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b33df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33df8.md) [`00b33e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33e28.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b34220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34220.md) [`00b34250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34250.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 52.38% / 新版 52.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b35630",
      "incomplete_value": false,
      "site": "00b35630",
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
                "const:1124000:8"
              ],
              [
                "leaf",
                "const:f50:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b35208",
      "incomplete_value": false,
      "site": "00b35208",
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
                "const:1124000:8"
              ],
              [
                "leaf",
                "const:b50:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b3564c",
      "incomplete_value": false,
      "site": "00b3564c",
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
                "const:1124000:8"
              ],
              [
                "leaf",
                "const:f80:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b35224",
      "incomplete_value": false,
      "site": "00b35224",
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
                "const:1124000:8"
              ],
              [
                "leaf",
                "const:b80:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "00b35628",
      "incomplete_value": false,
      "site": "00b35634",
      "value": [
        "leaf",
        "const:b34220:8"
      ]
    },
    "old": {
      "definition_site": "00b35200",
      "incomplete_value": false,
      "site": "00b3520c",
      "value": [
        "leaf",
        "const:b33df8:8"
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
      "00b35620",
      "PARAM",
      [
        "storage",
        "01124b50",
        null,
        null
      ]
    ],
    [
      "unmatched:00b35200",
      "PARAM",
      [
        "storage",
        "00b33df8",
        null,
        null
      ]
    ],
    [
      "00b3562c",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b35620",
      "PARAM",
      [
        "storage",
        "01124f50",
        null,
        null
      ]
    ],
    [
      "00b35628",
      "PARAM",
      [
        "storage",
        "00b34220",
        null,
        null
      ]
    ],
    [
      "00b3562c",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3520c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b351e0.md#insn-00b3520c) · [`00b351f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b351e0.md#insn-00b351f0) · [`00b351f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b351e0.md#insn-00b351f4)
- 新版 [`00b35634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35608.md#insn-00b35634) · [`00b35618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35608.md#insn-00b35618)

~~~diff
- 00b3520c ["INT_ADD", "register:40f0:8", ["const:b3520c:8", "const:4:8"]]
- 00b3520c ["CALL", null, ["callee:00c57e30:8"]]
+ 00b35634 ["INT_ADD", "register:40f0:8", ["const:b35634:8", "const:4:8"]]
+ 00b35634 ["CALL", null, ["callee:00c57e30:8"]]
- 00b3520c bytes 098a0494
+ 00b35634 bytes ff890494
- 00b351f0 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00b351f0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00b351f0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00b351f0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00b35618 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 00b35618 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00b35618 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00b35618 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00b351f0 bytes 73422e91
+ 00b35618 bytes 73423e91
- 00b351f4 ["COPY", "register:4008:8", ["const:1124000:8"]]
- 00b351f4 bytes 612f00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f03b73368588cb473012c1aade6f1b86"></a>

### [`00b35234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35234.md) → [`00b3565c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b3565c.md) FUN_00b3565c

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0066d050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d050.md) · 呼出先 12件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`0066d090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d090.md) · 呼出先 12件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.28% / 新版 82.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b356b8",
      "incomplete_value": true,
      "site": "00b356c8",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:cb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b35290",
      "incomplete_value": true,
      "site": "00b352a0",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:c78:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b356cc",
      "incomplete_value": true,
      "site": "00b356dc",
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
                "const:290:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b352a4",
      "incomplete_value": true,
      "site": "00b352b4",
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
                "const:250:8"
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
      "definition_site": "00b356bc",
      "incomplete_value": true,
      "site": "00b356e4",
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
                "const:c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b35294",
      "incomplete_value": true,
      "site": "00b352bc",
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
                "const:c:8"
              ]
            ]
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
      "00b356b8",
      "READ",
      [
        "storage",
        "002bac78",
        null,
        "string"
      ]
    ],
    [
      "00b356bc",
      "READ",
      [
        "storage",
        "002bac84",
        null,
        "string"
      ]
    ],
    [
      "00b356cc",
      "READ",
      [
        "storage",
        "002c3250",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b356b8",
      "READ",
      [
        "storage",
        "002bacb8",
        null,
        "string"
      ]
    ],
    [
      "00b356bc",
      "READ",
      [
        "storage",
        "002bacc4",
        null,
        "string"
      ]
    ],
    [
      "00b356cc",
      "READ",
      [
        "storage",
        "002c3290",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b35258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35234.md#insn-00b35258) · [`00b3526c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35234.md#insn-00b3526c) · [`00b35270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35234.md#insn-00b35270)
- 新版 [`00b35680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b3565c.md#insn-00b35680) · [`00b35694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b3565c.md#insn-00b35694) · [`00b35698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b3565c.md#insn-00b35698)

~~~diff
- 00b35258 ["INT_ADD", "register:40f0:8", ["const:b35258:8", "const:4:8"]]
- 00b35258 ["CALL", null, ["callee:00588e6c:8"]]
+ 00b35680 ["INT_ADD", "register:40f0:8", ["const:b35680:8", "const:4:8"]]
+ 00b35680 ["CALL", null, ["callee:00588e6c:8"]]
- 00b35258 bytes f54ee997
+ 00b35680 bytes fb4de997
- 00b3526c ["INT_ADD", "register:40f0:8", ["const:b3526c:8", "const:4:8"]]
- 00b3526c ["CALL", null, ["callee:005898d0:8"]]
+ 00b35694 ["INT_ADD", "register:40f0:8", ["const:b35694:8", "const:4:8"]]
+ 00b35694 ["CALL", null, ["callee:005898d0:8"]]
- 00b3526c bytes 8951e997
+ 00b35694 bytes 8f50e997
- 00b35270 ["INT_ADD", "register:40f0:8", ["const:b35270:8", "const:4:8"]]
- 00b35270 ["CALL", null, ["callee:0058915c:8"]]
+ 00b35698 ["INT_ADD", "register:40f0:8", ["const:b35698:8", "const:4:8"]]
+ 00b35698 ["CALL", null, ["callee:0058915c:8"]]
- 00b35270 bytes ab4fe997
+ 00b35698 bytes b14ee997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0145e74053ff93526e4e2ab3252d21e"></a>

### [`00b353c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b353c0.md) → [`00b357e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b357e8.md) FUN_00b357e8

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0066d09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d09c.md) [`0066d0c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d0c8.md) [`00763c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00763/00763c50.md) · 呼出先 12件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 3件 [`0066d0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d0dc.md) [`0066d108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d108.md) [`00763c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00763/00763c90.md) · 呼出先 12件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.81% / 新版 84.81%

CFGの説明率　旧版 78.57% / 新版 73.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b35830",
      "incomplete_value": true,
      "site": "00b35848",
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
                "const:2a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b35408",
      "incomplete_value": true,
      "site": "00b35420",
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
                "const:260:8"
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
      "definition_site": "00b3584c",
      "incomplete_value": true,
      "site": "00b35860",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:cd5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b35424",
      "incomplete_value": true,
      "site": "00b35438",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:c95:8"
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
      "definition_site": "00b3584c",
      "incomplete_value": true,
      "site": "00b35860",
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
      "definition_site": "00b35424",
      "incomplete_value": true,
      "site": "00b35438",
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
      "00b35830",
      "READ",
      [
        "storage",
        "002c3260",
        null,
        null
      ]
    ],
    [
      "00b3584c",
      "READ",
      [
        "storage",
        "002bac95",
        null,
        "string"
      ]
    ],
    [
      "00b3584c",
      "READ",
      [
        "storage",
        "002baca5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b35830",
      "READ",
      [
        "storage",
        "002c32a0",
        null,
        null
      ]
    ],
    [
      "00b3584c",
      "READ",
      [
        "storage",
        "002bacd5",
        null,
        "string"
      ]
    ],
    [
      "00b3584c",
      "READ",
      [
        "storage",
        "002bace5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b353e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b353c0.md#insn-00b353e4) · [`00b353ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b353c0.md#insn-00b353ec) · [`00b353f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b353c0.md#insn-00b353f8)
- 新版 [`00b3580c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b357e8.md#insn-00b3580c) · [`00b35814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b357e8.md#insn-00b35814) · [`00b35820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b357e8.md#insn-00b35820)

~~~diff
- 00b353e4 ["INT_ADD", "register:40f0:8", ["const:b353e4:8", "const:4:8"]]
- 00b353e4 ["CALL", null, ["callee:00588e6c:8"]]
+ 00b3580c ["INT_ADD", "register:40f0:8", ["const:b3580c:8", "const:4:8"]]
+ 00b3580c ["CALL", null, ["callee:00588e6c:8"]]
- 00b353e4 bytes 924ee997
+ 00b3580c bytes 984de997
- 00b353ec ["INT_ADD", "register:40f0:8", ["const:b353ec:8", "const:4:8"]]
- 00b353ec ["CALL", null, ["callee:0058915c:8"]]
+ 00b35814 ["INT_ADD", "register:40f0:8", ["const:b35814:8", "const:4:8"]]
+ 00b35814 ["CALL", null, ["callee:0058915c:8"]]
- 00b353ec bytes 4c4fe997
+ 00b35814 bytes 524ee997
- 00b353f8 ["INT_ADD", "register:40f0:8", ["const:b353f8:8", "const:4:8"]]
- 00b353f8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b35820 ["INT_ADD", "register:40f0:8", ["const:b35820:8", "const:4:8"]]
+ 00b35820 ["CALL", null, ["callee:00c57e90:8"]]
- 00b353f8 bytes a6890494
+ 00b35820 bytes 9c890494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58dff8e0ced428de05ca71a076eae876"></a>

### [`00b35548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35548.md) → [`00b35970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35970.md) _INIT_267

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 67.23% / 新版 67.23%

CFGの説明率　旧版 54.84% / 新版 45.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_store_alignment` 29件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35578"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b355a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b355c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b35578",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b35584",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b355a0",
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
      "00b359a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b359ac",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b359c8",
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

- 旧版 [`00b35578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35548.md#insn-00b35578) · [`00b355a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35548.md#insn-00b355a0) · [`00b355c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35548.md#insn-00b355c4)

~~~diff
- 00b35578 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b35578 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b35578 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b35578 bytes a9831ff8
- 00b355a0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00b355a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b355a0 bytes e013813c
- 00b355c4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00b355c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b355c4 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eb13daaca51a23636f1b5b888f76a71"></a>

### [`00b358e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b358e4.md) → [`00b35d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35d0c.md) FUN_00b35d0c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0043b694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b694.md) · 呼出先 5件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00b35ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35ad0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`0043b6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b6d4.md) · 呼出先 5件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00b35ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35ef8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 86.81% / 新版 86.81%

CFGの説明率　旧版 34.62% / 新版 34.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35914"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35958"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3595c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b35d38",
      "READ",
      [
        "storage",
        "01124bd8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b35914",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b35e18"
      ]
    ],
    [
      "00b35dec",
      "PARAM",
      [
        "storage",
        "01124bd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b35d38",
      "READ",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b35d3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b35e18"
      ]
    ],
    [
      "00b35dec",
      "PARAM",
      [
        "storage",
        "01124fd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b35914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b358e4.md#insn-00b35914) · [`00b35958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b358e4.md#insn-00b35958) · [`00b3595c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b358e4.md#insn-00b3595c)

~~~diff
- 00b35914 ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
- 00b35914 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b35914 bytes f80600b4
- 00b35958 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b35958 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b35958 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b35958 ["COPY", "register:40a8:8", ["tmp:0:8"]]
- 00b35958 bytes 15018b9a
- 00b3595c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b3595c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3595c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b3595c ["COPY", "register:40d0:8", ["tmp:0:8"]]
- 00b3595c bytes 5a01899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a62ac6a59b905d9462212fecdaf287d4"></a>

### [`00b35ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35ad0.md) → [`00b35ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35ef8.md) FUN_00b35ef8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b358e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b358e4.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00b35d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35d0c.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 93.85% / 新版 93.85%

CFGの説明率　旧版 20.00% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35b4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b35f74"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b35f9c",
      "incomplete_value": true,
      "site": "00b35fa8",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b35b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35ad0.md#insn-00b35b4c) · [`00b35b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35ad0.md#insn-00b35b80) · [`00b35bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35ad0.md#insn-00b35bd0)
- 新版 [`00b35fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35ef8.md#insn-00b35fa8)

~~~diff
- 00b35b4c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b35b4c ["COPY", "tmp:1:8", ["register:40d0:8"]]
- 00b35b4c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b35b4c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b35b4c bytes 5733999a
- 00b35b80 ["INT_ADD", "register:40f0:8", ["const:b35b80:8", "const:4:8"]]
- 00b35b80 ["CALL", null, ["callee:00c58050:8"]]
+ 00b35fa8 ["INT_ADD", "register:40f0:8", ["const:b35fa8:8", "const:4:8"]]
+ 00b35fa8 ["CALL", null, ["callee:00c58050:8"]]
- 00b35b80 bytes 34880494
+ 00b35fa8 bytes 2a880494
- 00b35bd0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b35bd0 ["RETURN", null, ["register:0:8"]]
- 00b35bd0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f84534401770482d5192762ca68e7a6"></a>

### [`00b35bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35bd4.md) → [`00b35ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35ffc.md) _INIT_268

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b358dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b358dc.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b35d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35d04.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b36018",
      "incomplete_value": false,
      "site": "00b36018",
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
                "const:1124000:8"
              ],
              [
                "leaf",
                "const:fd0:8"
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
      "definition_site": "00b35bf0",
      "incomplete_value": false,
      "site": "00b35bf0",
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
                "const:1124000:8"
              ],
              [
                "leaf",
                "const:bd0:8"
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b3601c",
      "incomplete_value": false,
      "site": "00b3601c",
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
                "const:1124000:8"
              ],
              [
                "leaf",
                "const:fd0:8"
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
      "definition_site": "00b35bf4",
      "incomplete_value": false,
      "site": "00b35bf4",
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
                "const:1124000:8"
              ],
              [
                "leaf",
                "const:bd0:8"
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b36020",
      "incomplete_value": false,
      "site": "00b36020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1124000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b35bf8",
      "incomplete_value": false,
      "site": "00b35bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1124000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
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
      "00b36000",
      "PARAM",
      [
        "storage",
        "01124bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b36008",
      "PARAM",
      [
        "storage",
        "00b358dc",
        null,
        null
      ]
    ],
    [
      "00b36014",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b36000",
      "PARAM",
      [
        "storage",
        "01124fd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b36008",
      "PARAM",
      [
        "storage",
        "00b35d04",
        null,
        null
      ]
    ],
    [
      "00b36014",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b35bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35bd4.md#insn-00b35bd8) · [`00b35be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35bd4.md#insn-00b35be0) · [`00b35bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35bd4.md#insn-00b35bec)
- 新版 [`00b36000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35ffc.md#insn-00b36000) · [`00b36008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35ffc.md#insn-00b36008) · [`00b36014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35ffc.md#insn-00b36014)

~~~diff
- 00b35bd8 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 00b35bd8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b35bd8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b35bd8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b36000 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 00b36000 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b36000 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b36000 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b35bd8 bytes 21402f91
+ 00b36000 bytes 21403f91
- 00b35be0 ["COPY", "register:4000:8", ["const:b358dc:8"]]
+ 00b36008 ["COPY", "register:4000:8", ["const:b35d04:8"]]
- 00b35be0 bytes e0e7ff10
+ 00b36008 bytes e0e7ff10
- 00b35bec ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00b35bec ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b35bec ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b35bec ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b36014 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 00b36014 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b36014 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b36014 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b35bec bytes 42402e91
+ 00b36014 bytes 42403e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68c324ae52d0a3bfea0227d9b3f310ce"></a>

### [`00b35c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35c00.md) → [`00b36028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36028.md) FUN_00b36028

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2bdd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bdd8.md) · 呼出先 9件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00b2c200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c200.md) · 呼出先 9件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.12% / 新版 78.12%

CFGの説明率　旧版 22.22% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35c04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35c04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35c08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b35c04",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b35c08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b35c40",
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
      "00b3602c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b36030",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b36068",
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

- 旧版 [`00b35c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35c00.md#insn-00b35c04) · [`00b35c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35c00.md#insn-00b35c08) · [`00b35c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35c00.md#insn-00b35c34)
- 新版 [`00b3605c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36028.md#insn-00b3605c)

~~~diff
- 00b35c04 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b35c04 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b35c04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b35c04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b35c04 bytes fd7b05a9
- 00b35c08 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b35c08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b35c08 bytes f53300f9
- 00b35c34 ["INT_ADD", "register:40f0:8", ["const:b35c34:8", "const:4:8"]]
- 00b35c34 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b3605c ["INT_ADD", "register:40f0:8", ["const:b3605c:8", "const:4:8"]]
+ 00b3605c ["CALL", null, ["callee:00c57e90:8"]]
- 00b35c34 bytes 97870494
+ 00b3605c bytes 8d870494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47416d021130fcabb906f11332bb7f21"></a>

### [`00b35d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35d3c.md) → [`00b36164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36164.md) FUN_00b36164

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005bac90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bac90.md) [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) · 呼出先 10件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 2件 [`005bacd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005bacd0.md) [`0089788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/0089788c.md) · 呼出先 10件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.42% / 新版 77.42%

CFGの説明率　旧版 52.38% / 新版 61.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35d94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35d98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35da4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b35d88",
      "READ",
      [
        "storage",
        "002b7be2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b35d8c",
      "READ",
      [
        "storage",
        "002b7bec",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b35d94",
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
      "00b361b0",
      "READ",
      [
        "storage",
        "002b7c22",
        null,
        "string"
      ]
    ],
    [
      "00b361b4",
      "READ",
      [
        "storage",
        "002b7c2c",
        null,
        "string"
      ]
    ],
    [
      "00b361bc",
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

- 旧版 [`00b35d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35d3c.md#insn-00b35d94) · [`00b35d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35d3c.md#insn-00b35d98) · [`00b35da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35d3c.md#insn-00b35da4)

~~~diff
- 00b35d94 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00b35d94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b35d94 bytes e01b00f9
- 00b35d98 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b35d98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b35d98 bytes 0000803d
- 00b35da4 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b35da4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:8:8"]]
- 00b35da4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b35da4 bytes e8230039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c55653d4c32d9a59a70545e2d0af8b68"></a>

### [`00b3611c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b3611c.md) → [`00b36544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36544.md) _INIT_270

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.28% / 新版 63.28%

CFGの説明率　旧版 55.88% / 新版 55.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3614c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b36160"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b36164"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3614c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b36158",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b36160",
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
      "00b36574",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b36580",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b36588",
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

- 旧版 [`00b3614c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b3611c.md#insn-00b3614c) · [`00b36160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b3611c.md#insn-00b36160) · [`00b36164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b3611c.md#insn-00b36164)

~~~diff
- 00b3614c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b3614c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b3614c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b3614c bytes a9831ff8
- 00b36160 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b36160 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00b36160 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b36160 bytes ea130278
- 00b36164 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b36164 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b36164 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e78e73dd99e7825578977f52906b8930"></a>

### [`00b365cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b365cc.md) → [`00b369f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b369f4.md) FUN_00b369f4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b14d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b14d4.md) · 呼出先 2件 [`00b34370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34370.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005b1514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1514.md) · 呼出先 2件 [`00b34798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34798.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 31.58% / 新版 26.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b365d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b365d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b365d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b365d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b365d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b365e4",
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
      "00b369f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b369fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b36a0c",
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

- 旧版 [`00b365d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b365cc.md#insn-00b365d0) · [`00b365d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b365cc.md#insn-00b365d4) · [`00b365e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b365cc.md#insn-00b365e4)

~~~diff
- 00b365d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b365d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b365d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b365d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b365d0 bytes fd7b04a9
- 00b365d4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b365d4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b365d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b365d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b365d4 bytes f44f05a9
- 00b365e4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b365e4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b365e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b365e4 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37c07359fa79897da14d56a7c89bff07"></a>

### [`00b36694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36694.md) → [`00b36abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36abc.md) FUN_00b36abc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b14d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b14d4.md) · 呼出先 2件 [`00b344d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b344d8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005b1514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1514.md) · 呼出先 2件 [`00b34900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34900.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 47.37% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b366ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b36b14"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b366f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b36afc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b366f8"
      ]
    ],
    [
      "00b36b04",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b366f8"
      ]
    ],
    [
      "unmatched:00b366ec",
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
      "00b36afc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b36b20"
      ]
    ],
    [
      "00b36b04",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b36b20"
      ]
    ],
    [
      "00b36b14",
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

- 旧版 [`00b366ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36694.md#insn-00b366ec) · [`00b366f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36694.md#insn-00b366f4) · [`00b36708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36694.md#insn-00b36708)
- 新版 [`00b36b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36abc.md#insn-00b36b30)

~~~diff
- 00b366ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b366ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b366ec bytes e81300f9
- 00b366f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b366f4 ["INT_ADD", "register:40f0:8", ["const:b366f4:8", "const:4:8"]]
- 00b366f4 ["CALLIND", null, ["register:0:8"]]
- 00b366f4 bytes 00013fd6
- 00b36708 ["INT_ADD", "register:40f0:8", ["const:b36708:8", "const:4:8"]]
- 00b36708 ["CALL", null, ["callee:00b34900:8"]]
+ 00b36b30 ["INT_ADD", "register:40f0:8", ["const:b36b30:8", "const:4:8"]]
+ 00b36b30 ["CALL", null, ["callee:00b34900:8"]]
- 00b36708 bytes 74f7ff97
+ 00b36b30 bytes 74f7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1665f6170cc96ca68fac2888a83d529"></a>

### [`00b3675c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b3675c.md) → [`00b36b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36b84.md) Java_jp_co_ponos_battlecats_MyGoogleSignInListener_onSuccess

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b367a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b36804"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b36bd0"
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
      "00b36bcc",
      "READ",
      [
        "storage",
        "01124c50",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b367a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b36c00"
      ]
    ],
    [
      "unmatched:00b36804",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b36c80"
      ]
    ]
  ],
  "added": [
    [
      "00b36bcc",
      "READ",
      [
        "storage",
        "01125050",
        null,
        "undefined8"
      ]
    ],
    [
      "00b36bd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b36c00"
      ]
    ],
    [
      "00b36c2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b36c80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b367a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b3675c.md#insn-00b367a8) · [`00b36804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b3675c.md#insn-00b36804)
- 新版 [`00b36bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36b84.md#insn-00b36bd0)

~~~diff
- 00b367a8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b367a8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b367a8 bytes 800100b4
- 00b36804 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b36804 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b36804 bytes a1020054
+ 00b36bd0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b36bd0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b36bd0 bytes 800100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96c7dfb5e537947a67e2bac0a2861fe5"></a>

### [`00b36890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36890.md) → [`00b36cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36cb8.md) Java_jp_co_ponos_battlecats_MyGoogleSignInListener_onFailure

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.74% / 新版 76.74%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b368d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b368dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b368e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b36cd8",
      "READ",
      [
        "storage",
        "01124c80",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b368cc",
      "READ",
      [
        "storage",
        "002b8996",
        null,
        null
      ]
    ],
    [
      "unmatched:00b368d0",
      "READ",
      [
        "storage",
        "002c2b10",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b36cd8",
      "READ",
      [
        "storage",
        "01125080",
        null,
        "undefined8"
      ]
    ],
    [
      "00b36cf4",
      "READ",
      [
        "storage",
        "002b89d6",
        null,
        null
      ]
    ],
    [
      "00b36cf8",
      "READ",
      [
        "storage",
        "002c2b50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b368b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36890.md#insn-00b368b4) · [`00b368d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36890.md#insn-00b368d8) · [`00b368dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36890.md#insn-00b368dc)
- 新版 [`00b36cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36cb8.md#insn-00b36cdc)

~~~diff
- 00b368b4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00b368b4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b36cdc ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00b36cdc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b368b4 bytes 330300b4
+ 00b36cdc bytes 330300b4
- 00b368d8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b368d8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b368d8 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:1d:8"]]
- 00b368d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b368d8 bytes 1f740039
- 00b368dc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b368dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b368dc bytes 0000803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a59d23f4d8fe4ccdad84e39979e035b"></a>

### [`00b36968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36968.md) → [`00b36d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36d90.md) Java_jp_co_ponos_battlecats_MyGoogleSignInListener_onCancel

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.45% / 新版 70.45%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b369b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b369b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b369bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b36db0",
      "READ",
      [
        "storage",
        "01124c80",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b369a4",
      "READ",
      [
        "storage",
        "002b14b5",
        null,
        null
      ]
    ],
    [
      "unmatched:00b369a4",
      "READ",
      [
        "storage",
        "002b14c5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b36db0",
      "READ",
      [
        "storage",
        "01125080",
        null,
        "undefined8"
      ]
    ],
    [
      "00b36dcc",
      "READ",
      [
        "storage",
        "002b14f5",
        null,
        null
      ]
    ],
    [
      "00b36dcc",
      "READ",
      [
        "storage",
        "002b1505",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3698c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36968.md#insn-00b3698c) · [`00b369b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36968.md#insn-00b369b0) · [`00b369b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36968.md#insn-00b369b8)
- 新版 [`00b36db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36d90.md#insn-00b36db4)

~~~diff
- 00b3698c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00b3698c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b36db4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00b36db4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b3698c bytes 530300b4
+ 00b36db4 bytes 530300b4
- 00b369b0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b369b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b369b0 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:25:8"]]
- 00b369b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b369b0 bytes 1f940039
- 00b369b8 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b369b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 00b369b8 bytes e203803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da185ee5ed39e014884538349a99485b"></a>

### [`00b36a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36a4c.md) → [`00b36e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36e74.md) _INIT_271

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00b33df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33df8.md) [`00b33e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33e28.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00b34220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34220.md) [`00b34250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34250.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 37.84% / 新版 34.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 16件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b36a7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b36a90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b36a94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b36a7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b36a88",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b36a90",
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
      "00b36ea4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b36eb0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b36eb8",
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

- 旧版 [`00b36a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36a4c.md#insn-00b36a7c) · [`00b36a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36a4c.md#insn-00b36a90) · [`00b36a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36a4c.md#insn-00b36a94)

~~~diff
- 00b36a7c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b36a7c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b36a7c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b36a7c bytes a9831ff8
- 00b36a90 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b36a90 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00b36a90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b36a90 bytes ea130278
- 00b36a94 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b36a94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b36a94 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c7e8d18c5b17ccc442aee599a217d8b"></a>

### [`00b36fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36fb4.md) → [`00b373dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b373dc.md) FUN_00b373dc

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008877a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008877a0.md) · 呼出先 16件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md)
- 新版 呼出元 1件 [`008877e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008877e0.md) · 呼出先 16件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.82% / 新版 92.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b3743c",
      "incomplete_value": true,
      "site": "00b3743c",
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
                "const:c3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b37014",
      "incomplete_value": true,
      "site": "00b37014",
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
                "const:bfd:8"
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
      "definition_site": "00b37440",
      "incomplete_value": true,
      "site": "00b37440",
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
      "definition_site": "00b37018",
      "incomplete_value": true,
      "site": "00b37018",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b3745c",
      "incomplete_value": true,
      "site": "00b37468",
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
                "const:360:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b37034",
      "incomplete_value": true,
      "site": "00b37040",
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
                "const:320:8"
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
      "00b37428",
      "READ",
      [
        "storage",
        "002b7bfd",
        null,
        "string"
      ]
    ],
    [
      "00b37430",
      "READ",
      [
        "storage",
        "002b7c03",
        null,
        "string"
      ]
    ],
    [
      "00b37458",
      "READ",
      [
        "storage",
        "002bc6ed",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b37428",
      "READ",
      [
        "storage",
        "002b7c3d",
        null,
        "string"
      ]
    ],
    [
      "00b37430",
      "READ",
      [
        "storage",
        "002b7c43",
        null,
        "string"
      ]
    ],
    [
      "00b37458",
      "READ",
      [
        "storage",
        "002bc72d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b370ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36fb4.md#insn-00b370ec) · [`00b36fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36fb4.md#insn-00b36fe8) · [`00b36ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36fb4.md#insn-00b36ff0)
- 新版 [`00b37514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b373dc.md#insn-00b37514) · [`00b37410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b373dc.md#insn-00b37410) · [`00b37418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b373dc.md#insn-00b37418)

~~~diff
- 00b370ec ["INT_ADD", "register:40f0:8", ["const:b370ec:8", "const:4:8"]]
- 00b370ec ["CALL", null, ["callee:0057bea8:8"]]
+ 00b37514 ["INT_ADD", "register:40f0:8", ["const:b37514:8", "const:4:8"]]
+ 00b37514 ["CALL", null, ["callee:0057bea8:8"]]
- 00b370ec bytes 5f13e997
+ 00b37514 bytes 6512e997
- 00b36fe8 ["INT_ADD", "register:40f0:8", ["const:b36fe8:8", "const:4:8"]]
- 00b36fe8 ["CALL", null, ["callee:00588e6c:8"]]
+ 00b37410 ["INT_ADD", "register:40f0:8", ["const:b37410:8", "const:4:8"]]
+ 00b37410 ["CALL", null, ["callee:00588e6c:8"]]
- 00b36fe8 bytes 9147e997
+ 00b37410 bytes 9746e997
- 00b36ff0 ["INT_ADD", "register:40f0:8", ["const:b36ff0:8", "const:4:8"]]
- 00b36ff0 ["CALL", null, ["callee:0058915c:8"]]
+ 00b37418 ["INT_ADD", "register:40f0:8", ["const:b37418:8", "const:4:8"]]
+ 00b37418 ["CALL", null, ["callee:0058915c:8"]]
- 00b36ff0 bytes 4b48e997
+ 00b37418 bytes 5147e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1df7c94eee0fa978c8821c4076cc2476"></a>

### [`00b3738c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b3738c.md) → [`00b377b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b377b4.md) FUN_00b377b4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00887790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887790.md) · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`008877d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008877d0.md) · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 91.94% / 新版 91.94%

CFGの説明率　旧版 61.54% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b377fc",
      "incomplete_value": true,
      "site": "00b37818",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:811:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b373d4",
      "incomplete_value": true,
      "site": "00b373f0",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:7d1:8"
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b37468"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b37890"
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
      "00b377fc",
      "READ",
      [
        "storage",
        "002c07d1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b37468",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b378e4"
      ]
    ]
  ],
  "added": [
    [
      "00b377fc",
      "READ",
      [
        "storage",
        "002c0811",
        null,
        "string"
      ]
    ],
    [
      "00b37890",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b378e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b37468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b3738c.md#insn-00b37468) · [`00b373b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b3738c.md#insn-00b373b0)
- 新版 [`00b37890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b377b4.md#insn-00b37890) · [`00b377d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b377b4.md#insn-00b377d8)

~~~diff
- 00b37468 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b37468 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b37468 bytes a1020054
+ 00b37890 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b37890 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00b37890 bytes a1020054
- 00b373b0 ["INT_ADD", "register:40f0:8", ["const:b373b0:8", "const:4:8"]]
- 00b373b0 ["CALL", null, ["callee:00588e6c:8"]]
+ 00b377d8 ["INT_ADD", "register:40f0:8", ["const:b377d8:8", "const:4:8"]]
+ 00b377d8 ["CALL", null, ["callee:00588e6c:8"]]
- 00b373b0 bytes 9f46e997
+ 00b377d8 bytes a545e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6b2ae4f88060abdce9e3dc1c011ce33"></a>

### [`00b374c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b374c0.md) → [`00b378e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b378e8.md) FUN_00b378e8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00887798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887798.md) · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`008877d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008877d8.md) · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b3792c",
      "incomplete_value": true,
      "site": "00b37944",
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
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:eb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b37504",
      "incomplete_value": true,
      "site": "00b3751c",
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
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:ab:8"
              ]
            ]
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
      "00b3792c",
      "READ",
      [
        "storage",
        "002bd0ab",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b3792c",
      "READ",
      [
        "storage",
        "002bd0eb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b374e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b374c0.md#insn-00b374e4) · [`00b374ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b374c0.md#insn-00b374ec) · [`00b374f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b374c0.md#insn-00b374f8)
- 新版 [`00b3790c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b378e8.md#insn-00b3790c) · [`00b37914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b378e8.md#insn-00b37914) · [`00b37920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b378e8.md#insn-00b37920)

~~~diff
- 00b374e4 ["INT_ADD", "register:40f0:8", ["const:b374e4:8", "const:4:8"]]
- 00b374e4 ["CALL", null, ["callee:00588e6c:8"]]
+ 00b3790c ["INT_ADD", "register:40f0:8", ["const:b3790c:8", "const:4:8"]]
+ 00b3790c ["CALL", null, ["callee:00588e6c:8"]]
- 00b374e4 bytes 5246e997
+ 00b3790c bytes 5845e997
- 00b374ec ["INT_ADD", "register:40f0:8", ["const:b374ec:8", "const:4:8"]]
- 00b374ec ["CALL", null, ["callee:0058915c:8"]]
+ 00b37914 ["INT_ADD", "register:40f0:8", ["const:b37914:8", "const:4:8"]]
+ 00b37914 ["CALL", null, ["callee:0058915c:8"]]
- 00b374ec bytes 0c47e997
+ 00b37914 bytes 1246e997
- 00b374f8 ["COPY", "tmp:0:8", ["const:ab:8"]]
- 00b374f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b374f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b374f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b37920 ["COPY", "tmp:0:8", ["const:eb:8"]]
+ 00b37920 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b37920 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b37920 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b374f8 bytes 29ad0291
+ 00b37920 bytes 29ad0391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-535617e1a2ad1d4336dc1164c3031b18"></a>

### [`00b37760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b37760.md) → [`00b37b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37b88.md) FUN_00b37b88

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00889b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889b64.md) [`0088a348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a348.md) [`0088bbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088bbac.md) · 呼出先 11件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 3件 [`00889ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889ba4.md) [`0088a388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a388.md) [`0088bbec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bbec.md) · 呼出先 11件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.40% / 新版 81.40%

CFGの説明率　旧版 28.26% / 新版 30.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b37834"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b378a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b378b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b37bf0",
      "PARAM",
      [
        "storage",
        "01124cc0",
        null,
        null
      ]
    ],
    [
      "00b37c08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b377f0"
      ]
    ],
    [
      "00b37c14",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b377f8"
      ]
    ]
  ],
  "added": [
    [
      "00b37bf0",
      "PARAM",
      [
        "storage",
        "011250c0",
        null,
        null
      ]
    ],
    [
      "00b37c08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b37c18"
      ]
    ],
    [
      "00b37c14",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b37c20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b377d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b37760.md#insn-00b377d4) · [`00b37800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b37760.md#insn-00b37800) · [`00b37834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b37760.md#insn-00b37834)
- 新版 [`00b37bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37b88.md#insn-00b37bfc)

~~~diff
- 00b377d4 ["INT_ADD", "register:40f0:8", ["const:b377d4:8", "const:4:8"]]
- 00b377d4 ["CALL", null, ["callee:0088956c:8"]]
+ 00b37bfc ["INT_ADD", "register:40f0:8", ["const:b37bfc:8", "const:4:8"]]
+ 00b37bfc ["CALL", null, ["callee:0088956c:8"]]
- 00b377d4 bytes 5647f597
+ 00b37bfc bytes 5c46f597
- 00b37800 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b37800 ["INT_ADD", "register:40f0:8", ["const:b37800:8", "const:4:8"]]
- 00b37800 ["CALLIND", null, ["register:0:8"]]
- 00b37800 bytes 00013fd6
- 00b37834 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b37834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b37834 bytes e82300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f8d1dc553386658c950740cd70335e6"></a>

### [`00b379a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b379a0.md) → [`00b37dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37dc8.md) FUN_00b37dc8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008883e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008883e8.md) · 呼出先 16件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 1件 [`00888428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888428.md) · 呼出先 16件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 41.94% / 新版 40.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b379a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b379a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b379a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b379a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b379a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b379ac",
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
      "00b37dcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b37dd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b37dd4",
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

- 旧版 [`00b379a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b379a0.md#insn-00b379a4) · [`00b379a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b379a0.md#insn-00b379a8) · [`00b379ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b379a0.md#insn-00b379ac)

~~~diff
- 00b379a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b379a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b379a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00b379a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b379a4 bytes fd7b0fa9
- 00b379a8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b379a8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b379a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00b379a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b379a8 bytes fc6710a9
- 00b379ac ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b379ac ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b379ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00b379ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b379ac bytes f85f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de08378c615ce625f60a36b5d1d2b17e"></a>

### [`00b382fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b382fc.md) → [`00b38724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b38/00b38724.md) Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdReady

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) [`005975d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) [`00596f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md) [`00597614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597614.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 25.81% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 3件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b3874c",
      "incomplete_value": true,
      "site": "00b3874c",
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
      "definition_site": "00b38324",
      "incomplete_value": true,
      "site": "00b38324",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3836c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b383b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b38748",
      "READ",
      [
        "storage",
        "01124ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b3836c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b387b0"
      ]
    ],
    [
      "00b387cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b383b0"
      ]
    ]
  ],
  "added": [
    [
      "00b38748",
      "READ",
      [
        "storage",
        "011250e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b38794",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b387b0"
      ]
    ],
    [
      "00b387cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b387d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b38324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b382fc.md#insn-00b38324) · [`00b3836c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b382fc.md#insn-00b3836c) · [`00b3837c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b382fc.md#insn-00b3837c)
- 新版 [`00b3874c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b38/00b38724.md#insn-00b3874c)

~~~diff
- 00b38324 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b38324 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00b3874c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b3874c ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00b38324 bytes a80600b4
+ 00b3874c bytes a80600b4
- 00b3836c ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b3836c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b3836c bytes e00000b5
- 00b3837c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3837c ["INT_ADD", "register:40f0:8", ["const:b3837c:8", "const:4:8"]]
- 00b3837c ["CALLIND", null, ["register:0:8"]]
- 00b3837c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40fe0417fedc144d4a9c95f4fea768df"></a>

### [`00b384c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b384c8.md) → [`00b388f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b38/00b388f0.md) Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdOpened

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) [`005975d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) [`00596f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md) [`00597614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597614.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.91% / 新版 83.91%

CFGの説明率　旧版 31.25% / 新版 25.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b38514"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b3893c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b384f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b384ec",
      "READ",
      [
        "storage",
        "01124da0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b384f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b389ec"
      ]
    ],
    [
      "unmatched:00b38514",
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
      "00b38914",
      "READ",
      [
        "storage",
        "011251a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b38918",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b389ec"
      ]
    ],
    [
      "00b3893c",
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

- 旧版 [`00b384f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b384c8.md#insn-00b384f0) · [`00b38514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b384c8.md#insn-00b38514) · [`00b38580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b384c8.md#insn-00b38580)

~~~diff
- 00b384f0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b384f0 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b384f0 bytes a80600b4
- 00b38514 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00b38514 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b38514 bytes e00f803d
- 00b38580 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b38580 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00b38580 bytes 600400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b7533d98aa177a81d780fa6e5b1d985"></a>

### [`00b38678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38678.md) → [`00b38aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b38/00b38aa0.md) Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdShowFailed

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 78.57% / 新版 55.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b386fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b386fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b38704"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b38acc",
      "READ",
      [
        "storage",
        "01124d40",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b386f4",
      "READ",
      [
        "storage",
        "01124d40",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b386fc",
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
      "00b38acc",
      "READ",
      [
        "storage",
        "01125140",
        null,
        "undefined8"
      ]
    ],
    [
      "00b38b1c",
      "READ",
      [
        "storage",
        "01125140",
        null,
        "undefined8"
      ]
    ],
    [
      "00b38b24",
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

- 旧版 [`00b386a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38678.md#insn-00b386a8) · [`00b386c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38678.md#insn-00b386c4) · [`00b386fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38678.md#insn-00b386fc)
- 新版 [`00b38ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b38/00b38aa0.md#insn-00b38ad0) · [`00b38aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b38/00b38aa0.md#insn-00b38aec)

~~~diff
- 00b386a8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b386a8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b38ad0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b38ad0 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b386a8 bytes e80400b4
+ 00b38ad0 bytes e80400b4
- 00b386c4 ["INT_ADD", "register:40f0:8", ["const:b386c4:8", "const:4:8"]]
- 00b386c4 ["CALL", null, ["callee:00589954:8"]]
+ 00b38aec ["INT_ADD", "register:40f0:8", ["const:b38aec:8", "const:4:8"]]
+ 00b38aec ["CALL", null, ["callee:00589954:8"]]
- 00b386c4 bytes 9444e997
+ 00b38aec bytes 9a43e997
- 00b386fc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b386fc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b386fc ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00b386fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b386fc bytes b3a73ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

