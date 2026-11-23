# v16.0.0 → v16.0.1 · 最優先の変更候補 (61)

[一覧の目次](README.md)

<a id="compare-f08257ce1f047bb419b6d3558ad4fee1"></a>

### [`00a648e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a648e0.md) → [`00a64ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64ad8.md) FUN_00a64ad8

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`009cc9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc9e0.md) [`009d79e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d79e0.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 13件 [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487b40.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488138.md)
- 新版 呼出元 3件 [`009ccb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009cc/009ccb7c.md) [`009d7b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d7/009d7b7c.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 13件 [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488178.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 94.98% / 新版 94.98%

CFGの説明率　旧版 69.77% / 新版 73.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a64b10",
      "incomplete_value": false,
      "site": "00a64b18",
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
      "definition_site": "00a64918",
      "incomplete_value": false,
      "site": "00a64920",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a64c00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a64c04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a64b18",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a64bec",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00a64bf0",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a64b18",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00a64de4",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "00a64de8",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a64a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a648e0.md#insn-00a64a2c) · [`00a64b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a648e0.md#insn-00a64b18) · [`00a64c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a648e0.md#insn-00a64c00)
- 新版 `00a64c24`（命令位置の公開資料なし） · `00a64d10`（命令位置の公開資料なし）

~~~diff
- 00a64a2c ["INT_ADD", "register:40f0:8", ["const:a64a2c:8", "const:4:8"]]
- 00a64a2c ["CALL", null, ["callee:0048793c:8"]]
+ 00a64c24 ["INT_ADD", "register:40f0:8", ["const:a64c24:8", "const:4:8"]]
+ 00a64c24 ["CALL", null, ["callee:0048793c:8"]]
- 00a64a2c bytes b48be897
+ 00a64c24 bytes 468be897
- 00a64b18 ["INT_ADD", "register:40f0:8", ["const:a64b18:8", "const:4:8"]]
- 00a64b18 ["CALL", null, ["callee:0048793c:8"]]
+ 00a64d10 ["INT_ADD", "register:40f0:8", ["const:a64d10:8", "const:4:8"]]
+ 00a64d10 ["CALL", null, ["callee:0048793c:8"]]
- 00a64b18 bytes 798be897
+ 00a64d10 bytes 0b8be897
- 00a64c00 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00a64c00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a64c00 bytes e81300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08fb79b381cd3965ade0fc359c0cd559"></a>

### [`00a64d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64d40.md) → [`00a64f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64f38.md) FUN_00a64f38

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 22件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`004883f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004883f4.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 22件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.38% / 新版 88.38%

CFGの説明率　旧版 70.32% / 新版 72.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 1件, `store_destination` 1件, `store_value` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 24件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a64d40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a64d40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a64d44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a64d40",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a64d44",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a64d48",
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
      "00a64f38",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a64f3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a64f40",
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

- 旧版 [`00a64d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64d40.md#insn-00a64d40) · [`00a64d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64d40.md#insn-00a64d44) · [`00a64d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64d40.md#insn-00a64d48)

~~~diff
- 00a64d40 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a64d40 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a64d40 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00a64d40 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a64d40 bytes fd7bbaa9
- 00a64d44 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a64d44 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a64d44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a64d44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a64d44 bytes fc6f01a9
- 00a64d48 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a64d48 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a64d48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a64d48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a64d48 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf23f8959d21a774c57c26086554e805"></a>

### [`00a65868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65868.md) → [`00a65a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65a60.md) FUN_00a65a60

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`007dd760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd760.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`006b8c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8c04.md) [`00a65668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65668.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`007dd7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd7a0.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`006b8c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8c44.md) [`00a65860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65860.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.13% / 新版 93.13%

CFGの説明率　旧版 39.13% / 新版 36.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_condition` 2件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a65a00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a65a30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a65a30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a65914",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a65b18"
      ]
    ],
    [
      "unmatched:00a6596c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a65b4c"
      ]
    ],
    [
      "unmatched:00a659a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a65bac"
      ]
    ]
  ],
  "added": [
    [
      "00a65b0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a65b18"
      ]
    ],
    [
      "00a65b64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a65b4c"
      ]
    ],
    [
      "00a65ba0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a65bac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a65914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65868.md#insn-00a65914) · [`00a6596c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65868.md#insn-00a6596c) · [`00a659a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65868.md#insn-00a659a8)

~~~diff
- 00a65914 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a65914 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00a65914 bytes 680000b4
- 00a6596c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a6596c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00a6596c bytes 48ffffb5
- 00a659a8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a659a8 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00a659a8 bytes 680000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57bfa43827e92a3b5dc8e958f95fc298"></a>

### [`00a65a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65a74.md) → [`00a65c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65c6c.md) FUN_00a65c6c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00a65668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65668.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00a65860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65860.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.96% / 新版 98.96%

CFGの説明率　旧版 73.68% / 新版 75.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a65cd4",
      "incomplete_value": false,
      "site": "00a65cdc",
      "value": [
        "leaf",
        "const:40:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a65ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65a74.md#insn-00a65ae4) · [`00a65a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65a74.md#insn-00a65a84) · [`00a65a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65a74.md#insn-00a65a94)
- 新版 `00a65cdc`（命令位置の公開資料なし） · `00a65c8c`（命令位置の公開資料なし）

~~~diff
- 00a65ae4 ["INT_ADD", "register:40f0:8", ["const:a65ae4:8", "const:4:8"]]
- 00a65ae4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a65cdc ["INT_ADD", "register:40f0:8", ["const:a65cdc:8", "const:4:8"]]
+ 00a65cdc ["CALL", null, ["callee:00c57e90:8"]]
- 00a65ae4 bytes ebc70794
+ 00a65cdc bytes 6dc80794
- 00a65a84 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00a65a84 bytes fd030091
- 00a65a94 ["INT_ADD", "register:40f0:8", ["const:a65a94:8", "const:4:8"]]
- 00a65a94 ["CALL", null, ["callee:00a65860:8"]]
+ 00a65c8c ["INT_ADD", "register:40f0:8", ["const:a65c8c:8", "const:4:8"]]
+ 00a65c8c ["CALL", null, ["callee:00a65860:8"]]
- 00a65a94 bytes f5feff97
+ 00a65c8c bytes f5feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ed7beb688c3a7ed23ca22b7d1c97ec4"></a>

### [`00a661e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a661e8.md) → [`00a663e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a66/00a663e0.md) FUN_00a663e0

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a65bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65bf4.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00a65dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65dec.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 94.34% / 新版 94.34%

CFGの説明率　旧版 52.94% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a66260"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a66268"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a66458"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a66260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a661e8.md#insn-00a66260) · [`00a66268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a661e8.md#insn-00a66268)
- 新版 `00a66458`（命令位置の公開資料なし）

~~~diff
- 00a66260 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a66260 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00a66260 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:30:8"]]
- 00a66260 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 00a66260 bytes 1f0d03f8
- 00a66268 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:28:8"]]
- 00a66268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a66268 bytes 081400f9
+ 00a66458 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00a66458 ["COPY", "tmp:1:8", ["tmp:0:8"]]
+ 00a66458 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:30:8"]]
+ 00a66458 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
+ 00a66458 bytes 1f0d03f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1145915c59fcd0e340caa83e210d3c46"></a>

### [`00a662bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a662bc.md) → [`00a664b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a66/00a664b4.md) FUN_00a664b4

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0080019c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/0080019c.md) [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`00802634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802634.md)
- 新版 呼出元 6件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`008001dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001dc.md) [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`00802674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802674.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.58% / 新版 89.58%

CFGの説明率　旧版 53.88% / 新版 55.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a662fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a664f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a663d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a662fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a6650c",
      "DATA",
      [
        "storage",
        "00387138",
        null,
        "uleb128"
      ]
    ],
    [
      "00a6657c",
      "DATA",
      [
        "storage",
        "00387138",
        null,
        "uleb128"
      ]
    ]
  ],
  "added": [
    [
      "00a664f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a6650c",
      "DATA",
      [
        "storage",
        "00387138",
        null,
        "qword"
      ]
    ],
    [
      "00a6657c",
      "DATA",
      [
        "storage",
        "00387138",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a662fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a662bc.md#insn-00a662fc) · [`00a663d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a662bc.md#insn-00a663d0) · [`00a66494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a662bc.md#insn-00a66494)
- 新版 `00a6668c`（命令位置の公開資料なし）

~~~diff
- 00a662fc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a662fc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a662fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a662fc bytes a8831ff8
- 00a663d0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a663d0 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00a663d0 bytes 280100b4
- 00a66494 ["INT_ADD", "register:40f0:8", ["const:a66494:8", "const:4:8"]]
- 00a66494 ["CALL", null, ["callee:0080e784:8"]]
+ 00a6668c ["INT_ADD", "register:40f0:8", ["const:a6668c:8", "const:4:8"]]
+ 00a6668c ["CALL", null, ["callee:0080e784:8"]]
- 00a66494 bytes aca0f697
+ 00a6668c bytes 3ea0f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27149aaf12de6345ad7f0363b9891a7d"></a>

### [`00a66aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66aa0.md) → [`00a66c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a66/00a66c98.md) FUN_00a66c98

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`007cb5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb5a0.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`007f8010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8010.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00802634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802634.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 5件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`007f8050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8050.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00802674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802674.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.72% / 新版 74.72%

CFGの説明率　旧版 52.90% / 新版 54.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a66bfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a66c04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a66c0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a66ad8",
      "DATA",
      [
        "storage",
        "003c75e0",
        null,
        "dword"
      ]
    ],
    [
      "unmatched:00a66ae8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a66d64"
      ]
    ],
    [
      "00a66d5c",
      "DATA",
      [
        "storage",
        "003bb950",
        "fde_003bb950",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "00a66cd0",
      "DATA",
      [
        "storage",
        "003c75e0",
        null,
        "byte[11]"
      ]
    ],
    [
      "00a66ce0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a66d64"
      ]
    ],
    [
      "00a66d5c",
      "DATA",
      [
        "storage",
        "003bb950",
        null,
        "uleb128"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a66bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66aa0.md#insn-00a66bfc) · [`00a66c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66aa0.md#insn-00a66c04) · [`00a66c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66aa0.md#insn-00a66c0c)

~~~diff
- 00a66bfc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:38:8"]]
- 00a66bfc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a66bfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00a66bfc bytes 1f1c00f9
- 00a66c04 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a66c04 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00a66c04 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:30:8"]]
- 00a66c04 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 00a66c04 bytes 1f0d03f8
- 00a66c0c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:28:8"]]
- 00a66c0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a66c0c bytes 081400f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f63ae784176e5943c76d54e9c1049b9"></a>

### [`00a66ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66ec4.md) → [`00a670bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a670bc.md) FUN_00a670bc

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00802634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802634.md) [`0080e8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e8a4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00802674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802674.md) [`0080e8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8e4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.44% / 新版 99.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a67310",
      "incomplete_value": false,
      "site": "00a67330",
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
      "definition_site": "00a67118",
      "incomplete_value": false,
      "site": "00a67138",
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
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a6710c",
      "DATA",
      [
        "storage",
        "003c75e0",
        null,
        "dword"
      ]
    ],
    [
      "00a67198",
      "DATA",
      [
        "storage",
        "003bb950",
        "fde_003bb950",
        "dword"
      ]
    ],
    [
      "00a67204",
      "DATA",
      [
        "storage",
        "003bb950",
        "fde_003bb950",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "00a6710c",
      "DATA",
      [
        "storage",
        "003c75e0",
        null,
        "byte[11]"
      ]
    ],
    [
      "00a67198",
      "DATA",
      [
        "storage",
        "003bb950",
        null,
        "uleb128"
      ]
    ],
    [
      "00a67204",
      "DATA",
      [
        "storage",
        "003bb950",
        null,
        "uleb128"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a67138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66ec4.md#insn-00a67138) · [`00a66f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66ec4.md#insn-00a66f08) · [`00a66f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66ec4.md#insn-00a66f98)
- 新版 `00a67330`（命令位置の公開資料なし） · `00a67100`（命令位置の公開資料なし） · `00a67190`（命令位置の公開資料なし）

~~~diff
- 00a67138 ["INT_ADD", "register:40f0:8", ["const:a67138:8", "const:4:8"]]
- 00a67138 ["CALL", null, ["callee:0080e8e4:8"]]
+ 00a67330 ["INT_ADD", "register:40f0:8", ["const:a67330:8", "const:4:8"]]
+ 00a67330 ["CALL", null, ["callee:0080e8e4:8"]]
- 00a67138 bytes db9df697
+ 00a67330 bytes 6d9df697
- 00a66f08 ["INT_ADD", "register:40f0:8", ["const:a66f08:8", "const:4:8"]]
- 00a66f08 ["CALL", null, ["callee:008514f8:8"]]
+ 00a67100 ["INT_ADD", "register:40f0:8", ["const:a67100:8", "const:4:8"]]
+ 00a67100 ["CALL", null, ["callee:008514f8:8"]]
- 00a66f08 bytes 6ca9f797
+ 00a67100 bytes fea8f797
- 00a66f98 ["INT_ADD", "register:40f0:8", ["const:a66f98:8", "const:4:8"]]
- 00a66f98 ["CALL", null, ["callee:008514f8:8"]]
+ 00a67190 ["INT_ADD", "register:40f0:8", ["const:a67190:8", "const:4:8"]]
+ 00a67190 ["CALL", null, ["callee:008514f8:8"]]
- 00a66f98 bytes 48a9f797
+ 00a67190 bytes daa8f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12d9ef5cb891445f8b32b81ef8cededb"></a>

### [`00a674e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a674e8.md) → [`00a676e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a676e0.md) FUN_00a676e0

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 4件 [`00802634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802634.md) [`0080ea04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080ea04.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 4件 [`00802674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802674.md) [`0080ea44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea44.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 73.08% / 新版 73.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a675e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a677d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a67588"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a67720",
      "DATA",
      [
        "storage",
        "003c75f8",
        "fde_003c75f8",
        "dword"
      ]
    ],
    [
      "unmatched:00a67588",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a67770"
      ]
    ],
    [
      "unmatched:00a675c4",
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
      "00a67720",
      "DATA",
      [
        "storage",
        "003c75f8",
        null,
        "byte[11]"
      ]
    ],
    [
      "00a67780",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a67770"
      ]
    ],
    [
      "00a677bc",
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

- 旧版 [`00a67588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a674e8.md#insn-00a67588) · [`00a675e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a674e8.md#insn-00a675e0) · [`00a675e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a674e8.md#insn-00a675e4)
- 新版 `00a677dc`（命令位置の公開資料なし）

~~~diff
- 00a67588 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a67588 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00a67588 bytes 81ffff54
- 00a675e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a675e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a675e0 bytes e80b00f9
- 00a675e4 ["INT_ADD", "register:40f0:8", ["const:a675e4:8", "const:4:8"]]
- 00a675e4 ["CALL", null, ["callee:0080ea44:8"]]
+ 00a677dc ["INT_ADD", "register:40f0:8", ["const:a677dc:8", "const:4:8"]]
+ 00a677dc ["CALL", null, ["callee:0080ea44:8"]]
- 00a675e4 bytes 089df697
+ 00a677dc bytes 9a9cf697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74f46600c4a21608703d4d7ed9ddb890"></a>

### [`00a678f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a678f8.md) → [`00a67af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67af0.md) FUN_00a67af0

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 4件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`005dfc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005dfc88.md) [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 4件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`005dfcc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005df/005dfcc8.md) [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a67bf8",
      "incomplete_value": false,
      "site": "00a67bfc",
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
      "definition_site": "00a67a00",
      "incomplete_value": false,
      "site": "00a67a04",
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
      "00a67bf8",
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
      "00a67bf8",
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

- 旧版 [`00a67a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a678f8.md#insn-00a67a04) · [`00a6790c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a678f8.md#insn-00a6790c) · [`00a67914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a678f8.md#insn-00a67914)
- 新版 `00a67bfc`（命令位置の公開資料なし） · `00a67b04`（命令位置の公開資料なし） · `00a67b0c`（命令位置の公開資料なし）

~~~diff
- 00a67a04 ["INT_ADD", "register:40f0:8", ["const:a67a04:8", "const:4:8"]]
- 00a67a04 ["CALL", null, ["callee:00442930:8"]]
+ 00a67bfc ["INT_ADD", "register:40f0:8", ["const:a67bfc:8", "const:4:8"]]
+ 00a67bfc ["CALL", null, ["callee:00442930:8"]]
- 00a67a04 bytes bb6be797
+ 00a67bfc bytes 4d6be797
- 00a6790c ["INT_ADD", "register:40f0:8", ["const:a6790c:8", "const:4:8"]]
- 00a6790c ["CALL", null, ["callee:008001ec:8"]]
+ 00a67b04 ["INT_ADD", "register:40f0:8", ["const:a67b04:8", "const:4:8"]]
+ 00a67b04 ["CALL", null, ["callee:008001ec:8"]]
- 00a6790c bytes 2862f697
+ 00a67b04 bytes ba61f697
- 00a67914 ["INT_ADD", "register:40f0:8", ["const:a67914:8", "const:4:8"]]
- 00a67914 ["CALL", null, ["callee:008514f8:8"]]
+ 00a67b0c ["INT_ADD", "register:40f0:8", ["const:a67b0c:8", "const:4:8"]]
+ 00a67b0c ["CALL", null, ["callee:008514f8:8"]]
- 00a67914 bytes e9a6f797
+ 00a67b0c bytes 7ba6f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db3282cbd575f81a41297a9e5680ab13"></a>

### [`00a68270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68270.md) → [`00a68468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68468.md) FUN_00a68468

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a67638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67638.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`00a67830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67830.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "00a68474",
      "incomplete_value": false,
      "site": "00a68478",
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
      "definition_site": "00a6827c",
      "incomplete_value": false,
      "site": "00a68280",
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
      "00a68474",
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
      "00a68474",
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

- 旧版 [`00a68280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68270.md#insn-00a68280) · [`00a6827c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68270.md#insn-00a6827c)
- 新版 `00a68478`（命令位置の公開資料なし） · `00a68474`（命令位置の公開資料なし）

~~~diff
- 00a68280 ["INT_ADD", "register:40f0:8", ["const:a68280:8", "const:4:8"]]
- 00a68280 ["CALL", null, ["callee:00442930:8"]]
+ 00a68478 ["INT_ADD", "register:40f0:8", ["const:a68478:8", "const:4:8"]]
+ 00a68478 ["CALL", null, ["callee:00442930:8"]]
- 00a68280 bytes 9c69e797
+ 00a68478 bytes 2e69e797
- 00a6827c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00a6827c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a6827c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a6827c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a68474 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00a68474 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a68474 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a68474 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a6827c bytes 00303c91
+ 00a68474 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bfe6a50b9e5601c431b57db5467b61e"></a>

### [`00a68284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68284.md) → [`00a6847c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a6847c.md) _INIT_221

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 77.40% / 新版 77.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 3件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a684b8",
      "incomplete_value": true,
      "site": "00a684d4",
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
      "definition_site": "00a682c0",
      "incomplete_value": true,
      "site": "00a682dc",
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
      "definition_site": "00a684dc",
      "incomplete_value": true,
      "site": "00a684f8",
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
      "definition_site": "00a682e4",
      "incomplete_value": true,
      "site": "00a68300",
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
      "definition_site": "00a684fc",
      "incomplete_value": true,
      "site": "00a68518",
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
      "definition_site": "00a68304",
      "incomplete_value": true,
      "site": "00a68320",
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
      "00a684b8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00a684dc",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00a684fc",
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
      "00a684b8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00a684dc",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00a684fc",
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

- 旧版 [`00a68330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68284.md#insn-00a68330) · [`00a6833c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68284.md#insn-00a6833c) · [`00a68348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68284.md#insn-00a68348)

~~~diff
- 00a68330 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:88:8"]]
- 00a68330 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00a68330 bytes e98b00b9
- 00a6833c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:71:8"]]
- 00a6833c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a6833c bytes e013873c
- 00a68348 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00a68348 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:99:8"]]
- 00a68348 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00a68348 bytes 89920978
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3689befff0be7e746cdc17eaca03ff22"></a>

### [`00a687bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a687bc.md) → [`00a689b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a689b4.md) FUN_00a689b4

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a68f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68f5c.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00a69154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69154.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`005c17e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c17e0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 83.72% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a687f8",
      "incomplete_value": true,
      "site": "00a68808",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a68a4c",
      "incomplete_value": true,
      "site": "00a68a50",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a68808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a687bc.md#insn-00a68808) · [`00a68858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a687bc.md#insn-00a68858) · [`00a687f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a687bc.md#insn-00a687f4)
- 新版 `00a68a00`（命令位置の公開資料なし） · `00a68a50`（命令位置の公開資料なし） · `00a689ec`（命令位置の公開資料なし）

~~~diff
- 00a68808 ["INT_ADD", "register:40f0:8", ["const:a68808:8", "const:4:8"]]
- 00a68808 ["CALL", null, ["callee:004803f0:8"]]
+ 00a68a00 ["INT_ADD", "register:40f0:8", ["const:a68a00:8", "const:4:8"]]
+ 00a68a00 ["CALL", null, ["callee:004803f0:8"]]
- 00a68808 bytes ea5ee897
+ 00a68a00 bytes 7c5ee897
- 00a68858 ["INT_ADD", "register:40f0:8", ["const:a68858:8", "const:4:8"]]
- 00a68858 ["CALL", null, ["callee:004803f0:8"]]
+ 00a68a50 ["INT_ADD", "register:40f0:8", ["const:a68a50:8", "const:4:8"]]
+ 00a68a50 ["CALL", null, ["callee:004803f0:8"]]
- 00a68858 bytes d65ee897
+ 00a68a50 bytes 685ee897
- 00a687f4 ["INT_ADD", "register:40f0:8", ["const:a687f4:8", "const:4:8"]]
- 00a687f4 ["CALL", null, ["callee:005c17e0:8"]]
+ 00a689ec ["INT_ADD", "register:40f0:8", ["const:a689ec:8", "const:4:8"]]
+ 00a689ec ["CALL", null, ["callee:005c17e0:8"]]
- 00a687f4 bytes eb63ed97
+ 00a689ec bytes 7d63ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f340056bda68ed02ecfeabe334a22e60"></a>

### [`00a68af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68af0.md) → [`00a68ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68ce8.md) FUN_00a68ce8

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a69950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69950.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00a69b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69b48.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.03% / 新版 98.03%

CFGの説明率　旧版 81.93% / 新版 80.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a68bbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a68bcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a68db4"
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
      "unmatched:00a68b80",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a68bbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a68d74"
      ]
    ],
    [
      "unmatched:00a68bcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a68dd4"
      ]
    ]
  ],
  "added": [
    [
      "00a68d78",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ],
    [
      "00a68db4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a68d74"
      ]
    ],
    [
      "00a68dc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a68dd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a68b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68af0.md#insn-00a68b84) · [`00a68bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68af0.md#insn-00a68bbc) · [`00a68bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68af0.md#insn-00a68bcc)
- 新版 `00a68d7c`（命令位置の公開資料なし）

~~~diff
- 00a68b84 ["INT_ADD", "register:40f0:8", ["const:a68b84:8", "const:4:8"]]
- 00a68b84 ["CALL", null, ["callee:00442930:8"]]
+ 00a68d7c ["INT_ADD", "register:40f0:8", ["const:a68d7c:8", "const:4:8"]]
+ 00a68d7c ["CALL", null, ["callee:00442930:8"]]
- 00a68b84 bytes 5b67e797
+ 00a68d7c bytes ed66e797
- 00a68bbc ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00a68bbc ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00a68bbc bytes 09feffb4
- 00a68bcc ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a68bcc ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
- 00a68bcc bytes 8a000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d7f2522095208b6162ddd06f2581a6c"></a>

### [`00a68f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68f5c.md) → [`00a69154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69154.md) FUN_00a69154

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`0086bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md) [`00a687bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a687bc.md) [`00a6ae18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ae18.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`0086bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md) [`00a689b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a689b4.md) [`00a6b010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6b/00a6b010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 96.38% / 新版 96.38%

CFGの説明率　旧版 68.29% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a691f0",
      "incomplete_value": false,
      "site": "00a691f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a68ff8",
      "incomplete_value": false,
      "site": "00a69000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a690cc",
      "incomplete_value": true,
      "site": "00a690d4",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a69314",
      "incomplete_value": true,
      "site": "00a69318",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "old": null,
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a691f8",
      "DATA",
      [
        "storage",
        "00c8b500",
        null,
        "pointer"
      ]
    ],
    [
      "00a6930c",
      "READ",
      [
        "storage",
        "00c8b510",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a69134",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00a691f8",
      "DATA",
      [
        "storage",
        "00c8b900",
        null,
        "pointer"
      ]
    ],
    [
      "00a6930c",
      "READ",
      [
        "storage",
        "00c8b910",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6932c",
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

- 旧版 [`00a690d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68f5c.md#insn-00a690d4) · [`00a69120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68f5c.md#insn-00a69120) · [`00a69134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68f5c.md#insn-00a69134)
- 新版 `00a692cc`（命令位置の公開資料なし） · `00a69318`（命令位置の公開資料なし）

~~~diff
- 00a690d4 ["INT_ADD", "register:40f0:8", ["const:a690d4:8", "const:4:8"]]
- 00a690d4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00a692cc ["INT_ADD", "register:40f0:8", ["const:a692cc:8", "const:4:8"]]
+ 00a692cc ["CALL", null, ["callee:00c53cd0:8"]]
- 00a690d4 bytes f7a90794
+ 00a692cc bytes 81aa0794
- 00a69120 ["INT_ADD", "register:40f0:8", ["const:a69120:8", "const:4:8"]]
- 00a69120 ["CALL", null, ["callee:00c57e80:8"]]
+ 00a69318 ["INT_ADD", "register:40f0:8", ["const:a69318:8", "const:4:8"]]
+ 00a69318 ["CALL", null, ["callee:00c57e80:8"]]
- 00a69120 bytes 58ba0794
+ 00a69318 bytes daba0794
- 00a69134 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a69134 ["INT_ADD", "register:40f0:8", ["const:a69134:8", "const:4:8"]]
- 00a69134 ["CALLIND", null, ["register:0:8"]]
- 00a69134 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55c31836eacde068d3414a280f7b5711"></a>

### [`00a69284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69284.md) → [`00a6947c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a6947c.md) FUN_00a6947c

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 1件 [`0086bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md)
- 新版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 1件 [`0086bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6929c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69284.md#insn-00a6929c)
- 新版 `00a69494`（命令位置の公開資料なし）

~~~diff
- 00a6929c ["INT_ADD", "register:40f0:8", ["const:a6929c:8", "const:4:8"]]
- 00a6929c ["CALL", null, ["callee:0086bdb8:8"]]
+ 00a69494 ["INT_ADD", "register:40f0:8", ["const:a69494:8", "const:4:8"]]
+ 00a69494 ["CALL", null, ["callee:0086bdb8:8"]]
- 00a6929c bytes b70af897
+ 00a69494 bytes 490af897
~~~


<a id="compare-0764eb0400f7ebb956b278de54b8b112"></a>

### [`00a69330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69330.md) → [`00a69528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69528.md) FUN_00a69528

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`007ca4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007ca4e8.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 3件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`007ca528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca528.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 91.23% / 新版 91.23%

CFGの説明率　旧版 89.47% / 新版 82.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a693d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a695d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a69590",
      "incomplete_value": false,
      "site": "00a69594",
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
      "definition_site": "00a69398",
      "incomplete_value": false,
      "site": "00a6939c",
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
      "00a69590",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a693d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6958c"
      ]
    ],
    [
      "unmatched:00a6940c",
      "DATA",
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
      "00a69590",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ],
    [
      "00a695d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6958c"
      ]
    ],
    [
      "00a69604",
      "DATA",
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

- 旧版 [`00a6939c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69330.md#insn-00a6939c) · [`00a693d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69330.md#insn-00a693d8) · [`00a69410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69330.md#insn-00a69410)
- 新版 `00a69594`（命令位置の公開資料なし）

~~~diff
- 00a6939c ["INT_ADD", "register:40f0:8", ["const:a6939c:8", "const:4:8"]]
- 00a6939c ["CALL", null, ["callee:00442930:8"]]
+ 00a69594 ["INT_ADD", "register:40f0:8", ["const:a69594:8", "const:4:8"]]
+ 00a69594 ["CALL", null, ["callee:00442930:8"]]
- 00a6939c bytes 5565e797
+ 00a69594 bytes e764e797
- 00a693d8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00a693d8 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00a693d8 bytes e9fdffb4
- 00a69410 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a69410 ["RETURN", null, ["register:0:8"]]
- 00a69410 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b48365c5d1ed729e78dd780dcaeb60"></a>

### [`00a69414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69414.md) → [`00a6960c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a6960c.md) FUN_00a6960c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`00937f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937f14.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 2件 [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`009380b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/009380b0.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a69668",
      "incomplete_value": false,
      "site": "00a6966c",
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
      "definition_site": "00a69470",
      "incomplete_value": false,
      "site": "00a69474",
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
      "00a69668",
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
      "00a69668",
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

- 旧版 [`00a69474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69414.md#insn-00a69474) · [`00a69470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69414.md#insn-00a69470)
- 新版 `00a6966c`（命令位置の公開資料なし） · `00a69668`（命令位置の公開資料なし）

~~~diff
- 00a69474 ["INT_ADD", "register:40f0:8", ["const:a69474:8", "const:4:8"]]
- 00a69474 ["CALL", null, ["callee:00442930:8"]]
+ 00a6966c ["INT_ADD", "register:40f0:8", ["const:a6966c:8", "const:4:8"]]
+ 00a6966c ["CALL", null, ["callee:00442930:8"]]
- 00a69474 bytes 1f65e797
+ 00a6966c bytes b164e797
- 00a69470 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00a69470 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a69470 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a69470 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a69668 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00a69668 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a69668 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a69668 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a69470 bytes 00c00391
+ 00a69668 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-071205e395e7f62795270f218a245df4"></a>

### [`00a69494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69494.md) → [`00a6968c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a6968c.md) FUN_00a6968c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a6ad34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ad34.md) · 呼出先 2件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00a69598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69598.md)
- 新版 呼出元 1件 [`00a6af2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6af2c.md) · 呼出先 2件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00a69790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69790.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.41% / 新版 98.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a696f4",
      "incomplete_value": false,
      "site": "00a696f8",
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
      "definition_site": "00a694fc",
      "incomplete_value": false,
      "site": "00a69500",
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
      "00a696f4",
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
      "00a696f4",
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

- 旧版 [`00a69500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69494.md#insn-00a69500) · [`00a694fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69494.md#insn-00a694fc)
- 新版 `00a696f8`（命令位置の公開資料なし） · `00a696f4`（命令位置の公開資料なし）

~~~diff
- 00a69500 ["INT_ADD", "register:40f0:8", ["const:a69500:8", "const:4:8"]]
- 00a69500 ["CALL", null, ["callee:00442930:8"]]
+ 00a696f8 ["INT_ADD", "register:40f0:8", ["const:a696f8:8", "const:4:8"]]
+ 00a696f8 ["CALL", null, ["callee:00442930:8"]]
- 00a69500 bytes fc64e797
+ 00a696f8 bytes 8e64e797
- 00a694fc ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00a694fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a694fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a694fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a696f4 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00a696f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a696f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a696f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a694fc bytes 00c00391
+ 00a696f4 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caf38c60d0cb5f8d54972e74e2920855"></a>

### [`00a69598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69598.md) → [`00a69790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69790.md) FUN_00a69790

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) [`00a69494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69494.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`0046da94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0071d1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d1fc.md) [`00a6968c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a6968c.md) · 呼出先 11件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046dabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dabc.md) [`0046dad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dad4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.26% / 新版 98.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a69808",
      "incomplete_value": false,
      "site": "00a6980c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a69610",
      "incomplete_value": false,
      "site": "00a69614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
    "new": {
      "definition_site": "00a69a00",
      "incomplete_value": false,
      "site": "00a69a04",
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
      "definition_site": "00a69808",
      "incomplete_value": false,
      "site": "00a6980c",
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
    "ordinal": 18,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a6980c",
      "DATA",
      [
        "storage",
        "00c8b500",
        null,
        "pointer"
      ]
    ],
    [
      "00a69a00",
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
      "00a6980c",
      "DATA",
      [
        "storage",
        "00c8b900",
        null,
        "pointer"
      ]
    ],
    [
      "00a69a00",
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

- 旧版 [`00a6980c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69598.md#insn-00a6980c) · [`00a69604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69598.md#insn-00a69604) · [`00a69610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69598.md#insn-00a69610)
- 新版 `00a69a04`（命令位置の公開資料なし） · `00a697fc`（命令位置の公開資料なし） · `00a69808`（命令位置の公開資料なし）

~~~diff
- 00a6980c ["INT_ADD", "register:40f0:8", ["const:a6980c:8", "const:4:8"]]
- 00a6980c ["CALL", null, ["callee:00442930:8"]]
+ 00a69a04 ["INT_ADD", "register:40f0:8", ["const:a69a04:8", "const:4:8"]]
+ 00a69a04 ["CALL", null, ["callee:00442930:8"]]
- 00a6980c bytes 3964e797
+ 00a69a04 bytes cb63e797
- 00a69604 ["INT_ADD", "register:40f0:8", ["const:a69604:8", "const:4:8"]]
- 00a69604 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a697fc ["INT_ADD", "register:40f0:8", ["const:a697fc:8", "const:4:8"]]
+ 00a697fc ["CALL", null, ["callee:00c57e90:8"]]
- 00a69604 bytes 23b90794
+ 00a697fc bytes a5b90794
- 00a69610 ["COPY", "tmp:0:8", ["const:500:8"]]
- 00a69610 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a69610 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a69610 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a69808 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 00a69808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a69808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a69808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a69610 bytes 08011491
+ 00a69808 bytes 08012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eb7df2f75965b0c776d89196d532993"></a>

### [`00a6986c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a6986c.md) → [`00a69a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69a64.md) FUN_00a69a64

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 2件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00a689f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a689f0.md)
- 新版 呼出元 3件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00a68be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68be8.md)

変更の種類 call_argument_candidate, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a69ad0",
      "incomplete_value": false,
      "site": "00a69ad4",
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
      "definition_site": "00a698d8",
      "incomplete_value": false,
      "site": "00a698dc",
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
      "00a69ad0",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      "00a69b44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a689f0"
      ]
    ]
  ],
  "added": [
    [
      "00a69ad0",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ],
    [
      "00a69b44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a68be8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a698dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a6986c.md#insn-00a698dc) · [`00a698d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a6986c.md#insn-00a698d8) · [`00a6994c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a6986c.md#insn-00a6994c)
- 新版 `00a69ad4`（命令位置の公開資料なし） · `00a69ad0`（命令位置の公開資料なし） · `00a69b44`（命令位置の公開資料なし）

~~~diff
- 00a698dc ["INT_ADD", "register:40f0:8", ["const:a698dc:8", "const:4:8"]]
- 00a698dc ["CALL", null, ["callee:00442930:8"]]
+ 00a69ad4 ["INT_ADD", "register:40f0:8", ["const:a69ad4:8", "const:4:8"]]
+ 00a69ad4 ["CALL", null, ["callee:00442930:8"]]
- 00a698dc bytes 0564e797
+ 00a69ad4 bytes 9763e797
- 00a698d8 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00a698d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a698d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a698d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a69ad0 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00a69ad0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a69ad0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a69ad0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a698d8 bytes 00c00391
+ 00a69ad0 bytes 00f40691
- 00a6994c ["BRANCH", null, ["ram:a689f0:8"]]
+ 00a69b44 ["BRANCH", null, ["ram:a68be8:8"]]
- 00a6994c bytes 29fcff17
+ 00a69b44 bytes 29fcff17
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdf7169b430015185d5d5c784adfe578"></a>

### [`00a69950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69950.md) → [`00a69b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69b48.md) FUN_00a69b48

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a6ad34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ad34.md) · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00a68af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68af0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00a6af2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6af2c.md) · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00a68ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68ce8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.86% / 新版 97.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a69bcc",
      "incomplete_value": false,
      "site": "00a69bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a699d4",
      "incomplete_value": false,
      "site": "00a699d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a69d2c",
      "incomplete_value": false,
      "site": "00a69d30",
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
      "definition_site": "00a69b34",
      "incomplete_value": false,
      "site": "00a69b38",
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
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a69bd0",
      "DATA",
      [
        "storage",
        "00c8b500",
        null,
        "pointer"
      ]
    ],
    [
      "00a69d2c",
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
      "00a69bd0",
      "DATA",
      [
        "storage",
        "00c8b900",
        null,
        "pointer"
      ]
    ],
    [
      "00a69d2c",
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

- 旧版 [`00a69b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69950.md#insn-00a69b38) · [`00a699c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69950.md#insn-00a699c8) · [`00a699d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69950.md#insn-00a699d4)
- 新版 `00a69d30`（命令位置の公開資料なし） · `00a69bc0`（命令位置の公開資料なし） · `00a69bcc`（命令位置の公開資料なし）

~~~diff
- 00a69b38 ["INT_ADD", "register:40f0:8", ["const:a69b38:8", "const:4:8"]]
- 00a69b38 ["CALL", null, ["callee:00442930:8"]]
+ 00a69d30 ["INT_ADD", "register:40f0:8", ["const:a69d30:8", "const:4:8"]]
+ 00a69d30 ["CALL", null, ["callee:00442930:8"]]
- 00a69b38 bytes 6e63e797
+ 00a69d30 bytes 0063e797
- 00a699c8 ["INT_ADD", "register:40f0:8", ["const:a699c8:8", "const:4:8"]]
- 00a699c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a69bc0 ["INT_ADD", "register:40f0:8", ["const:a69bc0:8", "const:4:8"]]
+ 00a69bc0 ["CALL", null, ["callee:00c57e90:8"]]
- 00a699c8 bytes 32b80794
+ 00a69bc0 bytes b4b80794
- 00a699d4 ["COPY", "tmp:0:8", ["const:500:8"]]
- 00a699d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a699d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a699d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a69bcc ["COPY", "tmp:0:8", ["const:900:8"]]
+ 00a69bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a69bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a69bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a699d4 bytes 08011491
+ 00a69bcc bytes 08012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7d306710f6f3cf72b296aec1bfa357a"></a>

### [`00a69bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69bd8.md) → [`00a69dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69dd0.md) FUN_00a69dd0

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a69bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69bb4.md) · 呼出先 19件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`00a69dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69dac.md) · 呼出先 19件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment

命令の説明率　旧版 94.16% / 新版 94.16%

CFGの説明率　旧版 95.45% / 新版 93.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件, `store_value` 4件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a69e0c",
      "incomplete_value": false,
      "site": "00a69e10",
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
      "definition_site": "00a69c14",
      "incomplete_value": false,
      "site": "00a69c18",
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
      "definition_site": "00a6a13c",
      "incomplete_value": true,
      "site": "00a6a140",
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
      "definition_site": "00a69f44",
      "incomplete_value": true,
      "site": "00a69f48",
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
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6a138",
      "incomplete_value": true,
      "site": "00a6a144",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
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
      "definition_site": "00a69f40",
      "incomplete_value": true,
      "site": "00a69f4c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
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
    "ordinal": 36,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a69e10",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00a69e18",
      "PARAM",
      [
        "storage",
        "01123af0",
        null,
        null
      ]
    ],
    [
      "00a69ea8",
      "PARAM",
      [
        "storage",
        "01123b28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00a69e10",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00a69e18",
      "PARAM",
      [
        "storage",
        "01123ef0",
        null,
        null
      ]
    ],
    [
      "00a69ea8",
      "PARAM",
      [
        "storage",
        "01123f28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a69c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69bd8.md#insn-00a69c30) · [`00a69cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69bd8.md#insn-00a69cb8) · [`00a69d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69bd8.md#insn-00a69d3c)
- 新版 `00a69e28`（命令位置の公開資料なし） · `00a69eb0`（命令位置の公開資料なし） · `00a69f34`（命令位置の公開資料なし）

~~~diff
- 00a69c30 ["INT_ADD", "register:40f0:8", ["const:a69c30:8", "const:4:8"]]
- 00a69c30 ["CALL", null, ["callee:00b110ec:8"]]
+ 00a69e28 ["INT_ADD", "register:40f0:8", ["const:a69e28:8", "const:4:8"]]
+ 00a69e28 ["CALL", null, ["callee:00b110ec:8"]]
- 00a69c30 bytes 259c0294
+ 00a69e28 bytes b19c0294
- 00a69cb8 ["INT_ADD", "register:40f0:8", ["const:a69cb8:8", "const:4:8"]]
- 00a69cb8 ["CALL", null, ["callee:0044108c:8"]]
+ 00a69eb0 ["INT_ADD", "register:40f0:8", ["const:a69eb0:8", "const:4:8"]]
+ 00a69eb0 ["CALL", null, ["callee:0044108c:8"]]
- 00a69cb8 bytes e55ce797
+ 00a69eb0 bytes 775ce797
- 00a69d3c ["INT_ADD", "register:40f0:8", ["const:a69d3c:8", "const:4:8"]]
- 00a69d3c ["CALL", null, ["callee:0044108c:8"]]
+ 00a69f34 ["INT_ADD", "register:40f0:8", ["const:a69f34:8", "const:4:8"]]
+ 00a69f34 ["CALL", null, ["callee:0044108c:8"]]
- 00a69d3c bytes c45ce797
+ 00a69f34 bytes 565ce797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d34a300e5cdd33542b4f72b0603efac3"></a>

### [`00a6a0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a0a8.md) → [`00a6a2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6a2a0.md) FUN_00a6a2a0

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a69bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69bb4.md) · 呼出先 18件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`004883f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004883f4.md) [`00493ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493ae0.md)
- 新版 呼出元 1件 [`00a69dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69dac.md) · 呼出先 18件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md) [`00493b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493b20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 82.61% / 新版 82.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 17件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6a0a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6a0a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6a0ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a6a0a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6a0ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6a0b0",
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
      "00a6a2a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a6a2a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a6a2a8",
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

- 旧版 [`00a6a0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a0a8.md#insn-00a6a0a8) · [`00a6a0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a0a8.md#insn-00a6a0ac) · [`00a6a0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a0a8.md#insn-00a6a0b0)

~~~diff
- 00a6a0a8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a6a0a8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a6a0a8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00a6a0a8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a6a0a8 bytes fd7bbaa9
- 00a6a0ac ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a6a0ac ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a6a0ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a6a0ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6a0ac bytes fc6f01a9
- 00a6a0b0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a6a0b0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a6a0b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a6a0b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6a0b0 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1828681cb800f482f95fc66cde2e6e8b"></a>

### [`00a6a740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a740.md) → [`00a6a938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6a938.md) FUN_00a6a938

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`009d79e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d79e0.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 3件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`009d7b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d7/009d7b7c.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "00a6a9b0",
      "incomplete_value": false,
      "site": "00a6a9b4",
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
      "definition_site": "00a6a7b8",
      "incomplete_value": false,
      "site": "00a6a7bc",
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
      "00a6a9b0",
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
      "00a6a9b0",
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

- 旧版 [`00a6a7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a740.md#insn-00a6a7bc) · [`00a6a7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a740.md#insn-00a6a7b8)
- 新版 `00a6a9b4`（命令位置の公開資料なし） · `00a6a9b0`（命令位置の公開資料なし）

~~~diff
- 00a6a7bc ["INT_ADD", "register:40f0:8", ["const:a6a7bc:8", "const:4:8"]]
- 00a6a7bc ["CALL", null, ["callee:00442930:8"]]
+ 00a6a9b4 ["INT_ADD", "register:40f0:8", ["const:a6a9b4:8", "const:4:8"]]
+ 00a6a9b4 ["CALL", null, ["callee:00442930:8"]]
- 00a6a7bc bytes 4d60e797
+ 00a6a9b4 bytes df5fe797
- 00a6a7b8 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00a6a7b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a6a7b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a6a7b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a6a9b0 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00a6a9b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6a9b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6a9b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a6a7b8 bytes 00c00391
+ 00a6a9b0 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-814582fe349e41a427072499b752b11a"></a>

### [`00a6a7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a7d0.md) → [`00a6a9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6a9c8.md) FUN_00a6a9c8

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`007ca4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007ca4e8.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007dd324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd324.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 6件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`007ca528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca528.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007dd364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd364.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a6aa30",
      "incomplete_value": false,
      "site": "00a6aa34",
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
      "definition_site": "00a6a838",
      "incomplete_value": false,
      "site": "00a6a83c",
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
      "00a6aa30",
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
      "00a6aa30",
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

- 旧版 [`00a6a83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a7d0.md#insn-00a6a83c) · [`00a6a838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a7d0.md#insn-00a6a838)
- 新版 `00a6aa34`（命令位置の公開資料なし） · `00a6aa30`（命令位置の公開資料なし）

~~~diff
- 00a6a83c ["INT_ADD", "register:40f0:8", ["const:a6a83c:8", "const:4:8"]]
- 00a6a83c ["CALL", null, ["callee:00442930:8"]]
+ 00a6aa34 ["INT_ADD", "register:40f0:8", ["const:a6aa34:8", "const:4:8"]]
+ 00a6aa34 ["CALL", null, ["callee:00442930:8"]]
- 00a6a83c bytes 2d60e797
+ 00a6aa34 bytes bf5fe797
- 00a6a838 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00a6a838 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a6a838 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a6a838 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a6aa30 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00a6aa30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6aa30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6aa30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a6a838 bytes 00c00391
+ 00a6aa30 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93c20f40c0ef04eef0f4d13fd97d3a18"></a>

### [`00a6a858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a858.md) → [`00a6aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6aa50.md) FUN_00a6aa50

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00937f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937f14.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`009380b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/009380b0.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a6aaac",
      "incomplete_value": false,
      "site": "00a6aab0",
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
      "definition_site": "00a6a8b4",
      "incomplete_value": false,
      "site": "00a6a8b8",
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
      "00a6aaac",
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
      "00a6aaac",
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

- 旧版 [`00a6a8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a858.md#insn-00a6a8b8) · [`00a6a8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a858.md#insn-00a6a8b4)
- 新版 `00a6aab0`（命令位置の公開資料なし） · `00a6aaac`（命令位置の公開資料なし）

~~~diff
- 00a6a8b8 ["INT_ADD", "register:40f0:8", ["const:a6a8b8:8", "const:4:8"]]
- 00a6a8b8 ["CALL", null, ["callee:00442930:8"]]
+ 00a6aab0 ["INT_ADD", "register:40f0:8", ["const:a6aab0:8", "const:4:8"]]
+ 00a6aab0 ["CALL", null, ["callee:00442930:8"]]
- 00a6a8b8 bytes 0e60e797
+ 00a6aab0 bytes a05fe797
- 00a6a8b4 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00a6a8b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a6a8b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a6a8b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a6aaac ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00a6aaac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6aaac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6aaac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a6a8b4 bytes 00c00391
+ 00a6aaac bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d44fdd78830ec338df31f1b9046cabe8"></a>

### [`00a6aaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6aaa4.md) → [`00a6ac9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6ac9c.md) FUN_00a6ac9c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a6ac98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ac98.md) · 呼出先 9件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00a6b518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b518.md) [`00a6b520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b520.md) [`00a6c018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c018.md) [`00a6c290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c290.md)
- 新版 呼出元 1件 [`00a6ae90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6ae90.md) · 呼出先 9件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00a6b710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6b/00a6b710.md) [`00a6b718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6b/00a6b718.md) [`00a6c210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c210.md) [`00a6c488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c488.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 82.41% / 新版 82.41%

CFGの説明率　旧版 25.00% / 新版 22.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6ab70"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6ac44"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a6ad38"
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
      "00a6ace4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6ae30"
      ]
    ],
    [
      "00a6acec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6ae30"
      ]
    ],
    [
      "00a6ad04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a6ac38"
      ]
    ]
  ],
  "added": [
    [
      "00a6ace4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6ae04"
      ]
    ],
    [
      "00a6acec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6ae04"
      ]
    ],
    [
      "00a6ad04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6ae30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6aae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6aaa4.md#insn-00a6aae8) · [`00a6ab50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6aaa4.md#insn-00a6ab50) · [`00a6ab70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6aaa4.md#insn-00a6ab70)
- 新版 `00a6ace0`（命令位置の公開資料なし） · `00a6ad48`（命令位置の公開資料なし）

~~~diff
- 00a6aae8 ["INT_ADD", "register:40f0:8", ["const:a6aae8:8", "const:4:8"]]
- 00a6aae8 ["CALL", null, ["callee:00a6c488:8"]]
+ 00a6ace0 ["INT_ADD", "register:40f0:8", ["const:a6ace0:8", "const:4:8"]]
+ 00a6ace0 ["CALL", null, ["callee:00a6c488:8"]]
- 00a6aae8 bytes ea050094
+ 00a6ace0 bytes ea050094
- 00a6ab50 ["INT_ADD", "register:40f0:8", ["const:a6ab50:8", "const:4:8"]]
- 00a6ab50 ["CALL", null, ["callee:00a6b718:8"]]
+ 00a6ad48 ["INT_ADD", "register:40f0:8", ["const:a6ad48:8", "const:4:8"]]
+ 00a6ad48 ["CALL", null, ["callee:00a6b718:8"]]
- 00a6ab50 bytes 74020094
+ 00a6ad48 bytes 74020094
- 00a6ab70 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a6ab70 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00a6ab70 bytes c1020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4451f948e44c6061c58d50d4a4a29cf"></a>

### [`00a6ac98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ac98.md) → [`00a6ae90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6ae90.md) FUN_00a6ae90

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) [`00a51dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) · 呼出先 3件 [`00a6aaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6aaa4.md) [`00a6bee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6bee4.md) [`00a6c290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c290.md)
- 新版 呼出元 2件 [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) · 呼出先 3件 [`00a6ac9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6ac9c.md) [`00a6c0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c0dc.md) [`00a6c488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c488.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

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
      "site": "00a6ac98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6ac98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6ac9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a6ac98",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6ac9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6aca0",
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
      "00a6ae90",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a6ae94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a6ae98",
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

- 旧版 [`00a6ac98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ac98.md#insn-00a6ac98) · [`00a6ac9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ac98.md#insn-00a6ac9c) · [`00a6aca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ac98.md#insn-00a6aca0)

~~~diff
- 00a6ac98 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a6ac98 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a6ac98 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00a6ac98 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a6ac98 bytes fd7bbda9
- 00a6ac9c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a6ac9c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a6ac9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a6ac9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6ac9c bytes f65701a9
- 00a6aca0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a6aca0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a6aca0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a6aca0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6aca0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-641ea1fbc7759f164488a34ced358b78"></a>

### [`00a6ad34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ad34.md) → [`00a6af2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6af2c.md) FUN_00a6af2c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) · 呼出先 3件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00a69494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69494.md) [`00a69950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69950.md)
- 新版 呼出元 2件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) · 呼出先 3件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00a6968c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a6968c.md) [`00a69b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69b48.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a6afa0",
      "incomplete_value": false,
      "site": "00a6afa4",
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
      "definition_site": "00a6ada8",
      "incomplete_value": false,
      "site": "00a6adac",
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
      "00a6afa0",
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
      "00a6afa0",
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

- 旧版 [`00a6adac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ad34.md#insn-00a6adac) · [`00a6ad44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ad34.md#insn-00a6ad44) · [`00a6ada8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ad34.md#insn-00a6ada8)
- 新版 `00a6afa4`（命令位置の公開資料なし） · `00a6af3c`（命令位置の公開資料なし） · `00a6afa0`（命令位置の公開資料なし）

~~~diff
- 00a6adac ["INT_ADD", "register:40f0:8", ["const:a6adac:8", "const:4:8"]]
- 00a6adac ["CALL", null, ["callee:00442930:8"]]
+ 00a6afa4 ["INT_ADD", "register:40f0:8", ["const:a6afa4:8", "const:4:8"]]
+ 00a6afa4 ["CALL", null, ["callee:00442930:8"]]
- 00a6adac bytes d15ee797
+ 00a6afa4 bytes 635ee797
- 00a6ad44 ["INT_ADD", "register:40f0:8", ["const:a6ad44:8", "const:4:8"]]
- 00a6ad44 ["CALL", null, ["callee:00a6968c:8"]]
+ 00a6af3c ["INT_ADD", "register:40f0:8", ["const:a6af3c:8", "const:4:8"]]
+ 00a6af3c ["CALL", null, ["callee:00a6968c:8"]]
- 00a6ad44 bytes d4f9ff97
+ 00a6af3c bytes d4f9ff97
- 00a6ada8 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00a6ada8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a6ada8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a6ada8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a6afa0 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00a6afa0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6afa0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6afa0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a6ada8 bytes 00c00391
+ 00a6afa0 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eb26acf287834107ad5eeaccac57767"></a>

### [`00a6add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6add8.md) → [`00a6afd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6afd0.md) FUN_00a6afd0

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "00a6afd4",
      "incomplete_value": false,
      "site": "00a6afd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6addc",
      "incomplete_value": false,
      "site": "00a6ade0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "00a6afd8",
      "DATA",
      [
        "storage",
        "00c8b500",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a6afd8",
      "DATA",
      [
        "storage",
        "00c8b900",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6addc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6add8.md#insn-00a6addc)
- 新版 `00a6afd4`（命令位置の公開資料なし）

~~~diff
- 00a6addc ["COPY", "tmp:0:8", ["const:500:8"]]
- 00a6addc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6addc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6addc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6afd4 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 00a6afd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6afd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6afd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6addc bytes 08011491
+ 00a6afd4 bytes 08012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6496c72375ebf42d563373a2634b92ab"></a>

### [`00a6ade8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ade8.md) → [`00a6afe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6afe0.md) FUN_00a6afe0

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00a6aff0",
      "incomplete_value": false,
      "site": "00a6aff8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6adf8",
      "incomplete_value": false,
      "site": "00a6ae00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "00a6aff8",
      "DATA",
      [
        "storage",
        "00c8b500",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a6aff8",
      "DATA",
      [
        "storage",
        "00c8b900",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6adf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ade8.md#insn-00a6adf8) · [`00a6ae04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ade8.md#insn-00a6ae04)
- 新版 `00a6aff0`（命令位置の公開資料なし） · `00a6affc`（命令位置の公開資料なし）

~~~diff
- 00a6adf8 ["COPY", "tmp:0:8", ["const:500:8"]]
- 00a6adf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6adf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6adf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6aff0 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 00a6aff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6aff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6aff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6adf8 bytes 08011491
+ 00a6aff0 bytes 08012491
- 00a6ae04 ["INT_ADD", "register:40f0:8", ["const:a6ae04:8", "const:4:8"]]
- 00a6ae04 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00a6affc ["INT_ADD", "register:40f0:8", ["const:a6affc:8", "const:4:8"]]
+ 00a6affc ["CALL", null, ["callee:00c57ea0:8"]]
- 00a6ae04 bytes 27b30794
+ 00a6affc bytes a9b30794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-269d1bbf74a87a8665acd127099404a1"></a>

### [`00a6ae28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ae28.md) → [`00a6b020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6b/00a6b020.md) FUN_00a6b020

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a692b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a692b8.md) · 呼出先 4件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00a694b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a694b0.md) · 呼出先 4件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 58.62% / 新版 54.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6aeb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6aec0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a6b0ac"
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
      "00a6b094",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a6aeb8"
      ]
    ],
    [
      "unmatched:00a6aeb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6b09c"
      ]
    ],
    [
      "unmatched:00a6aec0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6b0c0"
      ]
    ]
  ],
  "added": [
    [
      "00a6b094",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6b0b0"
      ]
    ],
    [
      "00a6b0ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6b09c"
      ]
    ],
    [
      "00a6b0b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6b0c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6aeb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ae28.md#insn-00a6aeb4) · [`00a6aec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ae28.md#insn-00a6aec0) · [`00a6af00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ae28.md#insn-00a6af00)

~~~diff
- 00a6aeb4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a6aeb4 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00a6aeb4 bytes 81ffff54
- 00a6aec0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a6aec0 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00a6aec0 bytes 41000054
- 00a6af00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6af00 ["INT_ADD", "register:40f0:8", ["const:a6af00:8", "const:4:8"]]
- 00a6af00 ["CALLIND", null, ["register:0:8"]]
- 00a6af00 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-345945d7df2390525f7e5e5fe42229cb"></a>

### [`00a6af24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6af24.md) → [`00a6b11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6b/00a6b11c.md) _INIT_222

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.36% / 新版 67.36%

CFGの説明率　旧版 38.18% / 新版 39.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6af28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6af28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6af2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a6af28",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6af2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6af30",
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
      "00a6b120",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a6b124",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a6b128",
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

- 旧版 [`00a6af28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6af24.md#insn-00a6af28) · [`00a6af2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6af24.md#insn-00a6af2c) · [`00a6af30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6af24.md#insn-00a6af30)

~~~diff
- 00a6af28 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a6af28 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a6af28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00a6af28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6af28 bytes fd7b10a9
- 00a6af2c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a6af2c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a6af2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00a6af2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6af2c bytes fc5711a9
- 00a6af30 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a6af30 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a6af30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00a6af30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6af30 bytes f44f12a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7642ab1062cc5817f11766193d7a41ee"></a>

### [`00a6b610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b610.md) → [`00a6b808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6b/00a6b808.md) FUN_00a6b808

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a6c020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c020.md) · 呼出先 12件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)
- 新版 呼出元 1件 [`00a6c218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c218.md) · 呼出先 12件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.86% / 新版 90.86%

CFGの説明率　旧版 76.26% / 新版 76.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 2件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6be68",
      "incomplete_value": false,
      "site": "00a6be68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6bc70",
      "incomplete_value": false,
      "site": "00a6bc70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "ordinal": 65,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6be90",
      "incomplete_value": false,
      "site": "00a6be90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6bc98",
      "incomplete_value": false,
      "site": "00a6bc98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:590:8"
          ]
        ]
      ]
    },
    "ordinal": 71,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6b938"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a6b844",
      "PARAM",
      [
        "storage",
        "01123b70",
        null,
        "undefined1"
      ]
    ],
    [
      "00a6b87c",
      "PARAM",
      [
        "storage",
        "01123b88",
        null,
        "undefined1"
      ]
    ],
    [
      "00a6b8d8",
      "PARAM",
      [
        "storage",
        "01123ba0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00a6b844",
      "PARAM",
      [
        "storage",
        "01123f70",
        null,
        "undefined1"
      ]
    ],
    [
      "00a6b87c",
      "PARAM",
      [
        "storage",
        "01123f88",
        null,
        "undefined1"
      ]
    ],
    [
      "00a6b8d8",
      "PARAM",
      [
        "storage",
        "01123fa0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6b654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b610.md#insn-00a6b654) · [`00a6b68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b610.md#insn-00a6b68c) · [`00a6b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b610.md#insn-00a6b6f8)
- 新版 `00a6b84c`（命令位置の公開資料なし） · `00a6b884`（命令位置の公開資料なし） · `00a6b8f0`（命令位置の公開資料なし）

~~~diff
- 00a6b654 ["INT_ADD", "register:40f0:8", ["const:a6b654:8", "const:4:8"]]
- 00a6b654 ["CALL", null, ["callee:0044108c:8"]]
+ 00a6b84c ["INT_ADD", "register:40f0:8", ["const:a6b84c:8", "const:4:8"]]
+ 00a6b84c ["CALL", null, ["callee:0044108c:8"]]
- 00a6b654 bytes 7e56e797
+ 00a6b84c bytes 1056e797
- 00a6b68c ["INT_ADD", "register:40f0:8", ["const:a6b68c:8", "const:4:8"]]
- 00a6b68c ["CALL", null, ["callee:0044108c:8"]]
+ 00a6b884 ["INT_ADD", "register:40f0:8", ["const:a6b884:8", "const:4:8"]]
+ 00a6b884 ["CALL", null, ["callee:0044108c:8"]]
- 00a6b68c bytes 7056e797
+ 00a6b884 bytes 0256e797
- 00a6b6f8 ["INT_ADD", "register:40f0:8", ["const:a6b6f8:8", "const:4:8"]]
- 00a6b6f8 ["CALL", null, ["callee:0044108c:8"]]
+ 00a6b8f0 ["INT_ADD", "register:40f0:8", ["const:a6b8f0:8", "const:4:8"]]
+ 00a6b8f0 ["CALL", null, ["callee:0044108c:8"]]
- 00a6b6f8 bytes 5556e797
+ 00a6b8f0 bytes e755e797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44dd113968d3f1430a79be3a437cbc48"></a>

### [`00a6be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6be98.md) → [`00a6c090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c090.md) FUN_00a6c090

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6c0b0",
      "incomplete_value": false,
      "site": "00a6c0b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6beb8",
      "incomplete_value": false,
      "site": "00a6bec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "00a6c0b8",
      "DATA",
      [
        "storage",
        "00c8b550",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00a6c0b8",
      "DATA",
      [
        "storage",
        "00c8b950",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6beb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6be98.md#insn-00a6beb8) · [`00a6bec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6be98.md#insn-00a6bec4)
- 新版 `00a6c0b0`（命令位置の公開資料なし） · `00a6c0bc`（命令位置の公開資料なし）

~~~diff
- 00a6beb8 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00a6beb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6beb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6beb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6c0b0 ["COPY", "tmp:0:8", ["const:950:8"]]
+ 00a6c0b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6c0b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6c0b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6beb8 bytes 08411591
+ 00a6c0b0 bytes 08412591
- 00a6bec4 ["INT_ADD", "register:40f0:8", ["const:a6bec4:8", "const:4:8"]]
- 00a6bec4 ["CALL", null, ["callee:005c179c:8"]]
+ 00a6c0bc ["INT_ADD", "register:40f0:8", ["const:a6c0bc:8", "const:4:8"]]
+ 00a6c0bc ["CALL", null, ["callee:005c179c:8"]]
- 00a6bec4 bytes 2656ed97
+ 00a6c0bc bytes b855ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cabecd168b86e3e96d003f249fb0706"></a>

### [`00a6bf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6bf40.md) → [`00a6c138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c138.md) FUN_00a6c138

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`00a6a8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a8d4.md) · 呼出先 1件 [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md)
- 新版 呼出元 1件 [`00a6aacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6aacc.md) · 呼出先 1件 [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a6bf64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0054075c"
      ]
    ]
  ],
  "added": [
    [
      "00a6c15c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0054075c"
      ]
    ]
  ]
}
~~~


<a id="compare-dd8c912c782bfc99e34b3f5d1f5dec6e"></a>

### [`00a6bf68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6bf68.md) → [`00a6c160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c160.md) FUN_00a6c160

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a6a8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a8d4.md) · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00a6aacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6aacc.md) · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6bf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6bf68.md#insn-00a6bf90) · [`00a6bf98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6bf68.md#insn-00a6bf98) · [`00a6bfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6bf68.md#insn-00a6bfb0)
- 新版 `00a6c188`（命令位置の公開資料なし） · `00a6c190`（命令位置の公開資料なし） · `00a6c1a8`（命令位置の公開資料なし）

~~~diff
- 00a6bf90 ["INT_RIGHT", "tmp:0:8", ["register:40a8:8", "const:3f:4"]]
- 00a6bf90 ["INT_AND", "tmp:1:8", ["tmp:0:8", "const:1:8"]]
- 00a6bf90 ["INT_EQUAL", "tmp:2:1", ["tmp:1:8", "const:0:8"]]
- 00a6bf90 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00a6c188 ["INT_RIGHT", "tmp:0:8", ["register:40a8:8", "const:3f:4"]]
+ 00a6c188 ["INT_AND", "tmp:1:8", ["tmp:0:8", "const:1:8"]]
+ 00a6c188 ["INT_EQUAL", "tmp:2:1", ["tmp:1:8", "const:0:8"]]
+ 00a6c188 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00a6bf90 bytes d501f8b7
+ 00a6c188 bytes d501f8b7
- 00a6bf98 ["INT_ADD", "register:40f0:8", ["const:a6bf98:8", "const:4:8"]]
- 00a6bf98 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a6c190 ["INT_ADD", "register:40f0:8", ["const:a6c190:8", "const:4:8"]]
+ 00a6c190 ["CALL", null, ["callee:00c57e90:8"]]
- 00a6bf98 bytes beae0794
+ 00a6c190 bytes 40af0794
- 00a6bfb0 ["INT_ADD", "register:40f0:8", ["const:a6bfb0:8", "const:4:8"]]
- 00a6bfb0 ["CALL", null, ["callee:00c58000:8"]]
+ 00a6c1a8 ["INT_ADD", "register:40f0:8", ["const:a6c1a8:8", "const:4:8"]]
+ 00a6c1a8 ["CALL", null, ["callee:00c58000:8"]]
- 00a6bfb0 bytes 14af0794
+ 00a6c1a8 bytes 96af0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59227f5766b978110630eb46fcdfd405"></a>

### [`00a6c020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c020.md) → [`00a6c218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c218.md) FUN_00a6c218

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a6a0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a0a8.md) · 呼出先 8件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00493ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493ae0.md) [`0086bc14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bc14.md) [`00a6b610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b610.md)
- 新版 呼出元 1件 [`00a6a2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6a2a0.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00493b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493b20.md) [`0086bc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bc54.md) [`00a6b808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6b/00a6b808.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.02% / 新版 87.02%

CFGの説明率　旧版 80.00% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6c024"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6c024"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6c028"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a6c024",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6c028",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6c02c",
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
      "00a6c21c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a6c220",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a6c224",
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

- 旧版 [`00a6c024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c020.md#insn-00a6c024) · [`00a6c028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c020.md#insn-00a6c028) · [`00a6c02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c020.md#insn-00a6c02c)

~~~diff
- 00a6c024 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a6c024 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a6c024 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a6c024 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6c024 bytes fd7b02a9
- 00a6c028 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a6c028 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a6c028 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00a6c028 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6c028 bytes fc6f03a9
- 00a6c02c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a6c02c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a6c02c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a6c02c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6c02c bytes fa6704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1645f655c1f84e7c5358b85383ca2815"></a>

### [`00a6c290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c290.md) → [`00a6c488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c488.md) FUN_00a6c488

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00a68d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68d5c.md) [`00a68d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68d90.md) [`00a6a8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a8d4.md) [`00a6aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6aa10.md) [`00a6aaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6aaa4.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 6件 [`00a68f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68f54.md) [`00a68f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68f88.md) [`00a6aacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6aacc.md) [`00a6ac08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6ac08.md) [`00a6ac9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6ac9c.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "00a6c530",
      "incomplete_value": false,
      "site": "00a6c534",
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
      "definition_site": "00a6c338",
      "incomplete_value": false,
      "site": "00a6c33c",
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
      "00a6c530",
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
      "00a6c530",
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

- 旧版 [`00a6c33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c290.md#insn-00a6c33c) · [`00a6c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c290.md#insn-00a6c338)
- 新版 `00a6c534`（命令位置の公開資料なし） · `00a6c530`（命令位置の公開資料なし）

~~~diff
- 00a6c33c ["INT_ADD", "register:40f0:8", ["const:a6c33c:8", "const:4:8"]]
- 00a6c33c ["CALL", null, ["callee:00442930:8"]]
+ 00a6c534 ["INT_ADD", "register:40f0:8", ["const:a6c534:8", "const:4:8"]]
+ 00a6c534 ["CALL", null, ["callee:00442930:8"]]
- 00a6c33c bytes 6d59e797
+ 00a6c534 bytes ff58e797
- 00a6c338 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00a6c338 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a6c338 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a6c338 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a6c530 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00a6c530 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6c530 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6c530 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a6c338 bytes 00c00391
+ 00a6c530 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6ca10308ef262e02255cd5e714d4895"></a>

### [`00a6c37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c37c.md) → [`00a6c574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c574.md) FUN_00a6c574

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6c590",
      "incomplete_value": false,
      "site": "00a6c598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6c398",
      "incomplete_value": false,
      "site": "00a6c3a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "00a6c598",
      "DATA",
      [
        "storage",
        "00c8b550",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00a6c598",
      "DATA",
      [
        "storage",
        "00c8b950",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6c398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c37c.md#insn-00a6c398) · [`00a6c3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c37c.md#insn-00a6c3a4)
- 新版 `00a6c590`（命令位置の公開資料なし） · `00a6c59c`（命令位置の公開資料なし）

~~~diff
- 00a6c398 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00a6c398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6c398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6c398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6c590 ["COPY", "tmp:0:8", ["const:950:8"]]
+ 00a6c590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6c590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6c590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6c398 bytes 08411591
+ 00a6c590 bytes 08412591
- 00a6c3a4 ["INT_ADD", "register:40f0:8", ["const:a6c3a4:8", "const:4:8"]]
- 00a6c3a4 ["CALL", null, ["callee:005c179c:8"]]
+ 00a6c59c ["INT_ADD", "register:40f0:8", ["const:a6c59c:8", "const:4:8"]]
+ 00a6c59c ["CALL", null, ["callee:005c179c:8"]]
- 00a6c3a4 bytes ee54ed97
+ 00a6c59c bytes 8054ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f3db2746439c5f70f7ea6437c971a64"></a>

### [`00a6c954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c954.md) → [`00a6cb4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6cb4c.md) _INIT_224

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 51.41% / 新版 51.41%

CFGの説明率　旧版 37.14% / 新版 38.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 38件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6c958"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6c958"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6c95c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a6c958",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6c95c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6c960",
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
      "00a6cb50",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a6cb54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a6cb58",
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

- 旧版 [`00a6c958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c954.md#insn-00a6c958) · [`00a6c95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c954.md#insn-00a6c95c) · [`00a6c960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c954.md#insn-00a6c960)

~~~diff
- 00a6c958 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a6c958 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a6c958 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00a6c958 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6c958 bytes fd7b0fa9
- 00a6c95c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a6c95c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a6c95c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00a6c95c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6c95c bytes fc5710a9
- 00a6c960 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a6c960 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a6c960 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00a6c960 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6c960 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bac157e658929f84f4723b7d2eee7f07"></a>

### [`00a6cce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6cce4.md) → [`00a6cedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6cedc.md) FUN_00a6cedc

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a6dadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6d/00a6dadc.md) · 呼出先 13件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0067e15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e15c.md)
- 新版 呼出元 1件 [`00a6dcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6d/00a6dcd4.md) · 呼出先 13件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0067e19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e19c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.36% / 新版 46.36%

CFGの説明率　旧版 32.88% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_value` 2件, `unresolved_branch_alignment` 31件, `unresolved_call_alignment` 45件, `unresolved_store_alignment` 113件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6cce8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6cce8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6ccec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a6cce8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6ccec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6ccf0",
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
      "00a6cee0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a6cee4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a6cee8",
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

- 旧版 [`00a6cce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6cce4.md#insn-00a6cce8) · [`00a6ccec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6cce4.md#insn-00a6ccec) · [`00a6ccf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6cce4.md#insn-00a6ccf0)

~~~diff
- 00a6cce8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a6cce8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a6cce8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00a6cce8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6cce8 bytes fd7b0ca9
- 00a6ccec ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a6ccec ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a6ccec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00a6ccec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6ccec bytes fc670da9
- 00a6ccf0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a6ccf0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a6ccf0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00a6ccf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6ccf0 bytes f85f0ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f98f6a233b1c475b861da0ee3f823d8b"></a>

### [`00a6dadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6d/00a6dadc.md) → [`00a6dcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6d/00a6dcd4.md) FUN_00a6dcd4

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 15件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00752b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/00752b90.md) [`009cc9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc9e0.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 15件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00752bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00752/00752bd0.md) [`009ccb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009cc/009ccb7c.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.91% / 新版 46.91%

CFGの説明率　旧版 11.76% / 新版 11.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 17件, `store_destination` 3件, `store_value` 2件, `unresolved_branch_alignment` 21件, `unresolved_call_alignment` 28件, `unresolved_store_alignment` 38件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a6dd18",
      "incomplete_value": false,
      "site": "00a6dd18",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6db20",
      "incomplete_value": false,
      "site": "00a6db20",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6dd10",
      "incomplete_value": true,
      "site": "00a6dd18",
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
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6db18",
      "incomplete_value": true,
      "site": "00a6db20",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a6dd1c",
      "incomplete_value": false,
      "site": "00a6dd1c",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6db24",
      "incomplete_value": false,
      "site": "00a6db24",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a6dd10",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00a6dd14",
      "READ",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ],
    [
      "00a6dd18",
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
      "00a6dd10",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00a6dd14",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "00a6dd18",
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

- 旧版 [`00a6db20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6d/00a6dadc.md#insn-00a6db20) · [`00a6db24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6d/00a6dadc.md#insn-00a6db24) · [`00a6db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6d/00a6dadc.md#insn-00a6db64)
- 新版 `00a6dd18`（命令位置の公開資料なし） · `00a6dd1c`（命令位置の公開資料なし） · `00a6dd5c`（命令位置の公開資料なし）

~~~diff
- 00a6db20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
- 00a6db20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00a6dd18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
+ 00a6dd18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00a6db20 bytes 09b502f9
+ 00a6dd18 bytes 09b504f9
- 00a6db24 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:578:8"]]
- 00a6db24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00a6dd1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:978:8"]]
+ 00a6dd1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00a6db24 bytes aabe02f9
+ 00a6dd1c bytes aabe04f9
- 00a6db64 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:578:8"]]
- 00a6db64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00a6dd5c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:978:8"]]
+ 00a6dd5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00a6db64 bytes b4be02f9
+ 00a6dd5c bytes b4be04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0244f69384694a61de8561859d8692d4"></a>

### [`00a6e110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6e/00a6e110.md) → [`00a6e308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6e/00a6e308.md) FUN_00a6e308

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 10件 [`0046ed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ed4c.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00859b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b0c.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 10件 [`0046ed8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ed8c.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00859b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b4c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.76% / 新版 88.76%

CFGの説明率　旧版 38.76% / 新版 38.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6e110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6e110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6e114"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a6e110",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6e114",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6e118",
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
      "00a6e308",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a6e30c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a6e310",
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

- 旧版 [`00a6e110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6e/00a6e110.md#insn-00a6e110) · [`00a6e114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6e/00a6e110.md#insn-00a6e114) · [`00a6e118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6e/00a6e110.md#insn-00a6e118)

~~~diff
- 00a6e110 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a6e110 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a6e110 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00a6e110 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a6e110 bytes fd7bbba9
- 00a6e114 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a6e114 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00a6e114 bytes f90b00f9
- 00a6e118 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a6e118 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a6e118 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a6e118 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6e118 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-014e216c883a09878718f655ab32339e"></a>

### [`00a6e6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6e/00a6e6a0.md) → [`00a6e898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6e/00a6e898.md) FUN_00a6e898

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 20件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`00468c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 20件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00468c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.90% / 新版 96.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 23件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a6e8d4",
      "incomplete_value": true,
      "site": "00a6e8d4",
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
      "definition_site": "00a6e6dc",
      "incomplete_value": true,
      "site": "00a6e6dc",
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
      "definition_site": "00a6e8e4",
      "incomplete_value": false,
      "site": "00a6e8f8",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6e6ec",
      "incomplete_value": false,
      "site": "00a6e700",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a6e8ec",
      "incomplete_value": false,
      "site": "00a6e8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6e6f4",
      "incomplete_value": false,
      "site": "00a6e700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
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
      "00a6e8d0",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00a6e8e4",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a6e8ec",
      "PARAM",
      [
        "storage",
        "00c87bd8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a6e8d0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00a6e8e4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a6e8ec",
      "PARAM",
      [
        "storage",
        "00c87fd8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6e700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6e/00a6e6a0.md#insn-00a6e700) · [`00a6e738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6e/00a6e6a0.md#insn-00a6e738) · [`00a6e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6e/00a6e6a0.md#insn-00a6e740)
- 新版 `00a6e8f8`（命令位置の公開資料なし） · `00a6e930`（命令位置の公開資料なし） · `00a6e938`（命令位置の公開資料なし）

~~~diff
- 00a6e700 ["INT_ADD", "register:40f0:8", ["const:a6e700:8", "const:4:8"]]
- 00a6e700 ["CALL", null, ["callee:00c58610:8"]]
+ 00a6e8f8 ["INT_ADD", "register:40f0:8", ["const:a6e8f8:8", "const:4:8"]]
+ 00a6e8f8 ["CALL", null, ["callee:00c58610:8"]]
- 00a6e700 bytes c4a60794
+ 00a6e8f8 bytes 46a70794
- 00a6e738 ["INT_ADD", "register:40f0:8", ["const:a6e738:8", "const:4:8"]]
- 00a6e738 ["CALL", null, ["ram:46c984:8"]]
+ 00a6e930 ["INT_ADD", "register:40f0:8", ["const:a6e930:8", "const:4:8"]]
+ 00a6e930 ["CALL", null, ["ram:46c9c4:8"]]
- 00a6e738 bytes 93f8e797
+ 00a6e930 bytes 25f8e797
- 00a6e740 ["INT_ADD", "register:40f0:8", ["const:a6e740:8", "const:4:8"]]
- 00a6e740 ["CALL", null, ["callee:008514f8:8"]]
+ 00a6e938 ["INT_ADD", "register:40f0:8", ["const:a6e938:8", "const:4:8"]]
+ 00a6e938 ["CALL", null, ["callee:008514f8:8"]]
- 00a6e740 bytes 5e8bf797
+ 00a6e938 bytes f08af797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b130de189c01e2b19055cd84c251bc8"></a>

### [`00a6f43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f43c.md) → [`00a6f634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6f/00a6f634.md) FUN_00a6f634

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a6f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f55c.md) · 呼出先 4件 [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00a6f754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6f/00a6f754.md) · 呼出先 4件 [`00672748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672748.md) [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6f650",
      "incomplete_value": false,
      "site": "00a6f654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6f458",
      "incomplete_value": false,
      "site": "00a6f45c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "definition_site": "00a6f70c",
      "incomplete_value": false,
      "site": "00a6f710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6f514",
      "incomplete_value": false,
      "site": "00a6f518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:410:8"
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
      "00a6f654",
      "DATA",
      [
        "storage",
        "00c8b5e0",
        null,
        "pointer"
      ]
    ],
    [
      "00a6f710",
      "DATA",
      [
        "storage",
        "00c74410",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a6f654",
      "DATA",
      [
        "storage",
        "00c8b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00a6f710",
      "DATA",
      [
        "storage",
        "00c74810",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6f458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f43c.md#insn-00a6f458) · [`00a6f46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f43c.md#insn-00a6f46c) · [`00a6f480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f43c.md#insn-00a6f480)
- 新版 `00a6f650`（命令位置の公開資料なし） · `00a6f664`（命令位置の公開資料なし） · `00a6f678`（命令位置の公開資料なし）

~~~diff
- 00a6f458 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 00a6f458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6f458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6f458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6f650 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00a6f650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6f650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6f650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6f458 bytes 08811791
+ 00a6f650 bytes 08812791
- 00a6f46c ["INT_ADD", "register:40f0:8", ["const:a6f46c:8", "const:4:8"]]
- 00a6f46c ["CALL", null, ["callee:00c53d00:8"]]
+ 00a6f664 ["INT_ADD", "register:40f0:8", ["const:a6f664:8", "const:4:8"]]
+ 00a6f664 ["CALL", null, ["callee:00c53d00:8"]]
- 00a6f46c bytes 1d910794
+ 00a6f664 bytes a7910794
- 00a6f480 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6f480 ["INT_ADD", "register:40f0:8", ["const:a6f480:8", "const:4:8"]]
- 00a6f480 ["CALLIND", null, ["register:0:8"]]
+ 00a6f678 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a6f678 ["INT_ADD", "register:40f0:8", ["const:a6f678:8", "const:4:8"]]
+ 00a6f678 ["CALLIND", null, ["register:0:8"]]
- 00a6f480 bytes 00013fd6
+ 00a6f678 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80a37582fec77113fa77ceedf41cafb1"></a>

### [`00a6f580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f580.md) → [`00a6f778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6f/00a6f778.md) _INIT_225

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.19% / 新版 71.19%

CFGの説明率　旧版 30.77% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6f5b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6f5d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6f5fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a6f5b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6f5bc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a6f5d8",
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
      "00a6f7a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a6f7b4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00a6f7d0",
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

- 旧版 [`00a6f5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f580.md#insn-00a6f5b0) · [`00a6f5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f580.md#insn-00a6f5d8) · [`00a6f5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f580.md#insn-00a6f5fc)

~~~diff
- 00a6f5b0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a6f5b0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a6f5b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a6f5b0 bytes a9831ff8
- 00a6f5d8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00a6f5d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a6f5d8 bytes e013813c
- 00a6f5fc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00a6f5fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a6f5fc bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d52228882444aea8378364eb15076a46"></a>

### [`00a6f910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f910.md) → [`00a6fb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6f/00a6fb08.md) FUN_00a6fb08

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 7件 [`00a83068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a83/00a83068.md) [`00a83254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a83/00a83254.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md)
- 新版 呼出元 1件 [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 7件 [`00a83260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a83260.md) [`00a8344c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a8344c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.17% / 新版 99.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a6fbd4",
      "incomplete_value": false,
      "site": "00a6fbdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:841:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6f9dc",
      "incomplete_value": false,
      "site": "00a6f9e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:801:8"
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
      "00a6fbd4",
      "PARAM",
      [
        "storage",
        "002b6801",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a6fbd4",
      "PARAM",
      [
        "storage",
        "002b6841",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6f9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f910.md#insn-00a6f9e4) · [`00a6f940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f910.md#insn-00a6f940) · [`00a6f9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f910.md#insn-00a6f9d4)
- 新版 `00a6fbdc`（命令位置の公開資料なし） · `00a6fb38`（命令位置の公開資料なし） · `00a6fbcc`（命令位置の公開資料なし）

~~~diff
- 00a6f9e4 ["INT_ADD", "register:40f0:8", ["const:a6f9e4:8", "const:4:8"]]
- 00a6f9e4 ["CALL", null, ["callee:00c57f70:8"]]
+ 00a6fbdc ["INT_ADD", "register:40f0:8", ["const:a6fbdc:8", "const:4:8"]]
+ 00a6fbdc ["CALL", null, ["callee:00c57f70:8"]]
- 00a6f9e4 bytes 63a00794
+ 00a6fbdc bytes e5a00794
- 00a6f940 ["INT_ADD", "register:40f0:8", ["const:a6f940:8", "const:4:8"]]
- 00a6f940 ["CALL", null, ["callee:00a83260:8"]]
+ 00a6fb38 ["INT_ADD", "register:40f0:8", ["const:a6fb38:8", "const:4:8"]]
+ 00a6fb38 ["CALL", null, ["callee:00a83260:8"]]
- 00a6f940 bytes ca4d0094
+ 00a6fb38 bytes ca4d0094
- 00a6f9d4 ["INT_ADD", "register:40f0:8", ["const:a6f9d4:8", "const:4:8"]]
- 00a6f9d4 ["CALL", null, ["callee:00c57f50:8"]]
+ 00a6fbcc ["INT_ADD", "register:40f0:8", ["const:a6fbcc:8", "const:4:8"]]
+ 00a6fbcc ["CALL", null, ["callee:00c57f50:8"]]
- 00a6f9d4 bytes 5fa00794
+ 00a6fbcc bytes e1a00794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b91ceed670927c78b408001b2f9e050"></a>

### [`00a6fb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6fb90.md) → [`00a6fd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6f/00a6fd88.md) FUN_00a6fd88

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 51件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md)
- 新版 呼出元 1件 [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 51件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 49.07% / 新版 49.07%

CFGの説明率　旧版 29.87% / 新版 29.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `call_target` 7件, `store_value` 18件, `unresolved_branch_alignment` 102件, `unresolved_call_alignment` 175件, `unresolved_store_alignment` 186件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6fe80",
      "incomplete_value": true,
      "site": "00a6fe84",
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6fc88",
      "incomplete_value": true,
      "site": "00a6fc8c",
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
                "const:2a0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00a6fe98",
      "incomplete_value": true,
      "site": "00a6febc",
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
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6fca0",
      "incomplete_value": true,
      "site": "00a6fcc4",
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
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:d70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6fea0",
      "incomplete_value": true,
      "site": "00a6fec0",
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
                "const:190:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6fca8",
      "incomplete_value": true,
      "site": "00a6fcc8",
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
                "const:150:8"
              ]
            ]
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
      "00a6fdd0",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00a6fde4",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a6fdec",
      "PARAM",
      [
        "storage",
        "00c74bd8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a6fdd0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00a6fde4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a6fdec",
      "PARAM",
      [
        "storage",
        "00c74fd8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6fc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6fb90.md#insn-00a6fc70) · [`00a6fcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6fb90.md#insn-00a6fcf0) · [`00a6fcf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6fb90.md#insn-00a6fcf4)
- 新版 `00a6fe68`（命令位置の公開資料なし）

~~~diff
- 00a6fc70 ["INT_ADD", "register:40f0:8", ["const:a6fc70:8", "const:4:8"]]
- 00a6fc70 ["CALL", null, ["ram:46c984:8"]]
+ 00a6fe68 ["INT_ADD", "register:40f0:8", ["const:a6fe68:8", "const:4:8"]]
+ 00a6fe68 ["CALL", null, ["ram:46c9c4:8"]]
- 00a6fc70 bytes 45f3e797
+ 00a6fe68 bytes d7f2e797
- 00a6fcf0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:b0:8"]]
- 00a6fcf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00a6fcf0 bytes c9b200b9
- 00a6fcf4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:bc:8"]]
- 00a6fcf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00a6fcf4 bytes d4be00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f3ead727f83651f1c20a55e58571756"></a>

### [`00a7239c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a72/00a7239c.md) → [`00a72594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a72/00a72594.md) FUN_00a72594

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`00693418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693418.md) [`00696290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696290.md) [`00698d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698d94.md) [`00a6fb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6fb90.md) [`00a73338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a73/00a73338.md) · 呼出先 35件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00615ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615ea0.md)
- 新版 呼出元 8件 [`00693458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693458.md) [`006962d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006962d0.md) [`00698dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698dd4.md) [`00a6fd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6f/00a6fd88.md) [`00a73530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a73/00a73530.md) · 呼出先 35件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00615ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.47% / 新版 98.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a72ae0",
      "incomplete_value": false,
      "site": "00a72ae0",
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
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a728e8",
      "incomplete_value": false,
      "site": "00a728e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:e20:8"
          ]
        ]
      ]
    },
    "ordinal": 70,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a73028",
      "incomplete_value": false,
      "site": "00a73028",
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
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a72e30",
      "incomplete_value": false,
      "site": "00a72e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "ordinal": 120,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a72670",
      "value": [
        "leaf",
        "ram:8111c8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a72478",
      "value": [
        "leaf",
        "ram:811188:8"
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
      "00a72670",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00811188"
      ]
    ],
    [
      "00a72834",
      "READ",
      [
        "storage",
        "00c9b120",
        null,
        "pointer"
      ]
    ],
    [
      "00a7283c",
      "PARAM",
      [
        "storage",
        "00310461",
        "_ZSt7nothrow",
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00a72670",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008111c8"
      ]
    ],
    [
      "00a72834",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ],
    [
      "00a7283c",
      "PARAM",
      [
        "storage",
        "003104a1",
        "_ZSt7nothrow",
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a72478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a72/00a7239c.md#insn-00a72478) · [`00a7258c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a72/00a7239c.md#insn-00a7258c) · [`00a72784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a72/00a7239c.md#insn-00a72784)
- 新版 `00a72670`（命令位置の公開資料なし） · `00a72784`（命令位置の公開資料なし） · `00a7297c`（命令位置の公開資料なし）

~~~diff
- 00a72478 ["INT_ADD", "register:40f0:8", ["const:a72478:8", "const:4:8"]]
- 00a72478 ["CALL", null, ["ram:811188:8"]]
+ 00a72670 ["INT_ADD", "register:40f0:8", ["const:a72670:8", "const:4:8"]]
+ 00a72670 ["CALL", null, ["ram:8111c8:8"]]
- 00a72478 bytes 447bf697
+ 00a72670 bytes d67af697
- 00a7258c ["INT_ADD", "register:40f0:8", ["const:a7258c:8", "const:4:8"]]
- 00a7258c ["CALL", null, ["callee:006878f4:8"]]
+ 00a72784 ["INT_ADD", "register:40f0:8", ["const:a72784:8", "const:4:8"]]
+ 00a72784 ["CALL", null, ["callee:006878f4:8"]]
- 00a7258c bytes ca54f097
+ 00a72784 bytes 5c54f097
- 00a72784 ["INT_ADD", "register:40f0:8", ["const:a72784:8", "const:4:8"]]
- 00a72784 ["CALL", null, ["ram:811630:8"]]
+ 00a7297c ["INT_ADD", "register:40f0:8", ["const:a7297c:8", "const:4:8"]]
+ 00a7297c ["CALL", null, ["ram:811670:8"]]
- 00a72784 bytes ab7bf697
+ 00a7297c bytes 3d7bf697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a58873552cfdf474e0296e8761f44c4a"></a>

### [`00a73338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a73/00a73338.md) → [`00a73530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a73/00a73530.md) FUN_00a73530

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 69件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 69件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.12% / 新版 62.12%

CFGの説明率　旧版 43.70% / 新版 43.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 23件, `call_target` 6件, `store_condition` 1件, `store_destination` 3件, `store_value` 22件, `unresolved_branch_alignment` 74件, `unresolved_call_alignment` 124件, `unresolved_store_alignment` 146件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a73584",
      "incomplete_value": false,
      "site": "00a73584",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7338c",
      "incomplete_value": false,
      "site": "00a7338c",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a7357c",
      "incomplete_value": true,
      "site": "00a73584",
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
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a73384",
      "incomplete_value": true,
      "site": "00a7338c",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a73588",
      "incomplete_value": false,
      "site": "00a73588",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a73390",
      "incomplete_value": false,
      "site": "00a73390",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a7357c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00a73580",
      "READ",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ],
    [
      "00a73584",
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
      "00a7357c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00a73580",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "00a73584",
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

- 旧版 [`00a7338c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a73/00a73338.md#insn-00a7338c) · [`00a73390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a73/00a73338.md#insn-00a73390) · [`00a733a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a73/00a73338.md#insn-00a733a0)
- 新版 `00a73584`（命令位置の公開資料なし） · `00a73588`（命令位置の公開資料なし） · `00a73598`（命令位置の公開資料なし）

~~~diff
- 00a7338c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
- 00a7338c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00a73584 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
+ 00a73584 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00a7338c bytes 09b502f9
+ 00a73584 bytes 09b504f9
- 00a73390 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:578:8"]]
- 00a73390 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00a73588 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:978:8"]]
+ 00a73588 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00a73390 bytes cabe02f9
+ 00a73588 bytes cabe04f9
- 00a733a0 ["INT_ADD", "register:40f0:8", ["const:a733a0:8", "const:4:8"]]
- 00a733a0 ["CALL", null, ["callee:00a7c4f4:8"]]
+ 00a73598 ["INT_ADD", "register:40f0:8", ["const:a73598:8", "const:4:8"]]
+ 00a73598 ["CALL", null, ["callee:00a7c4f4:8"]]
- 00a733a0 bytes d7230094
+ 00a73598 bytes d7230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eafe721f3f5c260d07e38a74c228eb44"></a>

### [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) → [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) FUN_00a75dac

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 94件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0043e7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e7e8.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 94件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.80% / 新版 86.80%

CFGの説明率　旧版 57.15% / 新版 56.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 81件, `call_target` 12件, `store_condition` 7件, `store_value` 1件, `unresolved_branch_alignment` 58件, `unresolved_call_alignment` 64件, `unresolved_store_alignment` 36件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a77460",
      "incomplete_value": true,
      "site": "00a77460",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:263:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a77268",
      "incomplete_value": true,
      "site": "00a77268",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:223:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 180,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a777b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a777b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a75f74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00811630"
      ]
    ],
    [
      "00a75fa8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ],
    [
      "00a75fcc",
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
      "00a75f74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00811670"
      ]
    ],
    [
      "00a75fa8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "00a75fcc",
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

- 旧版 [`00a777b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md#insn-00a777b0) · [`00a777b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md#insn-00a777b4) · [`00a777bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md#insn-00a777bc)

~~~diff
- 00a777b0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a777b0 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00a777b0 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:8:8"]]
- 00a777b0 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 00a777b0 bytes 1f8d00f8
- 00a777b4 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00a777b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a777b4 bytes 280000f9
- 00a777bc ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a777bc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a777bc ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a777bc ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00a777bc bytes 3ffc02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffe5358b3bd2cddca26ec57c28096861"></a>

### [`00a7989c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a7989c.md) → [`00a79a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a79/00a79a94.md) FUN_00a79a94

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00a7e63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e63c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00a7e834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e834.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.49% / 新版 70.49%

CFGの説明率　旧版 23.53% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a798a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a798a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a798a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a798a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a798a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a798a8",
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
      "00a79a98",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a79a9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a79aa0",
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

- 旧版 [`00a798a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a7989c.md#insn-00a798a0) · [`00a798a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a7989c.md#insn-00a798a4) · [`00a798a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a7989c.md#insn-00a798a8)

~~~diff
- 00a798a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a798a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a798a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a798a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a798a0 bytes fd7b02a9
- 00a798a4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a798a4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a798a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00a798a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a798a4 bytes f85f03a9
- 00a798a8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a798a8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a798a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a798a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a798a8 bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd59de5af6caad995ad41343eee97c70"></a>

### [`00a799b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a799b8.md) → [`00a79bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a79/00a79bb0.md) FUN_00a79bb0

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a799f8",
      "incomplete_value": false,
      "site": "00a799fc",
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
      "unmatched:00a799f8",
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
      "00a79bf0",
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

- 旧版 [`00a799fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a799b8.md#insn-00a799fc) · [`00a799c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a799b8.md#insn-00a799c4) · [`00a799d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a799b8.md#insn-00a799d4)
- 新版 `00a79bf4`（命令位置の公開資料なし） · `00a79bbc`（命令位置の公開資料なし） · `00a79bcc`（命令位置の公開資料なし）

~~~diff
- 00a799fc ["INT_ADD", "register:40f0:8", ["const:a799fc:8", "const:4:8"]]
- 00a799fc ["CALL", null, ["callee:00442930:8"]]
+ 00a79bf4 ["INT_ADD", "register:40f0:8", ["const:a79bf4:8", "const:4:8"]]
+ 00a79bf4 ["CALL", null, ["callee:00442930:8"]]
- 00a799fc bytes bd23e797
+ 00a79bf4 bytes 4f23e797
- 00a799c4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a799c4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00a79bbc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00a79bbc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00a799c4 bytes 880100b4
+ 00a79bbc bytes 880100b4
- 00a799d4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a799d4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00a79bcc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00a79bcc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00a799d4 bytes 080100b4
+ 00a79bcc bytes 080100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ca15bea104a6901fefe99a1ba4cad4c"></a>

### [`00a79a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a79a0c.md) → [`00a79c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a79/00a79c04.md) FUN_00a79c04

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 52件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00468c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 52件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 17.34% / 新版 17.51%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 138件, `call_target` 2件, `store_condition` 6件, `unresolved_branch_alignment` 25件, `unresolved_call_alignment` 35件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a79a2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a79a2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a79a30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a79a2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a79a30",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a79a38",
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
      "00a79c24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a79c28",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a79c30",
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

- 旧版 [`00a79a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a79a0c.md#insn-00a79a2c) · [`00a79a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a79a0c.md#insn-00a79a30) · [`00a79a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a79a0c.md#insn-00a79a38)

~~~diff
- 00a79a2c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a79a2c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a79a2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00a79a2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a79a2c bytes f65714a9
- 00a79a30 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a79a30 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a79a30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00a79a30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a79a30 bytes f44f15a9
- 00a79a38 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:80:8"]]
- 00a79a38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00a79a38 bytes e04300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ffee92e5e9cb26e3246adcf44a1772a"></a>

### [`00a7b960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7b960.md) → [`00a7bb58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7b/00a7bb58.md) FUN_00a7bb58

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7bb64",
      "incomplete_value": false,
      "site": "00a7bb64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7b96c",
      "incomplete_value": false,
      "site": "00a7b96c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "00a7bb64",
      "DATA",
      [
        "storage",
        "00c8b600",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7bb64",
      "DATA",
      [
        "storage",
        "00c8ba00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7b968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7b960.md#insn-00a7b968)
- 新版 `00a7bb60`（命令位置の公開資料なし）

~~~diff
- 00a7b968 ["COPY", "tmp:0:8", ["const:600:8"]]
- 00a7b968 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a7b968 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a7b968 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a7bb60 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00a7bb60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7bb60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7bb60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a7b968 bytes 29011891
+ 00a7bb60 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7afe1a22dd1bcc1f604de105dfdc5746"></a>

### [`00a7b97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7b97c.md) → [`00a7bb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7b/00a7bb74.md) FUN_00a7bb74

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.87% / 新版 80.87%

CFGの説明率　旧版 25.00% / 新版 23.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7ba8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7baac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7bab4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a7bbb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a7bb20"
      ]
    ],
    [
      "unmatched:00a7b9c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "unmatched:00a7b9d0",
      "READ",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a7bbb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7bd18"
      ]
    ],
    [
      "00a7bbc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a7bbc8",
      "READ",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7b9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7b97c.md#insn-00a7b9c8) · [`00a7b9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7b97c.md#insn-00a7b9d8) · [`00a7b9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7b97c.md#insn-00a7b9ec)

~~~diff
- 00a7b9c8 ["INT_ADD", "register:40f0:8", ["const:a7b9c8:8", "const:4:8"]]
- 00a7b9c8 ["CALL", null, ["ram:47acb4:8"]]
- 00a7b9c8 bytes bbfce797
- 00a7b9d8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a7b9d8 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 00a7b9d8 bytes e10d0054
- 00a7b9ec ["INT_ADD", "register:40f0:8", ["const:a7b9ec:8", "const:4:8"]]
- 00a7b9ec ["CALL", null, ["ram:47acb4:8"]]
- 00a7b9ec bytes b2fce797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bff48bcb136f50df60666f20ad667bf"></a>

### [`00a7bc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bc04.md) → [`00a7bdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7b/00a7bdfc.md) FUN_00a7bdfc

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7be10",
      "incomplete_value": false,
      "site": "00a7be14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7bc18",
      "incomplete_value": false,
      "site": "00a7bc1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "00a7be14",
      "DATA",
      [
        "storage",
        "00c8b670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7be14",
      "DATA",
      [
        "storage",
        "00c8ba70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7bc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bc04.md#insn-00a7bc10) · [`00a7bc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bc04.md#insn-00a7bc18)
- 新版 `00a7be08`（命令位置の公開資料なし） · `00a7be10`（命令位置の公開資料なし）

~~~diff
- 00a7bc10 ["INT_ADD", "register:40f0:8", ["const:a7bc10:8", "const:4:8"]]
- 00a7bc10 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a7be08 ["INT_ADD", "register:40f0:8", ["const:a7be08:8", "const:4:8"]]
+ 00a7be08 ["CALL", null, ["callee:00c57e90:8"]]
- 00a7bc10 bytes a06f0794
+ 00a7be08 bytes 22700794
- 00a7bc18 ["COPY", "tmp:0:8", ["const:670:8"]]
- 00a7bc18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7bc18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7bc18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7be10 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 00a7be10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7be10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7be10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7bc18 bytes 08c11991
+ 00a7be10 bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a04e1effd09dcb74a9bbadbb4ffa538b"></a>

### [`00a7bc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bc28.md) → [`00a7be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7b/00a7be20.md) FUN_00a7be20

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7be24",
      "incomplete_value": false,
      "site": "00a7be28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7bc2c",
      "incomplete_value": false,
      "site": "00a7bc30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "00a7be28",
      "DATA",
      [
        "storage",
        "00c8b670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7be28",
      "DATA",
      [
        "storage",
        "00c8ba70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7bc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bc28.md#insn-00a7bc2c)
- 新版 `00a7be24`（命令位置の公開資料なし）

~~~diff
- 00a7bc2c ["COPY", "tmp:0:8", ["const:670:8"]]
- 00a7bc2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7bc2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7bc2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7be24 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 00a7be24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7be24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7be24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7bc2c bytes 08c11991
+ 00a7be24 bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e6e48408671c32cfaee5ad5ff485115"></a>

### [`00a7bc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bc40.md) → [`00a7be38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7b/00a7be38.md) FUN_00a7be38

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a7bc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bc40.md#insn-00a7bc48)
- 新版 `00a7be40`（命令位置の公開資料なし）

~~~diff
- 00a7bc48 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a7bc48 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00a7be40 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a7be40 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00a7bc48 bytes 61000054
+ 00a7be40 bytes 61000054
~~~


<a id="compare-2b6cae5e84e4332930888daf7feb0d03"></a>

### [`00a7bcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bcd4.md) → [`00a7becc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7b/00a7becc.md) FUN_00a7becc

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.35% / 新版 84.35%

CFGの説明率　旧版 53.85% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7bcf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7bde4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7be04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7bcf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7bd10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7bf34"
      ]
    ],
    [
      "00a7bf18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a7bee8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a7bf08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7bf34"
      ]
    ],
    [
      "00a7bf18",
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

- 旧版 [`00a7bcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bcd4.md#insn-00a7bcf0) · [`00a7bd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bcd4.md#insn-00a7bd10) · [`00a7bd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bcd4.md#insn-00a7bd20)
- 新版 `00a7bf18`（命令位置の公開資料なし）

~~~diff
- 00a7bcf0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a7bcf0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a7bcf0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a7bcf0 bytes a8831ff8
- 00a7bd10 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00a7bd10 bytes 60010054
- 00a7bd20 ["INT_ADD", "register:40f0:8", ["const:a7bd20:8", "const:4:8"]]
- 00a7bd20 ["CALL", null, ["ram:47acb4:8"]]
+ 00a7bf18 ["INT_ADD", "register:40f0:8", ["const:a7bf18:8", "const:4:8"]]
+ 00a7bf18 ["CALL", null, ["ram:47acf4:8"]]
- 00a7bd20 bytes e5fbe797
+ 00a7bf18 bytes 77fbe797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75869a068b6d545814b04ba764d999bf"></a>

### [`00a7bf80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bf80.md) → [`00a7c178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7c/00a7c178.md) FUN_00a7c178

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7c17c",
      "incomplete_value": false,
      "site": "00a7c180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7bf84",
      "incomplete_value": false,
      "site": "00a7bf88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "00a7c180",
      "DATA",
      [
        "storage",
        "00c8b770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7c180",
      "DATA",
      [
        "storage",
        "00c8bb70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7bf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bf80.md#insn-00a7bf84)
- 新版 `00a7c17c`（命令位置の公開資料なし）

~~~diff
- 00a7bf84 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00a7bf84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7bf84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7bf84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7c17c ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00a7c17c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7c17c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7c17c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7bf84 bytes 08c11d91
+ 00a7c17c bytes 08c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74ab69ff248eeb0a485f90ccf4c8cef9"></a>

### [`00a7bfdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bfdc.md) → [`00a7c1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7c/00a7c1d4.md) FUN_00a7c1d4

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7c1f8",
      "incomplete_value": false,
      "site": "00a7c1f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7c000",
      "incomplete_value": false,
      "site": "00a7c000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "00a7c1f8",
      "DATA",
      [
        "storage",
        "00c8b800",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7c1f8",
      "DATA",
      [
        "storage",
        "00c8bc00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7bff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bfdc.md#insn-00a7bff0) · [`00a7bffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bfdc.md#insn-00a7bffc)
- 新版 `00a7c1e8`（命令位置の公開資料なし） · `00a7c1f4`（命令位置の公開資料なし）

~~~diff
- 00a7bff0 ["INT_ADD", "register:40f0:8", ["const:a7bff0:8", "const:4:8"]]
- 00a7bff0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a7c1e8 ["INT_ADD", "register:40f0:8", ["const:a7c1e8:8", "const:4:8"]]
+ 00a7c1e8 ["CALL", null, ["callee:00c57e90:8"]]
- 00a7bff0 bytes a86e0794
+ 00a7c1e8 bytes 2a6f0794
- 00a7bffc ["COPY", "tmp:0:8", ["const:800:8"]]
- 00a7bffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7bffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7bffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7c1f4 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 00a7c1f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7c1f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7c1f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7bffc bytes 08012091
+ 00a7c1f4 bytes 08013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-116378fb4fe5d75f34f3b339f8089107"></a>

### [`00a7c010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c010.md) → [`00a7c208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7c/00a7c208.md) FUN_00a7c208

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7c214",
      "incomplete_value": false,
      "site": "00a7c214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7c01c",
      "incomplete_value": false,
      "site": "00a7c01c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "00a7c214",
      "DATA",
      [
        "storage",
        "00c8b800",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7c214",
      "DATA",
      [
        "storage",
        "00c8bc00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7c018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c010.md#insn-00a7c018)
- 新版 `00a7c210`（命令位置の公開資料なし）

~~~diff
- 00a7c018 ["COPY", "tmp:0:8", ["const:800:8"]]
- 00a7c018 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a7c018 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a7c018 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a7c210 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 00a7c210 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7c210 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7c210 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a7c018 bytes 29012091
+ 00a7c210 bytes 29013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a76a069b1fcda9db43cd5841e3659a7"></a>

### [`00a7c02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c02c.md) → [`00a7c224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7c/00a7c224.md) FUN_00a7c224

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a466e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466e0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a468d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468d8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.43% / 新版 78.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c02c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c02c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c030"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7c02c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7c030",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7c050",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7c270"
      ]
    ]
  ],
  "added": [
    [
      "00a7c224",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a7c228",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a7c248",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7c270"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7c02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c02c.md#insn-00a7c02c) · [`00a7c030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c02c.md#insn-00a7c030) · [`00a7c050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c02c.md#insn-00a7c050)

~~~diff
- 00a7c02c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a7c02c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a7c02c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a7c02c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a7c02c bytes fd7bbea9
- 00a7c030 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a7c030 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a7c030 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a7c030 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7c030 bytes f44f01a9
- 00a7c050 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00a7c050 bytes 40010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35f46a817fa47ea6cf40706ce443ac7a"></a>

### [`00a7c124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c124.md) → [`00a7c31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7c/00a7c31c.md) FUN_00a7c31c

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c148"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c148"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7c340"
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
      "unmatched:00a7c148",
      "DATA",
      [
        "storage",
        "00c8b880",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a7c14c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7c150",
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
      "00a7c340",
      "DATA",
      [
        "storage",
        "00c8bc80",
        null,
        "undefined *"
      ]
    ],
    [
      "00a7c344",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a7c348",
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

- 旧版 [`00a7c138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c124.md#insn-00a7c138) · [`00a7c148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c124.md#insn-00a7c148) · [`00a7c154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c124.md#insn-00a7c154)
- 新版 `00a7c330`（命令位置の公開資料なし）

~~~diff
- 00a7c138 ["INT_ADD", "register:40f0:8", ["const:a7c138:8", "const:4:8"]]
- 00a7c138 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a7c330 ["INT_ADD", "register:40f0:8", ["const:a7c330:8", "const:4:8"]]
+ 00a7c330 ["CALL", null, ["callee:00c57e90:8"]]
- 00a7c138 bytes 566e0794
+ 00a7c330 bytes d86e0794
- 00a7c148 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a7c148 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a7c148 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a7c148 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7c148 bytes 082400a9
- 00a7c154 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7c154 ["RETURN", null, ["register:0:8"]]
- 00a7c154 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-875892748f947b0ce37fd0b30f5caf0a"></a>

### [`00a7c174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c174.md) → [`00a7c36c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7c/00a7c36c.md) FUN_00a7c36c

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0068adf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068a/0068adf0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ac8a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8a60.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0068ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068ae30.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00ac8c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8c5c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.42% / 新版 73.42%

CFGの説明率　旧版 10.34% / 新版 11.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c178"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c178"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c17c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7c178",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7c17c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7c180",
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
      "00a7c370",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a7c374",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a7c378",
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

- 旧版 [`00a7c178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c174.md#insn-00a7c178) · [`00a7c17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c174.md#insn-00a7c17c) · [`00a7c180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c174.md#insn-00a7c180)

~~~diff
- 00a7c178 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a7c178 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a7c178 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a7c178 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7c178 bytes fd7b02a9
- 00a7c17c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00a7c17c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00a7c17c bytes f51b00f9
- 00a7c180 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a7c180 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a7c180 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a7c180 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7c180 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f87bf62d9e108c18e6f1c1455b4a30b7"></a>

### [`00a7c2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c2fc.md) → [`00a7c4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7c/00a7c4f4.md) FUN_00a7c4f4

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a73338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a73/00a73338.md) · 呼出先 23件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md)
- 新版 呼出元 1件 [`00a73530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a73/00a73530.md) · 呼出先 23件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 42.11% / 新版 42.11%

CFGの説明率　旧版 7.37% / 新版 7.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 27件, `call_target` 1件, `unresolved_branch_alignment` 68件, `unresolved_call_alignment` 96件, `unresolved_store_alignment` 152件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c30c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c30c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c310"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7c30c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7c310",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7c314",
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
      "00a7c504",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a7c508",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a7c50c",
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

- 旧版 [`00a7c30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c2fc.md#insn-00a7c30c) · [`00a7c310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c2fc.md#insn-00a7c310) · [`00a7c314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c2fc.md#insn-00a7c314)

~~~diff
- 00a7c30c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a7c30c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a7c30c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00a7c30c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7c30c bytes f85f15a9
- 00a7c310 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a7c310 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a7c310 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 00a7c310 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7c310 bytes f65716a9
- 00a7c314 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a7c314 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a7c314 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 00a7c314 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7c314 bytes f44f17a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60bf5eff407ae503ed2a9cb339df6952"></a>

### [`00a7d968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7d968.md) → [`00a7db60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7d/00a7db60.md) FUN_00a7db60

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0091fdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091f/0091fdc0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0091ff5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0091f/0091ff5c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "00a7db78",
      "incomplete_value": false,
      "site": "00a7db7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7d980",
      "incomplete_value": false,
      "site": "00a7d984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:900:8"
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
      "00a7db7c",
      "DATA",
      [
        "storage",
        "00c8b900",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a7db7c",
      "DATA",
      [
        "storage",
        "00c8bd00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7d980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7d968.md#insn-00a7d980) · [`00a7d994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7d968.md#insn-00a7d994) · [`00a7d9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7d968.md#insn-00a7d9a8)
- 新版 `00a7db78`（命令位置の公開資料なし） · `00a7db8c`（命令位置の公開資料なし） · `00a7dba0`（命令位置の公開資料なし）

~~~diff
- 00a7d980 ["COPY", "tmp:0:8", ["const:900:8"]]
- 00a7d980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7d980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7d980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7db78 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 00a7db78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7db78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7db78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7d980 bytes 08012491
+ 00a7db78 bytes 08013491
- 00a7d994 ["INT_ADD", "register:40f0:8", ["const:a7d994:8", "const:4:8"]]
- 00a7d994 ["CALL", null, ["callee:00c53d00:8"]]
+ 00a7db8c ["INT_ADD", "register:40f0:8", ["const:a7db8c:8", "const:4:8"]]
+ 00a7db8c ["CALL", null, ["callee:00c53d00:8"]]
- 00a7d994 bytes d3570794
+ 00a7db8c bytes 5d580794
- 00a7d9a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a7d9a8 ["INT_ADD", "register:40f0:8", ["const:a7d9a8:8", "const:4:8"]]
- 00a7d9a8 ["CALLIND", null, ["register:0:8"]]
+ 00a7dba0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a7dba0 ["INT_ADD", "register:40f0:8", ["const:a7dba0:8", "const:4:8"]]
+ 00a7dba0 ["CALLIND", null, ["register:0:8"]]
- 00a7d9a8 bytes 00013fd6
+ 00a7dba0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1f5f0b3de033090e5a146246f546636"></a>

### [`00a7d9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7d9f4.md) → [`00a7dbec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7d/00a7dbec.md) FUN_00a7dbec

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0091fdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091f/0091fdc0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0091ff5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0091f/0091ff5c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00a7dc04",
      "incomplete_value": false,
      "site": "00a7dc08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7da0c",
      "incomplete_value": false,
      "site": "00a7da10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:900:8"
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
      "00a7dc08",
      "DATA",
      [
        "storage",
        "00c8b900",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a7dc08",
      "DATA",
      [
        "storage",
        "00c8bd00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7da0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7d9f4.md#insn-00a7da0c) · [`00a7da20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7d9f4.md#insn-00a7da20) · [`00a7da34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7d9f4.md#insn-00a7da34)
- 新版 `00a7dc04`（命令位置の公開資料なし） · `00a7dc18`（命令位置の公開資料なし） · `00a7dc2c`（命令位置の公開資料なし）

~~~diff
- 00a7da0c ["COPY", "tmp:0:8", ["const:900:8"]]
- 00a7da0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7da0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7da0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7dc04 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 00a7dc04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7dc04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7dc04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7da0c bytes 08012491
+ 00a7dc04 bytes 08013491
- 00a7da20 ["INT_ADD", "register:40f0:8", ["const:a7da20:8", "const:4:8"]]
- 00a7da20 ["CALL", null, ["callee:00c53d00:8"]]
+ 00a7dc18 ["INT_ADD", "register:40f0:8", ["const:a7dc18:8", "const:4:8"]]
+ 00a7dc18 ["CALL", null, ["callee:00c53d00:8"]]
- 00a7da20 bytes b0570794
+ 00a7dc18 bytes 3a580794
- 00a7da34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a7da34 ["INT_ADD", "register:40f0:8", ["const:a7da34:8", "const:4:8"]]
- 00a7da34 ["CALLIND", null, ["register:0:8"]]
+ 00a7dc2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a7dc2c ["INT_ADD", "register:40f0:8", ["const:a7dc2c:8", "const:4:8"]]
+ 00a7dc2c ["CALLIND", null, ["register:0:8"]]
- 00a7da34 bytes 00013fd6
+ 00a7dc2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d6a8aa5875f3fe1c0ca674f85f90277"></a>

### [`00a7da8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7da8c.md) → [`00a7dc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7d/00a7dc84.md) FUN_00a7dc84

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7dca8",
      "incomplete_value": false,
      "site": "00a7dca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7dab0",
      "incomplete_value": false,
      "site": "00a7dab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "00a7dca8",
      "DATA",
      [
        "storage",
        "00c8b920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7dca8",
      "DATA",
      [
        "storage",
        "00c8bd20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7daa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7da8c.md#insn-00a7daa0) · [`00a7daac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7da8c.md#insn-00a7daac)
- 新版 `00a7dc98`（命令位置の公開資料なし） · `00a7dca4`（命令位置の公開資料なし）

~~~diff
- 00a7daa0 ["INT_ADD", "register:40f0:8", ["const:a7daa0:8", "const:4:8"]]
- 00a7daa0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a7dc98 ["INT_ADD", "register:40f0:8", ["const:a7dc98:8", "const:4:8"]]
+ 00a7dc98 ["CALL", null, ["callee:00c57e90:8"]]
- 00a7daa0 bytes fc670794
+ 00a7dc98 bytes 7e680794
- 00a7daac ["COPY", "tmp:0:8", ["const:920:8"]]
- 00a7daac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7daac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7daac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7dca4 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00a7dca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7dca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7dca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7daac bytes 08812491
+ 00a7dca4 bytes 08813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e54d39619610563b977a1cdd6cf6815f"></a>

### [`00a7dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dac0.md) → [`00a7dcb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7d/00a7dcb8.md) FUN_00a7dcb8

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7dcc4",
      "incomplete_value": false,
      "site": "00a7dcc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7dacc",
      "incomplete_value": false,
      "site": "00a7dacc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "00a7dcc4",
      "DATA",
      [
        "storage",
        "00c8b920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7dcc4",
      "DATA",
      [
        "storage",
        "00c8bd20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7dac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dac0.md#insn-00a7dac8)
- 新版 `00a7dcc0`（命令位置の公開資料なし）

~~~diff
- 00a7dac8 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00a7dac8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a7dac8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a7dac8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a7dcc0 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00a7dcc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7dcc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7dcc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a7dac8 bytes 29812491
+ 00a7dcc0 bytes 29813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3856b2fbc20a33b078fa81d19e84211a"></a>

### [`00a7dbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dbc8.md) → [`00a7ddc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7d/00a7ddc0.md) FUN_00a7ddc0

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7dde4",
      "incomplete_value": false,
      "site": "00a7dde4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7dbec",
      "incomplete_value": false,
      "site": "00a7dbec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "00a7dde4",
      "DATA",
      [
        "storage",
        "00c8b9a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7dde4",
      "DATA",
      [
        "storage",
        "00c8bda0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7dbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dbc8.md#insn-00a7dbdc) · [`00a7dbe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dbc8.md#insn-00a7dbe8)
- 新版 `00a7ddd4`（命令位置の公開資料なし） · `00a7dde0`（命令位置の公開資料なし）

~~~diff
- 00a7dbdc ["INT_ADD", "register:40f0:8", ["const:a7dbdc:8", "const:4:8"]]
- 00a7dbdc ["CALL", null, ["callee:00c57e90:8"]]
+ 00a7ddd4 ["INT_ADD", "register:40f0:8", ["const:a7ddd4:8", "const:4:8"]]
+ 00a7ddd4 ["CALL", null, ["callee:00c57e90:8"]]
- 00a7dbdc bytes ad670794
+ 00a7ddd4 bytes 2f680794
- 00a7dbe8 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00a7dbe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7dbe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7dbe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7dde0 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00a7dde0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7dde0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7dde0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7dbe8 bytes 08812691
+ 00a7dde0 bytes 08813691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-804abf97c9d48b21cdae408941e4244b"></a>

### [`00a7dbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dbfc.md) → [`00a7ddf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7d/00a7ddf4.md) FUN_00a7ddf4

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7de00",
      "incomplete_value": false,
      "site": "00a7de00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7dc08",
      "incomplete_value": false,
      "site": "00a7dc08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "00a7de00",
      "DATA",
      [
        "storage",
        "00c8b9a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7de00",
      "DATA",
      [
        "storage",
        "00c8bda0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7dc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dbfc.md#insn-00a7dc04)
- 新版 `00a7ddfc`（命令位置の公開資料なし）

~~~diff
- 00a7dc04 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00a7dc04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a7dc04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a7dc04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a7ddfc ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00a7ddfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7ddfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7ddfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a7dc04 bytes 29812691
+ 00a7ddfc bytes 29813691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6538ed0b95407843b33ef3c49e0449ca"></a>

### [`00a7dc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dc7c.md) → [`00a7de74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7d/00a7de74.md) FUN_00a7de74

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7de98",
      "incomplete_value": false,
      "site": "00a7de98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7dca0",
      "incomplete_value": false,
      "site": "00a7dca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
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
      "00a7de98",
      "DATA",
      [
        "storage",
        "00c8ba20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7de98",
      "DATA",
      [
        "storage",
        "00c8be20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7dc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dc7c.md#insn-00a7dc90) · [`00a7dc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dc7c.md#insn-00a7dc9c)
- 新版 `00a7de88`（命令位置の公開資料なし） · `00a7de94`（命令位置の公開資料なし）

~~~diff
- 00a7dc90 ["INT_ADD", "register:40f0:8", ["const:a7dc90:8", "const:4:8"]]
- 00a7dc90 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a7de88 ["INT_ADD", "register:40f0:8", ["const:a7de88:8", "const:4:8"]]
+ 00a7de88 ["CALL", null, ["callee:00c57e90:8"]]
- 00a7dc90 bytes 80670794
+ 00a7de88 bytes 02680794
- 00a7dc9c ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00a7dc9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7dc9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7dc9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7de94 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 00a7de94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7de94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7de94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7dc9c bytes 08812891
+ 00a7de94 bytes 08813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a8cb29543994a5ebd455137b949179e"></a>

### [`00a7dcb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dcb0.md) → [`00a7dea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7d/00a7dea8.md) FUN_00a7dea8

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7deb4",
      "incomplete_value": false,
      "site": "00a7deb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7dcbc",
      "incomplete_value": false,
      "site": "00a7dcbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
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
      "00a7deb4",
      "DATA",
      [
        "storage",
        "00c8ba20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7deb4",
      "DATA",
      [
        "storage",
        "00c8be20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7dcb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dcb0.md#insn-00a7dcb8)
- 新版 `00a7deb0`（命令位置の公開資料なし）

~~~diff
- 00a7dcb8 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00a7dcb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a7dcb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a7dcb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a7deb0 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 00a7deb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7deb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7deb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a7dcb8 bytes 29812891
+ 00a7deb0 bytes 29813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-394f3afb21306d0bbbfdff231d30874e"></a>

### [`00a7dccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dccc.md) → [`00a7dec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7d/00a7dec4.md) FUN_00a7dec4

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.81% / 新版 93.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a7dfb8",
      "incomplete_value": true,
      "site": "00a7dfcc",
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
      "definition_site": "00a7ddc0",
      "incomplete_value": true,
      "site": "00a7ddd4",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a7dfe4",
      "incomplete_value": false,
      "site": "00a7dfec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7ddec",
      "incomplete_value": false,
      "site": "00a7ddf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a7df10",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a7dd18",
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
      "00a7df10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a7df2c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a7df78",
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
      "00a7df10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a7df2c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a7df78",
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

- 旧版 [`00a7dd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dccc.md#insn-00a7dd18) · [`00a7dd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dccc.md#insn-00a7dd34) · [`00a7dd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dccc.md#insn-00a7dd64)
- 新版 `00a7df10`（命令位置の公開資料なし） · `00a7df2c`（命令位置の公開資料なし） · `00a7df5c`（命令位置の公開資料なし）

~~~diff
- 00a7dd18 ["INT_ADD", "register:40f0:8", ["const:a7dd18:8", "const:4:8"]]
- 00a7dd18 ["CALL", null, ["ram:47acb4:8"]]
+ 00a7df10 ["INT_ADD", "register:40f0:8", ["const:a7df10:8", "const:4:8"]]
+ 00a7df10 ["CALL", null, ["ram:47acf4:8"]]
- 00a7dd18 bytes e7f3e797
+ 00a7df10 bytes 79f3e797
- 00a7dd34 ["INT_ADD", "register:40f0:8", ["const:a7dd34:8", "const:4:8"]]
- 00a7dd34 ["CALL", null, ["ram:47acb4:8"]]
+ 00a7df2c ["INT_ADD", "register:40f0:8", ["const:a7df2c:8", "const:4:8"]]
+ 00a7df2c ["CALL", null, ["ram:47acf4:8"]]
- 00a7dd34 bytes e0f3e797
+ 00a7df2c bytes 72f3e797
- 00a7dd64 ["INT_ADD", "register:40f0:8", ["const:a7dd64:8", "const:4:8"]]
- 00a7dd64 ["CALL", null, ["callee:0048ce50:8"]]
+ 00a7df5c ["INT_ADD", "register:40f0:8", ["const:a7df5c:8", "const:4:8"]]
+ 00a7df5c ["CALL", null, ["callee:0048ce50:8"]]
- 00a7dd64 bytes 2b3ce897
+ 00a7df5c bytes bd3be897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5cd78f41d13d66a72e8422e4477c149"></a>

### [`00a7df4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7df4c.md) → [`00a7e144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e144.md) FUN_00a7e144

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7e158",
      "incomplete_value": false,
      "site": "00a7e15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7df60",
      "incomplete_value": false,
      "site": "00a7df64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
      "00a7e15c",
      "DATA",
      [
        "storage",
        "00c8ba90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7e15c",
      "DATA",
      [
        "storage",
        "00c8be90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7df58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7df4c.md#insn-00a7df58) · [`00a7df60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7df4c.md#insn-00a7df60)
- 新版 `00a7e150`（命令位置の公開資料なし） · `00a7e158`（命令位置の公開資料なし）

~~~diff
- 00a7df58 ["INT_ADD", "register:40f0:8", ["const:a7df58:8", "const:4:8"]]
- 00a7df58 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a7e150 ["INT_ADD", "register:40f0:8", ["const:a7e150:8", "const:4:8"]]
+ 00a7e150 ["CALL", null, ["callee:00c57e90:8"]]
- 00a7df58 bytes ce660794
+ 00a7e150 bytes 50670794
- 00a7df60 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00a7df60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7df60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7df60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7e158 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00a7e158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7e158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7e158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7df60 bytes 08412a91
+ 00a7e158 bytes 08413a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aab57cd4460709afc9bb38b46b16dc8"></a>

### [`00a7df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7df70.md) → [`00a7e168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e168.md) FUN_00a7e168

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7e16c",
      "incomplete_value": false,
      "site": "00a7e170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7df74",
      "incomplete_value": false,
      "site": "00a7df78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
      "00a7e170",
      "DATA",
      [
        "storage",
        "00c8ba90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7e170",
      "DATA",
      [
        "storage",
        "00c8be90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7df74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7df70.md#insn-00a7df74)
- 新版 `00a7e16c`（命令位置の公開資料なし）

~~~diff
- 00a7df74 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00a7df74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7df74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7df74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7e16c ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00a7e16c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7e16c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7e16c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7df74 bytes 08412a91
+ 00a7e16c bytes 08413a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2d33cab712b34d01db09d7acb9c6a37"></a>

### [`00a7dfcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dfcc.md) → [`00a7e1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e1c4.md) FUN_00a7e1c4

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7e1e8",
      "incomplete_value": false,
      "site": "00a7e1e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7dff0",
      "incomplete_value": false,
      "site": "00a7dff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "00a7e1e8",
      "DATA",
      [
        "storage",
        "00c8bb20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7e1e8",
      "DATA",
      [
        "storage",
        "00c8bf20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7dfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dfcc.md#insn-00a7dfe0) · [`00a7dfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dfcc.md#insn-00a7dfec)
- 新版 `00a7e1d8`（命令位置の公開資料なし） · `00a7e1e4`（命令位置の公開資料なし）

~~~diff
- 00a7dfe0 ["INT_ADD", "register:40f0:8", ["const:a7dfe0:8", "const:4:8"]]
- 00a7dfe0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a7e1d8 ["INT_ADD", "register:40f0:8", ["const:a7e1d8:8", "const:4:8"]]
+ 00a7e1d8 ["CALL", null, ["callee:00c57e90:8"]]
- 00a7dfe0 bytes ac660794
+ 00a7e1d8 bytes 2e670794
- 00a7dfec ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00a7dfec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7dfec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7dfec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7e1e4 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00a7e1e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7e1e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7e1e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7dfec bytes 08812c91
+ 00a7e1e4 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76b4575b1d32143e1ed0f668fd28c80c"></a>

### [`00a7e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e000.md) → [`00a7e1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e1f8.md) FUN_00a7e1f8

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7e204",
      "incomplete_value": false,
      "site": "00a7e204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7e00c",
      "incomplete_value": false,
      "site": "00a7e00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
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
      "00a7e204",
      "DATA",
      [
        "storage",
        "00c8bb20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7e204",
      "DATA",
      [
        "storage",
        "00c8bf20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7e008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e000.md#insn-00a7e008)
- 新版 `00a7e200`（命令位置の公開資料なし）

~~~diff
- 00a7e008 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00a7e008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a7e008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a7e008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a7e200 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00a7e200 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7e200 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7e200 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a7e008 bytes 29812c91
+ 00a7e200 bytes 29813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16f4f82ce9da7bf403c9d3ffa8f71078"></a>

### [`00a7e01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e01c.md) → [`00a7e214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e214.md) FUN_00a7e214

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.81% / 新版 93.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a7e308",
      "incomplete_value": true,
      "site": "00a7e31c",
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
      "definition_site": "00a7e110",
      "incomplete_value": true,
      "site": "00a7e124",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a7e334",
      "incomplete_value": false,
      "site": "00a7e33c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7e13c",
      "incomplete_value": false,
      "site": "00a7e144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a7e260",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a7e068",
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
      "00a7e260",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a7e27c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a7e2c8",
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
      "00a7e260",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a7e27c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a7e2c8",
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

- 旧版 [`00a7e068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e01c.md#insn-00a7e068) · [`00a7e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e01c.md#insn-00a7e084) · [`00a7e0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e01c.md#insn-00a7e0b4)
- 新版 `00a7e260`（命令位置の公開資料なし） · `00a7e27c`（命令位置の公開資料なし） · `00a7e2ac`（命令位置の公開資料なし）

~~~diff
- 00a7e068 ["INT_ADD", "register:40f0:8", ["const:a7e068:8", "const:4:8"]]
- 00a7e068 ["CALL", null, ["ram:47acb4:8"]]
+ 00a7e260 ["INT_ADD", "register:40f0:8", ["const:a7e260:8", "const:4:8"]]
+ 00a7e260 ["CALL", null, ["ram:47acf4:8"]]
- 00a7e068 bytes 13f3e797
+ 00a7e260 bytes a5f2e797
- 00a7e084 ["INT_ADD", "register:40f0:8", ["const:a7e084:8", "const:4:8"]]
- 00a7e084 ["CALL", null, ["ram:47acb4:8"]]
+ 00a7e27c ["INT_ADD", "register:40f0:8", ["const:a7e27c:8", "const:4:8"]]
+ 00a7e27c ["CALL", null, ["ram:47acf4:8"]]
- 00a7e084 bytes 0cf3e797
+ 00a7e27c bytes 9ef2e797
- 00a7e0b4 ["INT_ADD", "register:40f0:8", ["const:a7e0b4:8", "const:4:8"]]
- 00a7e0b4 ["CALL", null, ["callee:0048ce50:8"]]
+ 00a7e2ac ["INT_ADD", "register:40f0:8", ["const:a7e2ac:8", "const:4:8"]]
+ 00a7e2ac ["CALL", null, ["callee:0048ce50:8"]]
- 00a7e0b4 bytes 573be897
+ 00a7e2ac bytes e93ae897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a79fc331e65a774bab9296b7afcb272"></a>

### [`00a7e29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e29c.md) → [`00a7e494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e494.md) FUN_00a7e494

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7e4a8",
      "incomplete_value": false,
      "site": "00a7e4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7e2b0",
      "incomplete_value": false,
      "site": "00a7e2b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "00a7e4ac",
      "DATA",
      [
        "storage",
        "00c8bb90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7e4ac",
      "DATA",
      [
        "storage",
        "00c8bf90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7e2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e29c.md#insn-00a7e2a8) · [`00a7e2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e29c.md#insn-00a7e2b0)
- 新版 `00a7e4a0`（命令位置の公開資料なし） · `00a7e4a8`（命令位置の公開資料なし）

~~~diff
- 00a7e2a8 ["INT_ADD", "register:40f0:8", ["const:a7e2a8:8", "const:4:8"]]
- 00a7e2a8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a7e4a0 ["INT_ADD", "register:40f0:8", ["const:a7e4a0:8", "const:4:8"]]
+ 00a7e4a0 ["CALL", null, ["callee:00c57e90:8"]]
- 00a7e2a8 bytes fa650794
+ 00a7e4a0 bytes 7c660794
- 00a7e2b0 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00a7e2b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7e2b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7e2b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7e4a8 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 00a7e4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7e4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7e4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7e2b0 bytes 08412e91
+ 00a7e4a8 bytes 08413e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d49a0417fe936fe1c22a5f7de16b72d1"></a>

### [`00a7e2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e2c0.md) → [`00a7e4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e4b8.md) FUN_00a7e4b8

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7e4bc",
      "incomplete_value": false,
      "site": "00a7e4c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7e2c4",
      "incomplete_value": false,
      "site": "00a7e2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "00a7e4c0",
      "DATA",
      [
        "storage",
        "00c8bb90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7e4c0",
      "DATA",
      [
        "storage",
        "00c8bf90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7e2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e2c0.md#insn-00a7e2c4)
- 新版 `00a7e4bc`（命令位置の公開資料なし）

~~~diff
- 00a7e2c4 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00a7e2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7e2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7e2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7e4bc ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 00a7e4bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7e4bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7e4bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7e2c4 bytes 08412e91
+ 00a7e4bc bytes 08413e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-314baf62dac4782e0a9f7adc114c9f35"></a>

### [`00a7e31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e31c.md) → [`00a7e514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e514.md) FUN_00a7e514

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7e538",
      "incomplete_value": false,
      "site": "00a7e538",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7e340",
      "incomplete_value": false,
      "site": "00a7e340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
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
      "00a7e538",
      "DATA",
      [
        "storage",
        "00c8bc20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7e538",
      "DATA",
      [
        "storage",
        "00c8c020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7e330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e31c.md#insn-00a7e330) · [`00a7e338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e31c.md#insn-00a7e338) · [`00a7e33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e31c.md#insn-00a7e33c)
- 新版 `00a7e528`（命令位置の公開資料なし） · `00a7e530`（命令位置の公開資料なし） · `00a7e534`（命令位置の公開資料なし）

~~~diff
- 00a7e330 ["INT_ADD", "register:40f0:8", ["const:a7e330:8", "const:4:8"]]
- 00a7e330 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a7e528 ["INT_ADD", "register:40f0:8", ["const:a7e528:8", "const:4:8"]]
+ 00a7e528 ["CALL", null, ["callee:00c57e90:8"]]
- 00a7e330 bytes d8650794
+ 00a7e528 bytes 5a660794
- 00a7e338 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a7e530 ["COPY", "register:4040:8", ["const:c8c000:8"]]
- 00a7e338 bytes 681000b0
+ 00a7e530 bytes 681000d0
- 00a7e33c ["COPY", "tmp:0:8", ["const:c20:8"]]
- 00a7e33c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7e33c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7e33c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7e534 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 00a7e534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7e534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7e534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7e33c bytes 08813091
+ 00a7e534 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52f116956aca6afab471a88ca69ec601"></a>

### [`00a7e350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e350.md) → [`00a7e548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e548.md) FUN_00a7e548

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7e554",
      "incomplete_value": false,
      "site": "00a7e554",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7e35c",
      "incomplete_value": false,
      "site": "00a7e35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
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
      "00a7e554",
      "DATA",
      [
        "storage",
        "00c8bc20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7e554",
      "DATA",
      [
        "storage",
        "00c8c020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7e354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e350.md#insn-00a7e354) · [`00a7e358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e350.md#insn-00a7e358)
- 新版 `00a7e54c`（命令位置の公開資料なし） · `00a7e550`（命令位置の公開資料なし）

~~~diff
- 00a7e354 ["COPY", "register:4048:8", ["const:c8b000:8"]]
+ 00a7e54c ["COPY", "register:4048:8", ["const:c8c000:8"]]
- 00a7e354 bytes 691000b0
+ 00a7e54c bytes 691000d0
- 00a7e358 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 00a7e358 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a7e358 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a7e358 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a7e550 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 00a7e550 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7e550 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7e550 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a7e358 bytes 29813091
+ 00a7e550 bytes 29810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b958c936ad76674b94c467f6f70391d"></a>

### [`00a7e36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e36c.md) → [`00a7e564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e564.md) FUN_00a7e564

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a466e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466e0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a468d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468d8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

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
      "site": "00a7e598",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a7e3a0",
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
      "site": "00a7e5bc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a7e3c4",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00a7e598",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a7e5bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a7e598",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a7e5bc",
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

- 旧版 [`00a7e3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e36c.md#insn-00a7e3a0) · [`00a7e3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e36c.md#insn-00a7e3c4) · [`00a7e3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e36c.md#insn-00a7e3d0)
- 新版 `00a7e598`（命令位置の公開資料なし） · `00a7e5bc`（命令位置の公開資料なし） · `00a7e5c8`（命令位置の公開資料なし）

~~~diff
- 00a7e3a0 ["INT_ADD", "register:40f0:8", ["const:a7e3a0:8", "const:4:8"]]
- 00a7e3a0 ["CALL", null, ["ram:47acb4:8"]]
+ 00a7e598 ["INT_ADD", "register:40f0:8", ["const:a7e598:8", "const:4:8"]]
+ 00a7e598 ["CALL", null, ["ram:47acf4:8"]]
- 00a7e3a0 bytes 45f2e797
+ 00a7e598 bytes d7f1e797
- 00a7e3c4 ["INT_ADD", "register:40f0:8", ["const:a7e3c4:8", "const:4:8"]]
- 00a7e3c4 ["CALL", null, ["ram:47acb4:8"]]
+ 00a7e5bc ["INT_ADD", "register:40f0:8", ["const:a7e5bc:8", "const:4:8"]]
+ 00a7e5bc ["CALL", null, ["ram:47acf4:8"]]
- 00a7e3c4 bytes 3cf2e797
+ 00a7e5bc bytes cef1e797
- 00a7e3d0 ["INT_ADD", "register:40f0:8", ["const:a7e3d0:8", "const:4:8"]]
- 00a7e3d0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00a7e5c8 ["INT_ADD", "register:40f0:8", ["const:a7e5c8:8", "const:4:8"]]
+ 00a7e5c8 ["CALL", null, ["callee:0047cdd4:8"]]
- 00a7e3d0 bytes 71fae797
+ 00a7e5c8 bytes 03fae797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9fef3b14745f09f3b2f22decedb8481"></a>

### [`00a7e498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e498.md) → [`00a7e690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e690.md) FUN_00a7e690

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7e69c",
      "incomplete_value": false,
      "site": "00a7e69c",
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
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7e4a4",
      "incomplete_value": false,
      "site": "00a7e4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "00a7e69c",
      "DATA",
      [
        "storage",
        "00c8bca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7e69c",
      "DATA",
      [
        "storage",
        "00c8c0a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7e49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e498.md#insn-00a7e49c) · [`00a7e4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e498.md#insn-00a7e4a0)
- 新版 `00a7e694`（命令位置の公開資料なし） · `00a7e698`（命令位置の公開資料なし）

~~~diff
- 00a7e49c ["COPY", "register:4048:8", ["const:c8b000:8"]]
+ 00a7e694 ["COPY", "register:4048:8", ["const:c8c000:8"]]
- 00a7e49c bytes 691000b0
+ 00a7e694 bytes 691000d0
- 00a7e4a0 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00a7e4a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a7e4a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a7e4a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a7e698 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 00a7e698 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7e698 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7e698 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a7e4a0 bytes 29813291
+ 00a7e698 bytes 29810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a970c5535eb309334915e095ce58482b"></a>

### [`00a7e4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e4b4.md) → [`00a7e6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e6ac.md) FUN_00a7e6ac

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0068adf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068a/0068adf0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ac8a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8a60.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0068ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068ae30.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00ac8c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8c5c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.41% / 新版 92.41%

CFGの説明率　旧版 82.35% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7e4d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7e6c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a7e6ec",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a7e4f4",
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
      "unmatched:00a7e4d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a7e6ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a7e724",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a7e6c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a7e6ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a7e724",
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

- 旧版 [`00a7e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e4b4.md#insn-00a7e4d0) · [`00a7e4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e4b4.md#insn-00a7e4f4) · [`00a7e52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e4b4.md#insn-00a7e52c)
- 新版 `00a7e6ec`（命令位置の公開資料なし） · `00a7e724`（命令位置の公開資料なし）

~~~diff
- 00a7e4d0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a7e4d0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a7e4d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a7e4d0 bytes a8831ff8
- 00a7e4f4 ["INT_ADD", "register:40f0:8", ["const:a7e4f4:8", "const:4:8"]]
- 00a7e4f4 ["CALL", null, ["ram:47acb4:8"]]
+ 00a7e6ec ["INT_ADD", "register:40f0:8", ["const:a7e6ec:8", "const:4:8"]]
+ 00a7e6ec ["CALL", null, ["ram:47acf4:8"]]
- 00a7e4f4 bytes f0f1e797
+ 00a7e6ec bytes 82f1e797
- 00a7e52c ["INT_ADD", "register:40f0:8", ["const:a7e52c:8", "const:4:8"]]
- 00a7e52c ["CALL", null, ["ram:47acb4:8"]]
+ 00a7e724 ["INT_ADD", "register:40f0:8", ["const:a7e724:8", "const:4:8"]]
+ 00a7e724 ["CALL", null, ["ram:47acf4:8"]]
- 00a7e52c bytes e2f1e797
+ 00a7e724 bytes 74f1e797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af918769a7ac754727b788459bf82362"></a>

### [`00a7e7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e7e4.md) → [`00a7e9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e9dc.md) FUN_00a7e9dc

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) [`00a7e7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e7e4.md) · 呼出先 2件 [`00a7e7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e7e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) [`00a7e9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e9dc.md) · 呼出先 2件 [`00a7e9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e9dc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a7e800",
      "incomplete_value": true,
      "site": "00a7e804",
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
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a7e804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e7e4.md#insn-00a7e804) · [`00a7e7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e7e4.md#insn-00a7e7e4) · [`00a7e810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e7e4.md#insn-00a7e810)
- 新版 `00a7e9fc`（命令位置の公開資料なし） · `00a7e9dc`（命令位置の公開資料なし） · `00a7ea08`（命令位置の公開資料なし）

~~~diff
- 00a7e804 ["INT_ADD", "register:40f0:8", ["const:a7e804:8", "const:4:8"]]
- 00a7e804 ["CALL", null, ["local:b0:8"]]
+ 00a7e9fc ["INT_ADD", "register:40f0:8", ["const:a7e9fc:8", "const:4:8"]]
+ 00a7e9fc ["CALL", null, ["local:b0:8"]]
- 00a7e804 bytes f8ffff97
+ 00a7e9fc bytes f8ffff97
- 00a7e7e4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00a7e7e4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00a7e9dc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00a7e9dc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00a7e7e4 bytes 010200b4
+ 00a7e9dc bytes 010200b4
- 00a7e810 ["INT_ADD", "register:40f0:8", ["const:a7e810:8", "const:4:8"]]
- 00a7e810 ["CALL", null, ["local:b0:8"]]
+ 00a7ea08 ["INT_ADD", "register:40f0:8", ["const:a7ea08:8", "const:4:8"]]
+ 00a7ea08 ["CALL", null, ["local:b0:8"]]
- 00a7e810 bytes f5ffff97
+ 00a7ea08 bytes f5ffff97
~~~


<a id="compare-040ce8ba985973d18759e373ede24f7b"></a>

### [`00a7e82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e82c.md) → [`00a7ea24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7ea24.md) FUN_00a7ea24

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7ea38",
      "incomplete_value": false,
      "site": "00a7ea3c",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7e840",
      "incomplete_value": false,
      "site": "00a7e844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "00a7ea3c",
      "DATA",
      [
        "storage",
        "00c8bd20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7ea3c",
      "DATA",
      [
        "storage",
        "00c8c120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e82c.md#insn-00a7e838) · [`00a7e83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e82c.md#insn-00a7e83c) · [`00a7e840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e82c.md#insn-00a7e840)
- 新版 `00a7ea30`（命令位置の公開資料なし） · `00a7ea34`（命令位置の公開資料なし） · `00a7ea38`（命令位置の公開資料なし）

~~~diff
- 00a7e838 ["INT_ADD", "register:40f0:8", ["const:a7e838:8", "const:4:8"]]
- 00a7e838 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a7ea30 ["INT_ADD", "register:40f0:8", ["const:a7ea30:8", "const:4:8"]]
+ 00a7ea30 ["CALL", null, ["callee:00c57e90:8"]]
- 00a7e838 bytes 96640794
+ 00a7ea30 bytes 18650794
- 00a7e83c ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a7ea34 ["COPY", "register:4040:8", ["const:c8c000:8"]]
- 00a7e83c bytes 681000b0
+ 00a7ea34 bytes 681000d0
- 00a7e840 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00a7e840 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7e840 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7e840 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7ea38 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 00a7ea38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7ea38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7ea38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7e840 bytes 08813491
+ 00a7ea38 bytes 08810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6194b0d0bb665c4b46d53d12b108758"></a>

### [`00a7e8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e8ac.md) → [`00a7eaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7eaa4.md) FUN_00a7eaa4

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7e8c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7eabc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a7eaac",
      "incomplete_value": false,
      "site": "00a7eab0",
      "value": [
        "leaf",
        "const:10:8"
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
      "unmatched:00a7e8c4",
      "DATA",
      [
        "storage",
        "00c8bda0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a7e8c8",
      "DATA",
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
      "00a7eabc",
      "DATA",
      [
        "storage",
        "00c8c1a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a7eac0",
      "DATA",
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

- 旧版 [`00a7e8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e8ac.md#insn-00a7e8b8) · [`00a7e8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e8ac.md#insn-00a7e8c4) · [`00a7e8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e8ac.md#insn-00a7e8cc)
- 新版 `00a7eab0`（命令位置の公開資料なし）

~~~diff
- 00a7e8b8 ["INT_ADD", "register:40f0:8", ["const:a7e8b8:8", "const:4:8"]]
- 00a7e8b8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a7eab0 ["INT_ADD", "register:40f0:8", ["const:a7eab0:8", "const:4:8"]]
+ 00a7eab0 ["CALL", null, ["callee:00c57e90:8"]]
- 00a7e8b8 bytes 76640794
+ 00a7eab0 bytes f8640794
- 00a7e8c4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a7e8c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a7e8c4 bytes 080000f9
- 00a7e8cc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7e8cc ["RETURN", null, ["register:0:8"]]
- 00a7e8cc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-436457edcea79fea8647ee9a4c5abf92"></a>

### [`00a7e8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e8d0.md) → [`00a7eac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7eac8.md) FUN_00a7eac8

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7eacc",
      "incomplete_value": false,
      "site": "00a7ead0",
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
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7e8d4",
      "incomplete_value": false,
      "site": "00a7e8d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:da0:8"
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
      "00a7ead0",
      "DATA",
      [
        "storage",
        "00c8bda0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7ead0",
      "DATA",
      [
        "storage",
        "00c8c1a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7e8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e8d0.md#insn-00a7e8d0) · [`00a7e8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e8d0.md#insn-00a7e8d4)
- 新版 `00a7eac8`（命令位置の公開資料なし） · `00a7eacc`（命令位置の公開資料なし）

~~~diff
- 00a7e8d0 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a7eac8 ["COPY", "register:4040:8", ["const:c8c000:8"]]
- 00a7e8d0 bytes 681000b0
+ 00a7eac8 bytes 681000d0
- 00a7e8d4 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00a7e8d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7e8d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7e8d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7eacc ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 00a7eacc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7eacc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7eacc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7e8d4 bytes 08813691
+ 00a7eacc bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8cf50aa1c816061b998080f5cf0aa53"></a>

### [`00a7e928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e928.md) → [`00a7eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7eb20.md) FUN_00a7eb20

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00a7239c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a72/00a7239c.md) [`00a7e928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e928.md) [`00a7ec68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ec68.md) · 呼出先 4件 [`00811394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00811/00811394.md) [`00a7e928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e928.md) [`00a7ec68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ec68.md) [`00a7ef68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ef68.md)
- 新版 呼出元 3件 [`00a72594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a72/00a72594.md) [`00a7eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7eb20.md) [`00a7ee60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7ee60.md) · 呼出先 4件 [`008113d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00811/008113d4.md) [`00a7eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7eb20.md) [`00a7ee60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7ee60.md) [`00a7f160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7f/00a7f160.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.87% / 新版 90.87%

CFGの説明率　旧版 53.73% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7e928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7e928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7e92c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7e928",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7e92c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7e930",
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
      "00a7eb20",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a7eb24",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a7eb28",
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

- 旧版 [`00a7e928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e928.md#insn-00a7e928) · [`00a7e92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e928.md#insn-00a7e92c) · [`00a7e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e928.md#insn-00a7e930)

~~~diff
- 00a7e928 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a7e928 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a7e928 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00a7e928 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a7e928 bytes fd7bbba9
- 00a7e92c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a7e92c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00a7e92c bytes f90b00f9
- 00a7e930 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a7e930 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a7e930 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a7e930 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7e930 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9ba65dfb787301a80ce01dd27418eb7"></a>

### [`00a7ec68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ec68.md) → [`00a7ee60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7ee60.md) FUN_00a7ee60

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a7e928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e928.md) · 呼出先 2件 [`00811394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00811/00811394.md) [`00a7e928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e928.md)
- 新版 呼出元 1件 [`00a7eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7eb20.md) · 呼出先 2件 [`008113d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00811/008113d4.md) [`00a7eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7eb20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.54% / 新版 88.54%

CFGの説明率　旧版 40.85% / 新版 42.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7ec80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7ec80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7eeb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7ec80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7ed70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7ef1c"
      ]
    ],
    [
      "unmatched:00a7eeb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7f098"
      ]
    ]
  ],
  "added": [
    [
      "00a7ee78",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a7ef68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7ef1c"
      ]
    ],
    [
      "00a7f0b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7f098"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7ec80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ec68.md#insn-00a7ec80) · [`00a7ed1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ec68.md#insn-00a7ed1c) · [`00a7ed70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ec68.md#insn-00a7ed70)
- 新版 `00a7ef14`（命令位置の公開資料なし）

~~~diff
- 00a7ec80 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a7ec80 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a7ec80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00a7ec80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7ec80 bytes f44f05a9
- 00a7ed1c ["BRANCH", null, ["local:b15:8"]]
+ 00a7ef14 ["BRANCH", null, ["local:b14:8"]]
- 00a7ed1c bytes 07000014
+ 00a7ef14 bytes 07000014
- 00a7ed70 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00a7ed70 bytes a0fdff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95bce13481a85a8812239a0228069de3"></a>

### [`00a7ef68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ef68.md) → [`00a7f160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7f/00a7f160.md) FUN_00a7f160

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a7e928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e928.md) [`00a7ef68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ef68.md) · 呼出先 3件 [`00811394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00811/00811394.md) [`00a7ef68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ef68.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 2件 [`00a7eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7eb20.md) [`00a7f160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7f/00a7f160.md) · 呼出先 3件 [`008113d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00811/008113d4.md) [`00a7f160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7f/00a7f160.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.85% / 新版 91.85%

CFGの説明率　旧版 65.99% / 新版 65.99%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 4件, `unresolved_branch_alignment` 9件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7ef78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7ef78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7ef7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7ef78",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7ef7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7ef80",
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
      "00a7f170",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a7f174",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a7f178",
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

- 旧版 [`00a7ef78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ef68.md#insn-00a7ef78) · [`00a7ef7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ef68.md#insn-00a7ef7c) · [`00a7ef80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ef68.md#insn-00a7ef80)

~~~diff
- 00a7ef78 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a7ef78 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a7ef78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00a7ef78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7ef78 bytes f85f06a9
- 00a7ef7c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a7ef7c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a7ef7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00a7ef7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7ef7c bytes f65707a9
- 00a7ef80 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a7ef80 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a7ef80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00a7ef80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7ef80 bytes f44f08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06f4a4149cd3c103135e2977a45ee7b4"></a>

### [`00a7f5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f5c0.md) → [`00a7f7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7f/00a7f7b8.md) FUN_00a7f7b8

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7f7dc",
      "incomplete_value": false,
      "site": "00a7f7dc",
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
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7f5e4",
      "incomplete_value": false,
      "site": "00a7f5e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "00a7f7dc",
      "DATA",
      [
        "storage",
        "00c8be20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7f7dc",
      "DATA",
      [
        "storage",
        "00c8c220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7f5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f5c0.md#insn-00a7f5d4) · [`00a7f5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f5c0.md#insn-00a7f5dc) · [`00a7f5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f5c0.md#insn-00a7f5e0)
- 新版 `00a7f7cc`（命令位置の公開資料なし） · `00a7f7d4`（命令位置の公開資料なし） · `00a7f7d8`（命令位置の公開資料なし）

~~~diff
- 00a7f5d4 ["INT_ADD", "register:40f0:8", ["const:a7f5d4:8", "const:4:8"]]
- 00a7f5d4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a7f7cc ["INT_ADD", "register:40f0:8", ["const:a7f7cc:8", "const:4:8"]]
+ 00a7f7cc ["CALL", null, ["callee:00c57e90:8"]]
- 00a7f5d4 bytes 2f610794
+ 00a7f7cc bytes b1610794
- 00a7f5dc ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a7f7d4 ["COPY", "register:4040:8", ["const:c8c000:8"]]
- 00a7f5dc bytes 68100090
+ 00a7f7d4 bytes 681000b0
- 00a7f5e0 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 00a7f5e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a7f5e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a7f5e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a7f7d8 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 00a7f7d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7f7d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a7f7d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a7f5e0 bytes 08813891
+ 00a7f7d8 bytes 08810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfb4e3a0e64a145bf4b3f821d12cb306"></a>

### [`00a7f5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f5f4.md) → [`00a7f7ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7f/00a7f7ec.md) FUN_00a7f7ec

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a7f7f8",
      "incomplete_value": false,
      "site": "00a7f7f8",
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
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7f600",
      "incomplete_value": false,
      "site": "00a7f600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "00a7f7f8",
      "DATA",
      [
        "storage",
        "00c8be20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7f7f8",
      "DATA",
      [
        "storage",
        "00c8c220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7f5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f5f4.md#insn-00a7f5f8) · [`00a7f5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f5f4.md#insn-00a7f5fc)
- 新版 `00a7f7f0`（命令位置の公開資料なし） · `00a7f7f4`（命令位置の公開資料なし）

~~~diff
- 00a7f5f8 ["COPY", "register:4048:8", ["const:c8b000:8"]]
+ 00a7f7f0 ["COPY", "register:4048:8", ["const:c8c000:8"]]
- 00a7f5f8 bytes 69100090
+ 00a7f7f0 bytes 691000b0
- 00a7f5fc ["COPY", "tmp:0:8", ["const:e20:8"]]
- 00a7f5fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a7f5fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a7f5fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a7f7f4 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 00a7f7f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7f7f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7f7f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a7f5fc bytes 29813891
+ 00a7f7f4 bytes 29810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f53e6306431c12b9872cc411014c4f13"></a>

### [`00a7f63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f63c.md) → [`00a7f834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7f/00a7f834.md) FUN_00a7f834

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00a7239c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a72/00a7239c.md) [`00a7f63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f63c.md) [`00a7fa98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7fa98.md) · 呼出先 5件 [`00a7f63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f63c.md) [`00a7f9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f9b8.md) [`00a7fa98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7fa98.md) [`00a7fd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7fd88.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`00a72594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a72/00a72594.md) [`00a7f834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7f/00a7f834.md) [`00a7fc90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7f/00a7fc90.md) · 呼出先 5件 [`00a7f834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7f/00a7f834.md) [`00a7fbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7f/00a7fbb0.md) [`00a7fc90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7f/00a7fc90.md) [`00a7ff80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7f/00a7ff80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.13% / 新版 77.13%

CFGの説明率　旧版 32.47% / 新版 30.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `unresolved_branch_alignment` 9件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7f898"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7f904"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7f904"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7f68c",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7f690",
      "READ",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7f694",
      "DATA",
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
      "00a7f884",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a7f888",
      "READ",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a7f88c",
      "DATA",
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

- 旧版 [`00a7f6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f63c.md#insn-00a7f6ac) · [`00a7f71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f63c.md#insn-00a7f71c) · [`00a7f730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7f63c.md#insn-00a7f730)
- 新版 `00a7f8a4`（命令位置の公開資料なし） · `00a7f928`（命令位置の公開資料なし）

~~~diff
- 00a7f6ac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a7f6ac ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00a7f8a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a7f8a4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00a7f6ac bytes 81010054
+ 00a7f8a4 bytes 81010054
- 00a7f71c ["CBRANCH", null, ["local:b1:8", "register:101:1"]]
- 00a7f71c bytes a0faff54
- 00a7f730 ["INT_ADD", "register:40f0:8", ["const:a7f730:8", "const:4:8"]]
- 00a7f730 ["CALL", null, ["callee:00a7fbb0:8"]]
+ 00a7f928 ["INT_ADD", "register:40f0:8", ["const:a7f928:8", "const:4:8"]]
+ 00a7f928 ["CALL", null, ["callee:00a7fbb0:8"]]
- 00a7f730 bytes a2000094
+ 00a7f928 bytes a2000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

