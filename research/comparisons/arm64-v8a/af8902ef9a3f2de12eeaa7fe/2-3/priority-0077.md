# v16.0.0 → v16.0.1 · 最優先の変更候補 (77)

[一覧の目次](README.md)

<a id="compare-d09d3ab5fcb5fd737760a8e8c3461e0f"></a>

### [`00b83eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b83/00b83eec.md) → [`00b84314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b84/00b84314.md) _ZN11flatbuffers6Parser9StartEnumERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEbPPNS_7EnumDefE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c3e0.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5c7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c7e0.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 75.00% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b84370",
      "incomplete_value": true,
      "site": "00b843a4",
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
                "const:ed8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b83f48",
      "incomplete_value": true,
      "site": "00b83f7c",
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
                "const:e98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b83fcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b843f4"
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
      "00b84370",
      "READ",
      [
        "storage",
        "002c3e98",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b83fcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84418"
      ]
    ],
    [
      "00b84464",
      "PARAM",
      [
        "storage",
        "002ad291",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b84370",
      "READ",
      [
        "storage",
        "002c3ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b843f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84418"
      ]
    ],
    [
      "00b84464",
      "PARAM",
      [
        "storage",
        "002ad2d1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b83/00b83eec.md#insn-00b83fcc) · [`00b84048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b83/00b83eec.md#insn-00b84048) · [`00b8405c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b83/00b83eec.md#insn-00b8405c)
- 新版 `00b84470`（命令位置の公開資料なし） · `00b84484`（命令位置の公開資料なし）

~~~diff
- 00b83fcc ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b83fcc bytes 20010054
- 00b84048 ["INT_ADD", "register:40f0:8", ["const:b84048:8", "const:4:8"]]
- 00b84048 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b84470 ["INT_ADD", "register:40f0:8", ["const:b84470:8", "const:4:8"]]
+ 00b84470 ["CALL", null, ["callee:00c580b0:8"]]
- 00b84048 bytes 1a4f0394
+ 00b84470 bytes 104f0394
- 00b8405c ["INT_ADD", "register:40f0:8", ["const:b8405c:8", "const:4:8"]]
- 00b8405c ["CALL", null, ["callee:00c580b0:8"]]
+ 00b84484 ["INT_ADD", "register:40f0:8", ["const:b84484:8", "const:4:8"]]
+ 00b84484 ["CALL", null, ["callee:00c580b0:8"]]
- 00b8405c bytes 154f0394
+ 00b84484 bytes 0b4f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bebd82e5c330c7723e34f97a4da3fc6"></a>

### [`00b84114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84114.md) → [`00b8453c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b84/00b8453c.md) _ZN11flatbuffers6Parser16ParseProtoOptionEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c220.md) · 呼出先 3件 [`00c5c160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c160.md) [`00c5c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2f0.md) [`00c5c350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c350.md)
- 新版 呼出元 1件 [`00c5c620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c620.md) · 呼出先 3件 [`00c5c560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c560.md) [`00c5c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6f0.md) [`00c5c750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c750.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 75.00% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8412c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84114.md#insn-00b8412c) · [`00b8413c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84114.md#insn-00b8413c) · [`00b84148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84114.md#insn-00b84148)
- 新版 `00b84554`（命令位置の公開資料なし） · `00b84564`（命令位置の公開資料なし） · `00b84570`（命令位置の公開資料なし）

~~~diff
- 00b8412c ["INT_ADD", "register:40f0:8", ["const:b8412c:8", "const:4:8"]]
- 00b8412c ["CALL", null, ["callee:00c5c6f0:8"]]
+ 00b84554 ["INT_ADD", "register:40f0:8", ["const:b84554:8", "const:4:8"]]
+ 00b84554 ["CALL", null, ["callee:00c5c6f0:8"]]
- 00b8412c bytes 71600394
+ 00b84554 bytes 67600394
- 00b8413c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b8413c ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00b84564 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b84564 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b8413c bytes 08060035
+ 00b84564 bytes 08060035
- 00b84148 ["INT_ADD", "register:40f0:8", ["const:b84148:8", "const:4:8"]]
- 00b84148 ["CALL", null, ["callee:00c5c560:8"]]
+ 00b84570 ["INT_ADD", "register:40f0:8", ["const:b84570:8", "const:4:8"]]
+ 00b84570 ["CALL", null, ["callee:00c5c560:8"]]
- 00b84148 bytes 06600394
+ 00b84570 bytes fc5f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f45232194a67f1d79ceb58ee845342b"></a>

### [`00b8420c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b8420c.md) → [`00b84634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b84/00b84634.md) _ZN11flatbuffers14EnumValBuilder21AssignEnumeratorValueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bd90.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5bdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bdb0.md)
- 新版 呼出元 1件 [`00c5c190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c190.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5c1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 72.50% / 新版 82.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b842c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b846e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b84738",
      "incomplete_value": false,
      "site": "00b84744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b5d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84310",
      "incomplete_value": false,
      "site": "00b8431c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b1d:8"
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
      "unmatched:00b84310",
      "PARAM",
      [
        "storage",
        "002c0b1d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b84324",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ],
    [
      "unmatched:00b84358",
      "PARAM",
      [
        "storage",
        "002a0ae9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b84738",
      "PARAM",
      [
        "storage",
        "002c0b5d",
        null,
        "string"
      ]
    ],
    [
      "00b8474c",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ],
    [
      "00b84780",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b842c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b8420c.md#insn-00b842c0) · [`00b8431c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b8420c.md#insn-00b8431c) · [`00b84334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b8420c.md#insn-00b84334)
- 新版 `00b84744`（命令位置の公開資料なし） · `00b8475c`（命令位置の公開資料なし）

~~~diff
- 00b842c0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b842c0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b842c0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b842c0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:1:8"]]
- 00b842c0 bytes 2115949a
- 00b8431c ["INT_ADD", "register:40f0:8", ["const:b8431c:8", "const:4:8"]]
- 00b8431c ["CALL", null, ["callee:00c580b0:8"]]
+ 00b84744 ["INT_ADD", "register:40f0:8", ["const:b84744:8", "const:4:8"]]
+ 00b84744 ["CALL", null, ["callee:00c580b0:8"]]
- 00b8431c bytes 654e0394
+ 00b84744 bytes 5b4e0394
- 00b84334 ["INT_ADD", "register:40f0:8", ["const:b84334:8", "const:4:8"]]
- 00b84334 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b8475c ["INT_ADD", "register:40f0:8", ["const:b8475c:8", "const:4:8"]]
+ 00b8475c ["CALL", null, ["callee:00c57f80:8"]]
- 00b84334 bytes 134e0394
+ 00b8475c bytes 094e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-345152775228c2852522b478ef701c11"></a>

### [`00b84598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84598.md) → [`00b849c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b84/00b849c0.md) _ZN11flatbuffers6Parser11StartStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPPNS_9StructDefE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c100.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5c500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c500.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.83% / 新版 96.83%

CFGの説明率　旧版 82.50% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8461c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b84a44"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b84af4",
      "incomplete_value": false,
      "site": "00b84b04",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b846cc",
      "incomplete_value": false,
      "site": "00b846dc",
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
            "const:a3b:8"
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
      "unmatched:00b8461c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84a68"
      ]
    ],
    [
      "unmatched:00b846cc",
      "PARAM",
      [
        "storage",
        "0029fa3b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b84700",
      "PARAM",
      [
        "storage",
        "002a0ae9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b84a44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84a68"
      ]
    ],
    [
      "00b84af4",
      "PARAM",
      [
        "storage",
        "0029fb08",
        null,
        "string"
      ]
    ],
    [
      "00b84b28",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8461c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84598.md#insn-00b8461c) · [`00b846dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84598.md#insn-00b846dc) · [`00b84708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84598.md#insn-00b84708)
- 新版 `00b84b04`（命令位置の公開資料なし） · `00b84b30`（命令位置の公開資料なし）

~~~diff
- 00b8461c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b8461c bytes 20010054
- 00b846dc ["INT_ADD", "register:40f0:8", ["const:b846dc:8", "const:4:8"]]
- 00b846dc ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b84b04 ["INT_ADD", "register:40f0:8", ["const:b84b04:8", "const:4:8"]]
+ 00b84b04 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b846dc bytes 3d510394
+ 00b84b04 bytes 33510394
- 00b84708 ["INT_ADD", "register:40f0:8", ["const:b84708:8", "const:4:8"]]
- 00b84708 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b84b30 ["INT_ADD", "register:40f0:8", ["const:b84b30:8", "const:4:8"]]
+ 00b84b30 ["CALL", null, ["callee:00c580b0:8"]]
- 00b84708 bytes 6a4d0394
+ 00b84b30 bytes 604d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba0f4a98f8ecf687a8bb063660993bf9"></a>

### [`00b84790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84790.md) → [`00b84bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b84/00b84bb8.md) _ZN11flatbuffers6Parser10CheckClashERNSt6__ndk16vectorIPNS_8FieldDefENS1_9allocatorIS4_EEEEPNS_9StructDefEPKcNS_8BaseTypeE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c040.md) · 呼出先 10件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5c440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c440.md) · 呼出先 10件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.53% / 新版 95.53%

CFGの説明率　旧版 52.78% / 新版 48.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b847bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b847d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b84be4"
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
      "unmatched:00b847bc",
      "WRITE",
      [
        "storage",
        "Stack[-0xe8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b847d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b84934",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84e80"
      ]
    ]
  ],
  "added": [
    [
      "00b84be4",
      "WRITE",
      [
        "storage",
        "Stack[-0xe8]",
        null,
        null
      ]
    ],
    [
      "00b84bfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b84d5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84e80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b847bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84790.md#insn-00b847bc) · [`00b847d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84790.md#insn-00b847d4) · [`00b84844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84790.md#insn-00b84844)
- 新版 `00b84c6c`（命令位置の公開資料なし）

~~~diff
- 00b847bc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b847bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b847bc bytes e80f00f9
- 00b847d4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b847d4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa8:8"]]
- 00b847d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b847d4 bytes a8831af8
- 00b84844 ["INT_ADD", "register:40f0:8", ["const:b84844:8", "const:4:8"]]
- 00b84844 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00b84c6c ["INT_ADD", "register:40f0:8", ["const:b84c6c:8", "const:4:8"]]
+ 00b84c6c ["CALL", null, ["callee:00c57fe0:8"]]
- 00b84844 bytes e74c0394
+ 00b84c6c bytes dd4c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e51a808d6fdbf080cc9f7bcc9d7521bc"></a>

### [`00b84a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84a5c.md) → [`00b84e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b84/00b84e84.md) _ZNK11flatbuffers6Parser16GetIncludedFilesEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5c660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c660.md) [`00c5cbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cbf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca60.md) [`00c5cff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cff0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_condition` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b84a84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b84eac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "CONDITIONAL_JUMP",
        "00b84a84"
      ],
      [
        "CONDITIONAL_JUMP",
        "00b84eac"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b84ea8",
      "incomplete_value": true,
      "site": "00b84ec8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4040:8"
              ],
              [
                "live",
                "register:4000:8"
              ]
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
      "definition_site": "00b84a80",
      "incomplete_value": true,
      "site": "00b84aa0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
              [
                "live",
                "register:4000:8"
              ]
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
      "unmatched:00b84a84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84ec8"
      ]
    ]
  ],
  "added": [
    [
      "00b84eac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84ec8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84a5c.md#insn-00b84a84) · [`00b84a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84a5c.md#insn-00b84a78)
- 新版 `00b84eac`（命令位置の公開資料なし） · `00b84ea0`（命令位置の公開資料なし）

~~~diff
- 00b84a84 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00b84a84 bytes e0000054
+ 00b84eac ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00b84eac bytes e0000054
- 00b84a78 ["INT_ADD", "register:40f0:8", ["const:b84a78:8", "const:4:8"]]
- 00b84a78 ["CALL", null, ["callee:00c5ca60:8"]]
+ 00b84ea0 ["INT_ADD", "register:40f0:8", ["const:b84ea0:8", "const:4:8"]]
+ 00b84ea0 ["CALL", null, ["callee:00c5ca60:8"]]
- 00b84a78 bytes fa5e0394
+ 00b84ea0 bytes f05e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a800d3c68659faceea05f102cf8e3dbe"></a>

### [`00b84ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84ab4.md) → [`00b84edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b84/00b84edc.md) _ZNSt6__ndk16vectorIN11flatbuffers12IncludedFileENS_9allocatorIS2_EEEC2INS_21__tree_const_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEEET_NS_9en

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cbf0.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)
- 新版 呼出元 1件 [`00c5cff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cff0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 39.47% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b84b08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b84b44"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b84b8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b84b08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84f44"
      ]
    ],
    [
      "unmatched:00b84b44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84f58"
      ]
    ],
    [
      "unmatched:00b84b8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b85018"
      ]
    ]
  ],
  "added": [
    [
      "00b84f30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84f44"
      ]
    ],
    [
      "00b84f6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84f58"
      ]
    ],
    [
      "00b84fb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b85018"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84ab4.md#insn-00b84b08) · [`00b84b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84ab4.md#insn-00b84b44) · [`00b84b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84ab4.md#insn-00b84b8c)

~~~diff
- 00b84b08 ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 00b84b08 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b84b08 bytes ab0000b4
- 00b84b44 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b84b44 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b84b44 bytes 61ffff54
- 00b84b8c ["CBRANCH", null, ["local:b25:8", "register:101:1"]]
- 00b84b8c bytes 20030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbd707dbcf05fe4a07548403fdf22238"></a>

### [`00b84c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84c0c.md) → [`00b85034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b85/00b85034.md) _ZN11flatbuffers6Parser23SupportsOptionalScalarsERKNS_10IDLOptionsE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-ecb5de2b72eb81d36080dbca3ab4cfbf"></a>

### [`00b84e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84e84.md) → [`00b852ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b85/00b852ac.md) _ZN11flatbuffers6Parser15UnqualifiedNameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c1e0.md) · 呼出先 7件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c5b250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b250.md)
- 新版 呼出元 1件 [`00c5c5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5e0.md) · 呼出先 7件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c5b650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b650.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 44.83% / 新版 46.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 6件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b84edc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b84ee0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b84ee4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b84ee4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b853e0"
      ]
    ],
    [
      "unmatched:00b84f90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b853e4"
      ]
    ]
  ],
  "added": [
    [
      "00b8530c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b853e0"
      ]
    ],
    [
      "00b853b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b853e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84e84.md#insn-00b84edc) · [`00b84ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84e84.md#insn-00b84ee0) · [`00b84ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84e84.md#insn-00b84ee4)

~~~diff
- 00b84edc ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b84edc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b84edc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b84edc ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00b84edc bytes 6201899a
- 00b84ee0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b84ee0 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b84ee0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b84ee0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:1:8"]]
- 00b84ee0 bytes 5715939a
- 00b84ee4 ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
- 00b84ee4 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00b84ee4 bytes a20600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99b04fb07381c10cefe9886e69a02e77"></a>

### [`00b85014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85014.md) → [`00b8543c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b85/00b8543c.md) _ZN11flatbuffers6Parser9ParseDeclEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c390.md) · 呼出先 30件 [`0054a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) [`00b76904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md) [`00b85e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85e84.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5c790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c790.md) · 呼出先 30件 [`0054a614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md) [`00b76d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76d2c.md) [`00b862ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b86/00b862ac.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.14% / 新版 78.14%

CFGの説明率　旧版 59.12% / 新版 59.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件, `store_condition` 1件, `store_value` 4件, `unresolved_branch_alignment` 22件, `unresolved_call_alignment` 16件, `unresolved_store_alignment` 45件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85048"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b85568",
      "incomplete_value": true,
      "site": "00b85598",
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
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:6a9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b85140",
      "incomplete_value": true,
      "site": "00b85170",
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
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:669:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b852c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b85048",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b85054",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b854d8"
      ]
    ],
    [
      "unmatched:00b85078",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b862a8"
      ]
    ]
  ],
  "added": [
    [
      "00b85470",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00b8547c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b854d8"
      ]
    ],
    [
      "00b854a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b862a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b85048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85014.md#insn-00b85048) · [`00b85130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85014.md#insn-00b85130) · [`00b852c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85014.md#insn-00b852c0)
- 新版 `00b85558`（命令位置の公開資料なし）

~~~diff
- 00b85048 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b85048 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffff98:8"]]
- 00b85048 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b85048 bytes a98319f8
- 00b85130 ["INT_ADD", "register:40f0:8", ["const:b85130:8", "const:4:8"]]
- 00b85130 ["CALL", null, ["callee:00c58050:8"]]
+ 00b85558 ["INT_ADD", "register:40f0:8", ["const:b85558:8", "const:4:8"]]
+ 00b85558 ["CALL", null, ["callee:00c58050:8"]]
- 00b85130 bytes c84a0394
+ 00b85558 bytes be4a0394
- 00b852c0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:40:8"]]
- 00b852c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b852c0 bytes 282300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0430aafe74b0b5e03d75034a6e0c1d25"></a>

### [`00b85e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85e84.md) → [`00b862ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b86/00b862ac.md) FUN_00b862ac

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b85014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85014.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a530.md) [`00c5c670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c670.md)
- 新版 呼出元 1件 [`00b8543c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b85/00b8543c.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a930.md) [`00c5ca70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 8.00% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85ef4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85f64"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b8631c"
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
      "00b8630c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b85eec"
      ]
    ],
    [
      "unmatched:00b85ef4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b85f00"
      ]
    ],
    [
      "unmatched:00b85efc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b85f04"
      ]
    ]
  ],
  "added": [
    [
      "00b8630c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b86314"
      ]
    ],
    [
      "00b8631c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b86328"
      ]
    ],
    [
      "00b86324",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8632c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b85ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85e84.md#insn-00b85ef4) · [`00b85f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85e84.md#insn-00b85f04) · [`00b85f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85e84.md#insn-00b85f18)
- 新版 `00b86340`（命令位置の公開資料なし）

~~~diff
- 00b85ef4 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 00b85ef4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b85ef4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b85ef4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b85ef4 bytes 6a000037
- 00b85f04 ["INT_ADD", "register:40f0:8", ["const:b85f04:8", "const:4:8"]]
- 00b85f04 ["CALL", null, ["callee:00c5a930:8"]]
- 00b85f04 bytes 8b510394
- 00b85f18 ["INT_ADD", "register:40f0:8", ["const:b85f18:8", "const:4:8"]]
- 00b85f18 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b86340 ["INT_ADD", "register:40f0:8", ["const:b86340:8", "const:4:8"]]
+ 00b86340 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b85f18 bytes e6460394
+ 00b86340 bytes dc460394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ee06324c4ac2952f76471e850240ab2"></a>

### [`00b85fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85fbc.md) → [`00b863e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b86/00b863e4.md) _ZN11flatbuffers6Parser12ParseServiceEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c110.md) · 呼出先 21件 [`0054a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`00c5c510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c510.md) · 呼出先 21件 [`0054a614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.72% / 新版 91.72%

CFGの説明率　旧版 66.67% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_value` 3件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86248"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8624c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86254"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b861f8",
      "READ",
      [
        "storage",
        "002c3e98",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b86260",
      "WRITE",
      [
        "storage",
        "Stack[-0x148]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b86278",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b866c4"
      ]
    ]
  ],
  "added": [
    [
      "00b86620",
      "READ",
      [
        "storage",
        "002c3ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b86688",
      "WRITE",
      [
        "storage",
        "Stack[-0x148]",
        null,
        null
      ]
    ],
    [
      "00b866a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b866c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85fbc.md#insn-00b86248) · [`00b8624c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85fbc.md#insn-00b8624c) · [`00b86250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85fbc.md#insn-00b86250)

~~~diff
- 00b86248 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8c:8"]]
- 00b86248 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 00b86248 bytes 08c008fc
- 00b8624c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b8624c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b8624c ["INT_ADD", "register:4050:8", ["register:4050:8", "const:a8:8"]]
- 00b8624c ["STORE", null, ["const:1b1:8", "register:4050:8", "tmp:1:8"]]
- 00b8624c bytes 5f8d0af8
- 00b86250 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b86250 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b86250 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b86250 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b86250 bytes 2101889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea1bb46c30e7e8f346613039077f28ff"></a>

### [`00b86a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86a1c.md) → [`00b86e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b86/00b86e44.md) _ZN11flatbuffers11SymbolTableINS_10ServiceDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc40.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5c040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c040.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 63.64% / 新版 56.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86a80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86bac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b86ea8"
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
      "unmatched:00b86a80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b86ed4"
      ]
    ],
    [
      "unmatched:00b86bac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b86ff8"
      ]
    ]
  ],
  "added": [
    [
      "00b86ea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b86ed4"
      ]
    ],
    [
      "00b86fd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b86ff8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86a1c.md#insn-00b86a80) · [`00b86b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86a1c.md#insn-00b86b48) · [`00b86bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86a1c.md#insn-00b86bac)
- 新版 `00b86f70`（命令位置の公開資料なし）

~~~diff
- 00b86a80 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00b86a80 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b86a80 bytes 6a0100b5
- 00b86b48 ["INT_ADD", "register:40f0:8", ["const:b86b48:8", "const:4:8"]]
- 00b86b48 ["CALL", null, ["callee:00c5b5b0:8"]]
+ 00b86f70 ["INT_ADD", "register:40f0:8", ["const:b86f70:8", "const:4:8"]]
+ 00b86f70 ["CALL", null, ["callee:00c5b5b0:8"]]
- 00b86b48 bytes 9a510394
+ 00b86f70 bytes 90510394
- 00b86bac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b86bac ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 00b86bac bytes 21010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e30cfd13e35cb2be3fdf8684464550f"></a>

### [`00b86bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86bd4.md) → [`00b86ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b86/00b86ffc.md) _ZN11flatbuffers11SymbolTableINS_7RPCCallEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc90.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5c090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c090.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 55.56% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 5件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86c84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b870ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86ce4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b86ce4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b87178"
      ]
    ]
  ],
  "added": [
    [
      "00b8710c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b87178"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86bd4.md#insn-00b86c84) · [`00b86ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86bd4.md#insn-00b86ce4) · [`00b86cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86bd4.md#insn-00b86cf0)
- 新版 `00b87118`（命令位置の公開資料なし）

~~~diff
- 00b86c84 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b86c84 ["COPY", "tmp:1:8", ["register:40e0:8"]]
- 00b86c84 ["INT_ADD", "register:40e0:8", ["register:40e0:8", "const:8:8"]]
- 00b86c84 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b86c84 bytes 938700f8
- 00b86ce4 ["INT_NOTEQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b86ce4 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00b86ce4 bytes 760300b5
- 00b86cf0 ["INT_ADD", "register:40f0:8", ["const:b86cf0:8", "const:4:8"]]
- 00b86cf0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b87118 ["INT_ADD", "register:40f0:8", ["const:b87118:8", "const:4:8"]]
+ 00b87118 ["CALL", null, ["callee:00c57e90:8"]]
- 00b86cf0 bytes 68430394
+ 00b87118 bytes 5e430394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26f01ad6c056232d005330d99b774b76"></a>

### [`00b86d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86d8c.md) → [`00b871b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b87/00b871b4.md) _ZN11flatbuffers6Parser11SetRootTypeEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c0f0.md) · 呼出先 8件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5c4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c4f0.md) · 呼出先 8件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.81% / 新版 88.81%

CFGの説明率　旧版 52.08% / 新版 56.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86dc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86dc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b86dc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b86dc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b86dc8",
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
      "00b871e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b871ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00b871f0",
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

- 旧版 [`00b86dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86d8c.md#insn-00b86dc0) · [`00b86dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86d8c.md#insn-00b86dc4) · [`00b86dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86d8c.md#insn-00b86dc8)

~~~diff
- 00b86dc0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b86dc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b86dc0 bytes e81f00f9
- 00b86dc4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b86dc4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b86dc4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b86dc4 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b86dc4 bytes ffff02a9
- 00b86dc8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b86dc8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b86dc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b86dc8 bytes ff1300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aba2531b1bffd04034227759dccd6c90"></a>

### [`00b870bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b870bc.md) → [`00b874e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b87/00b874e4.md) _ZN11flatbuffers6Parser14ParseNamespaceEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c180.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)
- 新版 呼出元 1件 [`00c5c580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c580.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 67.50% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b870cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b870cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b870d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b870cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b870d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b871e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b87628"
      ]
    ]
  ],
  "added": [
    [
      "00b874f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b874f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b8760c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b87628"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b870cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b870bc.md#insn-00b870cc) · [`00b870d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b870bc.md#insn-00b870d0) · [`00b87114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b870bc.md#insn-00b87114)
- 新版 `00b8753c`（命令位置の公開資料なし）

~~~diff
- 00b870cc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b870cc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b870cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b870cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b870cc bytes f44f04a9
- 00b870d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b870d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b870d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b870d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b870d0 bytes fd7b05a9
- 00b87114 ["INT_ADD", "register:40f0:8", ["const:b87114:8", "const:4:8"]]
- 00b87114 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b8753c ["INT_ADD", "register:40f0:8", ["const:b8753c:8", "const:4:8"]]
+ 00b8753c ["CALL", null, ["callee:00c57e90:8"]]
- 00b87114 bytes 5f420394
+ 00b8753c bytes 55420394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-652ddffc6acfe2fab75b92f08636d3ce"></a>

### [`00b8729c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b8729c.md) → [`00b876c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b87/00b876c4.md) _ZN11flatbuffers6Parser14ParseProtoDeclEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c190.md) · 呼出先 25件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5c590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c590.md) · 呼出先 25件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.80% / 新版 94.80%

CFGの説明率　旧版 81.82% / 新版 82.80%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b872cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b875d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b875d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b872cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b87310",
      "PARAM",
      [
        "storage",
        "002b267e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b87330",
      "PARAM",
      [
        "storage",
        "002b3618",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b876f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b87738",
      "PARAM",
      [
        "storage",
        "002b26be",
        null,
        "string"
      ]
    ],
    [
      "00b87758",
      "PARAM",
      [
        "storage",
        "002b3658",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b872cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b8729c.md#insn-00b872cc) · [`00b874a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b8729c.md#insn-00b874a0) · [`00b875d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b8729c.md#insn-00b875d4)

~~~diff
- 00b872cc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b872cc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa8:8"]]
- 00b872cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b872cc bytes a9831af8
- 00b874a0 ["CBRANCH", null, ["local:b161:8", "register:102:1"]]
- 00b874a0 bytes e2430054
- 00b875d4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b875d4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b875d4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b875d4 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b875d4 bytes ffff02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f7ca5585315c89b5f4b46431892c3bf"></a>

### [`00b87d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b87d20.md) → [`00b88148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b88/00b88148.md) _ZN11flatbuffers6Parser16ParseProtoFieldsEPNS_9StructDefEbb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b87d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b87d20.md) [`00c5c210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c210.md) · 呼出先 35件 [`00b87d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b87d20.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 2件 [`00b88148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b88/00b88148.md) [`00c5c610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c610.md) · 呼出先 35件 [`00b88148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b88/00b88148.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 90.06% / 新版 90.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b87df0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b87df8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b87e00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b87df0",
      "WRITE",
      [
        "storage",
        "Stack[-0x2f0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b87df8",
      "WRITE",
      [
        "storage",
        "Stack[-0x2f8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b87e00",
      "WRITE",
      [
        "storage",
        "Stack[-0x310]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b88218",
      "WRITE",
      [
        "storage",
        "Stack[-0x2f0]",
        null,
        null
      ]
    ],
    [
      "00b88220",
      "WRITE",
      [
        "storage",
        "Stack[-0x2f8]",
        null,
        null
      ]
    ],
    [
      "00b88228",
      "WRITE",
      [
        "storage",
        "Stack[-0x310]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b87df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b87d20.md#insn-00b87df0) · [`00b87df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b87d20.md#insn-00b87df8) · [`00b87e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b87/00b87d20.md#insn-00b87e00)

~~~diff
- 00b87df0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:80:8"]]
- 00b87df0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b87df0 bytes e84300f9
- 00b87df8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:78:8"]]
- 00b87df8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b87df8 bytes e93f00f9
- 00b87e00 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b87e00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b87e00 bytes e83300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b484343a0414b772ed90fc6ef8d4ed63"></a>

### [`00b895e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b895e4.md) → [`00b89a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b89/00b89a0c.md) _ZN11flatbuffers11SymbolTableINS_7EnumDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc70.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5c070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c070.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 88.24% / 新版 90.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b895e4.md#insn-00b89668) · [`00b89674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b895e4.md#insn-00b89674) · [`00b89680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b895e4.md#insn-00b89680)
- 新版 `00b89a90`（命令位置の公開資料なし） · `00b89a9c`（命令位置の公開資料なし） · `00b89aa8`（命令位置の公開資料なし）

~~~diff
- 00b89668 ["INT_EQUAL", "tmp:0:1", ["register:40d8:8", "const:0:8"]]
- 00b89668 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
+ 00b89a90 ["INT_EQUAL", "tmp:0:1", ["register:40d8:8", "const:0:8"]]
+ 00b89a90 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00b89668 bytes db0600b4
+ 00b89a90 bytes db0600b4
- 00b89674 ["INT_ADD", "register:40f0:8", ["const:b89674:8", "const:4:8"]]
- 00b89674 ["CALL", null, ["callee:00c5b140:8"]]
+ 00b89a9c ["INT_ADD", "register:40f0:8", ["const:b89a9c:8", "const:4:8"]]
+ 00b89a9c ["CALL", null, ["callee:00c5b140:8"]]
- 00b89674 bytes b3450394
+ 00b89a9c bytes a9450394
- 00b89680 ["INT_ADD", "register:40f0:8", ["const:b89680:8", "const:4:8"]]
- 00b89680 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b89aa8 ["INT_ADD", "register:40f0:8", ["const:b89aa8:8", "const:4:8"]]
+ 00b89aa8 ["CALL", null, ["callee:00c57e90:8"]]
- 00b89680 bytes 04390394
+ 00b89aa8 bytes fa380394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-065f71e1db5320d298a1aa62f4754b4e"></a>

### [`00b8979c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b8979c.md) → [`00b89bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b89/00b89bc4.md) _ZN11flatbuffers6Parser18ParseProtoMapFieldEPNS_9StructDefE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c270.md) · 呼出先 15件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5c670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c670.md) · 呼出先 15件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.88% / 新版 90.88%

CFGの説明率　旧版 44.57% / 新版 43.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b898b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b89978"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b89a58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b898b8",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b898bc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b89d4c"
      ]
    ],
    [
      "unmatched:00b89978",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b89ce0",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ],
    [
      "00b89ce4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b89d4c"
      ]
    ],
    [
      "00b89da0",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b89888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b8979c.md#insn-00b89888) · [`00b898b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b8979c.md#insn-00b898b8) · [`00b89978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b8979c.md#insn-00b89978)
- 新版 `00b89cb0`（命令位置の公開資料なし）

~~~diff
- 00b89888 ["INT_ADD", "register:40f0:8", ["const:b89888:8", "const:4:8"]]
- 00b89888 ["CALL", null, ["callee:00c5c750:8"]]
+ 00b89cb0 ["INT_ADD", "register:40f0:8", ["const:b89cb0:8", "const:4:8"]]
+ 00b89cb0 ["CALL", null, ["callee:00c5c750:8"]]
- 00b89888 bytes b24a0394
+ 00b89cb0 bytes a84a0394
- 00b898b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:80:8"]]
- 00b898b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b898b8 bytes e023803d
- 00b89978 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b89978 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b89978 bytes e01b803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0906f47bdc1b70db3fe778a985730051"></a>

### [`00b89cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89cc0.md) → [`00b8a0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8a0e8.md) _ZN11flatbuffers6Parser22ParseTypeFromProtoTypeEPNS_4TypeE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2c0.md) · 呼出先 5件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5c1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c1a0.md) [`00c5c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2f0.md)
- 新版 呼出元 1件 [`00c5c6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6c0.md) · 呼出先 5件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5c5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5a0.md) [`00c5c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.59% / 新版 95.59%

CFGの説明率　旧版 40.91% / 新版 40.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b89d04"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b8a12c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b89d18",
      "incomplete_value": true,
      "site": "00b89d1c",
      "value": [
        "live",
        "register:40b8:8"
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
      "00b8a138",
      "READ",
      [
        "storage",
        "00c90468",
        null,
        "pointer"
      ]
    ],
    [
      "00b8a140",
      "PARAM",
      [
        "storage",
        "002bbe42",
        null,
        "string"
      ]
    ],
    [
      "00b8a140",
      "PARAM",
      [
        "storage",
        "002ae233",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b8a138",
      "READ",
      [
        "storage",
        "00c90868",
        null,
        "pointer"
      ]
    ],
    [
      "00b8a140",
      "PARAM",
      [
        "storage",
        "002bbe82",
        null,
        "string"
      ]
    ],
    [
      "00b8a140",
      "PARAM",
      [
        "storage",
        "002ae273",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b89d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89cc0.md#insn-00b89d04) · [`00b89d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89cc0.md#insn-00b89d1c)
- 新版 `00b8a144`（命令位置の公開資料なし） · `00b8a12c`（命令位置の公開資料なし）

~~~diff
- 00b89d04 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b89d04 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b89d04 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b89d04 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00b89d04 bytes 3601889a
- 00b89d1c ["INT_ADD", "register:40f0:8", ["const:b89d1c:8", "const:4:8"]]
- 00b89d1c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00b8a144 ["INT_ADD", "register:40f0:8", ["const:b8a144:8", "const:4:8"]]
+ 00b8a144 ["CALL", null, ["callee:00c57fe0:8"]]
- 00b89d1c bytes b1370394
+ 00b8a144 bytes a7370394
+ 00b8a12c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b8a12c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b8a12c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b8a12c ["COPY", "register:40b0:8", ["tmp:0:8"]]
+ 00b8a12c bytes 3601889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b2e2ea4c8b1848b5b9f08af02282e96"></a>

### [`00b89dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89dd0.md) → [`00b8a1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8a1f8.md) _ZN11flatbuffers6Parser13ParseProtoKeyEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c160.md) · 呼出先 2件 [`00c5c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2f0.md) [`00c5c350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c350.md)
- 新版 呼出元 1件 [`00c5c560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c560.md) · 呼出先 2件 [`00c5c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6f0.md) [`00c5c750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c750.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 14.29% / 新版 16.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b89dd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b89dd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b89dd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b89dd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b89dd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b89dd8",
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
      "00b8a1f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b8a1fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b8a200",
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

- 旧版 [`00b89dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89dd0.md#insn-00b89dd0) · [`00b89dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89dd0.md#insn-00b89dd4) · [`00b89dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89dd0.md#insn-00b89dd8)

~~~diff
- 00b89dd0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b89dd0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b89dd0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b89dd0 bytes f50f1df8
- 00b89dd4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b89dd4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b89dd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b89dd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b89dd4 bytes f44f01a9
- 00b89dd8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b89dd8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b89dd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b89dd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b89dd8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33422d7fdc11782dffc43fdf7128cf00"></a>

### [`00b89ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89ed8.md) → [`00b8a300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8a300.md) _ZN11flatbuffers14EnumValBuilder16AcceptEnumeratorERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bd80.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5bc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc80.md) [`00c5bd70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bd70.md)
- 新版 呼出元 1件 [`00c5c180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c180.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5c080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c080.md) [`00c5c170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c170.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 53.33% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b89f00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b8a328"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b89f10",
      "incomplete_value": true,
      "site": "00b89f1c",
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
            "const:80:8"
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
      "unmatched:00b89f00",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b89f50",
      "PARAM",
      [
        "storage",
        "002aa80e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b89f64",
      "PARAM",
      [
        "storage",
        "002a0ae9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b8a328",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b8a378",
      "PARAM",
      [
        "storage",
        "002aa8db",
        null,
        "string"
      ]
    ],
    [
      "00b8a38c",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b89f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89ed8.md#insn-00b89f00) · [`00b89f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89ed8.md#insn-00b89f1c) · [`00b89f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89ed8.md#insn-00b89f70)
- 新版 `00b8a344`（命令位置の公開資料なし） · `00b8a398`（命令位置の公開資料なし）

~~~diff
- 00b89f00 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b89f00 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b89f00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b89f00 bytes a8831df8
- 00b89f1c ["INT_ADD", "register:40f0:8", ["const:b89f1c:8", "const:4:8"]]
- 00b89f1c ["CALL", null, ["callee:00c5c170:8"]]
+ 00b8a344 ["INT_ADD", "register:40f0:8", ["const:b8a344:8", "const:4:8"]]
+ 00b8a344 ["CALL", null, ["callee:00c5c170:8"]]
- 00b89f1c bytes 95470394
+ 00b8a344 bytes 8b470394
- 00b89f70 ["INT_ADD", "register:40f0:8", ["const:b89f70:8", "const:4:8"]]
- 00b89f70 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b8a398 ["INT_ADD", "register:40f0:8", ["const:b8a398:8", "const:4:8"]]
+ 00b8a398 ["CALL", null, ["callee:00c580b0:8"]]
- 00b89f70 bytes 50370394
+ 00b8a398 bytes 46370394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-803e326626e9c43aca88204fac2caf39"></a>

### [`00b89fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89fd8.md) → [`00b8a400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8a400.md) _ZN11flatbuffers6Parser30ParseFlexBufferNumericConstantEPN11flexbuffers7BuilderE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5c2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2e0.md) · 呼出先 6件 [`00b994c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b994c4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c581c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581c0.md)
- 新版 呼出元 1件 [`00c5c6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6e0.md) · 呼出先 6件 [`00b998ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b998ec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c585c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585c0.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a004"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b8a42c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8a470",
      "incomplete_value": false,
      "site": "00b8a47c",
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
            "const:724:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8a048",
      "incomplete_value": false,
      "site": "00b8a054",
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
            "const:6e4:8"
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
      "unmatched:00b8a004",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b8a470",
      "PARAM",
      [
        "storage",
        "002b46e4",
        null,
        "string"
      ]
    ],
    [
      "00b8a484",
      "PARAM",
      [
        "storage",
        "002a0ae9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b8a42c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b8a470",
      "PARAM",
      [
        "storage",
        "002b4724",
        null,
        "string"
      ]
    ],
    [
      "00b8a484",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8a004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89fd8.md#insn-00b8a004) · [`00b8a054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89fd8.md#insn-00b8a054) · [`00b8a068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89fd8.md#insn-00b8a068)
- 新版 `00b8a47c`（命令位置の公開資料なし） · `00b8a490`（命令位置の公開資料なし）

~~~diff
- 00b8a004 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b8a004 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b8a004 bytes e91f00f9
- 00b8a054 ["INT_ADD", "register:40f0:8", ["const:b8a054:8", "const:4:8"]]
- 00b8a054 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b8a47c ["INT_ADD", "register:40f0:8", ["const:b8a47c:8", "const:4:8"]]
+ 00b8a47c ["CALL", null, ["callee:00c580b0:8"]]
- 00b8a054 bytes 17370394
+ 00b8a47c bytes 0d370394
- 00b8a068 ["INT_ADD", "register:40f0:8", ["const:b8a068:8", "const:4:8"]]
- 00b8a068 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b8a490 ["INT_ADD", "register:40f0:8", ["const:b8a490:8", "const:4:8"]]
+ 00b8a490 ["CALL", null, ["callee:00c580b0:8"]]
- 00b8a068 bytes 12370394
+ 00b8a490 bytes 08370394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a159655734ed4aa9ad52938f3fa7f338"></a>

### [`00b8a110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8a110.md) → [`00b8a538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8a538.md) _ZN11flatbuffers6Parser20ParseFlexBufferValueEPN11flexbuffers7BuilderE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b8a110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8a110.md) [`00c5c2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2a0.md) · 呼出先 22件 [`00b8a110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8a110.md) [`00b994c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b994c4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00b8a538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8a538.md) [`00c5c6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6a0.md) · 呼出先 22件 [`00b8a538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8a538.md) [`00b998ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b998ec.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.70% / 新版 92.70%

CFGの説明率　旧版 72.22% / 新版 78.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 3件, `store_value` 6件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a114"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a114"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a118"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8a114",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8a118",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8a11c",
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
      "00b8a53c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b8a540",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b8a544",
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

- 旧版 [`00b8a114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8a110.md#insn-00b8a114) · [`00b8a118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8a110.md#insn-00b8a118) · [`00b8a11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8a110.md#insn-00b8a11c)

~~~diff
- 00b8a114 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b8a114 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b8a114 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b8a114 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8a114 bytes fc6f05a9
- 00b8a118 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b8a118 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b8a118 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b8a118 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8a118 bytes fa6706a9
- 00b8a11c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b8a11c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b8a11c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b8a11c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8a11c bytes f85f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a9209e82d21c6223f2faa24fbe4b2ea"></a>

### [`00b8aa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8aa0c.md) → [`00b8ae34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8ae34.md) _ZN11flexbuffers7Builder6EndMapEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c4d0.md) · 呼出先 8件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5c8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c8d0.md) · 呼出先 8件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 83.87% / 新版 78.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b8ab84",
      "incomplete_value": true,
      "site": "00b8ab90",
      "value": [
        "live",
        "register:40c0:8"
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b8ab88",
      "incomplete_value": true,
      "site": "00b8ab90",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b8ab8c",
      "incomplete_value": true,
      "site": "00b8ab90",
      "value": [
        "live",
        "register:40b8:8"
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b8ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8aa0c.md#insn-00b8ab90) · [`00b8aa7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8aa0c.md#insn-00b8aa7c) · [`00b8aa9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8aa0c.md#insn-00b8aa9c)
- 新版 `00b8afb8`（命令位置の公開資料なし） · `00b8aea4`（命令位置の公開資料なし） · `00b8aec4`（命令位置の公開資料なし）

~~~diff
- 00b8ab90 ["INT_ADD", "register:40f0:8", ["const:b8ab90:8", "const:4:8"]]
- 00b8ab90 ["CALL", null, ["callee:00c58000:8"]]
+ 00b8afb8 ["INT_ADD", "register:40f0:8", ["const:b8afb8:8", "const:4:8"]]
+ 00b8afb8 ["CALL", null, ["callee:00c58000:8"]]
- 00b8ab90 bytes 1c340394
+ 00b8afb8 bytes 12340394
- 00b8aa7c ["INT_ADD", "register:40f0:8", ["const:b8aa7c:8", "const:4:8"]]
- 00b8aa7c ["CALL", null, ["callee:00c5ce10:8"]]
+ 00b8aea4 ["INT_ADD", "register:40f0:8", ["const:b8aea4:8", "const:4:8"]]
+ 00b8aea4 ["CALL", null, ["callee:00c5ce10:8"]]
- 00b8aa7c bytes e5470394
+ 00b8aea4 bytes db470394
- 00b8aa9c ["INT_ADD", "register:40f0:8", ["const:b8aa9c:8", "const:4:8"]]
- 00b8aa9c ["CALL", null, ["callee:00c5c8b0:8"]]
+ 00b8aec4 ["INT_ADD", "register:40f0:8", ["const:b8aec4:8", "const:4:8"]]
+ 00b8aec4 ["CALL", null, ["callee:00c5c8b0:8"]]
- 00b8aa9c bytes 85460394
+ 00b8aec4 bytes 7b460394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-786afaed525934d4acd335b45180cb31"></a>

### [`00b8ad44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8ad44.md) → [`00b8b16c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8b16c.md) _ZN11flatbuffers6Parser15ParseFlexBufferEPKcS2_PN11flexbuffers7BuilderE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5c1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c1b0.md) [`00c5c2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2a0.md) [`00c5c4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c4e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5c5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5b0.md) [`00c5c6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6a0.md) [`00c5c8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c8e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 50.00% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8b1ec",
      "incomplete_value": true,
      "site": "00b8b1f0",
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
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8adc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b8b1e8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b8adc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8ad44.md#insn-00b8adc0) · [`00b8adc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8ad44.md#insn-00b8adc8)
- 新版 `00b8b1f0`（命令位置の公開資料なし） · `00b8b1e8`（命令位置の公開資料なし）

~~~diff
- 00b8adc0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b8adc0 ["RETURN", null, ["register:0:8"]]
- 00b8adc0 bytes c0035fd6
- 00b8adc8 ["INT_ADD", "register:40f0:8", ["const:b8adc8:8", "const:4:8"]]
- 00b8adc8 ["CALL", null, ["callee:00c5c8e0:8"]]
+ 00b8b1f0 ["INT_ADD", "register:40f0:8", ["const:b8b1f0:8", "const:4:8"]]
+ 00b8b1f0 ["CALL", null, ["callee:00c5c8e0:8"]]
- 00b8adc8 bytes c6450394
+ 00b8b1f0 bytes bc450394
+ 00b8b1e8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b8b1e8 ["RETURN", null, ["register:0:8"]]
+ 00b8b1e8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85e6e5ee10c6daf45b60d0e36b814a1c"></a>

### [`00b8add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8add8.md) → [`00b8b200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8b200.md) _ZN11flatbuffers6Parser14StartParseFileEPKcS2_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c1b0.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5c5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5b0.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 38.10% / 新版 34.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8aedc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b8b304"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b8ae68",
      "incomplete_value": true,
      "site": "00b8ae6c",
      "value": [
        "live",
        "register:40a0:8"
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
      "00b8b23c",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b8aeac",
      "READ",
      [
        "storage",
        "002a6041",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b8aec8",
      "PARAM",
      [
        "storage",
        "002a0ae9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b8b23c",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "00b8b2d4",
      "READ",
      [
        "storage",
        "002a611d",
        null,
        "string"
      ]
    ],
    [
      "00b8b2f0",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8ae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8add8.md#insn-00b8ae6c) · [`00b8aedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8add8.md#insn-00b8aedc) · [`00b8aee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8add8.md#insn-00b8aee4)
- 新版 `00b8b294`（命令位置の公開資料なし） · `00b8b30c`（命令位置の公開資料なし）

~~~diff
- 00b8ae6c ["INT_ADD", "register:40f0:8", ["const:b8ae6c:8", "const:4:8"]]
- 00b8ae6c ["CALL", null, ["callee:00c5c650:8"]]
+ 00b8b294 ["INT_ADD", "register:40f0:8", ["const:b8b294:8", "const:4:8"]]
+ 00b8b294 ["CALL", null, ["callee:00c5c650:8"]]
- 00b8ae6c bytes f9440394
+ 00b8b294 bytes ef440394
- 00b8aedc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:9:8"]]
- 00b8aedc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b8aedc bytes e093803c
- 00b8aee4 ["INT_ADD", "register:40f0:8", ["const:b8aee4:8", "const:4:8"]]
- 00b8aee4 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b8b30c ["INT_ADD", "register:40f0:8", ["const:b8b30c:8", "const:4:8"]]
+ 00b8b30c ["CALL", null, ["callee:00c580b0:8"]]
- 00b8aee4 bytes 73330394
+ 00b8b30c bytes 69330394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56981a07e20da358516e51fb13dfeb2c"></a>

### [`00b8af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8af50.md) → [`00b8b378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8b378.md) _ZN11flexbuffers7Builder6FinishEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c4e0.md) · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5c500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c500.md) [`00c5cc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc70.md) [`00c5cc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc80.md)
- 新版 呼出元 1件 [`00c5c8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c8e0.md) · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5c900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c900.md) [`00c5d070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d070.md) [`00c5d080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d080.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 52.38% / 新版 47.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8afc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b8b3e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8b4c0",
      "incomplete_value": true,
      "site": "00b8b4c4",
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
      "unmatched:00b8afc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8b420"
      ]
    ]
  ],
  "added": [
    [
      "00b8b3e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8b420"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8af50.md#insn-00b8afc0) · [`00b8b09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8af50.md#insn-00b8b09c)
- 新版 `00b8b4c4`（命令位置の公開資料なし） · `00b8b3e8`（命令位置の公開資料なし）

~~~diff
- 00b8afc0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b8afc0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b8afc0 bytes c3010054
- 00b8b09c ["INT_ADD", "register:40f0:8", ["const:b8b09c:8", "const:4:8"]]
- 00b8b09c ["CALL", null, ["callee:00c5d080:8"]]
+ 00b8b4c4 ["INT_ADD", "register:40f0:8", ["const:b8b4c4:8", "const:4:8"]]
+ 00b8b4c4 ["CALL", null, ["callee:00c5d080:8"]]
- 00b8b09c bytes f9460394
+ 00b8b4c4 bytes ef460394
+ 00b8b3e8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b8b3e8 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00b8b3e8 bytes c3010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-892667f9b0ad600c8f817d941bf8ec84"></a>

### [`00b8b0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8b0d0.md) → [`00b8b4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8b4f8.md) _ZN11flatbuffers6Parser9ParseRootEPKcPS2_S2_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c3c0.md) · 呼出先 17件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c5c7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c7c0.md) · 呼出先 17件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.89% / 新版 87.89%

CFGの説明率　旧版 55.83% / 新版 56.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_condition` 5件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b0d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b0d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b0d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8b0d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8b0d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8b0dc",
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
      "00b8b4fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b8b500",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b8b504",
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

- 旧版 [`00b8b0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8b0d0.md#insn-00b8b0d4) · [`00b8b0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8b0d0.md#insn-00b8b0d8) · [`00b8b0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8b0d0.md#insn-00b8b0dc)

~~~diff
- 00b8b0d4 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b8b0d4 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b8b0d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00b8b0d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8b0d4 bytes fc6f0fa9
- 00b8b0d8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b8b0d8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b8b0d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00b8b0d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8b0d8 bytes fa6710a9
- 00b8b0dc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b8b0dc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b8b0dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00b8b0dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8b0dc bytes f85f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2b6e33cbe4ca17e55a1d7269ce54570"></a>

### [`00b8b744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8b744.md) → [`00b8bb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8bb6c.md) _ZN11flatbuffers6Parser9ParseJsonEPKcS2_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5b610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b610.md) [`00c5c0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c0b0.md) [`00c5c1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c1b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5ba10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba10.md) [`00c5c4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c4b0.md) [`00c5c5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.51% / 新版 85.51%

CFGの説明率　旧版 18.75% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b758"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8b754",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8b758",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8b774",
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
      "00b8bb7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b8bb80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b8bb9c",
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

- 旧版 [`00b8b754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8b744.md#insn-00b8b754) · [`00b8b758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8b744.md#insn-00b8b758) · [`00b8b774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8b744.md#insn-00b8b774)

~~~diff
- 00b8b754 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b8b754 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b8b754 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b8b754 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8b754 bytes f44f05a9
- 00b8b758 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b8b758 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b8b758 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b8b758 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8b758 bytes fd7b06a9
- 00b8b774 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b8b774 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b8b774 bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-314cd2c963d2e9838bab81c6dc82c669"></a>

### [`00b8b858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8b858.md) → [`00b8bc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8bc80.md) _ZN11flatbuffers6Parser11DoParseJsonEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c0b0.md) · 呼出先 8件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5bf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf30.md)
- 新版 呼出元 1件 [`00c5c4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c4b0.md) · 呼出先 8件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5c330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c330.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.14% / 新版 80.14%

CFGの説明率　旧版 69.49% / 新版 65.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b87c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b8bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b8c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8b87c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8b888",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8bcfc"
      ]
    ],
    [
      "unmatched:00b8b8b0",
      "READ",
      [
        "storage",
        "002c2200",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b8bca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b8bcb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8bcfc"
      ]
    ],
    [
      "00b8bcd8",
      "READ",
      [
        "storage",
        "002c2240",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8b87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8b858.md#insn-00b8b87c) · [`00b8b888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8b858.md#insn-00b8b888) · [`00b8b8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8b858.md#insn-00b8b8bc)

~~~diff
- 00b8b87c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b8b87c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b8b87c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b8b87c bytes a9831df8
- 00b8b888 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b8b888 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b8b888 bytes 61020054
- 00b8b8bc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b8b8bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b8b8bc bytes e00b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa012d725c8107163152811cbf300875"></a>

### [`00b8ba8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8ba8c.md) → [`00b8beb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8beb4.md) _ZNK11flatbuffers6Parser13BytesConsumedEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-877ca20c248eb896b9c6297d1fb27667"></a>

### [`00b8ba9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8ba9c.md) → [`00b8bec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8bec4.md) _ZN11flatbuffers6Parser7DoParseEPKcPS2_S2_S2_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b8ba9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8ba9c.md) [`00c5c360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c360.md) · 呼出先 39件 [`0063947c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/0063947c.md) [`00b8ba9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8ba9c.md) [`00b8d690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d690.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00b8bec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8bec4.md) [`00c5c760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c760.md) · 呼出先 39件 [`006394bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/006394bc.md) [`00b8bec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8bec4.md) [`00b8dab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8d/00b8dab8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.18% / 新版 82.18%

CFGの説明率　旧版 40.53% / 新版 41.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 34件, `store_condition` 1件, `store_value` 4件, `unresolved_branch_alignment` 44件, `unresolved_call_alignment` 24件, `unresolved_store_alignment` 57件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8baa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8baa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8baa4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8baa0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8baa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8baa8",
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
      "00b8bec8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b8becc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b8bed0",
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

- 旧版 [`00b8baa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8ba9c.md#insn-00b8baa0) · [`00b8baa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8ba9c.md#insn-00b8baa4) · [`00b8baa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8ba9c.md#insn-00b8baa8)

~~~diff
- 00b8baa0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b8baa0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b8baa0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 00b8baa0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8baa0 bytes fc6f16a9
- 00b8baa4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b8baa4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b8baa4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 00b8baa4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8baa4 bytes fa6717a9
- 00b8baa8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b8baa8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b8baa8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 00b8baa8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8baa8 bytes f85f18a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88b64bd88719a20a5e113162828c9b22"></a>

### [`00b8d4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d4cc.md) → [`00b8d8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8d/00b8d8f4.md) _ZN11flatbuffers6Parser26CheckPrivatelyLeakedFieldsERKNS_10DefinitionES3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2d0.md) · 呼出先 6件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5c370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c370.md)
- 新版 呼出元 1件 [`00c5c6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6d0.md) · 呼出先 6件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5c770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c770.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.88% / 新版 77.88%

CFGの説明率　旧版 12.90% / 新版 6.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8d5d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8d5dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8d5e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8d544",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8d66c"
      ]
    ],
    [
      "unmatched:00b8d54c",
      "READ",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8d598",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8daa4"
      ]
    ]
  ],
  "added": [
    [
      "00b8d96c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8da94"
      ]
    ],
    [
      "00b8d974",
      "READ",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b8d9c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8daa4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8d538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d4cc.md#insn-00b8d538) · [`00b8d544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d4cc.md#insn-00b8d544) · [`00b8d58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d4cc.md#insn-00b8d58c)
- 新版 `00b8d960`（命令位置の公開資料なし） · `00b8d9b4`（命令位置の公開資料なし）

~~~diff
- 00b8d538 ["INT_ADD", "register:40f0:8", ["const:b8d538:8", "const:4:8"]]
- 00b8d538 ["CALL", null, ["callee:00c5ca70:8"]]
+ 00b8d960 ["INT_ADD", "register:40f0:8", ["const:b8d960:8", "const:4:8"]]
+ 00b8d960 ["CALL", null, ["callee:00c5ca70:8"]]
- 00b8d538 bytes 4e3c0394
+ 00b8d960 bytes 443c0394
- 00b8d544 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00b8d544 bytes 40090054
- 00b8d58c ["INT_ADD", "register:40f0:8", ["const:b8d58c:8", "const:4:8"]]
- 00b8d58c ["CALL", null, ["callee:00c5ca70:8"]]
+ 00b8d9b4 ["INT_ADD", "register:40f0:8", ["const:b8d9b4:8", "const:4:8"]]
+ 00b8d9b4 ["CALL", null, ["callee:00c5ca70:8"]]
- 00b8d58c bytes 393c0394
+ 00b8d9b4 bytes 2f3c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fef137c812e95b653562b3604700d140"></a>

### [`00b8d690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d690.md) → [`00b8dab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8d/00b8dab8.md) FUN_00b8dab8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8ba9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8b/00b8ba9c.md) · 呼出先 7件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00b8bec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8bec4.md) · 呼出先 7件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.08% / 新版 73.08%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8d694"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8d698"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8d698"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8d694",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8d698",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8d69c",
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
      "00b8dabc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b8dac0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b8dac4",
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

- 旧版 [`00b8d694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d690.md#insn-00b8d694) · [`00b8d698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d690.md#insn-00b8d698) · [`00b8d69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d690.md#insn-00b8d69c)

~~~diff
- 00b8d694 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b8d694 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b8d694 bytes f92300f9
- 00b8d698 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b8d698 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b8d698 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b8d698 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8d698 bytes f85f05a9
- 00b8d69c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b8d69c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b8d69c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b8d69c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8d69c bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2773d60a6034206c54aa31273b50170"></a>

### [`00b8d830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d830.md) → [`00b8dc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8d/00b8dc58.md) _ZNK11flatbuffers6Parser25GetIncludedFilesRecursiveERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0054a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) [`0054dc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dc10.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0054a614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md) [`0054dc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dc50.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 73.70% / 新版 73.70%

CFGの説明率　旧版 20.49% / 新版 24.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 1件, `unresolved_branch_alignment` 11件, `unresolved_store_alignment` 28件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8d868"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8d86c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8d870"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8d868",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8d874",
      "DATA",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8d878",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b8dc90",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b8dc9c",
      "DATA",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "00b8dca0",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8d868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d830.md#insn-00b8d868) · [`00b8d86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d830.md#insn-00b8d86c) · [`00b8d870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d830.md#insn-00b8d870)

~~~diff
- 00b8d868 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:58:8"]]
- 00b8d868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b8d868 bytes e82f00f9
- 00b8d86c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b8d86c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b8d86c ["INT_ADD", "register:40e0:8", ["register:40e0:8", "const:8:8"]]
- 00b8d86c ["STORE", null, ["const:1b1:8", "register:40e0:8", "tmp:1:8"]]
- 00b8d86c bytes 9f8f00f8
- 00b8d870 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00b8d870 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b8d870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b8d870 bytes 7f0a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77c58a4ff53e4468b166e6436e0d8c6c"></a>

### [`00b8dcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8dcb4.md) → [`00b8e0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8e/00b8e0dc.md) _ZN11flatbuffers6Parser9SerializeEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 32件 [`00540890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540890.md) [`0054a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) [`00bb0534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0534.md) [`00bb1218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1218.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 32件 [`005408d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408d0.md) [`0054a614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md) [`00bb095c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb095c.md) [`00bb1640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1640.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.47% / 新版 84.47%

CFGの説明率　旧版 47.13% / 新版 46.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 23件, `store_condition` 3件, `unresolved_branch_alignment` 27件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 23件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8dcb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8dcb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8dcbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8dcb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8dcbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8dcc0",
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
      "00b8e0e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b8e0e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b8e0e8",
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

- 旧版 [`00b8dcb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8dcb4.md#insn-00b8dcb8) · [`00b8dcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8dcb4.md#insn-00b8dcbc) · [`00b8dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8dcb4.md#insn-00b8dcc0)

~~~diff
- 00b8dcb8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b8dcb8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b8dcb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00b8dcb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8dcb8 bytes fc6f0ea9
- 00b8dcbc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b8dcbc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b8dcbc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00b8dcbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8dcbc bytes fa670fa9
- 00b8dcc0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b8dcc0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b8dcc0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00b8dcc0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8dcc0 bytes f85f10a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6302753cce10922d1d234169cf43004"></a>

### [`00b8e948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8e/00b8e948.md) → [`00b8ed70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8e/00b8ed70.md) _ZNK11flatbuffers9StructDef9SerializeEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c650.md) · 呼出先 13件 [`00b92a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a70.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5ca50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca50.md) · 呼出先 13件 [`00b92e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e98.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 95.38% / 新版 96.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8e994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8e/00b8e948.md#insn-00b8e994) · [`00b8e9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8e/00b8e948.md#insn-00b8e9c0) · [`00b8e9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8e/00b8e948.md#insn-00b8e9cc)
- 新版 `00b8edbc`（命令位置の公開資料なし） · `00b8ede8`（命令位置の公開資料なし） · `00b8edf4`（命令位置の公開資料なし）

~~~diff
- 00b8e994 ["CBRANCH", null, ["local:b20:8", "register:101:1"]]
+ 00b8edbc ["CBRANCH", null, ["local:b19:8", "register:101:1"]]
- 00b8e994 bytes c0070054
+ 00b8edbc bytes c0070054
- 00b8e9c0 ["INT_ADD", "register:40f0:8", ["const:b8e9c0:8", "const:4:8"]]
- 00b8e9c0 ["CALL", null, ["callee:00c5ca30:8"]]
+ 00b8ede8 ["INT_ADD", "register:40f0:8", ["const:b8ede8:8", "const:4:8"]]
+ 00b8ede8 ["CALL", null, ["callee:00c5ca30:8"]]
- 00b8e9c0 bytes 1c370394
+ 00b8ede8 bytes 12370394
- 00b8e9cc ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
+ 00b8edf4 ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
- 00b8e9cc bytes 82000054
+ 00b8edf4 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9ac834487b2fb2cee2ab010ba30b887"></a>

### [`00b8ec90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8e/00b8ec90.md) → [`00b8f0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8f/00b8f0b8.md) _ZNK11flatbuffers7EnumDef9SerializeEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c600.md) · 呼出先 22件 [`00b92a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a70.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5ca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca00.md) · 呼出先 22件 [`00b92e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e98.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 84.52% / 新版 81.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8eea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8eea4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8eea8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b8f22c",
      "READ",
      [
        "storage",
        "00c9b470",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b8f22c",
      "READ",
      [
        "storage",
        "00c9b870",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8eea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8e/00b8ec90.md#insn-00b8eea0) · [`00b8eea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8e/00b8ec90.md#insn-00b8eea4) · [`00b8eea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8e/00b8ec90.md#insn-00b8eea8)

~~~diff
- 00b8eea0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:40:8"]]
- 00b8eea0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b8eea0 bytes 892200f9
- 00b8eea4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:30:8"]]
- 00b8eea4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b8eea4 bytes 883200b9
- 00b8eea8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b8eea8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b8eea8 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00b8eea8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b8eea8 bytes 3f010039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f96a7f350a8855e36c983d1a8796ea00"></a>

### [`00b8f10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8f10c.md) → [`00b8f534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8f/00b8f534.md) _ZNK11flatbuffers10ServiceDef9SerializeEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c5c0.md) · 呼出先 19件 [`00b92a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a70.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5c9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c9c0.md) · 呼出先 19件 [`00b92e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e98.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 97.05% / 新版 97.05%

CFGの説明率　旧版 63.44% / 新版 62.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8f3bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b8f7e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8f1f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8f1f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8f630"
      ]
    ],
    [
      "00b8f6a8",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b8f3bc",
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
      "00b8f61c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8f630"
      ]
    ],
    [
      "00b8f6a8",
      "READ",
      [
        "storage",
        "00c9b878",
        null,
        "pointer"
      ]
    ],
    [
      "00b8f7e4",
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

- 旧版 [`00b8f1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8f10c.md#insn-00b8f1f4) · [`00b8f240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8f10c.md#insn-00b8f240) · [`00b8f25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8f10c.md#insn-00b8f25c)
- 新版 `00b8f668`（命令位置の公開資料なし）

~~~diff
- 00b8f1f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b8f1f4 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00b8f1f4 bytes ab000054
- 00b8f240 ["INT_ADD", "register:40f0:8", ["const:b8f240:8", "const:4:8"]]
- 00b8f240 ["CALL", null, ["callee:00c5ca40:8"]]
+ 00b8f668 ["INT_ADD", "register:40f0:8", ["const:b8f668:8", "const:4:8"]]
+ 00b8f668 ["CALL", null, ["callee:00c5ca40:8"]]
- 00b8f240 bytes 00350394
+ 00b8f668 bytes f6340394
- 00b8f25c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b8f25c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b8f25c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b8f25c ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b8f25c bytes 6101899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6bd19fe8c2677326c4953d8fdcbc1f0"></a>

### [`00b8f548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8f548.md) → [`00b8f970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8f/00b8f970.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE26CreateVectorOfSortedTablesIN10reflection10SchemaFileENSt6__ndk19allocatorINS_6OffsetIS4_EEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bed0.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a450.md) [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5c2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c2d0.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a850.md) [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 41.67% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8f9fc",
      "incomplete_value": true,
      "site": "00b8fa10",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8fa00",
      "incomplete_value": true,
      "site": "00b8fa10",
      "value": [
        "live",
        "register:40b0:8"
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
      "definition_site": "00b8f9f8",
      "incomplete_value": true,
      "site": "00b8fa10",
      "value": [
        "live",
        "register:8:8"
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
      "00b8f9a8",
      "READ",
      [
        "storage",
        "00c9b450",
        null,
        "pointer"
      ]
    ],
    [
      "00b8f9d0",
      "READ",
      [
        "storage",
        "00c9b120",
        null,
        "pointer"
      ]
    ],
    [
      "00b8f9e4",
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
      "00b8f9a8",
      "READ",
      [
        "storage",
        "00c9b850",
        null,
        "pointer"
      ]
    ],
    [
      "00b8f9d0",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ],
    [
      "00b8f9e4",
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

- 旧版 [`00b8f5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8f548.md#insn-00b8f5e8) · [`00b8f60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8f548.md#insn-00b8f60c) · [`00b8f628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8f548.md#insn-00b8f628)
- 新版 `00b8fa10`（命令位置の公開資料なし） · `00b8fa34`（命令位置の公開資料なし） · `00b8fa50`（命令位置の公開資料なし）

~~~diff
- 00b8f5e8 ["INT_ADD", "register:40f0:8", ["const:b8f5e8:8", "const:4:8"]]
- 00b8f5e8 ["CALL", null, ["callee:00c5caf0:8"]]
+ 00b8fa10 ["INT_ADD", "register:40f0:8", ["const:b8fa10:8", "const:4:8"]]
+ 00b8fa10 ["CALL", null, ["callee:00c5caf0:8"]]
- 00b8f5e8 bytes 42340394
+ 00b8fa10 bytes 38340394
- 00b8f60c ["INT_ADD", "register:40f0:8", ["const:b8f60c:8", "const:4:8"]]
- 00b8f60c ["CALL", null, ["callee:00c5caf0:8"]]
+ 00b8fa34 ["INT_ADD", "register:40f0:8", ["const:b8fa34:8", "const:4:8"]]
+ 00b8fa34 ["CALL", null, ["callee:00c5caf0:8"]]
- 00b8f60c bytes 39340394
+ 00b8fa34 bytes 2f340394
- 00b8f628 ["INT_ADD", "register:40f0:8", ["const:b8f628:8", "const:4:8"]]
- 00b8f628 ["CALL", null, ["callee:00c5c280:8"]]
+ 00b8fa50 ["INT_ADD", "register:40f0:8", ["const:b8fa50:8", "const:4:8"]]
+ 00b8fa50 ["CALL", null, ["callee:00c5c280:8"]]
- 00b8f628 bytes 16320394
+ 00b8fa50 bytes 0c320394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d1da01c075a4180cd0086078b03763d"></a>

### [`00b8f8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8f8f8.md) → [`00b8fd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8f/00b8fd20.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE26CreateVectorOfSortedTablesIN10reflection4EnumENSt6__ndk19allocatorINS_6OffsetIS4_EEEEEENS7_IN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bee0.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a450.md) [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5c2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c2e0.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a850.md) [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 46.67% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8fa10"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b8fe38"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b8f9c8",
      "incomplete_value": false,
      "site": "00b8f9d8",
      "value": [
        "leaf",
        "const:4:8"
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
      "00b8fd58",
      "READ",
      [
        "storage",
        "00c9b458",
        null,
        "pointer"
      ]
    ],
    [
      "00b8fd80",
      "READ",
      [
        "storage",
        "00c9b120",
        null,
        "pointer"
      ]
    ],
    [
      "00b8fd94",
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
      "00b8fd58",
      "READ",
      [
        "storage",
        "00c9b858",
        null,
        "pointer"
      ]
    ],
    [
      "00b8fd80",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ],
    [
      "00b8fd94",
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

- 旧版 [`00b8f9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8f8f8.md#insn-00b8f9d8) · [`00b8f9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8f8f8.md#insn-00b8f9f8) · [`00b8fa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8f8f8.md#insn-00b8fa10)
- 新版 `00b8fe00`（命令位置の公開資料なし） · `00b8fe20`（命令位置の公開資料なし）

~~~diff
- 00b8f9d8 ["INT_ADD", "register:40f0:8", ["const:b8f9d8:8", "const:4:8"]]
- 00b8f9d8 ["CALL", null, ["callee:00c5c280:8"]]
+ 00b8fe00 ["INT_ADD", "register:40f0:8", ["const:b8fe00:8", "const:4:8"]]
+ 00b8fe00 ["CALL", null, ["callee:00c5c280:8"]]
- 00b8f9d8 bytes 2a310394
+ 00b8fe00 bytes 20310394
- 00b8f9f8 ["INT_ADD", "register:40f0:8", ["const:b8f9f8:8", "const:4:8"]]
- 00b8f9f8 ["CALL", null, ["callee:00c5c250:8"]]
+ 00b8fe20 ["INT_ADD", "register:40f0:8", ["const:b8fe20:8", "const:4:8"]]
+ 00b8fe20 ["CALL", null, ["callee:00c5c250:8"]]
- 00b8f9f8 bytes 16310394
+ 00b8fe20 bytes 0c310394
- 00b8fa10 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b8fa10 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b8fa10 ["CBRANCH", null, ["local:b11:8", "tmp:1:1"]]
- 00b8fa10 bytes 48000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbb9d7726abe0fd661f4d27c930fc445"></a>

### [`00b8fad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8fad0.md) → [`00b8fef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8f/00b8fef8.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE26CreateVectorOfSortedTablesIN10reflection7ServiceENSt6__ndk19allocatorINS_6OffsetIS4_EEEEEENS7

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf10.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a450.md) [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5c310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c310.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a850.md) [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 34.29% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8fc3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b90064"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8fbfc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b8ff30",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "00b8ff58",
      "READ",
      [
        "storage",
        "00c9b120",
        null,
        "pointer"
      ]
    ],
    [
      "00b8ff6c",
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
      "00b8ff30",
      "READ",
      [
        "storage",
        "00c9b880",
        null,
        "pointer"
      ]
    ],
    [
      "00b8ff58",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ],
    [
      "00b8ff6c",
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

- 旧版 [`00b8fb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8fad0.md#insn-00b8fb94) · [`00b8fbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8fad0.md#insn-00b8fbfc) · [`00b8fc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8fad0.md#insn-00b8fc3c)
- 新版 `00b8ffbc`（命令位置の公開資料なし）

~~~diff
- 00b8fb94 ["INT_ADD", "register:40f0:8", ["const:b8fb94:8", "const:4:8"]]
- 00b8fb94 ["CALL", null, ["callee:00c5cb30:8"]]
+ 00b8ffbc ["INT_ADD", "register:40f0:8", ["const:b8ffbc:8", "const:4:8"]]
+ 00b8ffbc ["CALL", null, ["callee:00c5cb30:8"]]
- 00b8fb94 bytes e7320394
+ 00b8ffbc bytes dd320394
- 00b8fbfc ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00b8fbfc bytes 20feff54
- 00b8fc3c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b8fc3c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b8fc3c ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00b8fc3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b8fc3c bytes 3f010039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ee3a81b40c67ec02f80253b2425419d"></a>

### [`00b8fca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8fca8.md) → [`00b900d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b900d0.md) _ZN10reflection12CreateSchemaERN11flatbuffers21FlatBufferBuilderImplILb0EEENS0_6OffsetINS0_6VectorINS4_INS_6ObjectEEEjEEEENS4_INS5_INS4_INS_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb80.md) · 呼出先 9件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be70.md) [`00c5bf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf40.md) [`00c5bf60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf60.md) [`00c5bf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf70.md)
- 新版 呼出元 1件 [`00c5bf80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf80.md) · 呼出先 9件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c270.md) [`00c5c340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c340.md) [`00c5c360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c360.md) [`00c5c370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c370.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.95% / 新版 91.95%

CFGの説明率　旧版 15.38% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8fca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8fca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8fcac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8fca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8fcac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8fcb0",
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
      "00b900d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b900d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b900d8",
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

- 旧版 [`00b8fca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8fca8.md#insn-00b8fca8) · [`00b8fcac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8fca8.md#insn-00b8fcac) · [`00b8fcb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8fca8.md#insn-00b8fcb0)

~~~diff
- 00b8fca8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b8fca8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b8fca8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00b8fca8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b8fca8 bytes fc6fbaa9
- 00b8fcac ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b8fcac ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b8fcac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b8fcac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8fcac bytes fa6701a9
- 00b8fcb0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b8fcb0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b8fcb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b8fcb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8fcb0 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f303cff7386489f20d46e3cd7af64e36"></a>

### [`00b8fe04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8fe04.md) → [`00b9022c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b9022c.md) _ZNK11flatbuffers8FieldDef9SerializeEPNS_21FlatBufferBuilderImplILb0EEEtRKNS_6ParserE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c630.md) · 呼出先 9件 [`00b92a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a70.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c581c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581c0.md) [`00c5bb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb60.md)
- 新版 呼出元 1件 [`00c5ca30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca30.md) · 呼出先 9件 [`00b92e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e98.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c585c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585c0.md) [`00c5bf60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 19.51% / 新版 25.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8feec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8fffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b90314"
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
      "unmatched:00b8feec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b90334"
      ]
    ],
    [
      "00b90370",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b8ff58",
      "READ",
      [
        "storage",
        "01125de0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b90314",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b90334"
      ]
    ],
    [
      "00b90370",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ],
    [
      "00b90380",
      "READ",
      [
        "storage",
        "011261e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8fedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8fe04.md#insn-00b8fedc) · [`00b8feec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8fe04.md#insn-00b8feec) · [`00b8ff64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8fe04.md#insn-00b8ff64)
- 新版 `00b90304`（命令位置の公開資料なし） · `00b9038c`（命令位置の公開資料なし）

~~~diff
- 00b8fedc ["INT_ADD", "register:40f0:8", ["const:b8fedc:8", "const:4:8"]]
- 00b8fedc ["CALL", null, ["callee:00c585c0:8"]]
+ 00b90304 ["INT_ADD", "register:40f0:8", ["const:b90304:8", "const:4:8"]]
+ 00b90304 ["CALL", null, ["callee:00c585c0:8"]]
- 00b8fedc bytes b9200394
+ 00b90304 bytes af200394
- 00b8feec ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00b8feec bytes 00010054
- 00b8ff64 ["INT_ADD", "register:40f0:8", ["const:b8ff64:8", "const:4:8"]]
- 00b8ff64 ["CALL", null, ["callee:00c5d150:8"]]
+ 00b9038c ["INT_ADD", "register:40f0:8", ["const:b9038c:8", "const:4:8"]]
+ 00b9038c ["CALL", null, ["callee:00c5d150:8"]]
- 00b8ff64 bytes 7b330394
+ 00b9038c bytes 71330394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41ef2732d0ebb5f11b44dc4bda7be1cd"></a>

### [`00b9002c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b9002c.md) → [`00b90454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b90454.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE26CreateVectorOfSortedTablesIN10reflection5FieldENSt6__ndk19allocatorINS_6OffsetIS4_EEEEEENS7_I

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bef0.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a450.md) [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5c2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c2f0.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a850.md) [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 73.33% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b90144"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b9056c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b90120",
      "incomplete_value": true,
      "site": "00b9012c",
      "value": [
        "live",
        "register:4098:8"
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
      "00b9048c",
      "READ",
      [
        "storage",
        "00c9b460",
        null,
        "pointer"
      ]
    ],
    [
      "00b904b4",
      "READ",
      [
        "storage",
        "00c9b120",
        null,
        "pointer"
      ]
    ],
    [
      "00b904c8",
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
      "00b9048c",
      "READ",
      [
        "storage",
        "00c9b860",
        null,
        "pointer"
      ]
    ],
    [
      "00b904b4",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ],
    [
      "00b904c8",
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

- 旧版 [`00b9012c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b9002c.md#insn-00b9012c) · [`00b90144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b9002c.md#insn-00b90144)
- 新版 `00b90554`（命令位置の公開資料なし） · `00b9056c`（命令位置の公開資料なし）

~~~diff
- 00b9012c ["INT_ADD", "register:40f0:8", ["const:b9012c:8", "const:4:8"]]
- 00b9012c ["CALL", null, ["callee:00c5c250:8"]]
+ 00b90554 ["INT_ADD", "register:40f0:8", ["const:b90554:8", "const:4:8"]]
+ 00b90554 ["CALL", null, ["callee:00c5c250:8"]]
- 00b9012c bytes 492f0394
+ 00b90554 bytes 3f2f0394
- 00b90144 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b90144 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b90144 ["CBRANCH", null, ["local:b11:8", "tmp:1:1"]]
- 00b90144 bytes 48000054
+ 00b9056c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b9056c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b9056c ["CBRANCH", null, ["local:b14:8", "tmp:1:1"]]
+ 00b9056c bytes 48000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8f71caa8a2c834271164d8e3450770c"></a>

### [`00b90204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b90204.md) → [`00b9062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b9062c.md) _ZNK11flatbuffers10Definition19SerializeAttributesEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b92a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b92e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e98.md)

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
      "definition_site": "00b90214",
      "incomplete_value": true,
      "site": "00b9021c",
      "value": [
        "INT_AND",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:ffffffff:8"
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

- 旧版 [`00b90210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b90204.md#insn-00b90210)
- 新版 `00b90638`（命令位置の公開資料なし）

~~~diff
- 00b90210 ["INT_ADD", "register:40f0:8", ["const:b90210:8", "const:4:8"]]
- 00b90210 ["CALL", null, ["callee:00b92e98:8"]]
+ 00b90638 ["INT_ADD", "register:40f0:8", ["const:b90638:8", "const:4:8"]]
+ 00b90638 ["CALL", null, ["callee:00b92e98:8"]]
- 00b90210 bytes 180a0094
+ 00b90638 bytes 180a0094
~~~


<a id="compare-55eedb019619ee48e524da0abdc80ccf"></a>

### [`00b90220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b90220.md) → [`00b90648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b90648.md) _ZN10reflection12CreateObjectERN11flatbuffers21FlatBufferBuilderImplILb0EEENS0_6OffsetINS0_6StringEEENS4_INS0_6VectorINS4_INS_5FieldEEEjEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb70.md) · 呼出先 8件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5bde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bde0.md) [`00c5be40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be40.md) [`00c5bf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf40.md) [`00c5bf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf70.md)
- 新版 呼出元 1件 [`00c5bf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf70.md) · 呼出先 8件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1e0.md) [`00c5c240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c240.md) [`00c5c340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c340.md) [`00c5c370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c370.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 21.74% / 新版 17.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b90234"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b90234"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b90358"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b90234",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b90240",
      "READ",
      [
        "storage",
        "Stack[0x0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b90338",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b90774"
      ]
    ]
  ],
  "added": [
    [
      "00b9065c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b90668",
      "READ",
      [
        "storage",
        "Stack[0x0]",
        null,
        null
      ]
    ],
    [
      "00b90760",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b90774"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b90234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b90220.md#insn-00b90234) · [`00b90270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b90220.md#insn-00b90270) · [`00b90290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b90220.md#insn-00b90290)
- 新版 `00b90698`（命令位置の公開資料なし） · `00b906b8`（命令位置の公開資料なし）

~~~diff
- 00b90234 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b90234 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b90234 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b90234 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b90234 bytes fd7b05a9
- 00b90270 ["INT_ADD", "register:40f0:8", ["const:b90270:8", "const:4:8"]]
- 00b90270 ["CALL", null, ["callee:00c5c370:8"]]
+ 00b90698 ["INT_ADD", "register:40f0:8", ["const:b90698:8", "const:4:8"]]
+ 00b90698 ["CALL", null, ["callee:00c5c370:8"]]
- 00b90270 bytes 402f0394
+ 00b90698 bytes 362f0394
- 00b90290 ["INT_ADD", "register:40f0:8", ["const:b90290:8", "const:4:8"]]
- 00b90290 ["CALL", null, ["callee:00c5c3f0:8"]]
+ 00b906b8 ["INT_ADD", "register:40f0:8", ["const:b906b8:8", "const:4:8"]]
+ 00b906b8 ["CALL", null, ["callee:00c5c3f0:8"]]
- 00b90290 bytes 582f0394
+ 00b906b8 bytes 4e2f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9eee034830ea669c4018e297ffb59a3b"></a>

### [`00b903e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b903e8.md) → [`00b90810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b90810.md) _ZN11flatbuffers9StructDef11DeserializeERNS_6ParserEPKN10reflection6ObjectE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c490.md) · 呼出先 14件 [`00b92d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92d28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5c890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c890.md) · 呼出先 14件 [`00b93150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93150.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.69% / 新版 88.69%

CFGの説明率　旧版 56.30% / 新版 55.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b904bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b90548"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b90548"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9047c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b909c8"
      ]
    ],
    [
      "unmatched:00b90484",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b909c8"
      ]
    ],
    [
      "unmatched:00b90494",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b909c8"
      ]
    ]
  ],
  "added": [
    [
      "00b908a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b909c8"
      ]
    ],
    [
      "00b908ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b909c8"
      ]
    ],
    [
      "00b908bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b909c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b90434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b903e8.md#insn-00b90434) · [`00b9047c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b903e8.md#insn-00b9047c) · [`00b90484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b903e8.md#insn-00b90484)
- 新版 `00b9085c`（命令位置の公開資料なし）

~~~diff
- 00b90434 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b90434 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b9085c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b9085c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b90434 bytes e3000054
+ 00b9085c bytes e3000054
- 00b9047c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b9047c ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
- 00b9047c bytes 23090054
- 00b90484 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b90484 ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
- 00b90484 bytes e90800b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad4d63cafb2722c4b018d618d9e2fe12"></a>

### [`00b90a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b90a04.md) → [`00b90e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b90e2c.md) _ZN11flatbuffers8FieldDef11DeserializeERNS_6ParserEPKN10reflection5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c440.md) · 呼出先 12件 [`00b92d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92d28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5c840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c840.md) · 呼出先 12件 [`00b93150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93150.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.23% / 新版 87.23%

CFGの説明率　旧版 30.21% / 新版 28.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 8件, `unresolved_branch_alignment` 12件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b90a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b90a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b90a5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b90a58",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b90a5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b90a98",
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
      "00b90e80",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00b90e84",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "00b90ec0",
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

- 旧版 [`00b90a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b90a04.md#insn-00b90a58) · [`00b90a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b90a04.md#insn-00b90a5c) · [`00b90a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b90a04.md#insn-00b90a98)

~~~diff
- 00b90a58 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b90a58 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b90a58 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b90a58 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b90a58 bytes ffff01a9
- 00b90a5c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b90a5c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b90a5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b90a5c bytes ff0b00f9
- 00b90a98 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b90a98 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00b90a98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b90a98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b90a98 bytes e85b01a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f95e5a26f0153ac7651bd99740126218"></a>

### [`00b9116c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b9116c.md) → [`00b91594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b91/00b91594.md) _ZN10reflection11CreateFieldERN11flatbuffers21FlatBufferBuilderImplILb0EEENS0_6OffsetINS0_6StringEEENS4_INS_4TypeEEEttldbbbNS4_INS0_6VectorI

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb60.md) · 呼出先 10件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5bde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bde0.md) [`00c5be10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be10.md) [`00c5be20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be20.md) [`00c5be60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be60.md)
- 新版 呼出元 1件 [`00c5bf60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf60.md) · 呼出先 10件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1e0.md) [`00c5c210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c210.md) [`00c5c220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c220.md) [`00c5c260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c260.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.52% / 新版 84.52%

CFGの説明率　旧版 3.23% / 新版 3.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91180"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91180"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91184"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b91180",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b91184",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9118c",
      "READ",
      [
        "storage",
        "Stack[0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b915a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b915ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b915b4",
      "READ",
      [
        "storage",
        "Stack[0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b91180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b9116c.md#insn-00b91180) · [`00b91184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b9116c.md#insn-00b91184) · [`00b911c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b9116c.md#insn-00b911c4)

~~~diff
- 00b91180 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b91180 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b91180 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b91180 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b91180 bytes f44f06a9
- 00b91184 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b91184 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b91184 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b91184 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b91184 bytes fd7b07a9
- 00b911c4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b911c4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b911c4 bytes 61000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5339fca1c90bc0ae0b09e6b212e76d2"></a>

### [`00b91504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91504.md) → [`00b9192c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b91/00b9192c.md) _ZN11flatbuffers13FloatToStringIdEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_i

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bcc0.md) · 呼出先 9件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e10.md)
- 新版 呼出元 1件 [`00c5c0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c0c0.md) · 呼出先 9件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c58210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58210.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.18% / 新版 77.18%

CFGの説明率　旧版 40.74% / 新版 40.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b915b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b91a18",
      "incomplete_value": true,
      "site": "00b91a24",
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
      "definition_site": "00b915f0",
      "incomplete_value": true,
      "site": "00b915fc",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9161c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b91538",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b9153c",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ],
    [
      "00b919a4",
      "DATA",
      [
        "storage",
        "00c907d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b91960",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00b91964",
      "READ",
      [
        "storage",
        "00c9b840",
        null,
        "pointer"
      ]
    ],
    [
      "00b919a4",
      "DATA",
      [
        "storage",
        "00c90bd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b915b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91504.md#insn-00b915b8) · [`00b915c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91504.md#insn-00b915c8) · [`00b9161c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91504.md#insn-00b9161c)
- 新版 `00b919f0`（命令位置の公開資料なし）

~~~diff
- 00b915b8 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b915b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b915b8 bytes e90300f9
- 00b915c8 ["INT_ADD", "register:40f0:8", ["const:b915c8:8", "const:4:8"]]
- 00b915c8 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00b919f0 ["INT_ADD", "register:40f0:8", ["const:b919f0:8", "const:4:8"]]
+ 00b919f0 ["CALL", null, ["callee:00c5a7a0:8"]]
- 00b915c8 bytes 76230394
+ 00b919f0 bytes 6c230394
- 00b9161c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
- 00b9161c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:4"]]
- 00b9161c bytes 0a0900b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06e93be427cc0b90c08382901e9248cd"></a>

### [`00b91758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91758.md) → [`00b91b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b91/00b91b80.md) _ZNK11flatbuffers7RPCCall9SerializeEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c620.md) · 呼出先 8件 [`00b92a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a70.md) [`00c5bea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bea0.md) [`00c5bec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bec0.md) [`00c5bf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf40.md) [`00c5bf60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf60.md)
- 新版 呼出元 1件 [`00c5ca20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca20.md) · 呼出先 8件 [`00b92e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e98.md) [`00c5c2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c2a0.md) [`00c5c2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c2c0.md) [`00c5c340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c340.md) [`00c5c360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c360.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 16.67% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b91c08",
      "incomplete_value": false,
      "site": "00b91c20",
      "value": [
        "leaf",
        "const:c:8"
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b9182c",
      "incomplete_value": false,
      "site": "00b91838",
      "value": [
        "leaf",
        "const:4:8"
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b91c64",
      "incomplete_value": true,
      "site": "00b91c6c",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 8,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b917f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91758.md#insn-00b917f8) · [`00b91838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91758.md#insn-00b91838) · [`00b91844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91758.md#insn-00b91844)
- 新版 `00b91c20`（命令位置の公開資料なし） · `00b91c60`（命令位置の公開資料なし） · `00b91c6c`（命令位置の公開資料なし）

~~~diff
- 00b917f8 ["INT_ADD", "register:40f0:8", ["const:b917f8:8", "const:4:8"]]
- 00b917f8 ["CALL", null, ["callee:00c5c400:8"]]
+ 00b91c20 ["INT_ADD", "register:40f0:8", ["const:b91c20:8", "const:4:8"]]
+ 00b91c20 ["CALL", null, ["callee:00c5c400:8"]]
- 00b917f8 bytes 022a0394
+ 00b91c20 bytes f8290394
- 00b91838 ["INT_ADD", "register:40f0:8", ["const:b91838:8", "const:4:8"]]
- 00b91838 ["CALL", null, ["callee:00c5c370:8"]]
+ 00b91c60 ["INT_ADD", "register:40f0:8", ["const:b91c60:8", "const:4:8"]]
+ 00b91c60 ["CALL", null, ["callee:00c5c370:8"]]
- 00b91838 bytes ce290394
+ 00b91c60 bytes c4290394
- 00b91844 ["INT_ADD", "register:40f0:8", ["const:b91844:8", "const:4:8"]]
- 00b91844 ["CALL", null, ["callee:00c5c340:8"]]
+ 00b91c6c ["INT_ADD", "register:40f0:8", ["const:b91c6c:8", "const:4:8"]]
+ 00b91c6c ["CALL", null, ["callee:00c5c340:8"]]
- 00b91844 bytes bf290394
+ 00b91c6c bytes b5290394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b18b9b0606e926013b28605bf06be9c"></a>

### [`00b91860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91860.md) → [`00b91c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b91/00b91c88.md) _ZN11flatbuffers7RPCCall11DeserializeERNS_6ParserEPKN10reflection7RPCCallE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c430.md) · 呼出先 7件 [`00b92d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92d28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5c830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c830.md) · 呼出先 7件 [`00b93150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93150.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.62% / 新版 77.62%

CFGの説明率　旧版 22.11% / 新版 21.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 6件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91864"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91864"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91868"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b91864",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b91868",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9186c",
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
      "00b91c8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b91c90",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b91c94",
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

- 旧版 [`00b91864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91860.md#insn-00b91864) · [`00b91868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91860.md#insn-00b91868) · [`00b9186c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91860.md#insn-00b9186c)

~~~diff
- 00b91864 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b91864 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b91864 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b91864 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b91864 bytes fc6f04a9
- 00b91868 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b91868 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b91868 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b91868 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b91868 bytes fa6705a9
- 00b9186c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b9186c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b9186c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b9186c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9186c bytes f85f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fb95ff9353579882ea8a59521b78a5c"></a>

### [`00b91cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91cb4.md) → [`00b920dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b920dc.md) _ZN11flatbuffers10ServiceDef11DeserializeERNS_6ParserEPKN10reflection7ServiceE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bbc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbc0.md) · 呼出先 10件 [`00b92d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92d28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5bfc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfc0.md) · 呼出先 10件 [`00b93150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93150.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 32.95% / 新版 34.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91cb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91cbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91cbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b91cb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b91cbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b91cc0",
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
      "00b920e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b920e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b920e8",
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

- 旧版 [`00b91cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91cb4.md#insn-00b91cb8) · [`00b91cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91cb4.md#insn-00b91cbc) · [`00b91cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91cb4.md#insn-00b91cc0)

~~~diff
- 00b91cb8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00b91cb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 00b91cb8 bytes e82b00fd
- 00b91cbc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b91cbc ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b91cbc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b91cbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b91cbc bytes fc6f06a9
- 00b91cc0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b91cc0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b91cc0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b91cc0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b91cc0 bytes fa6707a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-152ab2e822cade6577502e161e06cb9a"></a>

### [`00b920bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b920bc.md) → [`00b924e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b924e4.md) _ZNK11flatbuffers7EnumVal9SerializeEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c610.md) · 呼出先 5件 [`00b92a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a70.md) [`00c5bb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb90.md) [`00c5bea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bea0.md) [`00c5bec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bec0.md) [`00c5c5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c5d0.md)
- 新版 呼出元 1件 [`00c5ca10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca10.md) · 呼出先 5件 [`00b92e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e98.md) [`00c5bf90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf90.md) [`00c5c2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c2a0.md) [`00c5c2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c2c0.md) [`00c5c9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c9d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 28.57% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b9257c",
      "incomplete_value": true,
      "site": "00b92588",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b92580",
      "incomplete_value": true,
      "site": "00b92588",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b92578",
      "incomplete_value": true,
      "site": "00b92588",
      "value": [
        "INT_AND",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:ffffffff:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 4
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b92160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b920bc.md#insn-00b92160) · [`00b92178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b920bc.md#insn-00b92178)
- 新版 `00b92588`（命令位置の公開資料なし） · `00b925a0`（命令位置の公開資料なし）

~~~diff
- 00b92160 ["INT_ADD", "register:40f0:8", ["const:b92160:8", "const:4:8"]]
- 00b92160 ["CALL", null, ["callee:00c5bf90:8"]]
+ 00b92588 ["INT_ADD", "register:40f0:8", ["const:b92588:8", "const:4:8"]]
+ 00b92588 ["CALL", null, ["callee:00c5bf90:8"]]
- 00b92160 bytes 8c260394
+ 00b92588 bytes 82260394
- 00b92178 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b92178 ["RETURN", null, ["register:0:8"]]
- 00b92178 bytes c0035fd6
+ 00b925a0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b925a0 ["RETURN", null, ["register:0:8"]]
+ 00b925a0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87893e09e97cae1d77060a715798b17d"></a>

### [`00b9217c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b9217c.md) → [`00b925a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b925a4.md) _ZN11flatbuffers7EnumDef11DeserializeERNS_6ParserEPKN10reflection4EnumE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c400.md) · 呼出先 11件 [`00b92d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92d28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5c800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c800.md) · 呼出先 11件 [`00b93150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93150.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.95% / 新版 82.95%

CFGの説明率　旧版 24.04% / 新版 24.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 1件, `unresolved_branch_alignment` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 24件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92180"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92180"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92184"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b92180",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b92184",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b92188",
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
      "00b925a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b925ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b925b0",
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

- 旧版 [`00b92180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b9217c.md#insn-00b92180) · [`00b92184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b9217c.md#insn-00b92184) · [`00b92188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b9217c.md#insn-00b92188)

~~~diff
- 00b92180 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b92180 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b92180 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b92180 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b92180 bytes fc6f05a9
- 00b92184 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b92184 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b92184 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b92184 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b92184 bytes fa6706a9
- 00b92188 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b92188 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b92188 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b92188 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b92188 bytes f85f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bf41c15a5f104ea8443bb911421f6f6"></a>

### [`00b9259c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b9259c.md) → [`00b929c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b929c4.md) _ZN11flatbuffers7EnumVal11DeserializeERNS_6ParserEPKN10reflection7EnumValE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c420.md) · 呼出先 7件 [`00b92d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92d28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5c820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c820.md) · 呼出先 7件 [`00b93150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93150.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 59.46% / 新版 69.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b925a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b925a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b925a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b925a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b925a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b925a8",
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
      "00b929c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b929cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b929d0",
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

- 旧版 [`00b925a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b9259c.md#insn-00b925a0) · [`00b925a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b9259c.md#insn-00b925a4) · [`00b925a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b9259c.md#insn-00b925a8)

~~~diff
- 00b925a0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b925a0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b925a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b925a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b925a0 bytes fc6f03a9
- 00b925a4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b925a4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b925a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b925a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b925a4 bytes fa6704a9
- 00b925a8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b925a8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b925a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b925a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b925a8 bytes f85f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-882bac306fbc0303e4c7d9d3da8c62af"></a>

### [`00b92a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a70.md) → [`00b92e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e98.md) FUN_00b92e98

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`00b8e948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8e/00b8e948.md) [`00b8ec90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8e/00b8ec90.md) [`00b8f10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8f10c.md) [`00b8fe04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8f/00b8fe04.md) [`00b90204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b90204.md) · 呼出先 10件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 8件 [`00b8ed70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8e/00b8ed70.md) [`00b8f0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8f/00b8f0b8.md) [`00b8f534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8f/00b8f534.md) [`00b9022c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b9022c.md) [`00b9062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b9062c.md) · 呼出先 10件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.12% / 新版 90.12%

CFGの説明率　旧版 59.02% / 新版 59.02%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92a74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92a74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92a78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b92a74",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b92a78",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b92a7c",
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
      "00b92e9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b92ea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b92ea4",
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

- 旧版 [`00b92a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a70.md#insn-00b92a74) · [`00b92a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a70.md#insn-00b92a78) · [`00b92a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a70.md#insn-00b92a7c)

~~~diff
- 00b92a74 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b92a74 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b92a74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b92a74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b92a74 bytes fc6f03a9
- 00b92a78 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b92a78 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b92a78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b92a78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b92a78 bytes fa6704a9
- 00b92a7c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b92a7c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b92a7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b92a7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b92a7c bytes f85f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13dabb0d20fadc9b9fc97217922f2fb9"></a>

### [`00b92d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92d28.md) → [`00b93150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93150.md) FUN_00b93150

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`00b903e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b903e8.md) [`00b909fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b909fc.md) [`00b90a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b90/00b90a04.md) [`00b91860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91860.md) [`00b91cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91cb4.md) · 呼出先 8件 [`0063947c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/0063947c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 8件 [`00b90810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b90810.md) [`00b90e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b90e24.md) [`00b90e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b90e2c.md) [`00b91c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b91/00b91c88.md) [`00b920dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b920dc.md) · 呼出先 8件 [`006394bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/006394bc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.58% / 新版 99.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b93208",
      "incomplete_value": false,
      "site": "00b9320c",
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
            "const:7b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b92de0",
      "incomplete_value": false,
      "site": "00b92de4",
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
            "const:3b:8"
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
      "00b93208",
      "PARAM",
      [
        "storage",
        "002b803b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b93208",
      "PARAM",
      [
        "storage",
        "002b807b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b92de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92d28.md#insn-00b92de4) · [`00b92dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92d28.md#insn-00b92dc0) · [`00b92de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92d28.md#insn-00b92de0)
- 新版 `00b9320c`（命令位置の公開資料なし） · `00b931e8`（命令位置の公開資料なし） · `00b93208`（命令位置の公開資料なし）

~~~diff
- 00b92de4 ["INT_ADD", "register:40f0:8", ["const:b92de4:8", "const:4:8"]]
- 00b92de4 ["CALL", null, ["callee:00c5b5c0:8"]]
+ 00b9320c ["INT_ADD", "register:40f0:8", ["const:b9320c:8", "const:4:8"]]
+ 00b9320c ["CALL", null, ["callee:00c5b5c0:8"]]
- 00b92de4 bytes f7200394
+ 00b9320c bytes ed200394
- 00b92dc0 ["INT_ADD", "register:40f0:8", ["const:b92dc0:8", "const:4:8"]]
- 00b92dc0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b931e8 ["INT_ADD", "register:40f0:8", ["const:b931e8:8", "const:4:8"]]
+ 00b931e8 ["CALL", null, ["callee:00c57e90:8"]]
- 00b92dc0 bytes 34130394
+ 00b931e8 bytes 2a130394
- 00b92de0 ["COPY", "tmp:0:8", ["const:3b:8"]]
- 00b92de0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b92de0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b92de0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b93208 ["COPY", "tmp:0:8", ["const:7b:8"]]
+ 00b93208 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b93208 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b93208 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b92de0 bytes 21ec0091
+ 00b93208 bytes 21ec0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b00e18312d986abe2343e68a7aa95a1"></a>

### [`00b93410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b93410.md) → [`00b93838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93838.md) _ZN11flatbuffers6Parser11DeserializeEPKhm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b93520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b93520.md) [`00b935bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b935bc.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5c0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c0a0.md) [`00c5cd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd30.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b93948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93948.md) [`00b939e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b939e4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5c4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c4a0.md) [`00c5d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9385c",
      "incomplete_value": true,
      "site": "00b9388c",
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
    "old": {
      "definition_site": "00b93434",
      "incomplete_value": true,
      "site": "00b93464",
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
                "const:d30:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b93880",
      "incomplete_value": false,
      "site": "00b938a4",
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
            "const:f0b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93458",
      "incomplete_value": false,
      "site": "00b9347c",
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
            "const:e2f:8"
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
      "definition_site": "00b938b4",
      "incomplete_value": false,
      "site": "00b938bc",
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
            "const:f0b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9348c",
      "incomplete_value": false,
      "site": "00b93494",
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
            "const:e2f:8"
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
      "00b9385c",
      "READ",
      [
        "storage",
        "002c3d30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b93880",
      "PARAM",
      [
        "storage",
        "002a4e2f",
        null,
        null
      ]
    ],
    [
      "00b938b4",
      "PARAM",
      [
        "storage",
        "002a4e2f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b9385c",
      "READ",
      [
        "storage",
        "002c3d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00b93880",
      "PARAM",
      [
        "storage",
        "002a4f0b",
        null,
        null
      ]
    ],
    [
      "00b938b4",
      "PARAM",
      [
        "storage",
        "002a4f0b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9347c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b93410.md#insn-00b9347c) · [`00b93494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b93410.md#insn-00b93494) · [`00b93434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b93410.md#insn-00b93434)
- 新版 `00b938a4`（命令位置の公開資料なし） · `00b938bc`（命令位置の公開資料なし） · `00b9385c`（命令位置の公開資料なし）

~~~diff
- 00b9347c ["INT_ADD", "register:40f0:8", ["const:b9347c:8", "const:4:8"]]
- 00b9347c ["CALL", null, ["callee:00c5d130:8"]]
+ 00b938a4 ["INT_ADD", "register:40f0:8", ["const:b938a4:8", "const:4:8"]]
+ 00b938a4 ["CALL", null, ["callee:00c5d130:8"]]
- 00b9347c bytes 2d260394
+ 00b938a4 bytes 23260394
- 00b93494 ["INT_ADD", "register:40f0:8", ["const:b93494:8", "const:4:8"]]
- 00b93494 ["CALL", null, ["callee:00c5d130:8"]]
+ 00b938bc ["INT_ADD", "register:40f0:8", ["const:b938bc:8", "const:4:8"]]
+ 00b938bc ["CALL", null, ["callee:00c5d130:8"]]
- 00b93494 bytes 27260394
+ 00b938bc bytes 1d260394
- 00b93434 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d30:8"]]
- 00b93434 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b93434 ["COPY", "register:5008:8", ["const:0:8"]]
- 00b93434 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00b9385c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d70:8"]]
+ 00b9385c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b9385c ["COPY", "register:5008:8", ["const:0:8"]]
+ 00b9385c ["COPY", "register:5010:8", ["const:0:8"]]
- 00b93434 bytes 209946fd
+ 00b9385c bytes 20b946fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2cab01dc2c3a335b15c5d22eede9cc6"></a>

### [`00b93520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b93520.md) → [`00b93948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93948.md) _ZN10reflection30VerifySizePrefixedSchemaBufferERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b93410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b93410.md) · 呼出先 2件 [`00c5c570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c570.md) [`00c5cd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd30.md)
- 新版 呼出元 1件 [`00b93838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93838.md) · 呼出先 2件 [`00c5c970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c970.md) [`00c5d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b9398c",
      "incomplete_value": false,
      "site": "00b93994",
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
            "const:f0b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93564",
      "incomplete_value": false,
      "site": "00b9356c",
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
            "const:e2f:8"
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
      "00b9398c",
      "PARAM",
      [
        "storage",
        "002a4e2f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b9398c",
      "PARAM",
      [
        "storage",
        "002a4f0b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9356c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b93520.md#insn-00b9356c) · [`00b93564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b93520.md#insn-00b93564)
- 新版 `00b93994`（命令位置の公開資料なし） · `00b9398c`（命令位置の公開資料なし）

~~~diff
- 00b9356c ["INT_ADD", "register:40f0:8", ["const:b9356c:8", "const:4:8"]]
- 00b9356c ["CALL", null, ["callee:00c5d130:8"]]
+ 00b93994 ["INT_ADD", "register:40f0:8", ["const:b93994:8", "const:4:8"]]
+ 00b93994 ["CALL", null, ["callee:00c5d130:8"]]
- 00b9356c bytes f1250394
+ 00b93994 bytes e7250394
- 00b93564 ["COPY", "tmp:0:8", ["const:e2f:8"]]
- 00b93564 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b93564 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b93564 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b9398c ["COPY", "tmp:0:8", ["const:f0b:8"]]
+ 00b9398c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b9398c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b9398c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b93564 bytes 21bc3891
+ 00b9398c bytes 212c3c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76a4ee5b0642547b4481f171a435cd81"></a>

### [`00b935bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b935bc.md) → [`00b939e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b939e4.md) _ZN10reflection18VerifySchemaBufferERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b93410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b93410.md) · 呼出先 2件 [`00c5c570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c570.md) [`00c5cd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd30.md)
- 新版 呼出元 1件 [`00b93838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93838.md) · 呼出先 2件 [`00c5c970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c970.md) [`00c5d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d130.md)

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
      "definition_site": "00b93a0c",
      "incomplete_value": false,
      "site": "00b93a18",
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
            "const:f0b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b935e4",
      "incomplete_value": false,
      "site": "00b935f0",
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
            "const:e2f:8"
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
      "00b93a0c",
      "PARAM",
      [
        "storage",
        "002a4e2f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b93a0c",
      "PARAM",
      [
        "storage",
        "002a4f0b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b935f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b935bc.md#insn-00b935f0) · [`00b935e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b935bc.md#insn-00b935e4)
- 新版 `00b93a18`（命令位置の公開資料なし） · `00b93a0c`（命令位置の公開資料なし）

~~~diff
- 00b935f0 ["INT_ADD", "register:40f0:8", ["const:b935f0:8", "const:4:8"]]
- 00b935f0 ["CALL", null, ["callee:00c5d130:8"]]
+ 00b93a18 ["INT_ADD", "register:40f0:8", ["const:b93a18:8", "const:4:8"]]
+ 00b93a18 ["CALL", null, ["callee:00c5d130:8"]]
- 00b935f0 bytes d0250394
+ 00b93a18 bytes c6250394
- 00b935e4 ["COPY", "tmp:0:8", ["const:e2f:8"]]
- 00b935e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b935e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b935e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b93a0c ["COPY", "tmp:0:8", ["const:f0b:8"]]
+ 00b93a0c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b93a0c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b93a0c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b935e4 bytes 21bc3891
+ 00b93a0c bytes 212c3c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94845ca76d9efe3ab84e526d8c1b7cb4"></a>

### [`00b94c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b94/00b94c88.md) → [`00b950b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b950b0.md) _ZN11flatbuffers6Parser9ConformToERKS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00b5abb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5abb4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 93.92% / 新版 93.92%

CFGの説明率　旧版 92.39% / 新版 90.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95348"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b954fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b95770"
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
      "00b951b4",
      "PARAM",
      [
        "storage",
        "002a630f",
        null,
        null
      ]
    ],
    [
      "00b952dc",
      "PARAM",
      [
        "storage",
        "002a2b2e",
        null,
        "string"
      ]
    ],
    [
      "00b95344",
      "PARAM",
      [
        "storage",
        "002a6055",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b951b4",
      "PARAM",
      [
        "storage",
        "002a63eb",
        null,
        null
      ]
    ],
    [
      "00b952dc",
      "PARAM",
      [
        "storage",
        "002a2bfb",
        null,
        "string"
      ]
    ],
    [
      "00b95344",
      "PARAM",
      [
        "storage",
        "002a6131",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b94f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b94/00b94c88.md#insn-00b94f20) · [`00b94f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b94/00b94c88.md#insn-00b94f7c) · [`00b9503c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b94/00b94c88.md#insn-00b9503c)
- 新版 `00b95348`（命令位置の公開資料なし） · `00b953a4`（命令位置の公開資料なし） · `00b95464`（命令位置の公開資料なし）

~~~diff
- 00b94f20 ["INT_ADD", "register:40f0:8", ["const:b94f20:8", "const:4:8"]]
- 00b94f20 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b95348 ["INT_ADD", "register:40f0:8", ["const:b95348:8", "const:4:8"]]
+ 00b95348 ["CALL", null, ["callee:00c580b0:8"]]
- 00b94f20 bytes 640b0394
+ 00b95348 bytes 5a0b0394
- 00b94f7c ["COPY", "tmp:0:8", ["const:58b:8"]]
- 00b94f7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b94f7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b94f7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b953a4 ["COPY", "tmp:0:8", ["const:658:8"]]
+ 00b953a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b953a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b953a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b94f7c bytes 002c1691
+ 00b953a4 bytes 00601991
- 00b9503c ["INT_ADD", "register:40f0:8", ["const:b9503c:8", "const:4:8"]]
- 00b9503c ["CALL", null, ["callee:00b5abb4:8"]]
+ 00b95464 ["INT_ADD", "register:40f0:8", ["const:b95464:8", "const:4:8"]]
+ 00b95464 ["CALL", null, ["callee:00b5abb4:8"]]
- 00b9503c bytes d415ff97
+ 00b95464 bytes d415ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-384646e3f902e480aa8046b9f8f6ad5c"></a>

### [`00b95948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95948.md) → [`00b95d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95d70.md) _ZN11flatbuffers8HashFnv1ItEET_PKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b95954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95948.md#insn-00b95954)
- 新版 `00b95d7c`（命令位置の公開資料なし）

~~~diff
- 00b95954 ["INT_EQUAL", "tmp:0:1", ["register:4050:4", "const:0:4"]]
- 00b95954 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b95d7c ["INT_EQUAL", "tmp:0:1", ["register:4050:4", "const:0:4"]]
+ 00b95d7c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b95954 bytes 2a010034
+ 00b95d7c bytes 2a010034
~~~


<a id="compare-952e07bdc541dc01d893e94427895892"></a>

### [`00b959b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b959b8.md) → [`00b95de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95de0.md) _ZN11flatbuffers8HashFnv1IjEET_PKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b959c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b959b8.md#insn-00b959c8)
- 新版 `00b95df0`（命令位置の公開資料なし）

~~~diff
- 00b959c8 ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b959c8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b95df0 ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
+ 00b95df0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b959c8 bytes 29010034
+ 00b95df0 bytes 29010034
~~~


<a id="compare-4109ea3795a62edf76976acf378d9a2e"></a>

### [`00b959f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b959f0.md) → [`00b95e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95e18.md) _ZN11flatbuffers9HashFnv1aIjEET_PKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b95a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b959f0.md#insn-00b95a00) · [`00b95a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b959f0.md#insn-00b95a20)
- 新版 `00b95e28`（命令位置の公開資料なし） · `00b95e48`（命令位置の公開資料なし）

~~~diff
- 00b95a00 ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b95a00 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b95e28 ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
+ 00b95e28 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b95a00 bytes 29010034
+ 00b95e28 bytes 29010034
- 00b95a20 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b95a20 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b95e48 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
+ 00b95e48 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b95a20 bytes 89ffff35
+ 00b95e48 bytes 89ffff35
~~~


<a id="compare-6fea85738993c7d8dbbf8207e59d350d"></a>

### [`00b95a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95a28.md) → [`00b95e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95e50.md) _ZN11flatbuffers8HashFnv1ImEET_PKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b95a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95a28.md#insn-00b95a40)
- 新版 `00b95e68`（命令位置の公開資料なし）

~~~diff
- 00b95a40 ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b95a40 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b95e68 ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
+ 00b95e68 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b95a40 bytes 29010034
+ 00b95e68 bytes 29010034
~~~


<a id="compare-da9495686bc8ebfb456ab758c17aab80"></a>

### [`00b95bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95bbc.md) → [`00b95fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95fe4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cad0.md) · 呼出先 5件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md) [`00c5b660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b660.md) [`00c5cae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cae0.md)
- 新版 呼出元 1件 [`00c5ced0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ced0.md) · 呼出先 5件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md) [`00c5ba60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba60.md) [`00c5cee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.58% / 新版 84.58%

CFGの説明率　旧版 28.79% / 新版 30.40%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 15件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95bd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95bd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b95ffc"
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
      "unmatched:00b95bd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b95c18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b96078"
      ]
    ],
    [
      "unmatched:00b95c2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b96084"
      ]
    ]
  ],
  "added": [
    [
      "00b95ffc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b96040",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b96078"
      ]
    ],
    [
      "00b96054",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b96084"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b95bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95bbc.md#insn-00b95bd4) · [`00b95c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95bbc.md#insn-00b95c18) · [`00b95c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95bbc.md#insn-00b95c2c)

~~~diff
- 00b95bd4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b95bd4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b95bd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b95bd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b95bd4 bytes fd7b06a9
- 00b95c18 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b95c18 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b95c18 bytes d60100b4
- 00b95c2c ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00b95c2c bytes 80010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d1928fb3428b9689be4658e4f72f1c3"></a>

### [`00b95f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95f48.md) → [`00b96370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b96370.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cae0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md)
- 新版 呼出元 1件 [`00c5cee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cee0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 61.54% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96064"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b9648c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9603c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9603c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b96474"
      ]
    ]
  ],
  "added": [
    [
      "00b96464",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b96474"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9603c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95f48.md#insn-00b9603c) · [`00b96064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95f48.md#insn-00b96064)
- 新版 `00b96464`（命令位置の公開資料なし）

~~~diff
- 00b9603c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b9603c ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00b9603c bytes 890000b4
- 00b96064 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00b96064 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b96064 bytes 680a00f9
+ 00b96464 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b96464 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 00b96464 bytes 890000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab36ce4b223d579b8b6e86c24edf32d8"></a>

### [`00b9607c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b9607c.md) → [`00b964a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b964a4.md) _ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_co

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc60.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5d060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d060.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.19% / 新版 94.19%

CFGの説明率　旧版 38.71% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b960b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b960d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b964dc"
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
      "unmatched:00b960b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9652c"
      ]
    ],
    [
      "unmatched:00b960d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b96528"
      ]
    ]
  ],
  "added": [
    [
      "00b964dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9652c"
      ]
    ],
    [
      "00b96500",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b96528"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b960b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b9607c.md#insn-00b960b4) · [`00b960d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b9607c.md#insn-00b960d8) · [`00b96134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b9607c.md#insn-00b96134)
- 新版 `00b9655c`（命令位置の公開資料なし）

~~~diff
- 00b960b4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b960b4 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b960b4 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 00b960b4 bytes 89020054
- 00b960d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b960d8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b960d8 bytes 490100b5
- 00b96134 ["INT_ADD", "register:40f0:8", ["const:b96134:8", "const:4:8"]]
- 00b96134 ["CALL", null, ["callee:00c57f40:8"]]
+ 00b9655c ["INT_ADD", "register:40f0:8", ["const:b9655c:8", "const:4:8"]]
+ 00b9655c ["CALL", null, ["callee:00c57f40:8"]]
- 00b96134 bytes 83060394
+ 00b9655c bytes 79060394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-996f8cfbd61f10c61df900503cde01f8"></a>

### [`00b96330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96330.md) → [`00b96758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b96758.md) _ZN11flatbuffers14EnumValBuilder13ValidateValueEPlb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bd70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bd70.md) · 呼出先 15件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5bcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bcd0.md)
- 新版 呼出元 1件 [`00c5c170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c170.md) · 呼出先 15件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5c0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c0d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.35% / 新版 88.35%

CFGの説明率　旧版 50.00% / 新版 45.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96350"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9641c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9641c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b96350",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b96374",
      "DATA",
      [
        "storage",
        "0030e17d",
        "switchD_00b9637c::switchdataD_0030e17d",
        "byte"
      ]
    ],
    [
      "unmatched:00b96404",
      "READ",
      [
        "storage",
        "002b070d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b96778",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b9679c",
      "DATA",
      [
        "storage",
        "0030e1bd",
        "switchD_00b967a4::switchdataD_0030e1bd",
        "byte"
      ]
    ],
    [
      "00b9682c",
      "READ",
      [
        "storage",
        "002b074d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b96350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96330.md#insn-00b96350) · [`00b9641c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96330.md#insn-00b9641c) · [`00b96420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96330.md#insn-00b96420)

~~~diff
- 00b96350 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b96350 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b96350 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b96350 bytes a9831df8
- 00b9641c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b9641c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00b9641c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b9641c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5040:16"]]
- 00b9641c bytes 010800ad
- 00b96420 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b96420 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1f:8"]]
- 00b96420 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00b96420 bytes 08f001b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0e43578554e80c737a383a5fd26ad0a"></a>

### [`00b964cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b964cc.md) → [`00b968f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b968f4.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE1EhEENS_12CheckedErrorEPli

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bce0.md) · 呼出先 8件 [`00b97ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97ad8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c5c0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c0e0.md) · 呼出先 8件 [`00b97f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97f00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 38.10% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b965b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b965b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b969d8"
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
      "unmatched:00b964fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9693c"
      ]
    ],
    [
      "unmatched:00b96524",
      "PARAM",
      [
        "storage",
        "002c0b1d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b96558",
      "PARAM",
      [
        "storage",
        "002c1c41",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b96924",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9693c"
      ]
    ],
    [
      "00b9694c",
      "PARAM",
      [
        "storage",
        "002c0b5d",
        null,
        "string"
      ]
    ],
    [
      "00b96980",
      "PARAM",
      [
        "storage",
        "002c1c81",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b964fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b964cc.md#insn-00b964fc) · [`00b96534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b964cc.md#insn-00b96534) · [`00b96558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b964cc.md#insn-00b96558)
- 新版 `00b9695c`（命令位置の公開資料なし）

~~~diff
- 00b964fc ["INT_RIGHT", "tmp:0:8", ["register:4000:8", "const:3f:4"]]
- 00b964fc ["INT_AND", "tmp:1:8", ["tmp:0:8", "const:1:8"]]
- 00b964fc ["INT_EQUAL", "tmp:2:1", ["tmp:1:8", "const:0:8"]]
- 00b964fc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b964fc bytes c000f8b7
- 00b96534 ["INT_ADD", "register:40f0:8", ["const:b96534:8", "const:4:8"]]
- 00b96534 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b9695c ["INT_ADD", "register:40f0:8", ["const:b9695c:8", "const:4:8"]]
+ 00b9695c ["CALL", null, ["callee:00c58fd0:8"]]
- 00b96534 bytes a7090394
+ 00b9695c bytes 9d090394
- 00b96558 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b96558 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b96558 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b96558 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b96558 bytes 4101899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f72d79123140d4807229a69df4aedde"></a>

### [`00b96700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96700.md) → [`00b96b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b96b28.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE2EhEENS_12CheckedErrorEPli

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bcf0.md) · 呼出先 8件 [`00b97ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97ad8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c5c0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c0f0.md) · 呼出先 8件 [`00b97f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97f00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.52% / 新版 86.52%

CFGの説明率　旧版 60.53% / 新版 57.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96728"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96790"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96794"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b96728",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b96758",
      "PARAM",
      [
        "storage",
        "002c0b1d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b9678c",
      "PARAM",
      [
        "storage",
        "002c1c41",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b96b50",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b96b80",
      "PARAM",
      [
        "storage",
        "002c0b5d",
        null,
        "string"
      ]
    ],
    [
      "00b96bb4",
      "PARAM",
      [
        "storage",
        "002c1c81",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b96728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96700.md#insn-00b96728) · [`00b96768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96700.md#insn-00b96768) · [`00b9678c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96700.md#insn-00b9678c)
- 新版 `00b96b90`（命令位置の公開資料なし）

~~~diff
- 00b96728 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b96728 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b96728 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b96728 bytes aa831df8
- 00b96768 ["INT_ADD", "register:40f0:8", ["const:b96768:8", "const:4:8"]]
- 00b96768 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b96b90 ["INT_ADD", "register:40f0:8", ["const:b96b90:8", "const:4:8"]]
+ 00b96b90 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b96768 bytes 1a090394
+ 00b96b90 bytes 10090394
- 00b9678c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b9678c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b9678c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b9678c ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b9678c bytes 4101899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d92b3d89ab9526b1147800f5cf6576c"></a>

### [`00b96934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96934.md) → [`00b96d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b96d5c.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE3EaEENS_12CheckedErrorEPli

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bd00.md) · 呼出先 8件 [`00b97c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97c78.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c5c100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c100.md) · 呼出先 8件 [`00b980a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b980a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.66% / 新版 93.66%

CFGの説明率　旧版 58.97% / 新版 60.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9695c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b96d84"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b969c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9695c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b96990",
      "PARAM",
      [
        "storage",
        "002c0b1d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b969c4",
      "PARAM",
      [
        "storage",
        "002c1c41",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b96d84",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b96db8",
      "PARAM",
      [
        "storage",
        "002c0b5d",
        null,
        "string"
      ]
    ],
    [
      "00b96dec",
      "PARAM",
      [
        "storage",
        "002c1c81",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96934.md#insn-00b9695c) · [`00b969a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96934.md#insn-00b969a0) · [`00b969c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96934.md#insn-00b969c4)
- 新版 `00b96dc8`（命令位置の公開資料なし）

~~~diff
- 00b9695c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b9695c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b9695c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b9695c bytes aa831df8
- 00b969a0 ["INT_ADD", "register:40f0:8", ["const:b969a0:8", "const:4:8"]]
- 00b969a0 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b96dc8 ["INT_ADD", "register:40f0:8", ["const:b96dc8:8", "const:4:8"]]
+ 00b96dc8 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b969a0 bytes 8c080394
+ 00b96dc8 bytes 82080394
- 00b969c4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b969c4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b969c4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b969c4 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b969c4 bytes 4101899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7d4c4eaf5d2d8440986bb134d03c03"></a>

### [`00b96b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96b6c.md) → [`00b96f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b96f94.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE4EhEENS_12CheckedErrorEPli

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bd10.md) · 呼出先 8件 [`00b97ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97ad8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c5c110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c110.md) · 呼出先 8件 [`00b97f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97f00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.33% / 新版 94.33%

CFGの説明率　旧版 64.86% / 新版 64.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96bf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b97020"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b96fec",
      "incomplete_value": false,
      "site": "00b96ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b5d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b96bc4",
      "incomplete_value": false,
      "site": "00b96bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b1d:8"
          ]
        ]
      ]
    },
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
      "unmatched:00b96bc4",
      "PARAM",
      [
        "storage",
        "002c0b1d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b96bf8",
      "PARAM",
      [
        "storage",
        "002c1c41",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b96bf8",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b96fec",
      "PARAM",
      [
        "storage",
        "002c0b5d",
        null,
        "string"
      ]
    ],
    [
      "00b97020",
      "PARAM",
      [
        "storage",
        "002c1c81",
        null,
        "string"
      ]
    ],
    [
      "00b97020",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b96bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96b6c.md#insn-00b96bd4) · [`00b96bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96b6c.md#insn-00b96bf8) · [`00b96c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96b6c.md#insn-00b96c14)
- 新版 `00b96ffc`（命令位置の公開資料なし） · `00b9703c`（命令位置の公開資料なし）

~~~diff
- 00b96bd4 ["INT_ADD", "register:40f0:8", ["const:b96bd4:8", "const:4:8"]]
- 00b96bd4 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b96ffc ["INT_ADD", "register:40f0:8", ["const:b96ffc:8", "const:4:8"]]
+ 00b96ffc ["CALL", null, ["callee:00c58fd0:8"]]
- 00b96bd4 bytes ff070394
+ 00b96ffc bytes f5070394
- 00b96bf8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b96bf8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b96bf8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b96bf8 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b96bf8 bytes 4101899a
- 00b96c14 ["INT_ADD", "register:40f0:8", ["const:b96c14:8", "const:4:8"]]
- 00b96c14 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b9703c ["INT_ADD", "register:40f0:8", ["const:b9703c:8", "const:4:8"]]
+ 00b9703c ["CALL", null, ["callee:00c57f80:8"]]
- 00b96c14 bytes db030394
+ 00b9703c bytes d1030394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76ee68a1c1d127e6650ddfea6d592fbb"></a>

### [`00b96da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96da0.md) → [`00b971c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b971c8.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE5EsEENS_12CheckedErrorEPli

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bd20.md) · 呼出先 8件 [`00b97e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97e18.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c5c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c120.md) · 呼出先 8件 [`00b98240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98240.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.37% / 新版 94.37%

CFGの説明率　旧版 64.86% / 新版 64.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96e30"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b97258"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b97224",
      "incomplete_value": false,
      "site": "00b97234",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b5d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b96dfc",
      "incomplete_value": false,
      "site": "00b96e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b1d:8"
          ]
        ]
      ]
    },
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
      "unmatched:00b96dfc",
      "PARAM",
      [
        "storage",
        "002c0b1d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b96e30",
      "PARAM",
      [
        "storage",
        "002c1c41",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b96e30",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b97224",
      "PARAM",
      [
        "storage",
        "002c0b5d",
        null,
        "string"
      ]
    ],
    [
      "00b97258",
      "PARAM",
      [
        "storage",
        "002c1c81",
        null,
        "string"
      ]
    ],
    [
      "00b97258",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b96e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96da0.md#insn-00b96e0c) · [`00b96e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96da0.md#insn-00b96e30) · [`00b96e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96da0.md#insn-00b96e4c)
- 新版 `00b97234`（命令位置の公開資料なし） · `00b97274`（命令位置の公開資料なし）

~~~diff
- 00b96e0c ["INT_ADD", "register:40f0:8", ["const:b96e0c:8", "const:4:8"]]
- 00b96e0c ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b97234 ["INT_ADD", "register:40f0:8", ["const:b97234:8", "const:4:8"]]
+ 00b97234 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b96e0c bytes 71070394
+ 00b97234 bytes 67070394
- 00b96e30 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b96e30 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b96e30 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b96e30 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b96e30 bytes 4101899a
- 00b96e4c ["INT_ADD", "register:40f0:8", ["const:b96e4c:8", "const:4:8"]]
- 00b96e4c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b97274 ["INT_ADD", "register:40f0:8", ["const:b97274:8", "const:4:8"]]
+ 00b97274 ["CALL", null, ["callee:00c57f80:8"]]
- 00b96e4c bytes 4d030394
+ 00b97274 bytes 43030394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc25342f5bbe0434aa8667a3f3f7e309"></a>

### [`00b96fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96fd8.md) → [`00b97400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97400.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE6EtEENS_12CheckedErrorEPli

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bd30.md) · 呼出先 8件 [`00b97fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97fb8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c5c130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c130.md) · 呼出先 8件 [`00b983e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b983e0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.07% / 新版 90.07%

CFGの説明率　旧版 55.26% / 新版 51.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97068"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97094"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b97490"
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
      "unmatched:00b97030",
      "PARAM",
      [
        "storage",
        "002c0b1d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b97064",
      "PARAM",
      [
        "storage",
        "002c1c41",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b97064",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b97458",
      "PARAM",
      [
        "storage",
        "002c0b5d",
        null,
        "string"
      ]
    ],
    [
      "00b9748c",
      "PARAM",
      [
        "storage",
        "002c1c81",
        null,
        "string"
      ]
    ],
    [
      "00b9748c",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96fd8.md#insn-00b97040) · [`00b97064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96fd8.md#insn-00b97064) · [`00b97068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96fd8.md#insn-00b97068)
- 新版 `00b97468`（命令位置の公開資料なし）

~~~diff
- 00b97040 ["INT_ADD", "register:40f0:8", ["const:b97040:8", "const:4:8"]]
- 00b97040 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b97468 ["INT_ADD", "register:40f0:8", ["const:b97468:8", "const:4:8"]]
+ 00b97468 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b97040 bytes e4060394
+ 00b97468 bytes da060394
- 00b97064 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b97064 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b97064 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b97064 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b97064 bytes 4101899a
- 00b97068 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00b97068 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b97068 bytes e00f803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e05661285c81433cdc79a1b85eec839"></a>

### [`00b9720c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b9720c.md) → [`00b97634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97634.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE7EiEENS_12CheckedErrorEPli

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bd40.md) · 呼出先 8件 [`00b98158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98158.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c5c140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c140.md) · 呼出先 8件 [`00b98580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98580.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.12% / 新版 81.12%

CFGの説明率　旧版 47.62% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97210"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97210"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97214"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b97210",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b97214",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b97218",
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
      "00b97638",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b9763c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b97640",
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

- 旧版 [`00b97210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b9720c.md#insn-00b97210) · [`00b97214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b9720c.md#insn-00b97214) · [`00b97218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b9720c.md#insn-00b97218)

~~~diff
- 00b97210 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b97210 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b97210 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00b97210 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b97210 bytes f6570da9
- 00b97214 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b97214 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b97214 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00b97214 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b97214 bytes f44f0ea9
- 00b97218 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b97218 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b97218 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00b97218 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b97218 bytes fd7b0fa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e1c8d84c0049a3a5ebef1b0ef4e61cc"></a>

### [`00b97448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97448.md) → [`00b97870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97870.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE8EjEENS_12CheckedErrorEPli

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bd50.md) · 呼出先 8件 [`00b982f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b982f8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c5c150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c150.md) · 呼出先 8件 [`00b98720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98720.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.07% / 新版 90.07%

CFGの説明率　旧版 72.50% / 新版 85.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b974d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b974dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97504"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b97478",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b978b8"
      ]
    ],
    [
      "unmatched:00b974a0",
      "PARAM",
      [
        "storage",
        "002c0b1d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b974d4",
      "PARAM",
      [
        "storage",
        "002c1c41",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b978a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b978b8"
      ]
    ],
    [
      "00b978c8",
      "PARAM",
      [
        "storage",
        "002c0b5d",
        null,
        "string"
      ]
    ],
    [
      "00b978fc",
      "PARAM",
      [
        "storage",
        "002c1c81",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97448.md#insn-00b97478) · [`00b974b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97448.md#insn-00b974b0) · [`00b974d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97448.md#insn-00b974d4)
- 新版 `00b978d8`（命令位置の公開資料なし）

~~~diff
- 00b97478 ["INT_RIGHT", "tmp:0:8", ["register:4000:8", "const:3f:4"]]
- 00b97478 ["INT_AND", "tmp:1:8", ["tmp:0:8", "const:1:8"]]
- 00b97478 ["INT_EQUAL", "tmp:2:1", ["tmp:1:8", "const:0:8"]]
- 00b97478 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b97478 bytes c000f8b7
- 00b974b0 ["INT_ADD", "register:40f0:8", ["const:b974b0:8", "const:4:8"]]
- 00b974b0 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b978d8 ["INT_ADD", "register:40f0:8", ["const:b978d8:8", "const:4:8"]]
+ 00b978d8 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b974b0 bytes c8050394
+ 00b978d8 bytes be050394
- 00b974d4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b974d4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b974d4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b974d4 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b974d4 bytes 4101899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5245bc6c10cb2cad0683a1939a1a91cf"></a>

### [`00b9767c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b9767c.md) → [`00b97aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97aa4.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE9ElEENS_12CheckedErrorEPli

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5bd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bd60.md) · 呼出先 8件 [`00b98498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98498.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c5c160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c160.md) · 呼出先 8件 [`00b988c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b988c0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b97af8",
      "incomplete_value": false,
      "site": "00b97b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b5d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b976d0",
      "incomplete_value": false,
      "site": "00b976e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b1d:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b97b58",
      "incomplete_value": false,
      "site": "00b97b74",
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
            "const:b5f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97730",
      "incomplete_value": false,
      "site": "00b9774c",
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
            "const:b1f:8"
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
      "definition_site": "00b97be0",
      "incomplete_value": false,
      "site": "00b97be8",
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
            "const:bb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b977b8",
      "incomplete_value": false,
      "site": "00b977c0",
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
            "const:ae9:8"
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
      "00b97af8",
      "PARAM",
      [
        "storage",
        "002c0b1d",
        null,
        "string"
      ]
    ],
    [
      "00b97b2c",
      "PARAM",
      [
        "storage",
        "002c1c41",
        null,
        "string"
      ]
    ],
    [
      "00b97b2c",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b97af8",
      "PARAM",
      [
        "storage",
        "002c0b5d",
        null,
        "string"
      ]
    ],
    [
      "00b97b2c",
      "PARAM",
      [
        "storage",
        "002c1c81",
        null,
        "string"
      ]
    ],
    [
      "00b97b2c",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b976e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b9767c.md#insn-00b976e0) · [`00b9774c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b9767c.md#insn-00b9774c) · [`00b977c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b9767c.md#insn-00b977c0)
- 新版 `00b97b08`（命令位置の公開資料なし） · `00b97b74`（命令位置の公開資料なし） · `00b97be8`（命令位置の公開資料なし）

~~~diff
- 00b976e0 ["INT_ADD", "register:40f0:8", ["const:b976e0:8", "const:4:8"]]
- 00b976e0 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b97b08 ["INT_ADD", "register:40f0:8", ["const:b97b08:8", "const:4:8"]]
+ 00b97b08 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b976e0 bytes 3c050394
+ 00b97b08 bytes 32050394
- 00b9774c ["INT_ADD", "register:40f0:8", ["const:b9774c:8", "const:4:8"]]
- 00b9774c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b97b74 ["INT_ADD", "register:40f0:8", ["const:b97b74:8", "const:4:8"]]
+ 00b97b74 ["CALL", null, ["callee:00c57f80:8"]]
- 00b9774c bytes 0d010394
+ 00b97b74 bytes 03010394
- 00b977c0 ["INT_ADD", "register:40f0:8", ["const:b977c0:8", "const:4:8"]]
- 00b977c0 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b97be8 ["INT_ADD", "register:40f0:8", ["const:b97be8:8", "const:4:8"]]
+ 00b97be8 ["CALL", null, ["callee:00c580b0:8"]]
- 00b977c0 bytes 3c010394
+ 00b97be8 bytes 32010394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6729127ddd3eae2540f3314eca657644"></a>

### [`00b978ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b978ac.md) → [`00b97cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97cd4.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE10EmEENS_12CheckedErrorEPli

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bcd0.md) · 呼出先 8件 [`00b98638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98638.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c5c0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c0d0.md) · 呼出先 8件 [`00b98a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98a60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.65% / 新版 90.65%

CFGの説明率　旧版 31.25% / 新版 21.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b979d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b979d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b979d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b978fc",
      "PARAM",
      [
        "storage",
        "002c0b1d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b97930",
      "PARAM",
      [
        "storage",
        "002c1c41",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b97930",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b97d24",
      "PARAM",
      [
        "storage",
        "002c0b5d",
        null,
        "string"
      ]
    ],
    [
      "00b97d58",
      "PARAM",
      [
        "storage",
        "002c1c81",
        null,
        "string"
      ]
    ],
    [
      "00b97d58",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9790c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b978ac.md#insn-00b9790c) · [`00b97930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b978ac.md#insn-00b97930) · [`00b97978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b978ac.md#insn-00b97978)
- 新版 `00b97d34`（命令位置の公開資料なし） · `00b97da0`（命令位置の公開資料なし）

~~~diff
- 00b9790c ["INT_ADD", "register:40f0:8", ["const:b9790c:8", "const:4:8"]]
- 00b9790c ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b97d34 ["INT_ADD", "register:40f0:8", ["const:b97d34:8", "const:4:8"]]
+ 00b97d34 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b9790c bytes b1040394
+ 00b97d34 bytes a7040394
- 00b97930 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b97930 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b97930 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b97930 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b97930 bytes 4101899a
- 00b97978 ["INT_ADD", "register:40f0:8", ["const:b97978:8", "const:4:8"]]
- 00b97978 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b97da0 ["INT_ADD", "register:40f0:8", ["const:b97da0:8", "const:4:8"]]
+ 00b97da0 ["CALL", null, ["callee:00c57f80:8"]]
- 00b97978 bytes 82000394
+ 00b97da0 bytes 78000394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba8c0ae184c53d50bfe040a65dead52b"></a>

### [`00b97ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97ad8.md) → [`00b97f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97f00.md) FUN_00b97f00

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b78538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md) [`00b964cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b964cc.md) [`00b96700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96700.md) [`00b96b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96b6c.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md) [`00c5bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbe0.md)
- 新版 呼出元 4件 [`00b78960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78960.md) [`00b968f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b968f4.md) [`00b96b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b96b28.md) [`00b96f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b96f94.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md) [`00c5bfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.65% / 新版 83.65%

CFGの説明率　旧版 6.06% / 新版 4.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97b30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97b34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97b58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b97b0c",
      "PARAM",
      [
        "storage",
        "002a998d",
        null,
        null
      ]
    ],
    [
      "unmatched:00b97b2c",
      "PARAM",
      [
        "storage",
        "002b0731",
        null,
        null
      ]
    ],
    [
      "unmatched:00b97b30",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b97f34",
      "PARAM",
      [
        "storage",
        "002a9a5a",
        null,
        null
      ]
    ],
    [
      "00b97f54",
      "PARAM",
      [
        "storage",
        "002b0771",
        null,
        null
      ]
    ],
    [
      "00b97f58",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97ad8.md#insn-00b97b1c) · [`00b97b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97ad8.md#insn-00b97b30) · [`00b97b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97ad8.md#insn-00b97b34)
- 新版 `00b97f44`（命令位置の公開資料なし）

~~~diff
- 00b97b1c ["INT_ADD", "register:40f0:8", ["const:b97b1c:8", "const:4:8"]]
- 00b97b1c ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b97f44 ["INT_ADD", "register:40f0:8", ["const:b97f44:8", "const:4:8"]]
+ 00b97f44 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b97b1c bytes 2d040394
+ 00b97f44 bytes 23040394
- 00b97b30 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00b97b30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b97b30 bytes e00f803d
- 00b97b34 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b97b34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b97b34 bytes e82300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b1789eea21c599cce83388677d5ab93"></a>

### [`00b97c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97c78.md) → [`00b980a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b980a0.md) FUN_00b980a0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b7cd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cd08.md) [`00b96934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96934.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md) [`00c5bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbe0.md)
- 新版 呼出元 2件 [`00b7d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d130.md) [`00b96d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b96d5c.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md) [`00c5bfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 91.35% / 新版 91.35%

CFGの説明率　旧版 2.63% / 新版 2.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97cfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97d48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97d70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b97cac",
      "PARAM",
      [
        "storage",
        "002a998d",
        null,
        null
      ]
    ],
    [
      "unmatched:00b97ccc",
      "PARAM",
      [
        "storage",
        "002b0731",
        null,
        null
      ]
    ],
    [
      "unmatched:00b97cfc",
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
      "00b980d4",
      "PARAM",
      [
        "storage",
        "002a9a5a",
        null,
        null
      ]
    ],
    [
      "00b980f4",
      "PARAM",
      [
        "storage",
        "002b0771",
        null,
        null
      ]
    ],
    [
      "00b98124",
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

- 旧版 [`00b97cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97c78.md#insn-00b97cbc) · [`00b97ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97c78.md#insn-00b97ce8) · [`00b97cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97c78.md#insn-00b97cfc)
- 新版 `00b980e4`（命令位置の公開資料なし） · `00b98110`（命令位置の公開資料なし）

~~~diff
- 00b97cbc ["INT_ADD", "register:40f0:8", ["const:b97cbc:8", "const:4:8"]]
- 00b97cbc ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b980e4 ["INT_ADD", "register:40f0:8", ["const:b980e4:8", "const:4:8"]]
+ 00b980e4 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b97cbc bytes c5030394
+ 00b980e4 bytes bb030394
- 00b97ce8 ["INT_ADD", "register:40f0:8", ["const:b97ce8:8", "const:4:8"]]
- 00b97ce8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b98110 ["INT_ADD", "register:40f0:8", ["const:b98110:8", "const:4:8"]]
+ 00b98110 ["CALL", null, ["callee:00c57f80:8"]]
- 00b97ce8 bytes a6ff0294
+ 00b98110 bytes 9cff0294
- 00b97cfc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b97cfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b97cfc bytes e83300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-004aec0ce78d92933310d5faa8f6e698"></a>

### [`00b97e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97e18.md) → [`00b98240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98240.md) FUN_00b98240

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b7d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d260.md) [`00b96da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96da0.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md) [`00c5bc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc20.md)
- 新版 呼出元 2件 [`00b7d688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d688.md) [`00b971c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b971c8.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md) [`00c5c020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c020.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.35% / 新版 91.35%

CFGの説明率　旧版 46.88% / 新版 68.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97e3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b98264"
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
      "unmatched:00b97e3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b97e44",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c020"
      ]
    ],
    [
      "unmatched:00b97e4c",
      "PARAM",
      [
        "storage",
        "002a998d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b98264",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b9826c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c020"
      ]
    ],
    [
      "00b98274",
      "PARAM",
      [
        "storage",
        "002a9a5a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97e18.md#insn-00b97e3c) · [`00b97e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97e18.md#insn-00b97e44) · [`00b97e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97e18.md#insn-00b97e5c)
- 新版 `00b98284`（命令位置の公開資料なし）

~~~diff
- 00b97e3c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b97e3c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b97e3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b97e3c bytes a8831df8
- 00b97e44 ["INT_ADD", "register:40f0:8", ["const:b97e44:8", "const:4:8"]]
- 00b97e44 ["CALL", null, ["callee:00c5c020:8"]]
- 00b97e44 bytes 770f0394
- 00b97e5c ["INT_ADD", "register:40f0:8", ["const:b97e5c:8", "const:4:8"]]
- 00b97e5c ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b98284 ["INT_ADD", "register:40f0:8", ["const:b98284:8", "const:4:8"]]
+ 00b98284 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b97e5c bytes 5d030394
+ 00b98284 bytes 53030394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebbb9af990892094fec528b827870d63"></a>

### [`00b97fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97fb8.md) → [`00b983e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b983e0.md) FUN_00b983e0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b76904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md) [`00b96fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96fd8.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md) [`00c5bc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc30.md)
- 新版 呼出元 2件 [`00b76d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76d2c.md) [`00b97400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97400.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md) [`00c5c030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c030.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 80.00% / 新版 86.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97fdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98010"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98014"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b97fdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b97fe4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c030"
      ]
    ],
    [
      "unmatched:00b97fec",
      "PARAM",
      [
        "storage",
        "002a998d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b98404",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b9840c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c030"
      ]
    ],
    [
      "00b98414",
      "PARAM",
      [
        "storage",
        "002a9a5a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97fb8.md#insn-00b97fdc) · [`00b97fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97fb8.md#insn-00b97fe4) · [`00b97ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97fb8.md#insn-00b97ffc)
- 新版 `00b98424`（命令位置の公開資料なし）

~~~diff
- 00b97fdc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b97fdc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b97fdc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b97fdc bytes a8831df8
- 00b97fe4 ["INT_ADD", "register:40f0:8", ["const:b97fe4:8", "const:4:8"]]
- 00b97fe4 ["CALL", null, ["callee:00c5c030:8"]]
- 00b97fe4 bytes 130f0394
- 00b97ffc ["INT_ADD", "register:40f0:8", ["const:b97ffc:8", "const:4:8"]]
- 00b97ffc ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b98424 ["INT_ADD", "register:40f0:8", ["const:b98424:8", "const:4:8"]]
+ 00b98424 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b97ffc bytes f5020394
+ 00b98424 bytes eb020394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83fac7a0d17e1d0e005ba34682ed78eb"></a>

### [`00b98158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98158.md) → [`00b98580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98580.md) FUN_00b98580

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 2件 [`00b7da24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7da24.md) [`00b9720c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b9720c.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md) [`00c5bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbe0.md)
- 新版 呼出元 2件 [`00b7de4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7de4c.md) [`00b97634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97634.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md) [`00c5bfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 65.22% / 新版 65.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b985b4",
      "incomplete_value": false,
      "site": "00b985c4",
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
            "const:a5a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9818c",
      "incomplete_value": false,
      "site": "00b9819c",
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
            "const:98d:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b985d4",
      "incomplete_value": false,
      "site": "00b985f0",
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
            "const:771:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b981ac",
      "incomplete_value": false,
      "site": "00b981c8",
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
            "const:731:8"
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
      "definition_site": "00b9864c",
      "incomplete_value": false,
      "site": "00b98668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:93b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98224",
      "incomplete_value": false,
      "site": "00b98240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:8fb:8"
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
      "00b985b4",
      "PARAM",
      [
        "storage",
        "002a998d",
        null,
        null
      ]
    ],
    [
      "00b985d4",
      "PARAM",
      [
        "storage",
        "002b0731",
        null,
        null
      ]
    ],
    [
      "00b9864c",
      "PARAM",
      [
        "storage",
        "002b38fb",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b985b4",
      "PARAM",
      [
        "storage",
        "002a9a5a",
        null,
        null
      ]
    ],
    [
      "00b985d4",
      "PARAM",
      [
        "storage",
        "002b0771",
        null,
        null
      ]
    ],
    [
      "00b9864c",
      "PARAM",
      [
        "storage",
        "002b393b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9819c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98158.md#insn-00b9819c) · [`00b981c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98158.md#insn-00b981c8) · [`00b98240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98158.md#insn-00b98240)
- 新版 `00b985c4`（命令位置の公開資料なし） · `00b985f0`（命令位置の公開資料なし） · `00b98668`（命令位置の公開資料なし）

~~~diff
- 00b9819c ["INT_ADD", "register:40f0:8", ["const:b9819c:8", "const:4:8"]]
- 00b9819c ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b985c4 ["INT_ADD", "register:40f0:8", ["const:b985c4:8", "const:4:8"]]
+ 00b985c4 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b9819c bytes 8d020394
+ 00b985c4 bytes 83020394
- 00b981c8 ["INT_ADD", "register:40f0:8", ["const:b981c8:8", "const:4:8"]]
- 00b981c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b985f0 ["INT_ADD", "register:40f0:8", ["const:b985f0:8", "const:4:8"]]
+ 00b985f0 ["CALL", null, ["callee:00c57f80:8"]]
- 00b981c8 bytes 6efe0294
+ 00b985f0 bytes 64fe0294
- 00b98240 ["INT_ADD", "register:40f0:8", ["const:b98240:8", "const:4:8"]]
- 00b98240 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b98668 ["INT_ADD", "register:40f0:8", ["const:b98668:8", "const:4:8"]]
+ 00b98668 ["CALL", null, ["callee:00c57f80:8"]]
- 00b98240 bytes 50fe0294
+ 00b98668 bytes 46fe0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7a018f29bc00ad6869d9e01fc3c6e2e"></a>

### [`00b982f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b982f8.md) → [`00b98720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98720.md) FUN_00b98720

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b77c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md) [`00b97448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97448.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md) [`00c5bbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbf0.md)
- 新版 呼出元 2件 [`00b780bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b780bc.md) [`00b97870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97870.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md) [`00c5bff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bff0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 86.36% / 新版 76.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b98318",
      "incomplete_value": false,
      "site": "00b98324",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b9832c",
      "incomplete_value": false,
      "site": "00b9833c",
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
            "const:98d:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b98774",
      "incomplete_value": false,
      "site": "00b98790",
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
            "const:771:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9834c",
      "incomplete_value": false,
      "site": "00b98368",
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
            "const:731:8"
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
      "unmatched:00b9832c",
      "PARAM",
      [
        "storage",
        "002a998d",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9834c",
      "PARAM",
      [
        "storage",
        "002b0731",
        null,
        null
      ]
    ],
    [
      "unmatched:00b983c4",
      "PARAM",
      [
        "storage",
        "002b38fb",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b98754",
      "PARAM",
      [
        "storage",
        "002a9a5a",
        null,
        null
      ]
    ],
    [
      "00b98774",
      "PARAM",
      [
        "storage",
        "002b0771",
        null,
        null
      ]
    ],
    [
      "00b987ec",
      "PARAM",
      [
        "storage",
        "002b393b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b982f8.md#insn-00b98324) · [`00b9833c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b982f8.md#insn-00b9833c) · [`00b98368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b982f8.md#insn-00b98368)
- 新版 `00b9874c`（命令位置の公開資料なし） · `00b98764`（命令位置の公開資料なし） · `00b98790`（命令位置の公開資料なし）

~~~diff
- 00b98324 ["INT_ADD", "register:40f0:8", ["const:b98324:8", "const:4:8"]]
- 00b98324 ["CALL", null, ["callee:00c5bff0:8"]]
+ 00b9874c ["INT_ADD", "register:40f0:8", ["const:b9874c:8", "const:4:8"]]
+ 00b9874c ["CALL", null, ["callee:00c5bff0:8"]]
- 00b98324 bytes 330e0394
+ 00b9874c bytes 290e0394
- 00b9833c ["INT_ADD", "register:40f0:8", ["const:b9833c:8", "const:4:8"]]
- 00b9833c ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b98764 ["INT_ADD", "register:40f0:8", ["const:b98764:8", "const:4:8"]]
+ 00b98764 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b9833c bytes 25020394
+ 00b98764 bytes 1b020394
- 00b98368 ["INT_ADD", "register:40f0:8", ["const:b98368:8", "const:4:8"]]
- 00b98368 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b98790 ["INT_ADD", "register:40f0:8", ["const:b98790:8", "const:4:8"]]
+ 00b98790 ["CALL", null, ["callee:00c57f80:8"]]
- 00b98368 bytes 06fe0294
+ 00b98790 bytes fcfd0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2be486485b32b21ffb104b9389211ced"></a>

### [`00b98498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98498.md) → [`00b988c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b988c0.md) FUN_00b988c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b7e068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e068.md) [`00b9767c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b9767c.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md) [`00c5bc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc00.md)
- 新版 呼出元 2件 [`00b7e490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7e490.md) [`00b97aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97aa4.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md) [`00c5c000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 40.74% / 新版 42.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b984bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98568"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9856c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b984bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b984c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c000"
      ]
    ],
    [
      "unmatched:00b984cc",
      "PARAM",
      [
        "storage",
        "002a998d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b988e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b988ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c000"
      ]
    ],
    [
      "00b988f4",
      "PARAM",
      [
        "storage",
        "002a9a5a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b984bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98498.md#insn-00b984bc) · [`00b984c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98498.md#insn-00b984c4) · [`00b984dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98498.md#insn-00b984dc)
- 新版 `00b98904`（命令位置の公開資料なし）

~~~diff
- 00b984bc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b984bc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b984bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b984bc bytes a8831df8
- 00b984c4 ["INT_ADD", "register:40f0:8", ["const:b984c4:8", "const:4:8"]]
- 00b984c4 ["CALL", null, ["callee:00c5c000:8"]]
- 00b984c4 bytes cf0d0394
- 00b984dc ["INT_ADD", "register:40f0:8", ["const:b984dc:8", "const:4:8"]]
- 00b984dc ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b98904 ["INT_ADD", "register:40f0:8", ["const:b98904:8", "const:4:8"]]
+ 00b98904 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b984dc bytes bd010394
+ 00b98904 bytes b3010394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcbe26340e395b6af71e86fd0e2860dd"></a>

### [`00b98638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98638.md) → [`00b98a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98a60.md) FUN_00b98a60

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b7e52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e52c.md) [`00b978ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b978ac.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md) [`00c5bc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc10.md)
- 新版 呼出元 2件 [`00b7e954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7e954.md) [`00b97cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97cd4.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md) [`00c5c010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 80.00% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9863c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98640"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98640"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9863c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b98640",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9865c",
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
      "00b98a64",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b98a68",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b98a84",
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

- 旧版 [`00b9863c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98638.md#insn-00b9863c) · [`00b98640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98638.md#insn-00b98640) · [`00b9865c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98638.md#insn-00b9865c)

~~~diff
- 00b9863c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b9863c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b9863c bytes f54b00f9
- 00b98640 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b98640 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b98640 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b98640 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b98640 bytes f44f0aa9
- 00b9865c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b9865c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b9865c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b9865c bytes a8831df8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-025fc74869ea17a432259845ea8d799f"></a>

### [`00b987e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b987e0.md) → [`00b98c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98c08.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b987f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b987e0.md#insn-00b987f4)
- 新版 `00b98c1c`（命令位置の公開資料なし）

~~~diff
- 00b987f4 ["INT_ADD", "register:40f0:8", ["const:b987f4:8", "const:4:8"]]
- 00b987f4 ["CALL", null, ["callee:00c5d0e0:8"]]
+ 00b98c1c ["INT_ADD", "register:40f0:8", ["const:b98c1c:8", "const:4:8"]]
+ 00b98c1c ["CALL", null, ["callee:00c5d0e0:8"]]
- 00b987f4 bytes 3b110394
+ 00b98c1c bytes 31110394
~~~


<a id="compare-22a1dbb0bd85eddc344fef1d1d5b558b"></a>

### [`00b98808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98808.md) → [`00b98c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98c30.md) _ZTv0_n24_NSt6__ndk113basic_istreamIcNS_11char_traitsIcEEED1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b98818",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5d0e0"
      ]
    ]
  ],
  "added": [
    [
      "00b98c40",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5d0e0"
      ]
    ]
  ]
}
~~~


<a id="compare-75ed46867ef3ae3c55cd9fab426d7c86"></a>

### [`00b9884c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b9884c.md) → [`00b98c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98c74.md) FUN_00b98c74

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 64.52% / 新版 64.52%

CFGの説明率　旧版 16.67% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98880"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98884"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98888"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b98860",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b98864",
      "READ",
      [
        "storage",
        "00c9a7c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b98880",
      "DATA",
      [
        "storage",
        "00c90690",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b98c88",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00b98c8c",
      "READ",
      [
        "storage",
        "00c9abc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b98ca8",
      "DATA",
      [
        "storage",
        "00c90a90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b9884c.md#insn-00b98880) · [`00b98884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b9884c.md#insn-00b98884) · [`00b98888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b9884c.md#insn-00b98888)

~~~diff
- 00b98880 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b98880 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:8"]]
- 00b98880 bytes 0b0000f9
- 00b98884 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:80:8"]]
- 00b98884 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4060:8"]]
- 00b98884 bytes 0c4000f9
- 00b98888 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b98888 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b98888 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:10:8"]]
- 00b98888 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b98888 bytes 082401a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5068fb6207febe3782d950ff8aa7fccc"></a>

### [`00b988c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b988c8.md) → [`00b98cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98cf0.md) FUN_00b98cf0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b98d14",
      "incomplete_value": true,
      "site": "00b98d14",
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
      "definition_site": "00b988ec",
      "incomplete_value": true,
      "site": "00b988ec",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b98d18",
      "incomplete_value": true,
      "site": "00b98d18",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b988f0",
      "incomplete_value": true,
      "site": "00b988f0",
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
            "const:68:8"
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
      "definition_site": "00b98d30",
      "incomplete_value": true,
      "site": "00b98d30",
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
      "definition_site": "00b98908",
      "incomplete_value": true,
      "site": "00b98908",
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
      "00b98d00",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "00b98d14",
      "DATA",
      [
        "storage",
        "00c90690",
        null,
        "pointer"
      ]
    ],
    [
      "00b98d18",
      "DATA",
      [
        "storage",
        "00c906e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b98d00",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00b98d14",
      "DATA",
      [
        "storage",
        "00c90a90",
        null,
        "pointer"
      ]
    ],
    [
      "00b98d18",
      "DATA",
      [
        "storage",
        "00c90ae0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b988d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b988c8.md#insn-00b988d8) · [`00b988fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b988c8.md#insn-00b988fc) · [`00b98914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b988c8.md#insn-00b98914)
- 新版 `00b98d00`（命令位置の公開資料なし） · `00b98d24`（命令位置の公開資料なし） · `00b98d3c`（命令位置の公開資料なし）

~~~diff
- 00b988d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:818:8"]]
- 00b988d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b98d00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
+ 00b98d00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b988d8 bytes 080d44f9
+ 00b98d00 bytes 080d46f9
- 00b988fc ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:7c0:8"]]
- 00b988fc ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b98d24 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:bc0:8"]]
+ 00b98d24 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00b988fc bytes 4ae143f9
+ 00b98d24 bytes 4ae145f9
- 00b98914 ["INT_ADD", "register:40f0:8", ["const:b98914:8", "const:4:8"]]
- 00b98914 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b98d3c ["INT_ADD", "register:40f0:8", ["const:b98d3c:8", "const:4:8"]]
+ 00b98d3c ["CALL", null, ["callee:00c57eb0:8"]]
- 00b98914 bytes 67fc0294
+ 00b98d3c bytes 5dfc0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-743c7fa2b86a938c2ed53d71fc8f2128"></a>

### [`00b98940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98940.md) → [`00b98d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98d68.md) FUN_00b98d68

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b98d8c",
      "incomplete_value": true,
      "site": "00b98d8c",
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
      "definition_site": "00b98964",
      "incomplete_value": true,
      "site": "00b98964",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b98d90",
      "incomplete_value": true,
      "site": "00b98d90",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98968",
      "incomplete_value": true,
      "site": "00b98968",
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
            "const:68:8"
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
      "definition_site": "00b98da8",
      "incomplete_value": true,
      "site": "00b98da8",
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
      "definition_site": "00b98980",
      "incomplete_value": true,
      "site": "00b98980",
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
      "00b98d78",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "00b98d8c",
      "DATA",
      [
        "storage",
        "00c90690",
        null,
        "pointer"
      ]
    ],
    [
      "00b98d90",
      "DATA",
      [
        "storage",
        "00c906e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b98d78",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00b98d8c",
      "DATA",
      [
        "storage",
        "00c90a90",
        null,
        "pointer"
      ]
    ],
    [
      "00b98d90",
      "DATA",
      [
        "storage",
        "00c90ae0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98940.md#insn-00b98950) · [`00b98974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98940.md#insn-00b98974) · [`00b9898c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98940.md#insn-00b9898c)
- 新版 `00b98d78`（命令位置の公開資料なし） · `00b98d9c`（命令位置の公開資料なし） · `00b98db4`（命令位置の公開資料なし）

~~~diff
- 00b98950 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:818:8"]]
- 00b98950 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b98d78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
+ 00b98d78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98950 bytes 080d44f9
+ 00b98d78 bytes 080d46f9
- 00b98974 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:7c0:8"]]
- 00b98974 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b98d9c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:bc0:8"]]
+ 00b98d9c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98974 bytes 4ae143f9
+ 00b98d9c bytes 4ae145f9
- 00b9898c ["INT_ADD", "register:40f0:8", ["const:b9898c:8", "const:4:8"]]
- 00b9898c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b98db4 ["INT_ADD", "register:40f0:8", ["const:b98db4:8", "const:4:8"]]
+ 00b98db4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b9898c bytes 49fc0294
+ 00b98db4 bytes 3ffc0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-213e4e05ade5089a2ececd45934a6020"></a>

### [`00b989c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b989c0.md) → [`00b98de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98de8.md) FUN_00b98de8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b98e08",
      "incomplete_value": true,
      "site": "00b98e14",
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
      "definition_site": "00b989e0",
      "incomplete_value": true,
      "site": "00b989ec",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b98e18",
      "incomplete_value": true,
      "site": "00b98e18",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b989f0",
      "incomplete_value": true,
      "site": "00b989f0",
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
            "const:68:8"
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
      "definition_site": "00b98e30",
      "incomplete_value": true,
      "site": "00b98e30",
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
      "definition_site": "00b98a08",
      "incomplete_value": true,
      "site": "00b98a08",
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
      "00b98e00",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "00b98e14",
      "DATA",
      [
        "storage",
        "00c90690",
        null,
        "pointer"
      ]
    ],
    [
      "00b98e18",
      "DATA",
      [
        "storage",
        "00c906e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b98e00",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00b98e14",
      "DATA",
      [
        "storage",
        "00c90a90",
        null,
        "pointer"
      ]
    ],
    [
      "00b98e18",
      "DATA",
      [
        "storage",
        "00c90ae0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b989d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b989c0.md#insn-00b989d8) · [`00b989f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b989c0.md#insn-00b989f4) · [`00b98a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b989c0.md#insn-00b98a00)
- 新版 `00b98e00`（命令位置の公開資料なし） · `00b98e28`（命令位置の公開資料なし）

~~~diff
- 00b989d8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:818:8"]]
- 00b989d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b98e00 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c18:8"]]
+ 00b98e00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b989d8 bytes 290d44f9
+ 00b98e00 bytes 290d46f9
- 00b989f4 ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 00b989f4 bytes 0a0800d0
- 00b98a00 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:7c0:8"]]
- 00b98a00 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b98e28 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:bc0:8"]]
+ 00b98e28 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98a00 bytes 4ae143f9
+ 00b98e28 bytes 4ae145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d35799267e8b71fbfdb9d2cdc63d4da"></a>

### [`00b98a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98a40.md) → [`00b98e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98e68.md) FUN_00b98e68

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b98e88",
      "incomplete_value": true,
      "site": "00b98e94",
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
      "definition_site": "00b98a60",
      "incomplete_value": true,
      "site": "00b98a6c",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b98e98",
      "incomplete_value": true,
      "site": "00b98e98",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98a70",
      "incomplete_value": true,
      "site": "00b98a70",
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
            "const:68:8"
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
      "definition_site": "00b98eb0",
      "incomplete_value": true,
      "site": "00b98eb0",
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
      "definition_site": "00b98a88",
      "incomplete_value": true,
      "site": "00b98a88",
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
      "00b98e80",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "00b98e94",
      "DATA",
      [
        "storage",
        "00c90690",
        null,
        "pointer"
      ]
    ],
    [
      "00b98e98",
      "DATA",
      [
        "storage",
        "00c906e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b98e80",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00b98e94",
      "DATA",
      [
        "storage",
        "00c90a90",
        null,
        "pointer"
      ]
    ],
    [
      "00b98e98",
      "DATA",
      [
        "storage",
        "00c90ae0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98a40.md#insn-00b98a58) · [`00b98a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98a40.md#insn-00b98a74) · [`00b98a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98a40.md#insn-00b98a80)
- 新版 `00b98e80`（命令位置の公開資料なし） · `00b98ea8`（命令位置の公開資料なし）

~~~diff
- 00b98a58 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:818:8"]]
- 00b98a58 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b98e80 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c18:8"]]
+ 00b98e80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98a58 bytes 290d44f9
+ 00b98e80 bytes 290d46f9
- 00b98a74 ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 00b98a74 bytes 0a0800d0
- 00b98a80 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:7c0:8"]]
- 00b98a80 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b98ea8 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:bc0:8"]]
+ 00b98ea8 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98a80 bytes 4ae143f9
+ 00b98ea8 bytes 4ae145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a08ee6072a0b5b3db3f6afff9f73310"></a>

### [`00b98ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98ac8.md) → [`00b98ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98ef0.md) FUN_00b98ef0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b98f0c",
      "incomplete_value": true,
      "site": "00b98f10",
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
      "definition_site": "00b98ae4",
      "incomplete_value": true,
      "site": "00b98ae8",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b98f2c",
      "incomplete_value": true,
      "site": "00b98f2c",
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
      "definition_site": "00b98b04",
      "incomplete_value": true,
      "site": "00b98b04",
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
      "00b98f04",
      "READ",
      [
        "storage",
        "00c9a7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b98f10",
      "DATA",
      [
        "storage",
        "00c90808",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b98f24",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b98f04",
      "READ",
      [
        "storage",
        "00c9abc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b98f10",
      "DATA",
      [
        "storage",
        "00c90c08",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b98f24",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98ac8.md#insn-00b98adc) · [`00b98af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98ac8.md#insn-00b98af4) · [`00b98afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98ac8.md#insn-00b98afc)
- 新版 `00b98f04`（命令位置の公開資料なし） · `00b98f1c`（命令位置の公開資料なし） · `00b98f24`（命令位置の公開資料なし）

~~~diff
- 00b98adc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
- 00b98adc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b98f04 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
+ 00b98f04 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98adc bytes 29e143f9
+ 00b98f04 bytes 29e145f9
- 00b98af4 ["INT_ADD", "register:40f0:8", ["const:b98af4:8", "const:4:8"]]
- 00b98af4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b98f1c ["INT_ADD", "register:40f0:8", ["const:b98f1c:8", "const:4:8"]]
+ 00b98f1c ["CALL", null, ["callee:00c57eb0:8"]]
- 00b98af4 bytes effb0294
+ 00b98f1c bytes e5fb0294
- 00b98afc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:448:8"]]
- 00b98afc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b98f24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:848:8"]]
+ 00b98f24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98afc bytes 082542f9
+ 00b98f24 bytes 082544f9
~~~


<a id="compare-a012b3500d26fa33bd6cdf824adc4694"></a>

### [`00b98b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98b18.md) → [`00b98f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98f40.md) FUN_00b98f40

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b98f5c",
      "incomplete_value": true,
      "site": "00b98f60",
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
      "definition_site": "00b98b34",
      "incomplete_value": true,
      "site": "00b98b38",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b98f80",
      "incomplete_value": true,
      "site": "00b98f80",
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
      "definition_site": "00b98b58",
      "incomplete_value": true,
      "site": "00b98b58",
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
      "00b98f54",
      "READ",
      [
        "storage",
        "00c9a7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b98f60",
      "DATA",
      [
        "storage",
        "00c90808",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b98f74",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b98f54",
      "READ",
      [
        "storage",
        "00c9abc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b98f60",
      "DATA",
      [
        "storage",
        "00c90c08",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b98f74",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98b18.md#insn-00b98b2c) · [`00b98b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98b18.md#insn-00b98b44) · [`00b98b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98b18.md#insn-00b98b4c)
- 新版 `00b98f54`（命令位置の公開資料なし） · `00b98f6c`（命令位置の公開資料なし） · `00b98f74`（命令位置の公開資料なし）

~~~diff
- 00b98b2c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
- 00b98b2c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b98f54 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
+ 00b98f54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98b2c bytes 29e143f9
+ 00b98f54 bytes 29e145f9
- 00b98b44 ["INT_ADD", "register:40f0:8", ["const:b98b44:8", "const:4:8"]]
- 00b98b44 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b98f6c ["INT_ADD", "register:40f0:8", ["const:b98f6c:8", "const:4:8"]]
+ 00b98f6c ["CALL", null, ["callee:00c57eb0:8"]]
- 00b98b44 bytes dbfb0294
+ 00b98f6c bytes d1fb0294
- 00b98b4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:448:8"]]
- 00b98b4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b98f74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:848:8"]]
+ 00b98f74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98b4c bytes 082542f9
+ 00b98f74 bytes 082544f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

