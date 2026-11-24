# v16.0.1 → v16.0.2 · 命令位置の検査未完了 (3)

[一覧の目次](README.md)

<a id="compare-733f9bb88fce8e9589c55282b3995311"></a>

### [`007877fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007877fc.md) → [`00787854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787854.md) FUN_00787854

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007883b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/007883b8.md) · 呼出先 10件 [`0078603c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078603c.md) [`00786ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/00786ba8.md) [`00787480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787480.md) [`00787518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787518.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md)
- 新版 呼出元 1件 [`00788410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/00788410.md) · 呼出先 10件 [`00786094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00786/00786094.md) [`00786c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00786/00786c00.md) [`007874d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/007874d8.md) [`00787570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787570.md) [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md)

変更の種類 call, call_argument_candidate, call_target, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.93% / 新版 95.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078792c",
      "value": [
        "leaf",
        "ram:a65e5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007878d4",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0078791c",
      "incomplete_value": true,
      "site": "0078792c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40c8:4"
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
      "definition_site": "00787918",
      "incomplete_value": true,
      "site": "0078792c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "INT_SUB",
            "4",
            [
              [
                "live",
                "register:4000:4"
              ],
              [
                "leaf",
                "const:1:4"
              ]
            ]
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0078792c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ],
  "added": [
    [
      "0078792c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65e5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078787c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007877fc.md#insn-0078787c) · [`007878d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007877fc.md#insn-007878d4) · [`007878f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007877fc.md#insn-007878f0)
- 新版 `007878d4`（命令位置の公開資料なし） · `0078792c`（命令位置の公開資料なし） · `00787948`（命令位置の公開資料なし）

~~~diff
- 0078787c ["INT_ADD", "register:40f0:8", ["const:78787c:8", "const:4:8"]]
- 0078787c ["CALL", null, ["callee:007874d8:8"]]
+ 007878d4 ["INT_ADD", "register:40f0:8", ["const:7878d4:8", "const:4:8"]]
+ 007878d4 ["CALL", null, ["callee:007874d8:8"]]
- 0078787c bytes 01ffff97
+ 007878d4 bytes 01ffff97
- 007878d4 ["INT_ADD", "register:40f0:8", ["const:7878d4:8", "const:4:8"]]
- 007878d4 ["CALL", null, ["ram:a65dec:8"]]
+ 0078792c ["INT_ADD", "register:40f0:8", ["const:78792c:8", "const:4:8"]]
+ 0078792c ["CALL", null, ["ram:a65e5c:8"]]
- 007878d4 bytes 46790b94
+ 0078792c bytes 4c790b94
- 007878f0 ["INT_ADD", "register:40f0:8", ["const:7878f0:8", "const:4:8"]]
- 007878f0 ["CALL", null, ["callee:00787570:8"]]
+ 00787948 ["INT_ADD", "register:40f0:8", ["const:787948:8", "const:4:8"]]
+ 00787948 ["CALL", null, ["callee:00787570:8"]]
- 007878f0 bytes 0affff97
+ 00787948 bytes 0affff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47af2cf06b55017d740478332d0f7cfd"></a>

### [`007879e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007879e8.md) → [`00787a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787a40.md) FUN_00787a40

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00787b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787b20.md) [`00788534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788534.md) · 呼出先 3件 [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b6f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f40.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 3件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`00787b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787b78.md) [`0078858c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/0078858c.md) · 呼出先 3件 [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b6f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f98.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 28.21% / 新版 28.21%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 17件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00787a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00787a98"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00787ad8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00787a04",
      "READ",
      [
        "storage",
        "00ca3f0c",
        null,
        "undefined4"
      ]
    ],
    [
      "00787a70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00787a44"
      ]
    ],
    [
      "unmatched:00787a24",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b7a20"
      ]
    ]
  ],
  "added": [
    [
      "00787a5c",
      "READ",
      [
        "storage",
        "00ca3fdc",
        null,
        "undefined4"
      ]
    ],
    [
      "00787a70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00787a9c"
      ]
    ],
    [
      "00787a7c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b7a20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00787a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007879e8.md#insn-00787a14) · [`00787a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007879e8.md#insn-00787a24) · [`00787a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007879e8.md#insn-00787a2c)
- 新版 `00787a6c`（命令位置の公開資料なし）

~~~diff
- 00787a14 ["INT_ADD", "register:40f0:8", ["const:787a14:8", "const:4:8"]]
- 00787a14 ["CALL", null, ["callee:008b7a20:8"]]
+ 00787a6c ["INT_ADD", "register:40f0:8", ["const:787a6c:8", "const:4:8"]]
+ 00787a6c ["CALL", null, ["callee:008b7a20:8"]]
- 00787a14 bytes edbf0494
+ 00787a6c bytes edbf0494
- 00787a24 ["INT_ADD", "register:40f0:8", ["const:787a24:8", "const:4:8"]]
- 00787a24 ["CALL", null, ["callee:008b7a20:8"]]
- 00787a24 bytes e9bf0494
- 00787a2c ["INT_ADD", "register:40f0:8", ["const:787a2c:8", "const:4:8"]]
- 00787a2c ["CALL", null, ["callee:008b6f98:8"]]
- 00787a2c bytes 45bd0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c73ca5c227869d8a177c6565bbf7358"></a>

### [`00787f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787f04.md) → [`00787f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787f5c.md) FUN_00787f5c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00787db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787db4.md) · 呼出先 3件 [`00467af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467af0.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md)
- 新版 呼出元 1件 [`00787e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787e0c.md) · 呼出先 3件 [`00467b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b30.md) [`00468c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468c1c.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.53% / 新版 97.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00787fec",
      "incomplete_value": true,
      "site": "0078800c",
      "value": [
        "live",
        "register:40a0:8"
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
      "definition_site": "00787ff0",
      "incomplete_value": true,
      "site": "0078800c",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00787ff4",
      "incomplete_value": true,
      "site": "0078800c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40b8:4"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00787fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787f04.md#insn-00787fb4) · [`0078800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787f04.md#insn-0078800c) · [`00788018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787f04.md#insn-00788018)
- 新版 `0078800c`（命令位置の公開資料なし） · `00788064`（命令位置の公開資料なし） · `00788070`（命令位置の公開資料なし）

~~~diff
- 00787fb4 ["INT_ADD", "register:40f0:8", ["const:787fb4:8", "const:4:8"]]
- 00787fb4 ["CALL", null, ["callee:00469c44:8"]]
+ 0078800c ["INT_ADD", "register:40f0:8", ["const:78800c:8", "const:4:8"]]
+ 0078800c ["CALL", null, ["callee:00469c44:8"]]
- 00787fb4 bytes 1487f397
+ 0078800c bytes 0e87f397
- 0078800c ["INT_ADD", "register:40f0:8", ["const:78800c:8", "const:4:8"]]
- 0078800c ["CALL", null, ["callee:00469c44:8"]]
+ 00788064 ["INT_ADD", "register:40f0:8", ["const:788064:8", "const:4:8"]]
+ 00788064 ["CALL", null, ["callee:00469c44:8"]]
- 0078800c bytes fe86f397
+ 00788064 bytes f886f397
- 00788018 ["INT_ADD", "register:40f0:8", ["const:788018:8", "const:4:8"]]
- 00788018 ["CALL", null, ["callee:00468c1c:8"]]
+ 00788070 ["INT_ADD", "register:40f0:8", ["const:788070:8", "const:4:8"]]
+ 00788070 ["CALL", null, ["callee:00468c1c:8"]]
- 00788018 bytes f182f397
+ 00788070 bytes eb82f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3065210a0e05622a90ac970710c1dedd"></a>

### [`00788060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788060.md) → [`007880b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/007880b8.md) FUN_007880b8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00764acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764acc.md) · 呼出先 2件 [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00764b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764b24.md) · 呼出先 2件 [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 56.25% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "007880e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0078813c"
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
      "unmatched:007880e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078814c"
      ]
    ]
  ],
  "added": [
    [
      "0078813c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078814c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007880e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788060.md#insn-007880e4) · [`0078809c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788060.md#insn-0078809c)
- 新版 `0078813c`（命令位置の公開資料なし） · `007880f4`（命令位置の公開資料なし）

~~~diff
- 007880e4 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 007880e4 bytes 80000054
+ 0078813c ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
+ 0078813c bytes 80000054
- 0078809c ["COPY", "register:0:8", ["register:4048:8"]]
- 0078809c ["INT_ADD", "register:40f0:8", ["const:78809c:8", "const:4:8"]]
- 0078809c ["CALLIND", null, ["register:0:8"]]
+ 007880f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 007880f4 ["INT_ADD", "register:40f0:8", ["const:7880f4:8", "const:4:8"]]
+ 007880f4 ["CALLIND", null, ["register:0:8"]]
- 0078809c bytes 20013fd6
+ 007880f4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4ab7f8c32c35e739fc9d6f31a72344c"></a>

### [`0078812c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/0078812c.md) → [`00788184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/00788184.md) FUN_00788184

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00764acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764acc.md) · 呼出先 2件 [`007887b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/007887b4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00764b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764b24.md) · 呼出先 2件 [`0078880c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/0078880c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.43% / 新版 78.43%

CFGの説明率　旧版 36.84% / 新版 38.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00788130"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00788130"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00788134"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00788130",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00788134",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00788148",
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
      "00788188",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0078818c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "007881a0",
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

- 旧版 [`00788130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/0078812c.md#insn-00788130) · [`00788134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/0078812c.md#insn-00788134) · [`00788148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/0078812c.md#insn-00788148)

~~~diff
- 00788130 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00788130 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00788130 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00788130 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00788130 bytes fd7b04a9
- 00788134 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00788134 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00788134 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00788134 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00788134 bytes f44f05a9
- 00788148 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00788148 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00788148 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00788148 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a27ed0b5cde361c1e85b988ad7775822"></a>

### [`0078824c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/0078824c.md) → [`007882a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/007882a4.md) FUN_007882a4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a468d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468d8.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`00a4692c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a4692c.md)

変更の種類 call, call_argument_candidate, call_target, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00788250"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00788250"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007882a8"
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
      "unmatched:00788250",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0078832c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00788338",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007882a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0078832c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00788338",
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

- 旧版 [`00788250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/0078824c.md#insn-00788250) · [`00788268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/0078824c.md#insn-00788268)
- 新版 `007882c0`（命令位置の公開資料なし） · `007882a8`（命令位置の公開資料なし）

~~~diff
- 00788250 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00788250 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00788250 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00788250 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00788250 bytes f44f01a9
- 00788268 ["INT_ADD", "register:40f0:8", ["const:788268:8", "const:4:8"]]
- 00788268 ["CALL", null, ["callee:008b6efc:8"]]
+ 007882c0 ["INT_ADD", "register:40f0:8", ["const:7882c0:8", "const:4:8"]]
+ 007882c0 ["CALL", null, ["callee:008b6efc:8"]]
- 00788268 bytes 0fbb0494
+ 007882c0 bytes 0fbb0494
+ 007882a8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 007882a8 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 007882a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 007882a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 007882a8 bytes f44f01a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26579db4e613cab18c95152dece463ca"></a>

### [`007887b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/007887b4.md) → [`0078880c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/0078880c.md) FUN_0078880c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0078812c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/0078812c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00788184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/00788184.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call, call_argument_candidate, call_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.38% / 新版 94.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00788850"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007888a0",
      "incomplete_value": true,
      "site": "007888a8",
      "value": [
        "live",
        "register:4098:8"
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
      "definition_site": "007888a4",
      "incomplete_value": true,
      "site": "007888a8",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:00788850",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:007888d8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "007888b8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00788930",
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

- 旧版 [`00788850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/007887b4.md#insn-00788850) · [`00788860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/007887b4.md#insn-00788860)
- 新版 `007888a8`（命令位置の公開資料なし） · `007888b8`（命令位置の公開資料なし）

~~~diff
- 00788850 ["COPY", "register:0:8", ["register:4040:8"]]
- 00788850 ["INT_ADD", "register:40f0:8", ["const:788850:8", "const:4:8"]]
- 00788850 ["CALLIND", null, ["register:0:8"]]
- 00788850 bytes 00013fd6
- 00788860 ["COPY", "register:0:8", ["register:4040:8"]]
- 00788860 ["INT_ADD", "register:40f0:8", ["const:788860:8", "const:4:8"]]
- 00788860 ["CALLIND", null, ["register:0:8"]]
+ 007888a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007888a8 ["INT_ADD", "register:40f0:8", ["const:7888a8:8", "const:4:8"]]
+ 007888a8 ["CALLIND", null, ["register:0:8"]]
- 00788860 bytes 00013fd6
+ 007888a8 bytes 00013fd6
+ 007888b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007888b8 ["INT_ADD", "register:40f0:8", ["const:7888b8:8", "const:4:8"]]
+ 007888b8 ["CALLIND", null, ["register:0:8"]]
+ 007888b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6fb267313f97392b18270e2428ea414"></a>

### [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) → [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) FUN_00800244

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 50件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`006c03ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c03ac.md) · 呼出先 0件 
- 新版 呼出元 50件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`0060e104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060e/0060e104.md) [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`006c0404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0404.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.70% / 新版 95.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00800260",
      "DATA",
      [
        "storage",
        "002ec8e4",
        "switchD_00800210::switchdataD_002ec8e4",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00800260",
      "DATA",
      [
        "storage",
        "002ec924",
        "switchD_00800268::switchdataD_002ec924",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008001fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md#insn-008001fc) · [`00800204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md#insn-00800204)
- 新版 `00800254`（命令位置の公開資料なし） · `0080025c`（命令位置の公開資料なし）

~~~diff
- 008001fc ["COPY", "tmp:0:8", ["const:8e4:8"]]
- 008001fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008001fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008001fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00800254 ["COPY", "tmp:0:8", ["const:924:8"]]
+ 00800254 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00800254 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00800254 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008001fc bytes 29912391
+ 00800254 bytes 29912491
- 00800204 ["COPY", "register:4050:8", ["const:800214:8"]]
- 00800204 bytes 8a000010
+ 0080025c ["COPY", "register:4050:8", ["const:80026c:8"]]
+ 0080025c bytes 8a000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fab6a780995e3fd45938a25be168050"></a>

### [`00800678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800678.md) → [`008006d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008006d0.md) FUN_008006d0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00aa3e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa3/00aa3e24.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`00aa3e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa3/00aa3e94.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008006e8",
      "DATA",
      [
        "storage",
        "002ec903",
        "switchD_00800698::switchdataD_002ec903",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "008006e8",
      "DATA",
      [
        "storage",
        "002ec943",
        "switchD_008006f0::switchdataD_002ec943",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00800688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800678.md#insn-00800688) · [`0080068c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800678.md#insn-0080068c)
- 新版 `008006e0`（命令位置の公開資料なし） · `008006e4`（命令位置の公開資料なし）

~~~diff
- 00800688 ["COPY", "tmp:0:8", ["const:903:8"]]
- 00800688 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00800688 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00800688 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008006e0 ["COPY", "tmp:0:8", ["const:943:8"]]
+ 008006e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008006e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008006e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00800688 bytes 4a0d2491
+ 008006e0 bytes 4a0d2591
- 0080068c ["COPY", "register:4058:8", ["const:80069c:8"]]
- 0080068c bytes 8b000010
+ 008006e4 ["COPY", "register:4058:8", ["const:8006f4:8"]]
+ 008006e4 bytes 8b000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9419b80a873456f8fa63d9b37091cd38"></a>

### [`008007c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008007c0.md) → [`00800818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800818.md) FUN_00800818

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00729108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00729/00729108.md) [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`00a52e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a52/00a52e30.md) · 呼出先 0件 
- 新版 呼出元 3件 [`00729160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00729/00729160.md) [`007b0a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0a70.md) [`00a52ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a52/00a52ea0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.85% / 新版 93.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00800834",
      "DATA",
      [
        "storage",
        "002ec922",
        "switchD_008007e4::switchdataD_002ec922",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00800834",
      "DATA",
      [
        "storage",
        "002ec962",
        "switchD_0080083c::switchdataD_002ec962",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008007d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008007c0.md#insn-008007d4) · [`008007d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008007c0.md#insn-008007d8)
- 新版 `0080082c`（命令位置の公開資料なし） · `00800830`（命令位置の公開資料なし）

~~~diff
- 008007d4 ["COPY", "tmp:0:8", ["const:922:8"]]
- 008007d4 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 008007d4 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 008007d4 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 0080082c ["COPY", "tmp:0:8", ["const:962:8"]]
+ 0080082c ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 0080082c ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 0080082c ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 008007d4 bytes 6b892491
+ 0080082c bytes 6b892591
- 008007d8 ["COPY", "register:4060:8", ["const:8007e8:8"]]
- 008007d8 bytes 8c000010
+ 00800830 ["COPY", "register:4060:8", ["const:800840:8"]]
+ 00800830 bytes 8c000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfa544593814e34d016e0ae945908768"></a>

### [`00805bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805bf4.md) → [`00805c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00805/00805c4c.md) FUN_00805c4c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0072c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c84c.md) [`0072f1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072f/0072f1d8.md) [`0073180c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/0073180c.md) [`00a87ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a87/00a87ad0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 4件 [`0072c8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072c/0072c8a4.md) [`0072f230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072f/0072f230.md) [`00731864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731864.md) [`00a87b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a87/00a87b40.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00805c78",
      "DATA",
      [
        "storage",
        "002ec9e3",
        "switchD_00805c2c::switchdataD_002ec9e3",
        "byte"
      ]
    ],
    [
      "00805d3c",
      "DATA",
      [
        "storage",
        "0038b098",
        null,
        "byte[27]"
      ]
    ],
    [
      "00805d3c",
      "DATA",
      [
        "storage",
        "0038a8c8",
        null,
        "byte[23]"
      ]
    ]
  ],
  "added": [
    [
      "00805c78",
      "DATA",
      [
        "storage",
        "002eca23",
        "switchD_00805c84::switchdataD_002eca23",
        "byte"
      ]
    ],
    [
      "00805d3c",
      "DATA",
      [
        "storage",
        "0038b098",
        null,
        "byte[39]"
      ]
    ],
    [
      "00805d3c",
      "DATA",
      [
        "storage",
        "0038a8c8",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00805c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805bf4.md#insn-00805c14) · [`00805c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805bf4.md#insn-00805c1c) · [`00805c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805bf4.md#insn-00805c34)
- 新版 `00805c6c`（命令位置の公開資料なし） · `00805c8c`（命令位置の公開資料なし）

~~~diff
- 00805c14 ["COPY", "tmp:0:8", ["const:9e3:8"]]
- 00805c14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00805c14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00805c14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00805c6c ["COPY", "tmp:0:8", ["const:a23:8"]]
+ 00805c6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00805c6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00805c6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00805c14 bytes 298d2791
+ 00805c6c bytes 298d2891
- 00805c1c ["COPY", "register:4050:8", ["const:805c30:8"]]
- 00805c1c bytes aa000010
- 00805c34 ["INT_ADD", "register:40f0:8", ["const:805c34:8", "const:4:8"]]
- 00805c34 ["CALL", null, ["callee:00851550:8"]]
+ 00805c8c ["INT_ADD", "register:40f0:8", ["const:805c8c:8", "const:4:8"]]
+ 00805c8c ["CALL", null, ["callee:00851550:8"]]
- 00805c34 bytes 312e0194
+ 00805c8c bytes 312e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80bb5d9c9cd15458e1b2cb28df7caad7"></a>

### [`00886f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886f44.md) → [`00886f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f9c.md) FUN_00886f9c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00457400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`00767da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767da4.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00457440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/00457440.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md) [`00764f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md) [`00767dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767dfc.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.95% / 新版 95.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00886fd8",
      "value": [
        "leaf",
        "ram:7643dc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00886f80",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00886f84"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00886fe4",
      "value": [
        "leaf",
        "ram:764f38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00886f8c",
      "value": [
        "leaf",
        "ram:764ee0:8"
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
      "00886fd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "unmatched:00886f84",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ],
    [
      "00886fe4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ]
  ],
  "added": [
    [
      "00886fd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ],
    [
      "00886fdc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ],
    [
      "00886fe4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764f38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886f44.md#insn-00886f80) · [`00886f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886f44.md#insn-00886f84) · [`00886f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886f44.md#insn-00886f8c)
- 新版 `00886fd8`（命令位置の公開資料なし） · `00886fe4`（命令位置の公開資料なし）

~~~diff
- 00886f80 ["INT_ADD", "register:40f0:8", ["const:886f80:8", "const:4:8"]]
- 00886f80 ["CALL", null, ["ram:764384:8"]]
+ 00886fd8 ["INT_ADD", "register:40f0:8", ["const:886fd8:8", "const:4:8"]]
+ 00886fd8 ["CALL", null, ["ram:7643dc:8"]]
- 00886f80 bytes 0175fb97
+ 00886fd8 bytes 0175fb97
- 00886f84 ["INT_ADD", "register:40f0:8", ["const:886f84:8", "const:4:8"]]
- 00886f84 ["CALL", null, ["callee:00851550:8"]]
- 00886f84 bytes 5d29ff97
- 00886f8c ["INT_ADD", "register:40f0:8", ["const:886f8c:8", "const:4:8"]]
- 00886f8c ["CALL", null, ["ram:764ee0:8"]]
+ 00886fe4 ["INT_ADD", "register:40f0:8", ["const:886fe4:8", "const:4:8"]]
+ 00886fe4 ["CALL", null, ["ram:764f38:8"]]
- 00886f8c bytes d577fb97
+ 00886fe4 bytes d577fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c82e24af2598b569c4f061ca9bf95ca6"></a>

### [`008c88e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c8/008c88e0.md) → [`008c8934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c8/008c8934.md) FUN_008c8934

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008c5da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c5/008c5da4.md) · 呼出先 4件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`009df5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df5fc.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md) [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md)
- 新版 呼出元 1件 [`008c5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c5df8.md) · 呼出先 4件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`009df650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df650.md) [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md) [`009e2fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e2fe8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 57.89% / 新版 61.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008c8954"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008c89a8"
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
      "unmatched:008c8954",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008c8a38"
      ]
    ]
  ],
  "added": [
    [
      "008c89a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008c8a38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c8954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c8/008c88e0.md#insn-008c8954) · [`008c88fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c8/008c88e0.md#insn-008c88fc)
- 新版 `008c89a8`（命令位置の公開資料なし） · `008c8950`（命令位置の公開資料なし）

~~~diff
- 008c8954 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 008c8954 bytes 80040054
+ 008c89a8 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 008c89a8 bytes 80040054
- 008c88fc ["INT_ADD", "register:40f0:8", ["const:8c88fc:8", "const:4:8"]]
- 008c88fc ["CALL", null, ["callee:00851550:8"]]
+ 008c8950 ["INT_ADD", "register:40f0:8", ["const:8c8950:8", "const:4:8"]]
+ 008c8950 ["CALL", null, ["callee:00851550:8"]]
- 008c88fc bytes ff22fe97
+ 008c8950 bytes 0023fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e599c5472a5902cb6369aca8284763e6"></a>

### [`008cbc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc08.md) → [`008cbc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc5c.md) FUN_008cbc5c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbc2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbc2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cbc80"
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
      "unmatched:008cbc2c",
      "DATA",
      [
        "storage",
        "00c83de8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cbc80",
      "DATA",
      [
        "storage",
        "00c83eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cbc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc08.md#insn-008cbc2c) · [`008cbc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc08.md#insn-008cbc1c)
- 新版 `008cbc80`（命令位置の公開資料なし） · `008cbc70`（命令位置の公開資料なし）

~~~diff
- 008cbc2c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008cbc2c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008cbc2c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008cbc2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cbc2c bytes 082400a9
+ 008cbc80 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008cbc80 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008cbc80 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008cbc80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008cbc80 bytes 082400a9
- 008cbc1c ["INT_ADD", "register:40f0:8", ["const:8cbc1c:8", "const:4:8"]]
- 008cbc1c ["CALL", null, ["callee:00c57f60:8"]]
+ 008cbc70 ["INT_ADD", "register:40f0:8", ["const:8cbc70:8", "const:4:8"]]
+ 008cbc70 ["CALL", null, ["callee:00c57f60:8"]]
- 008cbc1c bytes 9d300e94
+ 008cbc70 bytes bc300e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4a8cca5b839d7a457a08072b5d0ec34"></a>

### [`008cbc3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc3c.md) → [`008cbc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc90.md) FUN_008cbc90

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbc48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbc48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cbc9c"
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
      "unmatched:008cbc48",
      "DATA",
      [
        "storage",
        "00c83de8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cbc9c",
      "DATA",
      [
        "storage",
        "00c83eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cbc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc3c.md#insn-008cbc48) · [`008cbc44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc3c.md#insn-008cbc44)
- 新版 `008cbc9c`（命令位置の公開資料なし）

~~~diff
- 008cbc48 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008cbc48 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008cbc48 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 008cbc48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cbc48 bytes 292000a9
+ 008cbc9c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 008cbc9c ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 008cbc9c ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 008cbc9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008cbc9c bytes 292000a9
- 008cbc44 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 008cbc44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cbc44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cbc44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cbc44 bytes 29a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36bfe9176acbdaf7f60da59185420107"></a>

### [`008cbf68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbf68.md) → [`008cbfbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbfbc.md) FUN_008cbfbc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbf74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbf74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cbfc8"
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
      "unmatched:008cbf74",
      "DATA",
      [
        "storage",
        "00c83e68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cbfc8",
      "DATA",
      [
        "storage",
        "00c83f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cbf74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbf68.md#insn-008cbf74) · [`008cbf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbf68.md#insn-008cbf78)
- 新版 `008cbfc8`（命令位置の公開資料なし）

~~~diff
- 008cbf74 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008cbf74 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008cbf74 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 008cbf74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cbf74 bytes 292000a9
- 008cbf78 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008cbf78 ["RETURN", null, ["register:0:8"]]
- 008cbf78 bytes c0035fd6
+ 008cbfc8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 008cbfc8 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 008cbfc8 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 008cbfc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008cbfc8 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45a33aa0591a676c539440535675fd0a"></a>

### [`008cc4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc4c0.md) → [`008cc514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc514.md) FUN_008cc514

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008c385c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c3/008c385c.md) [`008c5208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c5/008c5208.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`008cc600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc600.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`008c38b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c3/008c38b4.md) [`008c525c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c525c.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008cc654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc654.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 66.67% / 新版 68.97%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc4d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc4d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cc524"
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
      "unmatched:008cc4d0",
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
      "008cc524",
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

- 旧版 [`008cc4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc4c0.md#insn-008cc4d0) · [`008cc524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc4c0.md#insn-008cc524)
- 新版 `008cc578`（命令位置の公開資料なし） · `008cc524`（命令位置の公開資料なし）

~~~diff
- 008cc4d0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008cc4d0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008cc4d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008cc4d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cc4d0 bytes f44f04a9
- 008cc524 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008cc524 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
+ 008cc578 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 008cc578 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 008cc524 bytes c80600b5
+ 008cc578 bytes c80600b5
+ 008cc524 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 008cc524 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 008cc524 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
+ 008cc524 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008cc524 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76913762125264df119ee32923816c89"></a>

### [`008ccdc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008ccdc4.md) → [`008cce18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cce18.md) FUN_008cce18

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 29.41% / 新版 31.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ccdd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ccdd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cce2c"
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
      "unmatched:008ccdd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ccde8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cce94"
      ]
    ],
    [
      "unmatched:008cce08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cce94"
      ]
    ]
  ],
  "added": [
    [
      "008cce2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008cce3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cce94"
      ]
    ],
    [
      "008cce5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cce94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ccdd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008ccdc4.md#insn-008ccdd8) · [`008ccde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008ccdc4.md#insn-008ccde8) · [`008cce08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008ccdc4.md#insn-008cce08)

~~~diff
- 008ccdd8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008ccdd8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008ccdd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008ccdd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ccdd8 bytes f44f02a9
- 008ccde8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 008ccde8 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 008ccde8 bytes c90200b4
- 008cce08 ["CBRANCH", null, ["local:b11:8", "register:102:1"]]
- 008cce08 bytes c2010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0841a0dbb15f6dc7463c4ac8b6f9d21"></a>

### [`008ced74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ced74.md) → [`008cedc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008cedc8.md) FUN_008cedc8

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008ce5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ce5c4.md) [`008ced74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ced74.md) · 呼出先 3件 [`008ced74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ced74.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`008ce618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ce618.md) [`008cedc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008cedc8.md) · 呼出先 3件 [`008cedc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008cedc8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.25% / 新版 93.25%

CFGの説明率　旧版 85.14% / 新版 84.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cee8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cef44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cef50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008cee48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cee78"
      ]
    ],
    [
      "unmatched:008cef5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cef34"
      ]
    ],
    [
      "008cf020",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008cefa8"
      ]
    ]
  ],
  "added": [
    [
      "008cee9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cee78"
      ]
    ],
    [
      "008cefb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cef34"
      ]
    ],
    [
      "008cf020",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ceffc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cee40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ced74.md#insn-008cee40) · [`008cee44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ced74.md#insn-008cee44) · [`008cee48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ced74.md#insn-008cee48)

~~~diff
- 008cee40 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008cee40 ["COPY", "tmp:1:8", ["register:4068:8"]]
- 008cee40 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 008cee40 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 008cee40 bytes acb18c9a
- 008cee44 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008cee44 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 008cee44 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 008cee44 ["COPY", "tmp:1:8", ["register:4070:8"]]
- 008cee44 bytes d6b28e9a
- 008cee48 ["INT_NOTEQUAL", "tmp:0:1", ["register:4060:8", "const:0:8"]]
- 008cee48 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 008cee48 bytes ecfeffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d4f464fd842cf63a0f2bcf75442b0c7"></a>

### [`008d05f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d05f4.md) → [`008d0648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0648.md) FUN_008d0648

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d061c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008d0670"
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
      "unmatched:008d061c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d06dc"
      ]
    ]
  ],
  "added": [
    [
      "008d0670",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d06dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d061c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d05f4.md#insn-008d061c) · [`008d0608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d05f4.md#insn-008d0608)
- 新版 `008d0670`（命令位置の公開資料なし） · `008d065c`（命令位置の公開資料なし）

~~~diff
- 008d061c ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 008d061c bytes 60030054
+ 008d0670 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 008d0670 bytes 60030054
- 008d0608 ["INT_ADD", "register:40f0:8", ["const:8d0608:8", "const:4:8"]]
- 008d0608 ["CALL", null, ["callee:00851550:8"]]
+ 008d065c ["INT_ADD", "register:40f0:8", ["const:8d065c:8", "const:4:8"]]
+ 008d065c ["CALL", null, ["callee:00851550:8"]]
- 008d0608 bytes bc03fe97
+ 008d065c bytes bd03fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c67a238ee15671f730a1a639a16cbf78"></a>

### [`008d0848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0848.md) → [`008d089c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d089c.md) FUN_008d089c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d0850"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d08a4"
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
      "unmatched:008d0850",
      "DATA",
      [
        "storage",
        "00c84528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d08a4",
      "DATA",
      [
        "storage",
        "00c845f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d0850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0848.md#insn-008d0850) · [`008d084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0848.md#insn-008d084c)
- 新版 `008d08a4`（命令位置の公開資料なし）

~~~diff
- 008d0850 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008d0850 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d0850 bytes 280000f9
+ 008d08a4 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008d08a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008d08a4 bytes 280000f9
- 008d084c ["COPY", "tmp:0:8", ["const:528:8"]]
- 008d084c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d084c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d084c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d084c bytes 08a11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abdd9ab159e84cd88a4821efbe073d05"></a>

### [`008d5a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5a7c.md) → [`008d5ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d5ad0.md) FUN_008d5ad0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00865af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865af4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 3件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00865b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865b4c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d5b5c",
      "incomplete_value": true,
      "site": "008d5b5c",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "008d5b08",
      "incomplete_value": true,
      "site": "008d5b08",
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
            "register:8:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5b18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008d5b6c"
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
      "unmatched:008d5b18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5b84"
      ]
    ]
  ],
  "added": [
    [
      "008d5b6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5b84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5a7c.md#insn-008d5b18) · [`008d5ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5a7c.md#insn-008d5ab8)
- 新版 `008d5b6c`（命令位置の公開資料なし） · `008d5b0c`（命令位置の公開資料なし）

~~~diff
- 008d5b18 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d5b18 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 008d5b18 bytes c1000054
+ 008d5b6c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008d5b6c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 008d5b6c bytes c1000054
- 008d5ab8 ["INT_ADD", "register:40f0:8", ["const:8d5ab8:8", "const:4:8"]]
- 008d5ab8 ["CALL", null, ["callee:005c17dc:8"]]
+ 008d5b0c ["INT_ADD", "register:40f0:8", ["const:8d5b0c:8", "const:4:8"]]
+ 008d5b0c ["CALL", null, ["callee:005c17dc:8"]]
- 008d5ab8 bytes 39aff397
+ 008d5b0c bytes 34aff397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e446e97feb2f26e379434919af226ea1"></a>

### [`008d5b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5b34.md) → [`008d5b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d5b88.md) FUN_008d5b88

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 3件 [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md)
- 新版 呼出元 1件 [`00a14de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14de0.md) · 呼出先 3件 [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md) [`004810d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004810d8.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.78% / 新版 98.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "008d5b58",
      "incomplete_value": true,
      "site": "008d5b5c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4040:4"
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
      "definition_site": "008d5bd0",
      "incomplete_value": true,
      "site": "008d5bd4",
      "value": [
        "live",
        "register:40a0:8"
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
      "definition_site": "008d5c0c",
      "incomplete_value": true,
      "site": "008d5c10",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 8,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008d5b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5b34.md#insn-008d5b5c) · [`008d5b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5b34.md#insn-008d5b80) · [`008d5bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5b34.md#insn-008d5bbc)
- 新版 `008d5bb0`（命令位置の公開資料なし） · `008d5bd4`（命令位置の公開資料なし） · `008d5c10`（命令位置の公開資料なし）

~~~diff
- 008d5b5c ["INT_ADD", "register:40f0:8", ["const:8d5b5c:8", "const:4:8"]]
- 008d5b5c ["CALL", null, ["callee:00480e68:8"]]
+ 008d5bb0 ["INT_ADD", "register:40f0:8", ["const:8d5bb0:8", "const:4:8"]]
+ 008d5bb0 ["CALL", null, ["callee:00480e68:8"]]
- 008d5b5c bytes b3acee97
+ 008d5bb0 bytes aeacee97
- 008d5b80 ["INT_ADD", "register:40f0:8", ["const:8d5b80:8", "const:4:8"]]
- 008d5b80 ["CALL", null, ["callee:004810d8:8"]]
+ 008d5bd4 ["INT_ADD", "register:40f0:8", ["const:8d5bd4:8", "const:4:8"]]
+ 008d5bd4 ["CALL", null, ["callee:004810d8:8"]]
- 008d5b80 bytes 46adee97
+ 008d5bd4 bytes 41adee97
- 008d5bbc ["INT_ADD", "register:40f0:8", ["const:8d5bbc:8", "const:4:8"]]
- 008d5bbc ["CALL", null, ["callee:004810d8:8"]]
+ 008d5c10 ["INT_ADD", "register:40f0:8", ["const:8d5c10:8", "const:4:8"]]
+ 008d5c10 ["CALL", null, ["callee:004810d8:8"]]
- 008d5bbc bytes 37adee97
+ 008d5c10 bytes 32adee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b2f738dbf459923ed9d6ae584ce6f6f"></a>

### [`008d6c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6c14.md) → [`008d6c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6c68.md) FUN_008d6c68

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00476708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476708.md) · 呼出先 0件 

命令の説明率　旧版 77.42% / 新版 77.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-42a7f80731851480546062a3439808bc"></a>

### [`008d94e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d94e4.md) → [`008d9538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9538.md) FUN_008d9538

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9508"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9508"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d955c"
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
      "unmatched:008d9508",
      "DATA",
      [
        "storage",
        "00c84aa8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d9510",
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
      "008d955c",
      "DATA",
      [
        "storage",
        "00c84b78",
        null,
        "undefined *"
      ]
    ],
    [
      "008d9564",
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

- 旧版 [`008d9508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d94e4.md#insn-008d9508) · [`008d9514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d94e4.md#insn-008d9514)
- 新版 `008d955c`（命令位置の公開資料なし）

~~~diff
- 008d9508 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d9508 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008d9508 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008d9508 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d9508 bytes 082400a9
- 008d9514 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008d9514 ["RETURN", null, ["register:0:8"]]
- 008d9514 bytes c0035fd6
+ 008d955c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008d955c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008d955c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008d955c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008d955c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-887057c96261a44f60567516ca770c3e"></a>

### [`008d970c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d970c.md) → [`008d9760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9760.md) FUN_008d9760

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b7994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7994.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b79ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b79ec.md) [`008b7a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a68.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9710"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d9764"
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
      "unmatched:008d9710",
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
      "008d9764",
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

- 旧版 [`008d9710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d970c.md#insn-008d9710) · [`008d9724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d970c.md#insn-008d9724)
- 新版 `008d9764`（命令位置の公開資料なし） · `008d9778`（命令位置の公開資料なし）

~~~diff
- 008d9710 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008d9710 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 008d9710 bytes f50b00f9
+ 008d9764 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 008d9764 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 008d9764 bytes f50b00f9
- 008d9724 ["INT_ADD", "register:40f0:8", ["const:8d9724:8", "const:4:8"]]
- 008d9724 ["CALL", null, ["callee:00851550:8"]]
+ 008d9778 ["INT_ADD", "register:40f0:8", ["const:8d9778:8", "const:4:8"]]
+ 008d9778 ["CALL", null, ["callee:00851550:8"]]
- 008d9724 bytes 75dffd97
+ 008d9778 bytes 76dffd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f877633ccb7dc8278f191f149a8e1c0"></a>

### [`008d97b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d97b0.md) → [`008d9804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9804.md) FUN_008d9804

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 44.44% / 新版 44.44%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d97c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d9814"
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
      "unmatched:008d97c0",
      "DATA",
      [
        "storage",
        "00c84ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9814",
      "DATA",
      [
        "storage",
        "00c84c78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d97c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d97b0.md#insn-008d97c0) · [`008d97b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d97b0.md#insn-008d97b0)
- 新版 `008d9814`（命令位置の公開資料なし）

~~~diff
- 008d97c0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d97c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008d97c0 bytes 090100f9
+ 008d9814 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008d9814 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008d9814 bytes 090100f9
- 008d97b0 ["COPY", "register:4040:8", ["register:4000:8"]]
- 008d97b0 bytes e80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f90e0498e996fd8fc5dad56508e3e37b"></a>

### [`008ddc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddc58.md) → [`008ddcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008ddcac.md) FUN_008ddcac

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008ddfa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddfa0.md) · 呼出先 1件 [`008dc120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dc/008dc120.md)
- 新版 呼出元 1件 [`008ddff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008ddff4.md) · 呼出先 1件 [`008dc174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dc/008dc174.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ddc84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008ddcd8"
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
      "unmatched:008ddc84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ddcf8"
      ]
    ]
  ],
  "added": [
    [
      "008ddcd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ddcf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ddc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddc58.md#insn-008ddc84) · [`008ddc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddc58.md#insn-008ddc80)
- 新版 `008ddcd8`（命令位置の公開資料なし）

~~~diff
- 008ddc84 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 008ddc84 bytes 00010054
+ 008ddcd8 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 008ddcd8 bytes 00010054
- 008ddc80 ["INT_LESSEQUAL", "register:105:1", ["register:40a8:8", "register:40a0:8"]]
- 008ddc80 ["INT_SBORROW", "register:106:1", ["register:40a0:8", "register:40a8:8"]]
- 008ddc80 ["INT_SUB", "tmp:0:8", ["register:40a0:8", "register:40a8:8"]]
- 008ddc80 ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
- 008ddc80 bytes 9f0215eb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1803aa3526a4b65782807fcc6a0a59c3"></a>

### [`008e8f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8f88.md) → [`008e8fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8fdc.md) FUN_008e8fdc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008e28bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e2/008e28bc.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`008e8a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8a04.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008e2910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008e8a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8a58.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.78% / 新版 98.78%

CFGの説明率　旧版 88.00% / 新版 91.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008e90c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "008e9114"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008e90c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8f88.md#insn-008e90c0) · [`008e8fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8f88.md#insn-008e8fb4)
- 新版 `008e9114`（命令位置の公開資料なし） · `008e9008`（命令位置の公開資料なし）

~~~diff
- 008e90c0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008e90c0 ["RETURN", null, ["register:0:8"]]
- 008e90c0 bytes c0035fd6
+ 008e9114 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 008e9114 ["RETURN", null, ["register:0:8"]]
+ 008e9114 bytes c0035fd6
- 008e8fb4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 008e8fb4 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 008e9008 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 008e9008 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 008e8fb4 bytes 8a0800b5
+ 008e9008 bytes 8a0800b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d230f6cfdd12626926bb8a2d2ce510f8"></a>

### [`008e90d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e90d0.md) → [`008e9124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9124.md) FUN_008e9124

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 55.56% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e9110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008e9164"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008e9110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e90d0.md#insn-008e9110) · [`008e90f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e90d0.md#insn-008e90f0)
- 新版 `008e9164`（命令位置の公開資料なし） · `008e9144`（命令位置の公開資料なし）

~~~diff
- 008e9110 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 008e9110 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008e9110 bytes 690a00f9
+ 008e9164 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
+ 008e9164 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008e9164 bytes 690a00f9
- 008e90f0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008e90f0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 008e9144 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 008e9144 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 008e90f0 bytes e00100b4
+ 008e9144 bytes e00100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b01bd9cf736dfdbdf80755785a2c7b39"></a>

### [`008e9138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9138.md) → [`008e918c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e918c.md) FUN_008e918c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008e28bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e2/008e28bc.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`008e8c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8c50.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008e2910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008e8ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ca4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e9224",
      "value": [
        "live",
        "register:4050:8"
      ]
    },
    "old": {
      "definition_site": "008e91bc",
      "incomplete_value": true,
      "site": "008e91d0",
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
            "register:40a0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e9204"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008e9258"
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
      "unmatched:008e9164",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e92c8"
      ]
    ]
  ],
  "added": [
    [
      "008e91b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e92c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9138.md#insn-008e9164) · [`008e9204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9138.md#insn-008e9204)
- 新版 `008e91b8`（命令位置の公開資料なし）

~~~diff
- 008e9164 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 008e9164 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 008e9164 bytes 8a0800b5
+ 008e91b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 008e91b8 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
+ 008e91b8 bytes 8a0800b5
- 008e9204 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
- 008e9204 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008e9204 bytes 0081803c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bf09cbf04456945ed3f9adbb34d89a1"></a>

### [`008eb988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb988.md) → [`008eb9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb9dc.md) FUN_008eb9dc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`008eb488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb488.md) [`008ec2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ec/008ec2a0.md) [`008f53b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f53b0.md) [`008f7008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f7/008f7008.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008c4920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c4/008c4920.md) [`008cabbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008cabbc.md)
- 新版 呼出元 4件 [`008eb4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb4dc.md) [`008ec2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008ec2f4.md) [`008f5404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5404.md) [`008f6b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6b3c.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008c4974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c4/008c4974.md) [`008cac10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ca/008cac10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 18.75% / 新版 17.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008eba14"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008eba68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008eba18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008eba14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ebacc"
      ]
    ],
    [
      "unmatched:008eba18",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ],
    [
      "unmatched:008eba70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008c4920"
      ]
    ]
  ],
  "added": [
    [
      "008eba68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ebacc"
      ]
    ],
    [
      "008eba6c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ],
    [
      "008ebac4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008c4974"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eba14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb988.md#insn-008eba14) · [`008eba18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb988.md#insn-008eba18)
- 新版 `008eba68`（命令位置の公開資料なし）

~~~diff
- 008eba14 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008eba14 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 008eba14 bytes 2a030054
- 008eba18 ["INT_ADD", "register:40f0:8", ["const:8eba18:8", "const:4:8"]]
- 008eba18 ["CALL", null, ["callee:00851550:8"]]
- 008eba18 bytes b896fd97
+ 008eba68 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 008eba68 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 008eba68 bytes 2a030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7d1d93751f23fd408e2102265d472c8"></a>

### [`008f22e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f2/008f22e4.md) → [`008f2338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f2338.md) FUN_008f2338

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f3044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f3/008f3044.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`008f3098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f3/008f3098.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008f2374"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "008f23c8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008f2374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f2/008f22e4.md#insn-008f2374) · [`008f22f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f2/008f22e4.md#insn-008f22f8)
- 新版 `008f23c8`（命令位置の公開資料なし） · `008f234c`（命令位置の公開資料なし）

~~~diff
- 008f2374 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008f2374 ["RETURN", null, ["register:0:8"]]
- 008f2374 bytes c0035fd6
+ 008f23c8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 008f23c8 ["RETURN", null, ["register:0:8"]]
+ 008f23c8 bytes c0035fd6
- 008f22f8 ["INT_ADD", "register:40f0:8", ["const:8f22f8:8", "const:4:8"]]
- 008f22f8 ["CALL", null, ["callee:00851550:8"]]
+ 008f234c ["INT_ADD", "register:40f0:8", ["const:8f234c:8", "const:4:8"]]
+ 008f234c ["CALL", null, ["callee:00851550:8"]]
- 008f22f8 bytes 807cfd97
+ 008f234c bytes 817cfd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c348aa7cf01d95201f44f0359c2d7bd6"></a>

### [`008f3950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f3/008f3950.md) → [`008f39a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f3/008f39a4.md) FUN_008f39a4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006d8768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d8768.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`006d87c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d87c0.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008f3968"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008f39bc"
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
      "unmatched:008f3968",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f39d0"
      ]
    ]
  ],
  "added": [
    [
      "008f39bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f39d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f3968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f3/008f3950.md#insn-008f3968) · [`008f3974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f3/008f3950.md#insn-008f3974)
- 新版 `008f39bc`（命令位置の公開資料なし） · `008f39c8`（命令位置の公開資料なし）

~~~diff
- 008f3968 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 008f3968 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008f3968 bytes b30000b4
+ 008f39bc ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 008f39bc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 008f39bc bytes b30000b4
- 008f3974 ["INT_ADD", "register:40f0:8", ["const:8f3974:8", "const:4:8"]]
- 008f3974 ["CALL", null, ["callee:00c53da0:8"]]
+ 008f39c8 ["INT_ADD", "register:40f0:8", ["const:8f39c8:8", "const:4:8"]]
+ 008f39c8 ["CALL", null, ["callee:00c53da0:8"]]
- 008f3974 bytes e3800d94
+ 008f39c8 bytes f6800d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f709096a95d789a535fed296a1d1b43"></a>

### [`008f9e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9e08.md) → [`008f9e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9e5c.md) FUN_008f9e5c

採用 · 移動量 `+0x54` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`008f52ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f52ec.md) [`008f9e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9e08.md) [`008fa27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa27c.md) · 呼出先 4件 [`008f9e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9e08.md) [`008fa10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa10c.md) [`008fa27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa27c.md) [`008fa544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa544.md)
- 新版 呼出元 3件 [`008f5340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5340.md) [`008f9e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9e5c.md) [`008fa2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa2d0.md) · 呼出先 4件 [`008f9e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9e5c.md) [`008fa160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa160.md) [`008fa2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa2d0.md) [`008fa598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa598.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 99.48% / 新版 99.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f9e14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f9e14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008f9e68"
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
      "unmatched:008f9e14",
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
      "008f9e68",
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

- 旧版 [`008f9e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9e08.md#insn-008f9e14) · [`008f9e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9e08.md#insn-008f9e54)
- 新版 `008f9e68`（命令位置の公開資料なし） · `008f9ea8`（命令位置の公開資料なし）

~~~diff
- 008f9e14 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 008f9e14 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 008f9e14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 008f9e14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008f9e14 bytes f65703a9
+ 008f9e68 ["COPY", "tmp:0:8", ["register:40b0:8"]]
+ 008f9e68 ["COPY", "tmp:1:8", ["register:40a8:8"]]
+ 008f9e68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
+ 008f9e68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008f9e68 bytes f65703a9
- 008f9e54 ["INT_ADD", "register:40f0:8", ["const:8f9e54:8", "const:4:8"]]
- 008f9e54 ["CALL", null, ["callee:008fa160:8"]]
+ 008f9ea8 ["INT_ADD", "register:40f0:8", ["const:8f9ea8:8", "const:4:8"]]
+ 008f9ea8 ["CALL", null, ["callee:008fa160:8"]]
- 008f9e54 bytes ae000094
+ 008f9ea8 bytes ae000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-465d1b6303786cb251de265650aaca4b"></a>

### [`008fadc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fadc0.md) → [`008fae14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fae14.md) FUN_008fae14

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008fadd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008fae2c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008fade0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008fadd8",
      "DATA",
      [
        "storage",
        "00c85a68",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008faddc",
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
      "008fae2c",
      "DATA",
      [
        "storage",
        "00c85b38",
        null,
        "undefined *"
      ]
    ],
    [
      "008fae30",
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

- 旧版 [`008fadd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fadc0.md#insn-008fadd8) · [`008fade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fadc0.md#insn-008fade0)
- 新版 `008fae2c`（命令位置の公開資料なし）

~~~diff
- 008fadd8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008fadd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008fadd8 bytes 080000f9
- 008fade0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008fade0 ["RETURN", null, ["register:0:8"]]
- 008fade0 bytes c0035fd6
+ 008fae2c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008fae2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008fae2c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a396246a7f775cc64787193f1494a2db"></a>

### [`008fd1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd1e0.md) → [`008fd234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fd/008fd234.md) FUN_008fd234

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008fc5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc5f0.md) [`008fd500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd500.md) · 呼出先 9件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005da584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005da/005da584.md) [`00691800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691800.md) [`0071ed00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071ed00.md)
- 新版 呼出元 2件 [`008fc644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fc/008fc644.md) [`008fd554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fd/008fd554.md) · 呼出先 9件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`005da5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005da/005da5c4.md) [`00691858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691858.md) [`0071ed58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071ed58.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008fd380"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008fd3d4"
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
      "008fd2dc",
      "READ",
      [
        "storage",
        "0029f635",
        null,
        "string"
      ]
    ],
    [
      "008fd2e0",
      "READ",
      [
        "storage",
        "0029f63c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008fd380",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008fd3cc"
      ]
    ]
  ],
  "added": [
    [
      "008fd2dc",
      "READ",
      [
        "storage",
        "0029f5e8",
        null,
        "string"
      ]
    ],
    [
      "008fd2e0",
      "READ",
      [
        "storage",
        "0029f5ef",
        null,
        "string"
      ]
    ],
    [
      "008fd3d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008fd3cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd1e0.md#insn-008fd380) · [`008fd218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd1e0.md#insn-008fd218)
- 新版 `008fd3d4`（命令位置の公開資料なし） · `008fd26c`（命令位置の公開資料なし）

~~~diff
- 008fd380 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 008fd380 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 008fd380 bytes c9ffffb5
+ 008fd3d4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 008fd3d4 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 008fd3d4 bytes c9ffffb5
- 008fd218 ["INT_ADD", "register:40f0:8", ["const:8fd218:8", "const:4:8"]]
- 008fd218 ["CALL", null, ["callee:008ac3d8:8"]]
+ 008fd26c ["INT_ADD", "register:40f0:8", ["const:8fd26c:8", "const:4:8"]]
+ 008fd26c ["CALL", null, ["callee:008ac3d8:8"]]
- 008fd218 bytes 5abcfe97
+ 008fd26c bytes 5bbcfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-170a10a423f27488a634e12ee08f072c"></a>

### [`008ff46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff46c.md) → [`008ff4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff4c0.md) FUN_008ff4c0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_value, call, call_target, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008ff53c",
      "incomplete_value": true,
      "site": "008ff53c",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff4e8",
      "incomplete_value": true,
      "site": "008ff4e8",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
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
      "site": "008ff4ec",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ff498",
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
      "008ff4ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "008ff4ec",
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

- 旧版 [`008ff498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff46c.md#insn-008ff498) · [`008ff4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff46c.md#insn-008ff4ec) · [`008ff47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff46c.md#insn-008ff47c)
- 新版 `008ff4ec`（命令位置の公開資料なし） · `008ff540`（命令位置の公開資料なし）

~~~diff
- 008ff498 ["INT_ADD", "register:40f0:8", ["const:8ff498:8", "const:4:8"]]
- 008ff498 ["CALL", null, ["ram:47acf4:8"]]
+ 008ff4ec ["INT_ADD", "register:40f0:8", ["const:8ff4ec:8", "const:4:8"]]
+ 008ff4ec ["CALL", null, ["ram:47ad34:8"]]
- 008ff498 bytes 17eeed97
+ 008ff4ec bytes 12eeed97
- 008ff4ec ["INT_ADD", "register:40f0:8", ["const:8ff4ec:8", "const:4:8"]]
- 008ff4ec ["CALL", null, ["callee:00851550:8"]]
+ 008ff540 ["INT_ADD", "register:40f0:8", ["const:8ff540:8", "const:4:8"]]
+ 008ff540 ["CALL", null, ["callee:00851550:8"]]
- 008ff4ec bytes 0348fd97
+ 008ff540 bytes 0448fd97
- 008ff47c ["COPY", "register:40e8:8", ["register:8:8"]]
- 008ff47c bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6a0dd4e9cc77cb8741f712cb2c87c72"></a>

### [`008ff67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff67c.md) → [`008ff6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff6d0.md) FUN_008ff6d0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008ff368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff368.md) [`008ff3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff3bc.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00691800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691800.md)
- 新版 呼出元 2件 [`008ff3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff3bc.md) [`008ff410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff410.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00691858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691858.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ff690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff67c.md#insn-008ff690) · [`008ff6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff67c.md#insn-008ff6d0)
- 新版 `008ff724`（命令位置の公開資料なし） · `008ff6e4`（命令位置の公開資料なし）

~~~diff
- 008ff690 ["COPY", "register:40e8:8", ["register:8:8"]]
- 008ff690 bytes fd030091
- 008ff6d0 ["INT_ADD", "register:40f0:8", ["const:8ff6d0:8", "const:4:8"]]
- 008ff6d0 ["CALL", null, ["callee:0043bb60:8"]]
+ 008ff724 ["INT_ADD", "register:40f0:8", ["const:8ff724:8", "const:4:8"]]
+ 008ff724 ["CALL", null, ["callee:0043bb60:8"]]
- 008ff6d0 bytes 14f1ec97
+ 008ff724 bytes 0ff1ec97
+ 008ff6e4 ["COPY", "register:40e8:8", ["register:8:8"]]
+ 008ff6e4 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ac769a93f23c1244e256ff3175038df"></a>

### [`0090153c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/0090153c.md) → [`00901590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/00901590.md) FUN_00901590

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0090155c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "009015b0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0090155c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/0090153c.md#insn-0090155c) · [`00901544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/0090153c.md#insn-00901544)
- 新版 `009015b0`（命令位置の公開資料なし） · `00901598`（命令位置の公開資料なし）

~~~diff
- 0090155c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0090155c ["RETURN", null, ["register:0:8"]]
- 0090155c bytes c0035fd6
+ 009015b0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 009015b0 ["RETURN", null, ["register:0:8"]]
+ 009015b0 bytes c0035fd6
- 00901544 ["INT_ADD", "register:40f0:8", ["const:901544:8", "const:4:8"]]
- 00901544 ["CALL", null, ["callee:00851550:8"]]
+ 00901598 ["INT_ADD", "register:40f0:8", ["const:901598:8", "const:4:8"]]
+ 00901598 ["CALL", null, ["callee:00851550:8"]]
- 00901544 bytes ed3ffd97
+ 00901598 bytes ee3ffd97
~~~


<a id="compare-6f1ff4d9dd70082ffdb99a0212dc1c6e"></a>

### [`009015c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009015c0.md) → [`00901614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/00901614.md) FUN_00901614

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009015cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009015cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00901620"
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
      "unmatched:009015cc",
      "DATA",
      [
        "storage",
        "00c85d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00901620",
      "DATA",
      [
        "storage",
        "00c85e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009015cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009015c0.md#insn-009015cc) · [`009015c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009015c0.md#insn-009015c8)
- 新版 `00901620`（命令位置の公開資料なし）

~~~diff
- 009015cc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009015cc ["COPY", "tmp:1:8", ["register:4040:8"]]
- 009015cc ["COPY", "tmp:2:8", ["register:4008:8"]]
- 009015cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009015cc bytes 292000a9
+ 00901620 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00901620 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00901620 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00901620 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00901620 bytes 292000a9
- 009015c8 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 009015c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009015c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009015c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009015c8 bytes 29413591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf4e9610eb357141504c615a4805db71"></a>

### [`0090a1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090a/0090a1d0.md) → [`0090a224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090a/0090a224.md) FUN_0090a224

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`009049b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009049b4.md) [`0090dcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090dcfc.md) [`00914e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00914/00914e30.md) · 呼出先 13件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005626f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/005626f4.md)
- 新版 呼出元 3件 [`00904a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00904/00904a08.md) [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) [`00914e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00914/00914e84.md) · 呼出先 13件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00562734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562734.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.37% / 新版 93.37%

CFGの説明率　旧版 79.66% / 新版 81.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0090a3c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0090a41c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0090a22c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0090a200",
      "READ",
      [
        "storage",
        "002a92f8",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0090a22c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "0090a300",
      "READ",
      [
        "storage",
        "00c9aca0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0090a254",
      "READ",
      [
        "storage",
        "002a9327",
        null,
        "string"
      ]
    ],
    [
      "0090a280",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "0090a300",
      "READ",
      [
        "storage",
        "00c9ad70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0090a22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090a/0090a1d0.md#insn-0090a22c) · [`0090a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090a/0090a1d0.md#insn-0090a280)
- 新版 `0090a2d4`（命令位置の公開資料なし） · `0090a280`（命令位置の公開資料なし）

~~~diff
- 0090a22c ["INT_ADD", "register:40f0:8", ["const:90a22c:8", "const:4:8"]]
- 0090a22c ["CALL", null, ["ram:71bed8:8"]]
- 0090a22c bytes 2b47f897
- 0090a280 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 0090a280 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0090a280 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0090a280 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 0090a2d4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 0090a2d4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 0090a2d4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 0090a2d4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 0090a280 bytes c80c0037
+ 0090a2d4 bytes c80c0037
+ 0090a280 ["INT_ADD", "register:40f0:8", ["const:90a280:8", "const:4:8"]]
+ 0090a280 ["CALL", null, ["ram:71bf30:8"]]
+ 0090a280 bytes 2c47f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa22d67c626474635b482a05ad0da2a7"></a>

### [`0090d834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090d834.md) → [`0090d888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090d888.md) FUN_0090d888

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009d3b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3b48.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0090d864"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0090d8b8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0090da38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0090d864",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:0090da38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0090da84"
      ]
    ]
  ],
  "added": [
    [
      "0090d8b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "0090da8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0090da84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0090d864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090d834.md#insn-0090d864) · [`0090d964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090d834.md#insn-0090d964)
- 新版 `0090d8b8`（命令位置の公開資料なし） · `0090d9b8`（命令位置の公開資料なし）

~~~diff
- 0090d864 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0090d864 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 0090d864 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0090d864 bytes a8831ef8
+ 0090d8b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0090d8b8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
+ 0090d8b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 0090d8b8 bytes a8831ef8
- 0090d964 ["INT_ADD", "register:40f0:8", ["const:90d964:8", "const:4:8"]]
- 0090d964 ["CALL", null, ["callee:00c580d0:8"]]
+ 0090d9b8 ["INT_ADD", "register:40f0:8", ["const:90d9b8:8", "const:4:8"]]
+ 0090d9b8 ["CALL", null, ["callee:00c580d0:8"]]
- 0090d964 bytes a7290d94
+ 0090d9b8 bytes c6290d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5e2cfe72b7d72a2f6544a80f22ad9d8"></a>

### [`00921804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00921/00921804.md) → [`00921858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00921/00921858.md) FUN_00921858

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00921804"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00921804"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00921808"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00921804",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00921808",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00921828",
      "DATA",
      [
        "storage",
        "00c85f10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00921858",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0092185c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0092187c",
      "DATA",
      [
        "storage",
        "00c85fe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00921804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00921/00921804.md#insn-00921804) · [`00921808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00921/00921804.md#insn-00921808) · [`00921828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00921/00921804.md#insn-00921828)

~~~diff
- 00921804 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00921804 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00921804 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00921804 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00921804 bytes fd7bbea9
- 00921808 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00921808 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00921808 bytes f30b00f9
- 00921828 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00921828 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00921828 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00921828 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00921828 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1b605731a30baf3fa3b2ad8b52e7d25"></a>

### [`00929c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929c60.md) → [`00929cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00929/00929cb4.md) FUN_00929cb4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929c84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929c84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00929cd8"
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
      "unmatched:00929c84",
      "DATA",
      [
        "storage",
        "00c865c8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00929c88",
      "READ",
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
      "00929cd8",
      "DATA",
      [
        "storage",
        "00c86698",
        null,
        "undefined *"
      ]
    ],
    [
      "00929cdc",
      "READ",
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

- 旧版 [`00929c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929c60.md#insn-00929c84) · [`00929c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929c60.md#insn-00929c74)
- 新版 `00929cd8`（命令位置の公開資料なし） · `00929cc8`（命令位置の公開資料なし）

~~~diff
- 00929c84 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00929c84 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00929c84 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00929c84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00929c84 bytes 082400a9
+ 00929cd8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00929cd8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00929cd8 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00929cd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00929cd8 bytes 082400a9
- 00929c74 ["INT_ADD", "register:40f0:8", ["const:929c74:8", "const:4:8"]]
- 00929c74 ["CALL", null, ["callee:00c57f60:8"]]
+ 00929cc8 ["INT_ADD", "register:40f0:8", ["const:929cc8:8", "const:4:8"]]
+ 00929cc8 ["CALL", null, ["callee:00c57f60:8"]]
- 00929c74 bytes 87b80c94
+ 00929cc8 bytes a6b80c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f58bbfa880d3e124d3e415edcd3a533b"></a>

### [`00929c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929c94.md) → [`00929ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00929/00929ce8.md) FUN_00929ce8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 40.00% / 新版 40.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929ca0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929ca0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00929cf4"
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
      "unmatched:00929ca0",
      "DATA",
      [
        "storage",
        "00c865c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00929cf4",
      "DATA",
      [
        "storage",
        "00c86698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00929ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929c94.md#insn-00929ca0) · [`00929c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929c94.md#insn-00929c98)
- 新版 `00929cf4`（命令位置の公開資料なし）

~~~diff
- 00929ca0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00929ca0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00929ca0 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00929ca0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00929ca0 bytes 292000a9
+ 00929cf4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00929cf4 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00929cf4 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00929cf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00929cf4 bytes 292000a9
- 00929c98 ["COPY", "register:4048:8", ["const:c86000:8"]]
- 00929c98 bytes e91a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d139c371f88338bf2780fdea1f7dd00d"></a>

### [`00929e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929e08.md) → [`00929e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00929/00929e5c.md) FUN_00929e5c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929e2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929e2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00929e80"
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
      "unmatched:00929e2c",
      "DATA",
      [
        "storage",
        "00c866c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00929e80",
      "DATA",
      [
        "storage",
        "00c86798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00929e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929e08.md#insn-00929e2c) · [`00929e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929e08.md#insn-00929e1c)
- 新版 `00929e80`（命令位置の公開資料なし） · `00929e70`（命令位置の公開資料なし）

~~~diff
- 00929e2c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00929e2c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00929e2c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00929e2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00929e2c bytes 082400a9
+ 00929e80 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00929e80 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00929e80 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00929e80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00929e80 bytes 082400a9
- 00929e1c ["INT_ADD", "register:40f0:8", ["const:929e1c:8", "const:4:8"]]
- 00929e1c ["CALL", null, ["callee:00c57f60:8"]]
+ 00929e70 ["INT_ADD", "register:40f0:8", ["const:929e70:8", "const:4:8"]]
+ 00929e70 ["CALL", null, ["callee:00c57f60:8"]]
- 00929e1c bytes 1db80c94
+ 00929e70 bytes 3cb80c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1230e438659652a30bbbcc78be5718a"></a>

### [`00929e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929e3c.md) → [`00929e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00929/00929e90.md) FUN_00929e90

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929e48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929e48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00929e9c"
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
      "unmatched:00929e48",
      "DATA",
      [
        "storage",
        "00c866c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00929e9c",
      "DATA",
      [
        "storage",
        "00c86798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00929e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929e3c.md#insn-00929e48) · [`00929e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929e3c.md#insn-00929e44)
- 新版 `00929e9c`（命令位置の公開資料なし）

~~~diff
- 00929e48 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00929e48 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00929e48 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00929e48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00929e48 bytes 292000a9
+ 00929e9c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00929e9c ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00929e9c ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00929e9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00929e9c bytes 292000a9
- 00929e44 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00929e44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00929e44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00929e44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00929e44 bytes 29211b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7810dc70bad56b73ea9c6b1cdf8c557"></a>

### [`00929e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929e58.md) → [`00929eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00929/00929eac.md) FUN_00929eac

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00929e80"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00929ed4"
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
      "unmatched:00929e80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00929ed4",
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

- 旧版 [`00929e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929e58.md#insn-00929e80) · [`00929e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929e58.md#insn-00929e64)
- 新版 `00929ed4`（命令位置の公開資料なし） · `00929eb8`（命令位置の公開資料なし）

~~~diff
- 00929e80 ["INT_ADD", "register:40f0:8", ["const:929e80:8", "const:4:8"]]
- 00929e80 ["CALL", null, ["ram:47acf4:8"]]
- 00929e80 bytes 9d43ed97
+ 00929ed4 ["INT_ADD", "register:40f0:8", ["const:929ed4:8", "const:4:8"]]
+ 00929ed4 ["CALL", null, ["ram:47ad34:8"]]
+ 00929ed4 bytes 9843ed97
- 00929e64 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00929e64 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00929eb8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00929eb8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00929e64 bytes e1010054
+ 00929eb8 bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec93b53b255cbc1afbb842ee9084bcdf"></a>

### [`00930fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930fe4.md) → [`00931038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00931/00931038.md) FUN_00931038

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00930fec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00931040"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00930ff0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00930fec",
      "DATA",
      [
        "storage",
        "00c86a38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00931040",
      "DATA",
      [
        "storage",
        "00c86b08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00930fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930fe4.md#insn-00930fec) · [`00930ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930fe4.md#insn-00930ff0)
- 新版 `00931040`（命令位置の公開資料なし）

~~~diff
- 00930fec ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00930fec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00930fec bytes 280000f9
- 00930ff0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00930ff0 ["RETURN", null, ["register:0:8"]]
- 00930ff0 bytes c0035fd6
+ 00931040 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00931040 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00931040 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-794fc46bdb5e1b528ddc194d88fc06c0"></a>

### [`0093150c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/0093150c.md) → [`00931560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00931/00931560.md) FUN_00931560

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0093150c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0093150c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00931510"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0093150c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00931510",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00931530",
      "DATA",
      [
        "storage",
        "00c86c48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00931560",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00931564",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00931584",
      "DATA",
      [
        "storage",
        "00c86d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0093150c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/0093150c.md#insn-0093150c) · [`00931510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/0093150c.md#insn-00931510) · [`00931530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/0093150c.md#insn-00931530)

~~~diff
- 0093150c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0093150c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0093150c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0093150c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0093150c bytes fd7bbea9
- 00931510 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00931510 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00931510 bytes f30b00f9
- 00931530 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00931530 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00931530 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00931530 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00931530 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73182a33ece496de325bfd65f440b4c0"></a>

### [`00932448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932448.md) → [`0093249c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00932/0093249c.md) FUN_0093249c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00764f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0093246c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009324c0"
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
      "unmatched:0093246c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ]
  ],
  "added": [
    [
      "009324c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764f38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0093246c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932448.md#insn-0093246c) · [`009324c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932448.md#insn-009324c0)
- 新版 `00932514`（命令位置の公開資料なし） · `009324c0`（命令位置の公開資料なし）

~~~diff
- 0093246c ["INT_ADD", "register:40f0:8", ["const:93246c:8", "const:4:8"]]
- 0093246c ["CALL", null, ["ram:764ee0:8"]]
- 0093246c bytes 9dcaf897
- 009324c0 ["INT_ADD", "register:40f0:8", ["const:9324c0:8", "const:4:8"]]
- 009324c0 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00932514 ["INT_ADD", "register:40f0:8", ["const:932514:8", "const:4:8"]]
+ 00932514 ["CALL", null, ["callee:00c57fb0:8"]]
- 009324c0 bytes 88960c94
+ 00932514 bytes a7960c94
+ 009324c0 ["INT_ADD", "register:40f0:8", ["const:9324c0:8", "const:4:8"]]
+ 009324c0 ["CALL", null, ["ram:764f38:8"]]
+ 009324c0 bytes 9ecaf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-618f711e7077b553780e3601ce42ec03"></a>

### [`009325f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009325f8.md) → [`0093264c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00932/0093264c.md) FUN_0093264c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00932600"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00932654"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00932604"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00932600",
      "DATA",
      [
        "storage",
        "00c870c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00932654",
      "DATA",
      [
        "storage",
        "00c87198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00932600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009325f8.md#insn-00932600) · [`00932604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009325f8.md#insn-00932604)
- 新版 `00932654`（命令位置の公開資料なし）

~~~diff
- 00932600 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00932600 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00932600 bytes 280000f9
- 00932604 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00932604 ["RETURN", null, ["register:0:8"]]
- 00932604 bytes c0035fd6
+ 00932654 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00932654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00932654 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ce7332f534044e2518e74556481bcbc"></a>

### [`00932c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932c94.md) → [`00932ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00932/00932ce8.md) FUN_00932ce8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00932cac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00932d00"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00932cb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00932cac",
      "DATA",
      [
        "storage",
        "00c87238",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00932cb0",
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
      "00932d00",
      "DATA",
      [
        "storage",
        "00c87308",
        null,
        "undefined *"
      ]
    ],
    [
      "00932d04",
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

- 旧版 [`00932cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932c94.md#insn-00932cac) · [`00932cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932c94.md#insn-00932cb4)
- 新版 `00932d00`（命令位置の公開資料なし）

~~~diff
- 00932cac ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00932cac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00932cac bytes 080000f9
- 00932cb4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00932cb4 ["RETURN", null, ["register:0:8"]]
- 00932cb4 bytes c0035fd6
+ 00932d00 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00932d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00932d00 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f498b15a2eaa931062f593b37a66b1e"></a>

### [`00932d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932d9c.md) → [`00932df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00932/00932df0.md) FUN_00932df0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00932da4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00932df8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00932da8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00932da4",
      "DATA",
      [
        "storage",
        "00c872c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00932df8",
      "DATA",
      [
        "storage",
        "00c87398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00932da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932d9c.md#insn-00932da4) · [`00932da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932d9c.md#insn-00932da8)
- 新版 `00932df8`（命令位置の公開資料なし）

~~~diff
- 00932da4 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00932da4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00932da4 bytes 280000f9
- 00932da8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00932da8 ["RETURN", null, ["register:0:8"]]
- 00932da8 bytes c0035fd6
+ 00932df8 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00932df8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00932df8 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-103fee4c4a177981297ace89f28553a4"></a>

### [`009331f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009331f8.md) → [`0093324c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00933/0093324c.md) FUN_0093324c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00933200"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00933254"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00933204"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00933200",
      "DATA",
      [
        "storage",
        "00c87338",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00933254",
      "DATA",
      [
        "storage",
        "00c87408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00933200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009331f8.md#insn-00933200) · [`00933204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009331f8.md#insn-00933204)
- 新版 `00933254`（命令位置の公開資料なし）

~~~diff
- 00933200 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00933200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00933200 bytes 280000f9
- 00933204 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00933204 ["RETURN", null, ["register:0:8"]]
- 00933204 bytes c0035fd6
+ 00933254 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00933254 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00933254 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e63bf9867f55f57ca5fe42facb19f4c9"></a>

### [`00935a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935a70.md) → [`00935ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00935/00935ac4.md) FUN_00935ac4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00935a80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00935ad4"
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
      "unmatched:00935a80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00935ae8"
      ]
    ]
  ],
  "added": [
    [
      "00935ad4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00935ae8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00935a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935a70.md#insn-00935a80) · [`00935a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935a70.md#insn-00935a8c)
- 新版 `00935ad4`（命令位置の公開資料なし） · `00935ae0`（命令位置の公開資料なし）

~~~diff
- 00935a80 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00935a80 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00935a80 bytes b30000b4
+ 00935ad4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00935ad4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00935ad4 bytes b30000b4
- 00935a8c ["INT_ADD", "register:40f0:8", ["const:935a8c:8", "const:4:8"]]
- 00935a8c ["CALL", null, ["callee:00c53da0:8"]]
+ 00935ae0 ["INT_ADD", "register:40f0:8", ["const:935ae0:8", "const:4:8"]]
+ 00935ae0 ["CALL", null, ["callee:00c53da0:8"]]
- 00935a8c bytes 9d780c94
+ 00935ae0 bytes b0780c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f216fe290e28d64a26a1e2870aac2154"></a>

### [`00935ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935ac0.md) → [`00935b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00935/00935b14.md) FUN_00935b14

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00935aec"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00935b40"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00935aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935ac0.md#insn-00935aec) · [`00935adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935ac0.md#insn-00935adc)
- 新版 `00935b40`（命令位置の公開資料なし） · `00935b30`（命令位置の公開資料なし）

~~~diff
- 00935aec ["COPY", "register:0:8", ["register:40f0:8"]]
- 00935aec ["RETURN", null, ["register:0:8"]]
- 00935aec bytes c0035fd6
+ 00935b40 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00935b40 ["RETURN", null, ["register:0:8"]]
+ 00935b40 bytes c0035fd6
- 00935adc ["INT_ADD", "register:40f0:8", ["const:935adc:8", "const:4:8"]]
- 00935adc ["CALL", null, ["callee:00c53da0:8"]]
+ 00935b30 ["INT_ADD", "register:40f0:8", ["const:935b30:8", "const:4:8"]]
+ 00935b30 ["CALL", null, ["callee:00c53da0:8"]]
- 00935adc bytes 89780c94
+ 00935b30 bytes 9c780c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d200357a492c3bdbb553548a4f4b593"></a>

### [`009379a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/009379a0.md) → [`009379f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00937/009379f4.md) FUN_009379f4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 79.31% / 新版 82.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00937a14",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00937a88"
      ]
    ],
    [
      "00937a68",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00937b00"
      ]
    ]
  ],
  "added": [
    [
      "00937a68",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00937a88"
      ]
    ],
    [
      "00937a70",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00937b00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009379a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/009379a0.md#insn-009379a4) · [`009379e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/009379a0.md#insn-009379e8) · [`009379fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/009379a0.md#insn-009379fc)
- 新版 `009379f8`（命令位置の公開資料なし） · `00937a3c`（命令位置の公開資料なし） · `00937a50`（命令位置の公開資料なし）

~~~diff
- 009379a4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009379a4 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 009379f8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 009379f8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 009379a4 bytes e80300b4
+ 009379f8 bytes e80300b4
- 009379e8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009379e8 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00937a3c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00937a3c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 009379e8 bytes 080200b4
+ 00937a3c bytes 080200b4
- 009379fc ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 009379fc ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
+ 00937a50 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00937a50 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 009379fc bytes 4a050054
+ 00937a50 bytes 4a050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8b4937f64358b861bfacf48c987c8e4"></a>

### [`00937ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/00937ac0.md) → [`00937b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00937/00937b14.md) FUN_00937b14

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`0071e96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e96c.md) [`007ca528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca528.md) [`007dd364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd364.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046dabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dabc.md) [`0080b040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b040.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 6件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`0071e9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e9c4.md) [`007ca580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ca/007ca580.md) [`007dd3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007dd/007dd3bc.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046dafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046dafc.md) [`0080b098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b098.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.45% / 新版 82.45%

CFGの説明率　旧版 60.00% / 新版 58.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00937d40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00937d48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00937d48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00937bbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00937b7c"
      ]
    ],
    [
      "unmatched:00937b78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00937bf0"
      ]
    ],
    [
      "unmatched:00937b88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00937bc4"
      ]
    ]
  ],
  "added": [
    [
      "00937bbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00937bd0"
      ]
    ],
    [
      "00937bcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00937bf0"
      ]
    ],
    [
      "00937bdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00937bc4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00937b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/00937ac0.md#insn-00937b34) · [`00937b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/00937ac0.md#insn-00937b78) · [`00937b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/00937ac0.md#insn-00937b88)
- 新版 `00937b88`（命令位置の公開資料なし）

~~~diff
- 00937b34 ["INT_ADD", "register:40f0:8", ["const:937b34:8", "const:4:8"]]
- 00937b34 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00937b88 ["INT_ADD", "register:40f0:8", ["const:937b88:8", "const:4:8"]]
+ 00937b88 ["CALL", null, ["callee:0043bbe4:8"]]
- 00937b34 bytes 1c10ec97
+ 00937b88 bytes 1710ec97
- 00937b78 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00937b78 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00937b78 bytes 280100b4
- 00937b88 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00937b88 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00937b88 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00937b88 ["CBRANCH", null, ["local:b13:8", "tmp:2:1"]]
- 00937b88 bytes 4cffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-babb2cee1e9355a4ab06072455441ba7"></a>

### [`0094270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094270c.md) → [`00942760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00942/00942760.md) FUN_00942760

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`0093f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3c4.md) [`0094288c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094288c.md) [`00942f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/00942f94.md) [`00943998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00943/00943998.md) [`00944178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 5件 [`0093f418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093f/0093f418.md) [`009428e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00942/009428e0.md) [`00942fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00942/00942fe8.md) [`009439ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00943/009439ec.md) [`009441cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00944/009441cc.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00942718"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00942718"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00942790"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00942718",
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
      "0094276c",
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

- 旧版 [`00942718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094270c.md#insn-00942718) · [`00942790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094270c.md#insn-00942790)
- 新版 `0094276c`（命令位置の公開資料なし）

~~~diff
- 00942718 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00942718 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00942718 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00942718 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00942718 bytes fa6706a9
+ 0094276c ["COPY", "tmp:0:8", ["register:40d0:8"]]
+ 0094276c ["COPY", "tmp:1:8", ["register:40c8:8"]]
+ 0094276c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
+ 0094276c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0094276c bytes fa6706a9
- 00942790 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00942790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00942790 bytes 0001803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c707613f1d06612ab2d6ee80a4b03e2c"></a>

### [`009612bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009612bc.md) → [`00961310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00961/00961310.md) FUN_00961310

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`009781a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00978/009781a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`009781fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00978/009781fc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 99.31% / 新版 99.31%

CFGの説明率　旧版 67.92% / 新版 64.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00961408"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009613dc"
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
      "unmatched:00961408",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bb60"
      ]
    ]
  ],
  "added": [
    [
      "009613dc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bb60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009613dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009612bc.md#insn-009613dc) · [`00961408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009612bc.md#insn-00961408)
- 新版 `00961430`（命令位置の公開資料なし） · `009613dc`（命令位置の公開資料なし）

~~~diff
- 009613dc ["INT_ADD", "register:40f0:8", ["const:9613dc:8", "const:4:8"]]
- 009613dc ["CALL", null, ["callee:0043bb60:8"]]
+ 00961430 ["INT_ADD", "register:40f0:8", ["const:961430:8", "const:4:8"]]
+ 00961430 ["CALL", null, ["callee:0043bb60:8"]]
- 009613dc bytes d169eb97
+ 00961430 bytes cc69eb97
+ 009613dc ["INT_ADD", "register:40f0:8", ["const:9613dc:8", "const:4:8"]]
+ 009613dc ["CALL", null, ["callee:0043bb60:8"]]
+ 009613dc bytes e169eb97
- 00961408 ["INT_ADD", "register:40f0:8", ["const:961408:8", "const:4:8"]]
- 00961408 ["CALL", null, ["callee:0043bb60:8"]]
- 00961408 bytes c669eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1b6ea082048f9dc8f531ea226b63ca3"></a>

### [`0097d978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d978.md) → [`0097d9cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097d/0097d9cc.md) FUN_0097d9cc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097d990"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0097d9e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0097d998"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097d990",
      "DATA",
      [
        "storage",
        "00c87ee8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0097d994",
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
      "0097d9e4",
      "DATA",
      [
        "storage",
        "00c87fb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097d9e8",
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

- 旧版 [`0097d990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d978.md#insn-0097d990) · [`0097d998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d978.md#insn-0097d998)
- 新版 `0097d9e4`（命令位置の公開資料なし）

~~~diff
- 0097d990 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0097d990 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0097d990 bytes 080000f9
- 0097d998 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0097d998 ["RETURN", null, ["register:0:8"]]
- 0097d998 bytes c0035fd6
+ 0097d9e4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0097d9e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0097d9e4 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecb135f2438e1329ec588f12c926aef4"></a>

### [`0097f77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f77c.md) → [`0097f7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097f/0097f7d0.md) FUN_0097f7d0

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00980868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980868.md) · 呼出先 3件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00981720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981720.md)
- 新版 呼出元 1件 [`009808bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00980/009808bc.md) · 呼出先 3件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00981774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/00981774.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.29% / 新版 84.29%

CFGの説明率　旧版 59.46% / 新版 57.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f7e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f7e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f7e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097f7e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097f7e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097f7f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0048cec4"
      ]
    ]
  ],
  "added": [
    [
      "0097f838",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0097f83c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0097f848",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0048cec4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097f7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f77c.md#insn-0097f7e4) · [`0097f7e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f77c.md#insn-0097f7e8) · [`0097f7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f77c.md#insn-0097f7f4)

~~~diff
- 0097f7e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0097f7e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0097f7e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0097f7e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097f7e4 bytes fd7b01a9
- 0097f7e8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0097f7e8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0097f7e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0097f7e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097f7e8 bytes f44f02a9
- 0097f7f4 ["INT_ADD", "register:40f0:8", ["const:97f7f4:8", "const:4:8"]]
- 0097f7f4 ["CALL", null, ["callee:0048cec4:8"]]
- 0097f7f4 bytes a435ec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae8e1fe2b718a564c3ae33740297b59d"></a>

### [`00980738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980738.md) → [`0098078c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00980/0098078c.md) FUN_0098078c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 38.46% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00980768"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "009807bc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00980768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980738.md#insn-00980768) · [`0098074c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980738.md#insn-0098074c)
- 新版 `009807bc`（命令位置の公開資料なし） · `009807a0`（命令位置の公開資料なし）

~~~diff
- 00980768 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00980768 ["RETURN", null, ["register:0:8"]]
- 00980768 bytes c0035fd6
+ 009807bc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 009807bc ["RETURN", null, ["register:0:8"]]
+ 009807bc bytes c0035fd6
- 0098074c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 0098074c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0098074c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0098074c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 009807a0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 009807a0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 009807a0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 009807a0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 0098074c bytes 08010037
+ 009807a0 bytes 08010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-455f480308b9549340e5f08ee5618a7a"></a>

### [`009807e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/009807e0.md) → [`00980834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00980/00980834.md) FUN_00980834

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009807fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00980850"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`009807fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/009807e0.md#insn-009807fc) · [`009807e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/009807e0.md#insn-009807e8)
- 新版 `00980850`（命令位置の公開資料なし） · `0098083c`（命令位置の公開資料なし）

~~~diff
- 009807fc ["COPY", "register:0:8", ["register:40f0:8"]]
- 009807fc ["RETURN", null, ["register:0:8"]]
- 009807fc bytes c0035fd6
+ 00980850 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00980850 ["RETURN", null, ["register:0:8"]]
+ 00980850 bytes c0035fd6
- 009807e8 ["INT_ADD", "register:40f0:8", ["const:9807e8:8", "const:4:8"]]
- 009807e8 ["CALL", null, ["callee:00851550:8"]]
+ 0098083c ["INT_ADD", "register:40f0:8", ["const:98083c:8", "const:4:8"]]
+ 0098083c ["CALL", null, ["callee:00851550:8"]]
- 009807e8 bytes 4443fb97
+ 0098083c bytes 4543fb97
~~~


<a id="compare-52af99fc6659b92f6fe3d45c1efb0500"></a>

### [`00980800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980800.md) → [`00980854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00980/00980854.md) FUN_00980854

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`00980868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`006103fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00610/006103fc.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 2件 [`009808bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00980/009808bc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 40.00% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980804"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980800",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980804",
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
      "00980854",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00980858",
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

- 旧版 [`00980800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980800.md#insn-00980800) · [`00980804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980800.md#insn-00980804)
- 新版 `00980854`（命令位置の公開資料なし）

~~~diff
- 00980800 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00980800 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00980800 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00980800 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00980800 bytes fd7bbda9
- 00980804 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00980804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00980804 bytes f50b00f9
+ 00980854 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00980854 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00980854 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
+ 00980854 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00980854 bytes fd7bbda9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfef164a939e0e65f6f941e62ba06b41"></a>

### [`009811a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/009811a4.md) → [`009811f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/009811f8.md) FUN_009811f8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 4件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`0075ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075ba1c.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009811a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009811a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009811a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009811a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:009811a8",
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
      "009811f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "009811fc",
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

- 旧版 [`009811a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/009811a4.md#insn-009811a4) · [`009811a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/009811a4.md#insn-009811a8) · [`009811f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/009811a4.md#insn-009811f8)
- 新版 `0098124c`（命令位置の公開資料なし）

~~~diff
- 009811a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009811a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009811a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 009811a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009811a4 bytes fd7bbca9
- 009811a8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009811a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 009811a8 bytes f70b00f9
- 009811f8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009811f8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0098124c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 0098124c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 009811f8 bytes 48ffffb5
+ 0098124c bytes 48ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec25bfd06abc83edd0c4cb71a7fb7b45"></a>

### [`0098126c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/0098126c.md) → [`009812c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/009812c0.md) FUN_009812c0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`006103fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00610/006103fc.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 10.53% / 新版 10.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981314"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00981368"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009812b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009812b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009812f0"
      ]
    ],
    [
      "unmatched:009812c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009812fc"
      ]
    ]
  ],
  "added": [
    [
      "00981308",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009812f0"
      ]
    ],
    [
      "00981314",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009812fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009812b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/0098126c.md#insn-009812b4) · [`009812c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/0098126c.md#insn-009812c0) · [`00981308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/0098126c.md#insn-00981308)
- 新版 `0098135c`（命令位置の公開資料なし）

~~~diff
- 009812b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009812b4 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 009812b4 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 009812b4 ["CBRANCH", null, ["local:b2:8", "tmp:2:1"]]
- 009812b4 bytes 4cffff54
- 009812c0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009812c0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 009812c0 bytes 48ffffb5
- 00981308 ["INT_ADD", "register:40f0:8", ["const:981308:8", "const:4:8"]]
- 00981308 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0098135c ["INT_ADD", "register:40f0:8", ["const:98135c:8", "const:4:8"]]
+ 0098135c ["CALL", null, ["callee:0043bbe4:8"]]
- 00981308 bytes 27eaea97
+ 0098135c bytes 22eaea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7275fc9846c239368e682aea242814ea"></a>

### [`009816cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/009816cc.md) → [`00981720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/00981720.md) FUN_00981720

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 2件 [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md) [`0086a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4b0.md)
- 新版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 2件 [`0086a4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a4b8.md) [`0086a508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a508.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009816e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/009816cc.md#insn-009816e8) · [`009816f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/009816cc.md#insn-009816f4) · [`00981700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/009816cc.md#insn-00981700)
- 新版 `0098173c`（命令位置の公開資料なし） · `00981754`（命令位置の公開資料なし）

~~~diff
- 009816e8 ["INT_ADD", "register:40f0:8", ["const:9816e8:8", "const:4:8"]]
- 009816e8 ["CALL", null, ["callee:0086a4b8:8"]]
+ 0098173c ["INT_ADD", "register:40f0:8", ["const:98173c:8", "const:4:8"]]
+ 0098173c ["CALL", null, ["callee:0086a4b8:8"]]
- 009816e8 bytes 5ea3fb97
+ 0098173c bytes 5fa3fb97
- 009816f4 ["INT_SUB", "register:4000:8", ["register:4098:8", "const:8:8"]]
- 009816f4 bytes 602200d1
- 00981700 ["INT_ADD", "register:40f0:8", ["const:981700:8", "const:4:8"]]
- 00981700 ["CALL", null, ["callee:0086a508:8"]]
+ 00981754 ["INT_ADD", "register:40f0:8", ["const:981754:8", "const:4:8"]]
+ 00981754 ["CALL", null, ["callee:0086a508:8"]]
- 00981700 bytes 6ca3fb97
+ 00981754 bytes 6da3fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8335d22a570e5abcc992aed9c97837a9"></a>

### [`00981720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981720.md) → [`00981774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/00981774.md) FUN_00981774

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0097f77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f77c.md) [`0097fb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097fb20.md) [`00980e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980e10.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 3件 [`0097f7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097f/0097f7d0.md) [`0097fb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097f/0097fb74.md) [`00980e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00980/00980e64.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981728"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981728"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0098177c"
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
      "unmatched:00981728",
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
      "0098177c",
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

- 旧版 [`00981728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981720.md#insn-00981728) · [`009817fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981720.md#insn-009817fc)
- 新版 `0098177c`（命令位置の公開資料なし）

~~~diff
- 00981728 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00981728 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00981728 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00981728 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00981728 bytes f85f02a9
+ 0098177c ["COPY", "tmp:0:8", ["register:40c0:8"]]
+ 0098177c ["COPY", "tmp:1:8", ["register:40b8:8"]]
+ 0098177c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
+ 0098177c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0098177c bytes f85f02a9
- 009817fc ["COPY", "tmp:0:4", ["register:4040:4"]]
- 009817fc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 009817fc ["COPY", "tmp:0:4", ["register:4048:4"]]
- 009817fc ["INT_ZEXT", "register:4040:8", ["tmp:0:4"]]
- 009817fc bytes 0801891a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e90c306801ee4bcad52f2d6144cf3bba"></a>

### [`00981828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981828.md) → [`0098187c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/0098187c.md) FUN_0098187c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098184c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098184c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009818a0"
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
      "unmatched:0098184c",
      "DATA",
      [
        "storage",
        "00c88000",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00981850",
      "READ",
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
      "009818a0",
      "DATA",
      [
        "storage",
        "00c880d0",
        null,
        "undefined *"
      ]
    ],
    [
      "009818a4",
      "READ",
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

- 旧版 [`0098184c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981828.md#insn-0098184c) · [`0098183c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981828.md#insn-0098183c)
- 新版 `009818a0`（命令位置の公開資料なし） · `00981890`（命令位置の公開資料なし）

~~~diff
- 0098184c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0098184c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0098184c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0098184c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0098184c bytes 082400a9
+ 009818a0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009818a0 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 009818a0 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 009818a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 009818a0 bytes 082400a9
- 0098183c ["INT_ADD", "register:40f0:8", ["const:98183c:8", "const:4:8"]]
- 0098183c ["CALL", null, ["callee:00c57f60:8"]]
+ 00981890 ["INT_ADD", "register:40f0:8", ["const:981890:8", "const:4:8"]]
+ 00981890 ["CALL", null, ["callee:00c57f60:8"]]
- 0098183c bytes 95590b94
+ 00981890 bytes b4590b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-670d87e1d58899c748c93e8f2175b34c"></a>

### [`00981fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981fc0.md) → [`00982014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00982/00982014.md) FUN_00982014

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00981dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981dbc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00981e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/00981e10.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 85.71% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981fc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981fc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981fc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981fc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981fc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981fc8",
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
      "00982014",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00982018",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0098201c",
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

- 旧版 [`00981fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981fc0.md#insn-00981fc0) · [`00981fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981fc0.md#insn-00981fc4) · [`00981fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981fc0.md#insn-00981fc8)

~~~diff
- 00981fc0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00981fc0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00981fc0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00981fc0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00981fc0 bytes fd7bbca9
- 00981fc4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00981fc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00981fc4 bytes f70b00f9
- 00981fc8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00981fc8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00981fc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00981fc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00981fc8 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d016395c5d00db0605e22d5a5835ee9"></a>

### [`009822fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009822fc.md) → [`00982350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00982/00982350.md) FUN_00982350

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009821cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821cc.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00982220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00982/00982220.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00982334"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009823d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00982388"
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
      "unmatched:009823d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009823a0"
      ]
    ]
  ],
  "added": [
    [
      "00982428",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009823a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00982334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009822fc.md#insn-00982334) · [`00982380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009822fc.md#insn-00982380)
- 新版 `009823d4`（命令位置の公開資料なし） · `00982388`（命令位置の公開資料なし）

~~~diff
- 00982334 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00982334 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00982334 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00982334 ["INT_ADD", "tmp:1:8", ["register:4010:8", "const:1:8"]]
- 00982334 bytes 9515829a
- 00982380 ["INT_ADD", "register:40f0:8", ["const:982380:8", "const:4:8"]]
- 00982380 ["CALL", null, ["callee:00c58120:8"]]
+ 009823d4 ["INT_ADD", "register:40f0:8", ["const:9823d4:8", "const:4:8"]]
+ 009823d4 ["CALL", null, ["callee:00c58120:8"]]
- 00982380 bytes 34570b94
+ 009823d4 bytes 53570b94
+ 00982388 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00982388 ["COPY", "tmp:1:8", ["register:4060:8"]]
+ 00982388 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00982388 ["INT_ADD", "tmp:1:8", ["register:4010:8", "const:1:8"]]
+ 00982388 bytes 9515829a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cea9fa0ee51d6eb0de4da66859230ec"></a>

### [`00982400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982400.md) → [`00982454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00982/00982454.md) FUN_00982454

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00982408"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0098245c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098240c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098240c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009824a0"
      ]
    ]
  ],
  "added": [
    [
      "00982460",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009824a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00982408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982400.md#insn-00982408) · [`0098240c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982400.md#insn-0098240c)
- 新版 `0098245c`（命令位置の公開資料なし）

~~~diff
- 00982408 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00982408 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00982408 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00982408 bytes 1f0100f9
- 0098240c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0098240c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0098240c bytes 000200b4
+ 0098245c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0098245c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 0098245c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 0098245c bytes 1f0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7d49d2bf24b7be3f8fc8b9f137b41fa"></a>

### [`00982450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982450.md) → [`009824a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00982/009824a4.md) FUN_009824a4

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097fb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097fb20.md) · 呼出先 5件 [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md) [`009826e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009826e0.md) [`00982840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982840.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)
- 新版 呼出元 1件 [`0097fb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097f/0097fb74.md) · 呼出先 5件 [`0086a4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a4b8.md) [`00982734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00982/00982734.md) [`00982894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00982/00982894.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58500.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.23% / 新版 83.23%

CFGの説明率　旧版 48.84% / 新版 49.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009824d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00982544"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00982554"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009824d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00982554"
      ]
    ],
    [
      "unmatched:009824d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00982574"
      ]
    ],
    [
      "unmatched:009824e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009824dc"
      ]
    ]
  ],
  "added": [
    [
      "00982524",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00982554"
      ]
    ],
    [
      "0098252c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00982574"
      ]
    ],
    [
      "00982538",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00982530"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009824d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982450.md#insn-009824d0) · [`009824d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982450.md#insn-009824d4) · [`009824d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982450.md#insn-009824d8)

~~~diff
- 009824d0 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 009824d0 bytes 80010054
- 009824d4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:8:8"]]
- 009824d4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 009824d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 009824d4 bytes ff0600f9
- 009824d8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009824d8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 009824d8 bytes 480200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ba38455a7ffc6064ea1b4f534c588ab"></a>

### [`009826e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009826e0.md) → [`00982734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00982/00982734.md) FUN_00982734

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00982450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982450.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`009824a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00982/009824a4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 16.67% / 新版 15.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009826e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009826e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009826e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009826e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:009826e4",
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
      "00982734",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00982738",
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

- 旧版 [`009826e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009826e0.md#insn-009826e0) · [`009826e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009826e0.md#insn-009826e4)
- 新版 `00982734`（命令位置の公開資料なし）

~~~diff
- 009826e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009826e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009826e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 009826e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009826e0 bytes fd7bbca9
- 009826e4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 009826e4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 009826e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 009826e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009826e4 bytes f85f01a9
+ 00982734 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00982734 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00982734 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
+ 00982734 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00982734 bytes fd7bbca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e27a93537f3eccab8e4f60b39497cfa"></a>

### [`009827e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009827e8.md) → [`0098283c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00982/0098283c.md) FUN_0098283c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0086a4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a4b8.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009827ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00982840"
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
      "unmatched:009827ec",
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
      "00982840",
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

- 旧版 [`009827ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009827e8.md#insn-009827ec) · [`00982800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009827e8.md#insn-00982800)
- 新版 `00982840`（命令位置の公開資料なし） · `00982854`（命令位置の公開資料なし）

~~~diff
- 009827ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009827ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009827ec bytes f30b00f9
+ 00982840 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 00982840 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00982840 bytes f30b00f9
- 00982800 ["INT_ADD", "register:40f0:8", ["const:982800:8", "const:4:8"]]
- 00982800 ["CALL", null, ["callee:0086a4b8:8"]]
+ 00982854 ["INT_ADD", "register:40f0:8", ["const:982854:8", "const:4:8"]]
+ 00982854 ["CALL", null, ["callee:0086a4b8:8"]]
- 00982800 bytes 189ffb97
+ 00982854 bytes 199ffb97
~~~


<a id="compare-ad50d30422d0377fb7a6d3652ec4dda3"></a>

### [`0098ced4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098c/0098ced4.md) → [`0098cf28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098c/0098cf28.md) FUN_0098cf28

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) [`0099ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0099b/0099ba70.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00997090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00997/00997090.md) [`0099bac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0099b/0099bac4.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 85.71% / 新版 88.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098cf58"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0098cfac"
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
      "unmatched:0098cf58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098cfb8"
      ]
    ]
  ],
  "added": [
    [
      "0098cfac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098cfb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098cf58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098c/0098ced4.md#insn-0098cf58) · [`0098ced8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098c/0098ced4.md#insn-0098ced8)
- 新版 `0098cfac`（命令位置の公開資料なし） · `0098cf2c`（命令位置の公開資料なし）

~~~diff
- 0098cf58 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0098cf58 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0098cf58 ["CBRANCH", null, ["local:b14:8", "tmp:1:1"]]
- 0098cf58 bytes 68000054
+ 0098cfac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0098cfac ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 0098cfac ["CBRANCH", null, ["local:b13:8", "tmp:1:1"]]
+ 0098cfac bytes 68000054
- 0098ced8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0098ced8 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 0098cf2c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 0098cf2c ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 0098ced8 bytes 280500b4
+ 0098cf2c bytes 280500b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3243038d321abc43809856d44f2c4edf"></a>

### [`00996b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00996/00996b58.md) → [`00996bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00996/00996bac.md) FUN_00996bac

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0098dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098d/0098dc5c.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.80% / 新版 89.80%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00996c00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00996c54"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00996ba8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00996ba8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00996c58"
      ]
    ],
    [
      "unmatched:00996bb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00996be8"
      ]
    ]
  ],
  "added": [
    [
      "00996bfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00996c58"
      ]
    ],
    [
      "00996c04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00996be8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00996ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00996/00996b58.md#insn-00996ba8) · [`00996bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00996/00996b58.md#insn-00996bb0) · [`00996bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00996/00996b58.md#insn-00996bfc)

~~~diff
- 00996ba8 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00996ba8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00996ba8 bytes ea020054
- 00996bb0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00996bb0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00996bb0 bytes 28ffffb5
- 00996bfc ["COPY", "tmp:0:8", ["const:1:8"]]
- 00996bfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00996bfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00996bfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00996bfc bytes 08050091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e06ef2bb36639b5bfe15b6bc9153da4"></a>

### [`009a137c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a1/009a137c.md) → [`009a13d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a1/009a13d0.md) FUN_009a13d0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) [`0099ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0099b/0099ba70.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 2件 [`00997090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00997/00997090.md) [`0099bac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0099b/0099bac4.md) · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.09% / 新版 89.09%

CFGの説明率　旧版 40.00% / 新版 41.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a13f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a1400"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a1440"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009a1434",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009a13f8"
      ]
    ],
    [
      "unmatched:009a13f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a1480"
      ]
    ],
    [
      "unmatched:009a1400",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a1438"
      ]
    ]
  ],
  "added": [
    [
      "009a1434",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "009a144c"
      ]
    ],
    [
      "009a1448",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a1480"
      ]
    ],
    [
      "009a1454",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a1438"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a13f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a1/009a137c.md#insn-009a13f4) · [`009a1400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a1/009a137c.md#insn-009a1400) · [`009a1440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a1/009a137c.md#insn-009a1440)

~~~diff
- 009a13f4 ["INT_EQUAL", "tmp:0:1", ["register:4068:8", "const:0:8"]]
- 009a13f4 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 009a13f4 bytes cd0100b4
- 009a1400 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 009a1400 bytes 20ffff54
- 009a1440 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 009a1440 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 009a1440 bytes 890000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d7b4baf490261dd9da70f698cb0aaeb"></a>

### [`009a2c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2c84.md) → [`009a2cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a2/009a2cd8.md) FUN_009a2cd8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009a2b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2b34.md) · 呼出先 0件 
- 新版 呼出元 1件 [`009a2b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a2/009a2b88.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 74.03% / 新版 74.03%

CFGの説明率　旧版 27.27% / 新版 25.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a2cd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a2d00"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a2d04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a2cd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a2d1c"
      ]
    ],
    [
      "009a2d40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009a2cfc"
      ]
    ],
    [
      "unmatched:009a2cf8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009a2d0c"
      ]
    ]
  ],
  "added": [
    [
      "009a2d28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a2d1c"
      ]
    ],
    [
      "009a2d40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a2d50"
      ]
    ],
    [
      "009a2d4c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "009a2d60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a2cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2c84.md#insn-009a2cd4) · [`009a2d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2c84.md#insn-009a2d00) · [`009a2d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2c84.md#insn-009a2d04)

~~~diff
- 009a2cd4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009a2cd4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 009a2cd4 bytes a1ffff54
- 009a2d00 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 009a2d00 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 009a2d00 bytes 63000054
- 009a2d04 ["COPY", "tmp:0:8", ["const:0:8"]]
- 009a2d04 ["INT_EQUAL", "tmp:1:1", ["register:4050:8", "const:0:8"]]
- 009a2d04 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 009a2d04 ["INT_DIV", "tmp:0:8", ["register:4078:8", "register:4050:8"]]
- 009a2d04 bytes f009ca9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dc295bdbd574a495605eec7ca906483"></a>

### [`009a2dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2dbc.md) → [`009a2e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a2/009a2e10.md) FUN_009a2e10

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a2de0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a2de0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009a2e34"
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
      "unmatched:009a2de0",
      "DATA",
      [
        "storage",
        "00c88080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a2e34",
      "DATA",
      [
        "storage",
        "00c88150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a2de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2dbc.md#insn-009a2de0) · [`009a2dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2dbc.md#insn-009a2dd0)
- 新版 `009a2e34`（命令位置の公開資料なし） · `009a2e24`（命令位置の公開資料なし）

~~~diff
- 009a2de0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009a2de0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 009a2de0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 009a2de0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009a2de0 bytes 082400a9
+ 009a2e34 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009a2e34 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 009a2e34 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 009a2e34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 009a2e34 bytes 082400a9
- 009a2dd0 ["INT_ADD", "register:40f0:8", ["const:9a2dd0:8", "const:4:8"]]
- 009a2dd0 ["CALL", null, ["callee:00c57f60:8"]]
+ 009a2e24 ["INT_ADD", "register:40f0:8", ["const:9a2e24:8", "const:4:8"]]
+ 009a2e24 ["CALL", null, ["callee:00c57f60:8"]]
- 009a2dd0 bytes 30d40a94
+ 009a2e24 bytes 4fd40a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50d843d02ebed957bcabb78be601e5df"></a>

### [`009a31b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a31b0.md) → [`009a3204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a3204.md) FUN_009a3204

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 10.00% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a31b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a31b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a31b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a31b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a31b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a31d4",
      "DATA",
      [
        "storage",
        "00c88110",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a3204",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009a3208",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009a3228",
      "DATA",
      [
        "storage",
        "00c881e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a31b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a31b0.md#insn-009a31b0) · [`009a31b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a31b0.md#insn-009a31b4) · [`009a31d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a31b0.md#insn-009a31d4)

~~~diff
- 009a31b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009a31b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009a31b0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009a31b0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009a31b0 bytes fd7bbea9
- 009a31b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009a31b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009a31b4 bytes f30b00f9
- 009a31d4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009a31d4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 009a31d4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 009a31d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009a31d4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efd6b553b4cb481b1d3da710e433fd0a"></a>

### [`009a3200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3200.md) → [`009a3254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a3254.md) FUN_009a3254

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`009c7784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7784.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`009c77d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009c7/009c77d8.md)

変更の種類 constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 23.08% / 新版 23.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009a3258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3200.md#insn-009a3258) · [`009a3284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3200.md#insn-009a3284) · [`009a32a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3200.md#insn-009a32a0)
- 新版 `009a32d8`（命令位置の公開資料なし） · `009a32f4`（命令位置の公開資料なし）

~~~diff
- 009a3258 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3:8"]]
- 009a3258 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 009a3258 ["INT_ZEXT", "register:4060:8", ["tmp:1:1"]]
- 009a3258 bytes 2c0d4039
- 009a3284 ["INT_ADD", "register:40f0:8", ["const:9a3284:8", "const:4:8"]]
- 009a3284 ["CALL", null, ["callee:009c77d8:8"]]
+ 009a32d8 ["INT_ADD", "register:40f0:8", ["const:9a32d8:8", "const:4:8"]]
+ 009a32d8 ["CALL", null, ["callee:009c77d8:8"]]
- 009a3284 bytes 40910094
+ 009a32d8 bytes 40910094
- 009a32a0 ["INT_ADD", "register:40f0:8", ["const:9a32a0:8", "const:4:8"]]
- 009a32a0 ["CALL", null, ["callee:00467ba0:8"]]
+ 009a32f4 ["INT_ADD", "register:40f0:8", ["const:9a32f4:8", "const:4:8"]]
+ 009a32f4 ["CALL", null, ["callee:00467ba0:8"]]
- 009a32a0 bytes 3012eb97
+ 009a32f4 bytes 2b12eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccac9d7cc144cb28d4aa5de115e915fc"></a>

### [`009a32e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a32e8.md) → [`009a333c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a333c.md) FUN_009a333c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 83.33% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a330c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a330c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009a3360"
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
      "unmatched:009a330c",
      "DATA",
      [
        "storage",
        "00c88190",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009a3310",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a3314",
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
      "009a3360",
      "DATA",
      [
        "storage",
        "00c88260",
        null,
        "undefined *"
      ]
    ],
    [
      "009a3364",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009a3368",
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

- 旧版 [`009a330c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a32e8.md#insn-009a330c) · [`009a3318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a32e8.md#insn-009a3318)
- 新版 `009a3360`（命令位置の公開資料なし）

~~~diff
- 009a330c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009a330c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 009a330c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 009a330c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009a330c bytes 082400a9
- 009a3318 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009a3318 ["RETURN", null, ["register:0:8"]]
- 009a3318 bytes c0035fd6
+ 009a3360 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009a3360 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 009a3360 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 009a3360 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 009a3360 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecbb824aeb53db81b30468c3a7676e58"></a>

### [`009a3554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3554.md) → [`009a35a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a35a8.md) FUN_009a35a8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009a35cc",
      "DATA",
      [
        "storage",
        "00c88210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a35cc",
      "DATA",
      [
        "storage",
        "00c882e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a3568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3554.md#insn-009a3568) · [`009a3574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3554.md#insn-009a3574)
- 新版 `009a35bc`（命令位置の公開資料なし） · `009a35c8`（命令位置の公開資料なし）

~~~diff
- 009a3568 ["INT_ADD", "register:40f0:8", ["const:9a3568:8", "const:4:8"]]
- 009a3568 ["CALL", null, ["callee:00c57f60:8"]]
+ 009a35bc ["INT_ADD", "register:40f0:8", ["const:9a35bc:8", "const:4:8"]]
+ 009a35bc ["CALL", null, ["callee:00c57f60:8"]]
- 009a3568 bytes 4ad20a94
+ 009a35bc bytes 69d20a94
- 009a3574 ["COPY", "tmp:0:8", ["const:210:8"]]
- 009a3574 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a3574 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a3574 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a3574 bytes 08410891
+ 009a35c8 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 009a35c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a35c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a35c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a35c8 bytes 08810b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94b5b9e2443b3b4c3f8d84906925cc43"></a>

### [`009a38b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a38b4.md) → [`009a3908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a3908.md) FUN_009a3908

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 40.00% / 新版 40.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a38c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a38c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009a3914"
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
      "unmatched:009a38c0",
      "DATA",
      [
        "storage",
        "00c88310",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a3914",
      "DATA",
      [
        "storage",
        "00c883e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a38c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a38b4.md#insn-009a38c0) · [`009a38b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a38b4.md#insn-009a38b8)
- 新版 `009a3914`（命令位置の公開資料なし）

~~~diff
- 009a38c0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009a38c0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 009a38c0 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 009a38c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009a38c0 bytes 292000a9
+ 009a3914 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 009a3914 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 009a3914 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 009a3914 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 009a3914 bytes 292000a9
- 009a38b8 ["COPY", "register:4048:8", ["const:c88000:8"]]
- 009a38b8 bytes 291700b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9222e145fac7cd2a2a07d43c912b0752"></a>

### [`009a3a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3a34.md) → [`009a3a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a3a88.md) FUN_009a3a88

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a3a34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a3a34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a3a38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a3a34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a3a38",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a3a58",
      "DATA",
      [
        "storage",
        "00c88410",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a3a88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009a3a8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009a3aac",
      "DATA",
      [
        "storage",
        "00c884e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a3a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3a34.md#insn-009a3a34) · [`009a3a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3a34.md#insn-009a3a38) · [`009a3a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3a34.md#insn-009a3a58)

~~~diff
- 009a3a34 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009a3a34 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009a3a34 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009a3a34 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009a3a34 bytes fd7bbea9
- 009a3a38 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009a3a38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009a3a38 bytes f30b00f9
- 009a3a58 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009a3a58 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 009a3a58 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 009a3a58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009a3a58 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe5ab6b8de25fb837b4c275753f2ad73"></a>

### [`009a3ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3ac8.md) → [`009a3b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a3b1c.md) FUN_009a3b1c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009a3ae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "009a3b3c"
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
      "009a3b34",
      "DATA",
      [
        "storage",
        "00c88490",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009a3ae4",
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
      "009a3b34",
      "DATA",
      [
        "storage",
        "00c88560",
        null,
        "undefined *"
      ]
    ],
    [
      "009a3b38",
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

- 旧版 [`009a3ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3ac8.md#insn-009a3ae8) · [`009a3ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3ac8.md#insn-009a3ad4)
- 新版 `009a3b3c`（命令位置の公開資料なし） · `009a3b28`（命令位置の公開資料なし）

~~~diff
- 009a3ae8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009a3ae8 ["RETURN", null, ["register:0:8"]]
- 009a3ae8 bytes c0035fd6
+ 009a3b3c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 009a3b3c ["RETURN", null, ["register:0:8"]]
+ 009a3b3c bytes c0035fd6
- 009a3ad4 ["INT_ADD", "register:40f0:8", ["const:9a3ad4:8", "const:4:8"]]
- 009a3ad4 ["CALL", null, ["callee:00c57f60:8"]]
+ 009a3b28 ["INT_ADD", "register:40f0:8", ["const:9a3b28:8", "const:4:8"]]
+ 009a3b28 ["CALL", null, ["callee:00c57f60:8"]]
- 009a3ad4 bytes efd00a94
+ 009a3b28 bytes 0ed10a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beb2702eb127a6a143f254bcf548b0ed"></a>

### [`009a3b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3b04.md) → [`009a3b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a3b58.md) FUN_009a3b58

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 20.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "009a3b28"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009a3b7c"
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
      "unmatched:009a3b28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "009a3b7c",
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

- 旧版 [`009a3b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3b04.md#insn-009a3b28) · [`009a3b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3b04.md#insn-009a3b0c)
- 新版 `009a3b7c`（命令位置の公開資料なし） · `009a3b60`（命令位置の公開資料なし）

~~~diff
- 009a3b28 ["INT_ADD", "register:40f0:8", ["const:9a3b28:8", "const:4:8"]]
- 009a3b28 ["CALL", null, ["ram:47acf4:8"]]
- 009a3b28 bytes 735ceb97
+ 009a3b7c ["INT_ADD", "register:40f0:8", ["const:9a3b7c:8", "const:4:8"]]
+ 009a3b7c ["CALL", null, ["ram:47ad34:8"]]
+ 009a3b7c bytes 6e5ceb97
- 009a3b0c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009a3b0c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 009a3b60 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009a3b60 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 009a3b0c bytes e1010054
+ 009a3b60 bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb2b91fb9a7543c7736a7ebeba045e21"></a>

### [`009a3bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3bb4.md) → [`009a3c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a3c08.md) FUN_009a3c08

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a3bbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009a3c10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "009a3bd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a3bbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a3c4c"
      ]
    ],
    [
      "unmatched:009a3bd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "009a3c10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a3c4c"
      ]
    ],
    [
      "009a3c2c",
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

- 旧版 [`009a3bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3bb4.md#insn-009a3bbc) · [`009a3bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3bb4.md#insn-009a3bd8)
- 新版 `009a3c10`（命令位置の公開資料なし）

~~~diff
- 009a3bbc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009a3bbc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 009a3bbc bytes e1010054
- 009a3bd8 ["INT_ADD", "register:40f0:8", ["const:9a3bd8:8", "const:4:8"]]
- 009a3bd8 ["CALL", null, ["ram:47acf4:8"]]
- 009a3bd8 bytes 475ceb97
+ 009a3c10 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009a3c10 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 009a3c10 bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-297ab5d2d18289a3fcc1bd55a96df3c8"></a>

### [`009a3c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3c4c.md) → [`009a3ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a3ca0.md) FUN_009a3ca0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a3c54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009a3ca8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009a3c58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a3c54",
      "DATA",
      [
        "storage",
        "00c88590",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a3ca8",
      "DATA",
      [
        "storage",
        "00c88660",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a3c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3c4c.md#insn-009a3c54) · [`009a3c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3c4c.md#insn-009a3c58)
- 新版 `009a3ca8`（命令位置の公開資料なし）

~~~diff
- 009a3c54 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 009a3c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009a3c54 bytes 280000f9
- 009a3c58 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009a3c58 ["RETURN", null, ["register:0:8"]]
- 009a3c58 bytes c0035fd6
+ 009a3ca8 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 009a3ca8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009a3ca8 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfaa8f8979029d831a079dfe5db18d5d"></a>

### [`009a4480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a4/009a4480.md) → [`009a44d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a44d4.md) FUN_009a44d4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) [`0098dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098d/0098dc5c.md) [`00997090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00997/00997090.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009a4494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a4/009a4480.md#insn-009a4494) · [`009a44a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a4/009a4480.md#insn-009a44a8) · [`009a44b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a4/009a4480.md#insn-009a44b8)
- 新版 `009a44e8`（命令位置の公開資料なし） · `009a44fc`（命令位置の公開資料なし） · `009a450c`（命令位置の公開資料なし）

~~~diff
- 009a4494 ["INT_ADD", "register:40f0:8", ["const:9a4494:8", "const:4:8"]]
- 009a4494 ["CALL", null, ["callee:00851550:8"]]
+ 009a44e8 ["INT_ADD", "register:40f0:8", ["const:9a44e8:8", "const:4:8"]]
+ 009a44e8 ["CALL", null, ["callee:00851550:8"]]
- 009a4494 bytes 19b4fa97
+ 009a44e8 bytes 1ab4fa97
- 009a44a8 ["INT_ADD", "register:40f0:8", ["const:9a44a8:8", "const:4:8"]]
- 009a44a8 ["CALL", null, ["callee:00851550:8"]]
+ 009a44fc ["INT_ADD", "register:40f0:8", ["const:9a44fc:8", "const:4:8"]]
+ 009a44fc ["CALL", null, ["callee:00851550:8"]]
- 009a44a8 bytes 14b4fa97
+ 009a44fc bytes 15b4fa97
- 009a44b8 ["INT_ADD", "register:40f0:8", ["const:9a44b8:8", "const:4:8"]]
- 009a44b8 ["CALL", null, ["callee:00851550:8"]]
+ 009a450c ["INT_ADD", "register:40f0:8", ["const:9a450c:8", "const:4:8"]]
+ 009a450c ["CALL", null, ["callee:00851550:8"]]
- 009a44b8 bytes 10b4fa97
+ 009a450c bytes 11b4fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74e051d86a5040a37bcc0447f6409c85"></a>

### [`009a50c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a5/009a50c0.md) → [`009a5114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5114.md) FUN_009a5114

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009a4eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a4/009a4eb4.md) · 呼出先 13件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`005a7534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7534.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md) [`00795e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e5c.md)
- 新版 呼出元 1件 [`009a4f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4f08.md) · 呼出先 13件 [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`005a7574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7574.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md) [`00795eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.07% / 新版 86.07%

CFGの説明率　旧版 50.00% / 新版 51.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a50f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a5134"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a518c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a50f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a5134",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009a518c",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009a5144",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "009a5188",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "009a51e0",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a50f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a5/009a50c0.md#insn-009a50f0) · [`009a5134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a5/009a50c0.md#insn-009a5134)
- 新版 `009a5144`（命令位置の公開資料なし）

~~~diff
- 009a50f0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009a50f0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009a50f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009a50f0 bytes a8831ff8
- 009a5134 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 009a5134 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009a5134 bytes a80200f9
+ 009a5144 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009a5144 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 009a5144 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 009a5144 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9950dcfbece18afd8469b4c4afbefd2d"></a>

### [`009a6258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6258.md) → [`009a62ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a62ac.md) FUN_009a62ac

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 62.50% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a6280"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009a62d4"
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
      "unmatched:009a6280",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a62d4",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a6280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6258.md#insn-009a6280) · [`009a626c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6258.md#insn-009a626c)
- 新版 `009a62d4`（命令位置の公開資料なし） · `009a62c0`（命令位置の公開資料なし）

~~~diff
- 009a6280 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 009a6280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009a6280 bytes 680200f9
+ 009a62d4 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 009a62d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009a62d4 bytes 680200f9
- 009a626c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 009a626c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 009a62c0 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 009a62c0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 009a626c bytes 330200b4
+ 009a62c0 bytes 330200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-085d2ad5f1044812c9aba69d08c7fd93"></a>

### [`009a6348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6348.md) → [`009a639c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a639c.md) FUN_009a639c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009a63c0",
      "DATA",
      [
        "storage",
        "00c88610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a63c0",
      "DATA",
      [
        "storage",
        "00c886e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a635c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6348.md#insn-009a635c) · [`009a6368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6348.md#insn-009a6368)
- 新版 `009a63b0`（命令位置の公開資料なし） · `009a63bc`（命令位置の公開資料なし）

~~~diff
- 009a635c ["INT_ADD", "register:40f0:8", ["const:9a635c:8", "const:4:8"]]
- 009a635c ["CALL", null, ["callee:00c57f60:8"]]
+ 009a63b0 ["INT_ADD", "register:40f0:8", ["const:9a63b0:8", "const:4:8"]]
+ 009a63b0 ["CALL", null, ["callee:00c57f60:8"]]
- 009a635c bytes cdc60a94
+ 009a63b0 bytes ecc60a94
- 009a6368 ["COPY", "tmp:0:8", ["const:610:8"]]
- 009a6368 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a6368 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a6368 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a6368 bytes 08411891
+ 009a63bc ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 009a63bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a63bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a63bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a63bc bytes 08811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0158facd4338202a2a3a5d4375b1318b"></a>

### [`009a6824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6824.md) → [`009a6878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6878.md) FUN_009a6878

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 58.33% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a685c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009a68b0"
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
      "unmatched:009a685c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a68c8"
      ]
    ]
  ],
  "added": [
    [
      "009a68b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a68c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a685c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6824.md#insn-009a685c) · [`009a6838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6824.md#insn-009a6838)
- 新版 `009a68b0`（命令位置の公開資料なし） · `009a688c`（命令位置の公開資料なし）

~~~diff
- 009a685c ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 009a685c bytes c0000054
+ 009a68b0 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 009a68b0 bytes c0000054
- 009a6838 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 009a6838 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 009a688c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 009a688c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 009a6838 bytes b40200b4
+ 009a688c bytes b40200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02d6fbf3cca11c1b741de978e51898b5"></a>

### [`009a689c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a689c.md) → [`009a68f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a68f0.md) FUN_009a68f0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009a63a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a63a0.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`009a69e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a69e4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009a63f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a63f4.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`009a6a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6a38.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.46% / 新版 91.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a68c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009a691c"
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
      "unmatched:009a68c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a6a2c"
      ]
    ]
  ],
  "added": [
    [
      "009a691c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a6a2c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a68c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a689c.md#insn-009a68c8) · [`009a68ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a689c.md#insn-009a68ac)
- 新版 `009a691c`（命令位置の公開資料なし）

~~~diff
- 009a68c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 009a68c8 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 009a68c8 bytes 8a0800b5
+ 009a691c ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 009a691c ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
+ 009a691c bytes 8a0800b5
- 009a68ac ["COPY", "register:40e8:8", ["register:8:8"]]
- 009a68ac bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52aff59490b0e5d84f3da503eca763d4"></a>

### [`009a6ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6ca4.md) → [`009a6cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6cf8.md) FUN_009a6cf8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a6cc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009a6d1c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009a6cd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a6cc8",
      "DATA",
      [
        "storage",
        "00c88720",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009a6cd4",
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
      "009a6d1c",
      "DATA",
      [
        "storage",
        "00c887f0",
        null,
        "undefined *"
      ]
    ],
    [
      "009a6d28",
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

- 旧版 [`009a6cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6ca4.md#insn-009a6cc8) · [`009a6cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6ca4.md#insn-009a6cd8)
- 新版 `009a6d1c`（命令位置の公開資料なし）

~~~diff
- 009a6cc8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009a6cc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009a6cc8 bytes 080000f9
- 009a6cd8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009a6cd8 ["RETURN", null, ["register:0:8"]]
- 009a6cd8 bytes c0035fd6
+ 009a6d1c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 009a6d1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009a6d1c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

