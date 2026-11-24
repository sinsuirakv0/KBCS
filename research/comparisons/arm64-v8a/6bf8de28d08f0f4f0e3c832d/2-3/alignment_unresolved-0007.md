# v16.0.2 → v16.0.3 · 命令位置の検査未完了 (7)

[一覧の目次](README.md)

<a id="compare-662b144655135fc5b698999fae2285c2"></a>

### [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) → [`00803b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803b14.md) FUN_00803b14

採用 · 移動量 `+0xf64` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 87件 [`005b070c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b070c.md) [`005e2e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e2/005e2e80.md) [`005e6e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e6/005e6e3c.md) [`005e7544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7544.md) [`005e7f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7f7c.md) · 呼出先 3件 [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00802be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802be4.md)
- 新版 呼出元 87件 [`005b0abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b0/005b0abc.md) [`005e3230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e3/005e3230.md) [`005e71ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e7/005e71ec.md) [`005e78f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e7/005e78f4.md) [`005e832c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e8/005e832c.md) · 呼出先 3件 [`008011a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00801/008011a8.md) [`00803674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803674.md) [`00803b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803b48.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00802bb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00802bb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00802bb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00802bb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00802bb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00802bcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802be4"
      ]
    ]
  ],
  "added": [
    [
      "00803b14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00803b18",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00803b30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00803b48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md#insn-00802bb0) · [`00802bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md#insn-00802bb4) · [`00802bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md#insn-00802bcc)

~~~diff
- 00802bb0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00802bb0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00802bb0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00802bb0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00802bb0 bytes fd7bbea9
- 00802bb4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00802bb4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00802bb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00802bb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00802bb4 bytes f44f01a9
- 00802bcc ["INT_ADD", "register:40f0:8", ["const:802bcc:8", "const:4:8"]]
- 00802bcc ["CALL", null, ["ram:802be4:8"]]
- 00802bcc bytes 06000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0b97c87d27d8cf8f188760157cf11d9"></a>

### [`00802dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802dd0.md) → [`00803d34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803d34.md) FUN_00803d34

採用 · 移動量 `+0xf64` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00802da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802da4.md) [`00a06780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06780.md) · 呼出先 8件 [`0067678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/0067678c.md) [`007bbda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbda0.md) [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00802be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802be4.md)
- 新版 呼出元 3件 [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`00803d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803d08.md) [`00a0772c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a07/00a0772c.md) · 呼出先 8件 [`00676b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676b3c.md) [`007bcd04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007bc/007bcd04.md) [`008011a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00801/008011a8.md) [`00803674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803674.md) [`00803b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803b48.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 52.94% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00802e80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00803de4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00802e4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00802e4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802be4"
      ]
    ],
    [
      "unmatched:00802e80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00803d74"
      ]
    ],
    [
      "unmatched:00802ec0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802be4"
      ]
    ]
  ],
  "added": [
    [
      "00803db0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00803b48"
      ]
    ],
    [
      "00803de4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00803d74"
      ]
    ],
    [
      "00803e24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00803b48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00802e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802dd0.md#insn-00802e4c) · [`00802e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802dd0.md#insn-00802e80)
- 新版 [`00803db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803d34.md#insn-00803db0)

~~~diff
- 00802e4c ["INT_ADD", "register:40f0:8", ["const:802e4c:8", "const:4:8"]]
- 00802e4c ["CALL", null, ["ram:802be4:8"]]
- 00802e4c bytes 66ffff97
- 00802e80 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00802e80 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00802e80 bytes 83fcff54
+ 00803db0 ["INT_ADD", "register:40f0:8", ["const:803db0:8", "const:4:8"]]
+ 00803db0 ["CALL", null, ["ram:803b48:8"]]
+ 00803db0 bytes 66ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-561587576b9ba4aa1d1ee0bbe55adede"></a>

### [`00802ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802ec4.md) → [`00803e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803e28.md) FUN_00803e28

採用 · 移動量 `+0xf64` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00a06780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06780.md) · 呼出先 4件 [`0067678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/0067678c.md) [`007bbda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbda0.md) [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 2件 [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`00a0772c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a07/00a0772c.md) · 呼出先 4件 [`00676b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676b3c.md) [`007bcd04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007bc/007bcd04.md) [`00803674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803674.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00802f34"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00803e98"
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
      "00803e8c",
      "DATA",
      [
        "storage",
        "0040f050",
        null,
        "byte[63]"
      ]
    ]
  ],
  "added": [
    [
      "00803e8c",
      "DATA",
      [
        "storage",
        "0040f050",
        null,
        "byte[39]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00802f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802ec4.md#insn-00802f34) · [`00802ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802ec4.md#insn-00802ed0)
- 新版 [`00803e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803e28.md#insn-00803e98) · [`00803e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803e28.md#insn-00803e34)

~~~diff
- 00802f34 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00802f34 ["RETURN", null, ["register:0:8"]]
- 00802f34 bytes c0035fd6
+ 00803e98 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00803e98 ["RETURN", null, ["register:0:8"]]
+ 00803e98 bytes c0035fd6
- 00802ed0 ["INT_ADD", "register:40f0:8", ["const:802ed0:8", "const:4:8"]]
- 00802ed0 ["CALL", null, ["callee:008524fc:8"]]
+ 00803e34 ["INT_ADD", "register:40f0:8", ["const:803e34:8", "const:4:8"]]
+ 00803e34 ["CALL", null, ["callee:008524fc:8"]]
- 00802ed0 bytes a0390194
+ 00803e34 bytes b2390194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6114078a0c4768127cbc6a1aa1c56f8"></a>

### [`00803208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00803/00803208.md) → [`0080416c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00804/0080416c.md) FUN_0080416c

採用 · 移動量 `+0xf64` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`006bedb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bedb4.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`007b0a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0a70.md) · 呼出先 3件 [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00802be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802be4.md) [`0080323c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00803/0080323c.md)
- 新版 呼出元 10件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`00605644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00605/00605644.md) [`006bf164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bf164.md) [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) [`007b19d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007b1/007b19d4.md) · 呼出先 3件 [`00803674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803674.md) [`00803b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803b48.md) [`008041a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00804/008041a0.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00803224"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00804188"
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
      "unmatched:00803224",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802be4"
      ]
    ],
    [
      "unmatched:00803238",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0080323c"
      ]
    ]
  ],
  "added": [
    [
      "00804188",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00803b48"
      ]
    ],
    [
      "0080419c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008041a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00803224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00803/00803208.md#insn-00803224) · [`00803218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00803/00803208.md#insn-00803218)
- 新版 [`00804188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00804/0080416c.md#insn-00804188) · [`0080417c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00804/0080416c.md#insn-0080417c)

~~~diff
- 00803224 ["INT_ADD", "register:40f0:8", ["const:803224:8", "const:4:8"]]
- 00803224 ["CALL", null, ["ram:802be4:8"]]
- 00803224 bytes 70feff97
+ 00804188 ["INT_ADD", "register:40f0:8", ["const:804188:8", "const:4:8"]]
+ 00804188 ["CALL", null, ["ram:803b48:8"]]
+ 00804188 bytes 70feff97
- 00803218 ["INT_ADD", "register:40f0:8", ["const:803218:8", "const:4:8"]]
- 00803218 ["CALL", null, ["callee:00803674:8"]]
+ 0080417c ["INT_ADD", "register:40f0:8", ["const:80417c:8", "const:4:8"]]
+ 0080417c ["CALL", null, ["callee:00803674:8"]]
- 00803218 bytes 3efdff97
+ 0080417c bytes 3efdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-663cb6a21bd6b523638a6157b843b3a5"></a>

### [`00803dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00803/00803dd4.md) → [`00804d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00804/00804d38.md) FUN_00804d38

採用 · 移動量 `+0xf64` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 12件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007cb638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cb/007cb638.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 3件 [`00744260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744260.md) [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 12件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`007bea00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007be/007bea00.md) [`007cc59c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cc/007cc59c.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`007e00a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007e0/007e00a4.md) · 呼出先 3件 [`00744610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744610.md) [`00803674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803674.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00803ddc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00804d40"
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
      "unmatched:00803ddc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "unmatched:00803de8",
      "DATA",
      [
        "storage",
        "0039bae0",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "00804d40",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "00804d4c",
      "DATA",
      [
        "storage",
        "0039bae0",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00803ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00803/00803dd4.md#insn-00803ddc) · [`00803dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00803/00803dd4.md#insn-00803dd8)
- 新版 [`00804d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00804/00804d38.md#insn-00804d40)

~~~diff
- 00803ddc ["INT_ADD", "register:40f0:8", ["const:803ddc:8", "const:4:8"]]
- 00803ddc ["CALL", null, ["callee:008524fc:8"]]
- 00803ddc bytes dd350194
+ 00804d40 ["INT_ADD", "register:40f0:8", ["const:804d40:8", "const:4:8"]]
+ 00804d40 ["CALL", null, ["callee:008524fc:8"]]
+ 00804d40 bytes ef350194
- 00803dd8 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00803dd8 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4eeb84d927df6b5f604c04d90ac88ebb"></a>

### [`00805c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00805/00805c4c.md) → [`00806bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00806/00806bb0.md) FUN_00806bb0

採用 · 移動量 `+0xf64` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0072c8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072c/0072c8a4.md) [`0072f230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072f/0072f230.md) [`00731864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731864.md) [`00a87b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a87/00a87b40.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 4件 [`0072cc54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0072c/0072cc54.md) [`0072f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0072f/0072f5e0.md) [`00731c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00731/00731c14.md) [`00a88b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a88/00a88b34.md) · 呼出先 1件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 74.36% / 新版 67.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00806bdc",
      "DATA",
      [
        "storage",
        "002eca23",
        "switchD_00805c84::switchdataD_002eca23",
        "byte"
      ]
    ],
    [
      "00806ca0",
      "DATA",
      [
        "storage",
        "0038b098",
        null,
        "byte[39]"
      ]
    ],
    [
      "00806ca0",
      "DATA",
      [
        "storage",
        "0038a8c8",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "00806bdc",
      "DATA",
      [
        "storage",
        "002eca63",
        "switchD_00806be8::switchdataD_002eca63",
        "byte"
      ]
    ],
    [
      "00806ca0",
      "DATA",
      [
        "storage",
        "0038b098",
        null,
        "qword"
      ]
    ],
    [
      "00806ca0",
      "DATA",
      [
        "storage",
        "0038a8c8",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00805c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00805/00805c4c.md#insn-00805c64) · [`00805c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00805/00805c4c.md#insn-00805c6c) · [`00805c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00805/00805c4c.md#insn-00805c74)
- 新版 [`00806bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00806/00806bb0.md#insn-00806bc8) · [`00806bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00806/00806bb0.md#insn-00806bd0)

~~~diff
- 00805c64 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00805c64 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00805c64 ["CBRANCH", null, ["local:b22:8", "tmp:1:1"]]
+ 00806bc8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00806bc8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00806bc8 ["CBRANCH", null, ["local:b26:8", "tmp:1:1"]]
- 00805c64 bytes c8080054
+ 00806bc8 bytes c8080054
- 00805c6c ["COPY", "tmp:0:8", ["const:a23:8"]]
- 00805c6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00805c6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00805c6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00806bd0 ["COPY", "tmp:0:8", ["const:a63:8"]]
+ 00806bd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00806bd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00806bd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00805c6c bytes 298d2891
+ 00806bd0 bytes 298d2991
- 00805c74 ["COPY", "register:4050:8", ["const:805c88:8"]]
- 00805c74 bytes aa000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffc94d70d7395fe3043915bd01edd28d"></a>

### [`0080bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080bd30.md) → [`0080cc94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080c/0080cc94.md) FUN_0080cc94

採用 · 移動量 `+0xf64` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 11件 [`0047b54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b54c.md) [`0080dc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080dc8c.md) [`0080deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080deac.md) [`0080e2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e2f0.md) [`0080e304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e304.md)
- 新版 呼出元 1件 [`00b1438c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b14/00b1438c.md) · 呼出先 11件 [`0047b86c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b86c.md) [`0080ebf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080e/0080ebf0.md) [`0080ee10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080e/0080ee10.md) [`0080f254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f254.md) [`0080f268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f268.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.42% / 新版 70.42%

CFGの説明率　旧版 70.55% / 新版 71.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 19件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0080c14c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0080c168"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0080c178"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0080d070",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0080c1b0"
      ]
    ],
    [
      "unmatched:0080c11c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0080c1c4"
      ]
    ],
    [
      "unmatched:0080c120",
      "READ",
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
      "0080d070",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0080d114"
      ]
    ],
    [
      "0080d080",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0080d128"
      ]
    ],
    [
      "0080d084",
      "READ",
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

- 旧版 [`0080c14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080bd30.md#insn-0080c14c) · [`0080c168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080bd30.md#insn-0080c168) · [`0080c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080bd30.md#insn-0080c178)

~~~diff
- 0080c14c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 0080c14c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0080c14c bytes e00700f9
- 0080c168 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 0080c168 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0080c168 bytes e80700f9
- 0080c178 ["COPY", "tmp:0:8", ["register:8:8"]]
- 0080c178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0080c178 bytes e80300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df31a138ab3e8c409a0771f7c37d51f7"></a>

### [`0080c4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c4b0.md) → [`0080d414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080d/0080d414.md) FUN_0080d414

採用 · 移動量 `+0xf64` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00850830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00850/00850830.md) · 呼出先 1件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 1件 [`008517dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00851/008517dc.md) · 呼出先 1件 [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 66.67% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0080c504"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0080d468"
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
      "unmatched:0080c504",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0080d514"
      ]
    ]
  ],
  "added": [
    [
      "0080d468",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0080d514"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080c504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c4b0.md#insn-0080c504) · [`0080c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c4b0.md#insn-0080c4b8)
- 新版 [`0080d468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080d/0080d414.md#insn-0080d468) · [`0080d41c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080d/0080d414.md#insn-0080d41c)

~~~diff
- 0080c504 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0080c504 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 0080c504 ["CBRANCH", null, ["local:b9:8", "tmp:1:1"]]
- 0080c504 bytes 69050054
+ 0080d468 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 0080d468 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 0080d468 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
+ 0080d468 bytes 69050054
- 0080c4b8 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
+ 0080d41c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 0080c4b8 bytes 60080054
+ 0080d41c bytes 60080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2343fbf3fb5c27d0ba5d64c768ba919f"></a>

### [`0080c5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c5c8.md) → [`0080d52c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080d/0080d52c.md) FUN_0080d52c

採用 · 移動量 `+0xf64` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 2件 [`00480b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480b78.md) [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md)
- 新版 呼出元 1件 [`00a2c310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · 呼出先 2件 [`00480e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480e98.md) [`00480ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480ef0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 70.59% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080c608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c5c8.md#insn-0080c608) · [`0080c614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c5c8.md#insn-0080c614) · [`0080c644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c5c8.md#insn-0080c644)
- 新版 [`0080d56c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080d/0080d52c.md#insn-0080d56c) · [`0080d578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080d/0080d52c.md#insn-0080d578) · [`0080d5a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080d/0080d52c.md#insn-0080d5a8)

~~~diff
- 0080c608 ["INT_ADD", "register:40f0:8", ["const:80c608:8", "const:4:8"]]
- 0080c608 ["CALL", null, ["callee:00480ef0:8"]]
+ 0080d56c ["INT_ADD", "register:40f0:8", ["const:80d56c:8", "const:4:8"]]
+ 0080d56c ["CALL", null, ["callee:00480ef0:8"]]
- 0080c608 bytes 72d1f197
+ 0080d56c bytes 61cef197
- 0080c614 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 0080d578 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 0080c614 bytes a00a0054
+ 0080d578 bytes a00a0054
- 0080c644 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0080c644 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 0080c644 ["CBRANCH", null, ["local:b11:8", "tmp:1:1"]]
+ 0080d5a8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 0080d5a8 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 0080d5a8 ["CBRANCH", null, ["local:b10:8", "tmp:1:1"]]
- 0080c644 bytes 29090054
+ 0080d5a8 bytes 29090054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc96dee108b4cda4c1292563c590c911"></a>

### [`0080de98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080de98.md) → [`0080edfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080e/0080edfc.md) FUN_0080edfc

採用 · 移動量 `+0xf64` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0080dc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080dc8c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0080ebf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080e/0080ebf0.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0080de98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0080de98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0080edfc"
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
      "unmatched:0080de98",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0080dea4",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0080dea8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ],
  "added": [
    [
      "0080edfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0080ee08",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ],
    [
      "0080ee0c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080de98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080de98.md#insn-0080de98) · [`0080dea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080de98.md#insn-0080dea8)
- 新版 [`0080edfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080e/0080edfc.md#insn-0080edfc)

~~~diff
- 0080de98 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0080de98 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0080de98 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0080de98 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0080de98 bytes fd7bbfa9
- 0080dea8 ["INT_ADD", "register:40f0:8", ["const:80dea8:8", "const:4:8"]]
- 0080dea8 ["CALL", null, ["callee:0043bad8:8"]]
- 0080dea8 bytes 44b6f097
+ 0080edfc ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0080edfc ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0080edfc ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 0080edfc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0080edfc bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-deb027ce79e5947a04711b62e3283332"></a>

### [`0080e220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e220.md) → [`0080f184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f184.md) FUN_0080f184

採用 · 移動量 `+0xf64` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 68.42% / 新版 59.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0080e280"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0080f1e4"
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
      "unmatched:0080e280",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0080f1b4"
      ]
    ]
  ],
  "added": [
    [
      "0080f1e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0080f1b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080e280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e220.md#insn-0080e280) · [`0080e240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e220.md#insn-0080e240)
- 新版 [`0080f1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f184.md#insn-0080f1e4) · [`0080f1a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f184.md#insn-0080f1a4)

~~~diff
- 0080e280 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0080e280 bytes 80feff54
+ 0080f1e4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 0080f1e4 bytes 80feff54
- 0080e240 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 0080f1a4 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 0080e240 bytes 60030054
+ 0080f1a4 bytes 60030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94c9a48e5a09c98c427203ace885c53c"></a>

### [`0080e2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e2dc.md) → [`0080f240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f240.md) FUN_0080f240

採用 · 移動量 `+0xf64` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0080deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080deac.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0080ee10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080e/0080ee10.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0080e2dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0080e2dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0080f240"
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
      "unmatched:0080e2dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0080e2e8",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0080e2ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ],
  "added": [
    [
      "0080f240",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0080f24c",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ],
    [
      "0080f250",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080e2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e2dc.md#insn-0080e2dc) · [`0080e2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e2dc.md#insn-0080e2ec)
- 新版 [`0080f240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f240.md#insn-0080f240)

~~~diff
- 0080e2dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0080e2dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0080e2dc ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0080e2dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0080e2dc bytes fd7bbfa9
- 0080e2ec ["INT_ADD", "register:40f0:8", ["const:80e2ec:8", "const:4:8"]]
- 0080e2ec ["CALL", null, ["callee:0043bad8:8"]]
- 0080e2ec bytes 33b5f097
+ 0080f240 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0080f240 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0080f240 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 0080f240 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0080f240 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b5fe73557d0fb6c6e29a0fb52b46c28"></a>

### [`0080e430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e430.md) → [`0080f394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f394.md) FUN_0080f394

採用 · 移動量 `+0xf64` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0080e304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e304.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0080f268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f268.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0080e430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0080e430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0080f394"
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
      "unmatched:0080e430",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0080e43c",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0080e440",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ],
  "added": [
    [
      "0080f394",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0080f3a0",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ],
    [
      "0080f3a4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080e430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e430.md#insn-0080e430) · [`0080e440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e430.md#insn-0080e440)
- 新版 [`0080f394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f394.md#insn-0080f394)

~~~diff
- 0080e430 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0080e430 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0080e430 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0080e430 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0080e430 bytes fd7bbfa9
- 0080e440 ["INT_ADD", "register:40f0:8", ["const:80e440:8", "const:4:8"]]
- 0080e440 ["CALL", null, ["callee:0043bad8:8"]]
- 0080e440 bytes deb4f097
+ 0080f394 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0080f394 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0080f394 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 0080f394 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0080f394 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-febe037e450f4e2500fb94dbc76db819"></a>

### [`0080e444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e444.md) → [`0080f3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f3a8.md) FUN_0080f3a8

採用 · 移動量 `+0xf64` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0080bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080bd30.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0080e650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e650.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 1件 [`0080cc94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080c/0080cc94.md) · 呼出先 5件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0080f5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f5b4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.89% / 新版 93.89%

CFGの説明率　旧版 82.76% / 新版 77.42%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0080e480"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0080e4cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0080e4d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0080e480",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0080f464"
      ]
    ]
  ],
  "added": [
    [
      "0080f3e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0080f464"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080e480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e444.md#insn-0080e480) · [`0080e4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e444.md#insn-0080e4cc) · [`0080e4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e444.md#insn-0080e4d4)

~~~diff
- 0080e480 ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
- 0080e480 bytes 02040054
- 0080e4cc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0080e4cc ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0080e4cc ["COPY", "tmp:2:8", ["register:4058:8"]]
- 0080e4cc ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 0080e4cc bytes 6a818a9a
- 0080e4d4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0080e4d4 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 0080e4d4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0080e4d4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0080e4d4 bytes 5731899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43aff1c6025d8ca673ddd6cad9924105"></a>

### [`0080e8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e8f8.md) → [`0080f85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f85c.md) FUN_0080f85c

採用 · 移動量 `+0xf64` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0080d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080d560.md) [`0080e8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e8f8.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849cf0.md) · 呼出先 2件 [`0080e8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e8f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 4件 [`0080e4c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080e/0080e4c4.md) [`0080f85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f85c.md) [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`0084ac9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084ac9c.md) · 呼出先 2件 [`0080f85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f85c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0080e8fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0080e8fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0080e900"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0080e8fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0080e900",
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
      "0080f860",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0080f864",
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

- 旧版 [`0080e8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e8f8.md#insn-0080e8fc) · [`0080e900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e8f8.md#insn-0080e900)
- 新版 [`0080f860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080f/0080f85c.md#insn-0080f860)

~~~diff
- 0080e8fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0080e8fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0080e8fc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0080e8fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0080e8fc bytes fd7bbea9
- 0080e900 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0080e900 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0080e900 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0080e900 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0080e900 bytes f44f01a9
+ 0080f860 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0080f860 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0080f860 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0080f860 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0080f860 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae4ec49f85fc3ad8ca5aa9a93294681a"></a>

### [`0080fb6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fb6c.md) → [`00810ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00810/00810ad0.md) FUN_00810ad0

採用 · 移動量 `+0xf64` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 2件 [`008108a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/008108a4.md) [`008108b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/008108b8.md)
- 新版 呼出元 3件 [`007bea00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007be/007bea00.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`007e00a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007e0/007e00a4.md) · 呼出先 2件 [`00811808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00811/00811808.md) [`0081181c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00811/0081181c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0080fbb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00810b14"
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
      "unmatched:0080fbb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00810b28"
      ]
    ]
  ],
  "added": [
    [
      "00810b14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00810b28"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080fbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fb6c.md#insn-0080fbb0) · [`0080fb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fb6c.md#insn-0080fb94)
- 新版 [`00810b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00810/00810ad0.md#insn-00810b14) · [`00810af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00810/00810ad0.md#insn-00810af8)

~~~diff
- 0080fbb0 ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
- 0080fbb0 bytes a2000054
+ 00810b14 ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
+ 00810b14 bytes a2000054
- 0080fb94 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0080fb94 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 0080fb94 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 00810af8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00810af8 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00810af8 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 0080fb94 bytes 69010054
+ 00810af8 bytes 69010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7bc971c2f99872e281116cde43b1b6b"></a>

### [`0080fc24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fc24.md) → [`00810b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00810/00810b88.md) FUN_00810b88

採用 · 移動量 `+0xf64` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`009d9598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d9/009d9598.md) · 呼出先 1件 [`00810a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810a10.md)
- 新版 呼出元 2件 [`007bea00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007be/007bea00.md) [`009da544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009da/009da544.md) · 呼出先 1件 [`00811974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00811/00811974.md)

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-828265a526aa360cc5d5a3716ccba962"></a>

### [`00810a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810a10.md) → [`00811974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00811/00811974.md) FUN_00811974

採用 · 移動量 `+0xf64` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0080fc24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fc24.md) · 呼出先 5件 [`007f1f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1f10.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00810b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00810/00810b88.md) · 呼出先 5件 [`007f2e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f2/007f2e74.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 79.17% / 新版 67.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00810a3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00810a7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00810a88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00810a3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00811a30"
      ]
    ],
    [
      "unmatched:00810a90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00811a9c"
      ]
    ]
  ],
  "added": [
    [
      "008119a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00811a30"
      ]
    ],
    [
      "008119f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00811a9c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00810a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810a10.md#insn-00810a3c) · [`00810a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810a10.md#insn-00810a7c) · [`00810a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810a10.md#insn-00810a88)

~~~diff
- 00810a3c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00810a3c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00810a3c ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00810a3c bytes 89040054
- 00810a7c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00810a7c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00810a7c ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00810a7c ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00810a7c bytes 2981839a
- 00810a88 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00810a88 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00810a88 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00810a88 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00810a88 bytes 2831889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f4accba28ea412df9bfdc46f15ca2d1"></a>

### [`00814030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00814/00814030.md) → [`00814f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00814/00814f94.md) FUN_00814f94

採用 · 移動量 `+0xf64` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00813a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00813/00813a00.md) [`008b6f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f1c.md) · 呼出先 5件 [`0046c4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c4a0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 2件 [`00814964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00814/00814964.md) [`008b7ec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ec8.md) · 呼出先 5件 [`0046c7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046c7c0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 58.33% / 新版 48.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00814030"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00814030"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00814034"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00814030",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00814034",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00814038",
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
      "00814f94",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00814f98",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00814f9c",
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

- 旧版 [`00814030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00814/00814030.md#insn-00814030) · [`00814034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00814/00814030.md#insn-00814034) · [`00814038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00814/00814030.md#insn-00814038)

~~~diff
- 00814030 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00814030 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00814030 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00814030 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00814030 bytes fd7bbca9
- 00814034 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00814034 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00814034 bytes f70b00f9
- 00814038 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00814038 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00814038 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00814038 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00814038 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff282991865c1cb200bc7796ee62a760"></a>

### [`00819a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819a04.md) → [`0081a9b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081a/0081a9b0.md) FUN_0081a9b0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 1件 [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)
- 新版 呼出元 1件 [`0081b818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081b/0081b818.md) · 呼出先 1件 [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.08% / 新版 98.08%

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
      "site": "00819ad0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "0081aa7c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00819ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819a04.md#insn-00819ad0) · [`00819a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819a04.md#insn-00819a20)
- 新版 [`0081aa7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081a/0081a9b0.md#insn-0081aa7c) · [`0081a9cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081a/0081a9b0.md#insn-0081a9cc)

~~~diff
- 00819ad0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00819ad0 ["RETURN", null, ["register:0:8"]]
- 00819ad0 bytes c0035fd6
+ 0081aa7c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 0081aa7c ["RETURN", null, ["register:0:8"]]
+ 0081aa7c bytes c0035fd6
- 00819a20 ["INT_ADD", "register:40f0:8", ["const:819a20:8", "const:4:8"]]
- 00819a20 ["CALL", null, ["callee:00487c9c:8"]]
+ 0081a9cc ["INT_ADD", "register:40f0:8", ["const:81a9cc:8", "const:4:8"]]
+ 0081a9cc ["CALL", null, ["callee:00487c9c:8"]]
- 00819a20 bytes d7b7f197
+ 0081a9cc bytes b4b4f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58c6c994e43c79b2f6d7f478253b5c7b"></a>

### [`00819ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819ad4.md) → [`0081aa80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081a/0081aa80.md) FUN_0081aa80

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`0081b818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081b/0081b818.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487dc4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 93.55% / 新版 96.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00819b2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00819b2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00819b30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00819b2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0081aad8",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00819b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819ad4.md#insn-00819b2c) · [`00819b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819ad4.md#insn-00819b30)
- 新版 [`0081aad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081a/0081aa80.md#insn-0081aad8)

~~~diff
- 00819b2c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00819b2c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00819b2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:8:8"]]
- 00819b2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00819b2c bytes e9a300a9
- 00819b30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:40:8"]]
- 00819b30 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00819b30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00819b30 bytes 9f2200f9
+ 0081aad8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0081aad8 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0081aad8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:8:8"]]
+ 0081aad8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0081aad8 bytes e9a300a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c7504fa6a244881b447e0ffb8c5c4a5"></a>

### [`0082eb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082eb50.md) → [`0082fafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082f/0082fafc.md) FUN_0082fafc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 21件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`0062714c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00627/0062714c.md) [`0067e838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e838.md) [`006adf88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ad/006adf88.md) [`006ee798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006ee798.md) · 呼出先 2件 [`008238b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/008238b8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 21件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`006274fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00627/006274fc.md) [`0067ebe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0067e/0067ebe8.md) [`006ae338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ae/006ae338.md) [`006eeb48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ee/006eeb48.md) · 呼出先 2件 [`00824864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00824/00824864.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 46.15% / 新版 46.15%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0082eb50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0082eb50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0082eb54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0082eb50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0082eb54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0082eb78",
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
      "0082fafc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0082fb00",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0082fb24",
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

- 旧版 [`0082eb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082eb50.md#insn-0082eb50) · [`0082eb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082eb50.md#insn-0082eb54)
- 新版 [`0082fafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082f/0082fafc.md#insn-0082fafc)

~~~diff
- 0082eb50 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0082eb50 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0082eb50 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0082eb50 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0082eb50 bytes fd7bbea9
- 0082eb54 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0082eb54 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0082eb54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0082eb54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0082eb54 bytes f44f01a9
+ 0082fafc ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0082fafc ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0082fafc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0082fafc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0082fafc bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6daa11643b128535632659b97d5427c"></a>

### [`008301c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008301c8.md) → [`00831174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831174.md) FUN_00831174

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00820774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/00820774.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00821720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00821/00821720.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 73.33% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008301d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008301c8.md#insn-008301d8) · [`008301e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008301c8.md#insn-008301e0) · [`00830204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008301c8.md#insn-00830204)
- 新版 [`0083118c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831174.md#insn-0083118c) · [`008311b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831174.md#insn-008311b0)

~~~diff
- 008301d8 ["COPY", "register:40e8:8", ["register:8:8"]]
- 008301d8 bytes fd030091
- 008301e0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 008301e0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 008301e0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 008301e0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 0083118c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 0083118c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 0083118c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 0083118c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 008301e0 bytes c8000036
+ 0083118c bytes c8000036
- 00830204 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00830204 ["CBRANCH", null, ["local:b1:8", "tmp:0:1"]]
+ 008311b0 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
+ 008311b0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00830204 bytes 16ffffb4
+ 008311b0 bytes 16ffffb4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7083cf86a2f15cdff157ab4012c11027"></a>

### [`008302cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302cc.md) → [`00831278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831278.md) FUN_00831278

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00819e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819e1c.md) [`0081c760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c760.md) [`008290d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008290d4.md) [`008295cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008295cc.md) [`008300b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008300b8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 5件 [`0081adc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081a/0081adc8.md) [`0081d70c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081d/0081d70c.md) [`0082a080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082a/0082a080.md) [`0082a578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082a/0082a578.md) [`00831064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831064.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008302cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008302cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00831278"
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
      "unmatched:008302cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008302d8",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008302dc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ],
  "added": [
    [
      "00831278",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00831284",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ],
    [
      "00831288",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008302cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302cc.md#insn-008302cc) · [`008302dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302cc.md#insn-008302dc)
- 新版 [`00831278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831278.md#insn-00831278)

~~~diff
- 008302cc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008302cc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008302cc ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 008302cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008302cc bytes fd7bbfa9
- 008302dc ["INT_ADD", "register:40f0:8", ["const:8302dc:8", "const:4:8"]]
- 008302dc ["CALL", null, ["callee:0043bad8:8"]]
- 008302dc bytes 372df097
+ 00831278 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00831278 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00831278 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00831278 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00831278 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afb8afc71dc0bfece8ed802a4b61da5f"></a>

### [`00830350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830350.md) → [`008312fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008312fc.md) FUN_008312fc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00830358"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00831304"
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
      "unmatched:00830358",
      "DATA",
      [
        "storage",
        "00c7e500",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0083035c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f40"
      ]
    ]
  ],
  "added": [
    [
      "00831304",
      "DATA",
      [
        "storage",
        "00c7f4d0",
        null,
        "pointer"
      ]
    ],
    [
      "00831308",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830350.md#insn-00830358) · [`00830350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830350.md#insn-00830350)
- 新版 [`00831304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008312fc.md#insn-00831304)

~~~diff
- 00830358 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00830358 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00830358 bytes 080000f9
+ 00831304 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00831304 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00831304 bytes 080000f9
- 00830350 ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 00830350 bytes 682200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-093c8f5818bf3dea8a24d678119d58d3"></a>

### [`00830360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830360.md) → [`0083130c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083130c.md) FUN_0083130c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00830378"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00831324"
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
      "unmatched:00830378",
      "DATA",
      [
        "storage",
        "00c7e500",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00831324",
      "DATA",
      [
        "storage",
        "00c7f4d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830360.md#insn-00830378) · [`0083036c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830360.md#insn-0083036c)
- 新版 [`00831324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083130c.md#insn-00831324) · [`00831318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083130c.md#insn-00831318)

~~~diff
- 00830378 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00830378 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00830378 bytes 080000f9
+ 00831324 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00831324 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00831324 bytes 080000f9
- 0083036c ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00831318 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0083036c bytes 682200d0
+ 00831318 bytes 682200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36077e54fb6cb849a6f676622217000f"></a>

### [`00830390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830390.md) → [`0083133c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083133c.md) FUN_0083133c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0081b818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081b/0081b818.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 38.46% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00830390"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00830390"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00830394"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00830390",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00830394",
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
      "0083133c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00831340",
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

- 旧版 [`00830390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830390.md#insn-00830390) · [`00830394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830390.md#insn-00830394)
- 新版 [`0083133c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083133c.md#insn-0083133c)

~~~diff
- 00830390 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00830390 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00830390 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00830390 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00830390 bytes fd7bbea9
- 00830394 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00830394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00830394 bytes f30b00f9
+ 0083133c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0083133c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0083133c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0083133c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0083133c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d47a6f342c6fdbc8d4da3e41532c4ac"></a>

### [`008303e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008303e8.md) → [`00831394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831394.md) FUN_00831394

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) [`008303e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008303e8.md) [`008478b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008478b8.md) · 呼出先 4件 [`008303e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008303e8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0081b818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081b/0081b818.md) [`00831394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831394.md) [`00848864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848864.md) · 呼出先 4件 [`00831394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831394.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00830438"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "008313e4"
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
      "unmatched:00830438",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "008313e4",
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

- 旧版 [`00830438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008303e8.md#insn-00830438) · [`008303e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008303e8.md#insn-008303e8)
- 新版 [`008313e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831394.md#insn-008313e4) · [`00831394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831394.md#insn-00831394)

~~~diff
- 00830438 ["COPY", "register:0:8", ["register:4040:8"]]
- 00830438 ["INT_ADD", "register:40f0:8", ["const:830438:8", "const:4:8"]]
- 00830438 ["CALLIND", null, ["register:0:8"]]
- 00830438 bytes 00013fd6
+ 008313e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008313e4 ["INT_ADD", "register:40f0:8", ["const:8313e4:8", "const:4:8"]]
+ 008313e4 ["CALLIND", null, ["register:0:8"]]
+ 008313e4 bytes 00013fd6
- 008303e8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 008303e8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00831394 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00831394 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 008303e8 bytes 610300b4
+ 00831394 bytes 610300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b4c32bb2b3cdeb111e941cfdbf773ae"></a>

### [`00830468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830468.md) → [`00831414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831414.md) FUN_00831414

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00830480"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0083142c"
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
      "unmatched:00830480",
      "DATA",
      [
        "storage",
        "00c7e550",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0083142c",
      "DATA",
      [
        "storage",
        "00c7f520",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830468.md#insn-00830480) · [`00830474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830468.md#insn-00830474)
- 新版 [`0083142c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831414.md#insn-0083142c) · [`00831420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831414.md#insn-00831420)

~~~diff
- 00830480 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00830480 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00830480 bytes 080000f9
+ 0083142c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0083142c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0083142c bytes 080000f9
- 00830474 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00831420 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00830474 bytes 682200d0
+ 00831420 bytes 682200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2160283e6019b38483694af131e032b"></a>

### [`008306f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008306f4.md) → [`008316a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008316a0.md) FUN_008316a0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008300a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008300a4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0081b818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081b/0081b818.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00831050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831050.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 70.97% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00830740"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0083074c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00830750"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00830750",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00831718"
      ]
    ],
    [
      "unmatched:008307e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083177c"
      ]
    ]
  ],
  "added": [
    [
      "008316fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00831718"
      ]
    ],
    [
      "0083178c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083177c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008306f4.md#insn-00830740) · [`0083074c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008306f4.md#insn-0083074c) · [`00830750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008306f4.md#insn-00830750)

~~~diff
- 00830740 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00830740 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00830740 ["COPY", "tmp:2:8", ["register:4050:8"]]
- 00830740 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00830740 bytes 4881889a
- 0083074c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0083074c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0083074c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0083074c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0083074c bytes 1831899a
- 00830750 ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
- 00830750 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00830750 bytes f80000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa36c6a5592de0d3d2687eeba0257d08"></a>

### [`00830b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b20.md) → [`00831acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831acc.md) FUN_00831acc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00830b48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00830b4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00830b50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00830b48",
      "DATA",
      [
        "storage",
        "00c7e608",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00830b54",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00830b58",
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
      "00831af4",
      "DATA",
      [
        "storage",
        "00c7f5d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00831b00",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00831b04",
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

- 旧版 [`00830b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b20.md#insn-00830b48) · [`00830b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b20.md#insn-00830b4c) · [`00830b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b20.md#insn-00830b50)

~~~diff
- 00830b48 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00830b48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00830b48 bytes 080000f9
- 00830b4c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00830b4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00830b4c bytes 0080803c
- 00830b50 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:18:8"]]
- 00830b50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00830b50 bytes 090c00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a0dc8fb082f938bdf9eafc0526a6b72"></a>

### [`00830b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b88.md) → [`00831b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831b34.md) FUN_00831b34

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00ab0e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab0/00ab0e4c.md) [`00ac86ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac86ac.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00ab1e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ab1/00ab1e40.md) [`00ac96a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac96a0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00830b88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00830b88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00830b8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00830b88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00830b8c",
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
      "00831b34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00831b38",
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

- 旧版 [`00830b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b88.md#insn-00830b88) · [`00830b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b88.md#insn-00830b8c)
- 新版 [`00831b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831b34.md#insn-00831b34)

~~~diff
- 00830b88 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00830b88 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00830b88 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00830b88 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00830b88 bytes fd7bbea9
- 00830b8c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00830b8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00830b8c bytes f30b00f9
+ 00831b34 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00831b34 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00831b34 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00831b34 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00831b34 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-197597d0fc5dd801a2f69262fa0c137e"></a>

### [`00831238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831238.md) → [`008321e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008321e4.md) FUN_008321e4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

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
      "site": "0083125c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083125c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00832208"
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
      "unmatched:0083125c",
      "DATA",
      [
        "storage",
        "00c7e808",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00831260",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00831264",
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
      "00832208",
      "DATA",
      [
        "storage",
        "00c7f7d8",
        null,
        "undefined *"
      ]
    ],
    [
      "0083220c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00832210",
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

- 旧版 [`0083125c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831238.md#insn-0083125c) · [`00831268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831238.md#insn-00831268)
- 新版 [`00832208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008321e4.md#insn-00832208)

~~~diff
- 0083125c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0083125c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0083125c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0083125c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083125c bytes 082400a9
- 00831268 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00831268 ["RETURN", null, ["register:0:8"]]
- 00831268 bytes c0035fd6
+ 00832208 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00832208 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00832208 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00832208 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00832208 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e68dc8e5cf6f44ca1e1c82d270aa23a"></a>

### [`00831288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831288.md) → [`00832234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832234.md) FUN_00832234

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 60.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008312ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00832258"
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
      "unmatched:008312ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00832258",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008312ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831288.md#insn-008312ac) · [`00831290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831288.md#insn-00831290)
- 新版 [`00832258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832234.md#insn-00832258) · [`0083223c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832234.md#insn-0083223c)

~~~diff
- 008312ac ["INT_ADD", "register:40f0:8", ["const:8312ac:8", "const:4:8"]]
- 008312ac ["CALL", null, ["ram:47ad34:8"]]
- 008312ac bytes a226f197
+ 00832258 ["INT_ADD", "register:40f0:8", ["const:832258:8", "const:4:8"]]
+ 00832258 ["CALL", null, ["ram:47b054:8"]]
+ 00832258 bytes 7f23f197
- 00831290 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00831290 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0083223c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0083223c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00831290 bytes e1010054
+ 0083223c bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b10590ef9755f3d279a32eb8afb9aba5"></a>

### [`008312fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008312fc.md) → [`008322a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008322a8.md) FUN_008322a8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

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
      "site": "00831320"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00831320"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008322cc"
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
      "unmatched:00831320",
      "DATA",
      [
        "storage",
        "00c7e888",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00831324",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00831328",
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
      "008322cc",
      "DATA",
      [
        "storage",
        "00c7f858",
        null,
        "undefined *"
      ]
    ],
    [
      "008322d0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008322d4",
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

- 旧版 [`00831320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008312fc.md#insn-00831320) · [`0083132c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008312fc.md#insn-0083132c)
- 新版 [`008322cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008322a8.md#insn-008322cc)

~~~diff
- 00831320 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00831320 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00831320 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00831320 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00831320 bytes 082400a9
- 0083132c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0083132c ["RETURN", null, ["register:0:8"]]
- 0083132c bytes c0035fd6
+ 008322cc ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008322cc ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008322cc ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008322cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008322cc bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b935b9fc59105501c4a41013a79b2d4"></a>

### [`00831330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831330.md) → [`008322dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008322dc.md) FUN_008322dc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083133c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083133c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008322e8"
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
      "unmatched:0083133c",
      "DATA",
      [
        "storage",
        "00c7e888",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008322e8",
      "DATA",
      [
        "storage",
        "00c7f858",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083133c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831330.md#insn-0083133c) · [`00831340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831330.md#insn-00831340)
- 新版 [`008322e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008322dc.md#insn-008322e8)

~~~diff
- 0083133c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0083133c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0083133c ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0083133c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083133c bytes 292000a9
- 00831340 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00831340 ["RETURN", null, ["register:0:8"]]
- 00831340 bytes c0035fd6
+ 008322e8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 008322e8 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 008322e8 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 008322e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008322e8 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3705e3db82867d5831faba2cfd114268"></a>

### [`00831d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d40.md) → [`00832cec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832cec.md) FUN_00832cec

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00831d64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00831d68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00832d10"
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
      "unmatched:00831d64",
      "DATA",
      [
        "storage",
        "00c7ea08",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00831d6c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00831d70",
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
      "00832d10",
      "DATA",
      [
        "storage",
        "00c7f9d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00832d18",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00832d1c",
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

- 旧版 [`00831d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d40.md#insn-00831d64) · [`00831d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d40.md#insn-00831d68) · [`00831d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d40.md#insn-00831d74)

~~~diff
- 00831d64 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00831d64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00831d64 bytes 080000f9
- 00831d68 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00831d68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00831d68 bytes 0080803c
- 00831d74 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00831d74 ["RETURN", null, ["register:0:8"]]
- 00831d74 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50bd5e6b54c22c7d110e535a29f2a090"></a>

### [`00831eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831eec.md) → [`00832e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832e98.md) FUN_00832e98

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00831f10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00831f10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00832ebc"
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
      "unmatched:00831f10",
      "DATA",
      [
        "storage",
        "00c7ea88",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00831f14",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00831f18",
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
      "00832ebc",
      "DATA",
      [
        "storage",
        "00c7fa58",
        null,
        "undefined *"
      ]
    ],
    [
      "00832ec0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00832ec4",
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

- 旧版 [`00831f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831eec.md#insn-00831f10) · [`00831f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831eec.md#insn-00831f1c)
- 新版 [`00832ebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832e98.md#insn-00832ebc)

~~~diff
- 00831f10 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00831f10 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00831f10 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00831f10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00831f10 bytes 082400a9
- 00831f1c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00831f1c ["RETURN", null, ["register:0:8"]]
- 00831f1c bytes c0035fd6
+ 00832ebc ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00832ebc ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00832ebc ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00832ebc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00832ebc bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6d91bc194d77a3b3a3020a6c6efd650"></a>

### [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) → [`00835138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/00835138.md) FUN_00835138

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`0083212c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083212c.md) [`008351c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008351c0.md) [`008352c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008352c4.md) [`00835558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835558.md) [`0083565c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083565c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 7件 [`008330d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/008330d8.md) [`0083616c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/0083616c.md) [`00836270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836270.md) [`00836504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836504.md) [`00836608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836608.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083418c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083418c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00835138"
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
      "unmatched:0083418c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00834198",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0083419c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ],
  "added": [
    [
      "00835138",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00835144",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ],
    [
      "00835148",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md#insn-0083418c) · [`0083419c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md#insn-0083419c)
- 新版 [`00835138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/00835138.md#insn-00835138)

~~~diff
- 0083418c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0083418c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0083418c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0083418c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0083418c bytes fd7bbfa9
- 0083419c ["INT_ADD", "register:40f0:8", ["const:83419c:8", "const:4:8"]]
- 0083419c ["CALL", null, ["callee:0043bad8:8"]]
- 0083419c bytes 871df097
+ 00835138 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00835138 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00835138 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00835138 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00835138 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed8610a0f09015000052ca3c72b62c7c"></a>

### [`00834668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834668.md) → [`00835614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/00835614.md) FUN_00835614

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008341a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/008341a0.md) · 呼出先 1件 [`008341a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/008341a0.md)
- 新版 呼出元 1件 [`0083514c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/0083514c.md) · 呼出先 1件 [`0083514c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/0083514c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.09% / 新版 91.09%

CFGの説明率　旧版 59.04% / 新版 54.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008346a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083496c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00834970"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00834688",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00835654"
      ]
    ],
    [
      "unmatched:00834744",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00835924"
      ]
    ],
    [
      "unmatched:008347e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00835750"
      ]
    ]
  ],
  "added": [
    [
      "00835634",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00835654"
      ]
    ],
    [
      "008356f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00835924"
      ]
    ],
    [
      "00835794",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00835750"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00834688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834668.md#insn-00834688) · [`008346a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834668.md#insn-008346a0) · [`00834744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834668.md#insn-00834744)

~~~diff
- 00834688 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00834688 bytes 00010054
- 008346a0 ["COPY", "tmp:0:8", ["register:4018:8"]]
- 008346a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008346a0 bytes 690000f9
- 00834744 ["CBRANCH", null, ["local:b52:8", "register:101:1"]]
- 00834744 bytes a0110054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-512606932f1ce9c0babc831616b3f6ea"></a>

### [`00834fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834fec.md) → [`00835f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/00835f98.md) FUN_00835f98

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00834990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834990.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0083593c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/0083593c.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 20.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00835050"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00835088"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00835090"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00835fec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0083508c"
      ]
    ],
    [
      "unmatched:00835088",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00835ff0"
      ]
    ],
    [
      "unmatched:00835090",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008360f4"
      ]
    ]
  ],
  "added": [
    [
      "00835fec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00836038"
      ]
    ],
    [
      "00836034",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00835ff0"
      ]
    ],
    [
      "0083603c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008360f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00835050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834fec.md#insn-00835050) · [`00835088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834fec.md#insn-00835088) · [`00835090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834fec.md#insn-00835090)

~~~diff
- 00835050 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00835050 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00835050 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00835050 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00835050 bytes 2101819a
- 00835088 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00835088 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00835088 bytes e1fdff54
- 00835090 ["CBRANCH", null, ["local:b25:8", "register:101:1"]]
- 00835090 bytes c0050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e34c64e060dbac147901e31e310ed2c"></a>

### [`008352c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008352c4.md) → [`00836270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836270.md) FUN_00836270

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00835138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/00835138.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 59.32% / 新版 59.32%

CFGの説明率　旧版 27.27% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008352f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008352f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00835350"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008352f4",
      "DATA",
      [
        "storage",
        "00c7ebf8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00835324",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00836334"
      ]
    ],
    [
      "unmatched:00835368",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c590a0"
      ]
    ]
  ],
  "added": [
    [
      "008362a0",
      "DATA",
      [
        "storage",
        "00c7fbc8",
        null,
        "undefined *"
      ]
    ],
    [
      "008362d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00836334"
      ]
    ],
    [
      "00836314",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c590a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008352f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008352c4.md#insn-008352f4) · [`00835324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008352c4.md#insn-00835324) · [`00835350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008352c4.md#insn-00835350)

~~~diff
- 008352f4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 008352f4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008352f4 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 008352f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008352f4 bytes 2a2000a9
- 00835324 ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
- 00835324 bytes 22030054
- 00835350 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00835350 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00835350 ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:10:8"]]
- 00835350 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00835350 bytes 600201a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a89c5404b13f757d16bf0df89ba1e1c"></a>

### [`00835558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835558.md) → [`00836504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836504.md) FUN_00836504

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00835138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/00835138.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.15% / 新版 86.15%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00835588"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00835588"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083558c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083558c",
      "DATA",
      [
        "storage",
        "00c7ec78",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008355a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008365c0"
      ]
    ]
  ],
  "added": [
    [
      "00836538",
      "DATA",
      [
        "storage",
        "00c7fc48",
        null,
        "undefined *"
      ]
    ],
    [
      "0083654c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008365c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00835588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835558.md#insn-00835588) · [`0083558c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835558.md#insn-0083558c) · [`00835598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835558.md#insn-00835598)

~~~diff
- 00835588 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00835588 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00835588 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00835588 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00835588 bytes 1ffc01a9
- 0083558c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0083558c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0083558c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0083558c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083558c bytes 082400a9
- 00835598 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00835598 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00835598 ["INT_ADD", "register:40a8:8", ["register:40a8:8", "const:10:8"]]
- 00835598 ["STORE", null, ["const:1b1:8", "register:40a8:8", "tmp:1:8"]]
- 00835598 bytes bf0e01f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edc164faa0750e229ddd17daf999d842"></a>

### [`00836038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836038.md) → [`00836fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836fe4.md) FUN_00836fe4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0082c8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c8bc.md) [`00836038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836038.md) [`00836838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836838.md) · 呼出先 7件 [`00836038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836038.md) [`0083669c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/0083669c.md) [`00836838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836838.md) [`00836dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836dc8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 3件 [`0082d868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082d/0082d868.md) [`00836fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836fe4.md) [`008377e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/008377e4.md) · 呼出先 7件 [`00836fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836fe4.md) [`00837648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/00837648.md) [`008377e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/008377e4.md) [`00837d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/00837d74.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 96.96% / 新版 96.96%

CFGの説明率　旧版 81.31% / 新版 79.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00836078"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00836354"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00836364"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00836078",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00837644"
      ]
    ],
    [
      "unmatched:00836354",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083732c"
      ]
    ],
    [
      "unmatched:00836360",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ]
  ],
  "added": [
    [
      "00837024",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00837644"
      ]
    ],
    [
      "00837300",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083732c"
      ]
    ],
    [
      "0083730c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00836078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836038.md#insn-00836078) · [`00836354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836038.md#insn-00836354) · [`00836360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836038.md#insn-00836360)

~~~diff
- 00836078 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00836078 ["CBRANCH", null, ["local:b66:8", "tmp:0:1"]]
- 00836078 bytes 01310054
- 00836354 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00836354 ["CBRANCH", null, ["local:b32:8", "tmp:0:1"]]
- 00836354 bytes 760100b4
- 00836360 ["INT_ADD", "register:40f0:8", ["const:836360:8", "const:4:8"]]
- 00836360 ["CALL", null, ["callee:00c54d90:8"]]
- 00836360 bytes 90761094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12f371c1a3c468b536cd5cbb114680ca"></a>

### [`00836838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836838.md) → [`008377e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/008377e4.md) FUN_008377e4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00836038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836038.md) · 呼出先 5件 [`00836038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836038.md) [`0083669c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/0083669c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00836fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836fe4.md) · 呼出先 5件 [`00836fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836fe4.md) [`00837648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/00837648.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 99.02% / 新版 99.02%

CFGの説明率　旧版 94.29% / 新版 95.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00836c74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00836c74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00836c78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00836c7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00837bf0"
      ]
    ]
  ],
  "added": [
    [
      "00837c28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00837bf0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00836c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836838.md#insn-00836c74) · [`00836c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836838.md#insn-00836c78) · [`00836c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836838.md#insn-00836c7c)

~~~diff
- 00836c74 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:20:8"]]
- 00836c74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 00836c74 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00836c74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00836c74 bytes 420101ad
- 00836c78 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:10:8"]]
- 00836c78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00836c78 bytes 4105803d
- 00836c7c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00836c7c ["CBRANCH", null, ["local:b38:8", "tmp:0:1"]]
- 00836c7c bytes 41feff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdd7bfea013b373d093ea34a990cb199"></a>

### [`00836d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836d3c.md) → [`00837ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/00837ce8.md) FUN_00837ce8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 46.15% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00836d80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00837d2c"
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
      "unmatched:00836d80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00837d64"
      ]
    ]
  ],
  "added": [
    [
      "00837d2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00837d64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00836d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836d3c.md#insn-00836d80) · [`00836d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836d3c.md#insn-00836d44)
- 新版 [`00837d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/00837ce8.md#insn-00837d2c) · [`00837cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/00837ce8.md#insn-00837cf0)

~~~diff
- 00836d80 ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
- 00836d80 bytes c2010054
+ 00837d2c ["CBRANCH", null, ["local:b8:8", "register:102:1"]]
+ 00837d2c bytes c2010054
- 00836d44 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00836d44 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00837cf0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00837cf0 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00836d44 bytes 080400b4
+ 00837cf0 bytes 080400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-359f9890bca2907cc29284b075de6b92"></a>

### [`008375e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/008375e0.md) → [`0083858c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00838/0083858c.md) FUN_0083858c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00836dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836dc8.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00837d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/00837d74.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.62% / 新版 89.62%

CFGの説明率　旧版 73.47% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00837618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008376e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008376e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00837618",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:008376b4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ],
    [
      "unmatched:008376b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00838680"
      ]
    ]
  ],
  "added": [
    [
      "008385c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00838660",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ],
    [
      "00838664",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00838680"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00837618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/008375e0.md#insn-00837618) · [`008376b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/008375e0.md#insn-008376b4) · [`008376b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/008375e0.md#insn-008376b8)

~~~diff
- 00837618 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00837618 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00837618 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00837618 bytes a8831ff8
- 008376b4 ["INT_ADD", "register:40f0:8", ["const:8376b4:8", "const:4:8"]]
- 008376b4 ["CALL", null, ["callee:00c54d90:8"]]
- 008376b4 bytes bb711094
- 008376b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008376b8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 008376b8 bytes e00000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9038ce3ecb047bb99fee525edbdf1d65"></a>

### [`008388e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/008388e0.md) → [`0083988c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/0083988c.md) FUN_0083988c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00682364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00682714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00682/00682714.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008388fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00838968"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008398a8"
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
      "unmatched:008388fc",
      "DATA",
      [
        "storage",
        "00c7ee08",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00838900",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008398d8"
      ]
    ],
    [
      "unmatched:0083890c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ]
  ],
  "added": [
    [
      "008398a8",
      "DATA",
      [
        "storage",
        "00c7fdd8",
        null,
        "pointer"
      ]
    ],
    [
      "008398ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008398d8"
      ]
    ],
    [
      "008398b8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008388fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/008388e0.md#insn-008388fc) · [`00838900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/008388e0.md#insn-00838900) · [`0083890c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/008388e0.md#insn-0083890c)

~~~diff
- 008388fc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008388fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008388fc bytes 080000f9
- 00838900 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00838900 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00838900 bytes 740100b4
- 0083890c ["INT_ADD", "register:40f0:8", ["const:83890c:8", "const:4:8"]]
- 0083890c ["CALL", null, ["callee:00c54d90:8"]]
- 0083890c bytes 256d1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a4f0ff0c570e951a15515f43393ab4f"></a>

### [`00838b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b18.md) → [`00839ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839ac4.md) FUN_00839ac4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

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
      "site": "00838b3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00838b3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00839ae8"
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
      "unmatched:00838b3c",
      "DATA",
      [
        "storage",
        "00c7eea8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00838b40",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00838b44",
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
      "00839ae8",
      "DATA",
      [
        "storage",
        "00c7fe78",
        null,
        "undefined *"
      ]
    ],
    [
      "00839aec",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00839af0",
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

- 旧版 [`00838b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b18.md#insn-00838b3c) · [`00838b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b18.md#insn-00838b48)
- 新版 [`00839ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839ac4.md#insn-00839ae8)

~~~diff
- 00838b3c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00838b3c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00838b3c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00838b3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00838b3c bytes 082400a9
- 00838b48 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00838b48 ["RETURN", null, ["register:0:8"]]
- 00838b48 bytes c0035fd6
+ 00839ae8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00839ae8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00839ae8 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00839ae8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00839ae8 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f7274c9bc3060ec8db8c303f57b44d7"></a>

### [`00838ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838ba8.md) → [`00839b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839b54.md) FUN_00839b54

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

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
      "site": "00838bcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00838bcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00839b78"
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
      "unmatched:00838bcc",
      "DATA",
      [
        "storage",
        "00c7ef28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00838bd0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00838bd4",
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
      "00839b78",
      "DATA",
      [
        "storage",
        "00c7fef8",
        null,
        "undefined *"
      ]
    ],
    [
      "00839b7c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00839b80",
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

- 旧版 [`00838bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838ba8.md#insn-00838bcc) · [`00838bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838ba8.md#insn-00838bd8)
- 新版 [`00839b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839b54.md#insn-00839b78)

~~~diff
- 00838bcc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00838bcc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00838bcc ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00838bcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00838bcc bytes 082400a9
- 00838bd8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00838bd8 ["RETURN", null, ["register:0:8"]]
- 00838bd8 bytes c0035fd6
+ 00839b78 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00839b78 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00839b78 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00839b78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00839b78 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85f49206a338fdf55edb8c04bc4963d6"></a>

### [`00839644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839644.md) → [`0083a5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083a5f0.md) FUN_0083a5f0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) [`00480558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480558.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00a07d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a07/00a07d9c.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00480658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480658.md) [`00480878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480878.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.41% / 新版 91.41%

CFGの説明率　旧版 63.64% / 新版 65.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008397b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008397c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008397d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008397b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008397c4"
      ]
    ],
    [
      "unmatched:008397b4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0083a794"
      ]
    ],
    [
      "unmatched:008397c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083a794"
      ]
    ]
  ],
  "added": [
    [
      "0083a75c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083a770"
      ]
    ],
    [
      "0083a760",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0083a794"
      ]
    ],
    [
      "0083a76c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083a794"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008397b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839644.md#insn-008397b0) · [`008397c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839644.md#insn-008397c0) · [`008397d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839644.md#insn-008397d0)

~~~diff
- 008397b0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008397b0 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 008397b0 bytes a80000b5
- 008397c0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008397c0 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 008397c0 bytes 480100b4
- 008397d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008397d0 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 008397d0 bytes 4bffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ee5d20b2e1d8c8f61e6773de596261b"></a>

### [`00839a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839a64.md) → [`0083aa10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083aa10.md) FUN_0083aa10

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0062c100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062c/0062c100.md) [`0075d7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d7b4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`0062c4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062c/0062c4b0.md) [`0075db64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075db64.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.96% / 新版 97.96%

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
      "site": "00839abc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0083aa68"
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
      "unmatched:00839abc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083aa50"
      ]
    ]
  ],
  "added": [
    [
      "0083aa68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083aa50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839abc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839a64.md#insn-00839abc) · [`00839a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839a64.md#insn-00839a94)
- 新版 [`0083aa68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083aa10.md#insn-0083aa68) · [`0083aa40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083aa10.md#insn-0083aa40)

~~~diff
- 00839abc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00839abc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00839abc bytes 48ffffb5
+ 0083aa68 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 0083aa68 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0083aa68 bytes 48ffffb5
- 00839a94 ["BRANCH", null, ["local:b7:8"]]
+ 0083aa40 ["BRANCH", null, ["local:b9:8"]]
- 00839a94 bytes 0c000014
+ 0083aa40 bytes 0c000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af3d5595fa19f8670ac5c46a15a3d10c"></a>

### [`00839d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839d50.md) → [`0083acfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083acfc.md) FUN_0083acfc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0075ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075ba1c.md) [`0075d7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d7b4.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 2件 [`0075bdcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075b/0075bdcc.md) [`0075db64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075db64.md) · 呼出先 1件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 25.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00839d58"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0083ad04"
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
      "unmatched:00839d58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083ad10"
      ]
    ]
  ],
  "added": [
    [
      "0083ad04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083ad10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839d50.md#insn-00839d58) · [`00839d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839d50.md#insn-00839d50)
- 新版 [`0083ad04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083acfc.md#insn-0083ad04)

~~~diff
- 00839d58 ["CBRANCH", null, ["local:b2:8", "register:102:1"]]
- 00839d58 bytes 62000054
+ 0083ad04 ["CBRANCH", null, ["local:b3:8", "register:102:1"]]
+ 0083ad04 bytes 62000054
- 00839d50 ["INT_SUB", "tmp:0:4", ["register:4000:4", "const:384:4"]]
- 00839d50 ["INT_ZEXT", "register:4040:8", ["tmp:0:4"]]
- 00839d50 bytes 08100e51
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b03f87f5485e91f9c276eafddb1653b8"></a>

### [`00847154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847154.md) → [`00848100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848100.md) FUN_00848100

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0067e628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e628.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0067e9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0067e/0067e9d8.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 50.00% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00847190"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0084813c"
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
      "unmatched:00847190",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0084813c",
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

- 旧版 [`00847190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847154.md#insn-00847190) · [`00847174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847154.md#insn-00847174)
- 新版 [`0084813c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848100.md#insn-0084813c) · [`00848120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848100.md#insn-00848120)

~~~diff
- 00847190 ["COPY", "register:0:8", ["register:4040:8"]]
- 00847190 ["INT_ADD", "register:40f0:8", ["const:847190:8", "const:4:8"]]
- 00847190 ["CALLIND", null, ["register:0:8"]]
- 00847190 bytes 00013fd6
+ 0084813c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0084813c ["INT_ADD", "register:40f0:8", ["const:84813c:8", "const:4:8"]]
+ 0084813c ["CALLIND", null, ["register:0:8"]]
+ 0084813c bytes 00013fd6
- 00847174 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00847174 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00848120 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00848120 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00847174 bytes 000100b4
+ 00848120 bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c67e8139cec8b80129a13af801e11c6"></a>

### [`008472b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008472b0.md) → [`0084825c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/0084825c.md) FUN_0084825c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008472b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008472b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008472b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008472b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008472b4",
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
      "0084825c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00848260",
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

- 旧版 [`008472b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008472b0.md#insn-008472b0) · [`008472b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008472b0.md#insn-008472b4)
- 新版 [`0084825c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/0084825c.md#insn-0084825c)

~~~diff
- 008472b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008472b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008472b0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008472b0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008472b0 bytes fd7bbea9
- 008472b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008472b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008472b4 bytes f30b00f9
+ 0084825c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0084825c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0084825c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0084825c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0084825c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15f4439f8f36e31ae255821e9b59d19b"></a>

### [`0084743c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/0084743c.md) → [`008483e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008483e8.md) FUN_008483e8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 4件 [`008691e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008691e0.md) [`00869280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869280.md) [`00869364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869364.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 4件 [`0086a18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a18c.md) [`0086a22c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a22c.md) [`0086a310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a310.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 85.71% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008474c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00848470"
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
      "unmatched:008474c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848460"
      ]
    ]
  ],
  "added": [
    [
      "00848470",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848460"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008474c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/0084743c.md#insn-008474c4) · [`0084745c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/0084743c.md#insn-0084745c)
- 新版 [`00848470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008483e8.md#insn-00848470) · [`00848408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008483e8.md#insn-00848408)

~~~diff
- 008474c4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008474c4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 008474c4 bytes 81ffff54
+ 00848470 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00848470 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00848470 bytes 81ffff54
- 0084745c ["INT_ADD", "register:40f0:8", ["const:84745c:8", "const:4:8"]]
- 0084745c ["CALL", null, ["callee:00c58f50:8"]]
+ 00848408 ["INT_ADD", "register:40f0:8", ["const:848408:8", "const:4:8"]]
+ 00848408 ["CALL", null, ["callee:00c58f50:8"]]
- 0084745c bytes c9421094
+ 00848408 bytes d2421094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a32a8b89e7d3623471cde70961a726f"></a>

### [`00847508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847508.md) → [`008484b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008484b4.md) FUN_008484b4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00869418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869418.md) [`00869478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869478.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0086a3c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a3c4.md) [`0086a424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a424.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00847508"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00847508"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084750c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00847508",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084750c",
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
      "008484b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008484b8",
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

- 旧版 [`00847508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847508.md#insn-00847508) · [`0084750c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847508.md#insn-0084750c)
- 新版 [`008484b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008484b4.md#insn-008484b4)

~~~diff
- 00847508 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00847508 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00847508 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00847508 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00847508 bytes fd7bbea9
- 0084750c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0084750c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0084750c bytes f30b00f9
+ 008484b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 008484b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 008484b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 008484b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 008484b4 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d522b2449d1a416a1c99d832b223ff8"></a>

### [`00847734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847734.md) → [`008486e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008486e0.md) FUN_008486e0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00846d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846d68.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`00847d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/00847d14.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.26% / 新版 75.26%

CFGの説明率　旧版 3.92% / 新版 3.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00847734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00847734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00847738"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00847734",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00847738",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00847750",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00847760"
      ]
    ]
  ],
  "added": [
    [
      "008486e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008486e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008486fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0084870c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00847734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847734.md#insn-00847734) · [`00847738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847734.md#insn-00847738) · [`00847750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847734.md#insn-00847750)

~~~diff
- 00847734 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00847734 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00847734 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00847734 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00847734 bytes fd7bbea9
- 00847738 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00847738 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00847738 bytes f30b00f9
- 00847750 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00847750 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78582128a1f6b23c26839ddd169e77a7"></a>

### [`00847a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847a90.md) → [`00848a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848a3c.md) FUN_00848a3c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 76.19% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00847b08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00848ab4"
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
      "unmatched:00847b08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848a74"
      ]
    ]
  ],
  "added": [
    [
      "00848ab4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848a74"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00847b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847a90.md#insn-00847b08) · [`00847aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847a90.md#insn-00847aa8)
- 新版 [`00848ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848a3c.md#insn-00848ab4) · [`00848a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848a3c.md#insn-00848a54)

~~~diff
- 00847b08 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00847b08 bytes 00feff54
+ 00848ab4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00848ab4 bytes 00feff54
- 00847aa8 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00847aa8 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00848a54 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00848a54 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00847aa8 bytes b40400b4
+ 00848a54 bytes b40400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9abac7b18ce5a3271dfa192515794b0"></a>

### [`00847c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847c7c.md) → [`00848c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848c28.md) FUN_00848c28

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0078f1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f1fc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0078f5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f5d8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00847c7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00847c7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00847c80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00847c7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00847c80",
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
      "00848c28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00848c2c",
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

- 旧版 [`00847c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847c7c.md#insn-00847c7c) · [`00847c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847c7c.md#insn-00847c80)
- 新版 [`00848c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848c28.md#insn-00848c28)

~~~diff
- 00847c7c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00847c7c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00847c7c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00847c7c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00847c7c bytes fd7bbea9
- 00847c80 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00847c80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00847c80 bytes f30b00f9
+ 00848c28 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00848c28 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00848c28 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00848c28 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00848c28 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f17cedf5697cc3e37aff285843832b23"></a>

### [`00847db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847db4.md) → [`00848d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848d60.md) FUN_00848d60

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 33.33% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00847df0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00848d9c"
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
      "unmatched:00847df0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848db4"
      ]
    ]
  ],
  "added": [
    [
      "00848d9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848db4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00847df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847db4.md#insn-00847df0) · [`00847dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847db4.md#insn-00847dc8)
- 新版 [`00848d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848d60.md#insn-00848d9c) · [`00848d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848d60.md#insn-00848d74)

~~~diff
- 00847df0 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00847df0 bytes c0000054
+ 00848d9c ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 00848d9c bytes c0000054
- 00847dc8 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00847dc8 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00848d74 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00848d74 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00847dc8 bytes d40200b4
+ 00848d74 bytes d40200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96439c76586e96164a770b6954115bfd"></a>

### [`00847e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847e30.md) → [`00848ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848ddc.md) FUN_00848ddc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 47.06% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00847e68"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00848e14"
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
      "unmatched:00847e68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848e54"
      ]
    ]
  ],
  "added": [
    [
      "00848e14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848e54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00847e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847e30.md#insn-00847e68) · [`00847e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847e30.md#insn-00847e4c)
- 新版 [`00848e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848ddc.md#insn-00848e14)

~~~diff
- 00847e68 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00847e68 bytes 00020054
+ 00848e14 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 00848e14 bytes 00020054
- 00847e4c ["COPY", "register:40a0:8", ["register:40a8:8"]]
- 00847e4c bytes f40315aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c27526f5d1154931753d6d6f4b81dbc"></a>

### [`008482a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008482a8.md) → [`00849254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/00849254.md) FUN_00849254

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00869b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869b94.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0086ab40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086ab40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 51.85% / 新版 60.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848334"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008492e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0084832c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008492cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00848330"
      ]
    ],
    [
      "unmatched:0084832c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008492fc"
      ]
    ],
    [
      "unmatched:00848338",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008492d4"
      ]
    ]
  ],
  "added": [
    [
      "008492cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008492dc"
      ]
    ],
    [
      "008492d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008492fc"
      ]
    ],
    [
      "008492e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008492d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084832c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008482a8.md#insn-0084832c) · [`00848334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008482a8.md#insn-00848334) · [`00848338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008482a8.md#insn-00848338)

~~~diff
- 0084832c ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 0084832c bytes 20010054
- 00848334 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00848334 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00848334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00848334 bytes df0200f9
- 00848338 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00848338 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00848338 bytes 94ffffb4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92179d600dfd76b23236ad6fdc8420b1"></a>

### [`00848438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848438.md) → [`008493e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/008493e4.md) FUN_008493e4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00848460"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00848480"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0084940c"
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
      "unmatched:00848460",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00849430"
      ]
    ],
    [
      "unmatched:00848480",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0084944c"
      ]
    ],
    [
      "00849440",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0084847c"
      ]
    ]
  ],
  "added": [
    [
      "0084940c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00849430"
      ]
    ],
    [
      "0084942c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0084944c"
      ]
    ],
    [
      "00849440",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00849428"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00848460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848438.md#insn-00848460) · [`00848478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848438.md#insn-00848478) · [`00848480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848438.md#insn-00848480)

~~~diff
- 00848460 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00848460 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00848460 bytes 21010054
- 00848478 ["COPY", "register:0:8", ["register:4040:8"]]
- 00848478 ["INT_ADD", "register:40f0:8", ["const:848478:8", "const:4:8"]]
- 00848478 ["CALLIND", null, ["register:0:8"]]
- 00848478 bytes 00013fd6
- 00848480 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00848480 bytes 00010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e149fc865fad2953cd8ec8874b6e5b32"></a>

### [`008485cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008485cc.md) → [`00849578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/00849578.md) FUN_00849578

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`007ab3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab3d4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`007ab7b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ab/007ab7b0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 20.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008485e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00849594"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00848604"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008485e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007ab3d4"
      ]
    ]
  ],
  "added": [
    [
      "00849594",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007ab7b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008485e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008485cc.md#insn-008485e8) · [`00848604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008485cc.md#insn-00848604)
- 新版 [`00849594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/00849578.md#insn-00849594)

~~~diff
- 008485e8 ["INT_ADD", "register:40f0:8", ["const:8485e8:8", "const:4:8"]]
- 008485e8 ["CALL", null, ["ram:7ab3d4:8"]]
- 008485e8 bytes 7b8bfd97
- 00848604 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00848604 ["RETURN", null, ["register:0:8"]]
- 00848604 bytes c0035fd6
+ 00849594 ["INT_ADD", "register:40f0:8", ["const:849594:8", "const:4:8"]]
+ 00849594 ["CALL", null, ["ram:7ab7b0:8"]]
+ 00849594 bytes 8788fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07df74cacc6f75bf28d355c7c850896a"></a>

### [`00848870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848870.md) → [`0084981c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/0084981c.md) FUN_0084981c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0086a008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a008.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0086afb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086afb4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 56.52% / 新版 52.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008488ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008498a0"
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
      "unmatched:008488ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00849870"
      ]
    ],
    [
      "00849858",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008498bc"
      ]
    ]
  ],
  "added": [
    [
      "00849858",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00849870"
      ]
    ],
    [
      "008498a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008498bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008488ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848870.md#insn-008488ac) · [`00848888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848870.md#insn-00848888)
- 新版 [`008498a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/0084981c.md#insn-008498a0) · [`00849834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/0084981c.md#insn-00849834)

~~~diff
- 008488ac ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 008488ac bytes c0000054
+ 008498a0 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
+ 008498a0 bytes e0000054
- 00848888 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00848888 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00849834 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00849834 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00848888 bytes 540200b4
+ 00849834 bytes 540200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e91079941a2c18836fcae2eb9f83fd8"></a>

### [`00848964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848964.md) → [`00849910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/00849910.md) FUN_00849910

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 60.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848964"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848964"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848968"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00848964",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00848968",
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
      "00849910",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00849914",
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

- 旧版 [`00848964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848964.md#insn-00848964) · [`00848968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848964.md#insn-00848968)
- 新版 [`00849910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/00849910.md#insn-00849910)

~~~diff
- 00848964 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00848964 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00848964 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00848964 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00848964 bytes fd7bbea9
- 00848968 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00848968 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00848968 bytes f30b00f9
+ 00849910 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00849910 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00849910 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00849910 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00849910 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5adaf8d4d54171cf89ae93ac8f60b09c"></a>

### [`00848d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848d9c.md) → [`00849d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/00849d48.md) FUN_00849d48

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 3件 [`00731a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731a00.md) [`00731ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731ad8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 3件 [`00731db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00731/00731db0.md) [`00731e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00731/00731e88.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.26% / 新版 89.26%

CFGの説明率　旧版 73.24% / 新版 70.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848ed4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00849e80"
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
      "unmatched:00848e34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00849df8"
      ]
    ],
    [
      "unmatched:00848ed0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00848edc"
      ]
    ],
    [
      "unmatched:00848ed8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f50"
      ]
    ]
  ],
  "added": [
    [
      "00849de0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00849df8"
      ]
    ],
    [
      "00849e7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00849e88"
      ]
    ],
    [
      "00849e84",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00848e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848d9c.md#insn-00848e34) · [`00848ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848d9c.md#insn-00848ed0) · [`00848ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848d9c.md#insn-00848ed4)

~~~diff
- 00848e34 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00848e34 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00848e34 bytes c1000054
- 00848ed0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00848ed0 ["CBRANCH", null, ["local:b32:8", "tmp:0:1"]]
- 00848ed0 bytes 600000b4
- 00848ed4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:20:8"]]
- 00848ed4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00848ed4 bytes 801200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7faa3a247abc69fa41b2dc23422557dd"></a>

### [`00848fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848fec.md) → [`00849f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/00849f98.md) FUN_00849f98

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 5件 [`00692488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692488.md) [`006924d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/006924d8.md) [`0086a330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a330.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 5件 [`00692838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692838.md) [`00692888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692888.md) [`0086b2dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b2dc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.27% / 新版 86.27%

CFGの説明率　旧版 75.00% / 新版 72.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848ff0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848ff0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848ff4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00848ff0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00848ff4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00848ff8",
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
      "00849f9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00849fa0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00849fa4",
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

- 旧版 [`00848ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848fec.md#insn-00848ff0) · [`00848ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848fec.md#insn-00848ff4) · [`00848ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848fec.md#insn-00848ff8)

~~~diff
- 00848ff0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00848ff0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00848ff0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00848ff0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00848ff0 bytes fd7b01a9
- 00848ff4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00848ff4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00848ff4 bytes f71300f9
- 00848ff8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00848ff8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00848ff8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00848ff8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00848ff8 bytes f65703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05db89249fd9ed7671ba3236a9724a4d"></a>

### [`0084932c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084932c.md) → [`0084a2d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084a2d8.md) FUN_0084a2d8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0086a3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a3e0.md) [`0086bec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bec4.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0086b38c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b38c.md) [`0086ce70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086c/0086ce70.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084932c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084932c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00849330"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084932c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00849330",
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
      "0084a2d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0084a2dc",
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

- 旧版 [`0084932c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084932c.md#insn-0084932c) · [`00849330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084932c.md#insn-00849330)
- 新版 [`0084a2d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084a2d8.md#insn-0084a2d8)

~~~diff
- 0084932c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0084932c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0084932c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0084932c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0084932c bytes fd7bbea9
- 00849330 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00849330 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00849330 bytes f30b00f9
+ 0084a2d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0084a2d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0084a2d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0084a2d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0084a2d8 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9e0e152615730f133b1b3695ebd3c15"></a>

### [`0084978c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084978c.md) → [`0084a738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084a738.md) FUN_0084a738

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084978c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084978c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00849790"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084978c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00849790",
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
      "0084a738",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0084a73c",
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

- 旧版 [`0084978c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084978c.md#insn-0084978c) · [`00849790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084978c.md#insn-00849790)
- 新版 [`0084a738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084a738.md#insn-0084a738)

~~~diff
- 0084978c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0084978c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0084978c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0084978c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0084978c bytes fd7bbea9
- 00849790 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00849790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00849790 bytes f30b00f9
+ 0084a738 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0084a738 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0084a738 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0084a738 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0084a738 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95403838e41dd911ecd44a279391a315"></a>

### [`00849c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849c2c.md) → [`0084abd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084abd8.md) FUN_0084abd8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`007263e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007263e8.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`00726798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00726/00726798.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00849c2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00849c2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00849c30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00849c2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00849c30",
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
      "0084abd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0084abdc",
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

- 旧版 [`00849c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849c2c.md#insn-00849c2c) · [`00849c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849c2c.md#insn-00849c30)
- 新版 [`0084abd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084abd8.md#insn-0084abd8)

~~~diff
- 00849c2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00849c2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00849c2c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00849c2c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00849c2c bytes fd7bbea9
- 00849c30 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00849c30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00849c30 bytes f30b00f9
+ 0084abd8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0084abd8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0084abd8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0084abd8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0084abd8 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc6db93ac0c3c1ac4cd7a2e5e01a9f32"></a>

### [`00849e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849e90.md) → [`0084ae3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084ae3c.md) FUN_0084ae3c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084a098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084a/0084a098.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0084b044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084b/0084b044.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00849eb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0084ae5c"
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
      "unmatched:00849ea8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0084ae60"
      ]
    ],
    [
      "unmatched:00849eb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0084ae78"
      ]
    ],
    [
      "0084ae64",
      "READ",
      [
        "storage",
        "01122c50",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0084ae54",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0084ae60"
      ]
    ],
    [
      "0084ae5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0084ae78"
      ]
    ],
    [
      "0084ae64",
      "READ",
      [
        "storage",
        "01123c10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00849eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849e90.md#insn-00849eb0) · [`00849ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849e90.md#insn-00849ea0)
- 新版 [`0084ae5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084ae3c.md#insn-0084ae5c) · [`0084ae4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084ae3c.md#insn-0084ae4c)

~~~diff
- 00849eb0 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00849eb0 bytes e0000054
+ 0084ae5c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 0084ae5c bytes e0000054
- 00849ea0 ["COPY", "register:40a0:8", ["const:1121000:8"]]
+ 0084ae4c ["COPY", "register:40a0:8", ["const:1122000:8"]]
- 00849ea0 bytes d4460090
+ 0084ae4c bytes d4460090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-882c20232f9cc4ae05b8ddb639e0b065"></a>

### [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) → [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) FUN_008524fc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2198件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md) [`0045abac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045abac.md) [`0045b914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b914.md) [`0045c948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c948.md) · 呼出先 0件 
- 新版 呼出元 2197件 [`0043c5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c5b8.md) [`0043e310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e310.md) [`0045aecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aecc.md) [`0045bc34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045bc34.md) [`0045cc68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045cc68.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00851558"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00852504"
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
      "unmatched:00851554",
      "DATA",
      [
        "storage",
        "00ca8270",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00852500",
      "DATA",
      [
        "storage",
        "00ca9230",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md#insn-00851558) · [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md#insn-00851550)
- 新版 [`00852504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md#insn-00852504)

~~~diff
- 00851558 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00851558 ["RETURN", null, ["register:0:8"]]
- 00851558 bytes c0035fd6
+ 00852504 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00852504 ["RETURN", null, ["register:0:8"]]
+ 00852504 bytes c0035fd6
- 00851550 ["COPY", "register:4000:8", ["const:ca8000:8"]]
- 00851550 bytes a02200f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67ff92d280b878247631c74cea107cc0"></a>

### [`00856d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856d48.md) → [`00857cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857cf4.md) FUN_00857cf4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00854944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/00854944.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008558f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00855/008558f0.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 85.71% / 新版 88.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00856d94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00857d40"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00856d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856d48.md#insn-00856d94) · [`00856d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856d48.md#insn-00856d78)
- 新版 [`00857d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857cf4.md#insn-00857d40) · [`00857d24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857cf4.md#insn-00857d24)

~~~diff
- 00856d94 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00856d94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00856d94 bytes a002803d
+ 00857d40 ["COPY", "tmp:0:8", ["register:40a8:8"]]
+ 00857d40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00857d40 bytes a002803d
- 00856d78 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00856d78 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00857d24 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00857d24 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00856d78 bytes 01020054
+ 00857d24 bytes 01020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beb16022e7e9abac004e41a82e64336d"></a>

### [`0085b350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b350.md) → [`0085c2fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c2fc.md) FUN_0085c2fc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0086defc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086defc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00852a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852a10.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0086eea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086eea8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.52% / 新版 88.52%

CFGの説明率　旧版 65.00% / 新版 81.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0085b354"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0085b354"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0085b358"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0085b354",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0085b358",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0085b35c",
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
      "0085c300",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0085c304",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0085c308",
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

- 旧版 [`0085b354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b350.md#insn-0085b354) · [`0085b358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b350.md#insn-0085b358) · [`0085b35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b350.md#insn-0085b35c)

~~~diff
- 0085b354 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0085b354 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0085b354 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0085b354 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0085b354 bytes fd7b04a9
- 0085b358 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 0085b358 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 0085b358 bytes f72b00f9
- 0085b35c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0085b35c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0085b35c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 0085b35c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0085b35c bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a7571dc3e39b91ab8167ff5b35c0756"></a>

### [`0085ce28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085c/0085ce28.md) → [`0085ddd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085d/0085ddd4.md) FUN_0085ddd4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) · 呼出先 3件 [`005509f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509f4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`007bea00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007be/007bea00.md) · 呼出先 3件 [`00550d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d14.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 63.33% / 新版 63.33%

CFGの説明率　旧版 34.78% / 新版 38.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0085ce2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0085ce2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0085ce30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0085ce2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0085ce30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0085ce34",
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
      "0085ddd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0085dddc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0085dde0",
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

- 旧版 [`0085ce2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085c/0085ce28.md#insn-0085ce2c) · [`0085ce30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085c/0085ce28.md#insn-0085ce30) · [`0085ce34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085c/0085ce28.md#insn-0085ce34)

~~~diff
- 0085ce2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0085ce2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0085ce2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 0085ce2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0085ce2c bytes fd7b07a9
- 0085ce30 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:80:8"]]
- 0085ce30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0085ce30 bytes f54300f9
- 0085ce34 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0085ce34 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0085ce34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 0085ce34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0085ce34 bytes f44f09a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2568946fe84d0bd87ab1358ee776f58"></a>

### [`008629d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00862/008629d8.md) → [`00863984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00863/00863984.md) FUN_00863984

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008acdac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ac/008acdac.md) · 呼出先 5件 [`00597efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597efc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`008add58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ad/008add58.md) · 呼出先 5件 [`0059821c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059821c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 51.95% / 新版 51.95%

CFGの説明率　旧版 22.58% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00862a04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00862a08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00862a0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00862a04",
      "WRITE",
      [
        "storage",
        "0112193a",
        null,
        "undefined2"
      ]
    ],
    [
      "unmatched:00862a08",
      "WRITE",
      [
        "storage",
        "00caa048",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00862a0c",
      "WRITE",
      [
        "storage",
        "00caa050",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008639b0",
      "WRITE",
      [
        "storage",
        "011228fa",
        null,
        "undefined2"
      ]
    ],
    [
      "008639b4",
      "WRITE",
      [
        "storage",
        "00cab008",
        null,
        "undefined4"
      ]
    ],
    [
      "008639b8",
      "WRITE",
      [
        "storage",
        "00cab010",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00862a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00862/008629d8.md#insn-00862a04) · [`00862a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00862/008629d8.md#insn-00862a08) · [`00862a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00862/008629d8.md#insn-00862a0c)

~~~diff
- 00862a04 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00862a04 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00862a04 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00862a04 ["COPY", "tmp:3:8", ["tmp:2:8"]]
- 00862a04 bytes 1f692978
- 00862a08 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00862a08 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00862a08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 00862a08 bytes 1f0100b9
- 00862a0c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00862a0c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00862a0c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00862a0c ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00862a0c bytes 1ffd00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4822ae5f02a3bd5dde41a5faec92844"></a>

### [`008655c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/008655c0.md) → [`0086656c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/0086656c.md) FUN_0086656c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) · 呼出先 0件 
- 新版 呼出元 1件 [`008969d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00896/008969d4.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 75.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00865654"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00866600"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00865654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/008655c0.md#insn-00865654) · [`008655e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/008655c0.md#insn-008655e0)
- 新版 [`00866600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/0086656c.md#insn-00866600) · [`0086658c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/0086656c.md#insn-0086658c)

~~~diff
- 00865654 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00865654 ["RETURN", null, ["register:0:8"]]
- 00865654 bytes c0035fd6
+ 00866600 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00866600 ["RETURN", null, ["register:0:8"]]
+ 00866600 bytes c0035fd6
- 008655e0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008655e0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0086658c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0086658c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 008655e0 bytes c1030054
+ 0086658c bytes c1030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feb07421cbbbeac3496d12e08d873024"></a>

### [`00865660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865660.md) → [`0086660c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/0086660c.md) FUN_0086660c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00865660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00865660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00865664"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00865660",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00865664",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0086569c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0086660c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00866610",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00866648",
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

- 旧版 [`00865660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865660.md#insn-00865660) · [`00865664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865660.md#insn-00865664) · [`0086569c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865660.md#insn-0086569c)

~~~diff
- 00865660 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00865660 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00865660 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00865660 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00865660 bytes fd7bbea9
- 00865664 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00865664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00865664 bytes f30b00f9
- 0086569c ["COPY", "register:0:8", ["register:4040:8"]]
- 0086569c ["INT_ADD", "register:40f0:8", ["const:86569c:8", "const:4:8"]]
- 0086569c ["CALLIND", null, ["register:0:8"]]
- 0086569c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfcf188c36dcd5dca7350d35d55bb66b"></a>

### [`008658e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/008658e4.md) → [`00866890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866890.md) FUN_00866890

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00865700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865700.md) · 呼出先 9件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00a346a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a34/00a346a4.md) [`00a346ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a34/00a346ac.md) [`00a346e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a34/00a346e0.md) [`00a346e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a34/00a346e8.md)
- 新版 呼出元 1件 [`008666ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/008666ac.md) · 呼出先 9件 [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`00a35698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a35/00a35698.md) [`00a356a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a35/00a356a0.md) [`00a356d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a35/00a356d4.md) [`00a356dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a35/00a356dc.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 89.80% / 新版 89.80%

CFGの説明率　旧版 11.11% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0086593c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008668e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0086591c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0086591c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a346e0"
      ]
    ],
    [
      "unmatched:0086593c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00866940"
      ]
    ],
    [
      "unmatched:00865978",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a346a4"
      ]
    ]
  ],
  "added": [
    [
      "008668c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a356d4"
      ]
    ],
    [
      "008668e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00866940"
      ]
    ],
    [
      "00866924",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a35698"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086591c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/008658e4.md#insn-0086591c) · [`0086593c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/008658e4.md#insn-0086593c) · [`00865978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/008658e4.md#insn-00865978)

~~~diff
- 0086591c ["INT_ADD", "register:40f0:8", ["const:86591c:8", "const:4:8"]]
- 0086591c ["CALL", null, ["ram:a346e0:8"]]
- 0086591c bytes 713b0794
- 0086593c ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 0086593c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 0086593c bytes ca020054
- 00865978 ["INT_ADD", "register:40f0:8", ["const:865978:8", "const:4:8"]]
- 00865978 ["CALL", null, ["ram:a346a4:8"]]
- 00865978 bytes 4b3b0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0369ea362738b85b514861e28017bc42"></a>

### [`008659a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/008659a8.md) → [`00866954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866954.md) FUN_00866954

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00865700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865700.md) · 呼出先 6件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00936618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00936/00936618.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008666ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/008666ac.md) · 呼出先 6件 [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`009375c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00937/009375c4.md) [`00a1b6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b6a4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 25.00% / 新版 23.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00865a04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00865a08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00865a0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008659f0",
      "READ",
      [
        "storage",
        "002c2cf0",
        null,
        null
      ]
    ],
    [
      "unmatched:008659fc",
      "READ",
      [
        "storage",
        "002b1129",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008659fc",
      "READ",
      [
        "storage",
        "002b1139",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0086699c",
      "READ",
      [
        "storage",
        "002c2d40",
        null,
        null
      ]
    ],
    [
      "008669a8",
      "READ",
      [
        "storage",
        "002b1200",
        null,
        "string"
      ]
    ],
    [
      "008669a8",
      "READ",
      [
        "storage",
        "002b1210",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00865a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/008659a8.md#insn-00865a04) · [`00865a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/008659a8.md#insn-00865a08) · [`00865a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/008659a8.md#insn-00865a0c)

~~~diff
- 00865a04 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 00865a04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00865a04 bytes 092000b9
- 00865a08 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00865a08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00865a08 bytes e003803d
- 00865a0c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00865a0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00865a0c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00865a0c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5040:16"]]
- 00865a0c bytes 010800ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceb3667285e13984b4b41f1a03dfdf7c"></a>

### [`00865dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865dfc.md) → [`00866da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866da8.md) FUN_00866da8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 55.00% / 新版 57.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00865e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00866dbc"
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
      "unmatched:00865e10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00866e30"
      ]
    ]
  ],
  "added": [
    [
      "00866dbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00866e30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00865e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865dfc.md#insn-00865e10) · [`00865e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865dfc.md#insn-00865e28)
- 新版 [`00866dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866da8.md#insn-00866dbc) · [`00866dd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866da8.md#insn-00866dd4)

~~~diff
- 00865e10 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00865e10 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00865e10 bytes b40300b4
+ 00866dbc ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00866dbc ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00866dbc bytes b40300b4
- 00865e28 ["BRANCH", null, ["local:b13:8"]]
+ 00866dd4 ["BRANCH", null, ["local:b12:8"]]
- 00865e28 bytes 12000014
+ 00866dd4 bytes 12000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d80fcd4a15106b7db68b48a9188b06ab"></a>

### [`0086602c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/0086602c.md) → [`00866fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866fd8.md) FUN_00866fd8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046ec04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ec04.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086602c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086602c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00866030"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0086602c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00866030",
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
      "00866fd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00866fdc",
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

- 旧版 [`0086602c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/0086602c.md#insn-0086602c) · [`00866030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/0086602c.md#insn-00866030)
- 新版 [`00866fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866fd8.md#insn-00866fd8)

~~~diff
- 0086602c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0086602c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0086602c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0086602c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0086602c bytes fd7bbea9
- 00866030 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00866030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00866030 bytes f30b00f9
+ 00866fd8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00866fd8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00866fd8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00866fd8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00866fd8 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ec692d9fa15a102451ea958c40f5dae"></a>

### [`00866ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866ac4.md) → [`00867a70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00867/00867a70.md) FUN_00867a70

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0083f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) · 呼出先 4件 [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md) [`0086776c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/0086776c.md) [`00867fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867fb4.md)
- 新版 呼出元 1件 [`00840888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/00840888.md) · 呼出先 4件 [`0046eb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eb24.md) [`0046f258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f258.md) [`00868718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00868/00868718.md) [`00868f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00868/00868f60.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 58.22% / 新版 58.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 66件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00866aec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00866af8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00866b04"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00866aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866ac4.md#insn-00866aec) · [`00866af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866ac4.md#insn-00866af8) · [`00866b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866ac4.md#insn-00866b04)

~~~diff
- 00866aec ["INT_ADD", "register:40b8:8", ["register:40b8:8", "const:68:8"]]
- 00866aec ["STORE", null, ["const:1b1:8", "register:40b8:8", "register:5000:16"]]
- 00866aec bytes e08e863c
- 00866af8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00866af8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00866af8 bytes 0101803d
- 00866b04 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:ffffffffffffffd8:8"]]
- 00866b04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00866b04 bytes e0829d3c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a5b8459694e1cb9190e8e6a5781b2ad"></a>

### [`00867944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867944.md) → [`008688f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00868/008688f0.md) FUN_008688f0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00866154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866154.md) [`00867a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867a60.md) · 呼出先 2件 [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md)
- 新版 呼出元 2件 [`00867100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00867/00867100.md) [`00868a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00868/00868a0c.md) · 呼出先 2件 [`0046eb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eb24.md) [`0046f258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f258.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.47% / 新版 73.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00867948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00867948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086794c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00867948",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0086794c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00867950",
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
      "008688f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008688f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008688fc",
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

- 旧版 [`00867948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867944.md#insn-00867948) · [`0086794c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867944.md#insn-0086794c) · [`00867950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867944.md#insn-00867950)

~~~diff
- 00867948 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00867948 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00867948 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00867948 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00867948 bytes f85f01a9
- 0086794c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0086794c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0086794c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0086794c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086794c bytes f65702a9
- 00867950 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00867950 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00867950 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00867950 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00867950 bytes f44f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-911625e6aa9156a5a7b0f4cf0ba7d754"></a>

### [`00868730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868730.md) → [`008696dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/008696dc.md) FUN_008696dc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0086828c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/0086828c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00869238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869238.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 76.67% / 新版 76.67%

CFGの説明率　旧版 55.56% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008687e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00868818"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00868850"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008687e4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ],
    [
      "unmatched:008687e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00869774"
      ]
    ],
    [
      "unmatched:00868818",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00869834"
      ]
    ]
  ],
  "added": [
    [
      "00869790",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ],
    [
      "00869794",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00869774"
      ]
    ],
    [
      "008697c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00869834"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00868790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868730.md#insn-00868790) · [`008687e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868730.md#insn-008687e4) · [`008687e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868730.md#insn-008687e8)

~~~diff
- 00868790 ["COPY", "register:0:8", ["register:4040:8"]]
- 00868790 ["INT_ADD", "register:40f0:8", ["const:868790:8", "const:4:8"]]
- 00868790 ["CALLIND", null, ["register:0:8"]]
- 00868790 bytes 00013fd6
- 008687e4 ["INT_ADD", "register:40f0:8", ["const:8687e4:8", "const:4:8"]]
- 008687e4 ["CALL", null, ["callee:00c54d90:8"]]
- 008687e4 bytes 6fad0f94
- 008687e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008687e8 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 008687e8 bytes 00ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b14d9a59df68b06679bc9d20f50ecf1d"></a>

### [`00868898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868898.md) → [`00869844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869844.md) FUN_00869844

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00866da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866da0.md) [`00868898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868898.md) · 呼出先 2件 [`00868898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868898.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00867d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00867/00867d4c.md) [`00869844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869844.md) · 呼出先 2件 [`00869844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869844.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086889c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086889c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008688a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0086889c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008688a0",
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
      "00869848",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0086984c",
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

- 旧版 [`0086889c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868898.md#insn-0086889c) · [`008688a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868898.md#insn-008688a0)
- 新版 [`00869848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869844.md#insn-00869848)

~~~diff
- 0086889c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0086889c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0086889c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0086889c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0086889c bytes fd7bbea9
- 008688a0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008688a0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008688a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008688a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008688a0 bytes f44f01a9
+ 00869848 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00869848 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00869848 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00869848 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00869848 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73fb58e96d57c91bef497f5a64fcff90"></a>

### [`00868920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868920.md) → [`008698cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/008698cc.md) FUN_008698cc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 62.50% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00868920"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00868920"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00868924"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00868920",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00868924",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00868928",
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
      "008698cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008698d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008698d4",
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

- 旧版 [`00868920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868920.md#insn-00868920) · [`00868924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868920.md#insn-00868924) · [`00868928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868920.md#insn-00868928)

~~~diff
- 00868920 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00868920 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00868920 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00868920 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00868920 bytes fd7bbda9
- 00868924 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00868924 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00868924 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00868924 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00868924 bytes f65701a9
- 00868928 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00868928 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00868928 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00868928 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00868928 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-644123826f3abeac24da658c37fec5fd"></a>

### [`00868b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868b18.md) → [`00869ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869ac4.md) FUN_00869ac4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00868a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868a50.md) [`008e3da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3da4.md) [`008e9614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9614.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`008699fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/008699fc.md) [`008e4d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4d50.md) [`008ea5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea5c0.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 66.67% / 新版 72.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00868bd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00868bf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00868c40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00868bd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00869bc0"
      ]
    ],
    [
      "unmatched:00868bf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00869bb4"
      ]
    ],
    [
      "00869bd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00868c3c"
      ]
    ]
  ],
  "added": [
    [
      "00869b7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00869bc0"
      ]
    ],
    [
      "00869b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00869bb4"
      ]
    ],
    [
      "00869bd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00869be8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00868bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868b18.md#insn-00868bd0) · [`00868bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868b18.md#insn-00868bf0) · [`00868c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868b18.md#insn-00868c40)

~~~diff
- 00868bd0 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00868bd0 ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
- 00868bd0 bytes 340200b4
- 00868bf0 ["CBRANCH", null, ["local:b27:8", "register:101:1"]]
- 00868bf0 bytes c0000054
- 00868c40 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00868c40 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00868c40 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00868c40 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00868c40 bytes 88ff0736
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2b2ef9860d58a4970d31b6372a24462"></a>

### [`00868c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868c78.md) → [`00869c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869c24.md) FUN_00869c24

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00868a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868a50.md) [`00868c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868c78.md) [`008e1d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1d98.md) [`008e45b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45b4.md) · 呼出先 2件 [`00868c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868c78.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 4件 [`008699fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/008699fc.md) [`00869c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869c24.md) [`008e2d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e2/008e2d44.md) [`008e5560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5560.md) · 呼出先 2件 [`00869c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869c24.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00868c7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00868c7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00868c80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00868c7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00868c80",
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
      "00869c28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00869c2c",
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

- 旧版 [`00868c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868c78.md#insn-00868c7c) · [`00868c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868c78.md#insn-00868c80)
- 新版 [`00869c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869c24.md#insn-00869c28)

~~~diff
- 00868c7c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00868c7c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00868c7c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00868c7c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00868c7c bytes fd7bbea9
- 00868c80 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00868c80 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00868c80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00868c80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00868c80 bytes f44f01a9
+ 00869c28 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00869c28 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00869c28 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00869c28 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00869c28 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dac8c4cf78b9e918eef70f28d31fa22"></a>

### [`00869364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869364.md) → [`0086a310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a310.md) FUN_0086a310

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0084743c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/0084743c.md) [`00a38120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a38120.md) [`00a3815c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3815c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`008483e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008483e8.md) [`00a39114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a39/00a39114.md) [`00a39150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a39/00a39150.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 73.33% / 新版 73.33%

CFGの説明率　旧版 61.54% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00869364"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00869364"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00869368"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00869364",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00869368",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0086936c",
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
      "0086a310",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0086a314",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0086a318",
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

- 旧版 [`00869364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869364.md#insn-00869364) · [`00869368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869364.md#insn-00869368) · [`0086936c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869364.md#insn-0086936c)

~~~diff
- 00869364 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00869364 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00869364 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00869364 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00869364 bytes fd7bbca9
- 00869368 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00869368 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00869368 bytes f70b00f9
- 0086936c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0086936c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0086936c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0086936c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086936c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b6b55dd47112d8206478fbfd47d8981"></a>

### [`008699e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008699e0.md) → [`0086a98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a98c.md) FUN_0086a98c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008699e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008699e0.md) [`00a82f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a82/00a82f9c.md) · 呼出先 4件 [`008699e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008699e0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`0086a98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a98c.md) [`00a83f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a83/00a83f90.md) · 呼出先 4件 [`0086a98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a98c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 50.00% / 新版 51.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008699f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008699f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0086a99c"
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
      "unmatched:008699f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00869a5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086aa1c"
      ]
    ],
    [
      "unmatched:00869a74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086aa10"
      ]
    ]
  ],
  "added": [
    [
      "0086a99c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0086aa08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086aa1c"
      ]
    ],
    [
      "0086aa20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086aa10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008699f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008699e0.md#insn-008699f0) · [`00869a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008699e0.md#insn-00869a5c) · [`00869a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008699e0.md#insn-00869a74)

~~~diff
- 008699f0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008699f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008699f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 008699f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008699f0 bytes f44f03a9
- 00869a5c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00869a5c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00869a5c bytes a1000054
- 00869a74 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00869a74 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00869a74 bytes 94ffffb4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13fd64e9581c6d36c7de517e7bda0f43"></a>

### [`00869b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869b94.md) → [`0086ab40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086ab40.md) FUN_0086ab40

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008482a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008482a8.md) [`008bace4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bace4.md) [`008bb594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bb594.md) [`008bbab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bbab8.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 5件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`00849254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/00849254.md) [`008bbc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bbc90.md) [`008bc540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bc/008bc540.md) [`008bca64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bc/008bca64.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 81.11% / 新版 81.11%

CFGの説明率　旧版 34.69% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00869c18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00869c1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00869c84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0086ab64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00869bc8"
      ]
    ],
    [
      "0086abc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00869bf8"
      ]
    ],
    [
      "0086abc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00869c0c"
      ]
    ]
  ],
  "added": [
    [
      "0086ab64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086ab74"
      ]
    ],
    [
      "0086ab94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086aba4"
      ]
    ],
    [
      "0086ab98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086abb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00869c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869b94.md#insn-00869c08) · [`00869c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869b94.md#insn-00869c18) · [`00869c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869b94.md#insn-00869c1c)

~~~diff
- 00869c08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00869c08 ["INT_ADD", "register:40f0:8", ["const:869c08:8", "const:4:8"]]
- 00869c08 ["CALLIND", null, ["register:0:8"]]
- 00869c08 bytes 00013fd6
- 00869c18 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00869c18 bytes 80000054
- 00869c1c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00869c1c ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00869c1c bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e3761584855d3f68af92481f92d4117"></a>

### [`00869cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869cfc.md) → [`0086aca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086aca8.md) FUN_0086aca8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 62.50% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00869cfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00869cfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00869d00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00869cfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00869d00",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00869d04",
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
      "0086aca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0086acac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0086acb0",
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

- 旧版 [`00869cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869cfc.md#insn-00869cfc) · [`00869d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869cfc.md#insn-00869d00) · [`00869d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869cfc.md#insn-00869d04)

~~~diff
- 00869cfc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00869cfc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00869cfc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00869cfc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00869cfc bytes fd7bbba9
- 00869d00 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00869d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00869d00 bytes f90b00f9
- 00869d04 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00869d04 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00869d04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00869d04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00869d04 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee19c8370242f4e92bd4c05b4b2f8b53"></a>

### [`00869dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869dd4.md) → [`0086ad80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086ad80.md) FUN_0086ad80

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00848550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848550.md) [`00869dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869dd4.md) · 呼出先 2件 [`00869dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869dd4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`008494fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/008494fc.md) [`0086ad80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086ad80.md) · 呼出先 2件 [`0086ad80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086ad80.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00869dd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00869dd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00869ddc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00869dd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00869ddc",
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
      "0086ad84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0086ad88",
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

- 旧版 [`00869dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869dd4.md#insn-00869dd8) · [`00869ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869dd4.md#insn-00869ddc)
- 新版 [`0086ad84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086ad80.md#insn-0086ad84)

~~~diff
- 00869dd8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00869dd8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00869dd8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00869dd8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00869dd8 bytes fd7bbea9
- 00869ddc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00869ddc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00869ddc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00869ddc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00869ddc bytes f44f01a9
+ 0086ad84 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0086ad84 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0086ad84 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0086ad84 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0086ad84 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df78f6f80a26fef7ee84c377b5d3ca04"></a>

### [`0086a444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a444.md) → [`0086b3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b3f0.md) FUN_0086b3f0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0084935c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084935c.md) [`0086a444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a444.md) [`00b07a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07a64.md) · 呼出先 2件 [`0086a444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a444.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 4件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`0084a308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084a308.md) [`0086b3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b3f0.md) [`00b08a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b08/00b08a58.md) · 呼出先 2件 [`0086b3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b3f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 69.23% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0086a478"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0086b424"
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
      "unmatched:0086a478",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086b450"
      ]
    ]
  ],
  "added": [
    [
      "0086b424",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086b450"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086a478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a444.md#insn-0086a478) · [`0086a444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a444.md#insn-0086a444)
- 新版 [`0086b424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b3f0.md#insn-0086b424) · [`0086b3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b3f0.md#insn-0086b3f0)

~~~diff
- 0086a478 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 0086a478 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 0086a478 bytes 740100b4
+ 0086b424 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 0086b424 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 0086b424 bytes 740100b4
- 0086a444 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 0086a444 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 0086b3f0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 0086b3f0 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 0086a444 bytes 810300b4
+ 0086b3f0 bytes 810300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd8bd513022f4c2fddbb0d5950eb4528"></a>

### [`0086a4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a4b8.md) → [`0086b464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b464.md) FUN_0086b464

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 8件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849458.md) [`0086a4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a4b8.md) [`0097fb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097f/0097fb74.md) [`00981494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/00981494.md) · 呼出先 2件 [`0086a4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a4b8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 8件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`0084a404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084a404.md) [`0086b464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b464.md) [`00980b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00980/00980b20.md) [`00982440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00982/00982440.md) · 呼出先 2件 [`0086b464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b464.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086a4c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086a4c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0086b46c"
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
      "unmatched:0086a4c0",
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
      "0086b46c",
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

- 旧版 [`0086a4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a4b8.md#insn-0086a4c0) · [`0086a4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a4b8.md#insn-0086a4e0)
- 新版 [`0086b48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b464.md#insn-0086b48c) · [`0086b46c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b464.md#insn-0086b46c)

~~~diff
- 0086a4c0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0086a4c0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0086a4c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0086a4c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086a4c0 bytes f44f01a9
- 0086a4e0 ["INT_ADD", "register:40f0:8", ["const:86a4e0:8", "const:4:8"]]
- 0086a4e0 ["CALL", null, ["local:b0:8"]]
+ 0086b48c ["INT_ADD", "register:40f0:8", ["const:86b48c:8", "const:4:8"]]
+ 0086b48c ["CALL", null, ["local:b0:8"]]
- 0086a4e0 bytes f6ffff97
+ 0086b48c bytes f6ffff97
+ 0086b46c ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 0086b46c ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 0086b46c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 0086b46c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0086b46c bytes f44f01a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fc4ef9187ee29cbefb4d3da840b16fd"></a>

### [`0086a5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a5fc.md) → [`0086b5a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b5a8.md) FUN_0086b5a8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008497d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/008497d0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`0084a77c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084a77c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 84.09% / 新版 84.09%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0086a618"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0086a62c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0086a668"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0086a618",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086b644"
      ]
    ],
    [
      "unmatched:0086a62c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086b5ec"
      ]
    ],
    [
      "0086b614",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086b5fc"
      ]
    ]
  ],
  "added": [
    [
      "0086b5c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086b644"
      ]
    ],
    [
      "0086b5d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086b5ec"
      ]
    ],
    [
      "0086b5f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086b5fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086a618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a5fc.md#insn-0086a618) · [`0086a62c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a5fc.md#insn-0086a62c) · [`0086a668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a5fc.md#insn-0086a668)

~~~diff
- 0086a618 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 0086a618 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 0086a618 bytes 150400b4
- 0086a62c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0086a62c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0086a62c bytes a1000054
- 0086a668 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 0086a668 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0086a668 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0086a668 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0086a668 bytes 68fe0736
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04d65b994d3ef0083429f856e0cc7643"></a>

### [`0086a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a9c0.md) → [`0086b96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b96c.md) FUN_0086b96c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0086a974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a974.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0086b920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b920.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 89.47% / 新版 94.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0086aa4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "0086b9f8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0086aa4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a9c0.md#insn-0086aa4c) · [`0086a9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a9c0.md#insn-0086a9f4)
- 新版 [`0086b9f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b96c.md#insn-0086b9f8) · [`0086b9a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086b96c.md#insn-0086b9a0)

~~~diff
- 0086aa4c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0086aa4c ["RETURN", null, ["register:0:8"]]
- 0086aa4c bytes c0035fd6
+ 0086b9f8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 0086b9f8 ["RETURN", null, ["register:0:8"]]
+ 0086b9f8 bytes c0035fd6
- 0086a9f4 ["INT_ADD", "register:40f0:8", ["const:86a9f4:8", "const:4:8"]]
- 0086a9f4 ["CALL", null, ["callee:00c58f50:8"]]
+ 0086b9a0 ["INT_ADD", "register:40f0:8", ["const:86b9a0:8", "const:4:8"]]
+ 0086b9a0 ["CALL", null, ["callee:00c58f50:8"]]
- 0086a9f4 bytes 63b50f94
+ 0086b9a0 bytes 6cb50f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

