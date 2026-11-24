# v16.0.0 → v16.0.1 · 最優先の変更候補 (70)

[一覧の目次](README.md)

<a id="compare-5e27d9effc6079fc7c67916f51fc1515"></a>

### [`00b42ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42ff0.md) → [`00b43418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43418.md) _ZN8firebase10FutureBaseaSERKS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) · 呼出先 6件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.20% / 新版 94.20%

CFGの説明率　旧版 37.50% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b4304c",
      "incomplete_value": true,
      "site": "00b43050",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b434b8",
      "incomplete_value": true,
      "site": "00b434bc",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": {
      "definition_site": "00b43090",
      "incomplete_value": true,
      "site": "00b43094",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b430c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b430c4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b434ec",
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

- 旧版 [`00b43050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42ff0.md#insn-00b43050) · [`00b43094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42ff0.md#insn-00b43094) · [`00b430c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42ff0.md#insn-00b430c4)
- 新版 [`00b43478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43418.md#insn-00b43478) · [`00b434bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43418.md#insn-00b434bc)

~~~diff
- 00b43050 ["INT_ADD", "register:40f0:8", ["const:b43050:8", "const:4:8"]]
- 00b43050 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00b43478 ["INT_ADD", "register:40f0:8", ["const:b43478:8", "const:4:8"]]
+ 00b43478 ["CALL", null, ["callee:00c5aa10:8"]]
- 00b43050 bytes 705d0494
+ 00b43478 bytes 665d0494
- 00b43094 ["INT_ADD", "register:40f0:8", ["const:b43094:8", "const:4:8"]]
- 00b43094 ["CALL", null, ["callee:00c5ae20:8"]]
+ 00b434bc ["INT_ADD", "register:40f0:8", ["const:b434bc:8", "const:4:8"]]
+ 00b434bc ["CALL", null, ["callee:00c5ae20:8"]]
- 00b43094 bytes 635e0494
+ 00b434bc bytes 595e0494
- 00b430c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b430c4 ["INT_ADD", "register:40f0:8", ["const:b430c4:8", "const:4:8"]]
- 00b430c4 ["CALLIND", null, ["register:0:8"]]
- 00b430c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6388266fad07533c0a2a5f8c080e4c6"></a>

### [`00b43164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43164.md) → [`00b4358c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b4358c.md) FUN_00b4358c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b42888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42888.md) · 呼出先 12件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00b42cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42cb0.md) · 呼出先 12件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.50% / 新版 84.50%

CFGの説明率　旧版 27.50% / 新版 24.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4317c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4317c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43238"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4317c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b43654",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b43244"
      ]
    ],
    [
      "unmatched:00b43238",
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
      "00b435a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b43654",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4366c"
      ]
    ],
    [
      "00b43660",
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

- 旧版 [`00b4317c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43164.md#insn-00b4317c) · [`00b431e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43164.md#insn-00b431e8) · [`00b431f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43164.md#insn-00b431f4)

~~~diff
- 00b4317c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4317c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4317c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b4317c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4317c bytes fd7b0aa9
- 00b431e8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b431e8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b431e8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b431e8 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b431e8 bytes 0801969a
- 00b431f4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b431f4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b431f4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b431f4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b431f4 bytes 3611889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd9bed406b00882744c9a98edd6ba79d"></a>

### [`00b43388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43388.md) → [`00b437b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b437b0.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS0_26Complet

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a960.md) · 呼出先 11件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5ad60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad60.md) · 呼出先 11件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43398"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43398"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b437c0"
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
      "unmatched:00b43398",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b433f4",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b437c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4381c",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43388.md#insn-00b43398) · [`00b433bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43388.md#insn-00b433bc) · [`00b433c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43388.md#insn-00b433c8)
- 新版 [`00b437e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b437b0.md#insn-00b437e4) · [`00b437f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b437b0.md#insn-00b437f0)

~~~diff
- 00b43398 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b43398 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b43398 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b43398 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b43398 bytes fd7b04a9
- 00b433bc ["INT_ADD", "register:40f0:8", ["const:b433bc:8", "const:4:8"]]
- 00b433bc ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b437e4 ["INT_ADD", "register:40f0:8", ["const:b437e4:8", "const:4:8"]]
+ 00b437e4 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b433bc bytes 915c0494
+ 00b437e4 bytes 875c0494
- 00b433c8 ["INT_ADD", "register:40f0:8", ["const:b433c8:8", "const:4:8"]]
- 00b433c8 ["CALL", null, ["callee:00c5ae80:8"]]
+ 00b437f0 ["INT_ADD", "register:40f0:8", ["const:b437f0:8", "const:4:8"]]
+ 00b437f0 ["CALL", null, ["callee:00c5ae80:8"]]
- 00b433c8 bytes ae5d0494
+ 00b437f0 bytes a45d0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d58c044760d441943e0743e05b1122d"></a>

### [`00b434c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b434c8.md) → [`00b438f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b438f0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5aca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aca0.md)
- 新版 呼出元 1件 [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5b0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 38.46% / 新版 37.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b434f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b4391c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b43530",
      "incomplete_value": true,
      "site": "00b4353c",
      "value": [
        "live",
        "register:40a8:8"
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
      "unmatched:00b434f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43944"
      ]
    ]
  ],
  "added": [
    [
      "00b4391c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43944"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b434f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b434c8.md#insn-00b434f4) · [`00b4353c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b434c8.md#insn-00b4353c) · [`00b43570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b434c8.md#insn-00b43570)
- 新版 [`00b43964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b438f0.md#insn-00b43964) · [`00b43998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b438f0.md#insn-00b43998)

~~~diff
- 00b434f4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b434f4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b434f4 bytes 43010054
- 00b4353c ["INT_ADD", "register:40f0:8", ["const:b4353c:8", "const:4:8"]]
- 00b4353c ["CALL", null, ["callee:00c57f40:8"]]
+ 00b43964 ["INT_ADD", "register:40f0:8", ["const:b43964:8", "const:4:8"]]
+ 00b43964 ["CALL", null, ["callee:00c57f40:8"]]
- 00b4353c bytes 81510494
+ 00b43964 bytes 77510494
- 00b43570 ["INT_ADD", "register:40f0:8", ["const:b43570:8", "const:4:8"]]
- 00b43570 ["CALL", null, ["callee:00c5b0a0:8"]]
+ 00b43998 ["INT_ADD", "register:40f0:8", ["const:b43998:8", "const:4:8"]]
+ 00b43998 ["CALL", null, ["callee:00c5b0a0:8"]]
- 00b43570 bytes cc5d0494
+ 00b43998 bytes c25d0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74bb00c83df97e57e966a99ce9fce8b0"></a>

### [`00b43590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43590.md) → [`00b439b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b439b8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aca0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ac90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac90.md)
- 新版 呼出元 1件 [`00c5b0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0a0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 19.35% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b436b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b43adc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43608"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b43610",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43a4c"
      ]
    ],
    [
      "unmatched:00b43668",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43aa8"
      ]
    ]
  ],
  "added": [
    [
      "00b43a38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43a4c"
      ]
    ],
    [
      "00b43a90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43aa8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43590.md#insn-00b43608) · [`00b43610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43590.md#insn-00b43610) · [`00b43648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43590.md#insn-00b43648)
- 新版 [`00b43a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b439b8.md#insn-00b43a70)

~~~diff
- 00b43608 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b43608 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b43608 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b43608 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b43608 bytes 2831889a
- 00b43610 ["CBRANCH", null, ["local:b10:8", "register:102:1"]]
- 00b43610 bytes a2000054
- 00b43648 ["INT_ADD", "register:40f0:8", ["const:b43648:8", "const:4:8"]]
- 00b43648 ["CALL", null, ["callee:00c58000:8"]]
+ 00b43a70 ["INT_ADD", "register:40f0:8", ["const:b43a70:8", "const:4:8"]]
+ 00b43a70 ["CALL", null, ["callee:00c58000:8"]]
- 00b43648 bytes 6e510494
+ 00b43a70 bytes 64510494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-242c6161e0a52b5df5be47600ca0adda"></a>

### [`00b436c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b436c8.md) → [`00b43af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43af0.md) FUN_00b43af0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b42c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42c50.md) · 呼出先 9件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5a8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8b0.md)
- 新版 呼出元 1件 [`00b43078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43078.md) · 呼出先 9件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5acb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5acb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.21% / 新版 87.21%

CFGの説明率　旧版 26.09% / 新版 26.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43700"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b43b28"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43730"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b43700",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43730",
      "PARAM",
      [
        "storage",
        "002a18e9",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b43750",
      "PARAM",
      [
        "storage",
        "002aa644",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b43b28",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b43b58",
      "PARAM",
      [
        "storage",
        "002a19b6",
        null,
        "string"
      ]
    ],
    [
      "00b43b78",
      "PARAM",
      [
        "storage",
        "002aa711",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b436c8.md#insn-00b43700) · [`00b43730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b436c8.md#insn-00b43730) · [`00b43748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b436c8.md#insn-00b43748)
- 新版 [`00b43b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43af0.md#insn-00b43b70)

~~~diff
- 00b43700 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b43700 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b43700 bytes e80f00f9
- 00b43730 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b43730 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b43730 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b43730 ["COPY", "register:4018:8", ["tmp:0:8"]]
- 00b43730 bytes 0301969a
- 00b43748 ["INT_ADD", "register:40f0:8", ["const:b43748:8", "const:4:8"]]
- 00b43748 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b43b70 ["INT_ADD", "register:40f0:8", ["const:b43b70:8", "const:4:8"]]
+ 00b43b70 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b43748 bytes 8a5c0494
+ 00b43b70 bytes 805c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-388419c9e6b659f95b687b97bd96955e"></a>

### [`00b43840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43840.md) → [`00b43c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43c68.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalImZNS0_26CompleteWithResultInternalImEEvRKNS_12FutureHandleEiPKcRKT_EUlPmE_EEvS5_i

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a990.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5ad90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad90.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 83.56% / 新版 83.56%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b438a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b43ccc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b43860",
      "incomplete_value": true,
      "site": "00b43874",
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
            "const:8:8"
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
      "00b43cac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b43930"
      ]
    ],
    [
      "unmatched:00b438a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43cdc"
      ]
    ],
    [
      "unmatched:00b438ac",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b43cac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43d58"
      ]
    ],
    [
      "00b43ccc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43cdc"
      ]
    ],
    [
      "00b43cd4",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43840.md#insn-00b43874) · [`00b4389c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43840.md#insn-00b4389c) · [`00b438a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43840.md#insn-00b438a4)
- 新版 [`00b43c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43c68.md#insn-00b43c9c)

~~~diff
- 00b43874 ["INT_ADD", "register:40f0:8", ["const:b43874:8", "const:4:8"]]
- 00b43874 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b43c9c ["INT_ADD", "register:40f0:8", ["const:b43c9c:8", "const:4:8"]]
+ 00b43c9c ["CALL", null, ["callee:00c5aa00:8"]]
- 00b43874 bytes 635b0494
+ 00b43c9c bytes 595b0494
- 00b4389c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4389c ["INT_ADD", "register:40f0:8", ["const:b4389c:8", "const:4:8"]]
- 00b4389c ["CALLIND", null, ["register:0:8"]]
- 00b4389c bytes 00013fd6
- 00b438a4 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b438a4 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bacfb0e468c994a3abdd476d190fc9c5"></a>

### [`00b43964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43964.md) → [`00b43d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43d8c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIiZNS0_26CompleteWithResultInternalIiEEvRKNS_12FutureHandleEiPKcRKT_EUlPiE_EEvS5_i

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a970.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5ad70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad70.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43964"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43968"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43968"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b43964",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43968",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4396c",
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
      "00b43d8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b43d90",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b43d94",
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

- 旧版 [`00b43964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43964.md#insn-00b43964) · [`00b43968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43964.md#insn-00b43968) · [`00b4396c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43964.md#insn-00b4396c)

~~~diff
- 00b43964 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b43964 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b43964 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b43964 bytes f90f1bf8
- 00b43968 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b43968 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b43968 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b43968 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b43968 bytes f85f01a9
- 00b4396c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4396c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4396c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b4396c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4396c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a77e6e878d0fbeeed3d6caf285185b5"></a>

### [`00b43a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43a88.md) → [`00b43eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43eb0.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9a0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ada0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43a88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43a88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43a8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b43a88",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43a8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43a90",
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
      "00b43eb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b43eb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b43eb8",
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

- 旧版 [`00b43a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43a88.md#insn-00b43a88) · [`00b43a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43a88.md#insn-00b43a8c) · [`00b43a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43a88.md#insn-00b43a90)

~~~diff
- 00b43a88 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b43a88 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b43a88 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b43a88 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b43a88 bytes f85fbca9
- 00b43a8c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b43a8c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b43a8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b43a8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b43a8c bytes f65701a9
- 00b43a90 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b43a90 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b43a90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b43a90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b43a90 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c52ef5bc75901bc0d998c7871a0ba19"></a>

### [`00b43b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43b90.md) → [`00b43fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43fb8.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00b42888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42888.md) [`00bbc3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc3b0.md) [`00bde3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde3f0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`00b42cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42cb0.md) [`00bbc7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc7d8.md) [`00bde818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde818.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b43b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43b90.md#insn-00b43b90) · [`00b43ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43b90.md#insn-00b43ba8) · [`00b43bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43b90.md#insn-00b43bb0)
- 新版 [`00b43fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43fb8.md#insn-00b43fb8) · [`00b43fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43fb8.md#insn-00b43fd0) · [`00b43fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43fb8.md#insn-00b43fd8)

~~~diff
- 00b43b90 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b43b90 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b43fb8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b43fb8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b43b90 bytes a00100b4
+ 00b43fb8 bytes a00100b4
- 00b43ba8 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b43ba8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b43ba8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b43ba8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00b43fd0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b43fd0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b43fd0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b43fd0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b43ba8 bytes 68000036
+ 00b43fd0 bytes 68000036
- 00b43bb0 ["INT_ADD", "register:40f0:8", ["const:b43bb0:8", "const:4:8"]]
- 00b43bb0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b43fd8 ["INT_ADD", "register:40f0:8", ["const:b43fd8:8", "const:4:8"]]
+ 00b43fd8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b43bb0 bytes c04f0494
+ 00b43fd8 bytes b64f0494
~~~


<a id="compare-5cc9eef60ee4f0c6f6605d9530eb6bc3"></a>

### [`00b43bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43bd4.md) → [`00b43ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43ffc.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIlZNS0_26CompleteWithResultInternalIlEEvRKNS_12FutureHandleEiPKcRKT_EUlPlE_EEvS5_i

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a980.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5ad80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad80.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 9.09% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43c38"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b44060"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43c30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b43c38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44070"
      ]
    ],
    [
      "unmatched:00b43c40",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b43c30",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b44060",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44070"
      ]
    ],
    [
      "00b44068",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ],
    [
      "00b44058",
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

- 旧版 [`00b43c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43bd4.md#insn-00b43c30) · [`00b43c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43bd4.md#insn-00b43c38) · [`00b43c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43bd4.md#insn-00b43c44)
- 新版 [`00b4406c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43ffc.md#insn-00b4406c)

~~~diff
- 00b43c30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b43c30 ["INT_ADD", "register:40f0:8", ["const:b43c30:8", "const:4:8"]]
- 00b43c30 ["CALLIND", null, ["register:0:8"]]
- 00b43c30 bytes 00013fd6
- 00b43c38 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00b43c38 bytes 80000054
- 00b43c44 ["INT_ADD", "register:40f0:8", ["const:b43c44:8", "const:4:8"]]
- 00b43c44 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4406c ["INT_ADD", "register:40f0:8", ["const:b4406c:8", "const:4:8"]]
+ 00b4406c ["CALL", null, ["callee:00c5b000:8"]]
- 00b43c44 bytes ef5b0494
+ 00b4406c bytes e55b0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38a20bb0bf39b9f9c3a82baba1367117"></a>

### [`00b43d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43d28.md) → [`00b44150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44150.md) _ZN8firebase23LogMessageWithCallbackVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md) · 呼出先 8件 [`00b43cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43cf8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b120.md) · 呼出先 8件 [`00b44120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44120.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 80.33% / 新版 80.33%

CFGの説明率　旧版 22.22% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4418c",
      "incomplete_value": true,
      "site": "00b4418c",
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
              "LOAD"
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
      "definition_site": "00b43d64",
      "incomplete_value": true,
      "site": "00b43d64",
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
              "LOAD"
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
      "definition_site": "00b441dc",
      "incomplete_value": false,
      "site": "00b441e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1125000:8"
          ],
          [
            "leaf",
            "const:421:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b43db4",
      "incomplete_value": false,
      "site": "00b43dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1125000:8"
          ],
          [
            "leaf",
            "const:21:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43de4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b44180",
      "READ",
      [
        "storage",
        "00c9b2d8",
        null,
        "pointer"
      ]
    ],
    [
      "00b44188",
      "READ",
      [
        "storage",
        "01125018",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b441a4",
      "WRITE",
      [
        "storage",
        "01125018",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b44180",
      "READ",
      [
        "storage",
        "00c9b6d8",
        null,
        "pointer"
      ]
    ],
    [
      "00b44188",
      "READ",
      [
        "storage",
        "01125418",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b441a4",
      "WRITE",
      [
        "storage",
        "01125418",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43d28.md#insn-00b43dc0) · [`00b43de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43d28.md#insn-00b43de4) · [`00b43e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43d28.md#insn-00b43e14)
- 新版 [`00b441e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44150.md#insn-00b441e8)

~~~diff
- 00b43dc0 ["INT_ADD", "register:40f0:8", ["const:b43dc0:8", "const:4:8"]]
- 00b43dc0 ["CALL", null, ["callee:00c5b150:8"]]
+ 00b441e8 ["INT_ADD", "register:40f0:8", ["const:b441e8:8", "const:4:8"]]
+ 00b441e8 ["CALL", null, ["callee:00c5b150:8"]]
- 00b43dc0 bytes e45b0494
+ 00b441e8 bytes da5b0494
- 00b43de4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b43de4 ["INT_ADD", "register:40f0:8", ["const:b43de4:8", "const:4:8"]]
- 00b43de4 ["CALLIND", null, ["register:0:8"]]
- 00b43de4 bytes 00013fd6
- 00b43e14 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b43e14 ["RETURN", null, ["register:0:8"]]
- 00b43e14 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1174326ceb8d1f8d8be6504f991fae56"></a>

### [`00b43e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43e5c.md) → [`00b44284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44284.md) _ZN8firebase8LogDebugEPKcz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md)
- 新版 呼出元 1件 [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b120.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 24.39% / 新版 24.39%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 26件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43e60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43e60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43e64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b43e60",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43e64",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43e6c",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b44288",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4428c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b44294",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43e5c.md#insn-00b43e60) · [`00b43e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43e5c.md#insn-00b43e64) · [`00b43e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43e5c.md#insn-00b43e6c)

~~~diff
- 00b43e60 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b43e60 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b43e60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00b43e60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b43e60 bytes fc4f11a9
- 00b43e64 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b43e64 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b43e64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00b43e64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b43e64 bytes fd7b12a9
- 00b43e6c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00b43e6c ["COPY", "tmp:1:8", ["register:4010:8"]]
- 00b43e6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:88:8"]]
- 00b43e6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b43e6c bytes e18b08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ced9e867b4e3227a525dcc815d60d874"></a>

### [`00b43fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43fa4.md) → [`00b443cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b443cc.md) _ZN8firebase10LogWarningEPKcz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md)
- 新版 呼出元 1件 [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b120.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 41.46% / 新版 41.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43fc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43fc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43fc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b43fc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x130]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43fc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43fcc",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b443ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x130]",
        null,
        null
      ]
    ],
    [
      "00b443f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ],
    [
      "00b443f4",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43fa4.md#insn-00b43fc4) · [`00b43fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43fa4.md#insn-00b43fc8) · [`00b43fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43fa4.md#insn-00b43fcc)

~~~diff
- 00b43fc4 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b43fc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b43fc4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b43fc4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b43fc4 bytes e00700ad
- 00b43fc8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b43fc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 00b43fc8 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b43fc8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5060:16"]]
- 00b43fc8 bytes e20f01ad
- 00b43fcc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b43fcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5080:16"]]
- 00b43fcc ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b43fcc ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:50a0:16"]]
- 00b43fcc bytes e41702ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e4a5c3cff9fbb45319009925eab8e81"></a>

### [`00b44048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44048.md) → [`00b44470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44470.md) _ZN8firebase8LogErrorEPKcz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md)
- 新版 呼出元 1件 [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b120.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.17% / 新版 73.17%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b440a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b440a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b440a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b440a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b440a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b440a8",
      "WRITE",
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
      "00b444c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b444cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b444d0",
      "WRITE",
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

- 旧版 [`00b440a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44048.md#insn-00b440a0) · [`00b440a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44048.md#insn-00b440a4) · [`00b440a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44048.md#insn-00b440a8)

~~~diff
- 00b440a0 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00b440a0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00b440a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b440a0 bytes ad831ef8
- 00b440a4 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b440a4 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b440a4 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00b440a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b440a4 bytes abab3ca9
- 00b440a8 ["COPY", "tmp:0:8", ["register:4070:8"]]
- 00b440a8 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00b440a8 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b440a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b440a8 bytes aeb33da9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cc67e5ab82154015d40c64009f56443"></a>

### [`00b440ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b440ec.md) → [`00b44514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44514.md) _ZN8firebase9LogAssertEPKcz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md)
- 新版 呼出元 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b120.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 24.39% / 新版 24.39%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 26件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b440f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b440f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b440f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b440f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b440f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b440fc",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b44518",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4451c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b44524",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b440f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b440ec.md#insn-00b440f0) · [`00b440f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b440ec.md#insn-00b440f4) · [`00b440fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b440ec.md#insn-00b440fc)

~~~diff
- 00b440f0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b440f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b440f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00b440f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b440f0 bytes fc4f11a9
- 00b440f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b440f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b440f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00b440f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b440f4 bytes fd7b12a9
- 00b440fc ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00b440fc ["COPY", "tmp:1:8", ["register:4010:8"]]
- 00b440fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:88:8"]]
- 00b440fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b440fc bytes e18b08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c72709263aaff331a26adc15d71ff7d"></a>

### [`00b44250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44250.md) → [`00b44678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44678.md) _ZN8firebase14LogGetCallbackEPPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b43cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43cf8.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b44120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44120.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `return_value_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b446a0",
      "incomplete_value": true,
      "site": "00b446a4",
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
      "definition_site": "00b44278",
      "incomplete_value": true,
      "site": "00b4427c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b44690",
      "incomplete_value": false,
      "site": "00b44694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:f7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44268",
      "incomplete_value": false,
      "site": "00b4426c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:f3a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b446b4",
      "incomplete_value": true,
      "site": "00b446bc",
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
      "definition_site": "00b4428c",
      "incomplete_value": true,
      "site": "00b44294",
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
      "00b44690",
      "PARAM",
      [
        "storage",
        "002abf3a",
        null,
        "string"
      ]
    ],
    [
      "00b4469c",
      "READ",
      [
        "storage",
        "00c9b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b446a0",
      "READ",
      [
        "storage",
        "01125010",
        "_ZN8firebase19g_log_callback_dataE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b44690",
      "PARAM",
      [
        "storage",
        "002abf7a",
        null,
        "string"
      ]
    ],
    [
      "00b4469c",
      "READ",
      [
        "storage",
        "00c9b6e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b446a0",
      "READ",
      [
        "storage",
        "01125410",
        "_ZN8firebase19g_log_callback_dataE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4426c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44250.md#insn-00b4426c) · [`00b44268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44250.md#insn-00b44268) · [`00b44274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44250.md#insn-00b44274)
- 新版 [`00b44694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44678.md#insn-00b44694) · [`00b44690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44678.md#insn-00b44690) · [`00b4469c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44678.md#insn-00b4469c)

~~~diff
- 00b4426c ["INT_ADD", "register:40f0:8", ["const:b4426c:8", "const:4:8"]]
- 00b4426c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b44694 ["INT_ADD", "register:40f0:8", ["const:b44694:8", "const:4:8"]]
+ 00b44694 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4426c bytes 655a0494
+ 00b44694 bytes 5b5a0494
- 00b44268 ["COPY", "tmp:0:8", ["const:f3a:8"]]
- 00b44268 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b44268 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b44268 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b44690 ["COPY", "tmp:0:8", ["const:f7a:8"]]
+ 00b44690 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b44690 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b44690 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b44268 bytes 00e83c91
+ 00b44690 bytes 00e83d91
- 00b44274 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e8:8"]]
- 00b44274 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4469c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6e8:8"]]
+ 00b4469c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b44274 bytes 087541f9
+ 00b4469c bytes 087543f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce68394892521dfd413cc90cd22752b7"></a>

### [`00b44298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44298.md) → [`00b446c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b446c0.md) FUN_00b446c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b43cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43cf8.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ace0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ace0.md)
- 新版 呼出元 1件 [`00b44120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44120.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 48.72% / 新版 48.72%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b442c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b442c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b442ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b442c0",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b442ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b442f0",
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
      "00b446e8",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "00b44714",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b44718",
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

- 旧版 [`00b442c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44298.md#insn-00b442c0) · [`00b442ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44298.md#insn-00b442ec) · [`00b442f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44298.md#insn-00b442f0)

~~~diff
- 00b442c0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b442c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:50c0:16"]]
- 00b442c0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b442c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:50e0:16"]]
- 00b442c0 bytes e61f03ad
- 00b442ec ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b442ec ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00b442ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b442ec bytes ac831ef8
- 00b442f0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b442f0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b442f0 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00b442f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b442f0 bytes aaa73ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adde05b253e806f0c49290449e8c423d"></a>

### [`00b44334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44334.md) → [`00b4475c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b4475c.md) _INIT_278

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_return_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b44774",
      "incomplete_value": true,
      "site": "00b44774",
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
              "LOAD"
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
      "definition_site": "00b4434c",
      "incomplete_value": true,
      "site": "00b4434c",
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
              "LOAD"
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
      "definition_site": "00b44780",
      "incomplete_value": false,
      "site": "00b44788",
      "value": [
        "leaf",
        "const:1:8"
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
      "site": "00b44370"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4476c",
      "READ",
      [
        "storage",
        "00c9b2d8",
        null,
        "pointer"
      ]
    ],
    [
      "00b44770",
      "READ",
      [
        "storage",
        "01125018",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b4478c",
      "WRITE",
      [
        "storage",
        "01125018",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4476c",
      "READ",
      [
        "storage",
        "00c9b6d8",
        null,
        "pointer"
      ]
    ],
    [
      "00b44770",
      "READ",
      [
        "storage",
        "01125418",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b4478c",
      "WRITE",
      [
        "storage",
        "01125418",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4434c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44334.md#insn-00b4434c) · [`00b44360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44334.md#insn-00b44360) · [`00b44370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44334.md#insn-00b44370)
- 新版 [`00b44774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b4475c.md#insn-00b44774) · [`00b44788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b4475c.md#insn-00b44788)

~~~diff
- 00b4434c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4434c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b44774 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b44774 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4434c bytes e80000b5
+ 00b44774 bytes e80000b5
- 00b44360 ["INT_ADD", "register:40f0:8", ["const:b44360:8", "const:4:8"]]
- 00b44360 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00b44788 ["INT_ADD", "register:40f0:8", ["const:b44788:8", "const:4:8"]]
+ 00b44788 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b44360 bytes 48590494
+ 00b44788 bytes 3e590494
- 00b44370 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b44370 ["RETURN", null, ["register:0:8"]]
- 00b44370 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20ae809684ce76a5bc5af2c3f0810699"></a>

### [`00b444d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b444d0.md) → [`00b448f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b448f8.md) _ZN8firebase4util12class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b444fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44924"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4490c",
      "incomplete_value": true,
      "site": "00b4490c",
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
      "definition_site": "00b444e4",
      "incomplete_value": true,
      "site": "00b444e4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b44908",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b444f0",
      "PARAM",
      [
        "storage",
        "002b89e6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b444f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b44908",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44918",
      "PARAM",
      [
        "storage",
        "002b8a26",
        null,
        "string"
      ]
    ],
    [
      "00b4491c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b444e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b444d0.md#insn-00b444e4) · [`00b444f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b444d0.md#insn-00b444f4) · [`00b444fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b444d0.md#insn-00b444fc)
- 新版 [`00b4490c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b448f8.md#insn-00b4490c)

~~~diff
- 00b444e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b444e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b4490c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4490c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b444e4 bytes e80000b5
+ 00b4490c bytes e80000b5
- 00b444f4 ["INT_ADD", "register:40f0:8", ["const:b444f4:8", "const:4:8"]]
- 00b444f4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b444f4 bytes 87590494
- 00b444fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:228:8"]]
- 00b444fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b444fc bytes 601601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35083837f696dbaaafde3951208be43d"></a>

### [`00b44510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44510.md) → [`00b44938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44938.md) _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassReq

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) · 呼出先 4件 [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md) [`00c5af30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af30.md) [`00c5b170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b170.md)
- 新版 呼出元 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) · 呼出先 4件 [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md) [`00c5b330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b330.md) [`00c5b570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b570.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.42% / 新版 93.42%

CFGの説明率　旧版 25.00% / 新版 26.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b44534",
      "incomplete_value": true,
      "site": "00b44544",
      "value": [
        "live",
        "register:4018:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b449a4",
      "incomplete_value": false,
      "site": "00b449b0",
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
            "const:595:8"
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
      "definition_site": "00b449e8",
      "incomplete_value": false,
      "site": "00b449f4",
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
            "const:535:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b445c0",
      "incomplete_value": false,
      "site": "00b445cc",
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
            "const:468:8"
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
      "unmatched:00b44530",
      "PARAM",
      [
        "storage",
        "002b6bd4",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4457c",
      "PARAM",
      [
        "storage",
        "002b2555",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b445c0",
      "PARAM",
      [
        "storage",
        "002a9468",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b44958",
      "PARAM",
      [
        "storage",
        "002b6c14",
        null,
        "string"
      ]
    ],
    [
      "00b449a4",
      "PARAM",
      [
        "storage",
        "002b2595",
        null,
        "string"
      ]
    ],
    [
      "00b449e8",
      "PARAM",
      [
        "storage",
        "002a9535",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44510.md#insn-00b44544) · [`00b44588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44510.md#insn-00b44588) · [`00b445cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44510.md#insn-00b445cc)
- 新版 [`00b4496c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44938.md#insn-00b4496c) · [`00b449b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44938.md#insn-00b449b0) · [`00b449f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44938.md#insn-00b449f4)

~~~diff
- 00b44544 ["INT_ADD", "register:40f0:8", ["const:b44544:8", "const:4:8"]]
- 00b44544 ["CALL", null, ["callee:00c5b130:8"]]
+ 00b4496c ["INT_ADD", "register:40f0:8", ["const:b4496c:8", "const:4:8"]]
+ 00b4496c ["CALL", null, ["callee:00c5b130:8"]]
- 00b44544 bytes fb590494
+ 00b4496c bytes f1590494
- 00b44588 ["INT_ADD", "register:40f0:8", ["const:b44588:8", "const:4:8"]]
- 00b44588 ["CALL", null, ["callee:00c5b130:8"]]
+ 00b449b0 ["INT_ADD", "register:40f0:8", ["const:b449b0:8", "const:4:8"]]
+ 00b449b0 ["CALL", null, ["callee:00c5b130:8"]]
- 00b44588 bytes ea590494
+ 00b449b0 bytes e0590494
- 00b445cc ["INT_ADD", "register:40f0:8", ["const:b445cc:8", "const:4:8"]]
- 00b445cc ["CALL", null, ["callee:00c5b130:8"]]
+ 00b449f4 ["INT_ADD", "register:40f0:8", ["const:b449f4:8", "const:4:8"]]
+ 00b449f4 ["CALL", null, ["callee:00c5b130:8"]]
- 00b445cc bytes d9590494
+ 00b449f4 bytes cf590494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b39b9ec9eb4da73f3bbb343ee2c0206e"></a>

### [`00b44640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44640.md) → [`00b44a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44a68.md) _ZN8firebase4util12class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b44a94",
      "incomplete_value": true,
      "site": "00b44a94",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4466c",
      "incomplete_value": true,
      "site": "00b4466c",
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
            "const:228:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b44a7c",
      "incomplete_value": true,
      "site": "00b44a7c",
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
      "definition_site": "00b44654",
      "incomplete_value": true,
      "site": "00b44654",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b44a84",
      "incomplete_value": false,
      "site": "00b44a8c",
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
            "const:a26:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4465c",
      "incomplete_value": false,
      "site": "00b44664",
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
            "const:9e6:8"
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
      "00b44a78",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44a84",
      "PARAM",
      [
        "storage",
        "002b89e6",
        null,
        "string"
      ]
    ],
    [
      "00b44a94",
      "WRITE",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b44a78",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44a84",
      "PARAM",
      [
        "storage",
        "002b8a26",
        null,
        "string"
      ]
    ],
    [
      "00b44a94",
      "WRITE",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44640.md#insn-00b44664) · [`00b4466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44640.md#insn-00b4466c) · [`00b44650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44640.md#insn-00b44650)
- 新版 [`00b44a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44a68.md#insn-00b44a8c) · [`00b44a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44a68.md#insn-00b44a94) · [`00b44a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44a68.md#insn-00b44a78)

~~~diff
- 00b44664 ["INT_ADD", "register:40f0:8", ["const:b44664:8", "const:4:8"]]
- 00b44664 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b44a8c ["INT_ADD", "register:40f0:8", ["const:b44a8c:8", "const:4:8"]]
+ 00b44a8c ["CALL", null, ["callee:00c5af10:8"]]
- 00b44664 bytes 2b590494
+ 00b44a8c bytes 21590494
- 00b4466c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:228:8"]]
- 00b4466c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b44a94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
+ 00b44a94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4466c bytes 601601f9
+ 00b44a94 bytes 601603f9
- 00b44650 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:228:8"]]
- 00b44650 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b44a78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
+ 00b44a78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b44650 bytes 681641f9
+ 00b44a78 bytes 681643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e7332950a48d639a8b866bbd79960ed"></a>

### [`00b44680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44680.md) → [`00b44aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44aa8.md) _ZN8firebase4util12class_loader10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b446b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44ad8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b44abc",
      "incomplete_value": true,
      "site": "00b44abc",
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
      "definition_site": "00b44694",
      "incomplete_value": true,
      "site": "00b44694",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b44ab8",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44abc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b446b4"
      ]
    ],
    [
      "unmatched:00b446a0",
      "PARAM",
      [
        "storage",
        "002b89e6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b44ab8",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44abc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44adc"
      ]
    ],
    [
      "00b44ac8",
      "PARAM",
      [
        "storage",
        "002b8a26",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b446a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44680.md#insn-00b446a8) · [`00b446b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44680.md#insn-00b446b0) · [`00b446c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44680.md#insn-00b446c0)

~~~diff
- 00b446a8 ["INT_ADD", "register:40f0:8", ["const:b446a8:8", "const:4:8"]]
- 00b446a8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b446a8 bytes 1a590494
- 00b446b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:228:8"]]
- 00b446b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b446b0 bytes 601601f9
- 00b446c0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b446c0 ["RETURN", null, ["register:0:8"]]
- 00b446c0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2c2c6cd3b45b3b81dde676a9d1a1644"></a>

### [`00b446c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b446c4.md) → [`00b44aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44aec.md) _ZN8firebase4util12class_loader10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b446f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44b1c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b44b00",
      "incomplete_value": true,
      "site": "00b44b00",
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
      "definition_site": "00b446d8",
      "incomplete_value": true,
      "site": "00b446d8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b44afc",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44b00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b446f8"
      ]
    ],
    [
      "unmatched:00b446e0",
      "PARAM",
      [
        "storage",
        "002b89e6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b44afc",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44b00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44b20"
      ]
    ],
    [
      "00b44b08",
      "PARAM",
      [
        "storage",
        "002b8a26",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b446d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b446c4.md#insn-00b446d8) · [`00b446ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b446c4.md#insn-00b446ec) · [`00b446f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b446c4.md#insn-00b446f4)
- 新版 [`00b44b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44aec.md#insn-00b44b00) · [`00b44b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44aec.md#insn-00b44b14)

~~~diff
- 00b446d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b446d8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b44b00 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b44b00 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b446d8 bytes 080100b5
+ 00b44b00 bytes 080100b5
- 00b446ec ["INT_ADD", "register:40f0:8", ["const:b446ec:8", "const:4:8"]]
- 00b446ec ["CALL", null, ["callee:00c5af10:8"]]
+ 00b44b14 ["INT_ADD", "register:40f0:8", ["const:b44b14:8", "const:4:8"]]
+ 00b44b14 ["CALL", null, ["callee:00c5af10:8"]]
- 00b446ec bytes 09590494
+ 00b44b14 bytes ff580494
- 00b446f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:228:8"]]
- 00b446f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b446f4 bytes 601601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c11ae4a326570e35ffb9949f79167e7a"></a>

### [`00b44714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44714.md) → [`00b44b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44b3c.md) _ZN8firebase4util12class_loader15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.36% / 新版 74.36%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4479c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44bc4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b44b70",
      "incomplete_value": true,
      "site": "00b44b7c",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:628:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44748",
      "incomplete_value": true,
      "site": "00b44754",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:228:8"
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
      "00b44b50",
      "READ",
      [
        "storage",
        "01125230",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b44748",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44b98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b44794"
      ]
    ]
  ],
  "added": [
    [
      "00b44b50",
      "READ",
      [
        "storage",
        "01125630",
        null,
        "undefined1"
      ]
    ],
    [
      "00b44b70",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44b98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44bbc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44714.md#insn-00b44754) · [`00b44780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44714.md#insn-00b44780) · [`00b44790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44714.md#insn-00b44790)
- 新版 [`00b44b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44b3c.md#insn-00b44b7c)

~~~diff
- 00b44754 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44754 ["INT_ADD", "register:40f0:8", ["const:b44754:8", "const:4:8"]]
- 00b44754 ["CALLIND", null, ["register:0:8"]]
+ 00b44b7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b44b7c ["INT_ADD", "register:40f0:8", ["const:b44b7c:8", "const:4:8"]]
+ 00b44b7c ["CALLIND", null, ["register:0:8"]]
- 00b44754 bytes 00013fd6
+ 00b44b7c bytes 00013fd6
- 00b44780 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44780 ["INT_ADD", "register:40f0:8", ["const:b44780:8", "const:4:8"]]
- 00b44780 ["CALLIND", null, ["register:0:8"]]
- 00b44780 bytes 00013fd6
- 00b44790 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44790 ["INT_ADD", "register:40f0:8", ["const:b44790:8", "const:4:8"]]
- 00b44790 ["CALLIND", null, ["register:0:8"]]
- 00b44790 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf50f0ef75254f5f09c37740eec48d88"></a>

### [`00b4480c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b4480c.md) → [`00b44c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44c34.md) _ZN8firebase4util12class_loader12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 45.45% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44848"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b44cc0",
      "incomplete_value": true,
      "site": "00b44cc0",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44898",
      "incomplete_value": true,
      "site": "00b44898",
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
            "const:228:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44c70"
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
      "00b44c48",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44c54",
      "READ",
      [
        "storage",
        "01125230",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b44848",
      "WRITE",
      [
        "storage",
        "01125230",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b44c48",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44c54",
      "READ",
      [
        "storage",
        "01125630",
        null,
        "undefined1"
      ]
    ],
    [
      "00b44c70",
      "WRITE",
      [
        "storage",
        "01125630",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b4480c.md#insn-00b44844) · [`00b44848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b4480c.md#insn-00b44848) · [`00b44880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b4480c.md#insn-00b44880)

~~~diff
- 00b44844 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44844 ["INT_ADD", "register:40f0:8", ["const:b44844:8", "const:4:8"]]
- 00b44844 ["CALLIND", null, ["register:0:8"]]
- 00b44844 bytes 00013fd6
- 00b44848 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b44848 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b44848 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:230:8"]]
- 00b44848 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b44848 bytes bfc20839
- 00b44880 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44880 ["INT_ADD", "register:40f0:8", ["const:b44880:8", "const:4:8"]]
- 00b44880 ["CALLIND", null, ["register:0:8"]]
- 00b44880 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db1003f307faae99a68e6b48923244f0"></a>

### [`00b448ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b448ac.md) → [`00b44cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44cd4.md) _ZN8firebase4util12class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b448ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44d14"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b448c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b448c0",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b448c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44d18"
      ]
    ],
    [
      "unmatched:00b448d0",
      "PARAM",
      [
        "storage",
        "002b89e6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b44ce8",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44cf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44d18"
      ]
    ],
    [
      "00b44cf8",
      "PARAM",
      [
        "storage",
        "002b8a26",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b448c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b448ac.md#insn-00b448c8) · [`00b448e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b448ac.md#insn-00b448e4) · [`00b448ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b448ac.md#insn-00b448ec)
- 新版 [`00b44d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44cd4.md#insn-00b44d0c)

~~~diff
- 00b448c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b448c8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b448c8 bytes 410100b5
- 00b448e4 ["INT_ADD", "register:40f0:8", ["const:b448e4:8", "const:4:8"]]
- 00b448e4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b44d0c ["INT_ADD", "register:40f0:8", ["const:b44d0c:8", "const:4:8"]]
+ 00b44d0c ["CALL", null, ["callee:00c5af10:8"]]
- 00b448e4 bytes 8b580494
+ 00b44d0c bytes 81580494
- 00b448ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:228:8"]]
- 00b448ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b448ec bytes 801601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db62d860fe48e21a4833e296ee7aeada"></a>

### [`00b4491c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b4491c.md) → [`00b44d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44d44.md) _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md) · 呼出先 5件 [`00b51378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51378.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md)
- 新版 呼出元 1件 [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md) · 呼出先 5件 [`00b517a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b517a0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.84% / 新版 74.84%

CFGの説明率　旧版 26.92% / 新版 25.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4492c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4492c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44930"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4492c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b44930",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b44934",
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
      "00b44d54",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b44d58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b44d5c",
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

- 旧版 [`00b4492c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b4491c.md#insn-00b4492c) · [`00b44930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b4491c.md#insn-00b44930) · [`00b44934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b4491c.md#insn-00b44934)

~~~diff
- 00b4492c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4492c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4492c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00b4492c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4492c bytes f65715a9
- 00b44930 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b44930 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b44930 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 00b44930 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b44930 bytes f44f16a9
- 00b44934 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b44934 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b44934 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 00b44934 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b44934 bytes fd7b17a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-923d5fd9289aa80102f18af342cd3806"></a>

### [`00b44b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44b88.md) → [`00b44fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44fb0.md) _ZN8firebase4util12class_loader11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b44fcc",
      "incomplete_value": false,
      "site": "00b44fd0",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44ba4",
      "incomplete_value": false,
      "site": "00b44ba8",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b44fdc",
      "incomplete_value": true,
      "site": "00b44fe8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44bb4",
      "incomplete_value": true,
      "site": "00b44bc0",
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
              "INT_LEFT"
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
      "00b44fcc",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b44fdc",
      "DATA",
      [
        "storage",
        "01125238",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b44fcc",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b44fdc",
      "DATA",
      [
        "storage",
        "01125638",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44b88.md#insn-00b44ba8) · [`00b44ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44b88.md#insn-00b44ba4) · [`00b44bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44b88.md#insn-00b44bb0)
- 新版 [`00b44fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44fb0.md#insn-00b44fd0) · [`00b44fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44fb0.md#insn-00b44fcc) · [`00b44fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44fb0.md#insn-00b44fd8)

~~~diff
- 00b44ba8 ["INT_ADD", "register:40f0:8", ["const:b44ba8:8", "const:4:8"]]
- 00b44ba8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b44fd0 ["INT_ADD", "register:40f0:8", ["const:b44fd0:8", "const:4:8"]]
+ 00b44fd0 ["CALL", null, ["callee:00c5b000:8"]]
- 00b44ba8 bytes 16580494
+ 00b44fd0 bytes 0c580494
- 00b44ba4 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b44ba4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b44ba4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b44ba4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b44fcc ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b44fcc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b44fcc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b44fcc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b44ba4 bytes 00680a91
+ 00b44fcc bytes 009c0d91
- 00b44bb0 ["COPY", "tmp:0:8", ["const:238:8"]]
- 00b44bb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b44bb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b44bb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b44fd8 ["COPY", "tmp:0:8", ["const:638:8"]]
+ 00b44fd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b44fd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b44fd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b44bb0 bytes 08e10891
+ 00b44fd8 bytes 08e11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d228fa7c8c6827ee82b075ac9972ec26"></a>

### [`00b44bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44bc4.md) → [`00b44fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44fec.md) _ZN8firebase4util12class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44c04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4502c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44be0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b44bd8",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b44be0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45030"
      ]
    ],
    [
      "unmatched:00b44be8",
      "PARAM",
      [
        "storage",
        "002b89e6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45000",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45008",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45030"
      ]
    ],
    [
      "00b45010",
      "PARAM",
      [
        "storage",
        "002b8a26",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44bc4.md#insn-00b44be0) · [`00b44bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44bc4.md#insn-00b44bfc) · [`00b44c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44bc4.md#insn-00b44c04)
- 新版 [`00b45024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44fec.md#insn-00b45024)

~~~diff
- 00b44be0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b44be0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b44be0 bytes 410100b5
- 00b44bfc ["INT_ADD", "register:40f0:8", ["const:b44bfc:8", "const:4:8"]]
- 00b44bfc ["CALL", null, ["callee:00c5af10:8"]]
+ 00b45024 ["INT_ADD", "register:40f0:8", ["const:b45024:8", "const:4:8"]]
+ 00b45024 ["CALL", null, ["callee:00c5af10:8"]]
- 00b44bfc bytes c5570494
+ 00b45024 bytes bb570494
- 00b44c04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:228:8"]]
- 00b44c04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44c04 bytes 801601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3effc603063bce2e1b8fa679488e4ffe"></a>

### [`00b44c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44c34.md) → [`00b4505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b4505c.md) _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) · 呼出先 5件 [`00b51378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51378.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md)
- 新版 呼出元 1件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) · 呼出先 5件 [`00b517a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b517a0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.71% / 新版 78.71%

CFGの説明率　旧版 38.18% / 新版 38.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44c4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44c4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44c74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b44c4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b44c74",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b450ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b44e24"
      ]
    ]
  ],
  "added": [
    [
      "00b45074",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4509c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b450ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4524c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44c34.md#insn-00b44c4c) · [`00b44c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44c34.md#insn-00b44c74) · [`00b44c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44c34.md#insn-00b44c94)
- 新版 [`00b450bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b4505c.md#insn-00b450bc)

~~~diff
- 00b44c4c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b44c4c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b44c4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 00b44c4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b44c4c bytes fd7b17a9
- 00b44c74 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b44c74 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b44c74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b44c74 bytes a8031af8
- 00b44c94 ["INT_ADD", "register:40f0:8", ["const:b44c94:8", "const:4:8"]]
- 00b44c94 ["CALL", null, ["callee:00c5b130:8"]]
+ 00b450bc ["INT_ADD", "register:40f0:8", ["const:b450bc:8", "const:4:8"]]
+ 00b450bc ["CALL", null, ["callee:00c5b130:8"]]
- 00b44c94 bytes 27580494
+ 00b450bc bytes 1d580494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cb0b8f805543ee4bfef9d9a682f66cc"></a>

### [`00b44edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44edc.md) → [`00b45304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45304.md) _ZN8firebase4util17jniresultcallback19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44f08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45330"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45318",
      "incomplete_value": true,
      "site": "00b45318",
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
      "definition_site": "00b44ef0",
      "incomplete_value": true,
      "site": "00b44ef0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b45314",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45318",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b44f0c"
      ]
    ],
    [
      "unmatched:00b44efc",
      "PARAM",
      [
        "storage",
        "002b04bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45314",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45318",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45334"
      ]
    ],
    [
      "00b45324",
      "PARAM",
      [
        "storage",
        "002b04fd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44edc.md#insn-00b44f00) · [`00b44f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44edc.md#insn-00b44f08) · [`00b44f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44edc.md#insn-00b44f18)

~~~diff
- 00b44f00 ["INT_ADD", "register:40f0:8", ["const:b44f00:8", "const:4:8"]]
- 00b44f00 ["CALL", null, ["callee:00c5af10:8"]]
- 00b44f00 bytes 04570494
- 00b44f08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:250:8"]]
- 00b44f08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44f08 bytes 602a01f9
- 00b44f18 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b44f18 ["RETURN", null, ["register:0:8"]]
- 00b44f18 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b732c460016e49abc99819734f0ae4d8"></a>

### [`00b44f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44f1c.md) → [`00b45344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45344.md) _ZN8firebase4util17jniresultcallback19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44f48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45370"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45358",
      "incomplete_value": true,
      "site": "00b45358",
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
      "definition_site": "00b44f30",
      "incomplete_value": true,
      "site": "00b44f30",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b45354",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b44f38",
      "PARAM",
      [
        "storage",
        "002b04bd",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b44f40",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b45354",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45360",
      "PARAM",
      [
        "storage",
        "002b04fd",
        null,
        "string"
      ]
    ],
    [
      "00b45368",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44f1c.md#insn-00b44f30) · [`00b44f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44f1c.md#insn-00b44f40) · [`00b44f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44f1c.md#insn-00b44f48)
- 新版 [`00b45358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45344.md#insn-00b45358)

~~~diff
- 00b44f30 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b44f30 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b45358 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b45358 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b44f30 bytes e80000b5
+ 00b45358 bytes e80000b5
- 00b44f40 ["INT_ADD", "register:40f0:8", ["const:b44f40:8", "const:4:8"]]
- 00b44f40 ["CALL", null, ["callee:00c5af10:8"]]
- 00b44f40 bytes f4560494
- 00b44f48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:250:8"]]
- 00b44f48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44f48 bytes 602a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9c7e4f1a59598bd582eb5657243546a"></a>

### [`00b44f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44f5c.md) → [`00b45384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45384.md) _ZN8firebase4util17jniresultcallback10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44f8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b453b4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45398",
      "incomplete_value": true,
      "site": "00b45398",
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
      "definition_site": "00b44f70",
      "incomplete_value": true,
      "site": "00b44f70",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b45394",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b44f7c",
      "PARAM",
      [
        "storage",
        "002b04bd",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b44f84",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b45394",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ],
    [
      "00b453a4",
      "PARAM",
      [
        "storage",
        "002b04fd",
        null,
        "string"
      ]
    ],
    [
      "00b453ac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44f5c.md#insn-00b44f70) · [`00b44f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44f5c.md#insn-00b44f84) · [`00b44f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44f5c.md#insn-00b44f8c)
- 新版 [`00b45398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45384.md#insn-00b45398)

~~~diff
- 00b44f70 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b44f70 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b45398 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b45398 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b44f70 bytes 080100b5
+ 00b45398 bytes 080100b5
- 00b44f84 ["INT_ADD", "register:40f0:8", ["const:b44f84:8", "const:4:8"]]
- 00b44f84 ["CALL", null, ["callee:00c5af10:8"]]
- 00b44f84 bytes e3560494
- 00b44f8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:250:8"]]
- 00b44f8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44f8c bytes 602a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-367a89b4a4ea144874c7b0887cc58dca"></a>

### [`00b44fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44fa0.md) → [`00b453c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b453c8.md) _ZN8firebase4util17jniresultcallback10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44fd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b453f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b453dc",
      "incomplete_value": true,
      "site": "00b453dc",
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
      "definition_site": "00b44fb4",
      "incomplete_value": true,
      "site": "00b44fb4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b453d8",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b44fbc",
      "PARAM",
      [
        "storage",
        "002b04bd",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b44fd0",
      "WRITE",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b453d8",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ],
    [
      "00b453e4",
      "PARAM",
      [
        "storage",
        "002b04fd",
        null,
        "string"
      ]
    ],
    [
      "00b453f8",
      "WRITE",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44fa0.md#insn-00b44fb4) · [`00b44fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44fa0.md#insn-00b44fc8) · [`00b44fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44fa0.md#insn-00b44fd0)
- 新版 [`00b453dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b453c8.md#insn-00b453dc) · [`00b453f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b453c8.md#insn-00b453f0)

~~~diff
- 00b44fb4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b44fb4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b453dc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b453dc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b44fb4 bytes 080100b5
+ 00b453dc bytes 080100b5
- 00b44fc8 ["INT_ADD", "register:40f0:8", ["const:b44fc8:8", "const:4:8"]]
- 00b44fc8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b453f0 ["INT_ADD", "register:40f0:8", ["const:b453f0:8", "const:4:8"]]
+ 00b453f0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b44fc8 bytes d2560494
+ 00b453f0 bytes c8560494
- 00b44fd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:250:8"]]
- 00b44fd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44fd0 bytes 602a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d06e887a936a09e6592d0b81c60aabb"></a>

### [`00b4512c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4512c.md) → [`00b45554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45554.md) _ZN8firebase4util17jniresultcallback14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45594",
      "incomplete_value": true,
      "site": "00b45594",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4516c",
      "incomplete_value": true,
      "site": "00b4516c",
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
            "const:250:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45570",
      "incomplete_value": true,
      "site": "00b45570",
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
      "definition_site": "00b45148",
      "incomplete_value": true,
      "site": "00b45148",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45578",
      "incomplete_value": false,
      "site": "00b4558c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4fd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45150",
      "incomplete_value": false,
      "site": "00b45164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4bd:8"
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
      "00b45568",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45578",
      "PARAM",
      [
        "storage",
        "002b04bd",
        null,
        "string"
      ]
    ],
    [
      "00b45594",
      "WRITE",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45568",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45578",
      "PARAM",
      [
        "storage",
        "002b04fd",
        null,
        "string"
      ]
    ],
    [
      "00b45594",
      "WRITE",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4512c.md#insn-00b45164) · [`00b4516c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4512c.md#insn-00b4516c) · [`00b45140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4512c.md#insn-00b45140)
- 新版 [`00b4558c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45554.md#insn-00b4558c) · [`00b45594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45554.md#insn-00b45594) · [`00b45568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45554.md#insn-00b45568)

~~~diff
- 00b45164 ["INT_ADD", "register:40f0:8", ["const:b45164:8", "const:4:8"]]
- 00b45164 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4558c ["INT_ADD", "register:40f0:8", ["const:b4558c:8", "const:4:8"]]
+ 00b4558c ["CALL", null, ["callee:00c5af10:8"]]
- 00b45164 bytes 6b560494
+ 00b4558c bytes 61560494
- 00b4516c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:250:8"]]
- 00b4516c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b45594 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:650:8"]]
+ 00b45594 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4516c bytes 802a01f9
+ 00b45594 bytes 802a03f9
- 00b45140 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:250:8"]]
- 00b45140 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b45568 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:650:8"]]
+ 00b45568 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b45140 bytes 812a41f9
+ 00b45568 bytes 812a43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9636da0e7513baf4dbc8a04232a7b709"></a>

### [`00b4519c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4519c.md) → [`00b455c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b455c4.md) _ZN8firebase4util17jniresultcallback11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b455e0",
      "incomplete_value": false,
      "site": "00b455e4",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b451b8",
      "incomplete_value": false,
      "site": "00b451bc",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b455f0",
      "incomplete_value": true,
      "site": "00b455fc",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b451c8",
      "incomplete_value": true,
      "site": "00b451d4",
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
              "INT_LEFT"
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
      "00b455e0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b455f0",
      "DATA",
      [
        "storage",
        "01125260",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b455e0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b455f0",
      "DATA",
      [
        "storage",
        "01125660",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b451bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4519c.md#insn-00b451bc) · [`00b451b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4519c.md#insn-00b451b8) · [`00b451c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4519c.md#insn-00b451c4)
- 新版 [`00b455e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b455c4.md#insn-00b455e4) · [`00b455e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b455c4.md#insn-00b455e0) · [`00b455ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b455c4.md#insn-00b455ec)

~~~diff
- 00b451bc ["INT_ADD", "register:40f0:8", ["const:b451bc:8", "const:4:8"]]
- 00b451bc ["CALL", null, ["callee:00c5b000:8"]]
+ 00b455e4 ["INT_ADD", "register:40f0:8", ["const:b455e4:8", "const:4:8"]]
+ 00b455e4 ["CALL", null, ["callee:00c5b000:8"]]
- 00b451bc bytes 91560494
+ 00b455e4 bytes 87560494
- 00b451b8 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b451b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b451b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b451b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b455e0 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b455e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b455e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b455e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b451b8 bytes 00680a91
+ 00b455e0 bytes 009c0d91
- 00b451c4 ["COPY", "tmp:0:8", ["const:260:8"]]
- 00b451c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b451c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b451c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b455ec ["COPY", "tmp:0:8", ["const:660:8"]]
+ 00b455ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b455ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b455ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b451c4 bytes 08810991
+ 00b455ec bytes 08811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43abe7f8bc711f63797b721ede006e93"></a>

### [`00b451d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b451d8.md) → [`00b45600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45600.md) _ZN8firebase4util17jniresultcallback13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45218"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45640"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b451f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b451ec",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b451f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45644"
      ]
    ],
    [
      "unmatched:00b451fc",
      "PARAM",
      [
        "storage",
        "002b04bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45614",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4561c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45644"
      ]
    ],
    [
      "00b45624",
      "PARAM",
      [
        "storage",
        "002b04fd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b451f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b451d8.md#insn-00b451f4) · [`00b45210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b451d8.md#insn-00b45210) · [`00b45218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b451d8.md#insn-00b45218)
- 新版 [`00b45638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45600.md#insn-00b45638)

~~~diff
- 00b451f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b451f4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b451f4 bytes 410100b5
- 00b45210 ["INT_ADD", "register:40f0:8", ["const:b45210:8", "const:4:8"]]
- 00b45210 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b45638 ["INT_ADD", "register:40f0:8", ["const:b45638:8", "const:4:8"]]
+ 00b45638 ["CALL", null, ["callee:00c5af10:8"]]
- 00b45210 bytes 40560494
+ 00b45638 bytes 36560494
- 00b45218 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:250:8"]]
- 00b45218 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45218 bytes 802a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4c8306774bdb2cfc32f8fe96210972b"></a>

### [`00b452c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b452c4.md) → [`00b456ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b456ec.md) _ZN8firebase4util26cppthreaddispatchercontext19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b452c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b452c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b452c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b452c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b452c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b456fc",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b456ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b456f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b456fc",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b452c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b452c4.md#insn-00b452c4) · [`00b452c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b452c4.md#insn-00b452c8) · [`00b452e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b452c4.md#insn-00b452e8)

~~~diff
- 00b452c4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b452c4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b452c4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b452c4 bytes f30f1ef8
- 00b452c8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b452c8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b452c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b452c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b452c8 bytes fd7b01a9
- 00b452e8 ["INT_ADD", "register:40f0:8", ["const:b452e8:8", "const:4:8"]]
- 00b452e8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b452e8 bytes 0a560494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df52f11fb9178d4b87c92bd6b976829e"></a>

### [`00b45348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45348.md) → [`00b45770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45770.md) _ZN8firebase4util26cppthreaddispatchercontext10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45378"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b457a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4535c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45358",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4535c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4537c"
      ]
    ],
    [
      "unmatched:00b45364",
      "PARAM",
      [
        "storage",
        "002be54b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45780",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45784",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b457a4"
      ]
    ],
    [
      "00b4578c",
      "PARAM",
      [
        "storage",
        "002be58b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4535c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45348.md#insn-00b4535c) · [`00b45370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45348.md#insn-00b45370) · [`00b45378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45348.md#insn-00b45378)
- 新版 [`00b45798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45770.md#insn-00b45798)

~~~diff
- 00b4535c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4535c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4535c bytes 080100b5
- 00b45370 ["INT_ADD", "register:40f0:8", ["const:b45370:8", "const:4:8"]]
- 00b45370 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b45798 ["INT_ADD", "register:40f0:8", ["const:b45798:8", "const:4:8"]]
+ 00b45798 ["CALL", null, ["callee:00c5af10:8"]]
- 00b45370 bytes e8550494
+ 00b45798 bytes de550494
- 00b45378 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:278:8"]]
- 00b45378 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45378 bytes 603e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d3b569ce7b6607893d00528fcf3a63a"></a>

### [`00b454d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b454d4.md) → [`00b458fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b458fc.md) _ZN8firebase4util26cppthreaddispatchercontext14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 28.57% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45514"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4593c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45918",
      "incomplete_value": true,
      "site": "00b45918",
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
      "definition_site": "00b454f0",
      "incomplete_value": true,
      "site": "00b454f0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b45910",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b454f8",
      "PARAM",
      [
        "storage",
        "002be54b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b45514",
      "WRITE",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45910",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45920",
      "PARAM",
      [
        "storage",
        "002be58b",
        null,
        "string"
      ]
    ],
    [
      "00b4593c",
      "WRITE",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b454f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b454d4.md#insn-00b454f0) · [`00b4550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b454d4.md#insn-00b4550c) · [`00b45514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b454d4.md#insn-00b45514)
- 新版 [`00b45918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b458fc.md#insn-00b45918) · [`00b45934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b458fc.md#insn-00b45934)

~~~diff
- 00b454f0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b454f0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b45918 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b45918 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b454f0 bytes 410100b5
+ 00b45918 bytes 410100b5
- 00b4550c ["INT_ADD", "register:40f0:8", ["const:b4550c:8", "const:4:8"]]
- 00b4550c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b45934 ["INT_ADD", "register:40f0:8", ["const:b45934:8", "const:4:8"]]
+ 00b45934 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4550c bytes 81550494
+ 00b45934 bytes 77550494
- 00b45514 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:278:8"]]
- 00b45514 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45514 bytes 803e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15310d92898131fad82deb8ba031c00d"></a>

### [`00b45544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45544.md) → [`00b4596c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b4596c.md) _ZN8firebase4util26cppthreaddispatchercontext11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 80.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45988",
      "incomplete_value": true,
      "site": "00b4598c",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45560",
      "incomplete_value": true,
      "site": "00b45564",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4557c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b459a4"
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
      "00b45988",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b45998",
      "DATA",
      [
        "storage",
        "01125288",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45988",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b45998",
      "DATA",
      [
        "storage",
        "01125688",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45544.md#insn-00b45564) · [`00b4557c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45544.md#insn-00b4557c)
- 新版 [`00b4598c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b4596c.md#insn-00b4598c) · [`00b459a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b4596c.md#insn-00b459a4)

~~~diff
- 00b45564 ["INT_ADD", "register:40f0:8", ["const:b45564:8", "const:4:8"]]
- 00b45564 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4598c ["INT_ADD", "register:40f0:8", ["const:b4598c:8", "const:4:8"]]
+ 00b4598c ["CALL", null, ["callee:00c5b000:8"]]
- 00b45564 bytes a7550494
+ 00b4598c bytes 9d550494
- 00b4557c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4557c ["RETURN", null, ["register:0:8"]]
- 00b4557c bytes c0035fd6
+ 00b459a4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b459a4 ["RETURN", null, ["register:0:8"]]
+ 00b459a4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6d650c940bee5d82e1e52a4ee7bde16"></a>

### [`00b45580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45580.md) → [`00b459a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b459a8.md) _ZN8firebase4util26cppthreaddispatchercontext13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45580"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45580"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45584"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45580",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45584",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45594",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b459a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b459ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b459bc",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45580.md#insn-00b45580) · [`00b45584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45580.md#insn-00b45584) · [`00b4559c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45580.md#insn-00b4559c)

~~~diff
- 00b45580 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b45580 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b45580 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b45580 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45580 bytes f44fbea9
- 00b45584 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45584 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45584 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45584 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45584 bytes fd7b01a9
- 00b4559c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4559c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b4559c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed80302cbd4ac489fccb1863ac68d0f2"></a>

### [`00b456ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b456ac.md) → [`00b45ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45ad4.md) _ZN8firebase4util19cppthreaddispatcher10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 23.53% / 新版 23.53%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b456ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b456b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b456b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b456ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b456b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b456bc",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45ad4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45ad8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45ae4",
      "READ",
      [
        "storage",
        "011256b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b456ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b456ac.md#insn-00b456ac) · [`00b456b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b456ac.md#insn-00b456b0) · [`00b456c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b456ac.md#insn-00b456c0)

~~~diff
- 00b456ac ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b456ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b456ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b456ac bytes f30f1ef8
- 00b456b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b456b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b456b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b456b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b456b0 bytes fd7b01a9
- 00b456c0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b456c0 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b456c0 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-065d1e988a649143e0d72c305ba5436d"></a>

### [`00b456f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b456f0.md) → [`00b45b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45b18.md) _ZN8firebase4util19cppthreaddispatcher10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b456f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b456f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b456f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b456f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b456f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45b28",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45b18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45b1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45b28",
      "READ",
      [
        "storage",
        "011256b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b456f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b456f0.md#insn-00b456f0) · [`00b456f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b456f0.md#insn-00b456f4) · [`00b45704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b456f0.md#insn-00b45704)
- 新版 [`00b45b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45b18.md#insn-00b45b2c)

~~~diff
- 00b456f0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b456f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b456f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b456f0 bytes f30f1ef8
- 00b456f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b456f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b456f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b456f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b456f4 bytes fd7b01a9
- 00b45704 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45704 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b45b2c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b45b2c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b45704 bytes 080100b5
+ 00b45b2c bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-277d1b4f6feb5f3d78caddec5d06ee17"></a>

### [`00b45740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45740.md) → [`00b45b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45b68.md) _ZN8firebase4util19cppthreaddispatcher15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.79% / 新版 71.79%

CFGの説明率　旧版 7.14% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b457c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45bf0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b45774",
      "incomplete_value": true,
      "site": "00b45780",
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:2b0:8"
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
      "00b45b7c",
      "READ",
      [
        "storage",
        "011252b8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b45774",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45bc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b457c0"
      ]
    ]
  ],
  "added": [
    [
      "00b45b7c",
      "READ",
      [
        "storage",
        "011256b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45b9c",
      "READ",
      [
        "storage",
        "011256b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45bc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45be8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45740.md#insn-00b45780) · [`00b45794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45740.md#insn-00b45794) · [`00b457ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45740.md#insn-00b457ac)
- 新版 [`00b45ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45b68.md#insn-00b45ba8)

~~~diff
- 00b45780 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45780 ["INT_ADD", "register:40f0:8", ["const:b45780:8", "const:4:8"]]
- 00b45780 ["CALLIND", null, ["register:0:8"]]
+ 00b45ba8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45ba8 ["INT_ADD", "register:40f0:8", ["const:b45ba8:8", "const:4:8"]]
+ 00b45ba8 ["CALLIND", null, ["register:0:8"]]
- 00b45780 bytes 00013fd6
+ 00b45ba8 bytes 00013fd6
- 00b45794 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45794 ["INT_ADD", "register:40f0:8", ["const:b45794:8", "const:4:8"]]
- 00b45794 ["CALLIND", null, ["register:0:8"]]
- 00b45794 bytes 00013fd6
- 00b457ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b457ac ["INT_ADD", "register:40f0:8", ["const:b457ac:8", "const:4:8"]]
- 00b457ac ["CALLIND", null, ["register:0:8"]]
- 00b457ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7022caa9e9810cdfdade94c5c071341"></a>

### [`00b457dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b457dc.md) → [`00b45c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45c04.md) _ZN8firebase4util19cppthreaddispatcher12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 36.36% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45818"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45c90",
      "incomplete_value": true,
      "site": "00b45c90",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45868",
      "incomplete_value": true,
      "site": "00b45868",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45c40"
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
      "00b45c18",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45c24",
      "READ",
      [
        "storage",
        "011252b8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b45818",
      "WRITE",
      [
        "storage",
        "011252b8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b45c18",
      "READ",
      [
        "storage",
        "011256b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45c24",
      "READ",
      [
        "storage",
        "011256b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45c40",
      "WRITE",
      [
        "storage",
        "011256b8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b457f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b457dc.md#insn-00b457f4) · [`00b45814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b457dc.md#insn-00b45814) · [`00b45818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b457dc.md#insn-00b45818)
- 新版 [`00b45c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45c04.md#insn-00b45c1c)

~~~diff
- 00b457f4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b457f4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b45c1c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b45c1c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b457f4 bytes c10300b4
+ 00b45c1c bytes c10300b4
- 00b45814 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45814 ["INT_ADD", "register:40f0:8", ["const:b45814:8", "const:4:8"]]
- 00b45814 ["CALLIND", null, ["register:0:8"]]
- 00b45814 bytes 00013fd6
- 00b45818 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b45818 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b45818 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2b8:8"]]
- 00b45818 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b45818 bytes bfe20a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1336063512f8b54e2d88fc2a324c4d24"></a>

### [`00b4587c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4587c.md) → [`00b45ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45ca4.md) _ZN8firebase4util19cppthreaddispatcher14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4587c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4587c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45880"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4587c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45880",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45890",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45ca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45ca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45cb8",
      "READ",
      [
        "storage",
        "011256b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4587c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4587c.md#insn-00b4587c) · [`00b45880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4587c.md#insn-00b45880) · [`00b45898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4587c.md#insn-00b45898)

~~~diff
- 00b4587c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4587c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4587c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4587c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4587c bytes f44fbea9
- 00b45880 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45880 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45880 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45880 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45880 bytes fd7b01a9
- 00b45898 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b45898 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b45898 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d1ebe096f2aebe36642feff52dcc758"></a>

### [`00b45928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45928.md) → [`00b45d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45d50.md) _ZN8firebase4util19cppthreaddispatcher13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4592c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45928",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4592c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4593c",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45d50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45d54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45d64",
      "READ",
      [
        "storage",
        "011256b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45928.md#insn-00b45928) · [`00b4592c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45928.md#insn-00b4592c) · [`00b45944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45928.md#insn-00b45944)

~~~diff
- 00b45928 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b45928 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b45928 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b45928 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45928 bytes f44fbea9
- 00b4592c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4592c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4592c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4592c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4592c bytes fd7b01a9
- 00b45944 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b45944 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b45944 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-757c5b128302c1ee301e519f6471e89f"></a>

### [`00b45a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a98.md) → [`00b45ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45ec0.md) _ZN8firebase4util3log10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45ac8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45ef0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45aac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45aa8",
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b45aac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45acc"
      ]
    ],
    [
      "unmatched:00b45ab4",
      "PARAM",
      [
        "storage",
        "002bbd77",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45ed0",
      "READ",
      [
        "storage",
        "011256d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45ed4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45ef4"
      ]
    ],
    [
      "00b45edc",
      "PARAM",
      [
        "storage",
        "002bbdb7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a98.md#insn-00b45aac) · [`00b45ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a98.md#insn-00b45ac0) · [`00b45ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a98.md#insn-00b45ac8)
- 新版 [`00b45ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45ec0.md#insn-00b45ee8)

~~~diff
- 00b45aac ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45aac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b45aac bytes 080100b5
- 00b45ac0 ["INT_ADD", "register:40f0:8", ["const:b45ac0:8", "const:4:8"]]
- 00b45ac0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b45ee8 ["INT_ADD", "register:40f0:8", ["const:b45ee8:8", "const:4:8"]]
+ 00b45ee8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b45ac0 bytes 14540494
+ 00b45ee8 bytes 0a540494
- 00b45ac8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2d8:8"]]
- 00b45ac8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45ac8 bytes 606e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03b6997051a49c19ee756be5a72ccc59"></a>

### [`00b45ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45ae8.md) → [`00b45f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45f10.md) _ZN8firebase4util3log15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 30.77% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45f98",
      "incomplete_value": true,
      "site": "00b45f98",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45b70",
      "incomplete_value": true,
      "site": "00b45b70",
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
            "const:2e0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45f44",
      "incomplete_value": true,
      "site": "00b45f50",
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:6d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45b1c",
      "incomplete_value": true,
      "site": "00b45b28",
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:2d8:8"
              ]
            ]
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
      "definition_site": "00b45f40",
      "incomplete_value": true,
      "site": "00b45f50",
      "value": [
        "live",
        "register:4008:8"
      ]
    },
    "old": null,
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
      "00b45f24",
      "READ",
      [
        "storage",
        "011252e0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b45b1c",
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45f98",
      "WRITE",
      [
        "storage",
        "011252e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b45f24",
      "READ",
      [
        "storage",
        "011256e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45f44",
      "READ",
      [
        "storage",
        "011256d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45f98",
      "WRITE",
      [
        "storage",
        "011256e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45ae8.md#insn-00b45b28) · [`00b45b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45ae8.md#insn-00b45b3c) · [`00b45b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45ae8.md#insn-00b45b64)
- 新版 [`00b45f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45f10.md#insn-00b45f50) · [`00b45f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45f10.md#insn-00b45f64)

~~~diff
- 00b45b28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45b28 ["INT_ADD", "register:40f0:8", ["const:b45b28:8", "const:4:8"]]
- 00b45b28 ["CALLIND", null, ["register:0:8"]]
+ 00b45f50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45f50 ["INT_ADD", "register:40f0:8", ["const:b45f50:8", "const:4:8"]]
+ 00b45f50 ["CALLIND", null, ["register:0:8"]]
- 00b45b28 bytes 00013fd6
+ 00b45f50 bytes 00013fd6
- 00b45b3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45b3c ["INT_ADD", "register:40f0:8", ["const:b45b3c:8", "const:4:8"]]
- 00b45b3c ["CALLIND", null, ["register:0:8"]]
+ 00b45f64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45f64 ["INT_ADD", "register:40f0:8", ["const:b45f64:8", "const:4:8"]]
+ 00b45f64 ["CALLIND", null, ["register:0:8"]]
- 00b45b3c bytes 00013fd6
+ 00b45f64 bytes 00013fd6
- 00b45b64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45b64 ["INT_ADD", "register:40f0:8", ["const:b45b64:8", "const:4:8"]]
- 00b45b64 ["CALLIND", null, ["register:0:8"]]
- 00b45b64 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16c14cf00e2b2605faf7e22cb83239d4"></a>

### [`00b45c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45c24.md) → [`00b4604c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4604c.md) _ZN8firebase4util3log14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45c64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4608c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45c40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45c38",
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b45c40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46090"
      ]
    ],
    [
      "unmatched:00b45c48",
      "PARAM",
      [
        "storage",
        "002bbd77",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46060",
      "READ",
      [
        "storage",
        "011256d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46068",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46090"
      ]
    ],
    [
      "00b46070",
      "PARAM",
      [
        "storage",
        "002bbdb7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45c24.md#insn-00b45c40) · [`00b45c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45c24.md#insn-00b45c5c) · [`00b45c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45c24.md#insn-00b45c64)
- 新版 [`00b46084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4604c.md#insn-00b46084)

~~~diff
- 00b45c40 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b45c40 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b45c40 bytes 410100b5
- 00b45c5c ["INT_ADD", "register:40f0:8", ["const:b45c5c:8", "const:4:8"]]
- 00b45c5c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b46084 ["INT_ADD", "register:40f0:8", ["const:b46084:8", "const:4:8"]]
+ 00b46084 ["CALL", null, ["callee:00c5af10:8"]]
- 00b45c5c bytes ad530494
+ 00b46084 bytes a3530494
- 00b45c64 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2d8:8"]]
- 00b45c64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45c64 bytes 806e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff683b9cef7de9db338b45256f752cf3"></a>

### [`00b45cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45cd0.md) → [`00b460f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b460f8.md) _ZN8firebase4util3log13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45cd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45cd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45cd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45cd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45cd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45ce4",
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b460f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b460fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4610c",
      "READ",
      [
        "storage",
        "011256d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45cd0.md#insn-00b45cd0) · [`00b45cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45cd0.md#insn-00b45cd4) · [`00b45cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45cd0.md#insn-00b45cec)

~~~diff
- 00b45cd0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b45cd0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b45cd0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b45cd0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45cd0 bytes f44fbea9
- 00b45cd4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45cd4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45cd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45cd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45cd4 bytes fd7b01a9
- 00b45cec ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b45cec ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b45cec bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6e1b5ed69a2bda0a80863ba9a071999"></a>

### [`00b45d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45d7c.md) → [`00b461a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b461a4.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45da8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b461d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b461b8",
      "incomplete_value": true,
      "site": "00b461b8",
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
      "definition_site": "00b45d90",
      "incomplete_value": true,
      "site": "00b45d90",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b461b4",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b461b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45dac"
      ]
    ],
    [
      "unmatched:00b45d9c",
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b461b4",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b461b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b461d4"
      ]
    ],
    [
      "00b461c4",
      "PARAM",
      [
        "storage",
        "002af30d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45d7c.md#insn-00b45d90) · [`00b45da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45d7c.md#insn-00b45da0) · [`00b45da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45d7c.md#insn-00b45da8)
- 新版 [`00b461b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b461a4.md#insn-00b461b8)

~~~diff
- 00b45d90 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45d90 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b461b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b461b8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b45d90 bytes e80000b5
+ 00b461b8 bytes e80000b5
- 00b45da0 ["INT_ADD", "register:40f0:8", ["const:b45da0:8", "const:4:8"]]
- 00b45da0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b45da0 bytes 5c530494
- 00b45da8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
- 00b45da8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45da8 bytes 607e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57f7e91b5dfeb8f30e171d2ee54f1bf3"></a>

### [`00b45dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45dbc.md) → [`00b461e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b461e4.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 43.75% / 新版 43.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45de8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46210"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b461f8",
      "incomplete_value": true,
      "site": "00b461f8",
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
      "definition_site": "00b45dd0",
      "incomplete_value": true,
      "site": "00b45dd0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b461f4",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b461f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45dec"
      ]
    ],
    [
      "unmatched:00b45dd8",
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b461f4",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b461f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46214"
      ]
    ],
    [
      "00b46200",
      "PARAM",
      [
        "storage",
        "002af30d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45dbc.md#insn-00b45dd0) · [`00b45de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45dbc.md#insn-00b45de0) · [`00b45de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45dbc.md#insn-00b45de8)
- 新版 [`00b461f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b461e4.md#insn-00b461f8)

~~~diff
- 00b45dd0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45dd0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b461f8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b461f8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b45dd0 bytes e80000b5
+ 00b461f8 bytes e80000b5
- 00b45de0 ["INT_ADD", "register:40f0:8", ["const:b45de0:8", "const:4:8"]]
- 00b45de0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b45de0 bytes 4c530494
- 00b45de8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
- 00b45de8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45de8 bytes 607e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcac8c9598b61cc6605c39adb388511f"></a>

### [`00b45e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e40.md) → [`00b46268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46268.md) _ZN8firebase4util10uribuilder10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 58.82% / 新版 58.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45e44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45e44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46298",
      "incomplete_value": true,
      "site": "00b46298",
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
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45e70",
      "incomplete_value": true,
      "site": "00b45e70",
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
            "const:2f8:8"
          ]
        ]
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
      "unmatched:00b45e44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45e50",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b45e54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4629c"
      ]
    ]
  ],
  "added": [
    [
      "00b4626c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b46278",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4627c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4629c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e40.md#insn-00b45e44) · [`00b45e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e40.md#insn-00b45e54) · [`00b45e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e40.md#insn-00b45e68)
- 新版 [`00b46290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46268.md#insn-00b46290)

~~~diff
- 00b45e44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45e44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45e44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45e44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45e44 bytes fd7b01a9
- 00b45e54 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45e54 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b45e54 bytes 080100b5
- 00b45e68 ["INT_ADD", "register:40f0:8", ["const:b45e68:8", "const:4:8"]]
- 00b45e68 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b46290 ["INT_ADD", "register:40f0:8", ["const:b46290:8", "const:4:8"]]
+ 00b46290 ["CALL", null, ["callee:00c5af10:8"]]
- 00b45e68 bytes 2a530494
+ 00b46290 bytes 20530494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c982cd35be2f71646843063e9ee31c9"></a>

### [`00b45e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e90.md) → [`00b462b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b462b8.md) _ZN8firebase4util10uribuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.49% / 新版 79.49%

CFGの説明率　旧版 20.00% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45f18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46340"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b462ec",
      "incomplete_value": true,
      "site": "00b462f8",
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
                "const:1125000:8"
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
      "definition_site": "00b45ec4",
      "incomplete_value": true,
      "site": "00b45ed0",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:2f8:8"
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
      "00b462cc",
      "READ",
      [
        "storage",
        "01125300",
        null,
        "undefined1"
      ]
    ],
    [
      "00b462d8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45f1c"
      ]
    ],
    [
      "00b462ec",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b462cc",
      "READ",
      [
        "storage",
        "01125700",
        null,
        "undefined1"
      ]
    ],
    [
      "00b462d8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46344"
      ]
    ],
    [
      "00b462ec",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e90.md#insn-00b45ed0) · [`00b45efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e90.md#insn-00b45efc) · [`00b45f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e90.md#insn-00b45f18)
- 新版 [`00b462f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b462b8.md#insn-00b462f8)

~~~diff
- 00b45ed0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45ed0 ["INT_ADD", "register:40f0:8", ["const:b45ed0:8", "const:4:8"]]
- 00b45ed0 ["CALLIND", null, ["register:0:8"]]
+ 00b462f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b462f8 ["INT_ADD", "register:40f0:8", ["const:b462f8:8", "const:4:8"]]
+ 00b462f8 ["CALLIND", null, ["register:0:8"]]
- 00b45ed0 bytes 00013fd6
+ 00b462f8 bytes 00013fd6
- 00b45efc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45efc ["INT_ADD", "register:40f0:8", ["const:b45efc:8", "const:4:8"]]
- 00b45efc ["CALLIND", null, ["register:0:8"]]
- 00b45efc bytes 00013fd6
- 00b45f18 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b45f18 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:300:8"]]
- 00b45f18 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b45f18 bytes a0020c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-054a49099e98398f5f8969d3e5401149"></a>

### [`00b45f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45f2c.md) → [`00b46354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46354.md) _ZN8firebase4util10uribuilder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 25.00% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45f2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45f30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45f30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45f2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45f30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45f34",
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
      "00b46354",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b46358",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4635c",
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

- 旧版 [`00b45f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45f2c.md#insn-00b45f2c) · [`00b45f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45f2c.md#insn-00b45f30) · [`00b45f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45f2c.md#insn-00b45f34)

~~~diff
- 00b45f2c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b45f2c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b45f2c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45f2c bytes f50f1df8
- 00b45f30 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b45f30 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b45f30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45f30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45f30 bytes f44f01a9
- 00b45f34 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45f34 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45f34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b45f34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45f34 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cf6d85766f1aa729c3126c786ae7cd5"></a>

### [`00b45fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45fcc.md) → [`00b463f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b463f4.md) _ZN8firebase4util10uribuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4600c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46434"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45fe8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45fe0",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b45fe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46438"
      ]
    ],
    [
      "unmatched:00b45ff0",
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46408",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46410",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46438"
      ]
    ],
    [
      "00b46418",
      "PARAM",
      [
        "storage",
        "002af30d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45fcc.md#insn-00b45fe8) · [`00b46004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45fcc.md#insn-00b46004) · [`00b4600c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45fcc.md#insn-00b4600c)
- 新版 [`00b4642c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b463f4.md#insn-00b4642c)

~~~diff
- 00b45fe8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b45fe8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b45fe8 bytes 410100b5
- 00b46004 ["INT_ADD", "register:40f0:8", ["const:b46004:8", "const:4:8"]]
- 00b46004 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4642c ["INT_ADD", "register:40f0:8", ["const:b4642c:8", "const:4:8"]]
+ 00b4642c ["CALL", null, ["callee:00c5af10:8"]]
- 00b46004 bytes c3520494
+ 00b4642c bytes b9520494
- 00b4600c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
- 00b4600c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4600c bytes 807e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca26bbb99a2fb6ba108fd1b259bc36ec"></a>

### [`00b46078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46078.md) → [`00b464a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b464a0.md) _ZN8firebase4util10uribuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b464e0",
      "incomplete_value": true,
      "site": "00b464e0",
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
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b460b8",
      "incomplete_value": true,
      "site": "00b460b8",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b464bc",
      "incomplete_value": true,
      "site": "00b464bc",
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
      "definition_site": "00b46094",
      "incomplete_value": true,
      "site": "00b46094",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b464c4",
      "incomplete_value": false,
      "site": "00b464d8",
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
            "const:30d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4609c",
      "incomplete_value": false,
      "site": "00b460b0",
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
            "const:2cd:8"
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
      "00b464b4",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b464c4",
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ],
    [
      "00b464e0",
      "WRITE",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b464b4",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b464c4",
      "PARAM",
      [
        "storage",
        "002af30d",
        null,
        "string"
      ]
    ],
    [
      "00b464e0",
      "WRITE",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b460b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46078.md#insn-00b460b0) · [`00b460b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46078.md#insn-00b460b8) · [`00b4608c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46078.md#insn-00b4608c)
- 新版 [`00b464d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b464a0.md#insn-00b464d8) · [`00b464e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b464a0.md#insn-00b464e0) · [`00b464b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b464a0.md#insn-00b464b4)

~~~diff
- 00b460b0 ["INT_ADD", "register:40f0:8", ["const:b460b0:8", "const:4:8"]]
- 00b460b0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b464d8 ["INT_ADD", "register:40f0:8", ["const:b464d8:8", "const:4:8"]]
+ 00b464d8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b460b0 bytes 98520494
+ 00b464d8 bytes 8e520494
- 00b460b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
- 00b460b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b464e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6f8:8"]]
+ 00b464e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b460b8 bytes 807e01f9
+ 00b464e0 bytes 807e03f9
- 00b4608c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
- 00b4608c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b464b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6f8:8"]]
+ 00b464b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4608c bytes 817e41f9
+ 00b464b4 bytes 817e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae0d5919c85c68f031edeb03c5fd04e5"></a>

### [`00b46124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46124.md) → [`00b4654c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4654c.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46578",
      "incomplete_value": true,
      "site": "00b46578",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46150",
      "incomplete_value": true,
      "site": "00b46150",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46560",
      "incomplete_value": true,
      "site": "00b46560",
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
      "definition_site": "00b46138",
      "incomplete_value": true,
      "site": "00b46138",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4656c",
      "incomplete_value": false,
      "site": "00b46570",
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
            "const:121:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46144",
      "incomplete_value": false,
      "site": "00b46148",
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
            "const:e1:8"
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
      "00b4655c",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4656c",
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      "00b46578",
      "WRITE",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4655c",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4656c",
      "PARAM",
      [
        "storage",
        "002bd121",
        null,
        "string"
      ]
    ],
    [
      "00b46578",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46124.md#insn-00b46148) · [`00b46150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46124.md#insn-00b46150) · [`00b46134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46124.md#insn-00b46134)
- 新版 [`00b46570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4654c.md#insn-00b46570) · [`00b46578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4654c.md#insn-00b46578) · [`00b4655c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4654c.md#insn-00b4655c)

~~~diff
- 00b46148 ["INT_ADD", "register:40f0:8", ["const:b46148:8", "const:4:8"]]
- 00b46148 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b46570 ["INT_ADD", "register:40f0:8", ["const:b46570:8", "const:4:8"]]
+ 00b46570 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46148 bytes 72520494
+ 00b46570 bytes 68520494
- 00b46150 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00b46150 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46578 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00b46578 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46150 bytes 609601f9
+ 00b46578 bytes 609603f9
- 00b46134 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00b46134 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4655c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00b4655c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46134 bytes 689641f9
+ 00b4655c bytes 689643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61c4525f0043d316151efae7d4b26077"></a>

### [`00b46164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46164.md) → [`00b4658c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4658c.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b465b8",
      "incomplete_value": true,
      "site": "00b465b8",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46190",
      "incomplete_value": true,
      "site": "00b46190",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b465a0",
      "incomplete_value": true,
      "site": "00b465a0",
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
      "definition_site": "00b46178",
      "incomplete_value": true,
      "site": "00b46178",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b465a8",
      "incomplete_value": false,
      "site": "00b465b0",
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
            "const:121:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46180",
      "incomplete_value": false,
      "site": "00b46188",
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
            "const:e1:8"
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
      "00b4659c",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "00b465a8",
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      "00b465b8",
      "WRITE",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4659c",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b465a8",
      "PARAM",
      [
        "storage",
        "002bd121",
        null,
        "string"
      ]
    ],
    [
      "00b465b8",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46164.md#insn-00b46188) · [`00b46190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46164.md#insn-00b46190) · [`00b46174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46164.md#insn-00b46174)
- 新版 [`00b465b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4658c.md#insn-00b465b0) · [`00b465b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4658c.md#insn-00b465b8) · [`00b4659c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4658c.md#insn-00b4659c)

~~~diff
- 00b46188 ["INT_ADD", "register:40f0:8", ["const:b46188:8", "const:4:8"]]
- 00b46188 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b465b0 ["INT_ADD", "register:40f0:8", ["const:b465b0:8", "const:4:8"]]
+ 00b465b0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46188 bytes 62520494
+ 00b465b0 bytes 58520494
- 00b46190 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00b46190 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b465b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00b465b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46190 bytes 609601f9
+ 00b465b8 bytes 609603f9
- 00b46174 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00b46174 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4659c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00b4659c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46174 bytes 689641f9
+ 00b4659c bytes 689643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db6bd9b5b1eddcbcebb5769b2a6ff28e"></a>

### [`00b461a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461a4.md) → [`00b465cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b465cc.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b461d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b465fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b465e0",
      "incomplete_value": true,
      "site": "00b465e0",
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
      "definition_site": "00b461b8",
      "incomplete_value": true,
      "site": "00b461b8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b465dc",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b461c4",
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b461cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b465dc",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b465ec",
      "PARAM",
      [
        "storage",
        "002bd121",
        null,
        "string"
      ]
    ],
    [
      "00b465f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b461b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461a4.md#insn-00b461b8) · [`00b461cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461a4.md#insn-00b461cc) · [`00b461d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461a4.md#insn-00b461d4)
- 新版 [`00b465e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b465cc.md#insn-00b465e0)

~~~diff
- 00b461b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b461b8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b465e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b465e0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b461b8 bytes 080100b5
+ 00b465e0 bytes 080100b5
- 00b461cc ["INT_ADD", "register:40f0:8", ["const:b461cc:8", "const:4:8"]]
- 00b461cc ["CALL", null, ["callee:00c5af10:8"]]
- 00b461cc bytes 51520494
- 00b461d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00b461d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b461d4 bytes 609601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8c5e67f3fce155242fa3988b944f08e"></a>

### [`00b461e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461e8.md) → [`00b46610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46610.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46218"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46640"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46624",
      "incomplete_value": true,
      "site": "00b46624",
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
      "definition_site": "00b461fc",
      "incomplete_value": true,
      "site": "00b461fc",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46620",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46624",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4621c"
      ]
    ],
    [
      "unmatched:00b46204",
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46620",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46624",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46644"
      ]
    ],
    [
      "00b4662c",
      "PARAM",
      [
        "storage",
        "002bd121",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461e8.md#insn-00b46210) · [`00b46218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461e8.md#insn-00b46218) · [`00b46228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461e8.md#insn-00b46228)
- 新版 [`00b46638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46610.md#insn-00b46638)

~~~diff
- 00b46210 ["INT_ADD", "register:40f0:8", ["const:b46210:8", "const:4:8"]]
- 00b46210 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b46638 ["INT_ADD", "register:40f0:8", ["const:b46638:8", "const:4:8"]]
+ 00b46638 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46210 bytes 40520494
+ 00b46638 bytes 36520494
- 00b46218 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00b46218 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46218 bytes 609601f9
- 00b46228 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b46228 ["RETURN", null, ["register:0:8"]]
- 00b46228 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-361cec80722af9a064d91158e5b65946"></a>

### [`00b46238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46238.md) → [`00b46660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46660.md) _ZN8firebase4util3url15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 37.50% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b466e8",
      "incomplete_value": true,
      "site": "00b466e8",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b462c0",
      "incomplete_value": true,
      "site": "00b462c0",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46694",
      "incomplete_value": true,
      "site": "00b466a0",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4626c",
      "incomplete_value": true,
      "site": "00b46278",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:328:8"
              ]
            ]
          ]
        ]
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
      "site": "00b4628c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46674",
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b4626c",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "00b466e8",
      "WRITE",
      [
        "storage",
        "01125330",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46674",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46694",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b466e8",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46238.md#insn-00b46278) · [`00b4628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46238.md#insn-00b4628c) · [`00b462c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46238.md#insn-00b462c0)
- 新版 [`00b466a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46660.md#insn-00b466a0) · [`00b466e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46660.md#insn-00b466e8)

~~~diff
- 00b46278 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46278 ["INT_ADD", "register:40f0:8", ["const:b46278:8", "const:4:8"]]
- 00b46278 ["CALLIND", null, ["register:0:8"]]
+ 00b466a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b466a0 ["INT_ADD", "register:40f0:8", ["const:b466a0:8", "const:4:8"]]
+ 00b466a0 ["CALLIND", null, ["register:0:8"]]
- 00b46278 bytes 00013fd6
+ 00b466a0 bytes 00013fd6
- 00b4628c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4628c ["INT_ADD", "register:40f0:8", ["const:b4628c:8", "const:4:8"]]
- 00b4628c ["CALLIND", null, ["register:0:8"]]
- 00b4628c bytes 00013fd6
- 00b462c0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b462c0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:330:8"]]
- 00b462c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b466e8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b466e8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:730:8"]]
+ 00b466e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b462c0 bytes a0c20c39
+ 00b466e8 bytes a0c21c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b745eff9abcc8eb8a02d8a6186f3583c"></a>

### [`00b462d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b462d4.md) → [`00b466fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b466fc.md) _ZN8firebase4util3url12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.00% / 新版 65.00%

CFGの説明率　旧版 30.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46788",
      "incomplete_value": true,
      "site": "00b46788",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46360",
      "incomplete_value": true,
      "site": "00b46360",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46738"
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
      "00b46710",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4671c",
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b46310",
      "WRITE",
      [
        "storage",
        "01125330",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46710",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4671c",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46738",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b462ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b462d4.md#insn-00b462ec) · [`00b4630c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b462d4.md#insn-00b4630c) · [`00b46310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b462d4.md#insn-00b46310)
- 新版 [`00b46714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b466fc.md#insn-00b46714)

~~~diff
- 00b462ec ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b462ec ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b46714 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b46714 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b462ec bytes c10300b4
+ 00b46714 bytes c10300b4
- 00b4630c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4630c ["INT_ADD", "register:40f0:8", ["const:b4630c:8", "const:4:8"]]
- 00b4630c ["CALLIND", null, ["register:0:8"]]
- 00b4630c bytes 00013fd6
- 00b46310 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b46310 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b46310 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:330:8"]]
- 00b46310 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b46310 bytes bfc20c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41c3f31f0d42668ff0c61ccf259d86ae"></a>

### [`00b46374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46374.md) → [`00b4679c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4679c.md) _ZN8firebase4util3url14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b467dc",
      "incomplete_value": true,
      "site": "00b467dc",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b463b4",
      "incomplete_value": true,
      "site": "00b463b4",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b467b8",
      "incomplete_value": true,
      "site": "00b467b8",
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
      "definition_site": "00b46390",
      "incomplete_value": true,
      "site": "00b46390",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b467c0",
      "incomplete_value": false,
      "site": "00b467d4",
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
            "const:121:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46398",
      "incomplete_value": false,
      "site": "00b463ac",
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
            "const:e1:8"
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
      "00b467b0",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "00b467c0",
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      "00b467dc",
      "WRITE",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b467b0",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b467c0",
      "PARAM",
      [
        "storage",
        "002bd121",
        null,
        "string"
      ]
    ],
    [
      "00b467dc",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b463ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46374.md#insn-00b463ac) · [`00b463b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46374.md#insn-00b463b4) · [`00b46388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46374.md#insn-00b46388)
- 新版 [`00b467d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4679c.md#insn-00b467d4) · [`00b467dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4679c.md#insn-00b467dc) · [`00b467b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4679c.md#insn-00b467b0)

~~~diff
- 00b463ac ["INT_ADD", "register:40f0:8", ["const:b463ac:8", "const:4:8"]]
- 00b463ac ["CALL", null, ["callee:00c5af10:8"]]
+ 00b467d4 ["INT_ADD", "register:40f0:8", ["const:b467d4:8", "const:4:8"]]
+ 00b467d4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b463ac bytes d9510494
+ 00b467d4 bytes cf510494
- 00b463b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
- 00b463b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b467dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
+ 00b467dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b463b4 bytes 809601f9
+ 00b467dc bytes 809603f9
- 00b46388 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
- 00b46388 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b467b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
+ 00b467b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46388 bytes 819641f9
+ 00b467b0 bytes 819643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74fcf8e988ef53df2c636f0e6ea2570c"></a>

### [`00b463e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b463e4.md) → [`00b4680c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4680c.md) _ZN8firebase4util3url11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46828",
      "incomplete_value": false,
      "site": "00b4682c",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46400",
      "incomplete_value": false,
      "site": "00b46404",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b46838",
      "incomplete_value": true,
      "site": "00b46844",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46410",
      "incomplete_value": true,
      "site": "00b4641c",
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
              "INT_LEFT"
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
      "00b46828",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b46838",
      "DATA",
      [
        "storage",
        "01125338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46828",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b46838",
      "DATA",
      [
        "storage",
        "01125738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b463e4.md#insn-00b46404) · [`00b46400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b463e4.md#insn-00b46400) · [`00b4640c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b463e4.md#insn-00b4640c)
- 新版 [`00b4682c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4680c.md#insn-00b4682c) · [`00b46828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4680c.md#insn-00b46828) · [`00b46834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4680c.md#insn-00b46834)

~~~diff
- 00b46404 ["INT_ADD", "register:40f0:8", ["const:b46404:8", "const:4:8"]]
- 00b46404 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4682c ["INT_ADD", "register:40f0:8", ["const:b4682c:8", "const:4:8"]]
+ 00b4682c ["CALL", null, ["callee:00c5b000:8"]]
- 00b46404 bytes ff510494
+ 00b4682c bytes f5510494
- 00b46400 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b46400 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46400 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46400 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46828 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b46828 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46828 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46828 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46400 bytes 00680a91
+ 00b46828 bytes 009c0d91
- 00b4640c ["COPY", "tmp:0:8", ["const:338:8"]]
- 00b4640c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4640c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4640c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b46834 ["COPY", "tmp:0:8", ["const:738:8"]]
+ 00b46834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b46834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b46834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4640c bytes 08e10c91
+ 00b46834 bytes 08e11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-773ccb7f3c68012ab528cfbcfebe5bed"></a>

### [`00b46420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46420.md) → [`00b46848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46848.md) _ZN8firebase4util3url13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46460"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46888"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4643c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b46434",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4643c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4688c"
      ]
    ],
    [
      "unmatched:00b46444",
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4685c",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46864",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4688c"
      ]
    ],
    [
      "00b4686c",
      "PARAM",
      [
        "storage",
        "002bd121",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4643c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46420.md#insn-00b4643c) · [`00b46458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46420.md#insn-00b46458) · [`00b46460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46420.md#insn-00b46460)
- 新版 [`00b46880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46848.md#insn-00b46880)

~~~diff
- 00b4643c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4643c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4643c bytes 410100b5
- 00b46458 ["INT_ADD", "register:40f0:8", ["const:b46458:8", "const:4:8"]]
- 00b46458 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b46880 ["INT_ADD", "register:40f0:8", ["const:b46880:8", "const:4:8"]]
+ 00b46880 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46458 bytes ae510494
+ 00b46880 bytes a4510494
- 00b46460 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
- 00b46460 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46460 bytes 809601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-137db6dbbfad0b4d553ef70eb7598c42"></a>

### [`00b464cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b464cc.md) → [`00b468f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b468f4.md) _ZN8firebase4util18file_output_stream19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b464cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b464d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b464d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b464cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b464d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b46904",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b468f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b468f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b46904",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b464cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b464cc.md#insn-00b464cc) · [`00b464d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b464cc.md#insn-00b464d0) · [`00b464e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b464cc.md#insn-00b464e0)
- 新版 [`00b46908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b468f4.md#insn-00b46908)

~~~diff
- 00b464cc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b464cc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b464cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b464cc bytes f30f1ef8
- 00b464d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b464d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b464d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b464d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b464d0 bytes fd7b01a9
- 00b464e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b464e0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b46908 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b46908 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b464e0 bytes e80000b5
+ 00b46908 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34d87eea51c523fcd452421608b264d3"></a>

### [`00b4650c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4650c.md) → [`00b46934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46934.md) _ZN8firebase4util18file_output_stream19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 20.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46538"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46960"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46948",
      "incomplete_value": true,
      "site": "00b46948",
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
      "definition_site": "00b46520",
      "incomplete_value": true,
      "site": "00b46520",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46944",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46528",
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b46530",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b46944",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46950",
      "PARAM",
      [
        "storage",
        "002b0534",
        null,
        "string"
      ]
    ],
    [
      "00b46958",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4650c.md#insn-00b46520) · [`00b46530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4650c.md#insn-00b46530) · [`00b46538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4650c.md#insn-00b46538)
- 新版 [`00b46948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46934.md#insn-00b46948)

~~~diff
- 00b46520 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b46520 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b46948 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b46948 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b46520 bytes e80000b5
+ 00b46948 bytes e80000b5
- 00b46530 ["INT_ADD", "register:40f0:8", ["const:b46530:8", "const:4:8"]]
- 00b46530 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46530 bytes 78510494
- 00b46538 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b46538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46538 bytes 60aa01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8fb6d0afad2b8fa26def447343a7d06"></a>

### [`00b4654c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4654c.md) → [`00b46974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46974.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4657c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b469a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46988",
      "incomplete_value": true,
      "site": "00b46988",
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
      "definition_site": "00b46560",
      "incomplete_value": true,
      "site": "00b46560",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46984",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4656c",
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b46574",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b46984",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46994",
      "PARAM",
      [
        "storage",
        "002b0534",
        null,
        "string"
      ]
    ],
    [
      "00b4699c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4654c.md#insn-00b46560) · [`00b46574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4654c.md#insn-00b46574) · [`00b4657c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4654c.md#insn-00b4657c)
- 新版 [`00b46988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46974.md#insn-00b46988)

~~~diff
- 00b46560 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b46560 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b46988 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b46988 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b46560 bytes 080100b5
+ 00b46988 bytes 080100b5
- 00b46574 ["INT_ADD", "register:40f0:8", ["const:b46574:8", "const:4:8"]]
- 00b46574 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46574 bytes 67510494
- 00b4657c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b4657c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4657c bytes 60aa01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6ad35a3c50aff814d66183e01089994"></a>

### [`00b46590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46590.md) → [`00b469b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b469b8.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b465c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b469e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b469cc",
      "incomplete_value": true,
      "site": "00b469cc",
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
      "definition_site": "00b465a4",
      "incomplete_value": true,
      "site": "00b465a4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b469c8",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b465ac",
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b465c0",
      "WRITE",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b469c8",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b469d4",
      "PARAM",
      [
        "storage",
        "002b0534",
        null,
        "string"
      ]
    ],
    [
      "00b469e8",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b465a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46590.md#insn-00b465a4) · [`00b465b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46590.md#insn-00b465b8) · [`00b465c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46590.md#insn-00b465c0)
- 新版 [`00b469cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b469b8.md#insn-00b469cc) · [`00b469e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b469b8.md#insn-00b469e0)

~~~diff
- 00b465a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b465a4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b469cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b469cc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b465a4 bytes 080100b5
+ 00b469cc bytes 080100b5
- 00b465b8 ["INT_ADD", "register:40f0:8", ["const:b465b8:8", "const:4:8"]]
- 00b465b8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b469e0 ["INT_ADD", "register:40f0:8", ["const:b469e0:8", "const:4:8"]]
+ 00b469e0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b465b8 bytes 56510494
+ 00b469e0 bytes 4c510494
- 00b465c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b465c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b465c0 bytes 60aa01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e90f59f0f7cb076a6895fea74acdc3fd"></a>

### [`00b465e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b465e0.md) → [`00b46a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46a08.md) _ZN8firebase4util18file_output_stream15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.49% / 新版 79.49%

CFGの説明率　旧版 28.57% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b465e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b465e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b465e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b465e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b465e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b465e8",
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
      "00b46a08",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b46a0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b46a10",
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

- 旧版 [`00b465e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b465e0.md#insn-00b465e0) · [`00b465e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b465e0.md#insn-00b465e4) · [`00b465e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b465e0.md#insn-00b465e8)

~~~diff
- 00b465e0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b465e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b465e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b465e0 bytes f50f1df8
- 00b465e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b465e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b465e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b465e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b465e4 bytes f44f01a9
- 00b465e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b465e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b465e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b465e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b465e8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8679e5fdcddca6d05c597ae48e7b6f21"></a>

### [`00b4667c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4667c.md) → [`00b46aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46aa4.md) _ZN8firebase4util18file_output_stream12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 40.00% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b466b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46b30",
      "incomplete_value": true,
      "site": "00b46b30",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46708",
      "incomplete_value": true,
      "site": "00b46708",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46ae0"
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
      "00b46ab8",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46ac4",
      "READ",
      [
        "storage",
        "01125358",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b466b8",
      "WRITE",
      [
        "storage",
        "01125358",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46ab8",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46ac4",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46ae0",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4667c.md#insn-00b46694) · [`00b466b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4667c.md#insn-00b466b8) · [`00b466d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4667c.md#insn-00b466d0)
- 新版 [`00b46abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46aa4.md#insn-00b46abc)

~~~diff
- 00b46694 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b46694 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b46abc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b46abc ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b46694 bytes c10300b4
+ 00b46abc bytes c10300b4
- 00b466b8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b466b8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b466b8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:358:8"]]
- 00b466b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b466b8 bytes bf620d39
- 00b466d0 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b466d0 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5af860d21f0f2f4a7eda84059a41ef09"></a>

### [`00b4671c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4671c.md) → [`00b46b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46b44.md) _ZN8firebase4util18file_output_stream14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46b84",
      "incomplete_value": true,
      "site": "00b46b84",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4675c",
      "incomplete_value": true,
      "site": "00b4675c",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46b60",
      "incomplete_value": true,
      "site": "00b46b60",
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
      "definition_site": "00b46738",
      "incomplete_value": true,
      "site": "00b46738",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46b68",
      "incomplete_value": false,
      "site": "00b46b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:534:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46740",
      "incomplete_value": false,
      "site": "00b46754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4f4:8"
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
      "00b46b58",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46b68",
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ],
    [
      "00b46b84",
      "WRITE",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46b58",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46b68",
      "PARAM",
      [
        "storage",
        "002b0534",
        null,
        "string"
      ]
    ],
    [
      "00b46b84",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4671c.md#insn-00b46754) · [`00b4675c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4671c.md#insn-00b4675c) · [`00b46730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4671c.md#insn-00b46730)
- 新版 [`00b46b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46b44.md#insn-00b46b7c) · [`00b46b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46b44.md#insn-00b46b84) · [`00b46b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46b44.md#insn-00b46b58)

~~~diff
- 00b46754 ["INT_ADD", "register:40f0:8", ["const:b46754:8", "const:4:8"]]
- 00b46754 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b46b7c ["INT_ADD", "register:40f0:8", ["const:b46b7c:8", "const:4:8"]]
+ 00b46b7c ["CALL", null, ["callee:00c5af10:8"]]
- 00b46754 bytes ef500494
+ 00b46b7c bytes e5500494
- 00b4675c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00b4675c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46b84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
+ 00b46b84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4675c bytes 80aa01f9
+ 00b46b84 bytes 80aa03f9
- 00b46730 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00b46730 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46b58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
+ 00b46b58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46730 bytes 81aa41f9
+ 00b46b58 bytes 81aa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd07957ece537872fb7229aba2b66b96"></a>

### [`00b467c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b467c8.md) → [`00b46bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46bf0.md) _ZN8firebase4util18file_output_stream13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46808"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46c30"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b467e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b467dc",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b467e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46c34"
      ]
    ],
    [
      "unmatched:00b467ec",
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46c04",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46c0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46c34"
      ]
    ],
    [
      "00b46c14",
      "PARAM",
      [
        "storage",
        "002b0534",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b467e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b467c8.md#insn-00b467e4) · [`00b46800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b467c8.md#insn-00b46800) · [`00b46808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b467c8.md#insn-00b46808)
- 新版 [`00b46c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46bf0.md#insn-00b46c28)

~~~diff
- 00b467e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b467e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b467e4 bytes 410100b5
- 00b46800 ["INT_ADD", "register:40f0:8", ["const:b46800:8", "const:4:8"]]
- 00b46800 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b46c28 ["INT_ADD", "register:40f0:8", ["const:b46c28:8", "const:4:8"]]
+ 00b46c28 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46800 bytes c4500494
+ 00b46c28 bytes ba500494
- 00b46808 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00b46808 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46808 bytes 80aa01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc65fdb2e6968221ab9cabfbc9d14ddc"></a>

### [`00b46838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46838.md) → [`00b46c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46c60.md) _ZN8firebase4util18file_output_stream10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46c7c",
      "incomplete_value": false,
      "site": "00b46c80",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46854",
      "incomplete_value": false,
      "site": "00b46858",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b46c8c",
      "incomplete_value": true,
      "site": "00b46c98",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46864",
      "incomplete_value": true,
      "site": "00b46870",
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
              "INT_LEFT"
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
      "00b46c7c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b46c8c",
      "DATA",
      [
        "storage",
        "01125378",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b46c7c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b46c8c",
      "DATA",
      [
        "storage",
        "01125778",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46838.md#insn-00b46858) · [`00b46854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46838.md#insn-00b46854) · [`00b46860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46838.md#insn-00b46860)
- 新版 [`00b46c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46c60.md#insn-00b46c80) · [`00b46c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46c60.md#insn-00b46c7c) · [`00b46c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46c60.md#insn-00b46c88)

~~~diff
- 00b46858 ["INT_ADD", "register:40f0:8", ["const:b46858:8", "const:4:8"]]
- 00b46858 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b46c80 ["INT_ADD", "register:40f0:8", ["const:b46c80:8", "const:4:8"]]
+ 00b46c80 ["CALL", null, ["callee:00c5b000:8"]]
- 00b46858 bytes ea500494
+ 00b46c80 bytes e0500494
- 00b46854 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b46854 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46854 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46854 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46c7c ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b46c7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46c7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46c7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46854 bytes 00441191
+ 00b46c7c bytes 00781491
- 00b46860 ["COPY", "tmp:0:8", ["const:378:8"]]
- 00b46860 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b46860 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b46860 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b46c88 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00b46c88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b46c88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b46c88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b46860 bytes 08e10d91
+ 00b46c88 bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf03705274686c33b94979bee40397eb"></a>

### [`00b468b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b468b4.md) → [`00b46cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46cdc.md) _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46d08",
      "incomplete_value": true,
      "site": "00b46d08",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b468e0",
      "incomplete_value": true,
      "site": "00b468e0",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46cf0",
      "incomplete_value": true,
      "site": "00b46cf0",
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
      "definition_site": "00b468c8",
      "incomplete_value": true,
      "site": "00b468c8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46cf8",
      "incomplete_value": false,
      "site": "00b46d00",
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
            "const:a56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b468d0",
      "incomplete_value": false,
      "site": "00b468d8",
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
            "const:a16:8"
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
      "00b46cec",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46cf8",
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ],
    [
      "00b46d08",
      "WRITE",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46cec",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46cf8",
      "PARAM",
      [
        "storage",
        "002b8a56",
        null,
        "string"
      ]
    ],
    [
      "00b46d08",
      "WRITE",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b468d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b468b4.md#insn-00b468d8) · [`00b468e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b468b4.md#insn-00b468e0) · [`00b468c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b468b4.md#insn-00b468c4)
- 新版 [`00b46d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46cdc.md#insn-00b46d00) · [`00b46d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46cdc.md#insn-00b46d08) · [`00b46cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46cdc.md#insn-00b46cec)

~~~diff
- 00b468d8 ["INT_ADD", "register:40f0:8", ["const:b468d8:8", "const:4:8"]]
- 00b468d8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b46d00 ["INT_ADD", "register:40f0:8", ["const:b46d00:8", "const:4:8"]]
+ 00b46d00 ["CALL", null, ["callee:00c5af10:8"]]
- 00b468d8 bytes 8e500494
+ 00b46d00 bytes 84500494
- 00b468e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:380:8"]]
- 00b468e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46d08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b46d08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b468e0 bytes 60c201f9
+ 00b46d08 bytes 60c203f9
- 00b468c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:380:8"]]
- 00b468c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46cec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b46cec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b468c4 bytes 68c241f9
+ 00b46cec bytes 68c243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb115a6ffbbb9e2101ca33e30e21b5a9"></a>

### [`00b46938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46938.md) → [`00b46d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46d60.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46968"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46d90"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46d74",
      "incomplete_value": true,
      "site": "00b46d74",
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
      "definition_site": "00b4694c",
      "incomplete_value": true,
      "site": "00b4694c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46d70",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46d74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4696c"
      ]
    ],
    [
      "unmatched:00b46954",
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46d70",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46d74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46d94"
      ]
    ],
    [
      "00b46d7c",
      "PARAM",
      [
        "storage",
        "002b8a56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46938.md#insn-00b46960) · [`00b46968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46938.md#insn-00b46968) · [`00b46978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46938.md#insn-00b46978)
- 新版 [`00b46d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46d60.md#insn-00b46d88)

~~~diff
- 00b46960 ["INT_ADD", "register:40f0:8", ["const:b46960:8", "const:4:8"]]
- 00b46960 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b46d88 ["INT_ADD", "register:40f0:8", ["const:b46d88:8", "const:4:8"]]
+ 00b46d88 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46960 bytes 6c500494
+ 00b46d88 bytes 62500494
- 00b46968 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:380:8"]]
- 00b46968 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46968 bytes 60c201f9
- 00b46978 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b46978 ["RETURN", null, ["register:0:8"]]
- 00b46978 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0830410e34b8f93af837210d36e418de"></a>

### [`00b46988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46988.md) → [`00b46db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46db0.md) _ZN8firebase4util16dex_class_loader15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46e38",
      "incomplete_value": true,
      "site": "00b46e38",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46a10",
      "incomplete_value": true,
      "site": "00b46a10",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46de4",
      "incomplete_value": true,
      "site": "00b46df0",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:780:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b469bc",
      "incomplete_value": true,
      "site": "00b469c8",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:380:8"
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
      "00b46dc4",
      "READ",
      [
        "storage",
        "01125388",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46de4",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46e38",
      "WRITE",
      [
        "storage",
        "01125388",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46dc4",
      "READ",
      [
        "storage",
        "01125788",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46de4",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46e38",
      "WRITE",
      [
        "storage",
        "01125788",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b469c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46988.md#insn-00b469c8) · [`00b46a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46988.md#insn-00b46a10) · [`00b4699c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46988.md#insn-00b4699c)
- 新版 [`00b46df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46db0.md#insn-00b46df0) · [`00b46e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46db0.md#insn-00b46e38) · [`00b46dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46db0.md#insn-00b46dc4)

~~~diff
- 00b469c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b469c8 ["INT_ADD", "register:40f0:8", ["const:b469c8:8", "const:4:8"]]
- 00b469c8 ["CALLIND", null, ["register:0:8"]]
+ 00b46df0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46df0 ["INT_ADD", "register:40f0:8", ["const:b46df0:8", "const:4:8"]]
+ 00b46df0 ["CALLIND", null, ["register:0:8"]]
- 00b469c8 bytes 00013fd6
+ 00b46df0 bytes 00013fd6
- 00b46a10 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b46a10 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:388:8"]]
- 00b46a10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b46e38 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b46e38 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:788:8"]]
+ 00b46e38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b46a10 bytes a0220e39
+ 00b46e38 bytes a0221e39
- 00b4699c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:388:8"]]
- 00b4699c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4699c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b46dc4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:788:8"]]
+ 00b46dc4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b46dc4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4699c bytes a8224e39
+ 00b46dc4 bytes a8225e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e31b35fac87fb2dd617e491d520b3168"></a>

### [`00b46a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46a24.md) → [`00b46e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46e4c.md) _ZN8firebase4util16dex_class_loader12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46e88",
      "incomplete_value": true,
      "site": "00b46e88",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46a60",
      "incomplete_value": true,
      "site": "00b46a60",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46ed8",
      "incomplete_value": true,
      "site": "00b46ed8",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46ab0",
      "incomplete_value": true,
      "site": "00b46ab0",
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
            "const:380:8"
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
      "definition_site": "00b46e64",
      "incomplete_value": true,
      "site": "00b46e64",
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
      "definition_site": "00b46a3c",
      "incomplete_value": true,
      "site": "00b46a3c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46e60",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46e6c",
      "READ",
      [
        "storage",
        "01125388",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46e88",
      "WRITE",
      [
        "storage",
        "01125388",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46e60",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46e6c",
      "READ",
      [
        "storage",
        "01125788",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46e88",
      "WRITE",
      [
        "storage",
        "01125788",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46a24.md#insn-00b46a60) · [`00b46aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46a24.md#insn-00b46aac) · [`00b46ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46a24.md#insn-00b46ab0)
- 新版 [`00b46e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46e4c.md#insn-00b46e88) · [`00b46ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46e4c.md#insn-00b46ed4) · [`00b46ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46e4c.md#insn-00b46ed8)

~~~diff
- 00b46a60 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b46a60 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b46a60 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:388:8"]]
- 00b46a60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b46e88 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b46e88 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b46e88 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:788:8"]]
+ 00b46e88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b46a60 bytes bf220e39
+ 00b46e88 bytes bf221e39
- 00b46aac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46aac ["INT_ADD", "register:40f0:8", ["const:b46aac:8", "const:4:8"]]
- 00b46aac ["CALLIND", null, ["register:0:8"]]
+ 00b46ed4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46ed4 ["INT_ADD", "register:40f0:8", ["const:b46ed4:8", "const:4:8"]]
+ 00b46ed4 ["CALLIND", null, ["register:0:8"]]
- 00b46aac bytes 00013fd6
+ 00b46ed4 bytes 00013fd6
- 00b46ab0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:380:8"]]
- 00b46ab0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b46ab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b46ed8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00b46ed8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b46ed8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b46ab0 bytes 9fc201f9
+ 00b46ed8 bytes 9fc203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a99123d6a1134fdf8e38fc5bbcc722d"></a>

### [`00b46ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ac4.md) → [`00b46eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46eec.md) _ZN8firebase4util16dex_class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46b04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46f2c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46ae0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b46ad8",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46ae0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46f30"
      ]
    ],
    [
      "unmatched:00b46ae8",
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46f00",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46f08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46f30"
      ]
    ],
    [
      "00b46f10",
      "PARAM",
      [
        "storage",
        "002b8a56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ac4.md#insn-00b46ae0) · [`00b46afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ac4.md#insn-00b46afc) · [`00b46b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ac4.md#insn-00b46b04)
- 新版 [`00b46f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46eec.md#insn-00b46f24)

~~~diff
- 00b46ae0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b46ae0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b46ae0 bytes 410100b5
- 00b46afc ["INT_ADD", "register:40f0:8", ["const:b46afc:8", "const:4:8"]]
- 00b46afc ["CALL", null, ["callee:00c5af10:8"]]
+ 00b46f24 ["INT_ADD", "register:40f0:8", ["const:b46f24:8", "const:4:8"]]
+ 00b46f24 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46afc bytes 05500494
+ 00b46f24 bytes fb4f0494
- 00b46b04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:380:8"]]
- 00b46b04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46b04 bytes 80c201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1197518b36093d1c26cad95ca6f9d0c"></a>

### [`00b46b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46b70.md) → [`00b46f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46f98.md) _ZN8firebase4util16dex_class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46bb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46fd8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46b8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b46b84",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46b8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46fdc"
      ]
    ],
    [
      "unmatched:00b46b94",
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46fac",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46fb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46fdc"
      ]
    ],
    [
      "00b46fbc",
      "PARAM",
      [
        "storage",
        "002b8a56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46b70.md#insn-00b46b8c) · [`00b46ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46b70.md#insn-00b46ba8) · [`00b46bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46b70.md#insn-00b46bb0)
- 新版 [`00b46fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46f98.md#insn-00b46fd0)

~~~diff
- 00b46b8c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b46b8c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b46b8c bytes 410100b5
- 00b46ba8 ["INT_ADD", "register:40f0:8", ["const:b46ba8:8", "const:4:8"]]
- 00b46ba8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b46fd0 ["INT_ADD", "register:40f0:8", ["const:b46fd0:8", "const:4:8"]]
+ 00b46fd0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46ba8 bytes da4f0494
+ 00b46fd0 bytes d04f0494
- 00b46bb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:380:8"]]
- 00b46bb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46bb0 bytes 80c201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84ebdcdb86abb852547a73583a345c8f"></a>

### [`00b46be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46be0.md) → [`00b47008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47008.md) _ZN8firebase4util16dex_class_loader10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47024",
      "incomplete_value": false,
      "site": "00b47028",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46bfc",
      "incomplete_value": false,
      "site": "00b46c00",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b47034",
      "incomplete_value": true,
      "site": "00b47040",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46c0c",
      "incomplete_value": true,
      "site": "00b46c18",
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
              "INT_LEFT"
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
      "00b47024",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b47034",
      "DATA",
      [
        "storage",
        "011253a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b47024",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b47034",
      "DATA",
      [
        "storage",
        "011257a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46be0.md#insn-00b46c00) · [`00b46bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46be0.md#insn-00b46bfc) · [`00b46c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46be0.md#insn-00b46c08)
- 新版 [`00b47028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47008.md#insn-00b47028) · [`00b47024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47008.md#insn-00b47024) · [`00b47030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47008.md#insn-00b47030)

~~~diff
- 00b46c00 ["INT_ADD", "register:40f0:8", ["const:b46c00:8", "const:4:8"]]
- 00b46c00 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b47028 ["INT_ADD", "register:40f0:8", ["const:b47028:8", "const:4:8"]]
+ 00b47028 ["CALL", null, ["callee:00c5b000:8"]]
- 00b46c00 bytes 00500494
+ 00b47028 bytes f64f0494
- 00b46bfc ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b46bfc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46bfc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46bfc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47024 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b47024 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47024 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47024 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46bfc bytes 00441191
+ 00b47024 bytes 00781491
- 00b46c08 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 00b46c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b46c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b46c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b47030 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 00b47030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b46c08 bytes 08810e91
+ 00b47030 bytes 08811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99f5cfa33c3a3b01cabf562149b32b48"></a>

### [`00b46c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c1c.md) → [`00b47044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47044.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46c48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47070"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47058",
      "incomplete_value": true,
      "site": "00b47058",
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
      "definition_site": "00b46c30",
      "incomplete_value": true,
      "site": "00b46c30",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47054",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46c3c",
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b46c40",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b47054",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47064",
      "PARAM",
      [
        "storage",
        "002b58bd",
        null,
        "string"
      ]
    ],
    [
      "00b47068",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c1c.md#insn-00b46c30) · [`00b46c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c1c.md#insn-00b46c40) · [`00b46c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c1c.md#insn-00b46c48)
- 新版 [`00b47058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47044.md#insn-00b47058)

~~~diff
- 00b46c30 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b46c30 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b47058 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b47058 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b46c30 bytes e80000b5
+ 00b47058 bytes e80000b5
- 00b46c40 ["INT_ADD", "register:40f0:8", ["const:b46c40:8", "const:4:8"]]
- 00b46c40 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46c40 bytes b44f0494
- 00b46c48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
- 00b46c48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46c48 bytes 60d601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07e4d2856b906e1a27019119e3fe7d57"></a>

### [`00b46c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c5c.md) → [`00b47084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47084.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46c88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b470b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47098",
      "incomplete_value": true,
      "site": "00b47098",
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
      "definition_site": "00b46c70",
      "incomplete_value": true,
      "site": "00b46c70",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47094",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46c78",
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b46c80",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b47094",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b470a0",
      "PARAM",
      [
        "storage",
        "002b58bd",
        null,
        "string"
      ]
    ],
    [
      "00b470a8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c5c.md#insn-00b46c70) · [`00b46c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c5c.md#insn-00b46c80) · [`00b46c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c5c.md#insn-00b46c88)
- 新版 [`00b47098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47084.md#insn-00b47098)

~~~diff
- 00b46c70 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b46c70 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b47098 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b47098 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b46c70 bytes e80000b5
+ 00b47098 bytes e80000b5
- 00b46c80 ["INT_ADD", "register:40f0:8", ["const:b46c80:8", "const:4:8"]]
- 00b46c80 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46c80 bytes a44f0494
- 00b46c88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
- 00b46c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46c88 bytes 60d601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a1507841b611e5c150b5772c02bb13f"></a>

### [`00b46c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c9c.md) → [`00b470c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b470c4.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46ccc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b470f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b470d8",
      "incomplete_value": true,
      "site": "00b470d8",
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
      "definition_site": "00b46cb0",
      "incomplete_value": true,
      "site": "00b46cb0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b470d4",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46cbc",
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b46cc4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b470d4",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b470e4",
      "PARAM",
      [
        "storage",
        "002b58bd",
        null,
        "string"
      ]
    ],
    [
      "00b470ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c9c.md#insn-00b46cb0) · [`00b46cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c9c.md#insn-00b46cc4) · [`00b46ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c9c.md#insn-00b46ccc)
- 新版 [`00b470d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b470c4.md#insn-00b470d8)

~~~diff
- 00b46cb0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b46cb0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b470d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b470d8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b46cb0 bytes 080100b5
+ 00b470d8 bytes 080100b5
- 00b46cc4 ["INT_ADD", "register:40f0:8", ["const:b46cc4:8", "const:4:8"]]
- 00b46cc4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46cc4 bytes 934f0494
- 00b46ccc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
- 00b46ccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46ccc bytes 60d601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a15709661b167246b3a8cb3bd6398d6"></a>

### [`00b46ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ce0.md) → [`00b47108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47108.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47138",
      "incomplete_value": true,
      "site": "00b47138",
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
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46d10",
      "incomplete_value": true,
      "site": "00b46d10",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4711c",
      "incomplete_value": true,
      "site": "00b4711c",
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
      "definition_site": "00b46cf4",
      "incomplete_value": true,
      "site": "00b46cf4",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47124",
      "incomplete_value": false,
      "site": "00b47130",
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
            "const:8bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46cfc",
      "incomplete_value": false,
      "site": "00b46d08",
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
            "const:87d:8"
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
      "00b47118",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47124",
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      "00b47138",
      "WRITE",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47118",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47124",
      "PARAM",
      [
        "storage",
        "002b58bd",
        null,
        "string"
      ]
    ],
    [
      "00b47138",
      "WRITE",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ce0.md#insn-00b46d08) · [`00b46d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ce0.md#insn-00b46d10) · [`00b46cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ce0.md#insn-00b46cf0)
- 新版 [`00b47130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47108.md#insn-00b47130) · [`00b47138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47108.md#insn-00b47138) · [`00b47118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47108.md#insn-00b47118)

~~~diff
- 00b46d08 ["INT_ADD", "register:40f0:8", ["const:b46d08:8", "const:4:8"]]
- 00b46d08 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47130 ["INT_ADD", "register:40f0:8", ["const:b47130:8", "const:4:8"]]
+ 00b47130 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46d08 bytes 824f0494
+ 00b47130 bytes 784f0494
- 00b46d10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
- 00b46d10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47138 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00b47138 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46d10 bytes 60d601f9
+ 00b47138 bytes 60d603f9
- 00b46cf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
- 00b46cf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00b47118 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46cf0 bytes 68d641f9
+ 00b47118 bytes 68d643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d566e25fc1e5f9d172521d54697b22a"></a>

### [`00b46d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46d30.md) → [`00b47158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47158.md) _ZN8firebase4util9resources15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b471e0",
      "incomplete_value": true,
      "site": "00b471e0",
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
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46db8",
      "incomplete_value": true,
      "site": "00b46db8",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4718c",
      "incomplete_value": true,
      "site": "00b47198",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:7a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46d64",
      "incomplete_value": true,
      "site": "00b46d70",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:3a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46dc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4716c",
      "READ",
      [
        "storage",
        "011253b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47178",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b46dbc"
      ]
    ],
    [
      "00b4718c",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4716c",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47178",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b471e4"
      ]
    ],
    [
      "00b4718c",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46d30.md#insn-00b46d70) · [`00b46db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46d30.md#insn-00b46db8) · [`00b46dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46d30.md#insn-00b46dc8)
- 新版 [`00b47198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47158.md#insn-00b47198) · [`00b471e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47158.md#insn-00b471e0)

~~~diff
- 00b46d70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46d70 ["INT_ADD", "register:40f0:8", ["const:b46d70:8", "const:4:8"]]
- 00b46d70 ["CALLIND", null, ["register:0:8"]]
+ 00b47198 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47198 ["INT_ADD", "register:40f0:8", ["const:b47198:8", "const:4:8"]]
+ 00b47198 ["CALLIND", null, ["register:0:8"]]
- 00b46d70 bytes 00013fd6
+ 00b47198 bytes 00013fd6
- 00b46db8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b46db8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3b0:8"]]
- 00b46db8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b471e0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b471e0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7b0:8"]]
+ 00b471e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b46db8 bytes a0c20e39
+ 00b471e0 bytes a0c21e39
- 00b46dc8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b46dc8 ["RETURN", null, ["register:0:8"]]
- 00b46dc8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bee9bb339ef8eeb1253f8a66d66a074"></a>

### [`00b46dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46dcc.md) → [`00b471f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b471f4.md) _ZN8firebase4util9resources12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47230",
      "incomplete_value": true,
      "site": "00b47230",
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
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46e08",
      "incomplete_value": true,
      "site": "00b46e08",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47280",
      "incomplete_value": true,
      "site": "00b47280",
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
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46e58",
      "incomplete_value": true,
      "site": "00b46e58",
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
            "const:3a8:8"
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
      "definition_site": "00b4720c",
      "incomplete_value": true,
      "site": "00b4720c",
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
      "definition_site": "00b46de4",
      "incomplete_value": true,
      "site": "00b46de4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47208",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47214",
      "READ",
      [
        "storage",
        "011253b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47230",
      "WRITE",
      [
        "storage",
        "011253b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47208",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47214",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47230",
      "WRITE",
      [
        "storage",
        "011257b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46dcc.md#insn-00b46e08) · [`00b46e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46dcc.md#insn-00b46e54) · [`00b46e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46dcc.md#insn-00b46e58)
- 新版 [`00b47230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b471f4.md#insn-00b47230) · [`00b4727c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b471f4.md#insn-00b4727c) · [`00b47280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b471f4.md#insn-00b47280)

~~~diff
- 00b46e08 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b46e08 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b46e08 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3b0:8"]]
- 00b46e08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b47230 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b47230 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b47230 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7b0:8"]]
+ 00b47230 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b46e08 bytes bfc20e39
+ 00b47230 bytes bfc21e39
- 00b46e54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46e54 ["INT_ADD", "register:40f0:8", ["const:b46e54:8", "const:4:8"]]
- 00b46e54 ["CALLIND", null, ["register:0:8"]]
+ 00b4727c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4727c ["INT_ADD", "register:40f0:8", ["const:b4727c:8", "const:4:8"]]
+ 00b4727c ["CALLIND", null, ["register:0:8"]]
- 00b46e54 bytes 00013fd6
+ 00b4727c bytes 00013fd6
- 00b46e58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3a8:8"]]
- 00b46e58 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b46e58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b47280 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
+ 00b47280 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b47280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b46e58 bytes 9fd601f9
+ 00b47280 bytes 9fd603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9327d495fe15e6da6a44fa397dddc527"></a>

### [`00b46e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46e6c.md) → [`00b47294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47294.md) _ZN8firebase4util9resources14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46e6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46e6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46e70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b46e6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b46e70",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b46e80",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47294",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b47298",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b472a8",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46e6c.md#insn-00b46e6c) · [`00b46e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46e6c.md#insn-00b46e70) · [`00b46e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46e6c.md#insn-00b46e88)

~~~diff
- 00b46e6c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b46e6c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b46e6c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b46e6c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b46e6c bytes f44fbea9
- 00b46e70 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b46e70 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b46e70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b46e70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b46e70 bytes fd7b01a9
- 00b46e88 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b46e88 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b46e88 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2b801fe445cefb659d2449b88f32dce"></a>

### [`00b46edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46edc.md) → [`00b47304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47304.md) _ZN8firebase4util9resources11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47320",
      "incomplete_value": false,
      "site": "00b47324",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46ef8",
      "incomplete_value": false,
      "site": "00b46efc",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b47330",
      "incomplete_value": true,
      "site": "00b4733c",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46f08",
      "incomplete_value": true,
      "site": "00b46f14",
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
              "INT_LEFT"
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
      "00b47320",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b47330",
      "DATA",
      [
        "storage",
        "011253b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47320",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b47330",
      "DATA",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46edc.md#insn-00b46efc) · [`00b46ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46edc.md#insn-00b46ef8) · [`00b46f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46edc.md#insn-00b46f04)
- 新版 [`00b47324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47304.md#insn-00b47324) · [`00b47320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47304.md#insn-00b47320) · [`00b4732c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47304.md#insn-00b4732c)

~~~diff
- 00b46efc ["INT_ADD", "register:40f0:8", ["const:b46efc:8", "const:4:8"]]
- 00b46efc ["CALL", null, ["callee:00c5b000:8"]]
+ 00b47324 ["INT_ADD", "register:40f0:8", ["const:b47324:8", "const:4:8"]]
+ 00b47324 ["CALL", null, ["callee:00c5b000:8"]]
- 00b46efc bytes 414f0494
+ 00b47324 bytes 374f0494
- 00b46ef8 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b46ef8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46ef8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46ef8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47320 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b47320 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47320 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47320 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46ef8 bytes 00680a91
+ 00b47320 bytes 009c0d91
- 00b46f04 ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 00b46f04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b46f04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b46f04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4732c ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 00b4732c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4732c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4732c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b46f04 bytes 08e10e91
+ 00b4732c bytes 08e11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9ce5fe1bd2a7713375409e0ac9744dd"></a>

### [`00b46f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f18.md) → [`00b47340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47340.md) _ZN8firebase4util9resources13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47380",
      "incomplete_value": true,
      "site": "00b47380",
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
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46f58",
      "incomplete_value": true,
      "site": "00b46f58",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4735c",
      "incomplete_value": true,
      "site": "00b4735c",
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
      "definition_site": "00b46f34",
      "incomplete_value": true,
      "site": "00b46f34",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47364",
      "incomplete_value": false,
      "site": "00b47378",
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
            "const:8bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46f3c",
      "incomplete_value": false,
      "site": "00b46f50",
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
            "const:87d:8"
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
      "00b47354",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47364",
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      "00b47380",
      "WRITE",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47354",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47364",
      "PARAM",
      [
        "storage",
        "002b58bd",
        null,
        "string"
      ]
    ],
    [
      "00b47380",
      "WRITE",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f18.md#insn-00b46f50) · [`00b46f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f18.md#insn-00b46f58) · [`00b46f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f18.md#insn-00b46f2c)
- 新版 [`00b47378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47340.md#insn-00b47378) · [`00b47380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47340.md#insn-00b47380) · [`00b47354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47340.md#insn-00b47354)

~~~diff
- 00b46f50 ["INT_ADD", "register:40f0:8", ["const:b46f50:8", "const:4:8"]]
- 00b46f50 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47378 ["INT_ADD", "register:40f0:8", ["const:b47378:8", "const:4:8"]]
+ 00b47378 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46f50 bytes f04e0494
+ 00b47378 bytes e64e0494
- 00b46f58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3a8:8"]]
- 00b46f58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47380 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
+ 00b47380 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46f58 bytes 80d601f9
+ 00b47380 bytes 80d603f9
- 00b46f2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3a8:8"]]
- 00b46f2c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47354 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
+ 00b47354 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46f2c bytes 81d641f9
+ 00b47354 bytes 81d643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca26204a01e5d066c4f1fde6488c1165"></a>

### [`00b46f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f88.md) → [`00b473b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473b0.md) _ZN8firebase4util9resources10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b473cc",
      "incomplete_value": false,
      "site": "00b473d0",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46fa4",
      "incomplete_value": false,
      "site": "00b46fa8",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b473dc",
      "incomplete_value": true,
      "site": "00b473e8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46fb4",
      "incomplete_value": true,
      "site": "00b46fc0",
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
              "INT_LEFT"
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
      "00b473cc",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b473dc",
      "DATA",
      [
        "storage",
        "011253c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b473cc",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b473dc",
      "DATA",
      [
        "storage",
        "011257c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f88.md#insn-00b46fa8) · [`00b46fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f88.md#insn-00b46fa4) · [`00b46fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f88.md#insn-00b46fb0)
- 新版 [`00b473d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473b0.md#insn-00b473d0) · [`00b473cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473b0.md#insn-00b473cc) · [`00b473d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473b0.md#insn-00b473d8)

~~~diff
- 00b46fa8 ["INT_ADD", "register:40f0:8", ["const:b46fa8:8", "const:4:8"]]
- 00b46fa8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b473d0 ["INT_ADD", "register:40f0:8", ["const:b473d0:8", "const:4:8"]]
+ 00b473d0 ["CALL", null, ["callee:00c5b000:8"]]
- 00b46fa8 bytes 164f0494
+ 00b473d0 bytes 0c4f0494
- 00b46fa4 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b46fa4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46fa4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46fa4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b473cc ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b473cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b473cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b473cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46fa4 bytes 00441191
+ 00b473cc bytes 00781491
- 00b46fb0 ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 00b46fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b46fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b46fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b473d8 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 00b473d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b473d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b473d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b46fb0 bytes 08010f91
+ 00b473d8 bytes 08011f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e55002e7789f2d1346f94411f237e02"></a>

### [`00b46fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46fc4.md) → [`00b473ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473ec.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47418",
      "incomplete_value": true,
      "site": "00b47418",
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
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46ff0",
      "incomplete_value": true,
      "site": "00b46ff0",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47400",
      "incomplete_value": true,
      "site": "00b47400",
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
      "definition_site": "00b46fd8",
      "incomplete_value": true,
      "site": "00b46fd8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4740c",
      "incomplete_value": false,
      "site": "00b47410",
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
            "const:5d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46fe4",
      "incomplete_value": false,
      "site": "00b46fe8",
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
            "const:591:8"
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
      "00b473fc",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4740c",
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      "00b47418",
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b473fc",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4740c",
      "PARAM",
      [
        "storage",
        "002be5d1",
        null,
        "string"
      ]
    ],
    [
      "00b47418",
      "WRITE",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46fc4.md#insn-00b46fe8) · [`00b46ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46fc4.md#insn-00b46ff0) · [`00b46fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46fc4.md#insn-00b46fd4)
- 新版 [`00b47410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473ec.md#insn-00b47410) · [`00b47418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473ec.md#insn-00b47418) · [`00b473fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473ec.md#insn-00b473fc)

~~~diff
- 00b46fe8 ["INT_ADD", "register:40f0:8", ["const:b46fe8:8", "const:4:8"]]
- 00b46fe8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47410 ["INT_ADD", "register:40f0:8", ["const:b47410:8", "const:4:8"]]
+ 00b47410 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46fe8 bytes ca4e0494
+ 00b47410 bytes c04e0494
- 00b46ff0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b46ff0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47418 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
+ 00b47418 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46ff0 bytes 60e601f9
+ 00b47418 bytes 60e603f9
- 00b46fd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b46fd4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b473fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
+ 00b473fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46fd4 bytes 68e641f9
+ 00b473fc bytes 68e643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-914cbacd66f9f5226ae667dee9c949a7"></a>

### [`00b47004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47004.md) → [`00b4742c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4742c.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47458",
      "incomplete_value": true,
      "site": "00b47458",
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
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47030",
      "incomplete_value": true,
      "site": "00b47030",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47440",
      "incomplete_value": true,
      "site": "00b47440",
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
      "definition_site": "00b47018",
      "incomplete_value": true,
      "site": "00b47018",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47448",
      "incomplete_value": false,
      "site": "00b47450",
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
            "const:5d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47020",
      "incomplete_value": false,
      "site": "00b47028",
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
            "const:591:8"
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
      "00b4743c",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47448",
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      "00b47458",
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4743c",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47448",
      "PARAM",
      [
        "storage",
        "002be5d1",
        null,
        "string"
      ]
    ],
    [
      "00b47458",
      "WRITE",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47004.md#insn-00b47028) · [`00b47030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47004.md#insn-00b47030) · [`00b47014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47004.md#insn-00b47014)
- 新版 [`00b47450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4742c.md#insn-00b47450) · [`00b47458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4742c.md#insn-00b47458) · [`00b4743c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4742c.md#insn-00b4743c)

~~~diff
- 00b47028 ["INT_ADD", "register:40f0:8", ["const:b47028:8", "const:4:8"]]
- 00b47028 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47450 ["INT_ADD", "register:40f0:8", ["const:b47450:8", "const:4:8"]]
+ 00b47450 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47028 bytes ba4e0494
+ 00b47450 bytes b04e0494
- 00b47030 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b47030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47458 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
+ 00b47458 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47030 bytes 60e601f9
+ 00b47458 bytes 60e603f9
- 00b47014 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b47014 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4743c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
+ 00b4743c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47014 bytes 68e641f9
+ 00b4743c bytes 68e643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6b82cf4419674208ebb833c542d4e79"></a>

### [`00b47044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47044.md) → [`00b4746c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4746c.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4749c",
      "incomplete_value": true,
      "site": "00b4749c",
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
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47074",
      "incomplete_value": true,
      "site": "00b47074",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47480",
      "incomplete_value": true,
      "site": "00b47480",
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
      "definition_site": "00b47058",
      "incomplete_value": true,
      "site": "00b47058",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4748c",
      "incomplete_value": false,
      "site": "00b47494",
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
            "const:5d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47064",
      "incomplete_value": false,
      "site": "00b4706c",
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
            "const:591:8"
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
      "00b4747c",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4748c",
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      "00b4749c",
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4747c",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4748c",
      "PARAM",
      [
        "storage",
        "002be5d1",
        null,
        "string"
      ]
    ],
    [
      "00b4749c",
      "WRITE",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4706c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47044.md#insn-00b4706c) · [`00b47074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47044.md#insn-00b47074) · [`00b47054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47044.md#insn-00b47054)
- 新版 [`00b47494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4746c.md#insn-00b47494) · [`00b4749c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4746c.md#insn-00b4749c) · [`00b4747c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4746c.md#insn-00b4747c)

~~~diff
- 00b4706c ["INT_ADD", "register:40f0:8", ["const:b4706c:8", "const:4:8"]]
- 00b4706c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47494 ["INT_ADD", "register:40f0:8", ["const:b47494:8", "const:4:8"]]
+ 00b47494 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4706c bytes a94e0494
+ 00b47494 bytes 9f4e0494
- 00b47074 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b47074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4749c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
+ 00b4749c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47074 bytes 60e601f9
+ 00b4749c bytes 60e603f9
- 00b47054 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b47054 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4747c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
+ 00b4747c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47054 bytes 68e641f9
+ 00b4747c bytes 68e643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afcce3b999884007c5590804c2254fc3"></a>

### [`00b47088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47088.md) → [`00b474b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b474b0.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b474e0",
      "incomplete_value": true,
      "site": "00b474e0",
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
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b470b8",
      "incomplete_value": true,
      "site": "00b470b8",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b474c4",
      "incomplete_value": true,
      "site": "00b474c4",
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
      "definition_site": "00b4709c",
      "incomplete_value": true,
      "site": "00b4709c",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b474cc",
      "incomplete_value": false,
      "site": "00b474d8",
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
            "const:5d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b470a4",
      "incomplete_value": false,
      "site": "00b470b0",
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
            "const:591:8"
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
      "00b474c0",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b474cc",
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      "00b474e0",
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b474c0",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b474cc",
      "PARAM",
      [
        "storage",
        "002be5d1",
        null,
        "string"
      ]
    ],
    [
      "00b474e0",
      "WRITE",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b470b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47088.md#insn-00b470b0) · [`00b470b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47088.md#insn-00b470b8) · [`00b47098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47088.md#insn-00b47098)
- 新版 [`00b474d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b474b0.md#insn-00b474d8) · [`00b474e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b474b0.md#insn-00b474e0) · [`00b474c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b474b0.md#insn-00b474c0)

~~~diff
- 00b470b0 ["INT_ADD", "register:40f0:8", ["const:b470b0:8", "const:4:8"]]
- 00b470b0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b474d8 ["INT_ADD", "register:40f0:8", ["const:b474d8:8", "const:4:8"]]
+ 00b474d8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b470b0 bytes 984e0494
+ 00b474d8 bytes 8e4e0494
- 00b470b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b470b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b474e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
+ 00b474e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b470b8 bytes 60e601f9
+ 00b474e0 bytes 60e603f9
- 00b47098 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b47098 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b474c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
+ 00b474c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47098 bytes 68e641f9
+ 00b474c0 bytes 68e643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27160e71b55058b46fdfd560a9460f42"></a>

### [`00b470d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b470d8.md) → [`00b47500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47500.md) _ZN8firebase4util8activity15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47588",
      "incomplete_value": true,
      "site": "00b47588",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47160",
      "incomplete_value": true,
      "site": "00b47160",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47534",
      "incomplete_value": true,
      "site": "00b47540",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:7c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4710c",
      "incomplete_value": true,
      "site": "00b47118",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:3c8:8"
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
      "00b47514",
      "READ",
      [
        "storage",
        "011253d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47534",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47588",
      "WRITE",
      [
        "storage",
        "011253d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47514",
      "READ",
      [
        "storage",
        "011257d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47534",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47588",
      "WRITE",
      [
        "storage",
        "011257d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b470d8.md#insn-00b47118) · [`00b47160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b470d8.md#insn-00b47160) · [`00b470ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b470d8.md#insn-00b470ec)
- 新版 [`00b47540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47500.md#insn-00b47540) · [`00b47588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47500.md#insn-00b47588) · [`00b47514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47500.md#insn-00b47514)

~~~diff
- 00b47118 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47118 ["INT_ADD", "register:40f0:8", ["const:b47118:8", "const:4:8"]]
- 00b47118 ["CALLIND", null, ["register:0:8"]]
+ 00b47540 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47540 ["INT_ADD", "register:40f0:8", ["const:b47540:8", "const:4:8"]]
+ 00b47540 ["CALLIND", null, ["register:0:8"]]
- 00b47118 bytes 00013fd6
+ 00b47540 bytes 00013fd6
- 00b47160 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b47160 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3d0:8"]]
- 00b47160 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b47588 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b47588 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7d0:8"]]
+ 00b47588 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b47160 bytes a0420f39
+ 00b47588 bytes a0421f39
- 00b470ec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3d0:8"]]
- 00b470ec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b470ec ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b47514 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7d0:8"]]
+ 00b47514 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b47514 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b470ec bytes a8424f39
+ 00b47514 bytes a8425f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

