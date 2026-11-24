# v16.0.1 → v16.0.2 · 最優先の変更候補 (30)

[一覧の目次](README.md)

<a id="compare-27486920cef9ee82a8a87bff7fc336de"></a>

### [`00688458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00688/00688458.md) → [`00688498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00688/00688498.md) FUN_00688498

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) [`00a79c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a79/00a79c04.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00688294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00688/00688294.md) [`00688620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00688/00688620.md) [`00691e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e2c.md) [`00691e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e54.md)
- 新版 呼出元 2件 [`00a75e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a75/00a75e1c.md) [`00a79c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a79/00a79c74.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`006882d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00688/006882d4.md) [`00688660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00688/00688660.md) [`00691e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md) [`00691eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691eac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00688628",
      "incomplete_value": false,
      "site": "0068862c",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006885e8",
      "incomplete_value": false,
      "site": "006885ec",
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
    "ordinal": 8,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00688628",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00688628",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006885ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00688/00688458.md#insn-006885ec) · [`006884c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00688/00688458.md#insn-006884c4) · [`006884cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00688/00688458.md#insn-006884cc)
- 新版 [`0068862c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00688/00688498.md#insn-0068862c) · [`00688504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00688/00688498.md#insn-00688504) · [`0068850c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00688/00688498.md#insn-0068850c)

~~~diff
- 006885ec ["INT_ADD", "register:40f0:8", ["const:6885ec:8", "const:4:8"]]
- 006885ec ["CALL", null, ["callee:00442970:8"]]
+ 0068862c ["INT_ADD", "register:40f0:8", ["const:68862c:8", "const:4:8"]]
+ 0068862c ["CALL", null, ["callee:00442970:8"]]
- 006885ec bytes d1e8f697
+ 0068862c bytes d1e8f697
- 006884c4 ["INT_ADD", "register:40f0:8", ["const:6884c4:8", "const:4:8"]]
- 006884c4 ["CALL", null, ["callee:00688660:8"]]
+ 00688504 ["INT_ADD", "register:40f0:8", ["const:688504:8", "const:4:8"]]
+ 00688504 ["CALL", null, ["callee:00688660:8"]]
- 006884c4 bytes 57000094
+ 00688504 bytes 57000094
- 006884cc ["INT_ADD", "register:40f0:8", ["const:6884cc:8", "const:4:8"]]
- 006884cc ["CALL", null, ["callee:00851550:8"]]
+ 0068850c ["INT_ADD", "register:40f0:8", ["const:68850c:8", "const:4:8"]]
+ 0068850c ["CALL", null, ["callee:00851550:8"]]
- 006884cc bytes 0b240794
+ 0068850c bytes 11240794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ca81a2d22236a8bfb55cd0bee3f45b0"></a>

### [`00689ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689ab4.md) → [`00689b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/00689b0c.md) FUN_00689b0c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`005e7f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7f3c.md) [`005e8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8060.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`005e7f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7f7c.md) [`005e80a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e8/005e80a0.md) [`005f57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f5/005f57d0.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 76.67% / 新版 79.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00689b8c",
      "incomplete_value": false,
      "site": "00689b90",
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
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00689ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689ab4.md#insn-00689ab8) · [`00689adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689ab4.md#insn-00689adc) · [`00689b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689ab4.md#insn-00689b4c)
- 新版 [`00689b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/00689b0c.md#insn-00689b10) · [`00689b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/00689b0c.md#insn-00689b34) · [`00689ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/00689b0c.md#insn-00689ba4)

~~~diff
- 00689ab8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00689ab8 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00689b10 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00689b10 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00689ab8 bytes e80300b4
+ 00689b10 bytes e80300b4
- 00689adc ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00689adc ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00689b34 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00689b34 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00689adc bytes 890200b4
+ 00689b34 bytes 890200b4
- 00689b4c ["INT_ADD", "register:40f0:8", ["const:689b4c:8", "const:4:8"]]
- 00689b4c ["CALL", null, ["callee:00c57f60:8"]]
+ 00689ba4 ["INT_ADD", "register:40f0:8", ["const:689ba4:8", "const:4:8"]]
+ 00689ba4 ["CALL", null, ["callee:00c57f60:8"]]
- 00689b4c bytes d1381794
+ 00689ba4 bytes ef381794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f92884f477354ef8c275b8a1f579e5a2"></a>

### [`00689cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689cbc.md) → [`00689d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/00689d14.md) FUN_00689d14

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) [`00afe40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afe40c.md) [`00aff62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00aff62c.md) · 呼出先 7件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`006877c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/006877c8.md) [`00691e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e2c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 6件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00a52034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a52/00a52034.md) [`00afe4a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afe4a8.md) [`00aff6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aff/00aff6c8.md) · 呼出先 7件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md) [`00687808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687808.md) [`00691e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.79% / 新版 94.79%

CFGの説明率　旧版 66.67% / 新版 63.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00689d70"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00689de4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00689e00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00689d70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00689db8"
      ]
    ],
    [
      "unmatched:00689de4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00689da0"
      ]
    ],
    [
      "unmatched:00689e00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00689e8c"
      ]
    ]
  ],
  "added": [
    [
      "00689dc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00689db8"
      ]
    ],
    [
      "00689e3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00689da0"
      ]
    ],
    [
      "00689e58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00689e8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00689d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689cbc.md#insn-00689d70) · [`00689de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689cbc.md#insn-00689de4)
- 新版 [`00689dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/00689d14.md#insn-00689dc8)

~~~diff
- 00689d70 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00689d70 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00689d70 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00689d70 ["CBRANCH", null, ["local:b8:8", "tmp:2:1"]]
- 00689d70 bytes 8cffff54
+ 00689dc8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00689dc8 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00689dc8 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00689dc8 ["CBRANCH", null, ["local:b9:8", "tmp:2:1"]]
+ 00689dc8 bytes 8cffff54
- 00689de4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00689de4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00689de4 bytes 21fbff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c70831e307c8f6fdaa7055ecfc94cd3f"></a>

### [`00689e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689e3c.md) → [`00689e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/00689e94.md) FUN_00689e94

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 7件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`006877c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/006877c8.md) [`00691e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e2c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 7件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md) [`00687808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687808.md) [`00691e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.22% / 新版 82.22%

CFGの説明率　旧版 46.67% / 新版 48.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00689e3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00689e3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00689e40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00689e3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00689e40",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00689e44",
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
      "00689e94",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00689e98",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00689e9c",
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

- 旧版 [`00689e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689e3c.md#insn-00689e3c) · [`00689e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689e3c.md#insn-00689e40) · [`00689e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689e3c.md#insn-00689e44)

~~~diff
- 00689e3c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00689e3c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00689e3c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00689e3c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00689e3c bytes fd7bbca9
- 00689e40 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00689e40 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00689e40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00689e40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00689e40 bytes f85f01a9
- 00689e44 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00689e44 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00689e44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00689e44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00689e44 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44b4ae8d5f860d2fc003f95a13698993"></a>

### [`00689fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689fa4.md) → [`00689ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/00689ffc.md) FUN_00689ffc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 7件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`006877c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/006877c8.md) [`00691e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e2c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 7件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md) [`00687808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687808.md) [`00691e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 99.21% / 新版 99.21%

CFGの説明率　旧版 96.61% / 新版 95.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0068a1d4",
      "incomplete_value": false,
      "site": "0068a1d8",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0068a17c",
      "incomplete_value": false,
      "site": "0068a180",
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
      "0068a1d4",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0068a1d4",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689fa4.md#insn-0068a180) · [`00689fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689fa4.md#insn-00689fd4) · [`00689fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689fa4.md#insn-00689fe8)
- 新版 [`0068a1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/00689ffc.md#insn-0068a1d8) · [`0068a02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/00689ffc.md#insn-0068a02c) · [`0068a040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/00689ffc.md#insn-0068a040)

~~~diff
- 0068a180 ["INT_ADD", "register:40f0:8", ["const:68a180:8", "const:4:8"]]
- 0068a180 ["CALL", null, ["callee:00442970:8"]]
+ 0068a1d8 ["INT_ADD", "register:40f0:8", ["const:68a1d8:8", "const:4:8"]]
+ 0068a1d8 ["CALL", null, ["callee:00442970:8"]]
- 0068a180 bytes ece1f697
+ 0068a1d8 bytes e6e1f697
- 00689fd4 ["INT_ADD", "register:40f0:8", ["const:689fd4:8", "const:4:8"]]
- 00689fd4 ["CALL", null, ["callee:00851550:8"]]
+ 0068a02c ["INT_ADD", "register:40f0:8", ["const:68a02c:8", "const:4:8"]]
+ 0068a02c ["CALL", null, ["callee:00851550:8"]]
- 00689fd4 bytes 491d0794
+ 0068a02c bytes 491d0794
- 00689fe8 ["INT_ADD", "register:40f0:8", ["const:689fe8:8", "const:4:8"]]
- 00689fe8 ["CALL", null, ["callee:00903f98:8"]]
+ 0068a040 ["INT_ADD", "register:40f0:8", ["const:68a040:8", "const:4:8"]]
+ 0068a040 ["CALL", null, ["callee:00903f98:8"]]
- 00689fe8 bytes d7e70994
+ 0068a040 bytes d6e70994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a30cdcfe92ced8e37c5c390fd6b7bee"></a>

### [`0068a2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a2b8.md) → [`0068a310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a310.md) FUN_0068a310

採用 · 移動量 `+0x58` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 16件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md) [`0068a19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a19c.md)
- 新版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 16件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md) [`0068a1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a1f4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 16.90% / 新版 17.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_destination` 1件, `store_value` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068a2ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068a300"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068a308"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0068a2ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:0068a2f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487e60"
      ]
    ],
    [
      "unmatched:0068a300",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0068a344",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "0068a348",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487e60"
      ]
    ],
    [
      "0068a358",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068a2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a2b8.md#insn-0068a2ec) · [`0068a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a2b8.md#insn-0068a2f0) · [`0068a300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a2b8.md#insn-0068a300)

~~~diff
- 0068a2ec ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0068a2ec ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 0068a2ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0068a2ec bytes a8831ef8
- 0068a2f0 ["INT_ADD", "register:40f0:8", ["const:68a2f0:8", "const:4:8"]]
- 0068a2f0 ["CALL", null, ["callee:00487e60:8"]]
- 0068a2f0 bytes ccf6f797
- 0068a300 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 0068a300 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0068a300 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8db76571b7a794206a45b862505c4c96"></a>

### [`0068a6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a6c4.md) → [`0068a71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a71c.md) FUN_0068a71c

採用 · 移動量 `+0x58` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0068bbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bbc8.md) · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`006924ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924ec.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`0068bc20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068bc20.md) · 呼出先 11件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md) [`00692544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692544.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.39% / 新版 84.39%

CFGの説明率　旧版 16.90% / 新版 16.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068a7c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068a7c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068a7c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0068a744",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0068a914"
      ]
    ],
    [
      "unmatched:0068a7b4",
      "READ",
      [
        "storage",
        "002a2323",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0068a7b8",
      "READ",
      [
        "storage",
        "002a232d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0068a79c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0068a914"
      ]
    ],
    [
      "0068a80c",
      "READ",
      [
        "storage",
        "002a22d6",
        null,
        "string"
      ]
    ],
    [
      "0068a810",
      "READ",
      [
        "storage",
        "002a22e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068a744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a6c4.md#insn-0068a744) · [`0068a768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a6c4.md#insn-0068a768) · [`0068a79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a6c4.md#insn-0068a79c)
- 新版 [`0068a7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a71c.md#insn-0068a7c0) · [`0068a7f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a71c.md#insn-0068a7f4)

~~~diff
- 0068a744 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0068a744 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 0068a744 ["CBRANCH", null, ["local:b29:8", "tmp:1:1"]]
- 0068a744 bytes c90b0054
- 0068a768 ["BRANCH", null, ["local:b13:8"]]
+ 0068a7c0 ["BRANCH", null, ["local:b14:8"]]
- 0068a768 bytes 0e000014
+ 0068a7c0 bytes 0e000014
- 0068a79c ["INT_ADD", "register:40f0:8", ["const:68a79c:8", "const:4:8"]]
- 0068a79c ["CALL", null, ["callee:0043bb60:8"]]
+ 0068a7f4 ["INT_ADD", "register:40f0:8", ["const:68a7f4:8", "const:4:8"]]
+ 0068a7f4 ["CALL", null, ["callee:0043bb60:8"]]
- 0068a79c bytes e1c4f697
+ 0068a7f4 bytes dbc4f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32925c0663bbf2dcbfcc8ab67b0ad06e"></a>

### [`0068aa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068aa88.md) → [`0068aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068aae0.md) FUN_0068aae0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0068bbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bbc8.md) · 呼出先 21件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00859b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b4c.md) [`0085b2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2ac.md) [`0085b2bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2bc.md)
- 新版 呼出元 1件 [`0068bc20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068bc20.md) · 呼出先 21件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00859ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859ba4.md) [`0085b304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b304.md) [`0085b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b314.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 87.67% / 新版 87.67%

CFGの説明率　旧版 73.68% / 新版 73.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0068abf8",
      "incomplete_value": true,
      "site": "0068abf8",
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
      "definition_site": "0068aba0",
      "incomplete_value": true,
      "site": "0068aba0",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0068ac6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0068ac94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0068abe0",
      "READ",
      [
        "storage",
        "002c4158",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:0068ac24",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b6eb0"
      ]
    ],
    [
      "unmatched:0068ac4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b6efc"
      ]
    ]
  ],
  "added": [
    [
      "0068abe0",
      "READ",
      [
        "storage",
        "002c4198",
        null,
        "undefined8"
      ]
    ],
    [
      "0068ac7c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b6eb0"
      ]
    ],
    [
      "0068aca4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b6efc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068abcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068aa88.md#insn-0068abcc) · [`0068ac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068aa88.md#insn-0068ac0c) · [`0068ac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068aa88.md#insn-0068ac24)
- 新版 [`0068ac24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068aae0.md#insn-0068ac24) · [`0068ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068aae0.md#insn-0068ac64)

~~~diff
- 0068abcc ["INT_ADD", "register:40f0:8", ["const:68abcc:8", "const:4:8"]]
- 0068abcc ["CALL", null, ["callee:00ac9134:8"]]
+ 0068ac24 ["INT_ADD", "register:40f0:8", ["const:68ac24:8", "const:4:8"]]
+ 0068ac24 ["CALL", null, ["callee:00ac9134:8"]]
- 0068abcc bytes 3ef91094
+ 0068ac24 bytes 44f91094
- 0068ac0c ["INT_ADD", "register:40f0:8", ["const:68ac0c:8", "const:4:8"]]
- 0068ac0c ["CALL", null, ["callee:00851550:8"]]
+ 0068ac64 ["INT_ADD", "register:40f0:8", ["const:68ac64:8", "const:4:8"]]
+ 0068ac64 ["CALL", null, ["callee:00851550:8"]]
- 0068ac0c bytes 3b1a0794
+ 0068ac64 bytes 3b1a0794
- 0068ac24 ["INT_ADD", "register:40f0:8", ["const:68ac24:8", "const:4:8"]]
- 0068ac24 ["CALL", null, ["callee:008b6eb0:8"]]
- 0068ac24 bytes 8db00894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9099165587eab186c7040c870d6678a6"></a>

### [`0068bad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bad0.md) → [`0068bb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068bb28.md) FUN_0068bb28

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00693388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693388.md) [`00693458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693458.md) [`00693cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693cb8.md) [`00693d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693d88.md) [`006944d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006944d0.md) · 呼出先 6件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f10.md) [`008b6f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f40.md) [`008b7948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7948.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 5件 [`006933e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006933e0.md) [`006934b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006934b0.md) [`00693d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693d10.md) [`00693de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693de0.md) [`00694528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694528.md) · 呼出先 6件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f68.md) [`008b6f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f98.md) [`008b79a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b79a0.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.26% / 新版 82.26%

CFGの説明率　旧版 45.45% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068bad0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068bad0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068bad4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0068bad0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0068bad4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0068bad8",
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
      "0068bb28",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0068bb2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0068bb30",
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

- 旧版 [`0068bad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bad0.md#insn-0068bad0) · [`0068bad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bad0.md#insn-0068bad4) · [`0068bad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bad0.md#insn-0068bad8)

~~~diff
- 0068bad0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0068bad0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0068bad0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0068bad0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0068bad0 bytes fd7bbda9
- 0068bad4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0068bad4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0068bad4 bytes f50b00f9
- 0068bad8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0068bad8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0068bad8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0068bad8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0068bad8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7659abc2ac9bbbd0821ba0f7670180c"></a>

### [`0068bbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bbc8.md) → [`0068bc20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068bc20.md) FUN_0068bc20

採用 · 移動量 `+0x58` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0068d948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068d/0068d948.md) [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 10件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0068a6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a6c4.md) [`0068aa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068aa88.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`0068d9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068d/0068d9a0.md) [`00a75e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a75/00a75e1c.md) · 呼出先 10件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0068a71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a71c.md) [`0068aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068aae0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.99% / 新版 88.99%

CFGの説明率　旧版 60.61% / 新版 60.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068bca4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068bca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068bcb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0068bc78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0068bd80"
      ]
    ],
    [
      "unmatched:0068bc98",
      "READ",
      [
        "storage",
        "002a33fe",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0068bc9c",
      "READ",
      [
        "storage",
        "002c2680",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0068bcd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0068bd80"
      ]
    ],
    [
      "0068bcf0",
      "READ",
      [
        "storage",
        "002a33b1",
        null,
        "string"
      ]
    ],
    [
      "0068bcf4",
      "READ",
      [
        "storage",
        "002c26c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068bc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bbc8.md#insn-0068bc6c) · [`0068bc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bbc8.md#insn-0068bc78) · [`0068bca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bbc8.md#insn-0068bca4)
- 新版 [`0068bcc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068bc20.md#insn-0068bcc4)

~~~diff
- 0068bc6c ["INT_ADD", "register:40f0:8", ["const:68bc6c:8", "const:4:8"]]
- 0068bc6c ["CALL", null, ["callee:00c57f80:8"]]
+ 0068bcc4 ["INT_ADD", "register:40f0:8", ["const:68bcc4:8", "const:4:8"]]
+ 0068bcc4 ["CALL", null, ["callee:00c57f80:8"]]
- 0068bc6c bytes 91301794
+ 0068bcc4 bytes af301794
- 0068bc78 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 0068bc78 bytes 80050054
- 0068bca4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0068bca4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0068bca4 bytes e00b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ebab1c08cfdaaf52c2c4824a9699047"></a>

### [`0068be10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068be10.md) → [`0068be68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068be68.md) FUN_0068be68

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0068d990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068d/0068d990.md) [`00a79c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a79/00a79c04.md) · 呼出先 21件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md) [`00467e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467e9c.md) [`00467ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ea4.md)
- 新版 呼出元 2件 [`0068d9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068d/0068d9e8.md) [`00a79c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a79/00a79c74.md) · 呼出先 21件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467df4.md) [`00467edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467edc.md) [`00467ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ee4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.73% / 新版 94.73%

CFGの説明率　旧版 4.55% / 新版 4.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 61件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068be10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068be10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068be14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0068be10",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:0068be14",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0068be18",
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
      "0068be68",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "0068be6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0068be70",
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

- 旧版 [`0068be10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068be10.md#insn-0068be10) · [`0068be14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068be10.md#insn-0068be14) · [`0068be18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068be10.md#insn-0068be18)

~~~diff
- 0068be10 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffff90:8"]]
- 0068be10 ["STORE", null, ["const:1b1:8", "register:8:8", "register:5160:8"]]
- 0068be10 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 0068be10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5140:8"]]
- 0068be10 bytes eb2bb96d
- 0068be14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0068be14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5120:8"]]
- 0068be14 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:8:8"]]
- 0068be14 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5100:8"]]
- 0068be14 bytes e923016d
- 0068be18 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0068be18 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0068be18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0068be18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0068be18 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-214656b343b5ed975b5d20c9ccbbd79a"></a>

### [`0068c610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068c/0068c610.md) → [`0068c668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068c/0068c668.md) FUN_0068c668

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006d9ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9ae8.md) [`009a3338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3338.md) [`00aed3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed3bc.md) · 呼出先 38件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md)
- 新版 呼出元 3件 [`006d9b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9b40.md) [`009a338c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a338c.md) [`00aed458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed458.md) · 呼出先 38件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`004709d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004709d4.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 58.16% / 新版 58.16%

CFGの説明率　旧版 17.94% / 新版 18.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 27件, `store_condition` 3件, `store_value` 3件, `unresolved_branch_alignment` 44件, `unresolved_call_alignment` 79件, `unresolved_store_alignment` 75件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068c6f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068c6f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068c774"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0068c6b0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00a46950"
      ]
    ],
    [
      "unmatched:0068c6b4",
      "READ",
      [
        "storage",
        "Stack[-0x1d0]",
        null,
        null
      ]
    ],
    [
      "unmatched:0068c6f4",
      "DATA",
      [
        "storage",
        "00c74ad0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0068c708",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00a46950"
      ]
    ],
    [
      "0068c70c",
      "READ",
      [
        "storage",
        "Stack[-0x1d0]",
        null,
        null
      ]
    ],
    [
      "0068c74c",
      "DATA",
      [
        "storage",
        "00c74ba0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068c6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068c/0068c610.md#insn-0068c6f4) · [`0068c71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068c/0068c610.md#insn-0068c71c)
- 新版 [`0068c6f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068c/0068c668.md#insn-0068c6f4) · [`0068c774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068c/0068c668.md#insn-0068c774)

~~~diff
- 0068c6f4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0068c6f4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0068c6f4 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffb0:8"]]
- 0068c6f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0068c6f4 bytes a8673ba9
+ 0068c6f4 ["COPY", "register:5040:8", ["register:4040:8"]]
+ 0068c6f4 ["COPY", "register:5048:8", ["const:0:8"]]
+ 0068c6f4 ["COPY", "register:5050:8", ["const:0:8"]]
+ 0068c6f4 ["COPY", "register:5058:8", ["const:0:8"]]
+ 0068c6f4 bytes 0201679e
- 0068c71c ["INT_ADD", "register:40f0:8", ["const:68c71c:8", "const:4:8"]]
- 0068c71c ["CALL", null, ["callee:008b7044:8"]]
+ 0068c774 ["INT_ADD", "register:40f0:8", ["const:68c774:8", "const:4:8"]]
+ 0068c774 ["CALL", null, ["callee:008b7044:8"]]
- 0068c71c bytes 34aa0894
+ 0068c774 bytes 34aa0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7784a4d0e3b40e90fc0571956bc607f"></a>

### [`0068d990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068d/0068d990.md) → [`0068d9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068d/0068d9e8.md) FUN_0068d9e8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · 呼出先 11件 [`0068be10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068be10.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6d9c.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 2件 [`00997090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00997/00997090.md) [`00ae1328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae1328.md) · 呼出先 11件 [`0068be68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068be68.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6df4.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.66% / 新版 79.66%

CFGの説明率　旧版 18.52% / 新版 17.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068d994"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068d994"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068d998"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0068d994",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0068d998",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0068d99c",
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
      "0068d9ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0068d9f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0068d9f4",
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

- 旧版 [`0068d994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068d/0068d990.md#insn-0068d994) · [`0068d998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068d/0068d990.md#insn-0068d998) · [`0068d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068d/0068d990.md#insn-0068d99c)

~~~diff
- 0068d994 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 0068d994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5160:8"]]
- 0068d994 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:8:8"]]
- 0068d994 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5140:8"]]
- 0068d994 bytes eb2b026d
- 0068d998 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 0068d998 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5120:8"]]
- 0068d998 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:8:8"]]
- 0068d998 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5100:8"]]
- 0068d998 bytes e923036d
- 0068d99c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0068d99c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0068d99c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0068d99c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0068d99c bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-067488674a90ff396017ab1ffdb89f35"></a>

### [`0068db8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068d/0068db8c.md) → [`0068dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068d/0068dbe4.md) FUN_0068dbe4

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007595dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00759/007595dc.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`006891c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/006891c8.md) [`00691e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e2c.md)
- 新版 呼出元 1件 [`00759634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00759/00759634.md) · 呼出先 8件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md) [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md) [`00689208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/00689208.md) [`00691e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.16% / 新版 66.16%

CFGの説明率　旧版 25.51% / 新版 25.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 47件, `unresolved_call_alignment` 14件, `unresolved_store_alignment` 63件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068dc80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068dc84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068dc84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0068dbfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0068dbdc"
      ]
    ],
    [
      "unmatched:0068dc04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0068dc80"
      ]
    ],
    [
      "unmatched:0068dc10",
      "READ",
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
      "0068dc54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0068dc34"
      ]
    ],
    [
      "0068dc5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0068dc80"
      ]
    ],
    [
      "0068dcac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0068dd18"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068dc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068d/0068db8c.md#insn-0068dc30) · [`0068dc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068d/0068db8c.md#insn-0068dc80) · [`0068dc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068d/0068db8c.md#insn-0068dc84)
- 新版 [`0068dc88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068d/0068dbe4.md#insn-0068dc88)

~~~diff
- 0068dc30 ["CBRANCH", null, ["local:b34:8", "register:101:1"]]
+ 0068dc88 ["CBRANCH", null, ["local:b36:8", "register:101:1"]]
- 0068dc30 bytes 60090054
+ 0068dc88 bytes 60090054
- 0068dc80 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:28:8"]]
- 0068dc80 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0068dc80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 0068dc80 bytes 1f1400f9
- 0068dc84 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0068dc84 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0068dc84 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0068dc84 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0068dc84 bytes 1f7c00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f53c45bf0fbc8a197277cb16e3c49a1"></a>

### [`0068e754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068e754.md) → [`0068e7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068e7ac.md) FUN_0068e7ac

採用 · 移動量 `+0x58` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 25件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00687904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/00687904.md) [`006924c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924c4.md)
- 新版 呼出元 1件 [`00a75e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a75/00a75e1c.md) · 呼出先 25件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00687944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687944.md) [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.91% / 新版 84.91%

CFGの説明率　旧版 35.29% / 新版 34.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068e7c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068e7c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068e7c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0068e7f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0068e7b4"
      ]
    ],
    [
      "unmatched:0068e7ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0068e7f0"
      ]
    ],
    [
      "unmatched:0068e7b4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ]
  ],
  "added": [
    [
      "0068e7f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0068e80c"
      ]
    ],
    [
      "0068e804",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0068e7f0"
      ]
    ],
    [
      "0068e80c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068e7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068e754.md#insn-0068e7ac) · [`0068e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068e754.md#insn-0068e7c4) · [`0068e7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068e754.md#insn-0068e7c8)

~~~diff
- 0068e7ac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0068e7ac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0068e7ac bytes 61ffff54
- 0068e7c4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:88:8"]]
- 0068e7c4 ["COPY", "tmp:1:4", ["const:0:4"]]
- 0068e7c4 ["COPY", "tmp:2:4", ["tmp:1:4"]]
- 0068e7c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:2:2"]]
- 0068e7c4 bytes ff130179
- 0068e7c8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0068e7c8 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 0068e7c8 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 0068e7c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0068e7c8 bytes a8533ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e1ccd017c322e0cc70b4ea6d57c17e7"></a>

### [`0068ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068ed80.md) → [`0068edd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068edd8.md) FUN_0068edd8

採用 · 移動量 `+0x58` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00694b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694b14.md) [`00696e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696e24.md) [`00698dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698dd4.md) [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 32件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 4件 [`00694b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694b6c.md) [`00696e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e7c.md) [`00698e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698e2c.md) [`00a75e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a75/00a75e1c.md) · 呼出先 32件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 60.95% / 新版 60.95%

CFGの説明率　旧版 32.17% / 新版 32.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 20件, `unresolved_call_alignment` 15件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 34件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068ed80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068ed80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068ed84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0068ed80",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0068ed84",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0068ed88",
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
      "0068edd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0068eddc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0068ede0",
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

- 旧版 [`0068ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068ed80.md#insn-0068ed80) · [`0068ed84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068ed80.md#insn-0068ed84) · [`0068ed88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068ed80.md#insn-0068ed88)

~~~diff
- 0068ed80 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0068ed80 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0068ed80 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 0068ed80 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0068ed80 bytes fd7bbba9
- 0068ed84 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0068ed84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 0068ed84 bytes fc0b00f9
- 0068ed88 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0068ed88 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0068ed88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0068ed88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0068ed88 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-418c0d12df5186f9e8332233300d43aa"></a>

### [`0068f5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068f/0068f5d8.md) → [`0068f630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md) FUN_0068f630

採用 · 移動量 `+0x58` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00696444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696444.md) [`00698788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698788.md) · 呼出先 43件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 2件 [`0069649c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/0069649c.md) [`006987e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006987e0.md) · 呼出先 43件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 57.02% / 新版 57.02%

CFGの説明率　旧版 44.86% / 新版 44.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 8件, `unresolved_branch_alignment` 37件, `unresolved_call_alignment` 63件, `unresolved_store_alignment` 45件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0068f6b8",
      "incomplete_value": false,
      "site": "0068f6b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0068f660",
      "incomplete_value": false,
      "site": "0068f660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068f734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068f738"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0068f6b8",
      "DATA",
      [
        "storage",
        "00c75280",
        null,
        "undefined *"
      ]
    ],
    [
      "0068f720",
      "READ",
      [
        "storage",
        "00c752a0",
        null,
        "pointer"
      ]
    ],
    [
      "0068f720",
      "READ",
      [
        "storage",
        "00c752a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0068f6b8",
      "DATA",
      [
        "storage",
        "00c75350",
        null,
        "undefined *"
      ]
    ],
    [
      "0068f720",
      "READ",
      [
        "storage",
        "00c75370",
        null,
        "pointer"
      ]
    ],
    [
      "0068f720",
      "READ",
      [
        "storage",
        "00c75378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068f6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068f/0068f5d8.md#insn-0068f6dc) · [`0068f6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068f/0068f5d8.md#insn-0068f6e0) · [`0068f710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068f/0068f5d8.md#insn-0068f710)
- 新版 [`0068f734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md#insn-0068f734) · [`0068f738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md#insn-0068f738) · [`0068f768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md#insn-0068f768)

~~~diff
- 0068f6dc ["INT_ADD", "register:40f0:8", ["const:68f6dc:8", "const:4:8"]]
- 0068f6dc ["CALL", null, ["callee:00c57f80:8"]]
+ 0068f734 ["INT_ADD", "register:40f0:8", ["const:68f734:8", "const:4:8"]]
+ 0068f734 ["CALL", null, ["callee:00c57f80:8"]]
- 0068f6dc bytes f5211794
+ 0068f734 bytes 13221794
- 0068f6e0 ["INT_ADD", "register:40f0:8", ["const:68f6e0:8", "const:4:8"]]
- 0068f6e0 ["CALL", null, ["callee:00851550:8"]]
+ 0068f738 ["INT_ADD", "register:40f0:8", ["const:68f738:8", "const:4:8"]]
+ 0068f738 ["CALL", null, ["callee:00851550:8"]]
- 0068f6e0 bytes 86070794
+ 0068f738 bytes 86070794
- 0068f710 ["INT_ADD", "register:40f0:8", ["const:68f710:8", "const:4:8"]]
- 0068f710 ["CALL", null, ["callee:00851550:8"]]
+ 0068f768 ["INT_ADD", "register:40f0:8", ["const:68f768:8", "const:4:8"]]
+ 0068f768 ["CALL", null, ["callee:00851550:8"]]
- 0068f710 bytes 7a070794
+ 0068f768 bytes 7a070794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d94da82f3e5e93d1efdc8240a025e86"></a>

### [`006906e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00690/006906e8.md) → [`00690740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690740.md) FUN_00690740

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00696e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696e24.md) · 呼出先 35件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 1件 [`00696e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e7c.md) · 呼出先 35件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 92.53% / 新版 92.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_value` 4件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006907c4",
      "incomplete_value": true,
      "site": "006907dc",
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
                "const:674:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0069076c",
      "incomplete_value": true,
      "site": "00690784",
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
                "const:6c8:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00690820"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00690820"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006907c4",
      "READ",
      [
        "storage",
        "002bb6c8",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00690820",
      "DATA",
      [
        "storage",
        "00c75500",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00690820",
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
      "006907c4",
      "READ",
      [
        "storage",
        "002bb674",
        null,
        "string"
      ]
    ],
    [
      "00690878",
      "DATA",
      [
        "storage",
        "00c755d0",
        null,
        "undefined *"
      ]
    ],
    [
      "00690878",
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

- 旧版 [`00690800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00690/006906e8.md#insn-00690800) · [`00690810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00690/006906e8.md#insn-00690810) · [`00690820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00690/006906e8.md#insn-00690820)
- 新版 [`00690858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690740.md#insn-00690858) · [`00690868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690740.md#insn-00690868)

~~~diff
- 00690800 ["INT_ADD", "register:40f0:8", ["const:690800:8", "const:4:8"]]
- 00690800 ["CALL", null, ["callee:0052dd40:8"]]
+ 00690858 ["INT_ADD", "register:40f0:8", ["const:690858:8", "const:4:8"]]
+ 00690858 ["CALL", null, ["callee:0052dd40:8"]]
- 00690800 bytes 4075fa97
+ 00690858 bytes 3a75fa97
- 00690810 ["INT_ADD", "register:40f0:8", ["const:690810:8", "const:4:8"]]
- 00690810 ["CALL", null, ["callee:005cd130:8"]]
+ 00690868 ["INT_ADD", "register:40f0:8", ["const:690868:8", "const:4:8"]]
+ 00690868 ["CALL", null, ["callee:005cd130:8"]]
- 00690810 bytes 38f2fc97
+ 00690868 bytes 32f2fc97
- 00690820 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00690820 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00690820 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffff80:8"]]
- 00690820 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00690820 bytes a84f38a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1327f782b332523d8a572faf0388ea3"></a>

### [`00690ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00690/00690ea0.md) → [`00690ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690ef8.md) FUN_00690ef8

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00696444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696444.md) · 呼出先 37件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md) [`005cd0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd0f0.md)
- 新版 呼出元 1件 [`0069649c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/0069649c.md) · 呼出先 37件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md) [`005cd130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 63.56% / 新版 63.56%

CFGの説明率　旧版 29.60% / 新版 29.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 1件, `store_value` 2件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 31件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 37件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00690ea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00690ea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00690ea4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00690ea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00690ea4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00690ea8",
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
      "00690ef8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00690efc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00690f00",
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

- 旧版 [`00690ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00690/00690ea0.md#insn-00690ea0) · [`00690ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00690/00690ea0.md#insn-00690ea4) · [`00690ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00690/00690ea0.md#insn-00690ea8)

~~~diff
- 00690ea0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00690ea0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00690ea0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00690ea0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00690ea0 bytes fd7bbaa9
- 00690ea4 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00690ea4 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00690ea4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00690ea4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00690ea4 bytes fc6f01a9
- 00690ea8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00690ea8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00690ea8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00690ea8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00690ea8 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-096ceaedd174e0905449af98bea68781"></a>

### [`00691c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691c18.md) → [`00691c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691c70.md) FUN_00691c70

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00691acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691acc.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00691b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691b24.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00691c7c",
      "incomplete_value": false,
      "site": "00691c80",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691c24",
      "incomplete_value": false,
      "site": "00691c28",
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
      "00691c7c",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00691c7c",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691c18.md#insn-00691c28) · [`00691c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691c18.md#insn-00691c24)
- 新版 [`00691c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691c70.md#insn-00691c80) · [`00691c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691c70.md#insn-00691c7c)

~~~diff
- 00691c28 ["INT_ADD", "register:40f0:8", ["const:691c28:8", "const:4:8"]]
- 00691c28 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00691c80 ["INT_ADD", "register:40f0:8", ["const:691c80:8", "const:4:8"]]
+ 00691c80 ["CALL", null, ["callee:0043b7b8:8"]]
- 00691c28 bytes d4a6f697
+ 00691c80 bytes cea6f697
- 00691c24 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00691c24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00691c24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00691c24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00691c7c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00691c7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00691c7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00691c7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00691c24 bytes 00303d91
+ 00691c7c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cc4c64f963401ed94d3b33346ae8f2d"></a>

### [`00691e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e18.md) → [`00691e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e70.md) FUN_00691e70

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00685ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685ae4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00685b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/00685b24.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00691e7c",
      "incomplete_value": false,
      "site": "00691e80",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691e24",
      "incomplete_value": false,
      "site": "00691e28",
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
      "00691e7c",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00691e7c",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e18.md#insn-00691e28) · [`00691e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e18.md#insn-00691e24)
- 新版 [`00691e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e70.md#insn-00691e80) · [`00691e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e70.md#insn-00691e7c)

~~~diff
- 00691e28 ["INT_ADD", "register:40f0:8", ["const:691e28:8", "const:4:8"]]
- 00691e28 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00691e80 ["INT_ADD", "register:40f0:8", ["const:691e80:8", "const:4:8"]]
+ 00691e80 ["CALL", null, ["callee:0043b7b8:8"]]
- 00691e28 bytes 54a6f697
+ 00691e80 bytes 4ea6f697
- 00691e24 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00691e24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00691e24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00691e24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00691e7c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00691e7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00691e7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00691e7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00691e24 bytes 00303d91
+ 00691e7c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d41892ed283e181b201f7029ce0a434e"></a>

### [`00691e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e2c.md) → [`00691e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md) FUN_00691e84

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 17件 [`00684f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684f0c.md) [`00685ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685ae4.md) [`00687628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/00687628.md) [`00687650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/00687650.md) [`00687b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/00687b4c.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 17件 [`00684f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684f4c.md) [`00685b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/00685b24.md) [`00687668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687668.md) [`00687690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687690.md) [`00687b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687b8c.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

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
      "definition_site": "00691e90",
      "incomplete_value": false,
      "site": "00691e94",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691e38",
      "incomplete_value": false,
      "site": "00691e3c",
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
      "00691e90",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00691e90",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e2c.md#insn-00691e3c) · [`00691e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e2c.md#insn-00691e38)
- 新版 [`00691e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md#insn-00691e94) · [`00691e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md#insn-00691e90)

~~~diff
- 00691e3c ["INT_ADD", "register:40f0:8", ["const:691e3c:8", "const:4:8"]]
- 00691e3c ["CALL", null, ["callee:00442970:8"]]
+ 00691e94 ["INT_ADD", "register:40f0:8", ["const:691e94:8", "const:4:8"]]
+ 00691e94 ["CALL", null, ["callee:00442970:8"]]
- 00691e3c bytes bdc2f697
+ 00691e94 bytes b7c2f697
- 00691e38 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00691e38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00691e38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00691e38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00691e90 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00691e90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00691e90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00691e90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00691e38 bytes 00303d91
+ 00691e90 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cad03e7fb1d5240a28e45b6096c5bffc"></a>

### [`00691e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e40.md) → [`00691e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e98.md) FUN_00691e98

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00685ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685ff0.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00686030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00686/00686030.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00691ea4",
      "incomplete_value": false,
      "site": "00691ea8",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691e4c",
      "incomplete_value": false,
      "site": "00691e50",
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
      "00691ea4",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00691ea4",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e40.md#insn-00691e50) · [`00691e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e40.md#insn-00691e4c)
- 新版 [`00691ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e98.md#insn-00691ea8) · [`00691ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e98.md#insn-00691ea4)

~~~diff
- 00691e50 ["INT_ADD", "register:40f0:8", ["const:691e50:8", "const:4:8"]]
- 00691e50 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00691ea8 ["INT_ADD", "register:40f0:8", ["const:691ea8:8", "const:4:8"]]
+ 00691ea8 ["CALL", null, ["callee:0043b7b8:8"]]
- 00691e50 bytes 4aa6f697
+ 00691ea8 bytes 44a6f697
- 00691e4c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00691e4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00691e4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00691e4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00691ea4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00691ea4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00691ea4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00691ea4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00691e4c bytes 00303d91
+ 00691ea4 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-227a6fd62bae5b261accb6f7f416d601"></a>

### [`00691e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e54.md) → [`00691eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691eac.md) FUN_00691eac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`00684e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684e3c.md) [`00684e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684e84.md) [`00684ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684ed8.md) [`00684fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684fb0.md) [`00685ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685ff0.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 7件 [`00684e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684e7c.md) [`00684ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684ec4.md) [`00684f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684f18.md) [`00684ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684ff0.md) [`00686030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00686/00686030.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

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
      "definition_site": "00691eb8",
      "incomplete_value": false,
      "site": "00691ebc",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691e60",
      "incomplete_value": false,
      "site": "00691e64",
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
      "00691eb8",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00691eb8",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e54.md#insn-00691e64) · [`00691e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e54.md#insn-00691e60)
- 新版 [`00691ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691eac.md#insn-00691ebc) · [`00691eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691eac.md#insn-00691eb8)

~~~diff
- 00691e64 ["INT_ADD", "register:40f0:8", ["const:691e64:8", "const:4:8"]]
- 00691e64 ["CALL", null, ["callee:00442970:8"]]
+ 00691ebc ["INT_ADD", "register:40f0:8", ["const:691ebc:8", "const:4:8"]]
+ 00691ebc ["CALL", null, ["callee:00442970:8"]]
- 00691e64 bytes b3c2f697
+ 00691ebc bytes adc2f697
- 00691e60 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00691e60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00691e60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00691e60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00691eb8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00691eb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00691eb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00691eb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00691e60 bytes 00303d91
+ 00691eb8 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6369aeb642f37f027622b2349262a2ec"></a>

### [`00692008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692008.md) → [`00692060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692060.md) FUN_00692060

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00691e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e68.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00691ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691ec0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "0069206c",
      "incomplete_value": false,
      "site": "00692070",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00692014",
      "incomplete_value": false,
      "site": "00692018",
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
      "0069206c",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0069206c",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00692018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692008.md#insn-00692018) · [`00692014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692008.md#insn-00692014)
- 新版 [`00692070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692060.md#insn-00692070) · [`0069206c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692060.md#insn-0069206c)

~~~diff
- 00692018 ["INT_ADD", "register:40f0:8", ["const:692018:8", "const:4:8"]]
- 00692018 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00692070 ["INT_ADD", "register:40f0:8", ["const:692070:8", "const:4:8"]]
+ 00692070 ["CALL", null, ["callee:0043b7b8:8"]]
- 00692018 bytes d8a5f697
+ 00692070 bytes d2a5f697
- 00692014 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00692014 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00692014 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00692014 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0069206c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0069206c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0069206c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0069206c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00692014 bytes 00303d91
+ 0069206c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28081b873cfd3645cbd01f75dc6898ea"></a>

### [`0069201c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/0069201c.md) → [`00692074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692074.md) FUN_00692074

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00686a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00686/00686a78.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00692244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692244.md) [`0069241c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/0069241c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00686ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00686/00686ab8.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0069229c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069229c.md) [`00692474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692474.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 72.97% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692140"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692140"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00692198"
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
      "006920d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006921f0"
      ]
    ],
    [
      "unmatched:00692140",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:006921f4",
      "READ",
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
      "006920d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692248"
      ]
    ],
    [
      "00692198",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0069224c",
      "READ",
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

- 旧版 [`00692140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/0069201c.md#insn-00692140) · [`0069214c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/0069201c.md#insn-0069214c)
- 新版 [`006921a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692074.md#insn-006921a4) · [`00692198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692074.md#insn-00692198)

~~~diff
- 00692140 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00692140 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00692140 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00692140 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00692140 bytes e92301a9
- 0069214c ["INT_ADD", "register:40f0:8", ["const:69214c:8", "const:4:8"]]
- 0069214c ["CALL", null, ["callee:0069229c:8"]]
+ 006921a4 ["INT_ADD", "register:40f0:8", ["const:6921a4:8", "const:4:8"]]
+ 006921a4 ["CALL", null, ["callee:0069229c:8"]]
- 0069214c bytes 3e000094
+ 006921a4 bytes 3e000094
+ 00692198 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00692198 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00692198 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 00692198 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00692198 bytes e92301a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bab03c0eef1b572ef72e9caf74c7715"></a>

### [`0069237c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/0069237c.md) → [`006923d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/006923d4.md) FUN_006923d4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 31.82% / 新版 35.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006923d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0069243c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "006923c8",
      "incomplete_value": true,
      "site": "006923cc",
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:fffffffffffffff8:8"
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
      "unmatched:006923d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692414"
      ]
    ],
    [
      "0069242c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006923f0"
      ]
    ]
  ],
  "added": [
    [
      "0069242c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692414"
      ]
    ],
    [
      "0069243c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006923f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006923cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/0069237c.md#insn-006923cc) · [`006923d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/0069237c.md#insn-006923d4) · [`006923ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/0069237c.md#insn-006923ec)
- 新版 [`00692424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/006923d4.md#insn-00692424) · [`00692444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/006923d4.md#insn-00692444)

~~~diff
- 006923cc ["INT_ADD", "register:40f0:8", ["const:6923cc:8", "const:4:8"]]
- 006923cc ["CALL", null, ["callee:00c57f80:8"]]
+ 00692424 ["INT_ADD", "register:40f0:8", ["const:692424:8", "const:4:8"]]
+ 00692424 ["CALL", null, ["callee:00c57f80:8"]]
- 006923cc bytes b9161794
+ 00692424 bytes d7161794
- 006923d4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 006923d4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 006923d4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 006923d4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 006923d4 bytes 48ff0736
- 006923ec ["INT_ADD", "register:40f0:8", ["const:6923ec:8", "const:4:8"]]
- 006923ec ["CALL", null, ["callee:00c57f80:8"]]
+ 00692444 ["INT_ADD", "register:40f0:8", ["const:692444:8", "const:4:8"]]
+ 00692444 ["CALL", null, ["callee:00c57f80:8"]]
- 006923ec bytes b1161794
+ 00692444 bytes cf161794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bdb8d472bae8905a2d3c614b06d7739"></a>

### [`0069241c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/0069241c.md) → [`00692474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692474.md) FUN_00692474

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0069201c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/0069201c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00692074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692074.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00692480",
      "incomplete_value": false,
      "site": "00692484",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00692428",
      "incomplete_value": false,
      "site": "0069242c",
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
      "00692480",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00692480",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069242c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/0069241c.md#insn-0069242c) · [`00692428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/0069241c.md#insn-00692428)
- 新版 [`00692484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692474.md#insn-00692484) · [`00692480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692474.md#insn-00692480)

~~~diff
- 0069242c ["INT_ADD", "register:40f0:8", ["const:69242c:8", "const:4:8"]]
- 0069242c ["CALL", null, ["callee:0043b7b8:8"]]
+ 00692484 ["INT_ADD", "register:40f0:8", ["const:692484:8", "const:4:8"]]
+ 00692484 ["CALL", null, ["callee:0043b7b8:8"]]
- 0069242c bytes d3a4f697
+ 00692484 bytes cda4f697
- 00692428 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00692428 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00692428 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00692428 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00692480 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00692480 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00692480 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00692480 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00692428 bytes 00303d91
+ 00692480 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-970be1d4e3696bd7f361fa62d6956392"></a>

### [`006924c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924c4.md) → [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) FUN_0069251c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 11件 [`00687904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/00687904.md) [`0068e754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068e754.md) [`0068f5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068f/0068f5d8.md) [`00694d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694d28.md) [`00694de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694de0.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 11件 [`00687944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687944.md) [`0068e7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068e7ac.md) [`0068f630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md) [`00694d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d80.md) [`00694e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694e38.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00692528",
      "incomplete_value": false,
      "site": "0069252c",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006924d0",
      "incomplete_value": false,
      "site": "006924d4",
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
      "00692528",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00692528",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006924d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924c4.md#insn-006924d4) · [`006924d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924c4.md#insn-006924d0)
- 新版 [`0069252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md#insn-0069252c) · [`00692528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md#insn-00692528)

~~~diff
- 006924d4 ["INT_ADD", "register:40f0:8", ["const:6924d4:8", "const:4:8"]]
- 006924d4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0069252c ["INT_ADD", "register:40f0:8", ["const:69252c:8", "const:4:8"]]
+ 0069252c ["CALL", null, ["callee:0043b7b8:8"]]
- 006924d4 bytes a9a4f697
+ 0069252c bytes a3a4f697
- 006924d0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 006924d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006924d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006924d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00692528 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00692528 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00692528 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00692528 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006924d0 bytes 00303d91
+ 00692528 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d90a6929309bd7d0cd25f860d1c52b2f"></a>

### [`006924d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924d8.md) → [`00692530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692530.md) FUN_00692530

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00684fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684fb0.md) [`00685248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685248.md) [`00685374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685374.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 3件 [`00684ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684ff0.md) [`00685288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/00685288.md) [`006853b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/006853b4.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

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
      "definition_site": "0069253c",
      "incomplete_value": false,
      "site": "00692540",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006924e4",
      "incomplete_value": false,
      "site": "006924e8",
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
      "0069253c",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0069253c",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006924e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924d8.md#insn-006924e8) · [`006924e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924d8.md#insn-006924e4)
- 新版 [`00692540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692530.md#insn-00692540) · [`0069253c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692530.md#insn-0069253c)

~~~diff
- 006924e8 ["INT_ADD", "register:40f0:8", ["const:6924e8:8", "const:4:8"]]
- 006924e8 ["CALL", null, ["callee:00442970:8"]]
+ 00692540 ["INT_ADD", "register:40f0:8", ["const:692540:8", "const:4:8"]]
+ 00692540 ["CALL", null, ["callee:00442970:8"]]
- 006924e8 bytes 12c1f697
+ 00692540 bytes 0cc1f697
- 006924e4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 006924e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006924e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006924e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0069253c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0069253c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0069253c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0069253c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006924e4 bytes 00303d91
+ 0069253c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3875536654b075c56d8e4b03792aab66"></a>

### [`006924ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924ec.md) → [`00692544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692544.md) FUN_00692544

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00684fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684fb0.md) [`006852e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/006852e0.md) [`00685374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685374.md) [`0068a6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a6c4.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 4件 [`00684ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684ff0.md) [`00685320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/00685320.md) [`006853b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/006853b4.md) [`0068a71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a71c.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

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
      "definition_site": "00692550",
      "incomplete_value": false,
      "site": "00692554",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006924f8",
      "incomplete_value": false,
      "site": "006924fc",
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
      "00692550",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00692550",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006924fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924ec.md#insn-006924fc) · [`006924f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924ec.md#insn-006924f8)
- 新版 [`00692554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692544.md#insn-00692554) · [`00692550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692544.md#insn-00692550)

~~~diff
- 006924fc ["INT_ADD", "register:40f0:8", ["const:6924fc:8", "const:4:8"]]
- 006924fc ["CALL", null, ["callee:00442970:8"]]
+ 00692554 ["INT_ADD", "register:40f0:8", ["const:692554:8", "const:4:8"]]
+ 00692554 ["CALL", null, ["callee:00442970:8"]]
- 006924fc bytes 0dc1f697
+ 00692554 bytes 07c1f697
- 006924f8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 006924f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006924f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006924f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00692550 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00692550 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00692550 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00692550 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006924f8 bytes 00303d91
+ 00692550 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5306cf5915eaa675c6e61cdb2b13cab"></a>

### [`00692500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692500.md) → [`00692558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692558.md) FUN_00692558

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0068a2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a2b8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`0068a310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a310.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00692564",
      "incomplete_value": false,
      "site": "00692568",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0069250c",
      "incomplete_value": false,
      "site": "00692510",
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
      "00692564",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00692564",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00692510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692500.md#insn-00692510) · [`0069250c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692500.md#insn-0069250c)
- 新版 [`00692568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692558.md#insn-00692568) · [`00692564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692558.md#insn-00692564)

~~~diff
- 00692510 ["INT_ADD", "register:40f0:8", ["const:692510:8", "const:4:8"]]
- 00692510 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00692568 ["INT_ADD", "register:40f0:8", ["const:692568:8", "const:4:8"]]
+ 00692568 ["CALL", null, ["callee:0043b7b8:8"]]
- 00692510 bytes 9aa4f697
+ 00692568 bytes 94a4f697
- 0069250c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0069250c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0069250c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0069250c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00692564 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00692564 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00692564 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00692564 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0069250c bytes 00303d91
+ 00692564 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2aea05570fd3373badec845cf54f908"></a>

### [`00692514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692514.md) → [`0069256c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069256c.md) FUN_0069256c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0068a2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a2b8.md) [`00692514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692514.md) [`006928b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006928b4.md) · 呼出先 4件 [`00692514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692514.md) [`006928b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006928b4.md) [`00692bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692bd8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`0068a310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a310.md) [`0069256c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069256c.md) [`0069290c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069290c.md) · 呼出先 4件 [`0069256c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069256c.md) [`0069290c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069290c.md) [`00692c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692c30.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.67% / 新版 92.67%

CFGの説明率　旧版 65.57% / 新版 64.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069261c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692620"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692684"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00692634",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006925a0"
      ]
    ],
    [
      "unmatched:00692684",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:00692688",
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
      "0069268c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006925a0"
      ]
    ],
    [
      "006926dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "006926e0",
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

- 旧版 [`0069261c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692514.md#insn-0069261c) · [`00692620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692514.md#insn-00692620) · [`00692634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692514.md#insn-00692634)

~~~diff
- 0069261c ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:c:8"]]
- 0069261c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0069261c bytes 60c1803c
- 00692620 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00692620 ["INT_ADD", "tmp:1:8", ["register:4058:8", "const:1c:8"]]
- 00692620 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00692620 bytes 6ac101f8
- 00692634 ["CBRANCH", null, ["local:b1:8", "register:101:1"]]
- 00692634 bytes a0f8ff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72cbdd2afddf4fe7dc12261babeacfc4"></a>

### [`00692bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692bd8.md) → [`00692c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692c30.md) FUN_00692c30

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00692514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692514.md) [`00692bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692bd8.md) · 呼出先 4件 [`00692bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692bd8.md) [`006930f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/006930f4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 2件 [`0069256c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069256c.md) [`00692c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692c30.md) · 呼出先 4件 [`00692c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692c30.md) [`0069314c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/0069314c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.85% / 新版 86.85%

CFGの説明率　旧版 67.50% / 新版 68.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 8件, `unresolved_store_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692bdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692bdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692be0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00692bdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00692be0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00692be4",
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
      "00692c34",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00692c38",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00692c3c",
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

- 旧版 [`00692bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692bd8.md#insn-00692bdc) · [`00692be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692bd8.md#insn-00692be0) · [`00692be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692bd8.md#insn-00692be4)

~~~diff
- 00692bdc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00692bdc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00692bdc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00692bdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00692bdc bytes fd7b07a9
- 00692be0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00692be0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00692be0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00692be0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00692be0 bytes fc6f08a9
- 00692be4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00692be4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00692be4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00692be4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00692be4 bytes fa6709a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a38c8ee25245ac9023f25cfd134bce8"></a>

### [`006930f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/006930f4.md) → [`0069314c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/0069314c.md) FUN_0069314c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00692bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692bd8.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00692c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692c30.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 27.50% / 新版 26.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 6件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069322c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069322c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00693230"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00693174",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00693304"
      ]
    ],
    [
      "unmatched:00693130",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00693228"
      ]
    ],
    [
      "unmatched:0069316c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006932c4"
      ]
    ]
  ],
  "added": [
    [
      "00693174",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069335c"
      ]
    ],
    [
      "00693188",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00693228"
      ]
    ],
    [
      "006931c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006932c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00693130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/006930f4.md#insn-00693130) · [`0069316c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/006930f4.md#insn-0069316c) · [`006931ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/006930f4.md#insn-006931ac)
- 新版 [`00693204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/0069314c.md#insn-00693204)

~~~diff
- 00693130 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 00693130 bytes 00050054
- 0069316c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0069316c ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 0069316c bytes 01080054
- 006931ac ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 00693204 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 006931ac bytes a0000054
+ 00693204 bytes a0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cda7c057d74777620cd275ecd390bca"></a>

### [`00693388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693388.md) → [`006933e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006933e0.md) FUN_006933e0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0068bad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bad0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068bb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068bb28.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

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
      "site": "00693400",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006933a8",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "0069340c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006933b4",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00693400",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0069340c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00693400",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "0069340c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006933a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693388.md#insn-006933a8) · [`006933b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693388.md#insn-006933b4)
- 新版 [`00693400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006933e0.md#insn-00693400) · [`0069340c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006933e0.md#insn-0069340c)

~~~diff
- 006933a8 ["INT_ADD", "register:40f0:8", ["const:6933a8:8", "const:4:8"]]
- 006933a8 ["CALL", null, ["ram:47acf4:8"]]
+ 00693400 ["INT_ADD", "register:40f0:8", ["const:693400:8", "const:4:8"]]
+ 00693400 ["CALL", null, ["ram:47ad34:8"]]
- 006933a8 bytes 539ef797
+ 00693400 bytes 4d9ef797
- 006933b4 ["INT_ADD", "register:40f0:8", ["const:6933b4:8", "const:4:8"]]
- 006933b4 ["CALL", null, ["ram:47acf4:8"]]
+ 0069340c ["INT_ADD", "register:40f0:8", ["const:69340c:8", "const:4:8"]]
+ 0069340c ["CALL", null, ["ram:47ad34:8"]]
- 006933b4 bytes 509ef797
+ 0069340c bytes 4a9ef797
~~~


<a id="compare-148e714e9a5c0ac9c2aeac3a0225cbf9"></a>

### [`00693458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693458.md) → [`006934b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006934b0.md) FUN_006934b0

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 15件 [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0068bad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bad0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`004709d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004709d4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0068bb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068bb28.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.40% / 新版 77.40%

CFGの説明率　旧版 55.56% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006935c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006935c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006935cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006934e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006934ac"
      ]
    ],
    [
      "unmatched:00693490",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "unmatched:00693498",
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
      "006934e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00693504"
      ]
    ],
    [
      "006934e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006934f0",
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

- 旧版 [`00693490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693458.md#insn-00693490) · [`006934a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693458.md#insn-006934a0) · [`006934ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693458.md#insn-006934ac)

~~~diff
- 00693490 ["INT_ADD", "register:40f0:8", ["const:693490:8", "const:4:8"]]
- 00693490 ["CALL", null, ["ram:47acf4:8"]]
- 00693490 bytes 199ef797
- 006934a0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006934a0 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 006934a0 bytes e1120054
- 006934ac ["INT_ADD", "register:40f0:8", ["const:6934ac:8", "const:4:8"]]
- 006934ac ["CALL", null, ["ram:47acf4:8"]]
- 006934ac bytes 129ef797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1986a81bc6811cdea2a8ef587bf57a9"></a>

### [`0069375c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/0069375c.md) → [`006937b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006937b4.md) FUN_006937b4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "006937d8",
      "incomplete_value": false,
      "site": "006937d8",
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
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00693780",
      "incomplete_value": false,
      "site": "00693780",
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
            "const:940:8"
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
      "006937d8",
      "DATA",
      [
        "storage",
        "00c74940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006937d8",
      "DATA",
      [
        "storage",
        "00c74a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00693770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/0069375c.md#insn-00693770) · [`0069377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/0069375c.md#insn-0069377c)
- 新版 [`006937c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006937b4.md#insn-006937c8) · [`006937d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006937b4.md#insn-006937d4)

~~~diff
- 00693770 ["INT_ADD", "register:40f0:8", ["const:693770:8", "const:4:8"]]
- 00693770 ["CALL", null, ["callee:00c57f60:8"]]
+ 006937c8 ["INT_ADD", "register:40f0:8", ["const:6937c8:8", "const:4:8"]]
+ 006937c8 ["CALL", null, ["callee:00c57f60:8"]]
- 00693770 bytes c8111794
+ 006937c8 bytes e6111794
- 0069377c ["COPY", "tmp:0:8", ["const:940:8"]]
- 0069377c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0069377c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0069377c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006937d4 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 006937d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006937d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006937d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0069377c bytes 08012591
+ 006937d4 bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f4498bd04fff7faea5131ee77c42baf"></a>

### [`006937ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/006937ac.md) → [`00693804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693804.md) FUN_00693804

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "00693820",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006937c8",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00693820",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00693820",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006937c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/006937ac.md#insn-006937c8) · [`006937d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/006937ac.md#insn-006937d4)
- 新版 [`00693820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693804.md#insn-00693820) · [`0069382c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693804.md#insn-0069382c)

~~~diff
- 006937c8 ["INT_ADD", "register:40f0:8", ["const:6937c8:8", "const:4:8"]]
- 006937c8 ["CALL", null, ["ram:47acf4:8"]]
+ 00693820 ["INT_ADD", "register:40f0:8", ["const:693820:8", "const:4:8"]]
+ 00693820 ["CALL", null, ["ram:47ad34:8"]]
- 006937c8 bytes 4b9df797
+ 00693820 bytes 459df797
- 006937d4 ["INT_ADD", "register:40f0:8", ["const:6937d4:8", "const:4:8"]]
- 006937d4 ["CALL", null, ["callee:0047ce14:8"]]
+ 0069382c ["INT_ADD", "register:40f0:8", ["const:69382c:8", "const:4:8"]]
+ 0069382c ["CALL", null, ["callee:0047ce14:8"]]
- 006937d4 bytes 80a5f797
+ 0069382c bytes 7aa5f797
~~~


<a id="compare-7d646b78259581a53b7d6829118db621"></a>

### [`00693818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693818.md) → [`00693870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693870.md) FUN_00693870

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00693894",
      "incomplete_value": false,
      "site": "00693894",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0069383c",
      "incomplete_value": false,
      "site": "0069383c",
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
            "const:9d0:8"
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
      "00693894",
      "DATA",
      [
        "storage",
        "00c749d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00693894",
      "DATA",
      [
        "storage",
        "00c74aa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069382c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693818.md#insn-0069382c) · [`00693838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693818.md#insn-00693838)
- 新版 [`00693884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693870.md#insn-00693884) · [`00693890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693870.md#insn-00693890)

~~~diff
- 0069382c ["INT_ADD", "register:40f0:8", ["const:69382c:8", "const:4:8"]]
- 0069382c ["CALL", null, ["callee:00c57f60:8"]]
+ 00693884 ["INT_ADD", "register:40f0:8", ["const:693884:8", "const:4:8"]]
+ 00693884 ["CALL", null, ["callee:00c57f60:8"]]
- 0069382c bytes 99111794
+ 00693884 bytes b7111794
- 00693838 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00693838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00693838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00693838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00693890 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 00693890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00693890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00693890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00693838 bytes 08412791
+ 00693890 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89dfb8a8dc6412cb20389dcfb129ed42"></a>

### [`00693868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693868.md) → [`006938c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006938c0.md) FUN_006938c0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0068a9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a9ac.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068aa04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068aa04.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

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
      "site": "006938e8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00693890",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "006938f8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006938a0",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "006938e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006938f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "006938e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006938f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00693890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693868.md#insn-00693890) · [`006938a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693868.md#insn-006938a0) · [`006938c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693868.md#insn-006938c0)
- 新版 [`006938e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006938c0.md#insn-006938e8) · [`006938f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006938c0.md#insn-006938f8) · [`00693918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006938c0.md#insn-00693918)

~~~diff
- 00693890 ["INT_ADD", "register:40f0:8", ["const:693890:8", "const:4:8"]]
- 00693890 ["CALL", null, ["ram:47acf4:8"]]
+ 006938e8 ["INT_ADD", "register:40f0:8", ["const:6938e8:8", "const:4:8"]]
+ 006938e8 ["CALL", null, ["ram:47ad34:8"]]
- 00693890 bytes 199df797
+ 006938e8 bytes 139df797
- 006938a0 ["INT_ADD", "register:40f0:8", ["const:6938a0:8", "const:4:8"]]
- 006938a0 ["CALL", null, ["ram:47acf4:8"]]
+ 006938f8 ["INT_ADD", "register:40f0:8", ["const:6938f8:8", "const:4:8"]]
+ 006938f8 ["CALL", null, ["ram:47ad34:8"]]
- 006938a0 bytes 159df797
+ 006938f8 bytes 0f9df797
- 006938c0 ["INT_ADD", "register:40f0:8", ["const:6938c0:8", "const:4:8"]]
- 006938c0 ["CALL", null, ["callee:0068aa04:8"]]
+ 00693918 ["INT_ADD", "register:40f0:8", ["const:693918:8", "const:4:8"]]
+ 00693918 ["CALL", null, ["callee:0068aa04:8"]]
- 006938c0 bytes 3bdcff97
+ 00693918 bytes 3bdcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0138b480d69dfead2f7a23daa21a140"></a>

### [`0069394c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/0069394c.md) → [`006939a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006939a4.md) FUN_006939a4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "006939c8",
      "incomplete_value": false,
      "site": "006939d0",
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
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00693970",
      "incomplete_value": false,
      "site": "00693978",
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
            "const:a50:8"
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
      "006939d0",
      "DATA",
      [
        "storage",
        "00c74a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006939d0",
      "DATA",
      [
        "storage",
        "00c74b20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00693960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/0069394c.md#insn-00693960) · [`00693970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/0069394c.md#insn-00693970)
- 新版 [`006939b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006939a4.md#insn-006939b8) · [`006939c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006939a4.md#insn-006939c8)

~~~diff
- 00693960 ["INT_ADD", "register:40f0:8", ["const:693960:8", "const:4:8"]]
- 00693960 ["CALL", null, ["callee:00c57f60:8"]]
+ 006939b8 ["INT_ADD", "register:40f0:8", ["const:6939b8:8", "const:4:8"]]
+ 006939b8 ["CALL", null, ["callee:00c57f60:8"]]
- 00693960 bytes 4c111794
+ 006939b8 bytes 6a111794
- 00693970 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 00693970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00693970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00693970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006939c8 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 006939c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006939c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006939c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00693970 bytes 08412991
+ 006939c8 bytes 08812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0370a5b9e3c91c052bb016dafeda209"></a>

### [`006939c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/006939c4.md) → [`00693a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693a1c.md) FUN_00693a1c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.73% / 新版 98.73%

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
      "site": "00693ac8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00693a70",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "00693af0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00693a98",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00693ac8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00693af0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00693ac8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00693af0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00693a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/006939c4.md#insn-00693a70) · [`00693a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/006939c4.md#insn-00693a98) · [`00693a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/006939c4.md#insn-00693a38)
- 新版 [`00693ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693a1c.md#insn-00693ac8) · [`00693af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693a1c.md#insn-00693af0) · [`00693a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693a1c.md#insn-00693a90)

~~~diff
- 00693a70 ["INT_ADD", "register:40f0:8", ["const:693a70:8", "const:4:8"]]
- 00693a70 ["CALL", null, ["ram:47acf4:8"]]
+ 00693ac8 ["INT_ADD", "register:40f0:8", ["const:693ac8:8", "const:4:8"]]
+ 00693ac8 ["CALL", null, ["ram:47ad34:8"]]
- 00693a70 bytes a19cf797
+ 00693ac8 bytes 9b9cf797
- 00693a98 ["INT_ADD", "register:40f0:8", ["const:693a98:8", "const:4:8"]]
- 00693a98 ["CALL", null, ["ram:47acf4:8"]]
+ 00693af0 ["INT_ADD", "register:40f0:8", ["const:693af0:8", "const:4:8"]]
+ 00693af0 ["CALL", null, ["ram:47ad34:8"]]
- 00693a98 bytes 979cf797
+ 00693af0 bytes 919cf797
- 00693a38 ["INT_ADD", "register:40f0:8", ["const:693a38:8", "const:4:8"]]
- 00693a38 ["CALL", null, ["callee:00c58520:8"]]
+ 00693a90 ["INT_ADD", "register:40f0:8", ["const:693a90:8", "const:4:8"]]
+ 00693a90 ["CALL", null, ["callee:00c58520:8"]]
- 00693a38 bytes 86121794
+ 00693a90 bytes a4121794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7fc0755045dd7fd2e6c52d0825079be"></a>

### [`00693cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693cb8.md) → [`00693d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693d10.md) FUN_00693d10

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0068bad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bad0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068bb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068bb28.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 33.33% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00693cd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00693d28"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00693d30",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00693cd8",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "unmatched:00693cd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00693ce4"
      ]
    ],
    [
      "00693d30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "unmatched:00693ce4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00693d28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00693d3c"
      ]
    ],
    [
      "00693d30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00693d3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00693cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693cb8.md#insn-00693cd0) · [`00693cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693cb8.md#insn-00693cd8) · [`00693ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693cb8.md#insn-00693ce4)
- 新版 [`00693d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693d10.md#insn-00693d30)

~~~diff
- 00693cd0 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00693cd0 bytes a0000054
- 00693cd8 ["INT_ADD", "register:40f0:8", ["const:693cd8:8", "const:4:8"]]
- 00693cd8 ["CALL", null, ["ram:47acf4:8"]]
+ 00693d30 ["INT_ADD", "register:40f0:8", ["const:693d30:8", "const:4:8"]]
+ 00693d30 ["CALL", null, ["ram:47ad34:8"]]
- 00693cd8 bytes 079cf797
+ 00693d30 bytes 019cf797
- 00693ce4 ["INT_ADD", "register:40f0:8", ["const:693ce4:8", "const:4:8"]]
- 00693ce4 ["CALL", null, ["ram:47acf4:8"]]
- 00693ce4 bytes 049cf797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4754acee885b424260e3f95d27867e8"></a>

### [`00693d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693d88.md) → [`00693de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693de0.md) FUN_00693de0

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0068bad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bad0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`004709d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004709d4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0068bb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068bb28.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.27% / 新版 79.27%

CFGの説明率　旧版 37.74% / 新版 34.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00693d8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00693d8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00693d90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00693d8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00693d90",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00693d94",
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
      "00693de4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00693de8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00693dec",
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

- 旧版 [`00693d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693d88.md#insn-00693d8c) · [`00693d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693d88.md#insn-00693d90) · [`00693d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693d88.md#insn-00693d94)

~~~diff
- 00693d8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00693d8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00693d8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00693d8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00693d8c bytes fd7b07a9
- 00693d90 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00693d90 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00693d90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00693d90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00693d90 bytes fc6f08a9
- 00693d94 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00693d94 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00693d94 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00693d94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00693d94 bytes fa6709a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d22e1584ca34504af85b704b3b01d9a"></a>

### [`0069439c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069439c.md) → [`006943f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006943f4.md) FUN_006943f4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0068a9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a9ac.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068aa04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068aa04.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 66.67% / 新版 66.67%

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
      "site": "0069441c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006943c4",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "0069442c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006943d4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "006943ec",
      "incomplete_value": true,
      "site": "006943f4",
      "value": [
        "live",
        "register:4098:8"
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
      "0069441c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0069442c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0069441c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "0069442c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006943c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069439c.md#insn-006943c4) · [`006943d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069439c.md#insn-006943d4) · [`006943f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069439c.md#insn-006943f4)
- 新版 [`0069441c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006943f4.md#insn-0069441c) · [`0069442c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006943f4.md#insn-0069442c) · [`0069444c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006943f4.md#insn-0069444c)

~~~diff
- 006943c4 ["INT_ADD", "register:40f0:8", ["const:6943c4:8", "const:4:8"]]
- 006943c4 ["CALL", null, ["ram:47acf4:8"]]
+ 0069441c ["INT_ADD", "register:40f0:8", ["const:69441c:8", "const:4:8"]]
+ 0069441c ["CALL", null, ["ram:47ad34:8"]]
- 006943c4 bytes 4c9af797
+ 0069441c bytes 469af797
- 006943d4 ["INT_ADD", "register:40f0:8", ["const:6943d4:8", "const:4:8"]]
- 006943d4 ["CALL", null, ["ram:47acf4:8"]]
+ 0069442c ["INT_ADD", "register:40f0:8", ["const:69442c:8", "const:4:8"]]
+ 0069442c ["CALL", null, ["ram:47ad34:8"]]
- 006943d4 bytes 489af797
+ 0069442c bytes 429af797
- 006943f4 ["INT_ADD", "register:40f0:8", ["const:6943f4:8", "const:4:8"]]
- 006943f4 ["CALL", null, ["callee:0068aa04:8"]]
+ 0069444c ["INT_ADD", "register:40f0:8", ["const:69444c:8", "const:4:8"]]
+ 0069444c ["CALL", null, ["callee:0068aa04:8"]]
- 006943f4 bytes 6ed9ff97
+ 0069444c bytes 6ed9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1435723f171821e4959e79662a030e1b"></a>

### [`006944b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006944b4.md) → [`0069450c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/0069450c.md) FUN_0069450c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00694518",
      "incomplete_value": false,
      "site": "00694518",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006944c0",
      "incomplete_value": false,
      "site": "006944c0",
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
            "const:cd0:8"
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
      "00694518",
      "DATA",
      [
        "storage",
        "00c74cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694518",
      "DATA",
      [
        "storage",
        "00c74da0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006944bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006944b4.md#insn-006944bc)
- 新版 [`00694514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/0069450c.md#insn-00694514)

~~~diff
- 006944bc ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 006944bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006944bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006944bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00694514 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00694514 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00694514 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00694514 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006944bc bytes 29413391
+ 00694514 bytes 29813691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-025384312002b968210d32bce16362c2"></a>

### [`0069456c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069456c.md) → [`006945c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006945c4.md) FUN_006945c4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "006945e8",
      "incomplete_value": false,
      "site": "006945e8",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00694590",
      "incomplete_value": false,
      "site": "00694590",
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
            "const:d50:8"
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
      "006945e8",
      "DATA",
      [
        "storage",
        "00c74d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006945e8",
      "DATA",
      [
        "storage",
        "00c74e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069456c.md#insn-00694580) · [`0069458c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069456c.md#insn-0069458c)
- 新版 [`006945d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006945c4.md#insn-006945d8) · [`006945e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006945c4.md#insn-006945e4)

~~~diff
- 00694580 ["INT_ADD", "register:40f0:8", ["const:694580:8", "const:4:8"]]
- 00694580 ["CALL", null, ["callee:00c57f60:8"]]
+ 006945d8 ["INT_ADD", "register:40f0:8", ["const:6945d8:8", "const:4:8"]]
+ 006945d8 ["CALL", null, ["callee:00c57f60:8"]]
- 00694580 bytes 440e1794
+ 006945d8 bytes 620e1794
- 0069458c ["COPY", "tmp:0:8", ["const:d50:8"]]
- 0069458c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0069458c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0069458c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006945e4 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 006945e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006945e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006945e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0069458c bytes 08413591
+ 006945e4 bytes 08813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1e9546154ed3bce8fab0385970a35bd"></a>

### [`006945a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006945a0.md) → [`006945f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006945f8.md) FUN_006945f8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00694604",
      "incomplete_value": false,
      "site": "00694604",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006945ac",
      "incomplete_value": false,
      "site": "006945ac",
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
            "const:d50:8"
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
      "00694604",
      "DATA",
      [
        "storage",
        "00c74d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694604",
      "DATA",
      [
        "storage",
        "00c74e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006945a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006945a0.md#insn-006945a8)
- 新版 [`00694600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006945f8.md#insn-00694600)

~~~diff
- 006945a8 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 006945a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006945a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006945a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00694600 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 00694600 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00694600 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00694600 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006945a8 bytes 29413591
+ 00694600 bytes 29813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05a66ffa06e84c6eeb27d924e0f6d90b"></a>

### [`006945bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006945bc.md) → [`00694614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694614.md) FUN_00694614

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a468d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468d8.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`00a4692c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a4692c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.61% / 新版 96.61%

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
      "site": "006946b8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00694660",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "006946e4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0069468c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 9,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006946b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006946e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "006946b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006946e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006945bc.md#insn-00694634) · [`00694660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006945bc.md#insn-00694660) · [`0069468c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006945bc.md#insn-0069468c)
- 新版 [`0069468c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694614.md#insn-0069468c) · [`006946b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694614.md#insn-006946b8) · [`006946e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694614.md#insn-006946e4)

~~~diff
- 00694634 ["INT_ADD", "register:40f0:8", ["const:694634:8", "const:4:8"]]
- 00694634 ["CALL", null, ["callee:00851550:8"]]
+ 0069468c ["INT_ADD", "register:40f0:8", ["const:69468c:8", "const:4:8"]]
+ 0069468c ["CALL", null, ["callee:00851550:8"]]
- 00694634 bytes b1f30694
+ 0069468c bytes b1f30694
- 00694660 ["INT_ADD", "register:40f0:8", ["const:694660:8", "const:4:8"]]
- 00694660 ["CALL", null, ["ram:47acf4:8"]]
+ 006946b8 ["INT_ADD", "register:40f0:8", ["const:6946b8:8", "const:4:8"]]
+ 006946b8 ["CALL", null, ["ram:47ad34:8"]]
- 00694660 bytes a599f797
+ 006946b8 bytes 9f99f797
- 0069468c ["INT_ADD", "register:40f0:8", ["const:69468c:8", "const:4:8"]]
- 0069468c ["CALL", null, ["ram:47acf4:8"]]
+ 006946e4 ["INT_ADD", "register:40f0:8", ["const:6946e4:8", "const:4:8"]]
+ 006946e4 ["CALL", null, ["ram:47ad34:8"]]
- 0069468c bytes 9a99f797
+ 006946e4 bytes 9499f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07745f60b238c9d101dbb18b6ad8432b"></a>

### [`006946d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006946d4.md) → [`0069472c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/0069472c.md) FUN_0069472c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00694750",
      "incomplete_value": false,
      "site": "00694758",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006946f8",
      "incomplete_value": false,
      "site": "00694700",
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
            "const:dd0:8"
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
      "00694758",
      "DATA",
      [
        "storage",
        "00c74dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694758",
      "DATA",
      [
        "storage",
        "00c74ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006946e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006946d4.md#insn-006946e8) · [`006946f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006946d4.md#insn-006946f8)
- 新版 [`00694740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/0069472c.md#insn-00694740) · [`00694750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/0069472c.md#insn-00694750)

~~~diff
- 006946e8 ["INT_ADD", "register:40f0:8", ["const:6946e8:8", "const:4:8"]]
- 006946e8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00694740 ["INT_ADD", "register:40f0:8", ["const:694740:8", "const:4:8"]]
+ 00694740 ["CALL", null, ["callee:00c57f60:8"]]
- 006946e8 bytes ea0d1794
+ 00694740 bytes 080e1794
- 006946f8 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 006946f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006946f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006946f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00694750 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00694750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00694750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00694750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006946f8 bytes 08413791
+ 00694750 bytes 08813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1420f0577dabb04abb49a9ff88a23eab"></a>

### [`0069471c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069471c.md) → [`00694774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694774.md) FUN_00694774

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00694778",
      "incomplete_value": false,
      "site": "0069477c",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00694720",
      "incomplete_value": false,
      "site": "00694724",
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
            "const:dd0:8"
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
      "0069477c",
      "DATA",
      [
        "storage",
        "00c74dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069477c",
      "DATA",
      [
        "storage",
        "00c74ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069471c.md#insn-00694720)
- 新版 [`00694778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694774.md#insn-00694778)

~~~diff
- 00694720 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 00694720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00694720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00694720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00694778 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00694778 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00694778 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00694778 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00694720 bytes 08413791
+ 00694778 bytes 08813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76b04cb8d8f02fce795ac543be233e23"></a>

### [`0069474c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069474c.md) → [`006947a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006947a4.md) FUN_006947a4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.84% / 新版 96.84%

CFGの説明率　旧版 62.79% / 新版 61.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00694920"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00694978"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00694850",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006947f8",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00694850",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00694878",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00694850",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00694878",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006947f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069474c.md#insn-006947f8) · [`00694820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069474c.md#insn-00694820) · [`006948a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069474c.md#insn-006948a8)
- 新版 [`00694850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006947a4.md#insn-00694850) · [`00694878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006947a4.md#insn-00694878) · [`00694900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006947a4.md#insn-00694900)

~~~diff
- 006947f8 ["INT_ADD", "register:40f0:8", ["const:6947f8:8", "const:4:8"]]
- 006947f8 ["CALL", null, ["ram:47acf4:8"]]
+ 00694850 ["INT_ADD", "register:40f0:8", ["const:694850:8", "const:4:8"]]
+ 00694850 ["CALL", null, ["ram:47ad34:8"]]
- 006947f8 bytes 3f99f797
+ 00694850 bytes 3999f797
- 00694820 ["INT_ADD", "register:40f0:8", ["const:694820:8", "const:4:8"]]
- 00694820 ["CALL", null, ["ram:47acf4:8"]]
+ 00694878 ["INT_ADD", "register:40f0:8", ["const:694878:8", "const:4:8"]]
+ 00694878 ["CALL", null, ["ram:47ad34:8"]]
- 00694820 bytes 3599f797
+ 00694878 bytes 2f99f797
- 006948a8 ["INT_ADD", "register:40f0:8", ["const:6948a8:8", "const:4:8"]]
- 006948a8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00694900 ["INT_ADD", "register:40f0:8", ["const:694900:8", "const:4:8"]]
+ 00694900 ["CALL", null, ["callee:00c57f60:8"]]
- 006948a8 bytes 7a0d1794
+ 00694900 bytes 980d1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a99e81991c6ec176a3cc4293a8a62da1"></a>

### [`006949f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006949f0.md) → [`00694a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a48.md) FUN_00694a48

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00694a6c",
      "incomplete_value": false,
      "site": "00694a6c",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00694a14",
      "incomplete_value": false,
      "site": "00694a14",
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
            "const:e50:8"
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
      "00694a6c",
      "DATA",
      [
        "storage",
        "00c74e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694a6c",
      "DATA",
      [
        "storage",
        "00c74f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006949f0.md#insn-00694a04) · [`00694a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006949f0.md#insn-00694a10)
- 新版 [`00694a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a48.md#insn-00694a5c) · [`00694a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a48.md#insn-00694a68)

~~~diff
- 00694a04 ["INT_ADD", "register:40f0:8", ["const:694a04:8", "const:4:8"]]
- 00694a04 ["CALL", null, ["callee:00c57f60:8"]]
+ 00694a5c ["INT_ADD", "register:40f0:8", ["const:694a5c:8", "const:4:8"]]
+ 00694a5c ["CALL", null, ["callee:00c57f60:8"]]
- 00694a04 bytes 230d1794
+ 00694a5c bytes 410d1794
- 00694a10 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00694a10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00694a10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00694a10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00694a68 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00694a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00694a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00694a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00694a10 bytes 08413991
+ 00694a68 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-921d3567957037ef210e7c525689572e"></a>

### [`00694a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694a40.md) → [`00694a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a98.md) FUN_00694a98

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00694a48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00694aa0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00694a5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00694a48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00694ad4"
      ]
    ],
    [
      "unmatched:00694a5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00694aa0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00694ad4"
      ]
    ],
    [
      "00694ab4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694a40.md#insn-00694a48) · [`00694a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694a40.md#insn-00694a5c)
- 新版 [`00694aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a98.md#insn-00694aa0)

~~~diff
- 00694a48 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00694a48 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00694a48 bytes a1010054
- 00694a5c ["INT_ADD", "register:40f0:8", ["const:694a5c:8", "const:4:8"]]
- 00694a5c ["CALL", null, ["ram:47acf4:8"]]
- 00694a5c bytes a698f797
+ 00694aa0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00694aa0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00694aa0 bytes a1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f79605415f9ed11ed84089475c6c0ccd"></a>

### [`00694aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694aac.md) → [`00694b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694b04.md) FUN_00694b04

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00694b28",
      "incomplete_value": false,
      "site": "00694b2c",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00694ad0",
      "incomplete_value": false,
      "site": "00694ad4",
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
            "const:ed0:8"
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
      "00694b2c",
      "DATA",
      [
        "storage",
        "00c74ed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694b2c",
      "DATA",
      [
        "storage",
        "00c74fa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694aac.md#insn-00694ac0) · [`00694ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694aac.md#insn-00694ad0)
- 新版 [`00694b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694b04.md#insn-00694b18) · [`00694b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694b04.md#insn-00694b28)

~~~diff
- 00694ac0 ["INT_ADD", "register:40f0:8", ["const:694ac0:8", "const:4:8"]]
- 00694ac0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00694b18 ["INT_ADD", "register:40f0:8", ["const:694b18:8", "const:4:8"]]
+ 00694b18 ["CALL", null, ["callee:00c57f60:8"]]
- 00694ac0 bytes f40c1794
+ 00694b18 bytes 120d1794
- 00694ad0 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 00694ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00694ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00694ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00694b28 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 00694b28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00694b28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00694b28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00694ad0 bytes 08413b91
+ 00694b28 bytes 08813e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-281638886933ba142c1c37a520725683"></a>

### [`00694b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694b14.md) → [`00694b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694b6c.md) FUN_00694b6c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006847fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/006847fc.md) [`0068ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068ed80.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068483c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/0068483c.md) [`0068edd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068edd8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 62.07% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694b38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00694b90"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00694b54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00694b38",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00694b54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00694bd8"
      ]
    ],
    [
      "00694bb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00694b90",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00694bac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00694bd8"
      ]
    ],
    [
      "00694bb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694b14.md#insn-00694b38) · [`00694b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694b14.md#insn-00694b54) · [`00694b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694b14.md#insn-00694b60)
- 新版 [`00694bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694b6c.md#insn-00694bb8)

~~~diff
- 00694b38 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00694b38 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00694b38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00694b38 bytes a8831ff8
- 00694b54 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00694b54 bytes 60010054
- 00694b60 ["INT_ADD", "register:40f0:8", ["const:694b60:8", "const:4:8"]]
- 00694b60 ["CALL", null, ["ram:47acf4:8"]]
+ 00694bb8 ["INT_ADD", "register:40f0:8", ["const:694bb8:8", "const:4:8"]]
+ 00694bb8 ["CALL", null, ["ram:47ad34:8"]]
- 00694b60 bytes 6598f797
+ 00694bb8 bytes 5f98f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e8645fbf5ec2c17cbc580e499309b7d"></a>

### [`00694cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694cc4.md) → [`00694d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d1c.md) FUN_00694d1c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00694d28",
      "incomplete_value": false,
      "site": "00694d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00694cd0",
      "incomplete_value": false,
      "site": "00694cd4",
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
            "const:f50:8"
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
      "00694d2c",
      "DATA",
      [
        "storage",
        "00c74f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694d2c",
      "DATA",
      [
        "storage",
        "00c75020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694cc4.md#insn-00694ccc) · [`00694cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694cc4.md#insn-00694cd0)
- 新版 [`00694d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d1c.md#insn-00694d24) · [`00694d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d1c.md#insn-00694d28)

~~~diff
- 00694ccc ["COPY", "register:4048:8", ["const:c74000:8"]]
+ 00694d24 ["COPY", "register:4048:8", ["const:c75000:8"]]
- 00694ccc bytes 092f0090
+ 00694d24 bytes 092f00b0
- 00694cd0 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 00694cd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00694cd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00694cd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00694d28 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 00694d28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00694d28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00694d28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00694cd0 bytes 29413d91
+ 00694d28 bytes 29810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d30d2c8b2e953cec894b386342d5a2e"></a>

### [`00694ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694ce8.md) → [`00694d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d40.md) FUN_00694d40

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

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
      "site": "00694cf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00694d4c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00694d68",
      "incomplete_value": true,
      "site": "00694d6c",
      "value": [
        "live",
        "register:4040:8"
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
      "unmatched:00694cf4",
      "DATA",
      [
        "storage",
        "00c74f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694d4c",
      "DATA",
      [
        "storage",
        "00c75020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694ce8.md#insn-00694cf4) · [`00694d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694ce8.md#insn-00694d14)
- 新版 [`00694d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d40.md#insn-00694d6c) · [`00694d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d40.md#insn-00694d4c)

~~~diff
- 00694cf4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00694cf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00694cf4 bytes 090000f9
- 00694d14 ["INT_ADD", "register:40f0:8", ["const:694d14:8", "const:4:8"]]
- 00694d14 ["CALL", null, ["callee:00c57f80:8"]]
+ 00694d6c ["INT_ADD", "register:40f0:8", ["const:694d6c:8", "const:4:8"]]
+ 00694d6c ["CALL", null, ["callee:00c57f80:8"]]
- 00694d14 bytes 670c1794
+ 00694d6c bytes 850c1794
+ 00694d4c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00694d4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00694d4c bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46dca3f4e4548eee0d9eb599b085d7e5"></a>

### [`00694d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694d28.md) → [`00694d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d80.md) FUN_00694d80

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`006924c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924c4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00694da0",
      "incomplete_value": false,
      "site": "00694da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00694d48",
      "incomplete_value": false,
      "site": "00694d50",
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
            "const:f50:8"
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
      "00694da8",
      "DATA",
      [
        "storage",
        "00c74f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694da8",
      "DATA",
      [
        "storage",
        "00c75020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694d28.md#insn-00694d40) · [`00694d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694d28.md#insn-00694d44) · [`00694d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694d28.md#insn-00694d48)
- 新版 [`00694d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d80.md#insn-00694d98) · [`00694d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d80.md#insn-00694d9c) · [`00694da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d80.md#insn-00694da0)

~~~diff
- 00694d40 ["INT_ADD", "register:40f0:8", ["const:694d40:8", "const:4:8"]]
- 00694d40 ["CALL", null, ["callee:00c57f60:8"]]
+ 00694d98 ["INT_ADD", "register:40f0:8", ["const:694d98:8", "const:4:8"]]
+ 00694d98 ["CALL", null, ["callee:00c57f60:8"]]
- 00694d40 bytes 540c1794
+ 00694d98 bytes 720c1794
- 00694d44 ["COPY", "register:4040:8", ["const:c74000:8"]]
+ 00694d9c ["COPY", "register:4040:8", ["const:c75000:8"]]
- 00694d44 bytes 082f0090
+ 00694d9c bytes 082f00b0
- 00694d48 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 00694d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00694d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00694d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00694da0 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 00694da0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00694da0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00694da0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00694d48 bytes 08413d91
+ 00694da0 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92b4fb0ff8f3bb6e0efe6097ee0c3041"></a>

### [`00694de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694de0.md) → [`00694e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694e38.md) FUN_00694e38

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`006924c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924c4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00694e4c",
      "incomplete_value": false,
      "site": "00694e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00694df4",
      "incomplete_value": false,
      "site": "00694dfc",
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
            "const:f50:8"
          ]
        ]
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
      "definition_site": "00694e78",
      "incomplete_value": true,
      "site": "00694e7c",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00694e54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00694e54",
      "DATA",
      [
        "storage",
        "00c74f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694e54",
      "DATA",
      [
        "storage",
        "00c75020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694de0.md#insn-00694e54) · [`00694e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694de0.md#insn-00694e7c)
- 新版 [`00694ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694e38.md#insn-00694ed4) · [`00694eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694e38.md#insn-00694eac)

~~~diff
- 00694e54 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00694e54 ["RETURN", null, ["register:0:8"]]
- 00694e54 bytes c0035fd6
- 00694e7c ["INT_ADD", "register:40f0:8", ["const:694e7c:8", "const:4:8"]]
- 00694e7c ["CALL", null, ["callee:00c53ffc:8"]]
+ 00694ed4 ["INT_ADD", "register:40f0:8", ["const:694ed4:8", "const:4:8"]]
+ 00694ed4 ["CALL", null, ["callee:00c53ffc:8"]]
- 00694e7c bytes 38fc1694
+ 00694ed4 bytes 4afc1694
+ 00694eac ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00694eac ["RETURN", null, ["register:0:8"]]
+ 00694eac bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aa27b02844a43176d7f49a872b9dc9f"></a>

### [`00694e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694e80.md) → [`00694ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694ed8.md) FUN_00694ed8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00694e88"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00694ee0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00694e88"
      ],
      [
        "FALL_THROUGH",
        "00694ee0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00694ee0",
      "incomplete_value": true,
      "site": "00694ee4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00694e88",
      "incomplete_value": true,
      "site": "00694e8c",
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
      "unmatched:00694e88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00694eec"
      ]
    ]
  ],
  "added": [
    [
      "00694ee0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00694eec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694e80.md#insn-00694e88) · [`00694e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694e80.md#insn-00694e80)
- 新版 [`00694ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694ed8.md#insn-00694ee0)

~~~diff
- 00694e88 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00694e88 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00694e88 bytes 600000b4
+ 00694ee0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00694ee0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00694ee0 bytes 600000b4
- 00694e80 ["COPY", "register:4040:8", ["register:4000:8"]]
- 00694e80 bytes e80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48f16dc6440b60147b9c9af8d5519567"></a>

### [`00694ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694ecc.md) → [`00694f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694f24.md) FUN_00694f24

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`00684fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684fb0.md) [`00685374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685374.md) [`00691e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e2c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00684ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684ff0.md) [`006853b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/006853b4.md) [`00691e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b92e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92e8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.48% / 新版 96.48%

CFGの説明率　旧版 87.27% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00694f58"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00694fb0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00694fd0",
      "incomplete_value": true,
      "site": "00694fe0",
      "value": [
        "TRUNC",
        "4",
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
    "old": null,
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
      "00694f80",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[59]"
      ]
    ],
    [
      "unmatched:00694f58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00694ffc"
      ]
    ],
    [
      "00694ff4",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[59]"
      ]
    ]
  ],
  "added": [
    [
      "00694f80",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[47]"
      ]
    ],
    [
      "00694fb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00694ffc"
      ]
    ],
    [
      "00694ff4",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[47]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694ecc.md#insn-00694f00) · [`00694f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694ecc.md#insn-00694f58) · [`00694f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694ecc.md#insn-00694f88)
- 新版 [`00694f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694f24.md#insn-00694f58) · [`00694fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694f24.md#insn-00694fe0)

~~~diff
- 00694f00 ["INT_ADD", "register:40f0:8", ["const:694f00:8", "const:4:8"]]
- 00694f00 ["CALL", null, ["callee:008b92e8:8"]]
+ 00694f58 ["INT_ADD", "register:40f0:8", ["const:694f58:8", "const:4:8"]]
+ 00694f58 ["CALL", null, ["callee:008b92e8:8"]]
- 00694f00 bytes e4900894
+ 00694f58 bytes e4900894
- 00694f58 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00694f58 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00694f58 bytes 6a020054
- 00694f88 ["INT_ADD", "register:40f0:8", ["const:694f88:8", "const:4:8"]]
- 00694f88 ["CALL", null, ["callee:009dce94:8"]]
+ 00694fe0 ["INT_ADD", "register:40f0:8", ["const:694fe0:8", "const:4:8"]]
+ 00694fe0 ["CALL", null, ["callee:009dce94:8"]]
- 00694f88 bytes ae1f0d94
+ 00694fe0 bytes ad1f0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4947c78b57f2baa759737f741b5deabe"></a>

### [`006952f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/006952f4.md) → [`0069534c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/0069534c.md) FUN_0069534c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00695358",
      "incomplete_value": false,
      "site": "0069535c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00695300",
      "incomplete_value": false,
      "site": "00695304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "0069535c",
      "DATA",
      [
        "storage",
        "00c75000",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069535c",
      "DATA",
      [
        "storage",
        "00c750d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00695300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/006952f4.md#insn-00695300)
- 新版 [`00695358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/0069534c.md#insn-00695358)

~~~diff
- 00695300 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00695300 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00695300 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00695300 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00695358 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 00695358 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00695358 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00695358 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00695300 bytes 29010091
+ 00695358 bytes 29410391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06eea2c89e8fb2c73c4dfbb5335867f7"></a>

### [`00695318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695318.md) → [`00695370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695370.md) FUN_00695370

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00695378",
      "incomplete_value": false,
      "site": "0069537c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00695320",
      "incomplete_value": false,
      "site": "00695324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "0069537c",
      "DATA",
      [
        "storage",
        "00c75000",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069537c",
      "DATA",
      [
        "storage",
        "00c750d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00695320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695318.md#insn-00695320) · [`00695344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695318.md#insn-00695344)
- 新版 [`00695378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695370.md#insn-00695378) · [`0069539c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695370.md#insn-0069539c)

~~~diff
- 00695320 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00695320 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00695320 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00695320 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00695378 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 00695378 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00695378 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00695378 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00695320 bytes 29010091
+ 00695378 bytes 29410391
- 00695344 ["INT_ADD", "register:40f0:8", ["const:695344:8", "const:4:8"]]
- 00695344 ["CALL", null, ["callee:00c57f80:8"]]
+ 0069539c ["INT_ADD", "register:40f0:8", ["const:69539c:8", "const:4:8"]]
+ 0069539c ["CALL", null, ["callee:00c57f80:8"]]
- 00695344 bytes db0a1794
+ 0069539c bytes f90a1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb902f7787bd2d9e279f7788f5485c60"></a>

### [`00695358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695358.md) → [`006953b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/006953b0.md) FUN_006953b0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`006924c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924c4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006953d0",
      "incomplete_value": false,
      "site": "006953d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00695378",
      "incomplete_value": false,
      "site": "00695380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "006953d8",
      "DATA",
      [
        "storage",
        "00c75000",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006953d8",
      "DATA",
      [
        "storage",
        "00c750d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00695370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695358.md#insn-00695370) · [`00695378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695358.md#insn-00695378) · [`006953b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695358.md#insn-006953b4)
- 新版 [`006953c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/006953b0.md#insn-006953c8) · [`006953d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/006953b0.md#insn-006953d0) · [`0069540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/006953b0.md#insn-0069540c)

~~~diff
- 00695370 ["INT_ADD", "register:40f0:8", ["const:695370:8", "const:4:8"]]
- 00695370 ["CALL", null, ["callee:00c57f60:8"]]
+ 006953c8 ["INT_ADD", "register:40f0:8", ["const:6953c8:8", "const:4:8"]]
+ 006953c8 ["CALL", null, ["callee:00c57f60:8"]]
- 00695370 bytes c80a1794
+ 006953c8 bytes e60a1794
- 00695378 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00695378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00695378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00695378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006953d0 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 006953d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006953d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006953d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00695378 bytes 08010091
+ 006953d0 bytes 08410391
- 006953b4 ["INT_ADD", "register:40f0:8", ["const:6953b4:8", "const:4:8"]]
- 006953b4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0069540c ["INT_ADD", "register:40f0:8", ["const:69540c:8", "const:4:8"]]
+ 0069540c ["CALL", null, ["callee:00c57f60:8"]]
- 006953b4 bytes b70a1794
+ 0069540c bytes d50a1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9984cc8c760303bfd58fa5c4db16cb52"></a>

### [`00695418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695418.md) → [`00695470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695470.md) FUN_00695470

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`006924c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924c4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00695484",
      "incomplete_value": false,
      "site": "0069548c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0069542c",
      "incomplete_value": false,
      "site": "00695434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "0069548c",
      "DATA",
      [
        "storage",
        "00c75000",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069548c",
      "DATA",
      [
        "storage",
        "00c750d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069542c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695418.md#insn-0069542c) · [`00695468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695418.md#insn-00695468) · [`00695480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695418.md#insn-00695480)
- 新版 [`00695484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695470.md#insn-00695484) · [`006954c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695470.md#insn-006954c0) · [`006954d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695470.md#insn-006954d8)

~~~diff
- 0069542c ["COPY", "tmp:0:8", ["const:0:8"]]
- 0069542c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0069542c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0069542c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00695484 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 00695484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00695484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00695484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0069542c bytes 08010091
+ 00695484 bytes 08410391
- 00695468 ["INT_ADD", "register:40f0:8", ["const:695468:8", "const:4:8"]]
- 00695468 ["CALL", null, ["callee:00c57f60:8"]]
+ 006954c0 ["INT_ADD", "register:40f0:8", ["const:6954c0:8", "const:4:8"]]
+ 006954c0 ["CALL", null, ["callee:00c57f60:8"]]
- 00695468 bytes 8a0a1794
+ 006954c0 bytes a80a1794
- 00695480 ["INT_ADD", "register:40f0:8", ["const:695480:8", "const:4:8"]]
- 00695480 ["CALL", null, ["callee:00c580d0:8"]]
+ 006954d8 ["INT_ADD", "register:40f0:8", ["const:6954d8:8", "const:4:8"]]
+ 006954d8 ["CALL", null, ["callee:00c580d0:8"]]
- 00695480 bytes e00a1794
+ 006954d8 bytes fe0a1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-703bb4ccba6f89f18c9a511916c6fc5e"></a>

### [`0069550c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/0069550c.md) → [`00695564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695564.md) FUN_00695564

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 24件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md)
- 新版 呼出元 0件  · 呼出先 24件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 93.52% / 新版 93.52%

CFGの説明率　旧版 71.43% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006955c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0069561c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00695594"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0069557c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:00695580",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00695588",
      "PARAM",
      [
        "storage",
        "00c74fd8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006955d4",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006955d8",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006955e0",
      "PARAM",
      [
        "storage",
        "00c750a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069556c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/0069550c.md#insn-0069556c) · [`00695594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/0069550c.md#insn-00695594) · [`006955b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/0069550c.md#insn-006955b4)
- 新版 [`006955c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695564.md#insn-006955c4) · [`0069560c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695564.md#insn-0069560c)

~~~diff
- 0069556c ["INT_ADD", "register:40f0:8", ["const:69556c:8", "const:4:8"]]
- 0069556c ["CALL", null, ["callee:004678a0:8"]]
+ 006955c4 ["INT_ADD", "register:40f0:8", ["const:6955c4:8", "const:4:8"]]
+ 006955c4 ["CALL", null, ["callee:004678a0:8"]]
- 0069556c bytes bd48f797
+ 006955c4 bytes b748f797
- 00695594 ["INT_ADD", "register:40f0:8", ["const:695594:8", "const:4:8"]]
- 00695594 ["CALL", null, ["callee:00c586e0:8"]]
- 00695594 bytes 1f0c1794
- 006955b4 ["INT_ADD", "register:40f0:8", ["const:6955b4:8", "const:4:8"]]
- 006955b4 ["CALL", null, ["callee:00695c04:8"]]
+ 0069560c ["INT_ADD", "register:40f0:8", ["const:69560c:8", "const:4:8"]]
+ 0069560c ["CALL", null, ["callee:00695c04:8"]]
- 006955b4 bytes 7e010094
+ 0069560c bytes 7e010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48a4a7e88be6add1c914fc3ec577acd0"></a>

### [`006959f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/006959f0.md) → [`00695a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695a48.md) FUN_00695a48

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0069550c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/0069550c.md) [`00696710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696710.md) [`00697fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697fd4.md) [`0069927c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00699/0069927c.md) · 呼出先 3件 [`005d8a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8a6c.md) [`00695f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695f50.md) [`00c5a820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a820.md)
- 新版 呼出元 4件 [`00695564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695564.md) [`00696768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696768.md) [`0069802c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/0069802c.md) [`006992d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006992d4.md) · 呼出先 3件 [`005d8aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8aac.md) [`00695fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695fa8.md) [`00c5a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.20% / 新版 94.20%

CFGの説明率　旧版 48.15% / 新版 48.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00695ac4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00695b1c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00695b34",
      "incomplete_value": true,
      "site": "00695b40",
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
            "const:10:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00695ac4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695b2c"
      ]
    ]
  ],
  "added": [
    [
      "00695b1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695b2c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00695ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/006959f0.md#insn-00695ac4) · [`00695ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/006959f0.md#insn-00695ae8)
- 新版 [`00695ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695a48.md#insn-00695ac4) · [`00695b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695a48.md#insn-00695b40)

~~~diff
- 00695ac4 ["CBRANCH", null, ["local:b14:8", "register:102:1"]]
- 00695ac4 bytes 82000054
+ 00695ac4 ["INT_ZEXT", "tmp:0:9", ["register:4040:8"]]
+ 00695ac4 ["INT2FLOAT", "register:5000:4", ["tmp:0:9"]]
+ 00695ac4 ["COPY", "register:5004:4", ["const:0:4"]]
+ 00695ac4 ["COPY", "register:5008:8", ["const:0:8"]]
+ 00695ac4 bytes 0001239e
- 00695ae8 ["INT_ADD", "register:40f0:8", ["const:695ae8:8", "const:4:8"]]
- 00695ae8 ["CALL", null, ["callee:00695fa8:8"]]
+ 00695b40 ["INT_ADD", "register:40f0:8", ["const:695b40:8", "const:4:8"]]
+ 00695b40 ["CALL", null, ["callee:00695fa8:8"]]
- 00695ae8 bytes 1a010094
+ 00695b40 bytes 1a010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84a6736e64fdcc732e50a6ea86baf2bb"></a>

### [`00695b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695b1c.md) → [`00695b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695b74.md) FUN_00695b74

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 38.46% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00695bcc",
      "incomplete_value": false,
      "site": "00695bd0",
      "value": [
        "leaf",
        "const:ffffffffffffffff:8"
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
      "definition_site": "00695bc8",
      "incomplete_value": true,
      "site": "00695bd0",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00695b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695b1c.md#insn-00695b78) · [`00695b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695b1c.md#insn-00695b40) · [`00695b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695b1c.md#insn-00695b58)
- 新版 [`00695bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695b74.md#insn-00695bd0) · [`00695b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695b74.md#insn-00695b98) · [`00695bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695b74.md#insn-00695bb0)

~~~diff
- 00695b78 ["INT_ADD", "register:40f0:8", ["const:695b78:8", "const:4:8"]]
- 00695b78 ["CALL", null, ["callee:00c53da0:8"]]
+ 00695bd0 ["INT_ADD", "register:40f0:8", ["const:695bd0:8", "const:4:8"]]
+ 00695bd0 ["CALL", null, ["callee:00c53da0:8"]]
- 00695b78 bytes 62f81694
+ 00695bd0 bytes 74f81694
- 00695b40 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00695b40 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00695b98 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00695b98 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00695b40 bytes e00200b4
+ 00695b98 bytes e00200b4
- 00695b58 ["INT_ADD", "register:40f0:8", ["const:695b58:8", "const:4:8"]]
- 00695b58 ["CALL", null, ["callee:00c57f80:8"]]
+ 00695bb0 ["INT_ADD", "register:40f0:8", ["const:695bb0:8", "const:4:8"]]
+ 00695bb0 ["CALL", null, ["callee:00c57f80:8"]]
- 00695b58 bytes d6081794
+ 00695bb0 bytes f4081794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c071e57df3a95a49af76793d2f4d3e6"></a>

### [`00695bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695bac.md) → [`00695c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695c04.md) FUN_00695c04

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 20件 [`0069550c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/0069550c.md) [`00697fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697fd4.md) [`00698a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698a78.md) [`0090b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090b/0090b908.md) [`0091ab78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0091a/0091ab78.md) · 呼出先 4件 [`005d8a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8a6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a820.md)
- 新版 呼出元 20件 [`00695564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695564.md) [`0069802c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/0069802c.md) [`00698ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698ad0.md) [`0090b95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090b/0090b95c.md) [`0091abcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0091a/0091abcc.md) · 呼出先 4件 [`005d8aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8aac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 46.88% / 新版 47.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695cb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695cb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695e14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00695dd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695e34"
      ]
    ],
    [
      "unmatched:00695dfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695e64"
      ]
    ],
    [
      "unmatched:00695e74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695f14"
      ]
    ]
  ],
  "added": [
    [
      "00695e28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695e34"
      ]
    ],
    [
      "00695e54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695e64"
      ]
    ],
    [
      "00695ecc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695f14"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00695cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695bac.md#insn-00695cb0) · [`00695cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695bac.md#insn-00695cd4) · [`00695d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695bac.md#insn-00695d08)

~~~diff
- 00695cb0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00695cb0 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00695cb0 ["COPY", "tmp:2:8", ["register:40c0:8"]]
- 00695cb0 ["COPY", "tmp:3:8", ["register:4000:8"]]
- 00695cb0 bytes 1f6000a9
- 00695cd4 ["COPY", "register:100:1", ["const:0:1"]]
- 00695cd4 ["COPY", "register:101:1", ["const:0:1"]]
- 00695cd4 ["COPY", "register:102:1", ["const:1:1"]]
- 00695cd4 ["COPY", "register:103:1", ["const:1:1"]]
- 00695cd4 bytes 4020201e
- 00695d08 ["INT_LESSEQUAL", "register:105:1", ["register:4050:8", "register:4040:8"]]
- 00695d08 ["INT_SBORROW", "register:106:1", ["register:4040:8", "register:4050:8"]]
- 00695d08 ["INT_SUB", "tmp:0:8", ["register:4040:8", "register:4050:8"]]
- 00695d08 ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
- 00695d08 bytes 1f010aeb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cef58d9f82a16fedaf0373dfe878b12"></a>

### [`00695ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695ec0.md) → [`00695f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695f18.md) FUN_00695f18

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.22% / 新版 97.22%

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
      "site": "00695ee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00695f3c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00695f6c",
      "incomplete_value": true,
      "site": "00695f74",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00695ee4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695f98"
      ]
    ]
  ],
  "added": [
    [
      "00695f3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695f98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00695ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695ec0.md#insn-00695ee4) · [`00695f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695ec0.md#insn-00695f1c) · [`00695f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695ec0.md#insn-00695f38)
- 新版 [`00695f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695f18.md#insn-00695f74) · [`00695f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695f18.md#insn-00695f90)

~~~diff
- 00695ee4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00695ee4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00695ee4 bytes e00200b4
- 00695f1c ["INT_ADD", "register:40f0:8", ["const:695f1c:8", "const:4:8"]]
- 00695f1c ["CALL", null, ["callee:00c53da0:8"]]
+ 00695f74 ["INT_ADD", "register:40f0:8", ["const:695f74:8", "const:4:8"]]
+ 00695f74 ["CALL", null, ["callee:00c53da0:8"]]
- 00695f1c bytes 79f71694
+ 00695f74 bytes 8bf71694
- 00695f38 ["INT_ADD", "register:40f0:8", ["const:695f38:8", "const:4:8"]]
- 00695f38 ["CALL", null, ["callee:00c57f50:8"]]
+ 00695f90 ["INT_ADD", "register:40f0:8", ["const:695f90:8", "const:4:8"]]
+ 00695f90 ["CALL", null, ["callee:00c57f50:8"]]
- 00695f38 bytes d2071794
+ 00695f90 bytes f0071794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0d63cc84c8849292155c00403f3cc6b"></a>

### [`00695f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695f50.md) → [`00695fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695fa8.md) FUN_00695fa8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006959f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/006959f0.md) · 呼出先 5件 [`005d8a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8a6c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a820.md)
- 新版 呼出元 1件 [`00695a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695a48.md) · 呼出先 5件 [`005d8aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8aac.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.10% / 新版 90.10%

CFGの説明率　旧版 71.11% / 新版 69.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695f54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695f54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695f58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00695f54",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00695f58",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00695f5c",
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
      "00695fac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00695fb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00695fb4",
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

- 旧版 [`00695f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695f50.md#insn-00695f54) · [`00695f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695f50.md#insn-00695f58) · [`00695f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695f50.md#insn-00695f5c)

~~~diff
- 00695f54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00695f54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00695f54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00695f54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00695f54 bytes fd7b02a9
- 00695f58 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00695f58 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00695f58 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00695f58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00695f58 bytes fa6703a9
- 00695f5c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00695f5c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00695f5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00695f5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00695f5c bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5399102f18edc3e8a4a0651e53276d42"></a>

### [`00696278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696278.md) → [`006962d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006962d0.md) FUN_006962d0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006962f0",
      "incomplete_value": false,
      "site": "006962f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00696298",
      "incomplete_value": false,
      "site": "0069629c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "006962f4",
      "DATA",
      [
        "storage",
        "00c75080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006962f4",
      "DATA",
      [
        "storage",
        "00c75150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069628c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696278.md#insn-0069628c) · [`00696298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696278.md#insn-00696298)
- 新版 [`006962e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006962d0.md#insn-006962e4) · [`006962f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006962d0.md#insn-006962f0)

~~~diff
- 0069628c ["INT_ADD", "register:40f0:8", ["const:69628c:8", "const:4:8"]]
- 0069628c ["CALL", null, ["callee:00c57f60:8"]]
+ 006962e4 ["INT_ADD", "register:40f0:8", ["const:6962e4:8", "const:4:8"]]
+ 006962e4 ["CALL", null, ["callee:00c57f60:8"]]
- 0069628c bytes 01071794
+ 006962e4 bytes 1f071794
- 00696298 ["COPY", "tmp:0:8", ["const:80:8"]]
- 00696298 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00696298 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00696298 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006962f0 ["COPY", "tmp:0:8", ["const:150:8"]]
+ 006962f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006962f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006962f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00696298 bytes 08010291
+ 006962f0 bytes 08410591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cf9641ccb858aee497d7c5c000273fb"></a>

### [`006962b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006962b0.md) → [`00696308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696308.md) FUN_00696308

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0069630c",
      "incomplete_value": false,
      "site": "00696310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006962b4",
      "incomplete_value": false,
      "site": "006962b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
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
      "00696310",
      "DATA",
      [
        "storage",
        "00c75080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00696310",
      "DATA",
      [
        "storage",
        "00c75150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006962b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006962b0.md#insn-006962b4)
- 新版 [`0069630c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696308.md#insn-0069630c)

~~~diff
- 006962b4 ["COPY", "tmp:0:8", ["const:80:8"]]
- 006962b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006962b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006962b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0069630c ["COPY", "tmp:0:8", ["const:150:8"]]
+ 0069630c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0069630c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0069630c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006962b4 bytes 08010291
+ 0069630c bytes 08410591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3a75b49abbdca2bf4d5d8ebdf0d2163"></a>

### [`006962d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006962d0.md) → [`00696328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696328.md) FUN_00696328

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00688294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00688/00688294.md) [`0068974c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/0068974c.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`006882d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00688/006882d4.md) [`0068978c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/0068978c.md) [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.16% / 新版 95.16%

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
      "site": "0069635c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00696304",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "006963e0",
      "value": [
        "leaf",
        "ram:71bf30:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00696388",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006963f0",
      "value": [
        "leaf",
        "ram:71d254:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00696398",
      "value": [
        "leaf",
        "ram:71d1fc:8"
      ]
    },
    "ordinal": 9,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0069635c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006963e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "006963f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d1fc"
      ]
    ]
  ],
  "added": [
    [
      "0069635c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006963e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "006963f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d254"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00696304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006962d0.md#insn-00696304) · [`00696340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006962d0.md#insn-00696340) · [`00696388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006962d0.md#insn-00696388)
- 新版 [`0069635c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696328.md#insn-0069635c) · [`00696398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696328.md#insn-00696398) · [`006963e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696328.md#insn-006963e0)

~~~diff
- 00696304 ["INT_ADD", "register:40f0:8", ["const:696304:8", "const:4:8"]]
- 00696304 ["CALL", null, ["ram:47acf4:8"]]
+ 0069635c ["INT_ADD", "register:40f0:8", ["const:69635c:8", "const:4:8"]]
+ 0069635c ["CALL", null, ["ram:47ad34:8"]]
- 00696304 bytes 7c92f797
+ 0069635c bytes 7692f797
- 00696340 ["INT_ADD", "register:40f0:8", ["const:696340:8", "const:4:8"]]
- 00696340 ["CALL", null, ["callee:00851550:8"]]
+ 00696398 ["INT_ADD", "register:40f0:8", ["const:696398:8", "const:4:8"]]
+ 00696398 ["CALL", null, ["callee:00851550:8"]]
- 00696340 bytes 6eec0694
+ 00696398 bytes 6eec0694
- 00696388 ["INT_ADD", "register:40f0:8", ["const:696388:8", "const:4:8"]]
- 00696388 ["CALL", null, ["ram:71bed8:8"]]
+ 006963e0 ["INT_ADD", "register:40f0:8", ["const:6963e0:8", "const:4:8"]]
+ 006963e0 ["CALL", null, ["ram:71bf30:8"]]
- 00696388 bytes d4160294
+ 006963e0 bytes d4160294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6305dd4d78cdb31cc38b814dd94730ac"></a>

### [`006963f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006963f4.md) → [`0069644c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/0069644c.md) FUN_0069644c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00696470",
      "incomplete_value": false,
      "site": "00696470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00696418",
      "incomplete_value": false,
      "site": "00696418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:100:8"
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
      "00696470",
      "DATA",
      [
        "storage",
        "00c75100",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00696470",
      "DATA",
      [
        "storage",
        "00c751d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00696408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006963f4.md#insn-00696408) · [`00696414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006963f4.md#insn-00696414)
- 新版 [`00696460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/0069644c.md#insn-00696460) · [`0069646c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/0069644c.md#insn-0069646c)

~~~diff
- 00696408 ["INT_ADD", "register:40f0:8", ["const:696408:8", "const:4:8"]]
- 00696408 ["CALL", null, ["callee:00c57f60:8"]]
+ 00696460 ["INT_ADD", "register:40f0:8", ["const:696460:8", "const:4:8"]]
+ 00696460 ["CALL", null, ["callee:00c57f60:8"]]
- 00696408 bytes a2061794
+ 00696460 bytes c0061794
- 00696414 ["COPY", "tmp:0:8", ["const:100:8"]]
- 00696414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00696414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00696414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0069646c ["COPY", "tmp:0:8", ["const:1d0:8"]]
+ 0069646c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0069646c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0069646c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00696414 bytes 08010491
+ 0069646c bytes 08410791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5229c3808514a54538c1a86479b1d03e"></a>

### [`00696428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696428.md) → [`00696480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696480.md) FUN_00696480

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0069648c",
      "incomplete_value": false,
      "site": "0069648c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00696434",
      "incomplete_value": false,
      "site": "00696434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:100:8"
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
      "0069648c",
      "DATA",
      [
        "storage",
        "00c75100",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069648c",
      "DATA",
      [
        "storage",
        "00c751d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00696430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696428.md#insn-00696430)
- 新版 [`00696488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696480.md#insn-00696488)

~~~diff
- 00696430 ["COPY", "tmp:0:8", ["const:100:8"]]
- 00696430 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00696430 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00696430 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00696488 ["COPY", "tmp:0:8", ["const:1d0:8"]]
+ 00696488 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00696488 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00696488 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00696430 bytes 29010491
+ 00696488 bytes 29410791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-444a7782d6700a2994c604b7ad394db7"></a>

### [`00696444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696444.md) → [`0069649c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/0069649c.md) FUN_0069649c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0068f5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068f/0068f5d8.md) [`00690ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00690/00690ea0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068f630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md) [`00690ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690ef8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 54.55% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00696478"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00696500",
      "incomplete_value": true,
      "site": "00696504",
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
            "const:3078:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006964a8",
      "incomplete_value": true,
      "site": "006964ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "live",
            "register:40a8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "006964d0"
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
      "unmatched:00696478",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "006964d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00696478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696444.md#insn-00696478) · [`006964ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696444.md#insn-006964ac)
- 新版 [`00696504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/0069649c.md#insn-00696504) · [`006964d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/0069649c.md#insn-006964d0)

~~~diff
- 00696478 ["INT_ADD", "register:40f0:8", ["const:696478:8", "const:4:8"]]
- 00696478 ["CALL", null, ["ram:47acf4:8"]]
- 00696478 bytes 1f92f797
- 006964ac ["INT_ADD", "register:40f0:8", ["const:6964ac:8", "const:4:8"]]
- 006964ac ["CALL", null, ["callee:00a832d0:8"]]
+ 00696504 ["INT_ADD", "register:40f0:8", ["const:696504:8", "const:4:8"]]
+ 00696504 ["CALL", null, ["callee:00a832d0:8"]]
- 006964ac bytes 6db30f94
+ 00696504 bytes 73b30f94
+ 006964d0 ["INT_ADD", "register:40f0:8", ["const:6964d0:8", "const:4:8"]]
+ 006964d0 ["CALL", null, ["ram:47ad34:8"]]
+ 006964d0 bytes 1992f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b2a579e6738a1b34fff84432ca01900"></a>

### [`00696530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696530.md) → [`00696588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696588.md) FUN_00696588

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "006965ac",
      "incomplete_value": false,
      "site": "006965ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00696554",
      "incomplete_value": false,
      "site": "00696554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:180:8"
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
      "006965ac",
      "DATA",
      [
        "storage",
        "00c75180",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006965ac",
      "DATA",
      [
        "storage",
        "00c75250",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00696544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696530.md#insn-00696544) · [`00696550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696530.md#insn-00696550)
- 新版 [`0069659c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696588.md#insn-0069659c) · [`006965a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696588.md#insn-006965a8)

~~~diff
- 00696544 ["INT_ADD", "register:40f0:8", ["const:696544:8", "const:4:8"]]
- 00696544 ["CALL", null, ["callee:00c57f60:8"]]
+ 0069659c ["INT_ADD", "register:40f0:8", ["const:69659c:8", "const:4:8"]]
+ 0069659c ["CALL", null, ["callee:00c57f60:8"]]
- 00696544 bytes 53061794
+ 0069659c bytes 71061794
- 00696550 ["COPY", "tmp:0:8", ["const:180:8"]]
- 00696550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00696550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00696550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006965a8 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 006965a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006965a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006965a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00696550 bytes 08010691
+ 006965a8 bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad189c3a31dcccea5dbd57c0924542cd"></a>

### [`00696564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696564.md) → [`006965bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006965bc.md) FUN_006965bc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006965c8",
      "incomplete_value": false,
      "site": "006965c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00696570",
      "incomplete_value": false,
      "site": "00696570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:180:8"
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
      "006965c8",
      "DATA",
      [
        "storage",
        "00c75180",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006965c8",
      "DATA",
      [
        "storage",
        "00c75250",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069656c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696564.md#insn-0069656c)
- 新版 [`006965c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006965bc.md#insn-006965c4)

~~~diff
- 0069656c ["COPY", "tmp:0:8", ["const:180:8"]]
- 0069656c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0069656c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0069656c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006965c4 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 006965c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006965c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006965c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0069656c bytes 29010691
+ 006965c4 bytes 29410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-003e202500901283bd3cad33e3715989"></a>

### [`00696580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696580.md) → [`006965d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006965d8.md) FUN_006965d8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0085b2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2e0.md) [`008b9298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9298.md) [`008b9500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9500.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0085b338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b338.md) [`008b92f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92f0.md) [`008b9558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b9558.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 40.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00696658",
      "incomplete_value": true,
      "site": "0069665c",
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
                "const:120:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00696600",
      "incomplete_value": true,
      "site": "00696604",
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
                "const:e0:8"
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
    "new": null,
    "old": {
      "definition_site": "00696654",
      "incomplete_value": true,
      "site": "0069665c",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00696654",
      "incomplete_value": true,
      "site": "0069665c",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006965b8",
      "DATA",
      [
        "storage",
        "00338758",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "00696658",
      "READ",
      [
        "storage",
        "002c40e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00696610",
      "DATA",
      [
        "storage",
        "00338758",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "00696658",
      "READ",
      [
        "storage",
        "002c4120",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069665c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696580.md#insn-0069665c) · [`006965b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696580.md#insn-006965b4) · [`006965b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696580.md#insn-006965b8)
- 新版 [`006966b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006965d8.md#insn-006966b4)

~~~diff
- 0069665c ["INT_ADD", "register:40f0:8", ["const:69665c:8", "const:4:8"]]
- 0069665c ["CALL", null, ["callee:008b9558:8"]]
+ 006966b4 ["INT_ADD", "register:40f0:8", ["const:6966b4:8", "const:4:8"]]
+ 006966b4 ["CALL", null, ["callee:008b9558:8"]]
- 0069665c bytes a98b0894
+ 006966b4 bytes a98b0894
- 006965b4 ["INT_LEFT", "tmp:0:8", ["const:338:8", "const:c:4"]]
- 006965b4 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 006965b4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:1:8"]]
- 006965b4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:1:8"]]
- 006965b4 bytes 96e24c91
- 006965b8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:758:8"]]
- 006965b8 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 006965b8 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 006965b8 bytes c85a47b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-991fbd14b5d0493f8cacc03e3f9c34d8"></a>

### [`006966b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006966b8.md) → [`00696710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696710.md) FUN_00696710

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00696730",
      "incomplete_value": false,
      "site": "00696734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006966d8",
      "incomplete_value": false,
      "site": "006966dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:200:8"
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
      "00696734",
      "DATA",
      [
        "storage",
        "00c75200",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00696734",
      "DATA",
      [
        "storage",
        "00c752d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006966cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006966b8.md#insn-006966cc) · [`006966d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006966b8.md#insn-006966d8)
- 新版 [`00696724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696710.md#insn-00696724) · [`00696730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696710.md#insn-00696730)

~~~diff
- 006966cc ["INT_ADD", "register:40f0:8", ["const:6966cc:8", "const:4:8"]]
- 006966cc ["CALL", null, ["callee:00c57f60:8"]]
+ 00696724 ["INT_ADD", "register:40f0:8", ["const:696724:8", "const:4:8"]]
+ 00696724 ["CALL", null, ["callee:00c57f60:8"]]
- 006966cc bytes f1051794
+ 00696724 bytes 0f061794
- 006966d8 ["COPY", "tmp:0:8", ["const:200:8"]]
- 006966d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006966d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006966d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00696730 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 00696730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00696730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00696730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006966d8 bytes 08010891
+ 00696730 bytes 08410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fbc01757fcb42f4a874142227ded13d"></a>

### [`006966f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006966f0.md) → [`00696748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696748.md) FUN_00696748

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0069674c",
      "incomplete_value": false,
      "site": "00696750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006966f4",
      "incomplete_value": false,
      "site": "006966f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:200:8"
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
      "00696750",
      "DATA",
      [
        "storage",
        "00c75200",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00696750",
      "DATA",
      [
        "storage",
        "00c752d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006966f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/006966f0.md#insn-006966f4)
- 新版 [`0069674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696748.md#insn-0069674c)

~~~diff
- 006966f4 ["COPY", "tmp:0:8", ["const:200:8"]]
- 006966f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006966f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006966f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0069674c ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 0069674c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0069674c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0069674c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006966f4 bytes 08010891
+ 0069674c bytes 08410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a55b962a73a4a3058f53390fedc387b7"></a>

### [`00696710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696710.md) → [`00696768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696768.md) FUN_00696768

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 21件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md)
- 新版 呼出元 0件  · 呼出先 21件 [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.93% / 新版 90.93%

CFGの説明率　旧版 22.67% / 新版 23.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00696c88"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00696d48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00696ce0"
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
      "unmatched:006967dc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0069683c"
      ]
    ],
    [
      "0069683c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:006967ec",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00696834",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0069683c"
      ]
    ],
    [
      "0069683c",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00696844",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006967fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696710.md#insn-006967fc) · [`0069680c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696710.md#insn-0069680c)
- 新版 [`00696854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696768.md#insn-00696854) · [`00696864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696768.md#insn-00696864)

~~~diff
- 006967fc ["INT_ADD", "register:40f0:8", ["const:6967fc:8", "const:4:8"]]
- 006967fc ["CALL", null, ["callee:00c586e0:8"]]
+ 00696854 ["INT_ADD", "register:40f0:8", ["const:696854:8", "const:4:8"]]
+ 00696854 ["CALL", null, ["callee:00c586e0:8"]]
- 006967fc bytes 85071794
+ 00696854 bytes a3071794
- 0069680c ["INT_ADD", "register:40f0:8", ["const:69680c:8", "const:4:8"]]
- 0069680c ["CALL", null, ["callee:00695a48:8"]]
- 0069680c bytes 79fcff97
+ 00696864 ["INT_ADD", "register:40f0:8", ["const:696864:8", "const:4:8"]]
+ 00696864 ["CALL", null, ["callee:00695a48:8"]]
+ 00696864 bytes 79fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97a9a665db8be41968c02e7193dc76dd"></a>

### [`00696e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696e04.md) → [`00696e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e5c.md) FUN_00696e5c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00696e60",
      "incomplete_value": false,
      "site": "00696e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00696e08",
      "incomplete_value": false,
      "site": "00696e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:280:8"
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
      "00696e64",
      "DATA",
      [
        "storage",
        "00c75280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00696e64",
      "DATA",
      [
        "storage",
        "00c75350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00696e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696e04.md#insn-00696e08)
- 新版 [`00696e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e5c.md#insn-00696e60)

~~~diff
- 00696e08 ["COPY", "tmp:0:8", ["const:280:8"]]
- 00696e08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00696e08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00696e08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00696e60 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 00696e60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00696e60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00696e60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00696e08 bytes 08010a91
+ 00696e60 bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c5231903388f3582ca7e9246839b8dc"></a>

### [`00696e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696e24.md) → [`00696e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e7c.md) FUN_00696e7c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 16件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0068ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068ed80.md) [`006906e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00690/006906e8.md) [`00697168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697168.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068edd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068edd8.md) [`00690740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690740.md) [`006971c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006971c0.md)

変更の種類 call, call_argument_candidate, call_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 54.29% / 新版 54.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_value` 3件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00696e44"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0069700c",
      "incomplete_value": false,
      "site": "00697014",
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
            "const:e26:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00696fb4",
      "incomplete_value": false,
      "site": "00696fbc",
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
            "const:df7:8"
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
      "definition_site": "00697034",
      "incomplete_value": false,
      "site": "00697040",
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
            "const:eb5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00696fdc",
      "incomplete_value": false,
      "site": "00696fe8",
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
            "const:f11:8"
          ]
        ]
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
      "unmatched:00696e44",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00696e58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00696ef8"
      ]
    ],
    [
      "unmatched:00696e60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00696ef8"
      ]
    ]
  ],
  "added": [
    [
      "00696e9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00696eb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00696ef8"
      ]
    ],
    [
      "00696eb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00696ef8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00696e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696e24.md#insn-00696e44) · [`00696e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696e24.md#insn-00696e58) · [`00696e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696e24.md#insn-00696e60)

~~~diff
- 00696e44 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00696e44 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00696e44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00696e44 bytes a8831ff8
- 00696e58 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00696e58 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00696e58 bytes 41020054
- 00696e60 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00696e60 bytes 00020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15efb7084143be24bce75debb34faf08"></a>

### [`0069740c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/0069740c.md) → [`00697464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697464.md) FUN_00697464

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f48.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa0.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 branch_condition_or_target, call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 63.64% / 新版 63.64%

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
      "site": "0069749c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00697444",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "006974b4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0069745c",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0069749c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006974b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0069749c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006974b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/0069740c.md#insn-00697444) · [`0069745c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/0069740c.md#insn-0069745c) · [`00697428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/0069740c.md#insn-00697428)
- 新版 [`0069749c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697464.md#insn-0069749c) · [`006974b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697464.md#insn-006974b4) · [`00697480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697464.md#insn-00697480)

~~~diff
- 00697444 ["INT_ADD", "register:40f0:8", ["const:697444:8", "const:4:8"]]
- 00697444 ["CALL", null, ["ram:47acf4:8"]]
+ 0069749c ["INT_ADD", "register:40f0:8", ["const:69749c:8", "const:4:8"]]
+ 0069749c ["CALL", null, ["ram:47ad34:8"]]
- 00697444 bytes 2c8ef797
+ 0069749c bytes 268ef797
- 0069745c ["INT_ADD", "register:40f0:8", ["const:69745c:8", "const:4:8"]]
- 0069745c ["CALL", null, ["ram:47acf4:8"]]
+ 006974b4 ["INT_ADD", "register:40f0:8", ["const:6974b4:8", "const:4:8"]]
+ 006974b4 ["CALL", null, ["ram:47ad34:8"]]
- 0069745c bytes 268ef797
+ 006974b4 bytes 208ef797
- 00697428 ["INT_ADD", "register:40f0:8", ["const:697428:8", "const:4:8"]]
- 00697428 ["CALL", null, ["callee:008b6fa0:8"]]
+ 00697480 ["INT_ADD", "register:40f0:8", ["const:697480:8", "const:4:8"]]
+ 00697480 ["CALL", null, ["callee:008b6fa0:8"]]
- 00697428 bytes c87e0894
+ 00697480 bytes c87e0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-706b35a9cba23ae210ef71011531a3f6"></a>

### [`006974b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006974b0.md) → [`00697508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697508.md) FUN_00697508

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00697528",
      "incomplete_value": false,
      "site": "0069752c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006974d0",
      "incomplete_value": false,
      "site": "006974d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:380:8"
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
      "0069752c",
      "DATA",
      [
        "storage",
        "00c75380",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069752c",
      "DATA",
      [
        "storage",
        "00c75450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006974c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006974b0.md#insn-006974c4) · [`006974d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006974b0.md#insn-006974d0)
- 新版 [`0069751c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697508.md#insn-0069751c) · [`00697528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697508.md#insn-00697528)

~~~diff
- 006974c4 ["INT_ADD", "register:40f0:8", ["const:6974c4:8", "const:4:8"]]
- 006974c4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0069751c ["INT_ADD", "register:40f0:8", ["const:69751c:8", "const:4:8"]]
+ 0069751c ["CALL", null, ["callee:00c57f60:8"]]
- 006974c4 bytes 73021794
+ 0069751c bytes 91021794
- 006974d0 ["COPY", "tmp:0:8", ["const:380:8"]]
- 006974d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006974d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006974d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00697528 ["COPY", "tmp:0:8", ["const:450:8"]]
+ 00697528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00697528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00697528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006974d0 bytes 08010e91
+ 00697528 bytes 08411191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f427d8beee25149b2bc1d63180df458"></a>

### [`006974e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006974e8.md) → [`00697540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697540.md) FUN_00697540

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00697544",
      "incomplete_value": false,
      "site": "00697548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006974ec",
      "incomplete_value": false,
      "site": "006974f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:380:8"
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
      "00697548",
      "DATA",
      [
        "storage",
        "00c75380",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697548",
      "DATA",
      [
        "storage",
        "00c75450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006974ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006974e8.md#insn-006974ec)
- 新版 [`00697544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697540.md#insn-00697544)

~~~diff
- 006974ec ["COPY", "tmp:0:8", ["const:380:8"]]
- 006974ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006974ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006974ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00697544 ["COPY", "tmp:0:8", ["const:450:8"]]
+ 00697544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00697544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00697544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006974ec bytes 08010e91
+ 00697544 bytes 08411191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-356164ea8d93016c59012fda3edd933f"></a>

### [`00697508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697508.md) → [`00697560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697560.md) FUN_00697560

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f48.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

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
      "site": "00697598",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00697540",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "006975a4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0069754c",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00697598",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006975a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00697598",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006975a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697508.md#insn-00697540) · [`0069754c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697508.md#insn-0069754c) · [`00697524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697508.md#insn-00697524)
- 新版 [`00697598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697560.md#insn-00697598) · [`006975a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697560.md#insn-006975a4) · [`0069757c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697560.md#insn-0069757c)

~~~diff
- 00697540 ["INT_ADD", "register:40f0:8", ["const:697540:8", "const:4:8"]]
- 00697540 ["CALL", null, ["ram:47acf4:8"]]
+ 00697598 ["INT_ADD", "register:40f0:8", ["const:697598:8", "const:4:8"]]
+ 00697598 ["CALL", null, ["ram:47ad34:8"]]
- 00697540 bytes ed8df797
+ 00697598 bytes e78df797
- 0069754c ["INT_ADD", "register:40f0:8", ["const:69754c:8", "const:4:8"]]
- 0069754c ["CALL", null, ["ram:47acf4:8"]]
+ 006975a4 ["INT_ADD", "register:40f0:8", ["const:6975a4:8", "const:4:8"]]
+ 006975a4 ["CALL", null, ["ram:47ad34:8"]]
- 0069754c bytes ea8df797
+ 006975a4 bytes e48df797
- 00697524 ["INT_ADD", "register:40f0:8", ["const:697524:8", "const:4:8"]]
- 00697524 ["CALL", null, ["callee:008b6fa0:8"]]
+ 0069757c ["INT_ADD", "register:40f0:8", ["const:69757c:8", "const:4:8"]]
+ 0069757c ["CALL", null, ["callee:008b6fa0:8"]]
- 00697524 bytes 897e0894
+ 0069757c bytes 897e0894
~~~


<a id="compare-b349f7e2a7403347d855ff6afdeebff1"></a>

### [`006975a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006975a8.md) → [`00697600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697600.md) FUN_00697600

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0069760c",
      "incomplete_value": false,
      "site": "00697610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006975b4",
      "incomplete_value": false,
      "site": "006975b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "00697610",
      "DATA",
      [
        "storage",
        "00c75400",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697610",
      "DATA",
      [
        "storage",
        "00c754d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006975b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006975a8.md#insn-006975b4)
- 新版 [`0069760c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697600.md#insn-0069760c)

~~~diff
- 006975b4 ["COPY", "tmp:0:8", ["const:400:8"]]
- 006975b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006975b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006975b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0069760c ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 0069760c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0069760c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0069760c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006975b4 bytes 29011091
+ 0069760c bytes 29411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-672a7ba596877006720a9ff1a6f6c84e"></a>

### [`006975cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006975cc.md) → [`00697624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697624.md) FUN_00697624

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0069762c",
      "incomplete_value": false,
      "site": "00697630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006975d4",
      "incomplete_value": false,
      "site": "006975d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "00697630",
      "DATA",
      [
        "storage",
        "00c75400",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697630",
      "DATA",
      [
        "storage",
        "00c754d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006975d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006975cc.md#insn-006975d4) · [`006975f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006975cc.md#insn-006975f8)
- 新版 [`0069762c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697624.md#insn-0069762c) · [`00697650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697624.md#insn-00697650)

~~~diff
- 006975d4 ["COPY", "tmp:0:8", ["const:400:8"]]
- 006975d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006975d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006975d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0069762c ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 0069762c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0069762c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0069762c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006975d4 bytes 29011091
+ 0069762c bytes 29411391
- 006975f8 ["INT_ADD", "register:40f0:8", ["const:6975f8:8", "const:4:8"]]
- 006975f8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00697650 ["INT_ADD", "register:40f0:8", ["const:697650:8", "const:4:8"]]
+ 00697650 ["CALL", null, ["callee:00c57f80:8"]]
- 006975f8 bytes 2e021794
+ 00697650 bytes 4c021794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63524ad525687e165db2c8bd51db55ac"></a>

### [`0069760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/0069760c.md) → [`00697664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697664.md) FUN_00697664

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`006924c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924c4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00697684",
      "incomplete_value": false,
      "site": "0069768c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0069762c",
      "incomplete_value": false,
      "site": "00697634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "0069768c",
      "DATA",
      [
        "storage",
        "00c75400",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069768c",
      "DATA",
      [
        "storage",
        "00c754d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/0069760c.md#insn-00697624) · [`0069762c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/0069760c.md#insn-0069762c) · [`00697660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/0069760c.md#insn-00697660)
- 新版 [`0069767c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697664.md#insn-0069767c) · [`00697684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697664.md#insn-00697684) · [`006976b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697664.md#insn-006976b8)

~~~diff
- 00697624 ["INT_ADD", "register:40f0:8", ["const:697624:8", "const:4:8"]]
- 00697624 ["CALL", null, ["callee:00c57f60:8"]]
+ 0069767c ["INT_ADD", "register:40f0:8", ["const:69767c:8", "const:4:8"]]
+ 0069767c ["CALL", null, ["callee:00c57f60:8"]]
- 00697624 bytes 1b021794
+ 0069767c bytes 39021794
- 0069762c ["COPY", "tmp:0:8", ["const:400:8"]]
- 0069762c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0069762c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0069762c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00697684 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 00697684 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00697684 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00697684 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0069762c bytes 08011091
+ 00697684 bytes 08411391
- 00697660 ["INT_ADD", "register:40f0:8", ["const:697660:8", "const:4:8"]]
- 00697660 ["CALL", null, ["callee:00c57f60:8"]]
+ 006976b8 ["INT_ADD", "register:40f0:8", ["const:6976b8:8", "const:4:8"]]
+ 006976b8 ["CALL", null, ["callee:00c57f60:8"]]
- 00697660 bytes 0c021794
+ 006976b8 bytes 2a021794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9eb8a4bc8840cc2ead5dab9d22d6111"></a>

### [`006976c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006976c4.md) → [`0069771c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/0069771c.md) FUN_0069771c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`006924c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924c4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00697730",
      "incomplete_value": false,
      "site": "00697738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006976d8",
      "incomplete_value": false,
      "site": "006976e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "00697738",
      "DATA",
      [
        "storage",
        "00c75400",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697738",
      "DATA",
      [
        "storage",
        "00c754d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006976d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006976c4.md#insn-006976d8) · [`0069770c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006976c4.md#insn-0069770c) · [`00697724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006976c4.md#insn-00697724)
- 新版 [`00697730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/0069771c.md#insn-00697730) · [`00697764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/0069771c.md#insn-00697764) · [`0069777c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/0069771c.md#insn-0069777c)

~~~diff
- 006976d8 ["COPY", "tmp:0:8", ["const:400:8"]]
- 006976d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006976d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006976d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00697730 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 00697730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00697730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00697730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006976d8 bytes 08011091
+ 00697730 bytes 08411391
- 0069770c ["INT_ADD", "register:40f0:8", ["const:69770c:8", "const:4:8"]]
- 0069770c ["CALL", null, ["callee:00c57f60:8"]]
+ 00697764 ["INT_ADD", "register:40f0:8", ["const:697764:8", "const:4:8"]]
+ 00697764 ["CALL", null, ["callee:00c57f60:8"]]
- 0069770c bytes e1011794
+ 00697764 bytes ff011794
- 00697724 ["INT_ADD", "register:40f0:8", ["const:697724:8", "const:4:8"]]
- 00697724 ["CALL", null, ["callee:00c580d0:8"]]
+ 0069777c ["INT_ADD", "register:40f0:8", ["const:69777c:8", "const:4:8"]]
+ 0069777c ["CALL", null, ["callee:00c580d0:8"]]
- 00697724 bytes 37021794
+ 0069777c bytes 55021794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-672b9d890d805ab1f30c9e75d9bfe018"></a>

### [`0069777c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/0069777c.md) → [`006977d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006977d4.md) FUN_006977d4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0068f5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068f/0068f5d8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0068f630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00697780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/0069777c.md#insn-00697780) · [`0069779c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/0069777c.md#insn-0069779c)
- 新版 [`006977d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006977d4.md#insn-006977d8) · [`006977f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006977d4.md#insn-006977f4)

~~~diff
- 00697780 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00697780 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 006977d8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 006977d8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00697780 bytes 680100b4
+ 006977d8 bytes 680100b4
- 0069779c ["INT_ADD", "register:40f0:8", ["const:69779c:8", "const:4:8"]]
- 0069779c ["CALL", null, ["callee:00c57f80:8"]]
+ 006977f4 ["INT_ADD", "register:40f0:8", ["const:6977f4:8", "const:4:8"]]
+ 006977f4 ["CALL", null, ["callee:00c57f80:8"]]
- 0069779c bytes c5011794
+ 006977f4 bytes e3011794
~~~


<a id="compare-3c4c574a514718edd339a81f66f7216d"></a>

### [`006977b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006977b0.md) → [`00697808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697808.md) FUN_00697808

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 24件 [`00684fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684fb0.md) [`00685374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685374.md) [`00691e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691e2c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085b2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2a4.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00684ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684ff0.md) [`006853b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/006853b4.md) [`00691e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085b2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b2fc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.94% / 新版 85.94%

CFGの説明率　旧版 30.00% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `store_condition` 10件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006977b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006977b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006977b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006977b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:006977b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:006977bc",
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
      "0069780c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00697810",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00697814",
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

- 旧版 [`006977b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006977b0.md#insn-006977b4) · [`006977b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006977b0.md#insn-006977b8) · [`006977bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006977b0.md#insn-006977bc)

~~~diff
- 006977b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006977b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006977b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 006977b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006977b4 bytes fd7b0ca9
- 006977b8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 006977b8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 006977b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 006977b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006977b8 bytes fc6f0da9
- 006977bc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 006977bc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 006977bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 006977bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006977bc bytes fa670ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d7790fe79dcf9b85c06236e667dac84"></a>

### [`00697e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697e20.md) → [`00697e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e78.md) FUN_00697e78

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`006924c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924c4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00697e98",
      "incomplete_value": false,
      "site": "00697ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00697e40",
      "incomplete_value": false,
      "site": "00697e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "00697ea0",
      "DATA",
      [
        "storage",
        "00c75480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697ea0",
      "DATA",
      [
        "storage",
        "00c75550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697e20.md#insn-00697e38) · [`00697e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697e20.md#insn-00697e40) · [`00697e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697e20.md#insn-00697e7c)
- 新版 [`00697e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e78.md#insn-00697e90) · [`00697e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e78.md#insn-00697e98) · [`00697ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e78.md#insn-00697ed4)

~~~diff
- 00697e38 ["INT_ADD", "register:40f0:8", ["const:697e38:8", "const:4:8"]]
- 00697e38 ["CALL", null, ["callee:00c57f60:8"]]
+ 00697e90 ["INT_ADD", "register:40f0:8", ["const:697e90:8", "const:4:8"]]
+ 00697e90 ["CALL", null, ["callee:00c57f60:8"]]
- 00697e38 bytes 16001794
+ 00697e90 bytes 34001794
- 00697e40 ["COPY", "tmp:0:8", ["const:480:8"]]
- 00697e40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00697e40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00697e40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00697e98 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00697e98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00697e98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00697e98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00697e40 bytes 08011291
+ 00697e98 bytes 08411591
- 00697e7c ["INT_ADD", "register:40f0:8", ["const:697e7c:8", "const:4:8"]]
- 00697e7c ["CALL", null, ["callee:00c57f60:8"]]
+ 00697ed4 ["INT_ADD", "register:40f0:8", ["const:697ed4:8", "const:4:8"]]
+ 00697ed4 ["CALL", null, ["callee:00c57f60:8"]]
- 00697e7c bytes 05001794
+ 00697ed4 bytes 23001794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2342cd5919c047eaa338ac6d394cb10"></a>

### [`00697ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697ee0.md) → [`00697f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697f38.md) FUN_00697f38

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`006924c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924c4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.90% / 新版 61.90%

CFGの説明率　旧版 16.67% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00697ee0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00697ee0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00697ee4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00697ee0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00697ee4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00697ee8",
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
      "00697f38",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00697f3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00697f40",
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

- 旧版 [`00697ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697ee0.md#insn-00697ee0) · [`00697ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697ee0.md#insn-00697ee4) · [`00697ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697ee0.md#insn-00697ee8)

~~~diff
- 00697ee0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00697ee0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00697ee0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00697ee0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00697ee0 bytes fd7bbda9
- 00697ee4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00697ee4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00697ee4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00697ee4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00697ee4 bytes f65701a9
- 00697ee8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00697ee8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00697ee8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00697ee8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00697ee8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28b912545afabe2e5fe21d81a4f6d4e5"></a>

### [`00697f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697f88.md) → [`00697fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697fe0.md) FUN_00697fe0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00697f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697f88.md#insn-00697f90)
- 新版 [`00697fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697fe0.md#insn-00697fe8)

~~~diff
- 00697f90 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00697f90 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00697fe8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00697fe8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00697f90 bytes 600000b4
+ 00697fe8 bytes 600000b4
~~~


