# v16.0.0 → v16.0.1 · 最優先の変更候補 (74)

[一覧の目次](README.md)

<a id="compare-8713dcd30f6ff45aacf1fbb7af878fad"></a>

### [`00b52288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52288.md) → [`00b526b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b526b0.md) FUN_00b526b0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b52284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52284.md) [`00b5258c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b5258c.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4f0.md)
- 新版 呼出元 2件 [`00b526ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b526ac.md) [`00b529b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b529b4.md) · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.08% / 新版 88.08%

CFGの説明率　旧版 66.67% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b524b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b528e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b526f0",
      "incomplete_value": true,
      "site": "00b526f8",
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
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b522c8",
      "incomplete_value": true,
      "site": "00b522d0",
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
                "const:858:8"
              ]
            ]
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
      "00b526f0",
      "READ",
      [
        "storage",
        "01125858",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5273c",
      "READ",
      [
        "storage",
        "01125898",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5278c",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b526f0",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5273c",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5278c",
      "READ",
      [
        "storage",
        "01125bc8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b522d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52288.md#insn-00b522d0) · [`00b52320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52288.md#insn-00b52320) · [`00b52374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52288.md#insn-00b52374)
- 新版 `00b526f8`（命令位置の公開資料なし） · `00b52748`（命令位置の公開資料なし） · `00b5279c`（命令位置の公開資料なし）

~~~diff
- 00b522d0 ["INT_ADD", "register:40f0:8", ["const:b522d0:8", "const:4:8"]]
- 00b522d0 ["CALL", null, ["callee:00497834:8"]]
+ 00b526f8 ["INT_ADD", "register:40f0:8", ["const:b526f8:8", "const:4:8"]]
+ 00b526f8 ["CALL", null, ["callee:00497834:8"]]
- 00b522d0 bytes 4915e597
+ 00b526f8 bytes 4f14e597
- 00b52320 ["INT_ADD", "register:40f0:8", ["const:b52320:8", "const:4:8"]]
- 00b52320 ["CALL", null, ["callee:00497834:8"]]
+ 00b52748 ["INT_ADD", "register:40f0:8", ["const:b52748:8", "const:4:8"]]
+ 00b52748 ["CALL", null, ["callee:00497834:8"]]
- 00b52320 bytes 3515e597
+ 00b52748 bytes 3b14e597
- 00b52374 ["INT_ADD", "register:40f0:8", ["const:b52374:8", "const:4:8"]]
- 00b52374 ["CALL", null, ["callee:00497a48:8"]]
+ 00b5279c ["INT_ADD", "register:40f0:8", ["const:b5279c:8", "const:4:8"]]
+ 00b5279c ["CALL", null, ["callee:00497a48:8"]]
- 00b52374 bytes a515e597
+ 00b5279c bytes ab14e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ca0a68619f70d8dea5108ad7d446560"></a>

### [`00b5258c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b5258c.md) → [`00b529b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b529b4.md) _ZN8firebase4util19JavaObjectToVariantEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b010.md) · 呼出先 19件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md)
- 新版 呼出元 1件 [`00c5b410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b410.md) · 呼出先 19件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.09% / 新版 90.09%

CFGの説明率　旧版 76.47% / 新版 69.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52a68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b52e90"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52a60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b529ec",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52a48",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52a68",
      "READ",
      [
        "storage",
        "01125630",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b529ec",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52a48",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52a68",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b525d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b5258c.md#insn-00b525d4) · [`00b52630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b5258c.md#insn-00b52630) · [`00b52640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b5258c.md#insn-00b52640)
- 新版 `00b529fc`（命令位置の公開資料なし） · `00b52a58`（命令位置の公開資料なし） · `00b52a68`（命令位置の公開資料なし）

~~~diff
- 00b525d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b525d4 ["INT_ADD", "register:40f0:8", ["const:b525d4:8", "const:4:8"]]
- 00b525d4 ["CALLIND", null, ["register:0:8"]]
+ 00b529fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b529fc ["INT_ADD", "register:40f0:8", ["const:b529fc:8", "const:4:8"]]
+ 00b529fc ["CALLIND", null, ["register:0:8"]]
- 00b525d4 bytes 00013fd6
+ 00b529fc bytes 00013fd6
- 00b52630 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b52630 ["INT_ADD", "register:40f0:8", ["const:b52630:8", "const:4:8"]]
- 00b52630 ["CALLIND", null, ["register:0:8"]]
+ 00b52a58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b52a58 ["INT_ADD", "register:40f0:8", ["const:b52a58:8", "const:4:8"]]
+ 00b52a58 ["CALLIND", null, ["register:0:8"]]
- 00b52630 bytes 00013fd6
+ 00b52a58 bytes 00013fd6
- 00b52640 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:630:8"]]
- 00b52640 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52a68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a30:8"]]
+ 00b52a68 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52640 bytes 021943f9
+ 00b52a68 bytes 021945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfaa07f9e0bcd7730143779d09f6c28c"></a>

### [`00b52ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52ca4.md) → [`00b530cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b530cc.md) _ZN8firebase4util24JavaSetToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b0d0.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5b4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b4d0.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 61.88% / 新版 61.88%

CFGの説明率　旧版 16.98% / 新版 11.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52ca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52ca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52cac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b52ca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b52cac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b52cb0",
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
      "00b530d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b530d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b530d8",
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

- 旧版 [`00b52ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52ca4.md#insn-00b52ca8) · [`00b52cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52ca4.md#insn-00b52cac) · [`00b52cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52ca4.md#insn-00b52cb0)

~~~diff
- 00b52ca8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b52ca8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b52ca8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b52ca8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b52ca8 bytes fc6f03a9
- 00b52cac ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b52cac ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b52cac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b52cac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b52cac bytes fa6704a9
- 00b52cb0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b52cb0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b52cb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b52cb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b52cb0 bytes f85f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1413385c95f9106e67f1000fb03aa96d"></a>

### [`00b53040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53040.md) → [`00b53468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53468.md) _ZN8firebase4util25JavaListToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_IS

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7b0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5abb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.88% / 新版 72.88%

CFGの説明率　旧版 3.92% / 新版 4.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53044"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53044"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53048"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53044",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53048",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5304c",
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
      "00b5346c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b53470",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b53474",
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

- 旧版 [`00b53044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53040.md#insn-00b53044) · [`00b53048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53040.md#insn-00b53048) · [`00b5304c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53040.md#insn-00b5304c)

~~~diff
- 00b53044 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b53044 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b53044 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b53044 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53044 bytes fa6702a9
- 00b53048 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b53048 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b53048 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b53048 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53048 bytes f85f03a9
- 00b5304c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5304c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5304c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5304c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5304c bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fa8cb52ceaa03281c37e798cf1cd0d6"></a>

### [`00b53328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53328.md) → [`00b53750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53750.md) _ZN8firebase4util31JavaObjectListToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7b0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5abb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 65.10% / 新版 65.10%

CFGの説明率　旧版 24.39% / 新版 20.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5332c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5332c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53330"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5332c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53330",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53334",
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
      "00b53754",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b53758",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5375c",
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

- 旧版 [`00b5332c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53328.md#insn-00b5332c) · [`00b53330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53328.md#insn-00b53330) · [`00b53334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53328.md#insn-00b53334)

~~~diff
- 00b5332c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b5332c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b5332c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5332c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5332c bytes fc6f02a9
- 00b53330 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b53330 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b53330 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b53330 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53330 bytes fa6703a9
- 00b53334 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b53334 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b53334 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b53334 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53334 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbe86069a038686e6725064b6c42c36b"></a>

### [`00b5357c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b5357c.md) → [`00b539a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b539a4.md) _ZN8firebase4util17JniObjectToStringEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md) [`00c5b5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5c0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.55% / 新版 79.55%

CFGの説明率　旧版 16.67% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5357c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53580"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53580"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5357c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53580",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53584",
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
      "00b539a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b539a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b539ac",
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

- 旧版 [`00b5357c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b5357c.md#insn-00b5357c) · [`00b53580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b5357c.md#insn-00b53580) · [`00b53584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b5357c.md#insn-00b53584)

~~~diff
- 00b5357c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5357c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5357c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5357c bytes f50f1df8
- 00b53580 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b53580 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b53580 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b53580 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53580 bytes f44f01a9
- 00b53584 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b53584 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b53584 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b53584 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53584 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-531b5a54e818cd6086b9f5784fc75773"></a>

### [`00b5362c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b5362c.md) → [`00b53a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53a54.md) _ZN8firebase4util21JavaListToVariantListEP7_JNIEnvPNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEEP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b0a0.md) · 呼出先 8件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)
- 新版 呼出元 1件 [`00c5b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b4a0.md) · 呼出先 8件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.17% / 新版 71.17%

CFGの説明率　旧版 5.71% / 新版 8.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53630"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53634"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53634"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53630",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53634",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53638",
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
      "00b53a58",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b53a5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b53a60",
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

- 旧版 [`00b53630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b5362c.md#insn-00b53630) · [`00b53634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b5362c.md#insn-00b53634) · [`00b53638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b5362c.md#insn-00b53638)

~~~diff
- 00b53630 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b53630 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b53630 bytes fb1300f9
- 00b53634 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b53634 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b53634 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b53634 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53634 bytes fa6703a9
- 00b53638 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b53638 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b53638 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b53638 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53638 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c68bf2cbd5ecb1617829cd615d0778a3"></a>

### [`00b537e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b537e8.md) → [`00b53c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53c10.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE7reserveEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b230.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b630.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 84.51% / 新版 84.51%

CFGの説明率　旧版 26.32% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53830"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b538b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b538cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53830",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53d28"
      ]
    ],
    [
      "unmatched:00b538b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53cf8"
      ]
    ],
    [
      "unmatched:00b538cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53ce0"
      ]
    ]
  ],
  "added": [
    [
      "00b53c58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53d28"
      ]
    ],
    [
      "00b53cdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53cf8"
      ]
    ],
    [
      "00b53cf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53ce0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b537e8.md#insn-00b53830) · [`00b53848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b537e8.md#insn-00b53848) · [`00b538b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b537e8.md#insn-00b538b4)
- 新版 `00b53c70`（命令位置の公開資料なし）

~~~diff
- 00b53830 ["CBRANCH", null, ["local:b14:8", "register:102:1"]]
- 00b53830 bytes 82060054
- 00b53848 ["INT_ADD", "register:40f0:8", ["const:b53848:8", "const:4:8"]]
- 00b53848 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b53c70 ["INT_ADD", "register:40f0:8", ["const:b53c70:8", "const:4:8"]]
+ 00b53c70 ["CALL", null, ["callee:00c57e90:8"]]
- 00b53848 bytes 92100494
+ 00b53c70 bytes 88100494
- 00b538b4 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00b538b4 bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7243b4961133e66329f239a524dc2a70"></a>

### [`00b53998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53998.md) → [`00b53dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53dc0.md) _ZN8firebase4util8IsJArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.05% / 新版 78.05%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53998"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5399c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5399c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53998",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5399c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b539a0",
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
      "00b53dc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b53dc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b53dc8",
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

- 旧版 [`00b53998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53998.md#insn-00b53998) · [`00b5399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53998.md#insn-00b5399c) · [`00b539a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53998.md#insn-00b539a0)

~~~diff
- 00b53998 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b53998 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b53998 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b53998 bytes f50f1df8
- 00b5399c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5399c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5399c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5399c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5399c bytes f44f01a9
- 00b539a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b539a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b539a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b539a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b539a0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84f87ef70f28cf641e6f854970b7802d"></a>

### [`00b53a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53a3c.md) → [`00b53e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53e64.md) _ZN8firebase4util16JObjectClassNameEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 20.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53a5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53e90",
      "incomplete_value": true,
      "site": "00b53e98",
      "value": [
        "live",
        "register:4000:8"
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
      "definition_site": "00b53e8c",
      "incomplete_value": true,
      "site": "00b53e98",
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
                "const:970:8"
              ]
            ]
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b53e8c",
      "READ",
      [
        "storage",
        "01125570",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53a5c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b53e8c",
      "READ",
      [
        "storage",
        "01125970",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53e84",
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

- 旧版 [`00b53a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53a3c.md#insn-00b53a5c) · [`00b53a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53a3c.md#insn-00b53a70)
- 新版 `00b53e98`（命令位置の公開資料なし） · `00b53e84`（命令位置の公開資料なし）

~~~diff
- 00b53a5c ["COPY", "register:0:8", ["register:4048:8"]]
- 00b53a5c ["INT_ADD", "register:40f0:8", ["const:b53a5c:8", "const:4:8"]]
- 00b53a5c ["CALLIND", null, ["register:0:8"]]
- 00b53a5c bytes 20013fd6
- 00b53a70 ["INT_ADD", "register:40f0:8", ["const:b53a70:8", "const:4:8"]]
- 00b53a70 ["CALL", null, ["callee:00497834:8"]]
+ 00b53e98 ["INT_ADD", "register:40f0:8", ["const:b53e98:8", "const:4:8"]]
+ 00b53e98 ["CALL", null, ["callee:00497834:8"]]
- 00b53a70 bytes 610fe597
+ 00b53e98 bytes 670ee597
+ 00b53e84 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b53e84 ["INT_ADD", "register:40f0:8", ["const:b53e84:8", "const:4:8"]]
+ 00b53e84 ["CALLIND", null, ["register:0:8"]]
+ 00b53e84 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5273cc33b35fcc2bf6a253f0d3fc1add"></a>

### [`00b53ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53ae0.md) → [`00b53f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53f08.md) _ZN8firebase4util14JBooleanToBoolEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aee0.md) · 呼出先 1件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md)
- 新版 呼出元 1件 [`00c5b2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b2e0.md) · 呼出先 1件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 59.26% / 新版 59.26%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53ae0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53ae0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53ae4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53ae0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53ae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b53f18",
      "READ",
      [
        "storage",
        "01125498",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53f08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b53f0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b53f18",
      "READ",
      [
        "storage",
        "01125898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53ae0.md#insn-00b53ae0) · [`00b53ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53ae0.md#insn-00b53ae4) · [`00b53af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53ae0.md#insn-00b53af8)
- 新版 `00b53f20`（命令位置の公開資料なし）

~~~diff
- 00b53ae0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b53ae0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b53ae0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b53ae0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b53ae0 bytes f44fbea9
- 00b53ae4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b53ae4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b53ae4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b53ae4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53ae4 bytes fd7b01a9
- 00b53af8 ["INT_ADD", "register:40f0:8", ["const:b53af8:8", "const:4:8"]]
- 00b53af8 ["CALL", null, ["callee:00497a48:8"]]
+ 00b53f20 ["INT_ADD", "register:40f0:8", ["const:b53f20:8", "const:4:8"]]
+ 00b53f20 ["CALL", null, ["callee:00497a48:8"]]
- 00b53af8 bytes c40fe597
+ 00b53f20 bytes ca0ee597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca1431e6c2a8c4f7aac88b750b515027"></a>

### [`00b53b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53b4c.md) → [`00b53f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53f74.md) _ZN8firebase4util12JByteToUInt8EP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ae00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b200.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53f84",
      "incomplete_value": true,
      "site": "00b53f8c",
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53b5c",
      "incomplete_value": true,
      "site": "00b53b64",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:520:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53ba0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b53fc8"
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
      "unmatched:00b53b5c",
      "READ",
      [
        "storage",
        "01125520",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53fa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53ba4"
      ]
    ],
    [
      "unmatched:00b53ba4",
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
      "00b53f84",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53fa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53fcc"
      ]
    ],
    [
      "00b53fcc",
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

- 旧版 [`00b53b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53b4c.md#insn-00b53b64) · [`00b53ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53b4c.md#insn-00b53ba0) · [`00b53bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53b4c.md#insn-00b53bb0)
- 新版 `00b53f8c`（命令位置の公開資料なし）

~~~diff
- 00b53b64 ["INT_ADD", "register:40f0:8", ["const:b53b64:8", "const:4:8"]]
- 00b53b64 ["CALL", null, ["callee:00c5b200:8"]]
+ 00b53f8c ["INT_ADD", "register:40f0:8", ["const:b53f8c:8", "const:4:8"]]
+ 00b53f8c ["CALL", null, ["callee:00c5b200:8"]]
- 00b53b64 bytes a71c0494
+ 00b53f8c bytes 9d1c0494
- 00b53ba0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53ba0 ["INT_ADD", "register:40f0:8", ["const:b53ba0:8", "const:4:8"]]
- 00b53ba0 ["CALLIND", null, ["register:0:8"]]
- 00b53ba0 bytes 00013fd6
- 00b53bb0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b53bb0 ["RETURN", null, ["register:0:8"]]
- 00b53bb0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c24101f8f4aeddb72d0b4ed6ba163ae1"></a>

### [`00b53c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53c50.md) → [`00b54078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54078.md) _ZN8firebase4util11JCharToCharEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ae10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54088",
      "incomplete_value": true,
      "site": "00b54090",
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
                "const:948:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53c60",
      "incomplete_value": true,
      "site": "00b53c68",
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
                "const:548:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53ca4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b540cc"
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
      "00b54088",
      "READ",
      [
        "storage",
        "01125548",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53ca4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54088",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "00b540cc",
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

- 旧版 [`00b53c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53c50.md#insn-00b53c68) · [`00b53ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53c50.md#insn-00b53ca4)
- 新版 `00b54090`（命令位置の公開資料なし） · `00b540cc`（命令位置の公開資料なし）

~~~diff
- 00b53c68 ["INT_ADD", "register:40f0:8", ["const:b53c68:8", "const:4:8"]]
- 00b53c68 ["CALL", null, ["callee:00c5b210:8"]]
+ 00b54090 ["INT_ADD", "register:40f0:8", ["const:b54090:8", "const:4:8"]]
+ 00b54090 ["CALL", null, ["callee:00c5b210:8"]]
- 00b53c68 bytes 6a1c0494
+ 00b54090 bytes 601c0494
- 00b53ca4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53ca4 ["INT_ADD", "register:40f0:8", ["const:b53ca4:8", "const:4:8"]]
- 00b53ca4 ["CALLIND", null, ["register:0:8"]]
- 00b53ca4 bytes 00013fd6
+ 00b540cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b540cc ["INT_ADD", "register:40f0:8", ["const:b540cc:8", "const:4:8"]]
+ 00b540cc ["CALLIND", null, ["register:0:8"]]
+ 00b540cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c38808950deb59dd8b6deb3eb3fcb8f"></a>

### [`00b53d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53d54.md) → [`00b5417c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b5417c.md) _ZN8firebase4util13JShortToInt16EP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ae20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b220.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53d88"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b541b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5418c",
      "incomplete_value": true,
      "site": "00b54194",
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53d64",
      "incomplete_value": true,
      "site": "00b53d6c",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:8c0:8"
              ]
            ]
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
      "unmatched:00b53d64",
      "READ",
      [
        "storage",
        "011258c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53d88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b541d4"
      ]
    ],
    [
      "unmatched:00b53d98",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5418c",
      "READ",
      [
        "storage",
        "01125cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b541b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b541d4"
      ]
    ],
    [
      "00b541c0",
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

- 旧版 [`00b53d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53d54.md#insn-00b53d6c) · [`00b53d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53d54.md#insn-00b53d88) · [`00b53d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53d54.md#insn-00b53d98)
- 新版 `00b54194`（命令位置の公開資料なし）

~~~diff
- 00b53d6c ["INT_ADD", "register:40f0:8", ["const:b53d6c:8", "const:4:8"]]
- 00b53d6c ["CALL", null, ["callee:00c5b220:8"]]
+ 00b54194 ["INT_ADD", "register:40f0:8", ["const:b54194:8", "const:4:8"]]
+ 00b54194 ["CALL", null, ["callee:00c5b220:8"]]
- 00b53d6c bytes 2d1c0494
+ 00b54194 bytes 231c0494
- 00b53d88 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b53d88 bytes 20010054
- 00b53d98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53d98 ["INT_ADD", "register:40f0:8", ["const:b53d98:8", "const:4:8"]]
- 00b53d98 ["CALLIND", null, ["register:0:8"]]
- 00b53d98 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4f53f997505ada26638b20057418e2d"></a>

### [`00b53ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53ec0.md) → [`00b542e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b542e8.md) _ZN8firebase4util12JLongToInt64EP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aad0.md) · 呼出先 1件 [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md)
- 新版 呼出元 1件 [`00c5aed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aed0.md) · 呼出先 1件 [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 16.67% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53ec0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53ec0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53ec4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53ec0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53ec4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b542f8",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b542e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b542ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b542f8",
      "READ",
      [
        "storage",
        "01125c28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53ec0.md#insn-00b53ec0) · [`00b53ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53ec0.md#insn-00b53ec4) · [`00b53ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53ec0.md#insn-00b53ed8)
- 新版 `00b54300`（命令位置の公開資料なし）

~~~diff
- 00b53ec0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b53ec0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b53ec0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b53ec0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b53ec0 bytes f44fbea9
- 00b53ec4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b53ec4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b53ec4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b53ec4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53ec4 bytes fd7b01a9
- 00b53ed8 ["INT_ADD", "register:40f0:8", ["const:b53ed8:8", "const:4:8"]]
- 00b53ed8 ["CALL", null, ["callee:0058f59c:8"]]
+ 00b54300 ["INT_ADD", "register:40f0:8", ["const:b54300:8", "const:4:8"]]
+ 00b54300 ["CALL", null, ["callee:0058f59c:8"]]
- 00b53ed8 bytes a1ede897
+ 00b54300 bytes a7ece897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df5011c636d89ce6293b2327b6353adf"></a>

### [`00b53f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53f28.md) → [`00b54350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54350.md) _ZN8firebase4util13JFloatToFloatEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54364",
      "incomplete_value": true,
      "site": "00b5436c",
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
                "const:b00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53f3c",
      "incomplete_value": true,
      "site": "00b53f44",
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
                "const:700:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53f58"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b54380"
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
      "00b54364",
      "READ",
      [
        "storage",
        "01125700",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53f58",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54364",
      "READ",
      [
        "storage",
        "01125b00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54380",
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

- 旧版 [`00b53f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53f28.md#insn-00b53f44) · [`00b53f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53f28.md#insn-00b53f58)
- 新版 `00b5436c`（命令位置の公開資料なし） · `00b54380`（命令位置の公開資料なし）

~~~diff
- 00b53f44 ["INT_ADD", "register:40f0:8", ["const:b53f44:8", "const:4:8"]]
- 00b53f44 ["CALL", null, ["callee:0057be0c:8"]]
+ 00b5436c ["INT_ADD", "register:40f0:8", ["const:b5436c:8", "const:4:8"]]
+ 00b5436c ["CALL", null, ["callee:0057be0c:8"]]
- 00b53f44 bytes a29fe897
+ 00b5436c bytes a89ee897
- 00b53f58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53f58 ["INT_ADD", "register:40f0:8", ["const:b53f58:8", "const:4:8"]]
- 00b53f58 ["CALLIND", null, ["register:0:8"]]
- 00b53f58 bytes 00013fd6
+ 00b54380 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b54380 ["INT_ADD", "register:40f0:8", ["const:b54380:8", "const:4:8"]]
+ 00b54380 ["CALLIND", null, ["register:0:8"]]
+ 00b54380 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7058fd48d33eea1bbb44f9f45ef517bc"></a>

### [`00b53f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53f98.md) → [`00b543c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b543c0.md) _ZN8firebase4util15JDoubleToDoubleEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b230.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b543d4",
      "incomplete_value": true,
      "site": "00b543dc",
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
                "const:a58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53fac",
      "incomplete_value": true,
      "site": "00b53fb4",
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
                "const:658:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53fc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53fe0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b543d4",
      "READ",
      [
        "storage",
        "01125658",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53fc8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b53fe0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b543d4",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b543f0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b54408",
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

- 旧版 [`00b53fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53f98.md#insn-00b53fb4) · [`00b53fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53f98.md#insn-00b53fc8) · [`00b53fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53f98.md#insn-00b53fe0)
- 新版 `00b543dc`（命令位置の公開資料なし）

~~~diff
- 00b53fb4 ["INT_ADD", "register:40f0:8", ["const:b53fb4:8", "const:4:8"]]
- 00b53fb4 ["CALL", null, ["callee:00c5b230:8"]]
+ 00b543dc ["INT_ADD", "register:40f0:8", ["const:b543dc:8", "const:4:8"]]
+ 00b543dc ["CALL", null, ["callee:00c5b230:8"]]
- 00b53fb4 bytes 9f1b0494
+ 00b543dc bytes 951b0494
- 00b53fc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53fc8 ["INT_ADD", "register:40f0:8", ["const:b53fc8:8", "const:4:8"]]
- 00b53fc8 ["CALLIND", null, ["register:0:8"]]
- 00b53fc8 bytes 00013fd6
- 00b53fe0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53fe0 ["INT_ADD", "register:40f0:8", ["const:b53fe0:8", "const:4:8"]]
- 00b53fe0 ["CALLIND", null, ["register:0:8"]]
- 00b53fe0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e6755fc06e086affa5b710953c0eae5"></a>

### [`00b5411c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b5411c.md) → [`00b54544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54544.md) _ZN8firebase4util12IsJByteArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54560",
      "incomplete_value": false,
      "site": "00b5456c",
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
            "const:db4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54138",
      "incomplete_value": false,
      "site": "00b54144",
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
            "const:d74:8"
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
      "site": "00b5417c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b545a4"
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
      "unmatched:00b54138",
      "PARAM",
      [
        "storage",
        "002bbd74",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5417c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54560",
      "PARAM",
      [
        "storage",
        "002bbdb4",
        null,
        null
      ]
    ],
    [
      "00b545a4",
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

- 旧版 [`00b54144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b5411c.md#insn-00b54144) · [`00b5417c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b5411c.md#insn-00b5417c) · [`00b54190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b5411c.md#insn-00b54190)
- 新版 `00b5456c`（命令位置の公開資料なし）

~~~diff
- 00b54144 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54144 ["INT_ADD", "register:40f0:8", ["const:b54144:8", "const:4:8"]]
- 00b54144 ["CALLIND", null, ["register:0:8"]]
+ 00b5456c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5456c ["INT_ADD", "register:40f0:8", ["const:b5456c:8", "const:4:8"]]
+ 00b5456c ["CALLIND", null, ["register:0:8"]]
- 00b54144 bytes 00013fd6
+ 00b5456c bytes 00013fd6
- 00b5417c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5417c ["INT_ADD", "register:40f0:8", ["const:b5417c:8", "const:4:8"]]
- 00b5417c ["CALLIND", null, ["register:0:8"]]
- 00b5417c bytes 00013fd6
- 00b54190 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b54190 ["RETURN", null, ["register:0:8"]]
- 00b54190 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf71d54c21fa70c0ec9658f82e3f431e"></a>

### [`00b5420c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b5420c.md) → [`00b54634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54634.md) _ZN8firebase4util13IsJShortArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54650",
      "incomplete_value": false,
      "site": "00b5465c",
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
            "const:5cb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54228",
      "incomplete_value": false,
      "site": "00b54234",
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
            "const:58b:8"
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
      "00b54650",
      "PARAM",
      [
        "storage",
        "002b458b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54650",
      "PARAM",
      [
        "storage",
        "002b45cb",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b5420c.md#insn-00b54234) · [`00b54228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b5420c.md#insn-00b54228) · [`00b54250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b5420c.md#insn-00b54250)
- 新版 `00b5465c`（命令位置の公開資料なし） · `00b54650`（命令位置の公開資料なし） · `00b54678`（命令位置の公開資料なし）

~~~diff
- 00b54234 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54234 ["INT_ADD", "register:40f0:8", ["const:b54234:8", "const:4:8"]]
- 00b54234 ["CALLIND", null, ["register:0:8"]]
+ 00b5465c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5465c ["INT_ADD", "register:40f0:8", ["const:b5465c:8", "const:4:8"]]
+ 00b5465c ["CALLIND", null, ["register:0:8"]]
- 00b54234 bytes 00013fd6
+ 00b5465c bytes 00013fd6
- 00b54228 ["COPY", "tmp:0:8", ["const:58b:8"]]
- 00b54228 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b54228 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b54228 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b54650 ["COPY", "tmp:0:8", ["const:5cb:8"]]
+ 00b54650 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b54650 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b54650 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b54228 bytes 212c1691
+ 00b54650 bytes 212c1791
- 00b54250 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54250 ["INT_ADD", "register:40f0:8", ["const:b54250:8", "const:4:8"]]
- 00b54250 ["CALLIND", null, ["register:0:8"]]
+ 00b54678 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b54678 ["INT_ADD", "register:40f0:8", ["const:b54678:8", "const:4:8"]]
+ 00b54678 ["CALLIND", null, ["register:0:8"]]
- 00b54250 bytes 00013fd6
+ 00b54678 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-673c7a6820e095712df992bff70ebdde"></a>

### [`00b54374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54374.md) → [`00b5479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b5479c.md) _ZN8firebase4util13IsJFloatArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54374"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54378"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54378"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54374",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54378",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5437c",
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
      "00b5479c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b547a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b547a4",
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

- 旧版 [`00b54374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54374.md#insn-00b54374) · [`00b54378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54374.md#insn-00b54378) · [`00b5437c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54374.md#insn-00b5437c)

~~~diff
- 00b54374 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b54374 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b54374 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b54374 bytes f50f1df8
- 00b54378 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b54378 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b54378 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b54378 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54378 bytes f44f01a9
- 00b5437c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5437c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5437c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5437c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5437c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9a6e444bb44a2f04a820b35970fd195"></a>

### [`00b54464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54464.md) → [`00b5488c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b5488c.md) _ZN8firebase4util22JBooleanArrayToVariantEP7_JNIEnvP14_jbooleanArray

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b0b0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b4b0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 96.91% / 新版 96.91%

CFGの説明率　旧版 27.27% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b545bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b549e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54978",
      "incomplete_value": true,
      "site": "00b5497c",
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
              [
                "live",
                "register:40b8:8"
              ]
            ]
          ],
          [
            "live",
            "register:40c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54550",
      "incomplete_value": true,
      "site": "00b54554",
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
            "register:40c0:8"
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
      "unmatched:00b545bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54a08"
      ]
    ]
  ],
  "added": [
    [
      "00b549e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54a08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54464.md#insn-00b54554) · [`00b545bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54464.md#insn-00b545bc) · [`00b545dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54464.md#insn-00b545dc)
- 新版 `00b5497c`（命令位置の公開資料なし）

~~~diff
- 00b54554 ["INT_ADD", "register:40f0:8", ["const:b54554:8", "const:4:8"]]
- 00b54554 ["CALL", null, ["callee:00c5a840:8"]]
+ 00b5497c ["INT_ADD", "register:40f0:8", ["const:b5497c:8", "const:4:8"]]
+ 00b5497c ["CALL", null, ["callee:00c5a840:8"]]
- 00b54554 bytes bb170494
+ 00b5497c bytes b1170494
- 00b545bc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b545bc ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00b545bc bytes 21010054
- 00b545dc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b545dc ["RETURN", null, ["register:0:8"]]
- 00b545dc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-121c575b873396018a165400d9936649"></a>

### [`00b54764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54764.md) → [`00b54b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54b8c.md) _ZN8firebase4util19JCharArrayToVariantEP7_JNIEnvP11_jcharArray

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5afe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afe0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3e0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 94.79% / 新版 94.79%

CFGの説明率　旧版 42.86% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54798"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b54bc0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54c18",
      "incomplete_value": true,
      "site": "00b54c1c",
      "value": [
        "INT_LEFT",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b547f0",
      "incomplete_value": true,
      "site": "00b547f4",
      "value": [
        "INT_LEFT",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:40d0:8"
              ],
              "INT_LEFT"
            ]
          ],
          [
            "leaf",
            "const:3:8"
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
      "unmatched:00b54798",
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
      "00b54bc0",
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

- 旧版 [`00b54798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54764.md#insn-00b54798) · [`00b547f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54764.md#insn-00b547f4) · [`00b54850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54764.md#insn-00b54850)
- 新版 `00b54c1c`（命令位置の公開資料なし） · `00b54c78`（命令位置の公開資料なし）

~~~diff
- 00b54798 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b54798 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b54798 bytes e90f00f9
- 00b547f4 ["INT_ADD", "register:40f0:8", ["const:b547f4:8", "const:4:8"]]
- 00b547f4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b54c1c ["INT_ADD", "register:40f0:8", ["const:b54c1c:8", "const:4:8"]]
+ 00b54c1c ["CALL", null, ["callee:00c57e90:8"]]
- 00b547f4 bytes a70c0494
+ 00b54c1c bytes 9d0c0494
- 00b54850 ["INT_ADD", "register:40f0:8", ["const:b54850:8", "const:4:8"]]
- 00b54850 ["CALL", null, ["callee:00c5a840:8"]]
+ 00b54c78 ["INT_ADD", "register:40f0:8", ["const:b54c78:8", "const:4:8"]]
+ 00b54c78 ["CALL", null, ["callee:00c5a840:8"]]
- 00b54850 bytes fc160494
+ 00b54c78 bytes f2160494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c70d93100f76bb5d91532273c333109"></a>

### [`00b548e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b548e4.md) → [`00b54d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54d0c.md) _ZN8firebase4util20JShortArrayToVariantEP7_JNIEnvP12_jshortArray

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b060.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b460.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.32% / 新版 86.32%

CFGの説明率　旧版 21.05% / 新版 26.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b548e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b548e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b548ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b548e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b548ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b548f0",
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
      "00b54d10",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b54d14",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b54d18",
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

- 旧版 [`00b548e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b548e4.md#insn-00b548e8) · [`00b548ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b548e4.md#insn-00b548ec) · [`00b548f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b548e4.md#insn-00b548f0)

~~~diff
- 00b548e8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b548e8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b548e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b548e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b548e8 bytes fc6f02a9
- 00b548ec ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b548ec ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b548ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b548ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b548ec bytes fa6703a9
- 00b548f0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b548f0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b548f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b548f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b548f0 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-297c5ad74c9b3ef5f803f1dd49b7e483"></a>

### [`00b54d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54d58.md) → [`00b55180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55180.md) _ZN8firebase4util20JFloatArrayToVariantEP7_JNIEnvP12_jfloatArray

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b050.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b450.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 23.53% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54d74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54d74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54d90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54d74",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54d90",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54e0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55224"
      ]
    ]
  ],
  "added": [
    [
      "00b5519c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b551b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b55234",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55224"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54d58.md#insn-00b54d74) · [`00b54d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54d58.md#insn-00b54d90) · [`00b54df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54d58.md#insn-00b54df8)

~~~diff
- 00b54d74 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b54d74 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b54d74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b54d74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54d74 bytes fd7b07a9
- 00b54d90 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b54d90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b54d90 bytes e90f00f9
- 00b54df8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:10:8"]]
- 00b54df8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b54df8 bytes e80a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-265547ec0405bdb368a783df83992b7d"></a>

### [`00b54ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54ee0.md) → [`00b55308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55308.md) _ZN8firebase4util21JDoubleArrayToVariantEP7_JNIEnvP13_jdoubleArray

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b080.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b480.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.26% / 新版 85.26%

CFGの説明率　旧版 37.50% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54ee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54ee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54ee8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54ee4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54ee8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54eec",
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
      "00b5530c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b55310",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b55314",
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

- 旧版 [`00b54ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54ee0.md#insn-00b54ee4) · [`00b54ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54ee0.md#insn-00b54ee8) · [`00b54eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54ee0.md#insn-00b54eec)

~~~diff
- 00b54ee4 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b54ee4 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b54ee4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b54ee4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54ee4 bytes fc6f02a9
- 00b54ee8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b54ee8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b54ee8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b54ee8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54ee8 bytes fa6703a9
- 00b54eec ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b54eec ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b54eec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b54eec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54eec bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3379b95300acf14f3142459a76d66720"></a>

### [`00b5505c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b5505c.md) → [`00b55484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55484.md) _ZN8firebase4util21JObjectArrayToVariantEP7_JNIEnvP13_jobjectArray

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b090.md) · 呼出先 7件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5b010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b010.md)
- 新版 呼出元 1件 [`00c5b490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b490.md) · 呼出先 7件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b410.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 6.67% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55090"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b554b8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5511c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55090",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5511c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b554b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b55544",
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

- 旧版 [`00b55090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b5505c.md#insn-00b55090) · [`00b5511c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b5505c.md#insn-00b5511c) · [`00b55130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b5505c.md#insn-00b55130)
- 新版 `00b55558`（命令位置の公開資料なし）

~~~diff
- 00b55090 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b55090 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b55090 bytes e90f00f9
- 00b5511c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5511c ["INT_ADD", "register:40f0:8", ["const:b5511c:8", "const:4:8"]]
- 00b5511c ["CALLIND", null, ["register:0:8"]]
- 00b5511c bytes 00013fd6
- 00b55130 ["INT_ADD", "register:40f0:8", ["const:b55130:8", "const:4:8"]]
- 00b55130 ["CALL", null, ["callee:00c5b410:8"]]
+ 00b55558 ["INT_ADD", "register:40f0:8", ["const:b55558:8", "const:4:8"]]
+ 00b55558 ["CALL", null, ["callee:00c5b410:8"]]
- 00b55130 bytes b8170494
+ 00b55558 bytes ae170494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b3a0c905df9d6c7ea19f13d2ad877c3"></a>

### [`00b551ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b551ac.md) → [`00b555d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b555d4.md) _ZN8firebase4util15JArrayToVariantEP7_JNIEnvP7_jarray

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5af00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af00.md) · 呼出先 11件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5afb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afb0.md) [`00c5afd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afd0.md) [`00c5afe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afe0.md)
- 新版 呼出元 1件 [`00c5b300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b300.md) · 呼出先 11件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3b0.md) [`00c5b3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3d0.md) [`00c5b3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 49.82% / 新版 49.82%

CFGの説明率　旧版 29.41% / 新版 32.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b552a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55310"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55380"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b551dc",
      "READ",
      [
        "storage",
        "01125568",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5566c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b55254"
      ]
    ],
    [
      "unmatched:00b5524c",
      "PARAM",
      [
        "storage",
        "002a4cbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b55604",
      "READ",
      [
        "storage",
        "01125968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5566c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5567c"
      ]
    ],
    [
      "00b55674",
      "PARAM",
      [
        "storage",
        "002a4d9b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b551d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b551ac.md#insn-00b551d4) · [`00b551ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b551ac.md#insn-00b551ec) · [`00b55200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b551ac.md#insn-00b55200)
- 新版 `00b55614`（命令位置の公開資料なし）

~~~diff
- 00b551d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b551d4 ["INT_ADD", "register:40f0:8", ["const:b551d4:8", "const:4:8"]]
- 00b551d4 ["CALLIND", null, ["register:0:8"]]
- 00b551d4 bytes 20013fd6
- 00b551ec ["INT_ADD", "register:40f0:8", ["const:b551ec:8", "const:4:8"]]
- 00b551ec ["CALL", null, ["callee:00497a48:8"]]
+ 00b55614 ["INT_ADD", "register:40f0:8", ["const:b55614:8", "const:4:8"]]
+ 00b55614 ["CALL", null, ["callee:00497a48:8"]]
- 00b551ec bytes 070ae597
+ 00b55614 bytes 0d09e597
- 00b55200 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55200 ["INT_ADD", "register:40f0:8", ["const:b55200:8", "const:4:8"]]
- 00b55200 ["CALLIND", null, ["register:0:8"]]
- 00b55200 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7af1ec14b2e7c0bc7bc84d7b50d44287"></a>

### [`00b5564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b5564c.md) → [`00b55a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55a74.md) _ZN8firebase4util14JniUriToStringEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aef0.md) · 呼出先 3件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)
- 新版 呼出元 1件 [`00c5b2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b2f0.md) · 呼出先 3件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md) [`00c5b5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5c0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55690"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b55ab8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b55a90",
      "incomplete_value": true,
      "site": "00b55a9c",
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b55668",
      "incomplete_value": true,
      "site": "00b55674",
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
                "const:930:8"
              ]
            ]
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
      "00b55a90",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b55690",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55adc"
      ]
    ],
    [
      "unmatched:00b55708",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b55a90",
      "READ",
      [
        "storage",
        "01125d30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55ab8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55adc"
      ]
    ],
    [
      "00b55b30",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b5564c.md#insn-00b55674) · [`00b55690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b5564c.md#insn-00b55690) · [`00b556b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b5564c.md#insn-00b556b0)
- 新版 `00b55a9c`（命令位置の公開資料なし）

~~~diff
- 00b55674 ["INT_ADD", "register:40f0:8", ["const:b55674:8", "const:4:8"]]
- 00b55674 ["CALL", null, ["callee:00497834:8"]]
+ 00b55a9c ["INT_ADD", "register:40f0:8", ["const:b55a9c:8", "const:4:8"]]
+ 00b55a9c ["CALL", null, ["callee:00497834:8"]]
- 00b55674 bytes 6008e597
+ 00b55a9c bytes 6607e597
- 00b55690 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00b55690 bytes 20010054
- 00b556b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b556b0 ["INT_ADD", "register:40f0:8", ["const:b556b0:8", "const:4:8"]]
- 00b556b0 ["CALLIND", null, ["register:0:8"]]
- 00b556b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d50022c376179a24b6a07d9b64ce139"></a>

### [`00b55714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55714.md) → [`00b55b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55b3c.md) _ZN8firebase4util13CharsToJniUriEP7_JNIEnvPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aeb0.md) · 呼出先 2件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md)
- 新版 呼出元 1件 [`00c5b2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b2b0.md) · 呼出先 2件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 85.51% / 新版 85.51%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b55b60",
      "incomplete_value": true,
      "site": "00b55b6c",
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
      "definition_site": "00b55738",
      "incomplete_value": true,
      "site": "00b55744",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b55b64",
      "incomplete_value": true,
      "site": "00b55b6c",
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
                "const:708:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5573c",
      "incomplete_value": true,
      "site": "00b55744",
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
                "const:308:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55774"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55738",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5573c",
      "READ",
      [
        "storage",
        "01125308",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55b88",
      "READ",
      [
        "storage",
        "01125310",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b55b60",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55b64",
      "READ",
      [
        "storage",
        "01125708",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55b88",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55714.md#insn-00b55744) · [`00b55774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55714.md#insn-00b55774) · [`00b557a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55714.md#insn-00b557a0)
- 新版 `00b55b6c`（命令位置の公開資料なし）

~~~diff
- 00b55744 ["INT_ADD", "register:40f0:8", ["const:b55744:8", "const:4:8"]]
- 00b55744 ["CALL", null, ["callee:005896f4:8"]]
+ 00b55b6c ["INT_ADD", "register:40f0:8", ["const:b55b6c:8", "const:4:8"]]
+ 00b55b6c ["CALL", null, ["callee:005896f4:8"]]
- 00b55744 bytes dccfe897
+ 00b55b6c bytes e2cee897
- 00b55774 ["INT_ADD", "register:40f0:8", ["const:b55774:8", "const:4:8"]]
- 00b55774 ["CALL", null, ["callee:00497834:8"]]
- 00b55774 bytes 2008e597
- 00b557a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b557a0 ["INT_ADD", "register:40f0:8", ["const:b557a0:8", "const:4:8"]]
- 00b557a0 ["CALLIND", null, ["register:0:8"]]
- 00b557a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e5669c9c3201eb55f1d7666bb7aea51"></a>

### [`00b55828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55828.md) → [`00b55c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55c50.md) _ZN8firebase4util14ParseUriStringEP7_JNIEnvPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md)

変更の種類 call, call_argument_candidate, call_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 85.37% / 新版 85.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b55c78",
      "incomplete_value": true,
      "site": "00b55c8c",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b55850",
      "incomplete_value": true,
      "site": "00b55864",
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
                "const:920:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b55c7c",
      "incomplete_value": true,
      "site": "00b55c8c",
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
                "const:d38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b55854",
      "incomplete_value": true,
      "site": "00b55864",
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
                "const:938:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55878"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55850",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b55854",
      "READ",
      [
        "storage",
        "01125938",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b55878",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b55c78",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55c7c",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55ca0",
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

- 旧版 [`00b55864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55828.md#insn-00b55864) · [`00b55878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55828.md#insn-00b55878) · [`00b55890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55828.md#insn-00b55890)
- 新版 `00b55c8c`（命令位置の公開資料なし） · `00b55cb8`（命令位置の公開資料なし）

~~~diff
- 00b55864 ["INT_ADD", "register:40f0:8", ["const:b55864:8", "const:4:8"]]
- 00b55864 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00b55c8c ["INT_ADD", "register:40f0:8", ["const:b55c8c:8", "const:4:8"]]
+ 00b55c8c ["CALL", null, ["callee:00c5aba0:8"]]
- 00b55864 bytes cf130494
+ 00b55c8c bytes c5130494
- 00b55878 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55878 ["INT_ADD", "register:40f0:8", ["const:b55878:8", "const:4:8"]]
- 00b55878 ["CALLIND", null, ["register:0:8"]]
- 00b55878 bytes 00013fd6
- 00b55890 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55890 ["INT_ADD", "register:40f0:8", ["const:b55890:8", "const:4:8"]]
- 00b55890 ["CALLIND", null, ["register:0:8"]]
+ 00b55cb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55cb8 ["INT_ADD", "register:40f0:8", ["const:b55cb8:8", "const:4:8"]]
+ 00b55cb8 ["CALLIND", null, ["register:0:8"]]
- 00b55890 bytes 00013fd6
+ 00b55cb8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31c0f9141673b43d42a2a5a1ac455861"></a>

### [`00b558cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b558cc.md) → [`00b55cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55cf4.md) _ZN8firebase4util10CharsToURLEP7_JNIEnvPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 58.54% / 新版 58.54%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b558cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b558d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b558d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b558cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b558d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b558d4",
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
      "00b55cf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b55cf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b55cfc",
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

- 旧版 [`00b558cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b558cc.md#insn-00b558cc) · [`00b558d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b558cc.md#insn-00b558d0) · [`00b558d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b558cc.md#insn-00b558d4)

~~~diff
- 00b558cc ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b558cc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b558cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b558cc bytes f50f1df8
- 00b558d0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b558d0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b558d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b558d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b558d0 bytes f44f01a9
- 00b558d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b558d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b558d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b558d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b558d4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b730954c71ab73c2e0c439aedaee1778"></a>

### [`00b559f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b559f4.md) → [`00b55e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55e1c.md) _ZN8firebase4util22LocalToGlobalReferenceEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_call_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 25.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55a18"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b55a28",
      "incomplete_value": true,
      "site": "00b55a30",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b55e40"
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
      "unmatched:00b55a18",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b55e40",
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

- 旧版 [`00b55a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b559f4.md#insn-00b55a18) · [`00b55a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b559f4.md#insn-00b55a30)
- 新版 `00b55e58`（命令位置の公開資料なし） · `00b55e40`（命令位置の公開資料なし）

~~~diff
- 00b55a18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55a18 ["INT_ADD", "register:40f0:8", ["const:b55a18:8", "const:4:8"]]
- 00b55a18 ["CALLIND", null, ["register:0:8"]]
- 00b55a18 bytes 00013fd6
- 00b55a30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55a30 ["INT_ADD", "register:40f0:8", ["const:b55a30:8", "const:4:8"]]
- 00b55a30 ["CALLIND", null, ["register:0:8"]]
+ 00b55e58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55e58 ["INT_ADD", "register:40f0:8", ["const:b55e58:8", "const:4:8"]]
+ 00b55e58 ["CALLIND", null, ["register:0:8"]]
- 00b55a30 bytes 00013fd6
+ 00b55e58 bytes 00013fd6
+ 00b55e40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55e40 ["INT_ADD", "register:40f0:8", ["const:b55e40:8", "const:4:8"]]
+ 00b55e40 ["CALLIND", null, ["register:0:8"]]
+ 00b55e40 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b7c21723feba4df2ebb7553be7d38a2"></a>

### [`00b55a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55a7c.md) → [`00b55ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55ea4.md) _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ab40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab40.md) · 呼出先 6件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md)
- 新版 呼出元 1件 [`00c5af40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af40.md) · 呼出先 6件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.77% / 新版 70.77%

CFGの説明率　旧版 15.00% / 新版 14.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55a7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55a80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55a80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55a7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55a80",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55a84",
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
      "00b55ea4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b55ea8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b55eac",
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

- 旧版 [`00b55a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55a7c.md#insn-00b55a7c) · [`00b55a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55a7c.md#insn-00b55a80) · [`00b55a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55a7c.md#insn-00b55a84)

~~~diff
- 00b55a7c ["COPY", "tmp:0:8", ["register:40d8:8"]]
- 00b55a7c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00b55a7c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b55a7c bytes fb0f1af8
- 00b55a80 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b55a80 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b55a80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b55a80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55a80 bytes fa6701a9
- 00b55a84 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b55a84 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b55a84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b55a84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55a84 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3a34bed77bcc4c0db7e9561f848cbff"></a>

### [`00b55c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55c84.md) → [`00b560ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b560ac.md) _ZN8firebase4util32JniResultCallback_nativeOnResultEP7_JNIEnvP8_jobjectS4_hhP8_jstringll

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_condition` 3件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55c98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55c98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55c9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55c98",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55c9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55cb4",
      "PARAM",
      [
        "storage",
        "01125988",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b560c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b560c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b560dc",
      "PARAM",
      [
        "storage",
        "01125d88",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55c84.md#insn-00b55c98) · [`00b55c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55c84.md#insn-00b55c9c) · [`00b55ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55c84.md#insn-00b55ce4)

~~~diff
- 00b55c98 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b55c98 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b55c98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b55c98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55c98 bytes f44f06a9
- 00b55c9c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b55c9c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b55c9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b55c9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55c9c bytes fd7b07a9
- 00b55ce4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b55ce4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b55ce4 bytes c10100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92478e5b95809d02b13a2e2ba5f61361"></a>

### [`00b55e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55e3c.md) → [`00b56264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56264.md) _ZN8firebase4util17JavaThreadContext24ReleaseExecuteCancelLockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ade0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ade0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5b1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 73.33% / 新版 73.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b55e5c",
      "incomplete_value": true,
      "site": "00b55e64",
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
                "const:298:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55e74"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b5629c"
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
      "00b5627c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b55ea8"
      ]
    ],
    [
      "00b56284",
      "READ",
      [
        "storage",
        "01125298",
        null,
        "undefined8"
      ]
    ],
    [
      "00b562a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b55ea8"
      ]
    ]
  ],
  "added": [
    [
      "00b5627c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b562d0"
      ]
    ],
    [
      "00b56284",
      "READ",
      [
        "storage",
        "01125698",
        null,
        "undefined8"
      ]
    ],
    [
      "00b562a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b562d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55e3c.md#insn-00b55e64) · [`00b55e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55e3c.md#insn-00b55e74) · [`00b55eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55e3c.md#insn-00b55eb0)
- 新版 `00b5628c`（命令位置の公開資料なし）

~~~diff
- 00b55e64 ["INT_ADD", "register:40f0:8", ["const:b55e64:8", "const:4:8"]]
- 00b55e64 ["CALL", null, ["callee:00574cec:8"]]
+ 00b5628c ["INT_ADD", "register:40f0:8", ["const:b5628c:8", "const:4:8"]]
+ 00b5628c ["CALL", null, ["callee:00574cec:8"]]
- 00b55e64 bytes 927be897
+ 00b5628c bytes 987ae897
- 00b55e74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55e74 ["INT_ADD", "register:40f0:8", ["const:b55e74:8", "const:4:8"]]
- 00b55e74 ["CALLIND", null, ["register:0:8"]]
- 00b55e74 bytes 00013fd6
- 00b55eb0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b55eb0 ["RETURN", null, ["register:0:8"]]
- 00b55eb0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56e4ddbfd0797f9057bc6e79983a6a95"></a>

### [`00b55eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55eb4.md) → [`00b562dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b562dc.md) _ZN8firebase4util17JavaThreadContext24AcquireExecuteCancelLockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c5ade0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ade0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c5b1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 69.70% / 新版 69.70%

CFGの説明率　旧版 11.11% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b562fc",
      "incomplete_value": true,
      "site": "00b56304",
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
                "const:6a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b55ed4",
      "incomplete_value": true,
      "site": "00b55edc",
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
                "const:2a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55ef4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55f0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b562fc",
      "READ",
      [
        "storage",
        "011252a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b55ef4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b55f0c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b562fc",
      "READ",
      [
        "storage",
        "011256a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5631c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b56334",
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

- 旧版 [`00b55edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55eb4.md#insn-00b55edc) · [`00b55ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55eb4.md#insn-00b55ef4) · [`00b55f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55eb4.md#insn-00b55f0c)
- 新版 `00b56304`（命令位置の公開資料なし）

~~~diff
- 00b55edc ["INT_ADD", "register:40f0:8", ["const:b55edc:8", "const:4:8"]]
- 00b55edc ["CALL", null, ["callee:00497a48:8"]]
+ 00b56304 ["INT_ADD", "register:40f0:8", ["const:b56304:8", "const:4:8"]]
+ 00b56304 ["CALL", null, ["callee:00497a48:8"]]
- 00b55edc bytes cb06e597
+ 00b56304 bytes d105e597
- 00b55ef4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55ef4 ["INT_ADD", "register:40f0:8", ["const:b55ef4:8", "const:4:8"]]
- 00b55ef4 ["CALLIND", null, ["register:0:8"]]
- 00b55ef4 bytes 00013fd6
- 00b55f0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55f0c ["INT_ADD", "register:40f0:8", ["const:b55f0c:8", "const:4:8"]]
- 00b55f0c ["CALLIND", null, ["register:0:8"]]
- 00b55f0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faefb810f538e945647b7514f012c87c"></a>

### [`00b55f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55f38.md) → [`00b56360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56360.md) _ZN8firebase4util17JavaThreadContext9TerminateEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5af80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af80.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b380.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 19.72% / 新版 19.72%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55f74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55fc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55ff0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b56374",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5637c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b55fc8"
      ]
    ],
    [
      "00b56384",
      "READ",
      [
        "storage",
        "01125280",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b56374",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5637c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b563f0"
      ]
    ],
    [
      "00b56384",
      "READ",
      [
        "storage",
        "01125680",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55f38.md#insn-00b55f54) · [`00b55f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55f38.md#insn-00b55f60) · [`00b55f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55f38.md#insn-00b55f70)
- 新版 `00b5637c`（命令位置の公開資料なし）

~~~diff
- 00b55f54 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b55f54 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00b5637c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b5637c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b55f54 bytes a10300b4
+ 00b5637c bytes a10300b4
- 00b55f60 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b55f60 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b55f60 bytes c8000034
- 00b55f70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55f70 ["INT_ADD", "register:40f0:8", ["const:b55f70:8", "const:4:8"]]
- 00b55f70 ["CALLIND", null, ["register:0:8"]]
- 00b55f70 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9f56695d8edab06a12793e388c244d0"></a>

### [`00b56054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56054.md) → [`00b5647c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b5647c.md) _ZN8firebase4util17JavaThreadContext13SetupInstanceEP7_JNIEnvPFvPvES4_S6_PS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5ad80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5b180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b180.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 66.67% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b564a4",
      "incomplete_value": true,
      "site": "00b564b0",
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5607c",
      "incomplete_value": true,
      "site": "00b56088",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:278:8"
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
      "definition_site": "00b564a8",
      "incomplete_value": true,
      "site": "00b564b0",
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
                "const:688:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56080",
      "incomplete_value": true,
      "site": "00b56088",
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
                "const:288:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5649c",
      "incomplete_value": true,
      "site": "00b564b0",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 5
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5607c",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b56080",
      "READ",
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
      "00b564a4",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "00b564a8",
      "READ",
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

- 旧版 [`00b56088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56054.md#insn-00b56088) · [`00b5607c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56054.md#insn-00b5607c) · [`00b56080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56054.md#insn-00b56080)
- 新版 `00b564b0`（命令位置の公開資料なし）

~~~diff
- 00b56088 ["INT_ADD", "register:40f0:8", ["const:b56088:8", "const:4:8"]]
- 00b56088 ["CALL", null, ["callee:005896f4:8"]]
+ 00b564b0 ["INT_ADD", "register:40f0:8", ["const:b564b0:8", "const:4:8"]]
+ 00b564b0 ["CALL", null, ["callee:005896f4:8"]]
- 00b56088 bytes 8bcde897
+ 00b564b0 bytes 91cce897
- 00b5607c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:278:8"]]
- 00b5607c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5607c bytes 013d41f9
- 00b56080 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:288:8"]]
- 00b56080 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b56080 bytes 224541f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b430744c8bd6d0825b5344c718f9093c"></a>

### [`00b560ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b560ec.md) → [`00b56514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56514.md) _ZN8firebase4util17JavaThreadContext15RunOnMainThreadEP7_JNIEnvP8_jobjectPFvPvES6_S8_PS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5af60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af60.md) · 呼出先 3件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5ad80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad80.md) [`00c5ae40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae40.md)
- 新版 呼出元 1件 [`00c5b360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b360.md) · 呼出先 3件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5b180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b180.md) [`00c5b240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b240.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 10.00% / 新版 7.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56140"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b561a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b56568"
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
      "unmatched:00b56118",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5611c",
      "READ",
      [
        "storage",
        "01125288",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b56140",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5658c"
      ]
    ]
  ],
  "added": [
    [
      "00b56540",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56544",
      "READ",
      [
        "storage",
        "01125688",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56568",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5658c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b56124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b560ec.md#insn-00b56124) · [`00b56140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b560ec.md#insn-00b56140) · [`00b56150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b560ec.md#insn-00b56150)
- 新版 `00b5654c`（命令位置の公開資料なし）

~~~diff
- 00b56124 ["INT_ADD", "register:40f0:8", ["const:b56124:8", "const:4:8"]]
- 00b56124 ["CALL", null, ["callee:005896f4:8"]]
+ 00b5654c ["INT_ADD", "register:40f0:8", ["const:b5654c:8", "const:4:8"]]
+ 00b5654c ["CALL", null, ["callee:005896f4:8"]]
- 00b56124 bytes 64cde897
+ 00b5654c bytes 6acce897
- 00b56140 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00b56140 bytes 20010054
- 00b56150 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b56150 ["INT_ADD", "register:40f0:8", ["const:b56150:8", "const:4:8"]]
- 00b56150 ["CALLIND", null, ["register:0:8"]]
- 00b56150 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b70135840d78645cb89522a8d8c516c3"></a>

### [`00b561ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b561ec.md) → [`00b56614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56614.md) _ZN8firebase4util17JavaThreadContext21RunOnBackgroundThreadEP7_JNIEnvPFvPvES4_S6_PS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5af70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af70.md) · 呼出先 3件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5ad80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad80.md) [`00c5ae40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae40.md)
- 新版 呼出元 1件 [`00c5b370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b370.md) · 呼出先 3件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5b180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b180.md) [`00c5b240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b240.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 69.35% / 新版 69.35%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5623c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b562a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b56664"
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
      "unmatched:00b56214",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b56218",
      "READ",
      [
        "storage",
        "01125288",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5623c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56688"
      ]
    ]
  ],
  "added": [
    [
      "00b5663c",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56640",
      "READ",
      [
        "storage",
        "01125688",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56664",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56688"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b56220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b561ec.md#insn-00b56220) · [`00b5623c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b561ec.md#insn-00b5623c) · [`00b5624c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b561ec.md#insn-00b5624c)
- 新版 `00b56648`（命令位置の公開資料なし）

~~~diff
- 00b56220 ["INT_ADD", "register:40f0:8", ["const:b56220:8", "const:4:8"]]
- 00b56220 ["CALL", null, ["callee:005896f4:8"]]
+ 00b56648 ["INT_ADD", "register:40f0:8", ["const:b56648:8", "const:4:8"]]
+ 00b56648 ["CALL", null, ["callee:005896f4:8"]]
- 00b56220 bytes 25cde897
+ 00b56648 bytes 2bcce897
- 00b5623c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b5623c bytes 20010054
- 00b5624c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5624c ["INT_ADD", "register:40f0:8", ["const:b5624c:8", "const:4:8"]]
- 00b5624c ["CALLIND", null, ["register:0:8"]]
- 00b5624c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8818da05160b7092229f7f3f204dc9fe"></a>

### [`00b562ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b562ec.md) → [`00b56714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56714.md) _ZN8firebase4util9FindClassEP7_JNIEnvPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b170.md) · 呼出先 1件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md)
- 新版 呼出元 1件 [`00c5b570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b570.md) · 呼出先 1件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 51.55% / 新版 51.55%

CFGの説明率　旧版 9.68% / 新版 10.34%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 9件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5678c",
      "incomplete_value": true,
      "site": "00b56790",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00b56364",
      "incomplete_value": true,
      "site": "00b56368",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56394"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56404"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b56780",
      "READ",
      [
        "storage",
        "01125970",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56798",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b56398"
      ]
    ],
    [
      "unmatched:00b56384",
      "READ",
      [
        "storage",
        "01125970",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b56780",
      "READ",
      [
        "storage",
        "01125d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56798",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b567c0"
      ]
    ],
    [
      "00b567ac",
      "READ",
      [
        "storage",
        "01125d70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b56324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b562ec.md#insn-00b56324) · [`00b5633c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b562ec.md#insn-00b5633c) · [`00b56350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b562ec.md#insn-00b56350)

~~~diff
- 00b56324 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b56324 ["INT_ADD", "register:40f0:8", ["const:b56324:8", "const:4:8"]]
- 00b56324 ["CALLIND", null, ["register:0:8"]]
- 00b56324 bytes 00013fd6
- 00b5633c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5633c ["INT_ADD", "register:40f0:8", ["const:b5633c:8", "const:4:8"]]
- 00b5633c ["CALLIND", null, ["register:0:8"]]
- 00b5633c bytes 00013fd6
- 00b56350 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b56350 ["INT_ADD", "register:40f0:8", ["const:b56350:8", "const:4:8"]]
- 00b56350 ["CALLIND", null, ["register:0:8"]]
- 00b56350 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b30b9f459202aad3f596d23b3f314286"></a>

### [`00b56470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56470.md) → [`00b56898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56898.md) _ZN8firebase4util16FindClassInFilesEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5af30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af30.md) · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5b330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b330.md) · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.73% / 新版 64.73%

CFGの説明率　旧版 15.57% / 新版 15.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_condition` 7件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 21件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56474"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56474"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56478"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56474",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56478",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5647c",
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
      "00b5689c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b568a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b568a4",
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

- 旧版 [`00b56474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56470.md#insn-00b56474) · [`00b56478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56470.md#insn-00b56478) · [`00b5647c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56470.md#insn-00b5647c)

~~~diff
- 00b56474 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b56474 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b56474 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b56474 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56474 bytes fc6f0aa9
- 00b56478 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b56478 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b56478 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00b56478 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56478 bytes fa670ba9
- 00b5647c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5647c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5647c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00b5647c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5647c bytes f85f0ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d47d6fa3d62dcbec822078559270041"></a>

### [`00b56b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56b70.md) → [`00b56f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56f98.md) _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_S6_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b270.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b670.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 11.11% / 新版 10.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56b70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56b70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56b74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56b70",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56b74",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56b78",
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
      "00b56f98",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b56f9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b56fa0",
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

- 旧版 [`00b56b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56b70.md#insn-00b56b70) · [`00b56b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56b70.md#insn-00b56b74) · [`00b56b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56b70.md#insn-00b56b78)

~~~diff
- 00b56b70 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b56b70 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b56b70 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b56b70 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b56b70 bytes f85fbca9
- 00b56b74 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b56b74 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b56b74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b56b74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56b74 bytes f65701a9
- 00b56b78 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b56b78 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b56b78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b56b78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56b78 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3df0a853e861e7e4452d77c53cc04170"></a>

### [`00b56ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56ca0.md) → [`00b570c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b570c8.md) _ZN8firebase4util25GetResourceIdFromActivityEP7_JNIEnvP8_jobjectPKcNS0_12ResourceTypeE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 65.45% / 新版 65.45%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 8件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56ce8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56d38"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56dcc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56cbc",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b56ce8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57134"
      ]
    ],
    [
      "00b57138",
      "READ",
      [
        "storage",
        "011253f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b570e4",
      "READ",
      [
        "storage",
        "01125800",
        null,
        "undefined8"
      ]
    ],
    [
      "00b57110",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57134"
      ]
    ],
    [
      "00b57138",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b56ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56ca0.md#insn-00b56ccc) · [`00b56ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56ca0.md#insn-00b56ce0) · [`00b56ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56ca0.md#insn-00b56ce8)
- 新版 `00b570f4`（命令位置の公開資料なし）

~~~diff
- 00b56ccc ["INT_ADD", "register:40f0:8", ["const:b56ccc:8", "const:4:8"]]
- 00b56ccc ["CALL", null, ["callee:00497834:8"]]
+ 00b570f4 ["INT_ADD", "register:40f0:8", ["const:b570f4:8", "const:4:8"]]
+ 00b570f4 ["CALL", null, ["callee:00497834:8"]]
- 00b56ccc bytes ca02e597
+ 00b570f4 bytes d001e597
- 00b56ce0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b56ce0 ["INT_ADD", "register:40f0:8", ["const:b56ce0:8", "const:4:8"]]
- 00b56ce0 ["CALLIND", null, ["register:0:8"]]
- 00b56ce0 bytes 00013fd6
- 00b56ce8 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b56ce8 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4f0e216c6227d6e34ba9be44f8b60be"></a>

### [`00b56e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56e58.md) → [`00b57280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57280.md) _ZN8firebase4util29GetResourceStringFromActivityEP7_JNIEnvP8_jobjecti

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.22% / 新版 62.22%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56e58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56e58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56e5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56e58",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56e5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56e60",
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
      "00b57280",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b57284",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b57288",
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

- 旧版 [`00b56e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56e58.md#insn-00b56e58) · [`00b56e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56e58.md#insn-00b56e5c) · [`00b56e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56e58.md#insn-00b56e60)

~~~diff
- 00b56e58 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b56e58 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b56e58 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b56e58 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b56e58 bytes f657bda9
- 00b56e5c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b56e5c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b56e5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b56e5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56e5c bytes f44f01a9
- 00b56e60 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b56e60 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b56e60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b56e60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56e60 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12631e58b4d9848d3e4238349bea9f88"></a>

### [`00b56f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f0c.md) → [`00b57334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57334.md) _ZN8firebase4util14GetPackageNameEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.89% / 新版 63.89%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56f10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56f10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56f0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56f10",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56f14",
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
      "00b57334",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b57338",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5733c",
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

- 旧版 [`00b56f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f0c.md#insn-00b56f0c) · [`00b56f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f0c.md#insn-00b56f10) · [`00b56f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f0c.md#insn-00b56f14)

~~~diff
- 00b56f0c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b56f0c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b56f0c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b56f0c bytes f50f1df8
- 00b56f10 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b56f10 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b56f10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b56f10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56f10 bytes f44f01a9
- 00b56f14 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b56f14 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b56f14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b56f14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56f14 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-571c398297ddf35d982f0bb0402fe6b1"></a>

### [`00b56f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f9c.md) → [`00b573c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b573c4.md) _ZN8firebase4util27GetAndClearExceptionMessageEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ab70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab70.md) · 呼出先 1件 [`00c5ab50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab50.md)
- 新版 呼出元 1件 [`00c5af70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af70.md) · 呼出先 1件 [`00c5af50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af50.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56f9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56fa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56fa0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56f9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56fa0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56fa4",
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
      "00b573c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b573c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b573cc",
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

- 旧版 [`00b56f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f9c.md#insn-00b56f9c) · [`00b56fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f9c.md#insn-00b56fa0) · [`00b56fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f9c.md#insn-00b56fa4)

~~~diff
- 00b56f9c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b56f9c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b56f9c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b56f9c bytes f50f1df8
- 00b56fa0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b56fa0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b56fa0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b56fa0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56fa0 bytes f44f01a9
- 00b56fa4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b56fa4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b56fa4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b56fa4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56fa4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6024bd7bec5fa13dcb5e752701b02e77"></a>

### [`00b571c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b571c4.md) → [`00b575ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b575ec.md) _ZN8firebase4util12LogExceptionEP7_JNIEnvNS_8LogLevelEPKcz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aae0.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5acc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acc0.md)
- 新版 呼出元 1件 [`00c5aee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aee0.md) · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md) [`00c5b0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0c0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 43.93% / 新版 43.93%

CFGの説明率　旧版 10.26% / 新版 8.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 15件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 28件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b571c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b571c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b571cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b571c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b571cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b571d0",
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
      "00b575f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b575f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b575f8",
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

- 旧版 [`00b571c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b571c4.md#insn-00b571c8) · [`00b571cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b571c4.md#insn-00b571cc) · [`00b571d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b571c4.md#insn-00b571d0)

~~~diff
- 00b571c8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b571c8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b571c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00b571c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b571c8 bytes fc6711a9
- 00b571cc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b571cc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b571cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00b571cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b571cc bytes f85f12a9
- 00b571d0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b571d0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b571d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00b571d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b571d0 bytes f65713a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a50c480b4168e01d1a62af4c6809afe"></a>

### [`00b574e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b574e0.md) → [`00b57908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57908.md) _ZN8firebase4util19AttachCurrentThreadEP7_JavaVMPP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-779d999493908730312fe9adef3aa8f2"></a>

### [`00b57504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57504.md) → [`00b5792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b5792c.md) _ZN8firebase4util19GetThreadsafeJNIEnvEP7_JavaVM

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afc0.md) · 呼出先 4件 [`00b574f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b574f0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c5b2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2c0.md)
- 新版 呼出元 1件 [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md) · 呼出先 4件 [`00b57918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57918.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5b6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 86.11% / 新版 86.11%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57574"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5757c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5799c"
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
      "unmatched:00b5752c",
      "READ",
      [
        "storage",
        "00c9b338",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b5752c",
      "PARAM",
      [
        "storage",
        "01125bb8",
        "_ZN8firebase4util23pthread_key_initializedE",
        "undefined4"
      ]
    ],
    [
      "unmatched:00b57530",
      "READ",
      [
        "storage",
        "00c9b310",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b57954",
      "READ",
      [
        "storage",
        "00c9b738",
        null,
        "pointer"
      ]
    ],
    [
      "00b57954",
      "PARAM",
      [
        "storage",
        "01125fb8",
        "_ZN8firebase4util23pthread_key_initializedE",
        "undefined4"
      ]
    ],
    [
      "00b57958",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b57534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57504.md#insn-00b57534) · [`00b57548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57504.md#insn-00b57548) · [`00b57560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57504.md#insn-00b57560)
- 新版 `00b5795c`（命令位置の公開資料なし） · `00b57970`（命令位置の公開資料なし） · `00b57988`（命令位置の公開資料なし）

~~~diff
- 00b57534 ["INT_ADD", "register:40f0:8", ["const:b57534:8", "const:4:8"]]
- 00b57534 ["CALL", null, ["callee:00c5b6c0:8"]]
+ 00b5795c ["INT_ADD", "register:40f0:8", ["const:b5795c:8", "const:4:8"]]
+ 00b5795c ["CALL", null, ["callee:00c5b6c0:8"]]
- 00b57534 bytes 630f0494
+ 00b5795c bytes 590f0494
- 00b57548 ["INT_ADD", "register:40f0:8", ["const:b57548:8", "const:4:8"]]
- 00b57548 ["CALL", null, ["callee:00c58140:8"]]
+ 00b57970 ["INT_ADD", "register:40f0:8", ["const:b57970:8", "const:4:8"]]
+ 00b57970 ["CALL", null, ["callee:00c58140:8"]]
- 00b57548 bytes fe010494
+ 00b57970 bytes f4010494
- 00b57560 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b57560 ["INT_ADD", "register:40f0:8", ["const:b57560:8", "const:4:8"]]
- 00b57560 ["CALLIND", null, ["register:0:8"]]
+ 00b57988 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b57988 ["INT_ADD", "register:40f0:8", ["const:b57988:8", "const:4:8"]]
+ 00b57988 ["CALLIND", null, ["register:0:8"]]
- 00b57560 bytes 00013fd6
+ 00b57988 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-818be7e729c6df85fa4e3d02b62c8d98"></a>

### [`00b57594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57594.md) → [`00b579bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b579bc.md) _ZN8firebase4util16GetJNIEnvFromAppEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5af40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af40.md) · 呼出先 3件 [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5b340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b340.md) · 呼出先 3件 [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b250.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5759c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57594.md#insn-00b5759c) · [`00b575a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57594.md#insn-00b575a0) · [`00b575a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57594.md#insn-00b575a4)
- 新版 `00b579c4`（命令位置の公開資料なし） · `00b579c8`（命令位置の公開資料なし） · `00b579cc`（命令位置の公開資料なし）

~~~diff
- 00b5759c ["INT_ADD", "register:40f0:8", ["const:b5759c:8", "const:4:8"]]
- 00b5759c ["CALL", null, ["callee:00c5b250:8"]]
+ 00b579c4 ["INT_ADD", "register:40f0:8", ["const:b579c4:8", "const:4:8"]]
+ 00b579c4 ["CALL", null, ["callee:00c5b250:8"]]
- 00b5759c bytes 2d0e0494
+ 00b579c4 bytes 230e0494
- 00b575a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b575a0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b579c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b579c8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b575a0 bytes 600000b5
+ 00b579c8 bytes 600000b5
- 00b575a4 ["INT_ADD", "register:40f0:8", ["const:b575a4:8", "const:4:8"]]
- 00b575a4 ["CALL", null, ["callee:00c5b260:8"]]
+ 00b579cc ["INT_ADD", "register:40f0:8", ["const:b579cc:8", "const:4:8"]]
+ 00b579cc ["CALL", null, ["callee:00c5b260:8"]]
- 00b575a4 bytes 2f0e0494
+ 00b579cc bytes 250e0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14521aaabad9947e06648bcf0221ce98"></a>

### [`00b575bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b575bc.md) → [`00b579e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b579e4.md) _ZN8firebase7Variant18set_mutable_stringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b180.md) · 呼出先 3件 [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a500.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5b580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b580.md) · 呼出先 3件 [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a900.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 38.46% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57610"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57614"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5764c"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b575f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b575bc.md#insn-00b575f8) · [`00b57610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b575bc.md#insn-00b57610) · [`00b57614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b575bc.md#insn-00b57614)
- 新版 `00b57a20`（命令位置の公開資料なし）

~~~diff
- 00b575f8 ["INT_ADD", "register:40f0:8", ["const:b575f8:8", "const:4:8"]]
- 00b575f8 ["CALL", null, ["callee:00c5a830:8"]]
+ 00b57a20 ["INT_ADD", "register:40f0:8", ["const:b57a20:8", "const:4:8"]]
+ 00b57a20 ["CALL", null, ["callee:00c5a830:8"]]
- 00b575f8 bytes 8e0b0494
+ 00b57a20 bytes 840b0494
- 00b57610 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b57610 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b57610 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b57610 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b57610 bytes 6801899a
- 00b57614 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b57614 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b57614 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b57614 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:1:8"]]
- 00b57614 bytes 4115939a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6815bbe5bfbf0e1625a7ead8125c18c8"></a>

### [`00b57664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57664.md) → [`00b57a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57a8c.md) _ZNSt6__ndk16__treeINS_12__value_typeIPKcNS_4listIN8firebase4util12CallbackDataENS_9allocatorIS7_EEEEEENS_19__map_value_compareIS3_SB_NS_4le

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b210.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5b610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b610.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 8.33% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57698"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b57ac0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b57aa4",
      "incomplete_value": true,
      "site": "00b57aac",
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
      "unmatched:00b57698",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57b00"
      ]
    ]
  ],
  "added": [
    [
      "00b57ac0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57b00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b57684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57664.md#insn-00b57684) · [`00b57690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57664.md#insn-00b57690) · [`00b57698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57664.md#insn-00b57698)
- 新版 `00b57aac`（命令位置の公開資料なし） · `00b57ab8`（命令位置の公開資料なし）

~~~diff
- 00b57684 ["INT_ADD", "register:40f0:8", ["const:b57684:8", "const:4:8"]]
- 00b57684 ["CALL", null, ["callee:00c5b610:8"]]
+ 00b57aac ["INT_ADD", "register:40f0:8", ["const:b57aac:8", "const:4:8"]]
+ 00b57aac ["CALL", null, ["callee:00c5b610:8"]]
- 00b57684 bytes e30e0494
+ 00b57aac bytes d90e0494
- 00b57690 ["INT_ADD", "register:40f0:8", ["const:b57690:8", "const:4:8"]]
- 00b57690 ["CALL", null, ["callee:00c5b610:8"]]
+ 00b57ab8 ["INT_ADD", "register:40f0:8", ["const:b57ab8:8", "const:4:8"]]
+ 00b57ab8 ["CALL", null, ["callee:00c5b610:8"]]
- 00b57690 bytes e00e0494
+ 00b57ab8 bytes d60e0494
- 00b57698 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b57698 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b57698 bytes 080200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ac7233aec9cdff5ba2fade33a0a3c72"></a>

### [`00b576f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b576f0.md) → [`00b57b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57b18.md) _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 10.87% / 新版 11.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b576f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b577ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57820"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b576fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57bd4"
      ]
    ],
    [
      "unmatched:00b57754",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57b88"
      ]
    ],
    [
      "unmatched:00b577cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57c00"
      ]
    ]
  ],
  "added": [
    [
      "00b57b24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57bd4"
      ]
    ],
    [
      "00b57b7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57b88"
      ]
    ],
    [
      "00b57bf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57c00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b576f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b576f0.md#insn-00b576f8) · [`00b576fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b576f0.md#insn-00b576fc) · [`00b57754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b576f0.md#insn-00b57754)

~~~diff
- 00b576f8 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b576f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:18:8"]]
- 00b576f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b576f8 bytes 28600039
- 00b576fc ["CBRANCH", null, ["local:b18:8", "register:101:1"]]
- 00b576fc bytes 80050054
- 00b57754 ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 00b57754 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b57754 bytes 6b0000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ea86cf96a97229c37337fd1f2c96a3f"></a>

### [`00b57890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57890.md) → [`00b57cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57cb8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 53.85% / 新版 43.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b578d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b57cf8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b578f8",
      "incomplete_value": true,
      "site": "00b578fc",
      "value": [
        "INT_AND",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:fffffffffffffff0:8"
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
      "unmatched:00b578d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57d5c"
      ]
    ]
  ],
  "added": [
    [
      "00b57cf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57d5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b578d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57890.md#insn-00b578d0) · [`00b578fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57890.md#insn-00b578fc)
- 新版 `00b57d24`（命令位置の公開資料なし） · `00b57cf8`（命令位置の公開資料なし）

~~~diff
- 00b578d0 ["CBRANCH", null, ["local:b10:8", "register:102:1"]]
- 00b578d0 bytes 22030054
- 00b578fc ["INT_ADD", "register:40f0:8", ["const:b578fc:8", "const:4:8"]]
- 00b578fc ["CALL", null, ["callee:00c57e90:8"]]
+ 00b57d24 ["INT_ADD", "register:40f0:8", ["const:b57d24:8", "const:4:8"]]
+ 00b57d24 ["CALL", null, ["callee:00c57e90:8"]]
- 00b578fc bytes 65000494
+ 00b57d24 bytes 5b000494
+ 00b57cf8 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
+ 00b57cf8 bytes 22030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d538d39045ef0b4684dbcbac32090321"></a>

### [`00b57938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57938.md) → [`00b57d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57d60.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE25__emp

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1f0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5b1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1a0.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md)
- 新版 呼出元 1件 [`00c5b5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5f0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5a0.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 22.22% / 新版 20.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b579f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57a38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b57e1c"
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
      "unmatched:00b5795c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57ddc"
      ]
    ],
    [
      "unmatched:00b579d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57de8"
      ]
    ]
  ],
  "added": [
    [
      "00b57d84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57ddc"
      ]
    ],
    [
      "00b57df8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57de8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5795c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57938.md#insn-00b5795c) · [`00b57974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57938.md#insn-00b57974) · [`00b579d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57938.md#insn-00b579d0)
- 新版 `00b57d9c`（命令位置の公開資料なし）

~~~diff
- 00b5795c ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
- 00b5795c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b5795c bytes d80200b4
- 00b57974 ["INT_ADD", "register:40f0:8", ["const:b57974:8", "const:4:8"]]
- 00b57974 ["CALL", null, ["callee:00c5b5a0:8"]]
+ 00b57d9c ["INT_ADD", "register:40f0:8", ["const:b57d9c:8", "const:4:8"]]
+ 00b57d9c ["CALL", null, ["callee:00c5b5a0:8"]]
- 00b57974 bytes 0b0e0494
+ 00b57d9c bytes 010e0494
- 00b579d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b579d0 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b579d0 bytes 95ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbf65fd666593a8ea1677b94ed80b648"></a>

### [`00b57a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57a54.md) → [`00b57e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57e7c.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIRKS6_EEvOT_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b240.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)
- 新版 呼出元 1件 [`00c5b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b640.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 86.90% / 新版 86.90%

CFGの説明率　旧版 32.26% / 新版 32.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57a8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57ab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57b24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b57a8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57fc8"
      ]
    ],
    [
      "unmatched:00b57ab8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57ef4"
      ]
    ],
    [
      "unmatched:00b57b24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57f28"
      ]
    ]
  ],
  "added": [
    [
      "00b57eb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57fc8"
      ]
    ],
    [
      "00b57ee0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57ef4"
      ]
    ],
    [
      "00b57f4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57f28"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b57a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57a54.md#insn-00b57a8c) · [`00b57ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57a54.md#insn-00b57ab8) · [`00b57ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57a54.md#insn-00b57ad4)
- 新版 `00b57efc`（命令位置の公開資料なし）

~~~diff
- 00b57a8c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b57a8c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b57a8c ["CBRANCH", null, ["local:b23:8", "tmp:1:1"]]
- 00b57a8c bytes a8080054
- 00b57ab8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b57ab8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b57ab8 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00b57ab8 bytes a8000054
- 00b57ad4 ["INT_ADD", "register:40f0:8", ["const:b57ad4:8", "const:4:8"]]
- 00b57ad4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b57efc ["INT_ADD", "register:40f0:8", ["const:b57efc:8", "const:4:8"]]
+ 00b57efc ["CALL", null, ["callee:00c57e90:8"]]
- 00b57ad4 bytes efff0394
+ 00b57efc bytes e5ff0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dca79c4df18fb1b062be199757c1d19"></a>

### [`00b57e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57e68.md) → [`00b58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58290.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE8__appendEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b260.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b660.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 86.76% / 新版 86.76%

CFGの説明率　旧版 33.33% / 新版 38.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57ea8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57eb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b582d0"
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
      "unmatched:00b57ea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5839c"
      ]
    ],
    [
      "unmatched:00b57eb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5831c"
      ]
    ]
  ],
  "added": [
    [
      "00b582d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5839c"
      ]
    ],
    [
      "00b582e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5831c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b57ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57e68.md#insn-00b57ea8) · [`00b57eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57e68.md#insn-00b57eb8) · [`00b57f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57e68.md#insn-00b57f18)
- 新版 `00b58340`（命令位置の公開資料なし）

~~~diff
- 00b57ea8 ["CBRANCH", null, ["local:b19:8", "register:100:1"]]
- 00b57ea8 bytes 64060054
- 00b57eb8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b57eb8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b57eb8 ["CBRANCH", null, ["local:b11:8", "tmp:1:1"]]
- 00b57eb8 bytes e8010054
- 00b57f18 ["INT_ADD", "register:40f0:8", ["const:b57f18:8", "const:4:8"]]
- 00b57f18 ["CALL", null, ["callee:00c58090:8"]]
+ 00b58340 ["INT_ADD", "register:40f0:8", ["const:b58340:8", "const:4:8"]]
+ 00b58340 ["CALL", null, ["callee:00c58090:8"]]
- 00b57f18 bytes 5eff0394
+ 00b58340 bytes 54ff0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81c04892220e3ce846c277fe338c3449"></a>

### [`00b57f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57f78.md) → [`00b583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b583a0.md) _ZNSt6__ndk16__treeINS_12__value_typeIPKcNS_4listIN8firebase4util12CallbackDataENS_9allocatorIS7_EEEEEENS_19__map_value_compareIS3_SB_NS_4le

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b200.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1d0.md)
- 新版 呼出元 1件 [`00c5b600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b600.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5d0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 42.86% / 新版 40.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58014"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5801c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5843c"
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
      "00b583c8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b57fd0"
      ]
    ],
    [
      "unmatched:00b57fb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b57fd0"
      ]
    ],
    [
      "unmatched:00b57fcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b57fb8"
      ]
    ]
  ],
  "added": [
    [
      "00b583c8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b583f8"
      ]
    ],
    [
      "00b583dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b583f8"
      ]
    ],
    [
      "00b583f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b583e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b57fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57f78.md#insn-00b57fb4) · [`00b57fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57f78.md#insn-00b57fcc) · [`00b57fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57f78.md#insn-00b57fd8)

~~~diff
- 00b57fb4 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b57fb4 bytes e0000054
- 00b57fcc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b57fcc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b57fcc bytes 61ffff54
- 00b57fd8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b57fd8 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b57fd8 bytes 41000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b30129c93101ebe3556e0febb61a92cf"></a>

### [`00b58058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58058.md) → [`00b58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58480.md) _ZNSt6__ndk113__tree_removeIPNS_16__tree_node_baseIPvEEEEvT_S5_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1d0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5b5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5d0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.59% / 新版 85.59%

CFGの説明率　旧版 34.78% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 4件

アドレスに依存する影響 `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b580dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b580f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b581fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b58658",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58494"
      ]
    ],
    [
      "unmatched:00b581f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b581f8"
      ]
    ],
    [
      "unmatched:00b58230",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58584"
      ]
    ]
  ],
  "added": [
    [
      "00b5849c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58494"
      ]
    ],
    [
      "00b58618",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58620"
      ]
    ],
    [
      "00b58658",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58584"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b580dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58058.md#insn-00b580dc) · [`00b580f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58058.md#insn-00b580f0) · [`00b581f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58058.md#insn-00b581f0)

~~~diff
- 00b580dc ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:10:8"]]
- 00b580dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4068:8"]]
- 00b580dc bytes 4d0900f9
- 00b580f0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b580f0 ["INT_ZEXT", "tmp:1:8", ["register:4070:4"]]
- 00b580f0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b580f0 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:3:8"]]
- 00b580f0 bytes aa592ef8
- 00b581f0 ["INT_EQUAL", "tmp:0:1", ["register:4060:8", "const:0:8"]]
- 00b581f0 ["CBRANCH", null, ["local:b43:8", "tmp:0:1"]]
- 00b581f0 bytes 4c0000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0a6fedc618409a00df7f770776c1e97"></a>

### [`00b58408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58408.md) → [`00b58830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58830.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) · 呼出先 2件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5aca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aca0.md)
- 新版 呼出元 1件 [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) · 呼出先 2件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 38.10% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b58880",
      "incomplete_value": true,
      "site": "00b58894",
      "value": [
        "live",
        "register:4098:8"
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
      "definition_site": "00b5887c",
      "incomplete_value": true,
      "site": "00b58894",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:4040:8"
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
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b588b0",
      "incomplete_value": true,
      "site": "00b588bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "live",
            "register:40a8:8"
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

- 旧版 [`00b5846c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58408.md#insn-00b5846c) · [`00b58494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58408.md#insn-00b58494) · [`00b584c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58408.md#insn-00b584c8)
- 新版 `00b58894`（命令位置の公開資料なし） · `00b588bc`（命令位置の公開資料なし）

~~~diff
- 00b5846c ["INT_ADD", "register:40f0:8", ["const:b5846c:8", "const:4:8"]]
- 00b5846c ["CALL", null, ["callee:00c5b0a0:8"]]
+ 00b58894 ["INT_ADD", "register:40f0:8", ["const:b58894:8", "const:4:8"]]
+ 00b58894 ["CALL", null, ["callee:00c5b0a0:8"]]
- 00b5846c bytes 0d0a0494
+ 00b58894 bytes 030a0494
- 00b58494 ["INT_ADD", "register:40f0:8", ["const:b58494:8", "const:4:8"]]
- 00b58494 ["CALL", null, ["callee:00c58000:8"]]
+ 00b588bc ["INT_ADD", "register:40f0:8", ["const:b588bc:8", "const:4:8"]]
+ 00b588bc ["CALL", null, ["callee:00c58000:8"]]
- 00b58494 bytes dbfd0394
+ 00b588bc bytes d1fd0394
- 00b584c8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b584c8 ["RETURN", null, ["register:0:8"]]
- 00b584c8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3934129fb5deddd69a019d5d39e830f"></a>

### [`00b584cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b584cc.md) → [`00b588f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b588f4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 88.41% / 新版 88.41%

CFGの説明率　旧版 44.00% / 新版 40.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b584f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5858c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5891c"
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
      "unmatched:00b584f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58a04"
      ]
    ],
    [
      "unmatched:00b5858c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b589cc"
      ]
    ]
  ],
  "added": [
    [
      "00b5891c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58a04"
      ]
    ],
    [
      "00b589b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b589cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b584f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b584cc.md#insn-00b584f4) · [`00b5858c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b584cc.md#insn-00b5858c) · [`00b585a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b584cc.md#insn-00b585a0)
- 新版 `00b589c8`（命令位置の公開資料なし）

~~~diff
- 00b584f4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b584f4 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b584f4 bytes 43070054
- 00b5858c ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00b5858c bytes c0000054
- 00b585a0 ["INT_ADD", "register:40f0:8", ["const:b585a0:8", "const:4:8"]]
- 00b585a0 ["CALL", null, ["callee:00c58000:8"]]
+ 00b589c8 ["INT_ADD", "register:40f0:8", ["const:b589c8:8", "const:4:8"]]
+ 00b589c8 ["CALL", null, ["callee:00c58000:8"]]
- 00b585a0 bytes 98fd0394
+ 00b589c8 bytes 8efd0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-057a36f358255cf764f396b5a5affdff"></a>

### [`00b585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b585e0.md) → [`00b58a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58a08.md) Java_com_google_firebase_app_internal_cpp_Log_nativeLog

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5acc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acc0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md) [`00c5b0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.64% / 新版 69.64%

CFGの説明率　旧版 16.67% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b585f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b585f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5860c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b585f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5860c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58648",
      "READ",
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
      "00b58a18",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b58a34",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b58a70",
      "READ",
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

- 旧版 [`00b585f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b585e0.md#insn-00b585f0) · [`00b5860c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b585e0.md#insn-00b5860c) · [`00b58630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b585e0.md#insn-00b58630)
- 新版 `00b58a58`（命令位置の公開資料なし）

~~~diff
- 00b585f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b585f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b585f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b585f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b585f0 bytes fd7b07a9
- 00b5860c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b5860c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5860c bytes e81f00f9
- 00b58630 ["INT_ADD", "register:40f0:8", ["const:b58630:8", "const:4:8"]]
- 00b58630 ["CALL", null, ["callee:00c5af20:8"]]
+ 00b58a58 ["INT_ADD", "register:40f0:8", ["const:b58a58:8", "const:4:8"]]
+ 00b58a58 ["CALL", null, ["callee:00c5af20:8"]]
- 00b58630 bytes 3c090494
+ 00b58a58 bytes 32090494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cd90d2ea6df840522e5ee908062a8b0"></a>

### [`00b58730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58730.md) → [`00b58b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58b58.md) _ZN8firebase8internal16JObjectReference9GetJavaVMEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5874c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58750"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b58b74"
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
      "unmatched:00b5874c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58750",
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
      "00b58b74",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b58b78",
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

- 旧版 [`00b5874c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58730.md#insn-00b5874c) · [`00b58750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58730.md#insn-00b58750) · [`00b5875c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58730.md#insn-00b5875c)
- 新版 `00b58b84`（命令位置の公開資料なし）

~~~diff
- 00b5874c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b5874c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5874c bytes e80700f9
- 00b58750 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b58750 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b58750 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b58750 bytes ff0300f9
- 00b5875c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5875c ["INT_ADD", "register:40f0:8", ["const:b5875c:8", "const:4:8"]]
- 00b5875c ["CALLIND", null, ["register:0:8"]]
+ 00b58b84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b58b84 ["INT_ADD", "register:40f0:8", ["const:b58b84:8", "const:4:8"]]
+ 00b58b84 ["CALLIND", null, ["register:0:8"]]
- 00b5875c bytes 00013fd6
+ 00b58b84 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c08473487b221f10b5309b7849e58252"></a>

### [`00b58788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58788.md) → [`00b58bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58bb0.md) _ZN8firebase8internal16JObjectReferenceC2EP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b587fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b58c24"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b58bd4",
      "incomplete_value": true,
      "site": "00b58bf0",
      "value": [
        "live",
        "register:4008:8"
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
      "unmatched:00b587fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58c3c"
      ]
    ]
  ],
  "added": [
    [
      "00b58c24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58c3c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b587c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58788.md#insn-00b587c8) · [`00b587fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58788.md#insn-00b587fc)
- 新版 `00b58bf0`（命令位置の公開資料なし） · `00b58c24`（命令位置の公開資料なし）

~~~diff
- 00b587c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b587c8 ["INT_ADD", "register:40f0:8", ["const:b587c8:8", "const:4:8"]]
- 00b587c8 ["CALLIND", null, ["register:0:8"]]
+ 00b58bf0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b58bf0 ["INT_ADD", "register:40f0:8", ["const:b58bf0:8", "const:4:8"]]
+ 00b58bf0 ["CALLIND", null, ["register:0:8"]]
- 00b587c8 bytes 00013fd6
+ 00b58bf0 bytes 00013fd6
- 00b587fc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b587fc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b587fc bytes c1000054
+ 00b58c24 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b58c24 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b58c24 bytes c1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e41daf79b729dea97b972d0894922d7"></a>

### [`00b588c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b588c0.md) → [`00b58ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58ce8.md) _ZN8firebase8internal16JObjectReferenceC2EOS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-871b3ab7616855010abea9a42f7341ef"></a>

### [`00b589a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b589a8.md) → [`00b58dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58dd0.md) _ZN8firebase8internal16JObjectReferenceaSERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 7.14% / 新版 5.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58a5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b58e84"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58a00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58a5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58ea0"
      ]
    ],
    [
      "unmatched:00b58a00",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b58a28",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b58e84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58ea0"
      ]
    ],
    [
      "00b58e28",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b58e50",
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

- 旧版 [`00b58a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b589a8.md#insn-00b58a00) · [`00b58a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b589a8.md#insn-00b58a28) · [`00b58a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b589a8.md#insn-00b58a5c)

~~~diff
- 00b58a00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58a00 ["INT_ADD", "register:40f0:8", ["const:b58a00:8", "const:4:8"]]
- 00b58a00 ["CALLIND", null, ["register:0:8"]]
- 00b58a00 bytes 00013fd6
- 00b58a28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58a28 ["INT_ADD", "register:40f0:8", ["const:b58a28:8", "const:4:8"]]
- 00b58a28 ["CALLIND", null, ["register:0:8"]]
- 00b58a28 bytes 00013fd6
- 00b58a5c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b58a5c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b58a5c bytes e1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c9ab60cf336ee6d0f1d6cce7b67ee6d"></a>

### [`00b58b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58b78.md) → [`00b58fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58fa0.md) _ZN8firebase8internal16JObjectReference18FromLocalReferenceEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ad70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad70.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5b170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b170.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.50% / 新版 67.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58b7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58b7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58b80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58b7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58b80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58b84",
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
      "00b58fa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b58fa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b58fac",
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

- 旧版 [`00b58b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58b78.md#insn-00b58b7c) · [`00b58b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58b78.md#insn-00b58b80) · [`00b58b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58b78.md#insn-00b58b84)

~~~diff
- 00b58b7c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b58b7c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b58b7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b58b7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58b7c bytes f65701a9
- 00b58b80 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b58b80 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b58b80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b58b80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58b80 bytes f44f02a9
- 00b58b84 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b58b84 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b58b84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b58b84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58b84 bytes fd7b03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d73143d301e91295950b18f48ccdf7ed"></a>

### [`00b58c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58c18.md) → [`00b59040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b59/00b59040.md) _ZN8firebase10app_common6AddAppEPNS_3AppEPNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS_10InitResultENS3_4l

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b350.md) · 呼出先 20件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5b750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b750.md) · 呼出先 20件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.88% / 新版 86.88%

CFGの説明率　旧版 25.58% / 新版 23.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 6件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58c30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58c30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58c4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58c30",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58c4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58c68",
      "PARAM",
      [
        "storage",
        "002ad0c9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b59058",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b59074",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b59090",
      "PARAM",
      [
        "storage",
        "002ad109",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58c18.md#insn-00b58c30) · [`00b58c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58c18.md#insn-00b58c4c) · [`00b58cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58c18.md#insn-00b58cbc)
- 新版 `00b590e4`（命令位置の公開資料なし）

~~~diff
- 00b58c30 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b58c30 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b58c30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b58c30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58c30 bytes fd7b09a9
- 00b58c4c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b58c4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b58c4c bytes e81f00f9
- 00b58cbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd0:8"]]
- 00b58cbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00b590e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd0:8"]]
+ 00b590e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b58cbc bytes 13e905f9
+ 00b590e4 bytes 13e907f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01db63e96e6be4530106e90ecea9d944"></a>

### [`00b58f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58f8c.md) → [`00b593b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b59/00b593b4.md) _ZN8firebase10app_common13FindAppByNameEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2f0.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5b6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6f0.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 7.41% / 新版 8.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58f9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58f9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58fa0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58f9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58fa0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58fb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b593c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b593c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b593dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58f8c.md#insn-00b58f9c) · [`00b58fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58f8c.md#insn-00b58fa0) · [`00b58fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58f8c.md#insn-00b58fb4)

~~~diff
- 00b58f9c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b58f9c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b58f9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b58f9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58f9c bytes f44f05a9
- 00b58fa0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b58fa0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b58fa0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b58fa0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58fa0 bytes fd7b06a9
- 00b58fb4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b58fb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b58fb4 bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-053f8fbb13922ef243c4300efe49f26c"></a>

### [`00b590c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590c4.md) → [`00b594ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b59/00b594ec.md) _ZN8firebase10app_common16IsDefaultAppNameEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b330.md) · 呼出先 1件 [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)
- 新版 呼出元 1件 [`00c5b730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b730.md) · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b594fc",
      "incomplete_value": false,
      "site": "00b59500",
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
            "const:932:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b590d4",
      "incomplete_value": false,
      "site": "00b590d8",
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
            "const:8f2:8"
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
      "definition_site": "00b594f4",
      "incomplete_value": true,
      "site": "00b59500",
      "value": [
        "live",
        "register:4000:8"
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
      "unmatched:00b590d4",
      "PARAM",
      [
        "storage",
        "002b58f2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b594fc",
      "PARAM",
      [
        "storage",
        "002b5932",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b590d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590c4.md#insn-00b590d8) · [`00b590d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590c4.md#insn-00b590d4)
- 新版 `00b59500`（命令位置の公開資料なし） · `00b594fc`（命令位置の公開資料なし）

~~~diff
- 00b590d8 ["INT_ADD", "register:40f0:8", ["const:b590d8:8", "const:4:8"]]
- 00b590d8 ["CALL", null, ["callee:00c5b850:8"]]
+ 00b59500 ["INT_ADD", "register:40f0:8", ["const:b59500:8", "const:4:8"]]
+ 00b59500 ["CALL", null, ["callee:00c5b850:8"]]
- 00b590d8 bytes de080494
+ 00b59500 bytes d4080494
- 00b590d4 ["COPY", "tmp:0:8", ["const:8f2:8"]]
- 00b590d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b590d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b590d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b590d4 bytes 00c82391
+ 00b594fc ["COPY", "tmp:0:8", ["const:932:8"]]
+ 00b594fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b594fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b594fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b594fc bytes 00c82491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cde1f5dc98a002d97ccbf307a274f96"></a>

### [`00b590f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590f8.md) → [`00b59520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b59/00b59520.md) _ZN8firebase10app_common9GetAnyAppEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 36.36% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b590f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b590f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b590fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b590f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b590fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b59530",
      "READ",
      [
        "storage",
        "01125bd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b59520",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b59524",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b59530",
      "READ",
      [
        "storage",
        "01125fd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b590f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590f8.md#insn-00b590f8) · [`00b590fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590f8.md#insn-00b590fc) · [`00b5911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590f8.md#insn-00b5911c)
- 新版 `00b59544`（命令位置の公開資料なし）

~~~diff
- 00b590f8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b590f8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b590f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b590f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b590f8 bytes f44fbea9
- 00b590fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b590fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b590fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b590fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b590fc bytes fd7b01a9
- 00b5911c ["INT_ADD", "register:40f0:8", ["const:b5911c:8", "const:4:8"]]
- 00b5911c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b59544 ["INT_ADD", "register:40f0:8", ["const:b59544:8", "const:4:8"]]
+ 00b59544 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5911c bytes 39050494
+ 00b59544 bytes 2f050494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e396d3432f9c4ef722c86f28f0467804"></a>

### [`00b59160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59160.md) → [`00b59588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b59/00b59588.md) _ZN8firebase10app_common10GetAllAppsEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2d0.md) · 呼出先 7件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5b6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6d0.md) · 呼出先 7件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 18.87% / 新版 18.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59198"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b595a8",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5918c",
      "READ",
      [
        "storage",
        "01125bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5919c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5aa00"
      ]
    ]
  ],
  "added": [
    [
      "00b595a8",
      "READ",
      [
        "storage",
        "01125fc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b595b4",
      "READ",
      [
        "storage",
        "01125fd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b595c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5aa00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b59194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59160.md#insn-00b59194) · [`00b59198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59160.md#insn-00b59198) · [`00b5919c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59160.md#insn-00b5919c)

~~~diff
- 00b59194 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b59194 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b59194 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b59194 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b59194 bytes 9f7e00a9
- 00b59198 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:10:8"]]
- 00b59198 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b59198 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b59198 bytes 9f0a00f9
- 00b5919c ["INT_ADD", "register:40f0:8", ["const:b5919c:8", "const:4:8"]]
- 00b5919c ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5919c bytes 19050494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8b7cbc3e4547b415d42733d621e0293"></a>

### [`00b59318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59318.md) → [`00b59740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b59/00b59740.md) _ZN8firebase10app_common9RemoveAppEPNS_3AppE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b360.md) · 呼出先 16件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`00c5b760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b760.md) · 呼出先 16件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.06% / 新版 81.06%

CFGの説明率　旧版 12.50% / 新版 12.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59330"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59330"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59344"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b59330",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b59344",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b59774",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b59758",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5976c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b59774",
      "READ",
      [
        "storage",
        "01125fc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b59330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59318.md#insn-00b59330) · [`00b59344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59318.md#insn-00b59344) · [`00b59354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59318.md#insn-00b59354)
- 新版 `00b5977c`（命令位置の公開資料なし）

~~~diff
- 00b59330 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b59330 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b59330 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b59330 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b59330 bytes fd7b07a9
- 00b59344 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b59344 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b59344 bytes e80f00f9
- 00b59354 ["INT_ADD", "register:40f0:8", ["const:b59354:8", "const:4:8"]]
- 00b59354 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5977c ["INT_ADD", "register:40f0:8", ["const:b5977c:8", "const:4:8"]]
+ 00b5977c ["CALL", null, ["callee:00c5aa00:8"]]
- 00b59354 bytes ab040494
+ 00b5977c bytes a1040494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ddbb26d57297055b57c737bdcfd5f0e"></a>

### [`00b59528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59528.md) → [`00b59950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b59/00b59950.md) _ZN8firebase10app_common14DestroyAllAppsEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.86% / 新版 78.86%

CFGの説明率　旧版 37.50% / 新版 38.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5962c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59764"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b59a54"
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
      "00b59970",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b59978",
      "READ",
      [
        "storage",
        "01125bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b59558",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5aa00"
      ]
    ]
  ],
  "added": [
    [
      "00b59970",
      "READ",
      [
        "storage",
        "01125fc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b59978",
      "READ",
      [
        "storage",
        "01125fd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b59980",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5aa00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b59558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59528.md#insn-00b59558) · [`00b59564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59528.md#insn-00b59564) · [`00b59598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59528.md#insn-00b59598)

~~~diff
- 00b59558 ["INT_ADD", "register:40f0:8", ["const:b59558:8", "const:4:8"]]
- 00b59558 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b59558 bytes 2a040494
- 00b59564 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b59564 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
- 00b59564 bytes 880900b4
- 00b59598 ["CBRANCH", null, ["local:b33:8", "register:101:1"]]
- 00b59598 bytes 40090054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48cca95b20f418b0e74b2fe28fc0e93f"></a>

### [`00b597e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b597e4.md) → [`00b59c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b59/00b59c0c.md) _ZN8firebase10app_common15RegisterLibraryEPKcS2_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b320.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5b300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b300.md) [`00c5b310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b310.md)
- 新版 呼出元 1件 [`00c5b720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b720.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b700.md) [`00c5b710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b710.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_store_alignment

命令の説明率　旧版 63.16% / 新版 63.16%

CFGの説明率　旧版 11.11% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b597e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b597e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b597e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b597e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b597e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b597ec",
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
      "00b59c0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b59c10",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b59c14",
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

- 旧版 [`00b597e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b597e4.md#insn-00b597e4) · [`00b597e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b597e4.md#insn-00b597e8) · [`00b597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b597e4.md#insn-00b597ec)

~~~diff
- 00b597e4 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b597e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b597e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b597e4 bytes f70f1cf8
- 00b597e8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b597e8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b597e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b597e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b597e8 bytes f65701a9
- 00b597ec ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b597ec ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b597ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b597ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b597ec bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ef600dd2ab428830c70ea6be0407282"></a>

### [`00b5987c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b5987c.md) → [`00b59ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b59/00b59ca4.md) _ZN8firebase10app_common15LibraryRegistry15RegisterLibraryEPKcS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b300.md) · 呼出先 12件 [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00493d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5b700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b700.md) · 呼出先 12件 [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00493dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 93.31% / 新版 93.31%

CFGの説明率　旧版 58.42% / 新版 59.60%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b598b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b598b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b598b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b598b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b598b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b598bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b59cdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b59ce0",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "00b59ce4",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b598b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b5987c.md#insn-00b598b4) · [`00b598b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b5987c.md#insn-00b598b8) · [`00b598bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b5987c.md#insn-00b598bc)

~~~diff
- 00b598b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:58:8"]]
- 00b598b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b598b4 bytes e82f00f9
- 00b598b8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b598b8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b598b8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b598b8 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b598b8 bytes ff7f04a9
- 00b598bc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b598bc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b598bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b598bc bytes ff1f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9626dfe155e1dc3897643364491c1613"></a>

### [`00b59f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59f10.md) → [`00b5a338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5a338.md) _ZN8firebase10app_common30RegisterLibrariesFromUserAgentEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.72% / 新版 83.72%

CFGの説明率　旧版 63.33% / 新版 65.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59f14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59f18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59f18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b59f14",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b59f18",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b59f1c",
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
      "00b5a33c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5a340",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5a344",
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

- 旧版 [`00b59f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59f10.md#insn-00b59f14) · [`00b59f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59f10.md#insn-00b59f18) · [`00b59f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59f10.md#insn-00b59f1c)

~~~diff
- 00b59f14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b59f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b59f14 bytes f91300f9
- 00b59f18 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b59f18 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b59f18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b59f18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b59f18 bytes f85f03a9
- 00b59f1c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b59f1c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b59f1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b59f1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b59f1c bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a9beb92ba2d98a6f89cff8d8243b7eb"></a>

### [`00b5a068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a068.md) → [`00b5a490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5a490.md) _ZN8firebase10app_common16RegisterSdkUsageEPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b340.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5b3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3b0.md)
- 新版 呼出元 1件 [`00c5b740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b740.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7b0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 61.76% / 新版 61.76%

CFGの説明率　旧版 25.00% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a068"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a06c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a06c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5a068",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a06c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a070",
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
      "00b5a490",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5a494",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5a498",
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

- 旧版 [`00b5a068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a068.md#insn-00b5a068) · [`00b5a06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a068.md#insn-00b5a06c) · [`00b5a070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a068.md#insn-00b5a070)

~~~diff
- 00b5a068 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5a068 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5a068 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5a068 bytes f50f1df8
- 00b5a06c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5a06c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5a06c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5a06c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a06c bytes f44f01a9
- 00b5a070 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5a070 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5a070 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5a070 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a070 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fff17516a2cec4ca997543df6161576"></a>

### [`00b5a178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a178.md) → [`00b5a5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5a5a0.md) _ZN8firebase10app_common12GetUserAgentEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2e0.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5b6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6e0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 57.14% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5a5c8",
      "incomplete_value": true,
      "site": "00b5a5c8",
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
      "definition_site": "00b5a1a0",
      "incomplete_value": true,
      "site": "00b5a1a0",
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
      "definition_site": "00b5a5b4",
      "incomplete_value": true,
      "site": "00b5a5b8",
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
                "const:fc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a18c",
      "incomplete_value": true,
      "site": "00b5a190",
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
                "const:bc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00b5a1a0"
      ],
      [
        "FALL_THROUGH",
        "00b5a5c8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b5a5c8",
      "incomplete_value": true,
      "site": "00b5a5d8",
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
      "definition_site": "00b5a1a0",
      "incomplete_value": true,
      "site": "00b5a1b0",
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
      "00b5a5b0",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5a5c0",
      "READ",
      [
        "storage",
        "00c9b350",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a5c4",
      "READ",
      [
        "storage",
        "01125bc8",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5a5b0",
      "READ",
      [
        "storage",
        "01125fc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5a5c0",
      "READ",
      [
        "storage",
        "00c9b750",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a5c4",
      "READ",
      [
        "storage",
        "01125fc8",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a178.md#insn-00b5a190) · [`00b5a1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a178.md#insn-00b5a1a0) · [`00b5a188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a178.md#insn-00b5a188)
- 新版 `00b5a5b8`（命令位置の公開資料なし） · `00b5a5c8`（命令位置の公開資料なし） · `00b5a5b0`（命令位置の公開資料なし）

~~~diff
- 00b5a190 ["INT_ADD", "register:40f0:8", ["const:b5a190:8", "const:4:8"]]
- 00b5a190 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5a5b8 ["INT_ADD", "register:40f0:8", ["const:b5a5b8:8", "const:4:8"]]
+ 00b5a5b8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5a190 bytes 1c010494
+ 00b5a5b8 bytes 12010494
- 00b5a1a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b5a1a0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b5a5c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b5a5c8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b5a1a0 bytes 400100b5
+ 00b5a5c8 bytes 400100b5
- 00b5a188 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bc0:8"]]
- 00b5a188 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5a5b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc0:8"]]
+ 00b5a5b0 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5a188 bytes 13e145f9
+ 00b5a5b0 bytes 13e147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf1ef8ed88aa08fba56d0f0dfc7bd8b8"></a>

### [`00b5a1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a1f8.md) → [`00b5a620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5a620.md) _ZN8firebase10app_common17GetLibraryVersionEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00493d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00493dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.60% / 新版 95.60%

CFGの説明率　旧版 3.70% / 新版 3.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a224"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a2c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a2c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5a224",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b5a654",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5a664",
      "READ",
      [
        "storage",
        "00c9b350",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5a64c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b5a654",
      "READ",
      [
        "storage",
        "01125fc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5a664",
      "READ",
      [
        "storage",
        "00c9b750",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a1f8.md#insn-00b5a224) · [`00b5a234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a1f8.md#insn-00b5a234) · [`00b5a244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a1f8.md#insn-00b5a244)
- 新版 `00b5a65c`（命令位置の公開資料なし） · `00b5a66c`（命令位置の公開資料なし）

~~~diff
- 00b5a224 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b5a224 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b5a224 bytes e90f00f9
- 00b5a234 ["INT_ADD", "register:40f0:8", ["const:b5a234:8", "const:4:8"]]
- 00b5a234 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5a65c ["INT_ADD", "register:40f0:8", ["const:b5a65c:8", "const:4:8"]]
+ 00b5a65c ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5a234 bytes f3000494
+ 00b5a65c bytes e9000494
- 00b5a244 ["INT_NOTEQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b5a244 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b5a66c ["INT_NOTEQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
+ 00b5a66c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5a244 bytes 760100b5
+ 00b5a66c bytes 760100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-442006be162f36e8e1a3450e36cfae3d"></a>

### [`00b5a364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a364.md) → [`00b5a78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5a78c.md) _ZN8firebase10app_common25GetOuterMostSdkAndVersionEPNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00493d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00493dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.17% / 新版 86.17%

CFGの説明率　旧版 28.77% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 4件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 8件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a37c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a37c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a388"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5a37c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a388",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a390",
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
      "00b5a7a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5a7b0",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ],
    [
      "00b5a7b8",
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

- 旧版 [`00b5a37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a364.md#insn-00b5a37c) · [`00b5a388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a364.md#insn-00b5a388) · [`00b5a390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a364.md#insn-00b5a390)

~~~diff
- 00b5a37c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5a37c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5a37c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00b5a37c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a37c bytes fd7b0ba9
- 00b5a388 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b5a388 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5a388 bytes e80f00f9
- 00b5a390 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:58:8"]]
- 00b5a390 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5a390 bytes e82f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bac08ea30525eefdd8693c7f581c219b"></a>

### [`00b5a654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a654.md) → [`00b5aa7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5aa7c.md) _ZN8firebase10app_common19FindAppLoggerByNameEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.90% / 新版 85.90%

CFGの説明率　旧版 34.78% / 新版 38.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a67c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a6f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a6f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5a67c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b5aaac",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5aabc",
      "READ",
      [
        "storage",
        "01125bd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5aaa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b5aaac",
      "READ",
      [
        "storage",
        "01125fc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5aabc",
      "READ",
      [
        "storage",
        "01125fd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a654.md#insn-00b5a67c) · [`00b5a68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a654.md#insn-00b5a68c) · [`00b5a698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a654.md#insn-00b5a698)
- 新版 `00b5aab4`（命令位置の公開資料なし） · `00b5aac0`（命令位置の公開資料なし）

~~~diff
- 00b5a67c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b5a67c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5a67c bytes e80f00f9
- 00b5a68c ["INT_ADD", "register:40f0:8", ["const:b5a68c:8", "const:4:8"]]
- 00b5a68c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5aab4 ["INT_ADD", "register:40f0:8", ["const:b5aab4:8", "const:4:8"]]
+ 00b5aab4 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5a68c bytes ddff0394
+ 00b5aab4 bytes d3ff0394
- 00b5a698 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b5a698 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00b5aac0 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00b5aac0 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b5a698 bytes b40500b4
+ 00b5aac0 bytes b40500b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5f458167ea5f1d2956c92dc4a2fd844"></a>

### [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) → [`00b5abb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5abb4.md) FUN_00b5abb4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 9件 [`00b59cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59cb0.md) [`00b5d210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d210.md) [`00b5d2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d2d4.md) [`00b7198c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b7198c.md) [`00b72b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b72b34.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 9件 [`00b5a0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5a0d8.md) [`00b5d638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d638.md) [`00b5d6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d6fc.md) [`00b71db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71db4.md) [`00b72f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72f5c.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 47.06% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5abe8",
      "incomplete_value": true,
      "site": "00b5abf0",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md#insn-00b5a7c8) · [`00b5a7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md#insn-00b5a7bc) · [`00b5a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md#insn-00b5a7d4)
- 新版 `00b5abf0`（命令位置の公開資料なし） · `00b5abe4`（命令位置の公開資料なし） · `00b5abfc`（命令位置の公開資料なし）

~~~diff
- 00b5a7c8 ["INT_ADD", "register:40f0:8", ["const:b5a7c8:8", "const:4:8"]]
- 00b5a7c8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00b5abf0 ["INT_ADD", "register:40f0:8", ["const:b5abf0:8", "const:4:8"]]
+ 00b5abf0 ["CALL", null, ["callee:00c57fe0:8"]]
- 00b5a7c8 bytes 06f50394
+ 00b5abf0 bytes fcf40394
- 00b5a7bc ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b5a7bc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b5a7bc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b5a7bc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b5abe4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b5abe4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b5abe4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b5abe4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b5a7bc bytes e8000037
+ 00b5abe4 bytes e8000037
- 00b5a7d4 ["BRANCH", null, ["local:b5:8"]]
+ 00b5abfc ["BRANCH", null, ["local:b4:8"]]
- 00b5a7d4 bytes 06000014
+ 00b5abfc bytes 06000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ef974a612e3ee58559f7b2a1979d53a"></a>

### [`00b5a934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a934.md) → [`00b5ad5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ad5c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b400.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5b800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b800.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 75.00% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a95c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a9e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5ad84"
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
      "unmatched:00b5a95c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5ae4c"
      ]
    ],
    [
      "unmatched:00b5a9e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5ae20"
      ]
    ]
  ],
  "added": [
    [
      "00b5ad84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5ae4c"
      ]
    ],
    [
      "00b5ae0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5ae20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a934.md#insn-00b5a95c) · [`00b5a9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a934.md#insn-00b5a9e4)
- 新版 `00b5ad84`（命令位置の公開資料なし）

~~~diff
- 00b5a95c ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b5a95c ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b5a95c bytes 570600b4
- 00b5a9e4 ["CBRANCH", null, ["local:b14:8", "register:102:1"]]
- 00b5a9e4 bytes a2000054
+ 00b5ad84 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
+ 00b5ad84 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00b5ad84 bytes 570600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5e8fcc1699009487398d105123a7cf7"></a>

### [`00b5ad94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ad94.md) → [`00b5b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b1bc.md) _INIT_279

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b5ade4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ade4.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b5b20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b20c.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5b200",
      "incomplete_value": false,
      "site": "00b5b200",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5add8",
      "incomplete_value": false,
      "site": "00b5add8",
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
            "const:bc0:8"
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
      "definition_site": "00b5b1d0",
      "incomplete_value": true,
      "site": "00b5b1e0",
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
      "definition_site": "00b5ada8",
      "incomplete_value": true,
      "site": "00b5adb8",
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
                "const:2f0:8"
              ]
            ]
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
      "definition_site": "00b5b1d4",
      "incomplete_value": true,
      "site": "00b5b1e0",
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
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5adac",
      "incomplete_value": true,
      "site": "00b5adb8",
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
                "const:358:8"
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
      "00b5b1d0",
      "READ",
      [
        "storage",
        "00c9b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5b1d0",
      "PARAM",
      [
        "storage",
        "00b5ade4",
        "_ZN8firebase6LoggerD1Ev",
        null
      ]
    ],
    [
      "00b5b1d4",
      "READ",
      [
        "storage",
        "00c9b358",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5b1d0",
      "READ",
      [
        "storage",
        "00c9b6f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5b1d0",
      "PARAM",
      [
        "storage",
        "00b5b20c",
        "_ZN8firebase6LoggerD1Ev",
        null
      ]
    ],
    [
      "00b5b1d4",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5adb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ad94.md#insn-00b5adb8) · [`00b5add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ad94.md#insn-00b5add8) · [`00b5ada8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ad94.md#insn-00b5ada8)
- 新版 `00b5b1e0`（命令位置の公開資料なし） · `00b5b200`（命令位置の公開資料なし） · `00b5b1d0`（命令位置の公開資料なし）

~~~diff
- 00b5adb8 ["INT_ADD", "register:40f0:8", ["const:b5adb8:8", "const:4:8"]]
- 00b5adb8 ["CALL", null, ["callee:00c57e30:8"]]
+ 00b5b1e0 ["INT_ADD", "register:40f0:8", ["const:b5b1e0:8", "const:4:8"]]
+ 00b5b1e0 ["CALL", null, ["callee:00c57e30:8"]]
- 00b5adb8 bytes 1ef30394
+ 00b5b1e0 bytes 14f30394
- 00b5add8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bc0:8"]]
- 00b5add8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00b5b200 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc0:8"]]
+ 00b5b200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b5add8 bytes 13e105f9
+ 00b5b200 bytes 13e107f9
- 00b5ada8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:2f0:8"]]
- 00b5ada8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5b1d0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:6f0:8"]]
+ 00b5b1d0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5ada8 bytes 007841f9
+ 00b5b1d0 bytes 007843f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75ac0454a9176aee1481443e9c0eadec"></a>

### [`00b5b0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b0f4.md) → [`00b5b51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b51c.md) _ZNK8firebase10LoggerBase8LogErrorEPKcz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 22.22% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b0f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b0f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b0fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5b0f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b0fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b100",
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
      "00b5b520",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5b524",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5b528",
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

- 旧版 [`00b5b0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b0f4.md#insn-00b5b0f8) · [`00b5b0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b0f4.md#insn-00b5b0fc) · [`00b5b100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b0f4.md#insn-00b5b100)

~~~diff
- 00b5b0f8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b5b0f8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5b0f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00b5b0f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b0f8 bytes fc5712a9
- 00b5b0fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5b0fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5b0fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00b5b0fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b0fc bytes f44f13a9
- 00b5b100 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5b100 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5b100 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b5b100 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b100 bytes fd7b14a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90b822f6426118d57956053b93464610"></a>

### [`00b5b294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b294.md) → [`00b5b6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b6bc.md) _ZNK8firebase10LoggerBase10LogMessageENS_8LogLevelEPKcz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 43.64% / 新版 43.64%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b2ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b2ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b2b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5b2ac",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b2b0",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b2b4",
      "WRITE",
      [
        "storage",
        "Stack[-0xb8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5b6d4",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ],
    [
      "00b5b6d8",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "00b5b6dc",
      "WRITE",
      [
        "storage",
        "Stack[-0xb8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b294.md#insn-00b5b2ac) · [`00b5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b294.md#insn-00b5b2b0) · [`00b5b2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b294.md#insn-00b5b2b4)

~~~diff
- 00b5b2ac ["COPY", "tmp:0:8", ["register:4018:8"]]
- 00b5b2ac ["COPY", "tmp:1:8", ["register:4020:8"]]
- 00b5b2ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:88:8"]]
- 00b5b2ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b2ac bytes e39308a9
- 00b5b2b0 ["COPY", "tmp:0:8", ["register:4028:8"]]
- 00b5b2b0 ["COPY", "tmp:1:8", ["register:4030:8"]]
- 00b5b2b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:98:8"]]
- 00b5b2b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b2b0 bytes e59b09a9
- 00b5b2b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:a8:8"]]
- 00b5b2b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4038:8"]]
- 00b5b2b4 bytes e75700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5868fe776fae256fa243b7a422b3b7e9"></a>

### [`00b5b51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b51c.md) → [`00b5b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b944.md) _ZN8firebase8callback10InitializeEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3d0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md)
- 新版 呼出元 1件 [`00c5b7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7d0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5b9a4",
      "incomplete_value": false,
      "site": "00b5b9a4",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b57c",
      "incomplete_value": false,
      "site": "00b5b57c",
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
            "const:bf0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5b9ac",
      "incomplete_value": true,
      "site": "00b5b9ac",
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
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b584",
      "incomplete_value": true,
      "site": "00b5b584",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5b95c",
      "incomplete_value": true,
      "site": "00b5b960",
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b534",
      "incomplete_value": true,
      "site": "00b5b538",
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
                "const:be0:8"
              ]
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
      "00b5b958",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5b968",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5b99c",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b5b958",
      "READ",
      [
        "storage",
        "01125fe0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5b968",
      "READ",
      [
        "storage",
        "01125fe8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5b99c",
      "READ",
      [
        "storage",
        "01125fe8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b51c.md#insn-00b5b538) · [`00b5b57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b51c.md#insn-00b5b57c) · [`00b5b584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b51c.md#insn-00b5b584)
- 新版 `00b5b960`（命令位置の公開資料なし） · `00b5b9a4`（命令位置の公開資料なし） · `00b5b9ac`（命令位置の公開資料なし）

~~~diff
- 00b5b538 ["INT_ADD", "register:40f0:8", ["const:b5b538:8", "const:4:8"]]
- 00b5b538 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5b960 ["INT_ADD", "register:40f0:8", ["const:b5b960:8", "const:4:8"]]
+ 00b5b960 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5b538 bytes 32fc0394
+ 00b5b960 bytes 28fc0394
- 00b5b57c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bf0:8"]]
- 00b5b57c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00b5b9a4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ff0:8"]]
+ 00b5b9a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00b5b57c bytes 34f905f9
+ 00b5b9a4 bytes 34f907f9
- 00b5b584 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:be8:8"]]
- 00b5b584 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b5b9ac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:fe8:8"]]
+ 00b5b9ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b5b584 bytes a8ea0bb9
+ 00b5b9ac bytes a8ea0fb9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d835b8250fa5f5710cd8410608b11fd"></a>

### [`00b5b70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b70c.md) → [`00b5bb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5bb34.md) FUN_00b5bb34

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00b5b5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b5b0.md) [`00b5bae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bae4.md) [`00b5bc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bc10.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md)
- 新版 呼出元 3件 [`00b5b9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b9d8.md) [`00b5bf0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5bf0c.md) [`00b5c038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c038.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5bb68",
      "incomplete_value": true,
      "site": "00b5bb68",
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
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b740",
      "incomplete_value": true,
      "site": "00b5b740",
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
            "const:be8:8"
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
      "definition_site": "00b5bb88",
      "incomplete_value": true,
      "site": "00b5bb88",
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
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b760",
      "incomplete_value": true,
      "site": "00b5b760",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5bb9c",
      "incomplete_value": false,
      "site": "00b5bb9c",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b774",
      "incomplete_value": false,
      "site": "00b5b774",
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
            "const:bf0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5bb48",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bb5c",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5bb68",
      "WRITE",
      [
        "storage",
        "01125be8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b5bb48",
      "READ",
      [
        "storage",
        "01125fe0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bb5c",
      "READ",
      [
        "storage",
        "01125fe8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5bb68",
      "WRITE",
      [
        "storage",
        "01125fe8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b70c.md#insn-00b5b72c) · [`00b5b740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b70c.md#insn-00b5b740) · [`00b5b750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b70c.md#insn-00b5b750)
- 新版 `00b5bb54`（命令位置の公開資料なし） · `00b5bb68`（命令位置の公開資料なし） · `00b5bb78`（命令位置の公開資料なし）

~~~diff
- 00b5b72c ["INT_ADD", "register:40f0:8", ["const:b5b72c:8", "const:4:8"]]
- 00b5b72c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5bb54 ["INT_ADD", "register:40f0:8", ["const:b5bb54:8", "const:4:8"]]
+ 00b5bb54 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5b72c bytes b5fb0394
+ 00b5bb54 bytes abfb0394
- 00b5b740 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:be8:8"]]
- 00b5b740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
+ 00b5bb68 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:fe8:8"]]
+ 00b5bb68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
- 00b5b740 bytes a1ea0bb9
+ 00b5bb68 bytes a1ea0fb9
- 00b5b750 ["INT_ADD", "register:40f0:8", ["const:b5b750:8", "const:4:8"]]
- 00b5b750 ["CALL", null, ["callee:00c5b130:8"]]
+ 00b5bb78 ["INT_ADD", "register:40f0:8", ["const:b5bb78:8", "const:4:8"]]
+ 00b5bb78 ["CALL", null, ["callee:00c5b130:8"]]
- 00b5b750 bytes 78fd0394
+ 00b5bb78 bytes 6efd0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b8ccd013c7ff194d4c28613153360a1"></a>

### [`00b5b7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b7cc.md) → [`00b5bbf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5bbf4.md) _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5b6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6f0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md) [`00c5b710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b710.md)
- 新版 呼出元 1件 [`00c5baf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5baf0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md) [`00c5bb10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bb10.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 84.78% / 新版 84.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5bc68",
      "incomplete_value": true,
      "site": "00b5bc68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b840",
      "incomplete_value": true,
      "site": "00b5b840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5bc74",
      "incomplete_value": true,
      "site": "00b5bc74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b84c",
      "incomplete_value": true,
      "site": "00b5b84c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5bc14",
      "incomplete_value": true,
      "site": "00b5bc18",
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b7ec",
      "incomplete_value": true,
      "site": "00b5b7f0",
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
                "const:be0:8"
              ]
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
      "00b5bc0c",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bc1c",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bc2c",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b5bc0c",
      "READ",
      [
        "storage",
        "01125fe0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bc1c",
      "READ",
      [
        "storage",
        "01125fe0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bc2c",
      "READ",
      [
        "storage",
        "01125fe8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b7cc.md#insn-00b5b7f0) · [`00b5b7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b7cc.md#insn-00b5b7fc) · [`00b5b840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b7cc.md#insn-00b5b840)
- 新版 `00b5bc18`（命令位置の公開資料なし） · `00b5bc24`（命令位置の公開資料なし） · `00b5bc68`（命令位置の公開資料なし）

~~~diff
- 00b5b7f0 ["INT_ADD", "register:40f0:8", ["const:b5b7f0:8", "const:4:8"]]
- 00b5b7f0 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5bc18 ["INT_ADD", "register:40f0:8", ["const:b5bc18:8", "const:4:8"]]
+ 00b5bc18 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5b7f0 bytes 84fb0394
+ 00b5bc18 bytes 7afb0394
- 00b5b7fc ["INT_ADD", "register:40f0:8", ["const:b5b7fc:8", "const:4:8"]]
- 00b5b7fc ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5bc24 ["INT_ADD", "register:40f0:8", ["const:b5bc24:8", "const:4:8"]]
+ 00b5bc24 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5b7fc bytes 81fb0394
+ 00b5bc24 bytes 77fb0394
- 00b5b840 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:bf0:8"]]
- 00b5b840 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
+ 00b5bc68 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:ff0:8"]]
+ 00b5bc68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 00b5b840 bytes f6fa05f9
+ 00b5bc68 bytes f6fa07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a95e7fb3dcdff016b93a4d907650456"></a>

### [`00b5bae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bae4.md) → [`00b5bf0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5bf0c.md) _ZN8firebase8callback14RemoveCallbackEPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b5b70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b70c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b5bb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5bb34.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.33% / 新版 85.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5bf90",
      "incomplete_value": true,
      "site": "00b5bf90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5bb68",
      "incomplete_value": true,
      "site": "00b5bb68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5bf9c",
      "incomplete_value": true,
      "site": "00b5bf9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5bb74",
      "incomplete_value": true,
      "site": "00b5bb74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5bf30",
      "incomplete_value": true,
      "site": "00b5bf34",
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5bb08",
      "incomplete_value": true,
      "site": "00b5bb0c",
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
                "const:be0:8"
              ]
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
      "00b5bf28",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bf3c",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5bf48",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5bf28",
      "READ",
      [
        "storage",
        "01125fe0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bf3c",
      "READ",
      [
        "storage",
        "01125fe8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5bf48",
      "READ",
      [
        "storage",
        "01125fe0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5bb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bae4.md#insn-00b5bb0c) · [`00b5bb28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bae4.md#insn-00b5bb28) · [`00b5bb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bae4.md#insn-00b5bb68)
- 新版 `00b5bf34`（命令位置の公開資料なし） · `00b5bf50`（命令位置の公開資料なし） · `00b5bf90`（命令位置の公開資料なし）

~~~diff
- 00b5bb0c ["INT_ADD", "register:40f0:8", ["const:b5bb0c:8", "const:4:8"]]
- 00b5bb0c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5bf34 ["INT_ADD", "register:40f0:8", ["const:b5bf34:8", "const:4:8"]]
+ 00b5bf34 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5bb0c bytes bdfa0394
+ 00b5bf34 bytes b3fa0394
- 00b5bb28 ["INT_ADD", "register:40f0:8", ["const:b5bb28:8", "const:4:8"]]
- 00b5bb28 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5bf50 ["INT_ADD", "register:40f0:8", ["const:b5bf50:8", "const:4:8"]]
+ 00b5bf50 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5bb28 bytes b6fa0394
+ 00b5bf50 bytes acfa0394
- 00b5bb68 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:bf0:8"]]
- 00b5bb68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
+ 00b5bf90 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:ff0:8"]]
+ 00b5bf90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 00b5bb68 bytes 36fb05f9
+ 00b5bf90 bytes 36fb07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff29c224f40c52668a5b522b478e9e8b"></a>

### [`00b5bc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bc10.md) → [`00b5c038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c038.md) _ZN8firebase8callback13PollCallbacksEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00b5b70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b70c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58220.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00b5bb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5bb34.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58620.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 79.66% / 新版 79.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5c0b4",
      "incomplete_value": true,
      "site": "00b5c0b4",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5bc8c",
      "incomplete_value": true,
      "site": "00b5bc8c",
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
            "const:bf0:8"
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
      "definition_site": "00b5c0c0",
      "incomplete_value": true,
      "site": "00b5c0c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5bc98",
      "incomplete_value": true,
      "site": "00b5bc98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5c0dc",
      "incomplete_value": false,
      "site": "00b5c0dc",
      "value": [
        "leaf",
        "const:1126000:8"
      ]
    },
    "old": {
      "definition_site": "00b5bcb4",
      "incomplete_value": false,
      "site": "00b5bcb4",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5c050",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c060",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5c06c",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5c050",
      "READ",
      [
        "storage",
        "01125fe0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c060",
      "READ",
      [
        "storage",
        "01125fe8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5c06c",
      "READ",
      [
        "storage",
        "01125fe0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5bc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bc10.md#insn-00b5bc30) · [`00b5bc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bc10.md#insn-00b5bc4c) · [`00b5bc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bc10.md#insn-00b5bc8c)
- 新版 `00b5c058`（命令位置の公開資料なし） · `00b5c074`（命令位置の公開資料なし） · `00b5c0b4`（命令位置の公開資料なし）

~~~diff
- 00b5bc30 ["INT_ADD", "register:40f0:8", ["const:b5bc30:8", "const:4:8"]]
- 00b5bc30 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5c058 ["INT_ADD", "register:40f0:8", ["const:b5c058:8", "const:4:8"]]
+ 00b5c058 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5bc30 bytes 74fa0394
+ 00b5c058 bytes 6afa0394
- 00b5bc4c ["INT_ADD", "register:40f0:8", ["const:b5bc4c:8", "const:4:8"]]
- 00b5bc4c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5c074 ["INT_ADD", "register:40f0:8", ["const:b5c074:8", "const:4:8"]]
+ 00b5c074 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5bc4c bytes 6dfa0394
+ 00b5c074 bytes 63fa0394
- 00b5bc8c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:bf0:8"]]
- 00b5bc8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 00b5c0b4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ff0:8"]]
+ 00b5c0b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b5bc8c bytes d5fa05f9
+ 00b5c0b4 bytes d5fa07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-341d42472011d17e883338cc419680c2"></a>

### [`00b5be34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5be34.md) → [`00b5c25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c25c.md) _ZN8firebase8callback18CallbackDispatcherD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b740.md) · 呼出先 6件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6a0.md)
- 新版 呼出元 1件 [`00c5bb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bb40.md) · 呼出先 6件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaa0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 89.47% / 新版 87.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5bf84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5c3ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c288",
      "incomplete_value": false,
      "site": "00b5c28c",
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
            "const:162:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5be60",
      "incomplete_value": false,
      "site": "00b5be64",
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
            "const:122:8"
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
      "00b5c288",
      "PARAM",
      [
        "storage",
        "002ae122",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5bf84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5c390"
      ]
    ]
  ],
  "added": [
    [
      "00b5c288",
      "PARAM",
      [
        "storage",
        "002ae162",
        null,
        "string"
      ]
    ],
    [
      "00b5c3ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5c390"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5be64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5be34.md#insn-00b5be64) · [`00b5bf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5be34.md#insn-00b5bf84)
- 新版 `00b5c28c`（命令位置の公開資料なし） · `00b5c3ac`（命令位置の公開資料なし）

~~~diff
- 00b5be64 ["INT_ADD", "register:40f0:8", ["const:b5be64:8", "const:4:8"]]
- 00b5be64 ["CALL", null, ["callee:00c5ade0:8"]]
+ 00b5c28c ["INT_ADD", "register:40f0:8", ["const:b5c28c:8", "const:4:8"]]
+ 00b5c28c ["CALL", null, ["callee:00c5ade0:8"]]
- 00b5be64 bytes dffa0394
+ 00b5c28c bytes d5fa0394
- 00b5bf84 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b5bf84 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00b5bf84 bytes 35ffffb4
+ 00b5c3ac ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00b5c3ac ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00b5c3ac bytes 35ffffb4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74d4b1860b38c31d6c76135deb291ac5"></a>

### [`00b5c048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c048.md) → [`00b5c470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c470.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c06c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5c494"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c090"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c060",
      "READ",
      [
        "storage",
        "00c9b388",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b5c06c",
      "DATA",
      [
        "storage",
        "00c8ff18",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "unmatched:00b5c090",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5c4a8"
      ]
    ]
  ],
  "added": [
    [
      "00b5c488",
      "READ",
      [
        "storage",
        "00c9b788",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c494",
      "DATA",
      [
        "storage",
        "00c90318",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00b5c4b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5c4a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c048.md#insn-00b5c06c) · [`00b5c074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c048.md#insn-00b5c074) · [`00b5c090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c048.md#insn-00b5c090)
- 新版 `00b5c49c`（命令位置の公開資料なし）

~~~diff
- 00b5c06c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b5c06c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5c06c bytes 080000f9
- 00b5c074 ["INT_ADD", "register:40f0:8", ["const:b5c074:8", "const:4:8"]]
- 00b5c074 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5c49c ["INT_ADD", "register:40f0:8", ["const:b5c49c:8", "const:4:8"]]
+ 00b5c49c ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5c074 bytes 63f90394
+ 00b5c49c bytes 59f90394
- 00b5c090 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b5c090 ["CBRANCH", null, ["local:b1:8", "tmp:0:1"]]
- 00b5c090 bytes 95ffffb4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e26275ca1b0cc6a77a37669cfcce102"></a>

### [`00b5c13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c13c.md) → [`00b5c564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c564.md) _ZN8firebase8callback16BlockingCallbackD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b780.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bb80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

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
      "site": "00b5c15c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5c584"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c588",
      "incomplete_value": true,
      "site": "00b5c58c",
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
            "register:4040:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c160",
      "incomplete_value": true,
      "site": "00b5c164",
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
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c150",
      "READ",
      [
        "storage",
        "00c9b380",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b5c15c",
      "DATA",
      [
        "storage",
        "00c8ff68",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b5c578",
      "READ",
      [
        "storage",
        "00c9b780",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c584",
      "DATA",
      [
        "storage",
        "00c90368",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c13c.md#insn-00b5c15c) · [`00b5c164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c13c.md#insn-00b5c164)
- 新版 `00b5c58c`（命令位置の公開資料なし） · `00b5c584`（命令位置の公開資料なし）

~~~diff
- 00b5c15c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b5c15c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b5c15c bytes 090000f9
- 00b5c164 ["INT_ADD", "register:40f0:8", ["const:b5c164:8", "const:4:8"]]
- 00b5c164 ["CALL", null, ["callee:00c5bb80:8"]]
+ 00b5c58c ["INT_ADD", "register:40f0:8", ["const:b5c58c:8", "const:4:8"]]
+ 00b5c58c ["CALL", null, ["callee:00c5bb80:8"]]
- 00b5c164 bytes 87fd0394
+ 00b5c58c bytes 7dfd0394
+ 00b5c584 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00b5c584 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00b5c584 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cc46f1eaacdc741749ac056fff0cd53"></a>

### [`00b5c190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c190.md) → [`00b5c5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c5b8.md) _ZN8firebase8callback16BlockingCallbackD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b780.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bb80.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5c5d4",
      "incomplete_value": true,
      "site": "00b5c5d8",
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
      "definition_site": "00b5c1ac",
      "incomplete_value": true,
      "site": "00b5c1b0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5c5cc",
      "READ",
      [
        "storage",
        "00c9b380",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c5d8",
      "DATA",
      [
        "storage",
        "00c8ff68",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b5c5cc",
      "READ",
      [
        "storage",
        "00c9b780",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c5d8",
      "DATA",
      [
        "storage",
        "00c90368",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c190.md#insn-00b5c1a4) · [`00b5c1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c190.md#insn-00b5c1b8) · [`00b5c1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c190.md#insn-00b5c1cc)
- 新版 `00b5c5cc`（命令位置の公開資料なし） · `00b5c5e0`（命令位置の公開資料なし） · `00b5c5f4`（命令位置の公開資料なし）

~~~diff
- 00b5c1a4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:380:8"]]
- 00b5c1a4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5c5cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:780:8"]]
+ 00b5c5cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5c1a4 bytes 29c141f9
+ 00b5c5cc bytes 29c143f9
- 00b5c1b8 ["INT_ADD", "register:40f0:8", ["const:b5c1b8:8", "const:4:8"]]
- 00b5c1b8 ["CALL", null, ["callee:00c5bb80:8"]]
+ 00b5c5e0 ["INT_ADD", "register:40f0:8", ["const:b5c5e0:8", "const:4:8"]]
+ 00b5c5e0 ["CALL", null, ["callee:00c5bb80:8"]]
- 00b5c1b8 bytes 72fd0394
+ 00b5c5e0 bytes 68fd0394
- 00b5c1cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5c1cc ["INT_ADD", "register:40f0:8", ["const:b5c1cc:8", "const:4:8"]]
- 00b5c1cc ["CALLIND", null, ["register:0:8"]]
+ 00b5c5f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c5f4 ["INT_ADD", "register:40f0:8", ["const:b5c5f4:8", "const:4:8"]]
+ 00b5c5f4 ["CALLIND", null, ["register:0:8"]]
- 00b5c1cc bytes 00013fd6
+ 00b5c5f4 bytes 00013fd6
~~~


<a id="compare-c7a828ee82bb6c0437bc8ddeb9a79095"></a>

### [`00b5c1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c1e0.md) → [`00b5c608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c608.md) _ZN8firebase8callback16BlockingCallback3RunEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-21679e1d78da9cc4860ed89d0b8f603a"></a>

### [`00b5c1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c1f0.md) → [`00b5c618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c618.md) _ZN8firebase8callback13CallbackEntry7ExecuteEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b700.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5bb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bb00.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 6.67% / 新版 6.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c1f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c1f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c1f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c1f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c1f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c1f8",
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
      "00b5c618",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5c61c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5c620",
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

- 旧版 [`00b5c1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c1f0.md#insn-00b5c1f0) · [`00b5c1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c1f0.md#insn-00b5c1f4) · [`00b5c1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c1f0.md#insn-00b5c1f8)

~~~diff
- 00b5c1f0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5c1f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5c1f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5c1f0 bytes f50f1df8
- 00b5c1f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5c1f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5c1f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5c1f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c1f4 bytes f44f01a9
- 00b5c1f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5c1f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5c1f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5c1f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c1f8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72d01b4eeaf57f388e45872949195a13"></a>

### [`00b5c2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c2b8.md) → [`00b5c6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c6e0.md) _INIT_280

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.33% / 新版 53.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c2b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c2bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c2bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c2b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c2bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c2e4",
      "WRITE",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5c6e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5c6e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5c70c",
      "WRITE",
      [
        "storage",
        "01125fe0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c2b8.md#insn-00b5c2b8) · [`00b5c2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c2b8.md#insn-00b5c2bc) · [`00b5c2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c2b8.md#insn-00b5c2d4)
- 新版 `00b5c6fc`（命令位置の公開資料なし）

~~~diff
- 00b5c2b8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b5c2b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b5c2b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5c2b8 bytes f30f1ef8
- 00b5c2bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5c2bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5c2bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5c2bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c2bc bytes fd7b01a9
- 00b5c2d4 ["INT_ADD", "register:40f0:8", ["const:b5c2d4:8", "const:4:8"]]
- 00b5c2d4 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00b5c6fc ["INT_ADD", "register:40f0:8", ["const:b5c6fc:8", "const:4:8"]]
+ 00b5c6fc ["CALL", null, ["callee:00c5ac80:8"]]
- 00b5c2d4 bytes 6bf90394
+ 00b5c6fc bytes 61f90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

