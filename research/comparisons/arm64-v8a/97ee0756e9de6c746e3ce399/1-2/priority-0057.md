# v15.7.3 → v15.7.4 · 最優先の変更候補 (57)

[一覧の目次](README.md)

<a id="compare-bf30246c0ae09a26f728d662bce8dac7"></a>

### [`00a8ac58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8a/00a8ac58.md) → [`00a8ac9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8a/00a8ac9c.md) FUN_00a8ac9c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00a82394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a82/00a82394.md) [`00a8f8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f8b4.md) [`00a905d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a905d4.md) · 呼出先 10件 [`0059be80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059b/0059be80.md) [`00719de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00719/00719de8.md) [`00719eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00719/00719eac.md) [`0071a054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a054.md) [`0071a0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a0c4.md)
- 新版 呼出元 3件 [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) [`00a8f8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f8f8.md) [`00a90618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90618.md) · 呼出先 10件 [`0059be80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059b/0059be80.md) [`00719de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00719/00719de8.md) [`00719eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00719/00719eac.md) [`0071a054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a054.md) [`0071a0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a0c4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.79% / 新版 80.79%

CFGの説明率　旧版 4.08% / 新版 4.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `return_value_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8ac80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8acf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a8acc4"
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
      "unmatched:00a8ac80",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a8ac98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a8ace8"
      ]
    ],
    [
      "unmatched:00a8acf8",
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
      "00a8acc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00a8acdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a8ace8"
      ]
    ],
    [
      "00a8ad3c",
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

- 旧版 [`00a8ac80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8a/00a8ac58.md#insn-00a8ac80) · [`00a8ac98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8a/00a8ac58.md#insn-00a8ac98) · [`00a8acc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8a/00a8ac58.md#insn-00a8acc0)
- 新版 `00a8ad04`（命令位置の公開資料なし）

~~~diff
- 00a8ac80 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00a8ac80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
- 00a8ac80 bytes e10b00b9
- 00a8ac98 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a8ac98 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00a8ac98 bytes 61000054
- 00a8acc0 ["INT_ADD", "register:40f0:8", ["const:a8acc0:8", "const:4:8"]]
- 00a8acc0 ["CALL", null, ["callee:009e4f3c:8"]]
+ 00a8ad04 ["INT_ADD", "register:40f0:8", ["const:a8ad04:8", "const:4:8"]]
+ 00a8ad04 ["CALL", null, ["callee:009e4f3c:8"]]
- 00a8acc0 bytes 8e68fd97
+ 00a8ad04 bytes 8e68fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60f9b72718cab626a4a4df11c9d921b2"></a>

### [`00a8b028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b028.md) → [`00a8b06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8b/00a8b06c.md) FUN_00a8b06c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a82394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a82/00a82394.md) [`00a914b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a914b8.md) · 呼出先 21件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md)
- 新版 呼出元 2件 [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) [`00a914fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a914fc.md) · 呼出先 21件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 74.86% / 新版 74.86%

CFGの説明率　旧版 33.90% / 新版 32.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 10件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a8b0a0",
      "incomplete_value": true,
      "site": "00a8b0a0",
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
      "definition_site": "00a8b05c",
      "incomplete_value": true,
      "site": "00a8b05c",
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
      "site": "00a8b1d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8b274"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a8b094",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8b0a8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8b0b0",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a8b094",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8b0a8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8b0b0",
      "PARAM",
      [
        "storage",
        "00c0df30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8b074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b028.md#insn-00a8b074) · [`00a8b0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b028.md#insn-00a8b0b8) · [`00a8b1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b028.md#insn-00a8b1b0)
- 新版 `00a8b0b8`（命令位置の公開資料なし） · `00a8b1f4`（命令位置の公開資料なし）

~~~diff
- 00a8b074 ["INT_ADD", "register:40f0:8", ["const:a8b074:8", "const:4:8"]]
- 00a8b074 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00a8b0b8 ["INT_ADD", "register:40f0:8", ["const:a8b0b8:8", "const:4:8"]]
+ 00a8b0b8 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00a8b074 bytes bf410594
+ 00a8b0b8 bytes c2410594
- 00a8b0b8 ["INT_SEXT", "tmp:0:8", ["register:4040:4"]]
- 00a8b0b8 ["INT_SEXT", "tmp:1:8", ["register:4050:4"]]
- 00a8b0b8 ["INT_MULT", "tmp:2:8", ["tmp:0:8", "tmp:1:8"]]
- 00a8b0b8 ["INT_ADD", "register:4040:8", ["register:40d8:8", "tmp:2:8"]]
- 00a8b0b8 bytes 086d2a9b
- 00a8b1b0 ["INT_ADD", "register:40f0:8", ["const:a8b1b0:8", "const:4:8"]]
- 00a8b1b0 ["CALL", null, ["callee:00446d2c:8"]]
+ 00a8b1f4 ["INT_ADD", "register:40f0:8", ["const:a8b1f4:8", "const:4:8"]]
+ 00a8b1f4 ["CALL", null, ["callee:00446d2c:8"]]
- 00a8b1b0 bytes dfeee697
+ 00a8b1f4 bytes ceeee697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9d1a235d5031d1e1fc3698527e077ef"></a>

### [`00a8b5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b5a0.md) → [`00a8b5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8b/00a8b5e4.md) FUN_00a8b5e4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`007c80a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c80a0.md) [`00963004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00963/00963004.md) [`00a82394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a82/00a82394.md) · 呼出先 8件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md)
- 新版 呼出元 3件 [`007c80a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c80a0.md) [`00963004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00963/00963004.md) [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) · 呼出先 8件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a8b604",
      "incomplete_value": true,
      "site": "00a8b60c",
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
            "register:40b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8b5c0",
      "incomplete_value": true,
      "site": "00a8b5c8",
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
            "const:2f88:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a8b5c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b5a0.md#insn-00a8b5c8) · [`00a8b5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b5a0.md#insn-00a8b5c0) · [`00a8b5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b5a0.md#insn-00a8b5d0)
- 新版 `00a8b60c`（命令位置の公開資料なし） · `00a8b614`（命令位置の公開資料なし）

~~~diff
- 00a8b5c8 ["INT_ADD", "register:40f0:8", ["const:a8b5c8:8", "const:4:8"]]
- 00a8b5c8 ["CALL", null, ["callee:00a24948:8"]]
+ 00a8b60c ["INT_ADD", "register:40f0:8", ["const:a8b60c:8", "const:4:8"]]
+ 00a8b60c ["CALL", null, ["callee:00a24948:8"]]
- 00a8b5c8 bytes cf64fe97
+ 00a8b60c bytes cf64fe97
- 00a8b5c0 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00a8b5c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a8b5c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a8b5c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a8b5c0 bytes 0000178b
- 00a8b5d0 ["INT_ADD", "register:40f0:8", ["const:a8b5d0:8", "const:4:8"]]
- 00a8b5d0 ["CALL", null, ["callee:00444988:8"]]
+ 00a8b614 ["INT_ADD", "register:40f0:8", ["const:a8b614:8", "const:4:8"]]
+ 00a8b614 ["CALL", null, ["callee:00444988:8"]]
- 00a8b5d0 bytes eee4e697
+ 00a8b614 bytes dde4e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08553ba556ab4f22da89295821c812f7"></a>

### [`00a8b6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b6f4.md) → [`00a8b738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8b/00a8b738.md) FUN_00a8b738

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00a70a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a70/00a70a80.md) [`00a70c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a70/00a70c4c.md) [`00a70fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a70/00a70fe4.md) · 呼出先 6件 [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 3件 [`00a70ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a70/00a70ac4.md) [`00a70c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a70/00a70c90.md) [`00a71028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a71/00a71028.md) · 呼出先 6件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 87.88% / 新版 93.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8b71c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a8b760"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8b730"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a8b71c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a8b730",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a8b844"
      ]
    ]
  ],
  "added": [
    [
      "00a8b760",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a8b774",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a8b844"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8b71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b6f4.md#insn-00a8b71c) · [`00a8b730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b6f4.md#insn-00a8b730)
- 新版 `00a8b760`（命令位置の公開資料なし）

~~~diff
- 00a8b71c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a8b71c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a8b71c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a8b71c bytes a8831ff8
- 00a8b730 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 00a8b730 bytes 80060054
+ 00a8b760 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a8b760 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 00a8b760 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00a8b760 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ce59b69376675d48ce251407288fba9"></a>

### [`00a8b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b898.md) → [`00a8b8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8b/00a8b8dc.md) FUN_00a8b8dc

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0063c0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c0d4.md) [`0063c178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c178.md)
- 新版 呼出元 2件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0063c0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c0d4.md) [`0063c178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c178.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.01% / 新版 92.01%

CFGの説明率　旧版 48.61% / 新版 49.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8b948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8bedc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8c024"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a8b948",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a8bb50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a8bd24"
      ]
    ],
    [
      "unmatched:00a8bb74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a8be98"
      ]
    ]
  ],
  "added": [
    [
      "00a8b98c",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ],
    [
      "00a8bb94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a8bd24"
      ]
    ],
    [
      "00a8bbb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a8be98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8b948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b898.md#insn-00a8b948) · [`00a8bb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b898.md#insn-00a8bb50)
- 新版 `00a8b98c`（命令位置の公開資料なし）

~~~diff
- 00a8b948 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00a8b948 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00a8b948 bytes f41b00f9
+ 00a8b98c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
+ 00a8b98c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00a8b98c bytes f41b00f9
- 00a8bb50 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a8bb50 ["CBRANCH", null, ["local:b41:8", "tmp:0:1"]]
- 00a8bb50 bytes 810c0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ffbadb1ca6ec5b37818c2173fc168d8"></a>

### [`00a8c290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c290.md) → [`00a8c2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8c2d4.md) FUN_00a8c2d4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 11件 [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`00ab11f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab11f0.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 11件 [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md) [`00ab1234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1234.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 45.45% / 新版 43.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8c2c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8c2ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8c2f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a8c2c8",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a8c2c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x1a0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a8c2d0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb040"
      ]
    ]
  ],
  "added": [
    [
      "00a8c30c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00a8c30c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1a0]",
        null,
        null
      ]
    ],
    [
      "00a8c314",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8c2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c290.md#insn-00a8c2c8) · [`00a8c2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c290.md#insn-00a8c2d0) · [`00a8c2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c290.md#insn-00a8c2ec)

~~~diff
- 00a8c2c8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00a8c2c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a8c2c8 bytes e81300f9
- 00a8c2d0 ["INT_ADD", "register:40f0:8", ["const:a8c2d0:8", "const:4:8"]]
- 00a8c2d0 ["CALL", null, ["callee:00bdb040:8"]]
- 00a8c2d0 bytes 483b0594
- 00a8c2ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a8c2ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00a8c2ec bytes e00b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49b0900cbfc91fa60ead831d72b333e8"></a>

### [`00a8c478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c478.md) → [`00a8c4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8c4bc.md) FUN_00a8c4bc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a90870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90870.md) [`00a90e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90e28.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0063fa4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063f/0063fa4c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 2件 [`00a908b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a908b4.md) [`00a90e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90e6c.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0063fa4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063fa4c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.45% / 新版 89.45%

CFGの説明率　旧版 94.12% / 新版 92.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8c77c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8c780"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8c788"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a8c4f4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8c500",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8c508",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a8c4f4",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8c500",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8c508",
      "PARAM",
      [
        "storage",
        "00c0df30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8c4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c478.md#insn-00a8c4d0) · [`00a8c668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c478.md#insn-00a8c668) · [`00a8c738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c478.md#insn-00a8c738)
- 新版 `00a8c514`（命令位置の公開資料なし） · `00a8c6ac`（命令位置の公開資料なし） · `00a8c77c`（命令位置の公開資料なし）

~~~diff
- 00a8c4d0 ["INT_ADD", "register:40f0:8", ["const:a8c4d0:8", "const:4:8"]]
- 00a8c4d0 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00a8c514 ["INT_ADD", "register:40f0:8", ["const:a8c514:8", "const:4:8"]]
+ 00a8c514 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00a8c4d0 bytes a83c0594
+ 00a8c514 bytes ab3c0594
- 00a8c668 ["INT_ADD", "register:40f0:8", ["const:a8c668:8", "const:4:8"]]
- 00a8c668 ["CALL", null, ["callee:0045b734:8"]]
+ 00a8c6ac ["INT_ADD", "register:40f0:8", ["const:a8c6ac:8", "const:4:8"]]
+ 00a8c6ac ["CALL", null, ["callee:0045b734:8"]]
- 00a8c668 bytes 333ce797
+ 00a8c6ac bytes 223ce797
- 00a8c738 ["INT_ADD", "register:40f0:8", ["const:a8c738:8", "const:4:8"]]
- 00a8c738 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a8c77c ["INT_ADD", "register:40f0:8", ["const:a8c77c:8", "const:4:8"]]
+ 00a8c77c ["CALL", null, ["callee:00bdb060:8"]]
- 00a8c738 bytes 363a0594
+ 00a8c77c bytes 393a0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a742490d2c8dacd4fc1f4f64e87bf5ca"></a>

### [`00a8c854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c854.md) → [`00a8c898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8c898.md) FUN_00a8c898

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`006dd65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006dd65c.md) [`008bb9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md) · 呼出先 10件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0063eaf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063eaf8.md) [`00aa3f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3f20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 3件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`006dd65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006dd65c.md) [`008bb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb9b0.md) · 呼出先 10件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0063eaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063eaf8.md) [`00aa3f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3f64.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.41% / 新版 81.41%

CFGの説明率　旧版 59.57% / 新版 54.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8c858"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8c858"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8c85c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a8c858",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a8c85c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a8c860",
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
      "00a8c89c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a8c8a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a8c8a4",
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

- 旧版 [`00a8c858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c854.md#insn-00a8c858) · [`00a8c85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c854.md#insn-00a8c85c) · [`00a8c860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c854.md#insn-00a8c860)

~~~diff
- 00a8c858 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a8c858 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a8c858 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00a8c858 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a8c858 bytes fd7b03a9
- 00a8c85c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a8c85c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a8c85c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a8c85c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a8c85c bytes fc6f04a9
- 00a8c860 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a8c860 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a8c860 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00a8c860 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a8c860 bytes fa6705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ba473f89952e369b700090031ee43c0"></a>

### [`00a8cda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8cda0.md) → [`00a8cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8cde4.md) FUN_00a8cde4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a8cdf0",
      "incomplete_value": false,
      "site": "00a8cdf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8cdac",
      "incomplete_value": false,
      "site": "00a8cdac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "00a8cdf0",
      "DATA",
      [
        "storage",
        "00c0df08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8cdf0",
      "DATA",
      [
        "storage",
        "00c0df58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8cda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8cda0.md#insn-00a8cda8)
- 新版 `00a8cdec`（命令位置の公開資料なし）

~~~diff
- 00a8cda8 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00a8cda8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8cda8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8cda8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8cdec ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00a8cdec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8cdec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8cdec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8cda8 bytes 29213c91
+ 00a8cdec bytes 29613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a8508880a478eb15d517cfb82c6a286"></a>

### [`00a8cdbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8cdbc.md) → [`00a8ce00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8ce00.md) FUN_00a8ce00

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0059be80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059b/0059be80.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0059be80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059b/0059be80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 27.50% / 新版 24.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8cf18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8cf84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8d0c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a8cf18",
      "DATA",
      [
        "storage",
        "0032fb85",
        null,
        "dword"
      ]
    ],
    [
      "unmatched:00a8cf84",
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
      "00a8cf5c",
      "DATA",
      [
        "storage",
        "0032fb85",
        null,
        "dword"
      ]
    ],
    [
      "00a8cfc8",
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

- 旧版 [`00a8cf18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8cdbc.md#insn-00a8cf18) · [`00a8cf84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8cdbc.md#insn-00a8cf84)
- 新版 `00a8cf5c`（命令位置の公開資料なし）

~~~diff
- 00a8cf18 ["COPY", "tmp:0:4", ["register:40b0:4"]]
- 00a8cf18 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a8cf18 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a8cf18 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00a8cf18 bytes 16682838
+ 00a8cf5c ["COPY", "tmp:0:4", ["register:40b0:4"]]
+ 00a8cf5c ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a8cf5c ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00a8cf5c ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00a8cf5c bytes 16682838
- 00a8cf84 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00a8cf84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00a8cf84 bytes f40700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6c404169e1fb53b8478ad1ac69cbf0c"></a>

### [`00a8d0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8d0fc.md) → [`00a8d140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d140.md) FUN_00a8d140

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-659f09cdbbc6827d7ee70682ab09e094"></a>

### [`00a8d15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8d15c.md) → [`00a8d1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d1a0.md) FUN_00a8d1a0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a8d1ac",
      "incomplete_value": false,
      "site": "00a8d1ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8d168",
      "incomplete_value": false,
      "site": "00a8d168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "00a8d1ac",
      "DATA",
      [
        "storage",
        "00c0df88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8d1ac",
      "DATA",
      [
        "storage",
        "00c0dfd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8d164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8d15c.md#insn-00a8d164)
- 新版 `00a8d1a8`（命令位置の公開資料なし）

~~~diff
- 00a8d164 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 00a8d164 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8d164 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8d164 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8d1a8 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 00a8d1a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8d1a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8d1a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8d164 bytes 29213e91
+ 00a8d1a8 bytes 29613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa8593a96785a4039e53a26e188b8f0b"></a>

### [`00a8d178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8d178.md) → [`00a8d1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d1bc.md) FUN_00a8d1bc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 26件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 26件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.36% / 新版 83.36%

CFGの説明率　旧版 54.35% / 新版 53.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 10件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 24件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8d284"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8d330"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8d33c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a8d22c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00a8d1f8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:00a8d200",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a8d22c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8d23c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8d244",
      "PARAM",
      [
        "storage",
        "00c0df30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8d284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8d178.md#insn-00a8d284) · [`00a8d2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8d178.md#insn-00a8d2c8)
- 新版 `00a8d2c8`（命令位置の公開資料なし）

~~~diff
- 00a8d284 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00a8d284 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a8d284 bytes e81300f9
- 00a8d2c8 ["INT_LEFT", "tmp:0:4", ["register:4058:4", "const:8:4"]]
- 00a8d2c8 ["INT_OR", "tmp:1:4", ["register:4050:4", "tmp:0:4"]]
- 00a8d2c8 ["INT_ZEXT", "register:4050:8", ["tmp:1:4"]]
- 00a8d2c8 bytes 4a210b2a
+ 00a8d2c8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
+ 00a8d2c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a8d2c8 bytes e81300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8aa62a8ca9c822106f3bc7f5003f523"></a>

### [`00a8dafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8dafc.md) → [`00a8db40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8db40.md) FUN_00a8db40

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a8db64",
      "incomplete_value": false,
      "site": "00a8db64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8db20",
      "incomplete_value": false,
      "site": "00a8db20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "00a8db64",
      "DATA",
      [
        "storage",
        "00c0e008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8db64",
      "DATA",
      [
        "storage",
        "00c0e058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8db10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8dafc.md#insn-00a8db10) · [`00a8db1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8dafc.md#insn-00a8db1c)
- 新版 `00a8db54`（命令位置の公開資料なし） · `00a8db60`（命令位置の公開資料なし）

~~~diff
- 00a8db10 ["INT_ADD", "register:40f0:8", ["const:a8db10:8", "const:4:8"]]
- 00a8db10 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a8db54 ["INT_ADD", "register:40f0:8", ["const:a8db54:8", "const:4:8"]]
+ 00a8db54 ["CALL", null, ["callee:00bdb040:8"]]
- 00a8db10 bytes 38350594
+ 00a8db54 bytes 3b350594
- 00a8db1c ["COPY", "tmp:0:8", ["const:8:8"]]
- 00a8db1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8db1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8db1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8db60 ["COPY", "tmp:0:8", ["const:58:8"]]
+ 00a8db60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8db60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8db60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8db1c bytes 08210091
+ 00a8db60 bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-681df31e1e24ff090803f050044bd3ad"></a>

### [`00a8db4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8db4c.md) → [`00a8db90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8db90.md) FUN_00a8db90

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00666298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00666/00666298.md) [`006a8e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8e60.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00666298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00666/00666298.md) [`006a8e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a8e60.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 66.67% / 新版 57.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a8dc40",
      "incomplete_value": true,
      "site": "00a8dc40",
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
      "definition_site": "00a8dbfc",
      "incomplete_value": true,
      "site": "00a8dbfc",
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a8dc48",
      "incomplete_value": false,
      "site": "00a8dc58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8dc04",
      "incomplete_value": false,
      "site": "00a8dc14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "definition_site": "00a8dc50",
      "incomplete_value": false,
      "site": "00a8dc58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8dc0c",
      "incomplete_value": false,
      "site": "00a8dc14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "00a8dc3c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8dc48",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8dc50",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a8dc3c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8dc48",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8dc50",
      "PARAM",
      [
        "storage",
        "00c0df30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8dbb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8db4c.md#insn-00a8dbb8) · [`00a8dc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8db4c.md#insn-00a8dc14) · [`00a8dcf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8db4c.md#insn-00a8dcf4)
- 新版 `00a8dbfc`（命令位置の公開資料なし） · `00a8dc58`（命令位置の公開資料なし）

~~~diff
- 00a8dbb8 ["INT_ADD", "register:40f0:8", ["const:a8dbb8:8", "const:4:8"]]
- 00a8dbb8 ["CALL", null, ["ram:457e1c:8"]]
+ 00a8dbfc ["INT_ADD", "register:40f0:8", ["const:a8dbfc:8", "const:4:8"]]
+ 00a8dbfc ["CALL", null, ["ram:457e1c:8"]]
- 00a8dbb8 bytes 9928e797
+ 00a8dbfc bytes 8828e797
- 00a8dc14 ["INT_ADD", "register:40f0:8", ["const:a8dc14:8", "const:4:8"]]
- 00a8dc14 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00a8dc58 ["INT_ADD", "register:40f0:8", ["const:a8dc58:8", "const:4:8"]]
+ 00a8dc58 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00a8dc14 bytes d7360594
+ 00a8dc58 bytes da360594
- 00a8dcf4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a8dcf4 ["RETURN", null, ["register:0:8"]]
- 00a8dcf4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0acdafb02a46097fdcd6f9055f04e2d1"></a>

### [`00a8dd4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8dd4c.md) → [`00a8dd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8dd90.md) FUN_00a8dd90

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-517145e40b3cd39033037be4c8d6a587"></a>

### [`00a8deb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8deb8.md) → [`00a8defc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8defc.md) FUN_00a8defc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a8df20",
      "incomplete_value": false,
      "site": "00a8df20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8dedc",
      "incomplete_value": false,
      "site": "00a8dedc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "00a8df20",
      "DATA",
      [
        "storage",
        "00c0e108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8df20",
      "DATA",
      [
        "storage",
        "00c0e158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8decc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8deb8.md#insn-00a8decc) · [`00a8ded8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8deb8.md#insn-00a8ded8)
- 新版 `00a8df10`（命令位置の公開資料なし） · `00a8df1c`（命令位置の公開資料なし）

~~~diff
- 00a8decc ["INT_ADD", "register:40f0:8", ["const:a8decc:8", "const:4:8"]]
- 00a8decc ["CALL", null, ["callee:00bdb040:8"]]
+ 00a8df10 ["INT_ADD", "register:40f0:8", ["const:a8df10:8", "const:4:8"]]
+ 00a8df10 ["CALL", null, ["callee:00bdb040:8"]]
- 00a8decc bytes 49340594
+ 00a8df10 bytes 4c340594
- 00a8ded8 ["COPY", "tmp:0:8", ["const:108:8"]]
- 00a8ded8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8ded8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8ded8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8df1c ["COPY", "tmp:0:8", ["const:158:8"]]
+ 00a8df1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8df1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8df1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8ded8 bytes 08210491
+ 00a8df1c bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a13831928b8601d9a03fcf0f5b96d5e"></a>

### [`00a8e068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e068.md) → [`00a8e0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e0ac.md) FUN_00a8e0ac

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a8e0d0",
      "incomplete_value": false,
      "site": "00a8e0d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8e08c",
      "incomplete_value": false,
      "site": "00a8e08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "00a8e0d0",
      "DATA",
      [
        "storage",
        "00c0e188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8e0d0",
      "DATA",
      [
        "storage",
        "00c0e1d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8e07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e068.md#insn-00a8e07c) · [`00a8e088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e068.md#insn-00a8e088)
- 新版 `00a8e0c0`（命令位置の公開資料なし） · `00a8e0cc`（命令位置の公開資料なし）

~~~diff
- 00a8e07c ["INT_ADD", "register:40f0:8", ["const:a8e07c:8", "const:4:8"]]
- 00a8e07c ["CALL", null, ["callee:00bdb040:8"]]
+ 00a8e0c0 ["INT_ADD", "register:40f0:8", ["const:a8e0c0:8", "const:4:8"]]
+ 00a8e0c0 ["CALL", null, ["callee:00bdb040:8"]]
- 00a8e07c bytes dd330594
+ 00a8e0c0 bytes e0330594
- 00a8e088 ["COPY", "tmp:0:8", ["const:188:8"]]
- 00a8e088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8e088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8e088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8e0cc ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 00a8e0cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8e0cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8e0cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8e088 bytes 08210691
+ 00a8e0cc bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c93e920f3be031cf0f4a08b885c016f"></a>

### [`00a8e0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e0b8.md) → [`00a8e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e0fc.md) FUN_00a8e0fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.58% / 新版 83.58%

CFGの説明率　旧版 39.34% / 新版 40.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8e0bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8e0bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8e0c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a8e0bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a8e0c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a8e0c4",
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
      "00a8e100",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a8e104",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a8e108",
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

- 旧版 [`00a8e0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e0b8.md#insn-00a8e0bc) · [`00a8e0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e0b8.md#insn-00a8e0c0) · [`00a8e0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e0b8.md#insn-00a8e0c4)

~~~diff
- 00a8e0bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a8e0bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a8e0bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00a8e0bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a8e0bc bytes fd7b0aa9
- 00a8e0c0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a8e0c0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a8e0c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00a8e0c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a8e0c0 bytes f6570ba9
- 00a8e0c4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a8e0c4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a8e0c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00a8e0c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a8e0c4 bytes f44f0ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-442841fb6e463a73b38f68759b27e9dc"></a>

### [`00a8e52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e52c.md) → [`00a8e570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e570.md) FUN_00a8e570

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a8e57c",
      "incomplete_value": false,
      "site": "00a8e57c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8e538",
      "incomplete_value": false,
      "site": "00a8e538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "00a8e57c",
      "DATA",
      [
        "storage",
        "00c0e1f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8e57c",
      "DATA",
      [
        "storage",
        "00c0e248",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8e534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e52c.md#insn-00a8e534)
- 新版 `00a8e578`（命令位置の公開資料なし）

~~~diff
- 00a8e534 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 00a8e534 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8e534 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8e534 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8e578 ["COPY", "tmp:0:8", ["const:248:8"]]
+ 00a8e578 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8e578 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8e578 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8e534 bytes 29e10791
+ 00a8e578 bytes 29210991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64a3f90a57b12b10d1521234ee657802"></a>

### [`00a8e548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e548.md) → [`00a8e58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e58c.md) FUN_00a8e58c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 36件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)
- 新版 呼出元 0件  · 呼出先 36件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.05% / 新版 89.05%

CFGの説明率　旧版 41.84% / 新版 41.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 18件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8e558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8e558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8e55c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a8e558",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a8e55c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a8e560",
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
      "00a8e59c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a8e5a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a8e5a4",
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

- 旧版 [`00a8e558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e548.md#insn-00a8e558) · [`00a8e55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e548.md#insn-00a8e55c) · [`00a8e560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e548.md#insn-00a8e560)

~~~diff
- 00a8e558 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a8e558 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a8e558 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00a8e558 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a8e558 bytes f85f0ea9
- 00a8e55c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a8e55c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a8e55c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00a8e55c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a8e55c bytes f6570fa9
- 00a8e560 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a8e560 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a8e560 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00a8e560 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a8e560 bytes f44f10a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76a05fb17b8299b9c082e48a17dcb423"></a>

### [`00a8ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8ef54.md) → [`00a8ef98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8ef98.md) FUN_00a8ef98

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-0418ad719cda58c2771830d66fc76186"></a>

### [`00a8ef80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8ef80.md) → [`00a8efc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8efc4.md) FUN_00a8efc4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8ef84"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a8efe8",
      "incomplete_value": false,
      "site": "00a8efe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8efa4",
      "incomplete_value": false,
      "site": "00a8efa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "definition_site": "00a8efe8",
      "incomplete_value": true,
      "site": "00a8efe8",
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
                "register:4098:8"
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
    "old": {
      "definition_site": "00a8efa4",
      "incomplete_value": true,
      "site": "00a8efa4",
      "value": [
        "live",
        "register:4048:8"
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
      "unmatched:00a8ef84",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a8efe8",
      "DATA",
      [
        "storage",
        "00c0e268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8efc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a8efe8",
      "DATA",
      [
        "storage",
        "00c0e2b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8ef84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8ef80.md#insn-00a8ef84) · [`00a8ef88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8ef80.md#insn-00a8ef88)
- 新版 `00a8efc8`（命令位置の公開資料なし）

~~~diff
- 00a8ef84 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a8ef84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a8ef84 bytes f30b00f9
+ 00a8efc8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 00a8efc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00a8efc8 bytes f30b00f9
- 00a8ef88 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00a8ef88 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8cc8415352da2e0308157278778c83e"></a>

### [`00a8efb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8efb4.md) → [`00a8eff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8eff8.md) FUN_00a8eff8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a8f004",
      "incomplete_value": false,
      "site": "00a8f004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8efc0",
      "incomplete_value": false,
      "site": "00a8efc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "00a8f004",
      "DATA",
      [
        "storage",
        "00c0e268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f004",
      "DATA",
      [
        "storage",
        "00c0e2b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8efbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8efb4.md#insn-00a8efbc)
- 新版 `00a8f000`（命令位置の公開資料なし）

~~~diff
- 00a8efbc ["COPY", "tmp:0:8", ["const:268:8"]]
- 00a8efbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8efbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8efbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8f000 ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 00a8f000 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f000 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f000 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8efbc bytes 29a10991
+ 00a8f000 bytes 29e10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-352f93965d25d4783d402efc1085d831"></a>

### [`00a8efd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8efd0.md) → [`00a8f014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f014.md) FUN_00a8f014

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046f248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f248.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046f248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f248.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 93.42% / 新版 93.42%

CFGの説明率　旧版 90.48% / 新版 86.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a8f0bc",
      "incomplete_value": true,
      "site": "00a8f0bc",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:4a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f078",
      "incomplete_value": true,
      "site": "00a8f078",
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
                "const:fb0:8"
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
      "definition_site": "00a8f0c0",
      "incomplete_value": true,
      "site": "00a8f0c0",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f07c",
      "incomplete_value": true,
      "site": "00a8f07c",
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
                "const:5:8"
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
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a8f0b4",
      "incomplete_value": true,
      "site": "00a8f0b8",
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
                "const:18:8"
              ]
            ]
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
      "00a8f0ac",
      "READ",
      [
        "storage",
        "002a5fb0",
        null,
        "string"
      ]
    ],
    [
      "00a8f0b4",
      "READ",
      [
        "storage",
        "002a5fb5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a8f0ac",
      "READ",
      [
        "storage",
        "002a604a",
        null,
        "string"
      ]
    ],
    [
      "00a8f0b4",
      "READ",
      [
        "storage",
        "002a604f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8efd0.md#insn-00a8f0b8) · [`00a8f0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8efd0.md#insn-00a8f0c0) · [`00a8f000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8efd0.md#insn-00a8f000)
- 新版 `00a8f0fc`（命令位置の公開資料なし） · `00a8f104`（命令位置の公開資料なし） · `00a8f044`（命令位置の公開資料なし）

~~~diff
- 00a8f0b8 ["INT_ADD", "register:40f0:8", ["const:a8f0b8:8", "const:4:8"]]
- 00a8f0b8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a8f0fc ["INT_ADD", "register:40f0:8", ["const:a8f0fc:8", "const:4:8"]]
+ 00a8f0fc ["CALL", null, ["callee:00bdb060:8"]]
- 00a8f0b8 bytes d62f0594
+ 00a8f0fc bytes d92f0594
- 00a8f0c0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00a8f0c0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00a8f0c0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00a8f0c0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00a8f104 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00a8f104 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00a8f104 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00a8f104 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00a8f0c0 bytes 68000036
+ 00a8f104 bytes 68000036
- 00a8f000 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00a8f000 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00a8f044 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00a8f044 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00a8f000 bytes e8060035
+ 00a8f044 bytes e8060035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df27f5a78138c08ba3d37e63c1759ae3"></a>

### [`00a8f19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f19c.md) → [`00a8f1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f1e0.md) FUN_00a8f1e0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a8f1ec",
      "incomplete_value": false,
      "site": "00a8f1ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f1a8",
      "incomplete_value": false,
      "site": "00a8f1a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
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
      "00a8f1ec",
      "DATA",
      [
        "storage",
        "00c0e2e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f1ec",
      "DATA",
      [
        "storage",
        "00c0e338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f1a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f19c.md#insn-00a8f1a4)
- 新版 `00a8f1e8`（命令位置の公開資料なし）

~~~diff
- 00a8f1a4 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 00a8f1a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f1a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f1a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8f1e8 ["COPY", "tmp:0:8", ["const:338:8"]]
+ 00a8f1e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f1e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f1e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8f1a4 bytes 29a10b91
+ 00a8f1e8 bytes 29e10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-695742963998614e8cb4c79ad67b7353"></a>

### [`00a8f1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f1b8.md) → [`00a8f1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f1fc.md) FUN_00a8f1fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md) [`008865a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865a8.md) [`0088823c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00888/0088823c.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md) [`008865a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/008865a8.md) [`0088823c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/0088823c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 60.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a8f1cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f1b8.md#insn-00a8f1cc) · [`00a8f1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f1b8.md#insn-00a8f1d0) · [`00a8f1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f1b8.md#insn-00a8f1d4)
- 新版 `00a8f210`（命令位置の公開資料なし） · `00a8f214`（命令位置の公開資料なし） · `00a8f218`（命令位置の公開資料なし）

~~~diff
- 00a8f1cc ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00a8f210 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00a8f1cc bytes 00010054
+ 00a8f210 bytes 00010054
- 00a8f1d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00a8f1d0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00a8f214 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00a8f214 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00a8f1d0 bytes c8020035
+ 00a8f214 bytes c8020035
- 00a8f1d4 ["INT_ADD", "register:40f0:8", ["const:a8f1d4:8", "const:4:8"]]
- 00a8f1d4 ["CALL", null, ["ram:457e1c:8"]]
+ 00a8f218 ["INT_ADD", "register:40f0:8", ["const:a8f218:8", "const:4:8"]]
+ 00a8f218 ["CALL", null, ["ram:457e1c:8"]]
- 00a8f1d4 bytes 1223e797
+ 00a8f218 bytes 0123e797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-276bb6d38f3860f1e0f2a81035ebe59c"></a>

### [`00a8f260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f260.md) → [`00a8f2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f2a4.md) FUN_00a8f2a4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a8f2b8",
      "incomplete_value": false,
      "site": "00a8f2bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f274",
      "incomplete_value": false,
      "site": "00a8f278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:368:8"
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
      "00a8f2bc",
      "DATA",
      [
        "storage",
        "00c0e368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f2bc",
      "DATA",
      [
        "storage",
        "00c0e3b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f260.md#insn-00a8f26c) · [`00a8f274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f260.md#insn-00a8f274)
- 新版 `00a8f2b0`（命令位置の公開資料なし） · `00a8f2b8`（命令位置の公開資料なし）

~~~diff
- 00a8f26c ["INT_ADD", "register:40f0:8", ["const:a8f26c:8", "const:4:8"]]
- 00a8f26c ["CALL", null, ["callee:00bdb040:8"]]
+ 00a8f2b0 ["INT_ADD", "register:40f0:8", ["const:a8f2b0:8", "const:4:8"]]
+ 00a8f2b0 ["CALL", null, ["callee:00bdb040:8"]]
- 00a8f26c bytes 612f0594
+ 00a8f2b0 bytes 642f0594
- 00a8f274 ["COPY", "tmp:0:8", ["const:368:8"]]
- 00a8f274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8f2b8 ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 00a8f2b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f2b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f2b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8f274 bytes 08a10d91
+ 00a8f2b8 bytes 08e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-282b6b07a3a1633cece2d14b79758e6a"></a>

### [`00a8f284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f284.md) → [`00a8f2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f2c8.md) FUN_00a8f2c8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a8f2cc",
      "incomplete_value": false,
      "site": "00a8f2d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f288",
      "incomplete_value": false,
      "site": "00a8f28c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:368:8"
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
      "00a8f2d0",
      "DATA",
      [
        "storage",
        "00c0e368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f2d0",
      "DATA",
      [
        "storage",
        "00c0e3b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f284.md#insn-00a8f288)
- 新版 `00a8f2cc`（命令位置の公開資料なし）

~~~diff
- 00a8f288 ["COPY", "tmp:0:8", ["const:368:8"]]
- 00a8f288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8f2cc ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 00a8f2cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f2cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f2cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8f288 bytes 08a10d91
+ 00a8f2cc bytes 08e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1155e35f0516493a13c0b3d91fc2ec8b"></a>

### [`00a8f2dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f2dc.md) → [`00a8f320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f320.md) FUN_00a8f320

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-75af2001287362a8d06a199f07f16eb3"></a>

### [`00a8f33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f33c.md) → [`00a8f380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f380.md) FUN_00a8f380

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a8f38c",
      "incomplete_value": false,
      "site": "00a8f38c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f348",
      "incomplete_value": false,
      "site": "00a8f348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
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
      "00a8f38c",
      "DATA",
      [
        "storage",
        "00c0e3f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f38c",
      "DATA",
      [
        "storage",
        "00c0e448",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f33c.md#insn-00a8f344)
- 新版 `00a8f388`（命令位置の公開資料なし）

~~~diff
- 00a8f344 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 00a8f344 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f344 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f344 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8f388 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 00a8f388 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f388 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f388 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8f344 bytes 29e10f91
+ 00a8f388 bytes 29211191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-112249211d58cb889cc5c878982e02b6"></a>

### [`00a8f358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f358.md) → [`00a8f39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f39c.md) FUN_00a8f39c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`0044ac14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac14.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`0044ac14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac14.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.76% / 新版 98.76%

CFGの説明率　旧版 70.83% / 新版 70.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a8f3f4",
      "incomplete_value": true,
      "site": "00a8f3f4",
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
      "definition_site": "00a8f3b0",
      "incomplete_value": true,
      "site": "00a8f3b0",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a8f3fc",
      "incomplete_value": false,
      "site": "00a8f40c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f3b8",
      "incomplete_value": false,
      "site": "00a8f3c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "definition_site": "00a8f404",
      "incomplete_value": false,
      "site": "00a8f40c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f3c0",
      "incomplete_value": false,
      "site": "00a8f3c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "00a8f3f0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8f3fc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8f404",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a8f3f0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8f3fc",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8f404",
      "PARAM",
      [
        "storage",
        "00c0df30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f358.md#insn-00a8f3c8) · [`00a8f400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f358.md#insn-00a8f400) · [`00a8f394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f358.md#insn-00a8f394)
- 新版 `00a8f40c`（命令位置の公開資料なし） · `00a8f444`（命令位置の公開資料なし） · `00a8f3d8`（命令位置の公開資料なし）

~~~diff
- 00a8f3c8 ["INT_ADD", "register:40f0:8", ["const:a8f3c8:8", "const:4:8"]]
- 00a8f3c8 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00a8f40c ["INT_ADD", "register:40f0:8", ["const:a8f40c:8", "const:4:8"]]
+ 00a8f40c ["CALL", null, ["callee:00bdb7c0:8"]]
- 00a8f3c8 bytes ea300594
+ 00a8f40c bytes ed300594
- 00a8f400 ["INT_ADD", "register:40f0:8", ["const:a8f400:8", "const:4:8"]]
- 00a8f400 ["CALL", null, ["callee:00444c88:8"]]
+ 00a8f444 ["INT_ADD", "register:40f0:8", ["const:a8f444:8", "const:4:8"]]
+ 00a8f444 ["CALL", null, ["callee:00444c88:8"]]
- 00a8f400 bytes 22d6e697
+ 00a8f444 bytes 11d6e697
- 00a8f394 ["INT_ADD", "register:40f0:8", ["const:a8f394:8", "const:4:8"]]
- 00a8f394 ["CALL", null, ["callee:0088600c:8"]]
+ 00a8f3d8 ["INT_ADD", "register:40f0:8", ["const:a8f3d8:8", "const:4:8"]]
+ 00a8f3d8 ["CALL", null, ["callee:0088600c:8"]]
- 00a8f394 bytes 1edbf797
+ 00a8f3d8 bytes 0ddbf797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30d9c37072bd3ba5df1b5e89ba4e3a03"></a>

### [`00a8f660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f660.md) → [`00a8f6a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f6a4.md) FUN_00a8f6a4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`006330dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00633/006330dc.md) [`00a8f820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f820.md) [`00a8f824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f824.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`006330dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/006330dc.md) [`00a8f864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f864.md) [`00a8f868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f868.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a8f734",
      "incomplete_value": false,
      "site": "00a8f734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f6f0",
      "incomplete_value": false,
      "site": "00a8f6f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
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
      "00a8f734",
      "DATA",
      [
        "storage",
        "00c0e4f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a8f770",
      "READ",
      [
        "storage",
        "00c0e518",
        null,
        "pointer"
      ]
    ],
    [
      "00a8f770",
      "READ",
      [
        "storage",
        "00c0e520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f734",
      "DATA",
      [
        "storage",
        "00c0e548",
        null,
        "undefined *"
      ]
    ],
    [
      "00a8f770",
      "READ",
      [
        "storage",
        "00c0e568",
        null,
        "pointer"
      ]
    ],
    [
      "00a8f770",
      "READ",
      [
        "storage",
        "00c0e570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f660.md#insn-00a8f694) · [`00a8f6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f660.md#insn-00a8f6b0) · [`00a8f6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f660.md#insn-00a8f6e4)
- 新版 `00a8f6d8`（命令位置の公開資料なし） · `00a8f6f4`（命令位置の公開資料なし） · `00a8f728`（命令位置の公開資料なし）

~~~diff
- 00a8f694 ["INT_ADD", "register:40f0:8", ["const:a8f694:8", "const:4:8"]]
- 00a8f694 ["CALL", null, ["ram:457e1c:8"]]
+ 00a8f6d8 ["INT_ADD", "register:40f0:8", ["const:a8f6d8:8", "const:4:8"]]
+ 00a8f6d8 ["CALL", null, ["ram:457e1c:8"]]
- 00a8f694 bytes e221e797
+ 00a8f6d8 bytes d121e797
- 00a8f6b0 ["INT_ADD", "register:40f0:8", ["const:a8f6b0:8", "const:4:8"]]
- 00a8f6b0 ["CALL", null, ["ram:457e1c:8"]]
+ 00a8f6f4 ["INT_ADD", "register:40f0:8", ["const:a8f6f4:8", "const:4:8"]]
+ 00a8f6f4 ["CALL", null, ["ram:457e1c:8"]]
- 00a8f6b0 bytes db21e797
+ 00a8f6f4 bytes ca21e797
- 00a8f6e4 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00a8f6e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f6e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f6e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8f728 ["COPY", "tmp:0:8", ["const:548:8"]]
+ 00a8f728 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f728 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f728 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8f6e4 bytes 29e11391
+ 00a8f728 bytes 29211591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86ba04afa0490d2d21431ccda059a9ec"></a>

### [`00a8f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f7d0.md) → [`00a8f814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f814.md) FUN_00a8f814

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

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
      "site": "00a8f7f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a8f838"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a8f824",
      "incomplete_value": false,
      "site": "00a8f828",
      "value": [
        "leaf",
        "const:18:8"
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
      "unmatched:00a8f7f4",
      "DATA",
      [
        "storage",
        "00c0e4f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f838",
      "DATA",
      [
        "storage",
        "00c0e548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f7d0.md#insn-00a8f7e4) · [`00a8f7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f7d0.md#insn-00a8f7f4)
- 新版 `00a8f828`（命令位置の公開資料なし） · `00a8f838`（命令位置の公開資料なし）

~~~diff
- 00a8f7e4 ["INT_ADD", "register:40f0:8", ["const:a8f7e4:8", "const:4:8"]]
- 00a8f7e4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a8f828 ["INT_ADD", "register:40f0:8", ["const:a8f828:8", "const:4:8"]]
+ 00a8f828 ["CALL", null, ["callee:00bdb040:8"]]
- 00a8f7e4 bytes 032e0594
+ 00a8f828 bytes 062e0594
- 00a8f7f4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a8f7f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a8f7f4 bytes 080000f9
+ 00a8f838 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00a8f838 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a8f838 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14e1ae54ad365649b53b245e6e1c6341"></a>

### [`00a8f808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f808.md) → [`00a8f84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f84c.md) FUN_00a8f84c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a8f850",
      "incomplete_value": false,
      "site": "00a8f854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f80c",
      "incomplete_value": false,
      "site": "00a8f810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
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
      "00a8f854",
      "DATA",
      [
        "storage",
        "00c0e4f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f854",
      "DATA",
      [
        "storage",
        "00c0e548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f80c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f808.md#insn-00a8f80c)
- 新版 `00a8f850`（命令位置の公開資料なし）

~~~diff
- 00a8f80c ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00a8f80c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f80c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f80c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8f850 ["COPY", "tmp:0:8", ["const:548:8"]]
+ 00a8f850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8f80c bytes 08e11391
+ 00a8f850 bytes 08211591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4eae8082d665f92a295fe37adb1f65c"></a>

### [`00a8f8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f8b4.md) → [`00a8f8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f8f8.md) FUN_00a8f8f8

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 33件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md)
- 新版 呼出元 0件  · 呼出先 33件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 36.03% / 新版 37.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 30件, `store_value` 1件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 24件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8f8b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8f8b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a8f8bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a8f8b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a8f8bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a8f8c0",
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
      "00a8f8fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a8f900",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a8f904",
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

- 旧版 [`00a8f8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f8b4.md#insn-00a8f8b8) · [`00a8f8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f8b4.md#insn-00a8f8bc) · [`00a8f8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f8b4.md#insn-00a8f8c0)

~~~diff
- 00a8f8b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a8f8b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a8f8b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00a8f8b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a8f8b8 bytes fd7b0fa9
- 00a8f8bc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a8f8bc ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a8f8bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00a8f8bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a8f8bc bytes fc6f10a9
- 00a8f8c0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a8f8c0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a8f8c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00a8f8c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a8f8c0 bytes fa6711a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac9706cf26ee6c4b4d9183af9d126e04"></a>

### [`00a8ffe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8ffe4.md) → [`00a90028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90028.md) FUN_00a90028

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a9004c",
      "incomplete_value": false,
      "site": "00a9004c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90008",
      "incomplete_value": false,
      "site": "00a90008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a9004c",
      "DATA",
      [
        "storage",
        "00c0e5f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a9004c",
      "DATA",
      [
        "storage",
        "00c0e648",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8ffe4.md#insn-00a8fff8) · [`00a90004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8ffe4.md#insn-00a90004)
- 新版 `00a9003c`（命令位置の公開資料なし） · `00a90048`（命令位置の公開資料なし）

~~~diff
- 00a8fff8 ["INT_ADD", "register:40f0:8", ["const:a8fff8:8", "const:4:8"]]
- 00a8fff8 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a9003c ["INT_ADD", "register:40f0:8", ["const:a9003c:8", "const:4:8"]]
+ 00a9003c ["CALL", null, ["callee:00bdb040:8"]]
- 00a8fff8 bytes fe2b0594
+ 00a9003c bytes 012c0594
- 00a90004 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00a90004 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90004 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90004 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90048 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 00a90048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90004 bytes 08e11791
+ 00a90048 bytes 08211991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e99c17927ca3bb2feaecc77cbbd75db8"></a>

### [`00a90018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90018.md) → [`00a9005c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a9005c.md) FUN_00a9005c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a90068",
      "incomplete_value": false,
      "site": "00a90068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90024",
      "incomplete_value": false,
      "site": "00a90024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a90068",
      "DATA",
      [
        "storage",
        "00c0e5f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90068",
      "DATA",
      [
        "storage",
        "00c0e648",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90018.md#insn-00a90020)
- 新版 `00a90064`（命令位置の公開資料なし）

~~~diff
- 00a90020 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00a90020 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a90020 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a90020 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a90064 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 00a90064 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a90064 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a90064 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a90020 bytes 29e11791
+ 00a90064 bytes 29211991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37d90078234e98cab7fa1ee6b4f1c3d7"></a>

### [`00a90144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90144.md) → [`00a90188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90188.md) FUN_00a90188

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a901ac",
      "incomplete_value": false,
      "site": "00a901ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90168",
      "incomplete_value": false,
      "site": "00a90168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "00a901ac",
      "DATA",
      [
        "storage",
        "00c0e678",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a901ac",
      "DATA",
      [
        "storage",
        "00c0e6c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90144.md#insn-00a90158) · [`00a90164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90144.md#insn-00a90164)
- 新版 `00a9019c`（命令位置の公開資料なし） · `00a901a8`（命令位置の公開資料なし）

~~~diff
- 00a90158 ["INT_ADD", "register:40f0:8", ["const:a90158:8", "const:4:8"]]
- 00a90158 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a9019c ["INT_ADD", "register:40f0:8", ["const:a9019c:8", "const:4:8"]]
+ 00a9019c ["CALL", null, ["callee:00bdb040:8"]]
- 00a90158 bytes a62b0594
+ 00a9019c bytes a92b0594
- 00a90164 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00a90164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a901a8 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00a901a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a901a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a901a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90164 bytes 08e11991
+ 00a901a8 bytes 08211b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d2c373616d5d7d5ea1f711c1e627d74"></a>

### [`00a90178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90178.md) → [`00a901bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a901bc.md) FUN_00a901bc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a901c8",
      "incomplete_value": false,
      "site": "00a901c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90184",
      "incomplete_value": false,
      "site": "00a90184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "00a901c8",
      "DATA",
      [
        "storage",
        "00c0e678",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a901c8",
      "DATA",
      [
        "storage",
        "00c0e6c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90178.md#insn-00a90180)
- 新版 `00a901c4`（命令位置の公開資料なし）

~~~diff
- 00a90180 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00a90180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a90180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a90180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a901c4 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00a901c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a901c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a901c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a90180 bytes 29e11991
+ 00a901c4 bytes 29211b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a023e97149056731620b9d93648c4ea9"></a>

### [`00a901f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a901f0.md) → [`00a90234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90234.md) FUN_00a90234

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a90258",
      "incomplete_value": false,
      "site": "00a90258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90214",
      "incomplete_value": false,
      "site": "00a90214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
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
      "00a90258",
      "DATA",
      [
        "storage",
        "00c0e6f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90258",
      "DATA",
      [
        "storage",
        "00c0e748",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a901f0.md#insn-00a90204) · [`00a90210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a901f0.md#insn-00a90210)
- 新版 `00a90248`（命令位置の公開資料なし） · `00a90254`（命令位置の公開資料なし）

~~~diff
- 00a90204 ["INT_ADD", "register:40f0:8", ["const:a90204:8", "const:4:8"]]
- 00a90204 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a90248 ["INT_ADD", "register:40f0:8", ["const:a90248:8", "const:4:8"]]
+ 00a90248 ["CALL", null, ["callee:00bdb040:8"]]
- 00a90204 bytes 7b2b0594
+ 00a90248 bytes 7e2b0594
- 00a90210 ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 00a90210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90254 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00a90254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90210 bytes 08e11b91
+ 00a90254 bytes 08211d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7681d894a38be507ff8db76f473fc78c"></a>

### [`00a90224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90224.md) → [`00a90268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90268.md) FUN_00a90268

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a90274",
      "incomplete_value": false,
      "site": "00a90274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90230",
      "incomplete_value": false,
      "site": "00a90230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
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
      "00a90274",
      "DATA",
      [
        "storage",
        "00c0e6f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90274",
      "DATA",
      [
        "storage",
        "00c0e748",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9022c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90224.md#insn-00a9022c)
- 新版 `00a90270`（命令位置の公開資料なし）

~~~diff
- 00a9022c ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 00a9022c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a9022c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a9022c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a90270 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00a90270 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a90270 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a90270 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a9022c bytes 29e11b91
+ 00a90270 bytes 29211d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16e312ea6c9b8b125a6e714994e659bd"></a>

### [`00a90240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90240.md) → [`00a90284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90284.md) FUN_00a90284

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00883bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883bb8.md) [`008847e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/008847e4.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00883bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883bb8.md) [`008847e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/008847e4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.47% / 新版 98.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a902d4",
      "incomplete_value": true,
      "site": "00a902d4",
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
      "definition_site": "00a90290",
      "incomplete_value": true,
      "site": "00a90290",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a902dc",
      "incomplete_value": false,
      "site": "00a902ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90298",
      "incomplete_value": false,
      "site": "00a902a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "definition_site": "00a902e4",
      "incomplete_value": false,
      "site": "00a902ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a902a0",
      "incomplete_value": false,
      "site": "00a902a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "00a902d0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a902dc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a902e4",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a902d0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a902dc",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a902e4",
      "PARAM",
      [
        "storage",
        "00c0df30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a902a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90240.md#insn-00a902a8) · [`00a903e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90240.md#insn-00a903e4) · [`00a9026c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90240.md#insn-00a9026c)
- 新版 `00a902ec`（命令位置の公開資料なし） · `00a90428`（命令位置の公開資料なし） · `00a902b0`（命令位置の公開資料なし）

~~~diff
- 00a902a8 ["INT_ADD", "register:40f0:8", ["const:a902a8:8", "const:4:8"]]
- 00a902a8 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00a902ec ["INT_ADD", "register:40f0:8", ["const:a902ec:8", "const:4:8"]]
+ 00a902ec ["CALL", null, ["callee:00bdb7c0:8"]]
- 00a902a8 bytes 322d0594
+ 00a902ec bytes 352d0594
- 00a903e4 ["INT_ADD", "register:40f0:8", ["const:a903e4:8", "const:4:8"]]
- 00a903e4 ["CALL", null, ["callee:00886510:8"]]
+ 00a90428 ["INT_ADD", "register:40f0:8", ["const:a90428:8", "const:4:8"]]
+ 00a90428 ["CALL", null, ["callee:00886510:8"]]
- 00a903e4 bytes 4bd8f797
+ 00a90428 bytes 3ad8f797
- 00a9026c ["INT_ADD", "register:40f0:8", ["const:a9026c:8", "const:4:8"]]
- 00a9026c ["CALL", null, ["callee:0088600c:8"]]
+ 00a902b0 ["INT_ADD", "register:40f0:8", ["const:a902b0:8", "const:4:8"]]
+ 00a902b0 ["CALL", null, ["callee:0088600c:8"]]
- 00a9026c bytes 68d7f797
+ 00a902b0 bytes 57d7f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19b555c720ebce765a583f30fb45b48e"></a>

### [`00a9057c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a9057c.md) → [`00a905c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a905c0.md) FUN_00a905c0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a905e0",
      "incomplete_value": false,
      "site": "00a905e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a9059c",
      "incomplete_value": false,
      "site": "00a905a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a905e4",
      "DATA",
      [
        "storage",
        "00c0e778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a905e4",
      "DATA",
      [
        "storage",
        "00c0e7c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a9057c.md#insn-00a90590) · [`00a9059c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a9057c.md#insn-00a9059c)
- 新版 `00a905d4`（命令位置の公開資料なし） · `00a905e0`（命令位置の公開資料なし）

~~~diff
- 00a90590 ["INT_ADD", "register:40f0:8", ["const:a90590:8", "const:4:8"]]
- 00a90590 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a905d4 ["INT_ADD", "register:40f0:8", ["const:a905d4:8", "const:4:8"]]
+ 00a905d4 ["CALL", null, ["callee:00bdb040:8"]]
- 00a90590 bytes 982a0594
+ 00a905d4 bytes 9b2a0594
- 00a9059c ["COPY", "tmp:0:8", ["const:778:8"]]
- 00a9059c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a9059c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a9059c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a905e0 ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 00a905e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a905e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a905e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a9059c bytes 08e11d91
+ 00a905e0 bytes 08211f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-184b5e83316b7a731777e5e8b4493df3"></a>

### [`00a905b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a905b4.md) → [`00a905f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a905f8.md) FUN_00a905f8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a905fc",
      "incomplete_value": false,
      "site": "00a90600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a905b8",
      "incomplete_value": false,
      "site": "00a905bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "00a90600",
      "DATA",
      [
        "storage",
        "00c0e778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90600",
      "DATA",
      [
        "storage",
        "00c0e7c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a905b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a905b4.md#insn-00a905b8)
- 新版 `00a905fc`（命令位置の公開資料なし）

~~~diff
- 00a905b8 ["COPY", "tmp:0:8", ["const:778:8"]]
- 00a905b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a905b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a905b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a905fc ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 00a905fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a905fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a905fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a905b8 bytes 08e11d91
+ 00a905fc bytes 08211f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3db34b14832e349b819424d8901bb844"></a>

### [`00a906e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a906e8.md) → [`00a9072c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a9072c.md) FUN_00a9072c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a9074c",
      "incomplete_value": false,
      "site": "00a90750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90708",
      "incomplete_value": false,
      "site": "00a9070c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:808:8"
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
      "00a90750",
      "DATA",
      [
        "storage",
        "00c0e808",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90750",
      "DATA",
      [
        "storage",
        "00c0e858",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a906fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a906e8.md#insn-00a906fc) · [`00a90708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a906e8.md#insn-00a90708)
- 新版 `00a90740`（命令位置の公開資料なし） · `00a9074c`（命令位置の公開資料なし）

~~~diff
- 00a906fc ["INT_ADD", "register:40f0:8", ["const:a906fc:8", "const:4:8"]]
- 00a906fc ["CALL", null, ["callee:00bdb040:8"]]
+ 00a90740 ["INT_ADD", "register:40f0:8", ["const:a90740:8", "const:4:8"]]
+ 00a90740 ["CALL", null, ["callee:00bdb040:8"]]
- 00a906fc bytes 3d2a0594
+ 00a90740 bytes 402a0594
- 00a90708 ["COPY", "tmp:0:8", ["const:808:8"]]
- 00a90708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a9074c ["COPY", "tmp:0:8", ["const:858:8"]]
+ 00a9074c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a9074c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a9074c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90708 bytes 08212091
+ 00a9074c bytes 08612191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9998b10d2faf4e47e97625b4d4f67d05"></a>

### [`00a90820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90820.md) → [`00a90864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90864.md) FUN_00a90864

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a90888",
      "incomplete_value": false,
      "site": "00a90888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90844",
      "incomplete_value": false,
      "site": "00a90844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:888:8"
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
      "00a90888",
      "DATA",
      [
        "storage",
        "00c0e888",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90888",
      "DATA",
      [
        "storage",
        "00c0e8d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90820.md#insn-00a90834) · [`00a90840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90820.md#insn-00a90840)
- 新版 `00a90878`（命令位置の公開資料なし） · `00a90884`（命令位置の公開資料なし）

~~~diff
- 00a90834 ["INT_ADD", "register:40f0:8", ["const:a90834:8", "const:4:8"]]
- 00a90834 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a90878 ["INT_ADD", "register:40f0:8", ["const:a90878:8", "const:4:8"]]
+ 00a90878 ["CALL", null, ["callee:00bdb040:8"]]
- 00a90834 bytes ef290594
+ 00a90878 bytes f2290594
- 00a90840 ["COPY", "tmp:0:8", ["const:888:8"]]
- 00a90840 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90840 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90840 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90884 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 00a90884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90840 bytes 08212291
+ 00a90884 bytes 08612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8265260d5c39152b8b6d942cffd2011e"></a>

### [`00a90870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90870.md) → [`00a908b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a908b4.md) FUN_00a908b4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) [`0071a0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a0c4.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`0071a0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a0c4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.46% / 新版 79.46%

CFGの説明率　旧版 42.37% / 新版 43.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 2件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a90874"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a90874"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a90878"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a90874",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a90878",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a9087c",
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
      "00a908b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a908bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a908c0",
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

- 旧版 [`00a90874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90870.md#insn-00a90874) · [`00a90878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90870.md#insn-00a90878) · [`00a9087c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90870.md#insn-00a9087c)

~~~diff
- 00a90874 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a90874 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a90874 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00a90874 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a90874 bytes fd7b07a9
- 00a90878 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:80:8"]]
- 00a90878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00a90878 bytes fb4300f9
- 00a9087c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a9087c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a9087c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00a9087c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a9087c bytes fa6709a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da73b257d382e108768c30b52d3d6853"></a>

### [`00a90d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90d28.md) → [`00a90d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90d6c.md) FUN_00a90d6c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a90d80",
      "incomplete_value": false,
      "site": "00a90d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90d3c",
      "incomplete_value": false,
      "site": "00a90d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "00a90d84",
      "DATA",
      [
        "storage",
        "00c0e8f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90d84",
      "DATA",
      [
        "storage",
        "00c0e948",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90d28.md#insn-00a90d34) · [`00a90d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90d28.md#insn-00a90d3c)
- 新版 `00a90d78`（命令位置の公開資料なし） · `00a90d80`（命令位置の公開資料なし）

~~~diff
- 00a90d34 ["INT_ADD", "register:40f0:8", ["const:a90d34:8", "const:4:8"]]
- 00a90d34 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a90d78 ["INT_ADD", "register:40f0:8", ["const:a90d78:8", "const:4:8"]]
+ 00a90d78 ["CALL", null, ["callee:00bdb040:8"]]
- 00a90d34 bytes af280594
+ 00a90d78 bytes b2280594
- 00a90d3c ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00a90d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90d80 ["COPY", "tmp:0:8", ["const:948:8"]]
+ 00a90d80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90d80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90d80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90d3c bytes 08e12391
+ 00a90d80 bytes 08212591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-411c3057a753cc76b754116abcf6627d"></a>

### [`00a90d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90d4c.md) → [`00a90d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90d90.md) FUN_00a90d90

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a90d94",
      "incomplete_value": false,
      "site": "00a90d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90d50",
      "incomplete_value": false,
      "site": "00a90d54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "00a90d98",
      "DATA",
      [
        "storage",
        "00c0e8f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90d98",
      "DATA",
      [
        "storage",
        "00c0e948",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90d4c.md#insn-00a90d50)
- 新版 `00a90d94`（命令位置の公開資料なし）

~~~diff
- 00a90d50 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00a90d50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90d50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90d50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90d94 ["COPY", "tmp:0:8", ["const:948:8"]]
+ 00a90d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90d50 bytes 08e12391
+ 00a90d94 bytes 08212591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b3de770caa7ade5ffd5557107ba6c6e"></a>

### [`00a90d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90d64.md) → [`00a90da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90da8.md) FUN_00a90da8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 75.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a90d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90d64.md#insn-00a90d6c) · [`00a90d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90d64.md#insn-00a90d74) · [`00a90d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90d64.md#insn-00a90d88)
- 新版 `00a90db0`（命令位置の公開資料なし） · `00a90db8`（命令位置の公開資料なし） · `00a90dcc`（命令位置の公開資料なし）

~~~diff
- 00a90d6c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a90d6c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00a90db0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a90db0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00a90d6c bytes e1010054
+ 00a90db0 bytes e1010054
- 00a90d74 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00a90d74 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00a90db8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00a90db8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00a90d74 bytes a8010035
+ 00a90db8 bytes a8010035
- 00a90d88 ["INT_ADD", "register:40f0:8", ["const:a90d88:8", "const:4:8"]]
- 00a90d88 ["CALL", null, ["ram:457e1c:8"]]
+ 00a90dcc ["INT_ADD", "register:40f0:8", ["const:a90dcc:8", "const:4:8"]]
+ 00a90dcc ["CALL", null, ["ram:457e1c:8"]]
- 00a90d88 bytes 251ce797
+ 00a90dcc bytes 141ce797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-478407c16eb26b13038ed5a89a925896"></a>

### [`00a90e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90e28.md) → [`00a90e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90e6c.md) FUN_00a90e6c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md) [`00a8c478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c478.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md) [`00a8c4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8c4bc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 20.00% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a90e78"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a90ebc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a90e9c",
      "incomplete_value": false,
      "site": "00a90ea4",
      "value": [
        "leaf",
        "const:b:8"
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
      "unmatched:00a90e78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a90ee8"
      ]
    ]
  ],
  "added": [
    [
      "00a90ebc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a90ee8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90e28.md#insn-00a90e60) · [`00a90e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90e28.md#insn-00a90e78)
- 新版 `00a90ea4`（命令位置の公開資料なし） · `00a90ebc`（命令位置の公開資料なし）

~~~diff
- 00a90e60 ["INT_ADD", "register:40f0:8", ["const:a90e60:8", "const:4:8"]]
- 00a90e60 ["CALL", null, ["callee:00459efc:8"]]
+ 00a90ea4 ["INT_ADD", "register:40f0:8", ["const:a90ea4:8", "const:4:8"]]
+ 00a90ea4 ["CALL", null, ["callee:00459efc:8"]]
- 00a90e60 bytes 2724e797
+ 00a90ea4 bytes 1624e797
- 00a90e78 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a90e78 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00a90e78 bytes 61010054
+ 00a90ebc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a90ebc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00a90ebc bytes 61010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08c682adc5307725c323aa5b4a1a9742"></a>

### [`00a90f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90f00.md) → [`00a90f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90f44.md) FUN_00a90f44

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a90f48",
      "incomplete_value": false,
      "site": "00a90f4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90f04",
      "incomplete_value": false,
      "site": "00a90f08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:a08:8"
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
      "00a90f4c",
      "DATA",
      [
        "storage",
        "00c0ea08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90f4c",
      "DATA",
      [
        "storage",
        "00c0ea58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90f00.md#insn-00a90f04)
- 新版 `00a90f48`（命令位置の公開資料なし）

~~~diff
- 00a90f04 ["COPY", "tmp:0:8", ["const:a08:8"]]
- 00a90f04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90f04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90f04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90f48 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 00a90f48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90f48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90f48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90f04 bytes 08212891
+ 00a90f48 bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f55c91ede1f99ba5b4019b75722deb82"></a>

### [`00a90f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90f90.md) → [`00a90fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90fd4.md) FUN_00a90fd4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a90ff8",
      "incomplete_value": false,
      "site": "00a90ff8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90fb4",
      "incomplete_value": false,
      "site": "00a90fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "00a90ff8",
      "DATA",
      [
        "storage",
        "00c0ea88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90ff8",
      "DATA",
      [
        "storage",
        "00c0ead8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90f90.md#insn-00a90fa4) · [`00a90fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90f90.md#insn-00a90fb0)
- 新版 `00a90fe8`（命令位置の公開資料なし） · `00a90ff4`（命令位置の公開資料なし）

~~~diff
- 00a90fa4 ["INT_ADD", "register:40f0:8", ["const:a90fa4:8", "const:4:8"]]
- 00a90fa4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a90fe8 ["INT_ADD", "register:40f0:8", ["const:a90fe8:8", "const:4:8"]]
+ 00a90fe8 ["CALL", null, ["callee:00bdb040:8"]]
- 00a90fa4 bytes 13280594
+ 00a90fe8 bytes 16280594
- 00a90fb0 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00a90fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90ff4 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 00a90ff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90ff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90ff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90fb0 bytes 08212a91
+ 00a90ff4 bytes 08612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a68d5a68d9cf34e5645bc1b1a491c79"></a>

### [`00a90fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90fc4.md) → [`00a91008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91008.md) FUN_00a91008

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a91014",
      "incomplete_value": false,
      "site": "00a91014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90fd0",
      "incomplete_value": false,
      "site": "00a90fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "00a91014",
      "DATA",
      [
        "storage",
        "00c0ea88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91014",
      "DATA",
      [
        "storage",
        "00c0ead8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90fc4.md#insn-00a90fcc)
- 新版 `00a91010`（命令位置の公開資料なし）

~~~diff
- 00a90fcc ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00a90fcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a90fcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a90fcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a91010 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 00a91010 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91010 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91010 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a90fcc bytes 29212a91
+ 00a91010 bytes 29612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41210fc3f1c96c145b731c387dc25b5f"></a>

### [`00a912c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a912c0.md) → [`00a91304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91304.md) FUN_00a91304

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-754d081b87fe0c2dbaf266c164f59826"></a>

### [`00a91320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91320.md) → [`00a91364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91364.md) FUN_00a91364

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a91370",
      "incomplete_value": false,
      "site": "00a91370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a9132c",
      "incomplete_value": false,
      "site": "00a9132c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "00a91370",
      "DATA",
      [
        "storage",
        "00c0eaf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91370",
      "DATA",
      [
        "storage",
        "00c0eb48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91320.md#insn-00a91328)
- 新版 `00a9136c`（命令位置の公開資料なし）

~~~diff
- 00a91328 ["COPY", "tmp:0:8", ["const:af8:8"]]
- 00a91328 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a91328 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a91328 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a9136c ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00a9136c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a9136c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a9136c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a91328 bytes 29e12b91
+ 00a9136c bytes 29212d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e26c55a3510f7526bfb1045f25156fa8"></a>

### [`00a9133c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a9133c.md) → [`00a91380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91380.md) FUN_00a91380

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md) [`009bd60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd60c.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md) [`009bd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd618.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 83.33% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a91348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a9133c.md#insn-00a91348) · [`00a91350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a9133c.md#insn-00a91350) · [`00a91364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a9133c.md#insn-00a91364)
- 新版 `00a9138c`（命令位置の公開資料なし） · `00a91394`（命令位置の公開資料なし） · `00a913a8`（命令位置の公開資料なし）

~~~diff
- 00a91348 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a91348 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00a9138c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a9138c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00a91348 bytes e1010054
+ 00a9138c bytes e1010054
- 00a91350 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00a91350 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00a91394 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
+ 00a91394 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00a91350 bytes a9010035
+ 00a91394 bytes a9010035
- 00a91364 ["INT_ADD", "register:40f0:8", ["const:a91364:8", "const:4:8"]]
- 00a91364 ["CALL", null, ["ram:457e1c:8"]]
+ 00a913a8 ["INT_ADD", "register:40f0:8", ["const:a913a8:8", "const:4:8"]]
+ 00a913a8 ["CALL", null, ["ram:457e1c:8"]]
- 00a91364 bytes ae1ae797
+ 00a913a8 bytes 9d1ae797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e23504b9b2e6419b60decfc0227b6d62"></a>

### [`00a913d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a913d0.md) → [`00a91414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91414.md) FUN_00a91414

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a91438",
      "incomplete_value": false,
      "site": "00a91438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a913f4",
      "incomplete_value": false,
      "site": "00a913f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "00a91438",
      "DATA",
      [
        "storage",
        "00c0eb78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91438",
      "DATA",
      [
        "storage",
        "00c0ebc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a913e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a913d0.md#insn-00a913e4) · [`00a913f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a913d0.md#insn-00a913f0)
- 新版 `00a91428`（命令位置の公開資料なし） · `00a91434`（命令位置の公開資料なし）

~~~diff
- 00a913e4 ["INT_ADD", "register:40f0:8", ["const:a913e4:8", "const:4:8"]]
- 00a913e4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a91428 ["INT_ADD", "register:40f0:8", ["const:a91428:8", "const:4:8"]]
+ 00a91428 ["CALL", null, ["callee:00bdb040:8"]]
- 00a913e4 bytes 03270594
+ 00a91428 bytes 06270594
- 00a913f0 ["COPY", "tmp:0:8", ["const:b78:8"]]
- 00a913f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a913f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a913f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91434 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 00a91434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a913f0 bytes 08e12d91
+ 00a91434 bytes 08212f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baddd558a6923da312e3e8ccbd3db5dd"></a>

### [`00a91404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91404.md) → [`00a91448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91448.md) FUN_00a91448

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a91454",
      "incomplete_value": false,
      "site": "00a91454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91410",
      "incomplete_value": false,
      "site": "00a91410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "00a91454",
      "DATA",
      [
        "storage",
        "00c0eb78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91454",
      "DATA",
      [
        "storage",
        "00c0ebc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9140c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91404.md#insn-00a9140c)
- 新版 `00a91450`（命令位置の公開資料なし）

~~~diff
- 00a9140c ["COPY", "tmp:0:8", ["const:b78:8"]]
- 00a9140c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a9140c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a9140c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a91450 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 00a91450 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91450 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91450 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a9140c bytes 29e12d91
+ 00a91450 bytes 29212f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf1a53b1543bcd403576124221c74a14"></a>

### [`00a9143c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a9143c.md) → [`00a91480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91480.md) FUN_00a91480

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-01c8353b87e2c608b08faa2e0dda53f8"></a>

### [`00a91468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91468.md) → [`00a914ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a914ac.md) FUN_00a914ac

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a914d0",
      "incomplete_value": false,
      "site": "00a914d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a9148c",
      "incomplete_value": false,
      "site": "00a9148c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "00a914d0",
      "DATA",
      [
        "storage",
        "00c0ebf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a914d0",
      "DATA",
      [
        "storage",
        "00c0ec48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9147c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91468.md#insn-00a9147c) · [`00a91488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91468.md#insn-00a91488)
- 新版 `00a914c0`（命令位置の公開資料なし） · `00a914cc`（命令位置の公開資料なし）

~~~diff
- 00a9147c ["INT_ADD", "register:40f0:8", ["const:a9147c:8", "const:4:8"]]
- 00a9147c ["CALL", null, ["callee:00bdb040:8"]]
+ 00a914c0 ["INT_ADD", "register:40f0:8", ["const:a914c0:8", "const:4:8"]]
+ 00a914c0 ["CALL", null, ["callee:00bdb040:8"]]
- 00a9147c bytes dd260594
+ 00a914c0 bytes e0260594
- 00a91488 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00a91488 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91488 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91488 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a914cc ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 00a914cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a914cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a914cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91488 bytes 08e12f91
+ 00a914cc bytes 08213191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0b13331926b5144a5b9614fc38f586d"></a>

### [`00a9149c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a9149c.md) → [`00a914e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a914e0.md) FUN_00a914e0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a914ec",
      "incomplete_value": false,
      "site": "00a914ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a914a8",
      "incomplete_value": false,
      "site": "00a914a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "00a914ec",
      "DATA",
      [
        "storage",
        "00c0ebf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a914ec",
      "DATA",
      [
        "storage",
        "00c0ec48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a914a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a9149c.md#insn-00a914a4)
- 新版 `00a914e8`（命令位置の公開資料なし）

~~~diff
- 00a914a4 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00a914a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a914a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a914a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a914e8 ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 00a914e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a914e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a914e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a914a4 bytes 29e12f91
+ 00a914e8 bytes 29213191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3765f7b4e1fa162ebb580b6593ffd2c1"></a>

### [`00a914b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a914b8.md) → [`00a914fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a914fc.md) FUN_00a914fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00445d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d88.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`00a8b028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b028.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00445d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d88.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`0044aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa9c.md) [`00a8b06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8b/00a8b06c.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a91534",
      "incomplete_value": true,
      "site": "00a91534",
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
      "definition_site": "00a914f0",
      "incomplete_value": true,
      "site": "00a914f0",
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
      "definition_site": "00a9153c",
      "incomplete_value": false,
      "site": "00a9154c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a914f8",
      "incomplete_value": false,
      "site": "00a91508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "definition_site": "00a91544",
      "incomplete_value": false,
      "site": "00a9154c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91500",
      "incomplete_value": false,
      "site": "00a91508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "00a91520",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a9153c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a91544",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a91520",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a9153c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a91544",
      "PARAM",
      [
        "storage",
        "00c0df30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a914b8.md#insn-00a91508) · [`00a9154c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a914b8.md#insn-00a9154c) · [`00a91578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a914b8.md#insn-00a91578)
- 新版 `00a9154c`（命令位置の公開資料なし） · `00a91590`（命令位置の公開資料なし） · `00a915bc`（命令位置の公開資料なし）

~~~diff
- 00a91508 ["INT_ADD", "register:40f0:8", ["const:a91508:8", "const:4:8"]]
- 00a91508 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00a9154c ["INT_ADD", "register:40f0:8", ["const:a9154c:8", "const:4:8"]]
+ 00a9154c ["CALL", null, ["callee:00bdb7c0:8"]]
- 00a91508 bytes 9a280594
+ 00a9154c bytes 9d280594
- 00a9154c ["INT_ADD", "register:40f0:8", ["const:a9154c:8", "const:4:8"]]
- 00a9154c ["CALL", null, ["callee:0044aa9c:8"]]
+ 00a91590 ["INT_ADD", "register:40f0:8", ["const:a91590:8", "const:4:8"]]
+ 00a91590 ["CALL", null, ["callee:0044aa9c:8"]]
- 00a9154c bytes 54e5e697
+ 00a91590 bytes 43e5e697
- 00a91578 ["INT_ADD", "register:40f0:8", ["const:a91578:8", "const:4:8"]]
- 00a91578 ["CALL", null, ["callee:00446d2c:8"]]
+ 00a915bc ["INT_ADD", "register:40f0:8", ["const:a915bc:8", "const:4:8"]]
+ 00a915bc ["CALL", null, ["callee:00446d2c:8"]]
- 00a91578 bytes edd5e697
+ 00a915bc bytes dcd5e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf4462c84a77770b771a1f11009b0450"></a>

### [`00a9159c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a9159c.md) → [`00a915e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a915e0.md) FUN_00a915e0

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-78a1dd1248b452af9d9ade011916c80d"></a>

### [`00a915c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a915c8.md) → [`00a9160c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a9160c.md) FUN_00a9160c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a91630",
      "incomplete_value": false,
      "site": "00a91630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a915ec",
      "incomplete_value": false,
      "site": "00a915ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "00a91630",
      "DATA",
      [
        "storage",
        "00c0ec88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91630",
      "DATA",
      [
        "storage",
        "00c0ecd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a915dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a915c8.md#insn-00a915dc) · [`00a915e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a915c8.md#insn-00a915e8)
- 新版 `00a91620`（命令位置の公開資料なし） · `00a9162c`（命令位置の公開資料なし）

~~~diff
- 00a915dc ["INT_ADD", "register:40f0:8", ["const:a915dc:8", "const:4:8"]]
- 00a915dc ["CALL", null, ["callee:00bdb040:8"]]
+ 00a91620 ["INT_ADD", "register:40f0:8", ["const:a91620:8", "const:4:8"]]
+ 00a91620 ["CALL", null, ["callee:00bdb040:8"]]
- 00a915dc bytes 85260594
+ 00a91620 bytes 88260594
- 00a915e8 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00a915e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a915e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a915e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a9162c ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00a9162c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a9162c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a9162c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a915e8 bytes 08213291
+ 00a9162c bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49e155fc5c5dec9bb10d806b2393d535"></a>

### [`00a915fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a915fc.md) → [`00a91640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91640.md) FUN_00a91640

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a9164c",
      "incomplete_value": false,
      "site": "00a9164c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91608",
      "incomplete_value": false,
      "site": "00a91608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "00a9164c",
      "DATA",
      [
        "storage",
        "00c0ec88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a9164c",
      "DATA",
      [
        "storage",
        "00c0ecd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a915fc.md#insn-00a91604)
- 新版 `00a91648`（命令位置の公開資料なし）

~~~diff
- 00a91604 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00a91604 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a91604 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a91604 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a91648 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00a91648 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91648 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91648 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a91604 bytes 29213291
+ 00a91648 bytes 29613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d43fc894d2f0fc4d570fc07add4bb8b"></a>

### [`00a91634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91634.md) → [`00a91678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91678.md) FUN_00a91678

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-b329c0ac9d290c76d89308b5511df997"></a>

### [`00a91694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91694.md) → [`00a916d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a916d8.md) FUN_00a916d8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a916e4",
      "incomplete_value": false,
      "site": "00a916e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a916a0",
      "incomplete_value": false,
      "site": "00a916a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "00a916e4",
      "DATA",
      [
        "storage",
        "00c0ed08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a916e4",
      "DATA",
      [
        "storage",
        "00c0ed58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9169c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91694.md#insn-00a9169c)
- 新版 `00a916e0`（命令位置の公開資料なし）

~~~diff
- 00a9169c ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00a9169c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a9169c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a9169c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a916e0 ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 00a916e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a916e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a916e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a9169c bytes 29213491
+ 00a916e0 bytes 29613591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74176cfb9b11112c8eddd979481ff3b1"></a>

### [`00a916b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a916b0.md) → [`00a916f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a916f4.md) FUN_00a916f4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00448c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448c90.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`0044aad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aad4.md) [`00883bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883bb8.md) [`00883c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883c74.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00448c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448c90.md) [`0044aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa9c.md) [`0044aad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aad4.md) [`00883bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883bb8.md) [`00883c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883c74.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.40% / 新版 81.40%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a916c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a916c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a917c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a916c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a916dc",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00a916e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9174c"
      ]
    ]
  ],
  "added": [
    [
      "00a9170c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a91720",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a91728",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9174c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a916c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a916b0.md#insn-00a916c8) · [`00a916e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a916b0.md#insn-00a916e4) · [`00a916fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a916b0.md#insn-00a916fc)
- 新版 `00a91740`（命令位置の公開資料なし）

~~~diff
- 00a916c8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a916c8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a916c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00a916c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a916c8 bytes f44f07a9
- 00a916e4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00a916e4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00a916e4 bytes 200100b4
- 00a916fc ["INT_ADD", "register:40f0:8", ["const:a916fc:8", "const:4:8"]]
- 00a916fc ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00a91740 ["INT_ADD", "register:40f0:8", ["const:a91740:8", "const:4:8"]]
+ 00a91740 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00a916fc bytes 1d280594
+ 00a91740 bytes 20280594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6b49396c1d7b6f6cb8bfe94f287597d"></a>

### [`00a91834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91834.md) → [`00a91878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91878.md) FUN_00a91878

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a9189c",
      "incomplete_value": false,
      "site": "00a9189c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91858",
      "incomplete_value": false,
      "site": "00a91858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "00a9189c",
      "DATA",
      [
        "storage",
        "00c0ed88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a9189c",
      "DATA",
      [
        "storage",
        "00c0edd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91834.md#insn-00a91848) · [`00a91854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91834.md#insn-00a91854)
- 新版 `00a9188c`（命令位置の公開資料なし） · `00a91898`（命令位置の公開資料なし）

~~~diff
- 00a91848 ["INT_ADD", "register:40f0:8", ["const:a91848:8", "const:4:8"]]
- 00a91848 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a9188c ["INT_ADD", "register:40f0:8", ["const:a9188c:8", "const:4:8"]]
+ 00a9188c ["CALL", null, ["callee:00bdb040:8"]]
- 00a91848 bytes ea250594
+ 00a9188c bytes ed250594
- 00a91854 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 00a91854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91898 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00a91898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91854 bytes 08213691
+ 00a91898 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c048698973a2feacb05d9775f0253942"></a>

### [`00a91868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91868.md) → [`00a918ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a918ac.md) FUN_00a918ac

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a918b8",
      "incomplete_value": false,
      "site": "00a918b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91874",
      "incomplete_value": false,
      "site": "00a91874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "00a918b8",
      "DATA",
      [
        "storage",
        "00c0ed88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a918b8",
      "DATA",
      [
        "storage",
        "00c0edd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91868.md#insn-00a91870)
- 新版 `00a918b4`（命令位置の公開資料なし）

~~~diff
- 00a91870 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 00a91870 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a91870 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a91870 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a918b4 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00a918b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a918b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a918b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a91870 bytes 29213691
+ 00a918b4 bytes 29613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-020e4a11a2dd51c55eabf737c59578bb"></a>

### [`00a9195c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a9195c.md) → [`00a919a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a919a0.md) FUN_00a919a0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 27.27% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a919a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a919ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a9198c",
      "incomplete_value": false,
      "site": "00a91990",
      "value": [
        "leaf",
        "const:0:8"
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
      "unmatched:00a919a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a91a04"
      ]
    ]
  ],
  "added": [
    [
      "00a919ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a91a04"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a9195c.md#insn-00a91990) · [`00a919a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a9195c.md#insn-00a919a8)
- 新版 `00a919d4`（命令位置の公開資料なし） · `00a919ec`（命令位置の公開資料なし）

~~~diff
- 00a91990 ["INT_ADD", "register:40f0:8", ["const:a91990:8", "const:4:8"]]
- 00a91990 ["CALL", null, ["callee:00459efc:8"]]
+ 00a919d4 ["INT_ADD", "register:40f0:8", ["const:a919d4:8", "const:4:8"]]
+ 00a919d4 ["CALL", null, ["callee:00459efc:8"]]
- 00a91990 bytes 5b21e797
+ 00a919d4 bytes 4a21e797
- 00a919a8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a919a8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00a919a8 bytes c1000054
+ 00a919ec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a919ec ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00a919ec bytes c1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bdc1b69b129db433353ed8092d76a27"></a>

### [`00a919c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a919c4.md) → [`00a91a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91a08.md) FUN_00a91a08

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 14.29% / 新版 14.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-b2b9f2679a8cbd1faa262129ccde82e6"></a>

### [`00a919f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a919f0.md) → [`00a91a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91a34.md) FUN_00a91a34

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "site": "00a91a14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a91a14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a91a58"
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
      "unmatched:00a91a14",
      "DATA",
      [
        "storage",
        "00c0ee88",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a91a18",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a91a1c",
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
      "00a91a58",
      "DATA",
      [
        "storage",
        "00c0eed8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a91a5c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a91a60",
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

- 旧版 [`00a91a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a919f0.md#insn-00a91a04) · [`00a91a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a919f0.md#insn-00a91a14) · [`00a91a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a919f0.md#insn-00a91a20)
- 新版 `00a91a48`（命令位置の公開資料なし）

~~~diff
- 00a91a04 ["INT_ADD", "register:40f0:8", ["const:a91a04:8", "const:4:8"]]
- 00a91a04 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a91a48 ["INT_ADD", "register:40f0:8", ["const:a91a48:8", "const:4:8"]]
+ 00a91a48 ["CALL", null, ["callee:00bdb040:8"]]
- 00a91a04 bytes 7b250594
+ 00a91a48 bytes 7e250594
- 00a91a14 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a91a14 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a91a14 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a91a14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a91a14 bytes 082400a9
- 00a91a20 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a91a20 ["RETURN", null, ["register:0:8"]]
- 00a91a20 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5808ab840fafc0a7f2d61d2c95dcb76"></a>

### [`00a91a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91a40.md) → [`00a91a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91a84.md) FUN_00a91a84

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a91a4c",
      "DATA",
      [
        "storage",
        "00332ed8",
        null,
        "byte[35]"
      ]
    ],
    [
      "unmatched:00a91a54",
      "DATA",
      [
        "storage",
        "00332ed8",
        null,
        "byte[35]"
      ]
    ]
  ],
  "added": [
    [
      "00a91a90",
      "DATA",
      [
        "storage",
        "00332ed8",
        null,
        "byte[35]"
      ]
    ],
    [
      "00a91a98",
      "DATA",
      [
        "storage",
        "00332ed8",
        null,
        "byte[35]"
      ]
    ]
  ]
}
~~~


<a id="compare-26f885cd4a4459f9bd236bf858af6503"></a>

### [`00a91a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91a88.md) → [`00a91acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91acc.md) FUN_00a91acc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a91af0",
      "incomplete_value": false,
      "site": "00a91af0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91aac",
      "incomplete_value": false,
      "site": "00a91aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "00a91af0",
      "DATA",
      [
        "storage",
        "00c0ef08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91af0",
      "DATA",
      [
        "storage",
        "00c0ef58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91a88.md#insn-00a91a9c) · [`00a91aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91a88.md#insn-00a91aa8)
- 新版 `00a91ae0`（命令位置の公開資料なし） · `00a91aec`（命令位置の公開資料なし）

~~~diff
- 00a91a9c ["INT_ADD", "register:40f0:8", ["const:a91a9c:8", "const:4:8"]]
- 00a91a9c ["CALL", null, ["callee:00bdb040:8"]]
+ 00a91ae0 ["INT_ADD", "register:40f0:8", ["const:a91ae0:8", "const:4:8"]]
+ 00a91ae0 ["CALL", null, ["callee:00bdb040:8"]]
- 00a91a9c bytes 55250594
+ 00a91ae0 bytes 58250594
- 00a91aa8 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00a91aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91aec ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00a91aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91aa8 bytes 08213c91
+ 00a91aec bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-708280d527f9676e10f1b52553c7377f"></a>

### [`00a91abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91abc.md) → [`00a91b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91b00.md) FUN_00a91b00

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a91b0c",
      "incomplete_value": false,
      "site": "00a91b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91ac8",
      "incomplete_value": false,
      "site": "00a91ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "00a91b0c",
      "DATA",
      [
        "storage",
        "00c0ef08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91b0c",
      "DATA",
      [
        "storage",
        "00c0ef58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91abc.md#insn-00a91ac4)
- 新版 `00a91b08`（命令位置の公開資料なし）

~~~diff
- 00a91ac4 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00a91ac4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a91ac4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a91ac4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a91b08 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00a91b08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91b08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91b08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a91ac4 bytes 29213c91
+ 00a91b08 bytes 29613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9751833b1a0c26395b1290458870ecab"></a>

### [`00a91ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91ad8.md) → [`00a91b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91b1c.md) FUN_00a91b1c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00448c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448c90.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`0044aad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aad4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883bb8.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00448c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448c90.md) [`0044aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa9c.md) [`0044aad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aad4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883bb8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a91b50",
      "incomplete_value": true,
      "site": "00a91b50",
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
      "definition_site": "00a91b0c",
      "incomplete_value": true,
      "site": "00a91b0c",
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
      "definition_site": "00a91b58",
      "incomplete_value": false,
      "site": "00a91b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91b14",
      "incomplete_value": false,
      "site": "00a91b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "definition_site": "00a91b60",
      "incomplete_value": false,
      "site": "00a91b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91b1c",
      "incomplete_value": false,
      "site": "00a91b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "00a91b48",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a91b58",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a91b60",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a91b48",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a91b58",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a91b60",
      "PARAM",
      [
        "storage",
        "00c0df30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91ad8.md#insn-00a91b24) · [`00a91b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91ad8.md#insn-00a91b68) · [`00a91b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91ad8.md#insn-00a91b04)
- 新版 `00a91b68`（命令位置の公開資料なし） · `00a91bac`（命令位置の公開資料なし） · `00a91b48`（命令位置の公開資料なし）

~~~diff
- 00a91b24 ["INT_ADD", "register:40f0:8", ["const:a91b24:8", "const:4:8"]]
- 00a91b24 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00a91b68 ["INT_ADD", "register:40f0:8", ["const:a91b68:8", "const:4:8"]]
+ 00a91b68 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00a91b24 bytes 13270594
+ 00a91b68 bytes 16270594
- 00a91b68 ["INT_ADD", "register:40f0:8", ["const:a91b68:8", "const:4:8"]]
- 00a91b68 ["CALL", null, ["callee:00883bb8:8"]]
+ 00a91bac ["INT_ADD", "register:40f0:8", ["const:a91bac:8", "const:4:8"]]
+ 00a91bac ["CALL", null, ["callee:00883bb8:8"]]
- 00a91b68 bytes 14c8f797
+ 00a91bac bytes 03c8f797
- 00a91b04 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
- 00a91b04 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a91b48 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ab8:8"]]
+ 00a91b48 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a91b04 bytes 203d45f9
+ 00a91b48 bytes 205d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9e4b8f01005be0148349a4cad34befd"></a>

### [`00a91c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91c88.md) → [`00a91ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91ccc.md) FUN_00a91ccc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a91ce0",
      "incomplete_value": false,
      "site": "00a91ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91c9c",
      "incomplete_value": false,
      "site": "00a91ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "00a91ce4",
      "DATA",
      [
        "storage",
        "00c0ef88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91ce4",
      "DATA",
      [
        "storage",
        "00c0efd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91c88.md#insn-00a91c94) · [`00a91c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91c88.md#insn-00a91c9c)
- 新版 `00a91cd8`（命令位置の公開資料なし） · `00a91ce0`（命令位置の公開資料なし）

~~~diff
- 00a91c94 ["INT_ADD", "register:40f0:8", ["const:a91c94:8", "const:4:8"]]
- 00a91c94 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a91cd8 ["INT_ADD", "register:40f0:8", ["const:a91cd8:8", "const:4:8"]]
+ 00a91cd8 ["CALL", null, ["callee:00bdb040:8"]]
- 00a91c94 bytes d7240594
+ 00a91cd8 bytes da240594
- 00a91c9c ["COPY", "tmp:0:8", ["const:f88:8"]]
- 00a91c9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91c9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91c9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91ce0 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 00a91ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91c9c bytes 08213e91
+ 00a91ce0 bytes 08613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e765fa73f67ce8c42d610fcb4539dd0"></a>

### [`00a91cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91cac.md) → [`00a91cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91cf0.md) FUN_00a91cf0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a91cf4",
      "incomplete_value": false,
      "site": "00a91cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91cb0",
      "incomplete_value": false,
      "site": "00a91cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "00a91cf8",
      "DATA",
      [
        "storage",
        "00c0ef88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91cf8",
      "DATA",
      [
        "storage",
        "00c0efd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91cac.md#insn-00a91cb0)
- 新版 `00a91cf4`（命令位置の公開資料なし）

~~~diff
- 00a91cb0 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 00a91cb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91cb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91cb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91cf4 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 00a91cf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91cf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91cf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91cb0 bytes 08213e91
+ 00a91cf4 bytes 08613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53b92c0cc79960b0c7edffad4e0ac4a5"></a>

### [`00a91d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91d30.md) → [`00a91d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91d74.md) FUN_00a91d74

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a91d88",
      "incomplete_value": false,
      "site": "00a91d8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91d44",
      "incomplete_value": false,
      "site": "00a91d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "00a91d8c",
      "DATA",
      [
        "storage",
        "00c0f008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91d8c",
      "DATA",
      [
        "storage",
        "00c0f058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91d30.md#insn-00a91d3c) · [`00a91d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91d30.md#insn-00a91d44)
- 新版 `00a91d80`（命令位置の公開資料なし） · `00a91d88`（命令位置の公開資料なし）

~~~diff
- 00a91d3c ["INT_ADD", "register:40f0:8", ["const:a91d3c:8", "const:4:8"]]
- 00a91d3c ["CALL", null, ["callee:00bdb040:8"]]
+ 00a91d80 ["INT_ADD", "register:40f0:8", ["const:a91d80:8", "const:4:8"]]
+ 00a91d80 ["CALL", null, ["callee:00bdb040:8"]]
- 00a91d3c bytes ad240594
+ 00a91d80 bytes b0240594
- 00a91d44 ["COPY", "tmp:0:8", ["const:8:8"]]
- 00a91d44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91d44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91d44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91d88 ["COPY", "tmp:0:8", ["const:58:8"]]
+ 00a91d88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91d88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91d88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91d44 bytes 08210091
+ 00a91d88 bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-720520a7bad611a1490b524f14139106"></a>

### [`00a91d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91d54.md) → [`00a91d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91d98.md) FUN_00a91d98

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a91d9c",
      "incomplete_value": false,
      "site": "00a91da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91d58",
      "incomplete_value": false,
      "site": "00a91d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "00a91da0",
      "DATA",
      [
        "storage",
        "00c0f008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91da0",
      "DATA",
      [
        "storage",
        "00c0f058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91d54.md#insn-00a91d58)
- 新版 `00a91d9c`（命令位置の公開資料なし）

~~~diff
- 00a91d58 ["COPY", "tmp:0:8", ["const:8:8"]]
- 00a91d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91d9c ["COPY", "tmp:0:8", ["const:58:8"]]
+ 00a91d9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91d9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91d9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91d58 bytes 08210091
+ 00a91d9c bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49da2a454f29c6386a12d9c64959a319"></a>

### [`00a91dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91dd8.md) → [`00a91e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91e1c.md) FUN_00a91e1c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a91e30",
      "incomplete_value": false,
      "site": "00a91e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91dec",
      "incomplete_value": false,
      "site": "00a91df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:88:8"
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
      "00a91e34",
      "DATA",
      [
        "storage",
        "00c0f088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91e34",
      "DATA",
      [
        "storage",
        "00c0f0d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91dd8.md#insn-00a91de4) · [`00a91dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91dd8.md#insn-00a91dec)
- 新版 `00a91e28`（命令位置の公開資料なし） · `00a91e30`（命令位置の公開資料なし）

~~~diff
- 00a91de4 ["INT_ADD", "register:40f0:8", ["const:a91de4:8", "const:4:8"]]
- 00a91de4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a91e28 ["INT_ADD", "register:40f0:8", ["const:a91e28:8", "const:4:8"]]
+ 00a91e28 ["CALL", null, ["callee:00bdb040:8"]]
- 00a91de4 bytes 83240594
+ 00a91e28 bytes 86240594
- 00a91dec ["COPY", "tmp:0:8", ["const:88:8"]]
- 00a91dec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91dec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91dec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91e30 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 00a91e30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91e30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91e30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91dec bytes 08210291
+ 00a91e30 bytes 08610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41224f180d346debc4f77bf863b46d30"></a>

### [`00a91dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91dfc.md) → [`00a91e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91e40.md) FUN_00a91e40

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a91e44",
      "incomplete_value": false,
      "site": "00a91e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91e00",
      "incomplete_value": false,
      "site": "00a91e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:88:8"
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
      "00a91e48",
      "DATA",
      [
        "storage",
        "00c0f088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91e48",
      "DATA",
      [
        "storage",
        "00c0f0d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91dfc.md#insn-00a91e00)
- 新版 `00a91e44`（命令位置の公開資料なし）

~~~diff
- 00a91e00 ["COPY", "tmp:0:8", ["const:88:8"]]
- 00a91e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91e44 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 00a91e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91e00 bytes 08210291
+ 00a91e44 bytes 08610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-626d8637845e6ef39c6c715dd3b24a56"></a>

### [`00a91f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91f30.md) → [`00a91f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91f74.md) FUN_00a91f74

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a91f88",
      "incomplete_value": false,
      "site": "00a91f8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91f44",
      "incomplete_value": false,
      "site": "00a91f48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "00a91f8c",
      "DATA",
      [
        "storage",
        "00c0f108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91f8c",
      "DATA",
      [
        "storage",
        "00c0f158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91f30.md#insn-00a91f3c) · [`00a91f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91f30.md#insn-00a91f44)
- 新版 `00a91f80`（命令位置の公開資料なし） · `00a91f88`（命令位置の公開資料なし）

~~~diff
- 00a91f3c ["INT_ADD", "register:40f0:8", ["const:a91f3c:8", "const:4:8"]]
- 00a91f3c ["CALL", null, ["callee:00bdb040:8"]]
+ 00a91f80 ["INT_ADD", "register:40f0:8", ["const:a91f80:8", "const:4:8"]]
+ 00a91f80 ["CALL", null, ["callee:00bdb040:8"]]
- 00a91f3c bytes 2d240594
+ 00a91f80 bytes 30240594
- 00a91f44 ["COPY", "tmp:0:8", ["const:108:8"]]
- 00a91f44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91f44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91f44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91f88 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 00a91f88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91f88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91f88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91f44 bytes 08210491
+ 00a91f88 bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf39f5ee7f0edcf44f1d741c1356789b"></a>

### [`00a91f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91f54.md) → [`00a91f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91f98.md) FUN_00a91f98

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a91f9c",
      "incomplete_value": false,
      "site": "00a91fa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91f58",
      "incomplete_value": false,
      "site": "00a91f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "00a91fa0",
      "DATA",
      [
        "storage",
        "00c0f108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91fa0",
      "DATA",
      [
        "storage",
        "00c0f158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91f54.md#insn-00a91f58)
- 新版 `00a91f9c`（命令位置の公開資料なし）

~~~diff
- 00a91f58 ["COPY", "tmp:0:8", ["const:108:8"]]
- 00a91f58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91f58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91f58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91f9c ["COPY", "tmp:0:8", ["const:158:8"]]
+ 00a91f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91f58 bytes 08210491
+ 00a91f9c bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57cdec0f382033388a6ed45d8043b5fe"></a>

### [`00a9204c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a9204c.md) → [`00a92090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a92/00a92090.md) FUN_00a92090

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a920b0",
      "incomplete_value": false,
      "site": "00a920b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a9206c",
      "incomplete_value": false,
      "site": "00a92070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "00a920b4",
      "DATA",
      [
        "storage",
        "00c0f188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a920b4",
      "DATA",
      [
        "storage",
        "00c0f1d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a92060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a9204c.md#insn-00a92060) · [`00a9206c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a9204c.md#insn-00a9206c)
- 新版 `00a920a4`（命令位置の公開資料なし） · `00a920b0`（命令位置の公開資料なし）

~~~diff
- 00a92060 ["INT_ADD", "register:40f0:8", ["const:a92060:8", "const:4:8"]]
- 00a92060 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a920a4 ["INT_ADD", "register:40f0:8", ["const:a920a4:8", "const:4:8"]]
+ 00a920a4 ["CALL", null, ["callee:00bdb040:8"]]
- 00a92060 bytes e4230594
+ 00a920a4 bytes e7230594
- 00a9206c ["COPY", "tmp:0:8", ["const:188:8"]]
- 00a9206c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a9206c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a9206c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a920b0 ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 00a920b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a920b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a920b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a9206c bytes 08210691
+ 00a920b0 bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1df62d254119805803a64e98f2dc99d"></a>

### [`00a92084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92084.md) → [`00a920c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a92/00a920c8.md) FUN_00a920c8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a920cc",
      "incomplete_value": false,
      "site": "00a920d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a92088",
      "incomplete_value": false,
      "site": "00a9208c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "00a920d0",
      "DATA",
      [
        "storage",
        "00c0f188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a920d0",
      "DATA",
      [
        "storage",
        "00c0f1d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a92088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92084.md#insn-00a92088)
- 新版 `00a920cc`（命令位置の公開資料なし）

~~~diff
- 00a92088 ["COPY", "tmp:0:8", ["const:188:8"]]
- 00a92088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a92088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a92088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a920cc ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 00a920cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a920cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a920cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a92088 bytes 08210691
+ 00a920cc bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9392da5fdc135501d46264e4f1d9c27c"></a>

### [`00a920a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a920a4.md) → [`00a920e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a92/00a920e8.md) FUN_00a920e8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.19% / 新版 97.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a9241c",
      "incomplete_value": true,
      "site": "00a9241c",
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
      "definition_site": "00a923d8",
      "incomplete_value": true,
      "site": "00a923d8",
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a922f4",
      "incomplete_value": true,
      "site": "00a92304",
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a922b0",
      "incomplete_value": true,
      "site": "00a922c0",
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a92318",
      "incomplete_value": true,
      "site": "00a92334",
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a922d4",
      "incomplete_value": true,
      "site": "00a922f0",
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a922f4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a922f8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a922fc",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a922f4",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a922f8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a922fc",
      "PARAM",
      [
        "storage",
        "00c0df30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a922ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a920a4.md#insn-00a922ac) · [`00a922c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a920a4.md#insn-00a922c0) · [`00a922f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a920a4.md#insn-00a922f0)
- 新版 `00a922f0`（命令位置の公開資料なし） · `00a92304`（命令位置の公開資料なし） · `00a92334`（命令位置の公開資料なし）

~~~diff
- 00a922ac ["INT_ADD", "register:40f0:8", ["const:a922ac:8", "const:4:8"]]
- 00a922ac ["CALL", null, ["callee:0044507c:8"]]
+ 00a922f0 ["INT_ADD", "register:40f0:8", ["const:a922f0:8", "const:4:8"]]
+ 00a922f0 ["CALL", null, ["callee:0044507c:8"]]
- 00a922ac bytes 74cbe697
+ 00a922f0 bytes 63cbe697
- 00a922c0 ["INT_ADD", "register:40f0:8", ["const:a922c0:8", "const:4:8"]]
- 00a922c0 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00a92304 ["INT_ADD", "register:40f0:8", ["const:a92304:8", "const:4:8"]]
+ 00a92304 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00a922c0 bytes 2c250594
+ 00a92304 bytes 2f250594
- 00a922f0 ["INT_ADD", "register:40f0:8", ["const:a922f0:8", "const:4:8"]]
- 00a922f0 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00a92334 ["INT_ADD", "register:40f0:8", ["const:a92334:8", "const:4:8"]]
+ 00a92334 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00a922f0 bytes 20250594
+ 00a92334 bytes 23250594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-272cc10195e3e04235e260c2c6c9d34a"></a>

### [`00a92660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92660.md) → [`00a926a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a92/00a926a4.md) FUN_00a926a4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00a926b8",
      "incomplete_value": false,
      "site": "00a926bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a92674",
      "incomplete_value": false,
      "site": "00a92678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "00a926bc",
      "DATA",
      [
        "storage",
        "00c0f208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a926bc",
      "DATA",
      [
        "storage",
        "00c0f258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9266c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92660.md#insn-00a9266c) · [`00a92674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92660.md#insn-00a92674)
- 新版 `00a926b0`（命令位置の公開資料なし） · `00a926b8`（命令位置の公開資料なし）

~~~diff
- 00a9266c ["INT_ADD", "register:40f0:8", ["const:a9266c:8", "const:4:8"]]
- 00a9266c ["CALL", null, ["callee:00bdb040:8"]]
+ 00a926b0 ["INT_ADD", "register:40f0:8", ["const:a926b0:8", "const:4:8"]]
+ 00a926b0 ["CALL", null, ["callee:00bdb040:8"]]
- 00a9266c bytes 61220594
+ 00a926b0 bytes 64220594
- 00a92674 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00a92674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a92674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a92674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a926b8 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 00a926b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a926b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a926b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a92674 bytes 08210891
+ 00a926b8 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1cfc2c95ed818285512eede22618e2b"></a>

### [`00a92684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92684.md) → [`00a926c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a92/00a926c8.md) FUN_00a926c8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a926cc",
      "incomplete_value": false,
      "site": "00a926d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a92688",
      "incomplete_value": false,
      "site": "00a9268c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "00a926d0",
      "DATA",
      [
        "storage",
        "00c0f208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a926d0",
      "DATA",
      [
        "storage",
        "00c0f258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a92688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92684.md#insn-00a92688)
- 新版 `00a926cc`（命令位置の公開資料なし）

~~~diff
- 00a92688 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00a92688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a92688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a92688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a926cc ["COPY", "tmp:0:8", ["const:258:8"]]
+ 00a926cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a926cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a926cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a92688 bytes 08210891
+ 00a926cc bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6ff2a7c7f9e9262074593b95a676f4b"></a>

### [`00a92704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92704.md) → [`00a92748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a92/00a92748.md) _INIT_240

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
      "definition_site": "00a92784",
      "incomplete_value": true,
      "site": "00a927a0",
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
      "definition_site": "00a92740",
      "incomplete_value": true,
      "site": "00a9275c",
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
      "definition_site": "00a927a8",
      "incomplete_value": true,
      "site": "00a927c4",
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
      "definition_site": "00a92764",
      "incomplete_value": true,
      "site": "00a92780",
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
      "definition_site": "00a927c8",
      "incomplete_value": true,
      "site": "00a927e4",
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
      "definition_site": "00a92784",
      "incomplete_value": true,
      "site": "00a927a0",
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
      "00a92784",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a927a8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a927c8",
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
      "00a92784",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00a927a8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00a927c8",
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

- 旧版 [`00a9273c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92704.md#insn-00a9273c) · [`00a92864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92704.md#insn-00a92864) · [`00a92938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92704.md#insn-00a92938)
- 新版 `00a92780`（命令位置の公開資料なし） · `00a928a8`（命令位置の公開資料なし） · `00a9297c`（命令位置の公開資料なし）

~~~diff
- 00a9273c ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00a9273c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a9273c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a9273c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a92780 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00a92780 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a92780 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a92780 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a9273c bytes 29750b91
+ 00a92780 bytes 29dd0d91
- 00a92864 ["INT_ADD", "register:40f0:8", ["const:a92864:8", "const:4:8"]]
- 00a92864 ["CALL", null, ["callee:00418cb8:8"]]
+ 00a928a8 ["INT_ADD", "register:40f0:8", ["const:a928a8:8", "const:4:8"]]
+ 00a928a8 ["CALL", null, ["callee:00418cb8:8"]]
- 00a92864 bytes 1519e697
+ 00a928a8 bytes 0419e697
- 00a92938 ["INT_ADD", "register:40f0:8", ["const:a92938:8", "const:4:8"]]
- 00a92938 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00a9297c ["INT_ADD", "register:40f0:8", ["const:a9297c:8", "const:4:8"]]
+ 00a9297c ["CALL", null, ["callee:00bdafe0:8"]]
- 00a92938 bytes 96210594
+ 00a9297c bytes 99210594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1347b72dfefdea992fcd6625599aed57"></a>

### [`00a92a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92a94.md) → [`00a92ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a92/00a92ad8.md) _INIT_241

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
      "definition_site": "00a92b14",
      "incomplete_value": true,
      "site": "00a92b30",
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
      "definition_site": "00a92ad0",
      "incomplete_value": true,
      "site": "00a92aec",
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
      "definition_site": "00a92b38",
      "incomplete_value": true,
      "site": "00a92b54",
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
      "definition_site": "00a92af4",
      "incomplete_value": true,
      "site": "00a92b10",
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
      "definition_site": "00a92b58",
      "incomplete_value": true,
      "site": "00a92b74",
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
      "definition_site": "00a92b14",
      "incomplete_value": true,
      "site": "00a92b30",
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
      "00a92b14",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a92b38",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a92b58",
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
      "00a92b14",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00a92b38",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00a92b58",
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

- 旧版 [`00a92acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92a94.md#insn-00a92acc) · [`00a92bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92a94.md#insn-00a92bf4) · [`00a92cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92a94.md#insn-00a92cc8)
- 新版 `00a92b10`（命令位置の公開資料なし） · `00a92c38`（命令位置の公開資料なし） · `00a92d0c`（命令位置の公開資料なし）

~~~diff
- 00a92acc ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00a92acc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a92acc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a92acc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a92b10 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00a92b10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a92b10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a92b10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a92acc bytes 29750b91
+ 00a92b10 bytes 29dd0d91
- 00a92bf4 ["INT_ADD", "register:40f0:8", ["const:a92bf4:8", "const:4:8"]]
- 00a92bf4 ["CALL", null, ["callee:00418cb8:8"]]
+ 00a92c38 ["INT_ADD", "register:40f0:8", ["const:a92c38:8", "const:4:8"]]
+ 00a92c38 ["CALL", null, ["callee:00418cb8:8"]]
- 00a92bf4 bytes 3118e697
+ 00a92c38 bytes 2018e697
- 00a92cc8 ["INT_ADD", "register:40f0:8", ["const:a92cc8:8", "const:4:8"]]
- 00a92cc8 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00a92d0c ["INT_ADD", "register:40f0:8", ["const:a92d0c:8", "const:4:8"]]
+ 00a92d0c ["CALL", null, ["callee:00bdafe0:8"]]
- 00a92cc8 bytes b2200594
+ 00a92d0c bytes b5200594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daf7c9b1a60522ca57e29ee09a910e1e"></a>

### [`00a93074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93074.md) → [`00a930b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a930b8.md) FUN_00a930b8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`005d1f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d1/005d1f2c.md) [`005d8f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d8/005d8f58.md) [`006eb464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md) [`009eadc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ea/009eadc8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 4件 [`005d1f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d1/005d1f2c.md) [`005d8f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d8/005d8f58.md) [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00a930dc",
      "incomplete_value": true,
      "site": "00a930e8",
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
    "old": null,
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a93084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93074.md#insn-00a93084)
- 新版 `00a930c8`（命令位置の公開資料なし）

~~~diff
- 00a93084 ["INT_ADD", "register:40f0:8", ["const:a93084:8", "const:4:8"]]
- 00a93084 ["CALL", null, ["callee:0081f580:8"]]
+ 00a930c8 ["INT_ADD", "register:40f0:8", ["const:a930c8:8", "const:4:8"]]
+ 00a930c8 ["CALL", null, ["callee:0081f580:8"]]
- 00a93084 bytes 3f31f697
+ 00a930c8 bytes 2e31f697
~~~


<a id="compare-86b385d1a6c0efcdcdafc8148994a85f"></a>

### [`00a93210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93210.md) → [`00a93254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93254.md) FUN_00a93254

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) [`009eadc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ea/009eadc8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a93210"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a93210"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a93214"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a93210",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a93214",
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
      "00a93254",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a93258",
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

- 旧版 [`00a93210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93210.md#insn-00a93210) · [`00a93214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93210.md#insn-00a93214)
- 新版 `00a93254`（命令位置の公開資料なし）

~~~diff
- 00a93210 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a93210 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a93210 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a93210 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a93210 bytes fd7bbea9
- 00a93214 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a93214 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a93214 bytes f30b00f9
+ 00a93254 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00a93254 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00a93254 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00a93254 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00a93254 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7fef807933ab28059572a7d22e468a6"></a>

### [`00a93320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93320.md) → [`00a93364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93364.md) FUN_00a93364

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 6件 [`005d6740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6740.md) [`005d6c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6c3c.md) [`005d76a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d7/005d76a0.md) [`005d8f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d8/005d8f58.md) [`006eb464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 6件 [`005d6740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6740.md) [`005d6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6c3c.md) [`005d76a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d7/005d76a0.md) [`005d8f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d8/005d8f58.md) [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a93330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93320.md#insn-00a93330)
- 新版 `00a93374`（命令位置の公開資料なし）

~~~diff
- 00a93330 ["INT_ADD", "register:40f0:8", ["const:a93330:8", "const:4:8"]]
- 00a93330 ["CALL", null, ["callee:0081f580:8"]]
+ 00a93374 ["INT_ADD", "register:40f0:8", ["const:a93374:8", "const:4:8"]]
+ 00a93374 ["CALL", null, ["callee:0081f580:8"]]
- 00a93330 bytes 9430f697
+ 00a93374 bytes 8330f697
~~~


<a id="compare-f08091ba08abf1d4059eaede81cc481e"></a>

### [`00a93354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93354.md) → [`00a93398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93398.md) FUN_00a93398

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009eadc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ea/009eadc8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a93368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93354.md#insn-00a93368)
- 新版 `00a933ac`（命令位置の公開資料なし）

~~~diff
- 00a93368 ["INT_ADD", "register:40f0:8", ["const:a93368:8", "const:4:8"]]
- 00a93368 ["CALL", null, ["callee:0081f580:8"]]
+ 00a933ac ["INT_ADD", "register:40f0:8", ["const:a933ac:8", "const:4:8"]]
+ 00a933ac ["CALL", null, ["callee:0081f580:8"]]
- 00a93368 bytes 8630f697
+ 00a933ac bytes 7530f697
~~~


<a id="compare-f1a261472bcba821e4185ecfaf1fae9b"></a>

### [`00a933c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a933c0.md) → [`00a93404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93404.md) FUN_00a93404

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`005d8f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d8/005d8f58.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`005d8f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d8/005d8f58.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a933d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a933c0.md#insn-00a933d4)
- 新版 `00a93418`（命令位置の公開資料なし）

~~~diff
- 00a933d4 ["INT_ADD", "register:40f0:8", ["const:a933d4:8", "const:4:8"]]
- 00a933d4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a93418 ["INT_ADD", "register:40f0:8", ["const:a93418:8", "const:4:8"]]
+ 00a93418 ["CALL", null, ["callee:0081f580:8"]]
- 00a933d4 bytes 6b30f697
+ 00a93418 bytes 5a30f697
~~~


<a id="compare-c8363474deae7db57a0b61213e680f24"></a>

### [`00a9342c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a9342c.md) → [`00a93470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93470.md) FUN_00a93470

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009eadc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ea/009eadc8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a93440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a9342c.md#insn-00a93440)
- 新版 `00a93484`（命令位置の公開資料なし）

~~~diff
- 00a93440 ["INT_ADD", "register:40f0:8", ["const:a93440:8", "const:4:8"]]
- 00a93440 ["CALL", null, ["callee:0081f580:8"]]
+ 00a93484 ["INT_ADD", "register:40f0:8", ["const:a93484:8", "const:4:8"]]
+ 00a93484 ["CALL", null, ["callee:0081f580:8"]]
- 00a93440 bytes 5030f697
+ 00a93484 bytes 3f30f697
~~~


