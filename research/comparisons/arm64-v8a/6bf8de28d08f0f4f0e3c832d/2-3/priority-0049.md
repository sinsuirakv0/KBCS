# v16.0.2 → v16.0.3 · 最優先の変更候補 (49)

[一覧の目次](README.md)

<a id="compare-4178cf4bbd459c9a9d430b2c24d5b795"></a>

### [`0087d3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d3d8.md) → [`0087e384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087e384.md) FUN_0087e384

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00575ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575ce4.md) [`0058ae08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ae08.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00576004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576004.md) [`0058b128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b128.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.73% / 新版 70.73%

CFGの説明率　旧版 2.78% / 新版 2.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087d3dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087d3dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087d3e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087d3dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087d3e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087d3e4",
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
      "0087e388",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0087e38c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0087e390",
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

- 旧版 [`0087d3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d3d8.md#insn-0087d3dc) · [`0087d3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d3d8.md#insn-0087d3e0) · [`0087d3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d3d8.md#insn-0087d3e4)

~~~diff
- 0087d3dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087d3dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087d3dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0087d3dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087d3dc bytes fd7b03a9
- 0087d3e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 0087d3e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 0087d3e0 bytes f72300f9
- 0087d3e4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0087d3e4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0087d3e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0087d3e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087d3e4 bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3fcc2d0da93d3df7cd57505a32b5c2b"></a>

### [`0087d5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d5b8.md) → [`0087e564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087e564.md) _INIT_162

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 52.54% / 新版 52.54%

CFGの説明率　旧版 64.71% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_store_alignment` 39件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087d5e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087d5fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087d600"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087d5e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087d5f4",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0087d5fc",
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
      "0087e594",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0087e5a0",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0087e5a8",
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

- 旧版 [`0087d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d5b8.md#insn-0087d5e8) · [`0087d5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d5b8.md#insn-0087d5fc) · [`0087d600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d5b8.md#insn-0087d600)

~~~diff
- 0087d5e8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0087d5e8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0087d5e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0087d5e8 bytes a9831ff8
- 0087d5fc ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0087d5fc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 0087d5fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 0087d5fc bytes ea130278
- 0087d600 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 0087d600 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0087d600 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4267448a93cec495ee68f95ccc6ebc83"></a>

### [`0087da1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087da1c.md) → [`0087e9c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087e9c8.md) FUN_0087e9c8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087eb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb78.md) · 呼出先 15件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) [`00597648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597648.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0087fb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fb24.md) · 呼出先 15件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00597070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597070.md) [`00597968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597968.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.71% / 新版 88.71%

CFGの説明率　旧版 30.95% / 新版 28.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087da2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087da2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087da44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087da2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087da44",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087da4c",
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
      "0087e9d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0087e9f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "0087e9f8",
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

- 旧版 [`0087da2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087da1c.md#insn-0087da2c) · [`0087da44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087da1c.md#insn-0087da44) · [`0087da4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087da1c.md#insn-0087da4c)

~~~diff
- 0087da2c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0087da2c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0087da2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 0087da2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087da2c bytes f44f08a9
- 0087da44 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0087da44 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0087da44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0087da44 bytes a8831ff8
- 0087da4c ["COPY", "tmp:0:8", ["const:0:8"]]
- 0087da4c ["COPY", "tmp:1:8", ["const:0:8"]]
- 0087da4c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0087da4c ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0087da4c bytes bf7f3ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6522c654f0655418d82d874ed2727148"></a>

### [`0087dd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dd68.md) → [`0087ed14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087ed14.md) _INIT_163

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0087dc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dc7c.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0087ec28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087ec28.md) [`00bc5880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5880.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.17% / 新版 46.17%

CFGの説明率　旧版 13.91% / 新版 14.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 15件, `unresolved_store_alignment` 66件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087dd6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087dd6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087dd70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087dd6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087dd70",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087dda4",
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
      "0087ed18",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0087ed1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0087ed50",
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

- 旧版 [`0087dd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dd68.md#insn-0087dd6c) · [`0087dd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dd68.md#insn-0087dd70) · [`0087dda4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dd68.md#insn-0087dda4)

~~~diff
- 0087dd6c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087dd6c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087dd6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 0087dd6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087dd6c bytes fd7b12a9
- 0087dd70 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0087dd70 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0087dd70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 0087dd70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087dd70 bytes fc6f13a9
- 0087dda4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0087dda4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 0087dda4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0087dda4 bytes a9031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8358bf13c7ac792f49e6e1f7252083a"></a>

### [`0087e768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e768.md) → [`0087f714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087f714.md) FUN_0087f714

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087e764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e764.md) · 呼出先 15件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0087eda4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eda4.md) [`0087f090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f090.md)
- 新版 呼出元 1件 [`0087f710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087f710.md) · 呼出先 15件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0087fd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fd50.md) [`0088003c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/0088003c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.26% / 新版 74.26%

CFGの説明率　旧版 7.59% / 新版 8.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087e76c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087e76c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087e770"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087e76c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087e770",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087e790",
      "WRITE",
      [
        "storage",
        "Stack[-0xe8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0087f718",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0087f71c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0087f73c",
      "WRITE",
      [
        "storage",
        "Stack[-0xe8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087e76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e768.md#insn-0087e76c) · [`0087e770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e768.md#insn-0087e770) · [`0087e790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e768.md#insn-0087e790)

~~~diff
- 0087e76c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087e76c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087e76c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 0087e76c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087e76c bytes fd7b09a9
- 0087e770 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0087e770 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0087e770 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 0087e770 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087e770 bytes fc6f0aa9
- 0087e790 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 0087e790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0087e790 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c8cab07b4f95385dfde0f5fd2bf13c2"></a>

### [`0087eb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb78.md) → [`0087fb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fb24.md) FUN_0087fb24

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009cc69c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc69c.md) · 呼出先 2件 [`0087da1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087da1c.md) [`0087eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eca0.md)
- 新版 呼出元 1件 [`009cd648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd648.md) · 呼出先 2件 [`0087e9c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087e9c8.md) [`0087fc4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fc4c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087eb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb78.md#insn-0087eb90) · [`0087eb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb78.md#insn-0087eb9c)
- 新版 [`0087fb3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fb24.md#insn-0087fb3c) · [`0087fb48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fb24.md#insn-0087fb48)

~~~diff
- 0087eb90 ["INT_ADD", "register:40f0:8", ["const:87eb90:8", "const:4:8"]]
- 0087eb90 ["CALL", null, ["callee:0087fc4c:8"]]
+ 0087fb3c ["INT_ADD", "register:40f0:8", ["const:87fb3c:8", "const:4:8"]]
+ 0087fb3c ["CALL", null, ["callee:0087fc4c:8"]]
- 0087eb90 bytes 44000094
+ 0087fb3c bytes 44000094
- 0087eb9c ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 0087fb48 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0087eb9c bytes c0000054
+ 0087fb48 bytes c0000054
~~~


<a id="compare-cc86f1e1a970c91aa230a6bd55ba8c12"></a>

### [`0087eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eca0.md) → [`0087fc4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fc4c.md) FUN_0087fc4c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0087eb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb18.md) [`0087eb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb78.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 2件 [`0087fac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fac4.md) [`0087fb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fb24.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 10件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087eca0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087eca0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087eca4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087eca0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087eca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087eca8",
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
      "0087fc4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0087fc50",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0087fc54",
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

- 旧版 [`0087eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eca0.md#insn-0087eca0) · [`0087eca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eca0.md#insn-0087eca4) · [`0087eca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eca0.md#insn-0087eca8)

~~~diff
- 0087eca0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087eca0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087eca0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 0087eca0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0087eca0 bytes fd7bbba9
- 0087eca4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0087eca4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 0087eca4 bytes f90b00f9
- 0087eca8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0087eca8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0087eca8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0087eca8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087eca8 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d612c023c18aa071304122b31649d2fe"></a>

### [`0087eda4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eda4.md) → [`0087fd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fd50.md) FUN_0087fd50

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087e768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e768.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0087eed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eed0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0087f714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087f714.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0087fe7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fe7c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 18.75% / 新版 17.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087ee48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0087fdf4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0087fe38",
      "incomplete_value": true,
      "site": "0087fe50",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0087ee48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eda4.md#insn-0087ee48) · [`0087edd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eda4.md#insn-0087edd8)
- 新版 [`0087fdf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fd50.md#insn-0087fdf4) · [`0087fd84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fd50.md#insn-0087fd84)

~~~diff
- 0087ee48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:10:8"]]
- 0087ee48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0087ee48 bytes 880a00f9
+ 0087fdf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:10:8"]]
+ 0087fdf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0087fdf4 bytes 880a00f9
- 0087edd8 ["INT_ADD", "register:40f0:8", ["const:87edd8:8", "const:4:8"]]
- 0087edd8 ["CALL", null, ["callee:0087fe7c:8"]]
+ 0087fd84 ["INT_ADD", "register:40f0:8", ["const:87fd84:8", "const:4:8"]]
+ 0087fd84 ["CALL", null, ["callee:0087fe7c:8"]]
- 0087edd8 bytes 3e000094
+ 0087fd84 bytes 3e000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44ee045f4002802c020192af6380a051"></a>

### [`0087eed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eed0.md) → [`0087fe7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fe7c.md) FUN_0087fe7c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087eda4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eda4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`0087fd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fd50.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 75.38% / 新版 75.38%

CFGの説明率　旧版 26.67% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087ef08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087ef0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087ef40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087ef54",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c590f0"
      ]
    ],
    [
      "unmatched:0087ef9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087ff60"
      ]
    ],
    [
      "unmatched:0087efa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087fecc"
      ]
    ]
  ],
  "added": [
    [
      "0087ff00",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c590f0"
      ]
    ],
    [
      "0087ff48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087ff60"
      ]
    ],
    [
      "0087ff54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087fecc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087ef08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eed0.md#insn-0087ef08) · [`0087ef0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eed0.md#insn-0087ef0c) · [`0087ef40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eed0.md#insn-0087ef40)

~~~diff
- 0087ef08 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0087ef08 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 0087ef08 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0087ef08 ["INT_ADD", "tmp:1:8", ["register:4010:8", "const:1:8"]]
- 0087ef08 bytes 9515829a
- 0087ef0c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 0087ef0c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0087ef0c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 0087ef0c ["COPY", "register:40c8:8", ["tmp:0:8"]]
- 0087ef0c bytes 59018b9a
- 0087ef40 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0087ef40 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0087ef40 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 0087ef40 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 0087ef40 bytes 16018b9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f76b438acff1e6c7cda7fa6c9da6ae23"></a>

### [`0087f050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f050.md) → [`0087fffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fffc.md) FUN_0087fffc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md)

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
      "definition_site": "00880000",
      "incomplete_value": false,
      "site": "00880004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087f054",
      "incomplete_value": false,
      "site": "0087f058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "00880004",
      "DATA",
      [
        "storage",
        "00c806d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00880004",
      "DATA",
      [
        "storage",
        "00c816a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087f050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f050.md#insn-0087f050) · [`0087f054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f050.md#insn-0087f054)
- 新版 [`0087fffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fffc.md#insn-0087fffc) · [`00880000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fffc.md#insn-00880000)

~~~diff
- 0087f050 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0087fffc ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0087f050 bytes 082000b0
+ 0087fffc bytes 082000d0
- 0087f054 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 0087f054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087f054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087f054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00880000 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 00880000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00880000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00880000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087f054 bytes 08411b91
+ 00880000 bytes 08811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-197f5f9971c49548fb74a52988c46433"></a>

### [`0087f090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f090.md) → [`0088003c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/0088003c.md) FUN_0088003c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087e768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e768.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md)
- 新版 呼出元 1件 [`0087f714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087f714.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 27.27% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f090"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f090"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f094"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087f090",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087f094",
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
      "0088003c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00880040",
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

- 旧版 [`0087f090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f090.md#insn-0087f090) · [`0087f094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f090.md#insn-0087f094) · [`0087f0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f090.md#insn-0087f0c4)
- 新版 [`00880070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/0088003c.md#insn-00880070)

~~~diff
- 0087f090 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087f090 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087f090 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0087f090 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0087f090 bytes fd7bbea9
- 0087f094 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0087f094 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0087f094 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0087f094 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087f094 bytes f44f01a9
- 0087f0c4 ["INT_ADD", "register:40f0:8", ["const:87f0c4:8", "const:4:8"]]
- 0087f0c4 ["CALL", null, ["callee:00c5b8d0:8"]]
+ 00880070 ["INT_ADD", "register:40f0:8", ["const:880070:8", "const:4:8"]]
+ 00880070 ["CALL", null, ["callee:00c5b8d0:8"]]
- 0087f0c4 bytes 0f6e0f94
+ 00880070 bytes 186e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dcbc654c805229820200c67fadf706f"></a>

### [`0087f0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f0fc.md) → [`008800a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/008800a8.md) FUN_008800a8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0087f0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f0fc.md) [`00bc8a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8a74.md) · 呼出先 3件 [`0087f0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f0fc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md)
- 新版 呼出元 2件 [`008800a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/008800a8.md) [`00bc9a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc9/00bc9a68.md) · 呼出先 3件 [`008800a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/008800a8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f0fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f0fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f100"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087f0fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087f100",
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
      "008800a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008800ac",
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

- 旧版 [`0087f0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f0fc.md#insn-0087f0fc) · [`0087f100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f0fc.md#insn-0087f100) · [`0087f124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f0fc.md#insn-0087f124)
- 新版 [`008800d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/008800a8.md#insn-008800d0)

~~~diff
- 0087f0fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087f0fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087f0fc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0087f0fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0087f0fc bytes fd7bbea9
- 0087f100 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0087f100 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0087f100 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0087f100 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087f100 bytes f44f01a9
- 0087f124 ["INT_ADD", "register:40f0:8", ["const:87f124:8", "const:4:8"]]
- 0087f124 ["CALL", null, ["local:b0:8"]]
+ 008800d0 ["INT_ADD", "register:40f0:8", ["const:8800d0:8", "const:4:8"]]
+ 008800d0 ["CALL", null, ["local:b0:8"]]
- 0087f124 bytes f6ffff97
+ 008800d0 bytes f6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e310a0c6f1f2bb4c1459b118610c9f0a"></a>

### [`0087f164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f164.md) → [`00880110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/00880110.md) FUN_00880110

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048eb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048eb40.md) [`00492c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492c0c.md) [`00493064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493064.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.29% / 新版 74.29%

CFGの説明率　旧版 15.38% / 新版 10.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f168"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f168"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f16c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087f168",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087f16c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087f170",
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
      "00880114",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00880118",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0088011c",
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

- 旧版 [`0087f168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f164.md#insn-0087f168) · [`0087f16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f164.md#insn-0087f16c) · [`0087f170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f164.md#insn-0087f170)

~~~diff
- 0087f168 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087f168 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087f168 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0087f168 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087f168 bytes fd7b04a9
- 0087f16c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0087f16c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0087f16c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0087f16c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087f16c bytes f65705a9
- 0087f170 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0087f170 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0087f170 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 0087f170 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087f170 bytes f44f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0ec52dbae7354c5cea1a8a813c08049"></a>

### [`0087f2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f2c0.md) → [`0088026c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/0088026c.md) FUN_0088026c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048eb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048eb40.md) [`00492c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492c0c.md) [`00493064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493064.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.32% / 新版 55.32%

CFGの説明率　旧版 7.14% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f2c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f2c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f2c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087f2c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087f2c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087f2d8",
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
      "00880270",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00880274",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00880284",
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

- 旧版 [`0087f2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f2c0.md#insn-0087f2c4) · [`0087f2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f2c0.md#insn-0087f2c8) · [`0087f2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f2c0.md#insn-0087f2d8)

~~~diff
- 0087f2c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087f2c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087f2c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0087f2c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087f2c4 bytes fd7b04a9
- 0087f2c8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0087f2c8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0087f2c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0087f2c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087f2c8 bytes f44f05a9
- 0087f2d8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0087f2d8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0087f2d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0087f2d8 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17a20afd8158ff5de51ef3f986ece2fa"></a>

### [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) → [`0088036c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/0088036c.md) FUN_0088036c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 55件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`0043f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md) [`0043f7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f7cc.md)
- 新版 呼出元 0件  · 呼出先 55件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043ecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md) [`0043efc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043efc0.md) [`0043f798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f798.md) [`0043faec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043faec.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.14% / 新版 66.14%

CFGの説明率　旧版 14.40% / 新版 14.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 33件, `call_target` 1件, `return_value_candidate` 1件, `store_condition` 1件, `store_value` 1件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 59件, `unresolved_store_alignment` 50件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f3c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f3c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f3c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087f3c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087f3c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087f3cc",
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
      "00880370",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00880374",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00880378",
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

- 旧版 [`0087f3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md#insn-0087f3c4) · [`0087f3c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md#insn-0087f3c8) · [`0087f3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md#insn-0087f3cc)

~~~diff
- 0087f3c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087f3c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087f3c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 0087f3c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087f3c4 bytes fd7b18a9
- 0087f3c8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0087f3c8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0087f3c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:190:8"]]
- 0087f3c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087f3c8 bytes fc6719a9
- 0087f3cc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0087f3cc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0087f3cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 0087f3cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087f3cc bytes f85f1aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3436eb8b80aa92e3e8945ab3c25e2ca0"></a>

### [`008801e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/008801e4.md) → [`00881190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881190.md) FUN_00881190

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) · 呼出先 9件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00492c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492c40.md) [`00493914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md)
- 新版 呼出元 1件 [`0088036c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/0088036c.md) · 呼出先 9件 [`0043ecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md) [`0043f798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f798.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`00492f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492f60.md) [`00493c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493c34.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.69% / 新版 82.69%

CFGの説明率　旧版 28.57% / 新版 27.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00880214"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00880218"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088021c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00880214",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00880218",
      "DATA",
      [
        "storage",
        "0039b1d7",
        null,
        "qword"
      ]
    ],
    [
      "unmatched:00880220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ],
  "added": [
    [
      "008811c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008811c4",
      "DATA",
      [
        "storage",
        "0039b1d7",
        null,
        "dword"
      ]
    ],
    [
      "008811cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00880214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/008801e4.md#insn-00880214) · [`00880218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/008801e4.md#insn-00880218) · [`0088021c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/008801e4.md#insn-0088021c)

~~~diff
- 00880214 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00880214 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00880214 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00880214 bytes a8831ff8
- 00880218 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00880218 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00880218 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00880218 ["COPY", "tmp:3:8", ["tmp:2:8"]]
- 00880218 bytes 1f682978
- 0088021c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3478:8"]]
- 0088021c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:8"]]
- 0088021c bytes 003c1afd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db10be8484f32780adcbb54aea0ee4fb"></a>

### [`00880418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880418.md) → [`008813c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/008813c4.md) FUN_008813c4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 67.74% / 新版 67.74%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00880438"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008813e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0088043c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088042c",
      "READ",
      [
        "storage",
        "00c9ad68",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00880438",
      "DATA",
      [
        "storage",
        "00c65668",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0088043c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008813fc"
      ]
    ]
  ],
  "added": [
    [
      "008813d8",
      "READ",
      [
        "storage",
        "00c9bd38",
        null,
        "pointer"
      ]
    ],
    [
      "008813e4",
      "DATA",
      [
        "storage",
        "00c66638",
        null,
        "undefined *"
      ]
    ],
    [
      "008813e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008813fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00880438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880418.md#insn-00880438) · [`0088043c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880418.md#insn-0088043c) · [`00880448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880418.md#insn-00880448)
- 新版 [`008813f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/008813c4.md#insn-008813f4)

~~~diff
- 00880438 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00880438 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00880438 bytes 080000f9
- 0088043c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 0088043c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0088043c bytes b40000b4
- 00880448 ["INT_ADD", "register:40f0:8", ["const:880448:8", "const:4:8"]]
- 00880448 ["CALL", null, ["callee:00c54d90:8"]]
+ 008813f4 ["INT_ADD", "register:40f0:8", ["const:8813f4:8", "const:4:8"]]
+ 008813f4 ["CALL", null, ["callee:00c54d90:8"]]
- 00880448 bytes 564e0f94
+ 008813f4 bytes 674e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c4356afdd5ac8b54f60893d37776ad5"></a>

### [`00880494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880494.md) → [`00881440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881440.md) FUN_00881440

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 15件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f7cc.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047cfd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cfd8.md) [`0047cff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cff8.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0043ecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md) [`0043faec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043faec.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d2f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d2f8.md) [`0047d318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d318.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.76% / 新版 50.76%

CFGの説明率　旧版 2.56% / 新版 4.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 11件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00880498"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00880498"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088049c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00880498",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088049c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008804a0",
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
      "00881444",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00881448",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0088144c",
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

- 旧版 [`00880498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880494.md#insn-00880498) · [`0088049c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880494.md#insn-0088049c) · [`008804a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880494.md#insn-008804a0)

~~~diff
- 00880498 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00880498 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00880498 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00880498 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00880498 bytes fd7b04a9
- 0088049c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 0088049c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0088049c bytes f52b00f9
- 008804a0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008804a0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008804a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 008804a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008804a0 bytes f44f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9339abd38334eab7bbf8561843ab36e3"></a>

### [`00880c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880c44.md) → [`00881bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881bf0.md) FUN_00881bf0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00881c3c",
      "incomplete_value": false,
      "site": "00881c40",
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
      "definition_site": "00881c38",
      "incomplete_value": true,
      "site": "00881c40",
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

- 旧版 [`00880c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880c44.md#insn-00880c94) · [`00880c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880c44.md#insn-00880c60) · [`00880c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880c44.md#insn-00880c64)
- 新版 [`00881c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881bf0.md#insn-00881c40) · [`00881c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881bf0.md#insn-00881c0c) · [`00881c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881bf0.md#insn-00881c10)

~~~diff
- 00880c94 ["INT_ADD", "register:40f0:8", ["const:880c94:8", "const:4:8"]]
- 00880c94 ["CALL", null, ["callee:00c54d90:8"]]
+ 00881c40 ["INT_ADD", "register:40f0:8", ["const:881c40:8", "const:4:8"]]
+ 00881c40 ["CALL", null, ["callee:00c54d90:8"]]
- 00880c94 bytes 434c0f94
+ 00881c40 bytes 544c0f94
- 00880c60 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00881c0c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00880c60 bytes 80000054
+ 00881c0c bytes 80000054
- 00880c64 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00880c64 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00881c10 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00881c10 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00880c64 bytes 000100b4
+ 00881c10 bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e746a28c2266691a9f149e8210ca8e42"></a>

### [`00880cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880cc8.md) → [`00881c74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881c74.md) FUN_00881c74

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 23.08% / 新版 18.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00880ce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00880d0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00881c90"
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
      "unmatched:00880ce4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00881ca0"
      ]
    ],
    [
      "unmatched:00880d0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00881ccc"
      ]
    ],
    [
      "unmatched:00880d38",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00881c90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00881ca0"
      ]
    ],
    [
      "00881cb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00881ccc"
      ]
    ],
    [
      "00881ce4",
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

- 旧版 [`00880ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880cc8.md#insn-00880ce4) · [`00880d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880cc8.md#insn-00880d0c) · [`00880d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880cc8.md#insn-00880d18)
- 新版 [`00881cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881c74.md#insn-00881cc4)

~~~diff
- 00880ce4 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00880ce4 bytes 80000054
- 00880d0c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00880d0c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00880d0c bytes b30000b4
- 00880d18 ["INT_ADD", "register:40f0:8", ["const:880d18:8", "const:4:8"]]
- 00880d18 ["CALL", null, ["callee:00c54d90:8"]]
+ 00881cc4 ["INT_ADD", "register:40f0:8", ["const:881cc4:8", "const:4:8"]]
+ 00881cc4 ["CALL", null, ["callee:00c54d90:8"]]
- 00880d18 bytes 224c0f94
+ 00881cc4 bytes 334c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dcf584fcd76c94da319d0d80521570e"></a>

### [`00880d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md) → [`00881cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881cf8.md) FUN_00881cf8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 16件 [`004737bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004737bc.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`00873e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873e20.md) [`008810f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008810f0.md) [`00883b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883b2c.md) · 呼出先 14件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md) [`00768420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768420.md)
- 新版 呼出元 16件 [`00473adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/00473adc.md) [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) [`00874dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874dcc.md) [`0088209c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/0088209c.md) [`00884ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884ad8.md) · 呼出先 14件 [`0044fc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044fc40.md) [`00452fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00452/00452fb4.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`007647b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/007647b8.md) [`007687fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007687fc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.88% / 新版 78.88%

CFGの説明率　旧版 30.67% / 新版 29.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 1件, `store_value` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00880d50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00880d50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00880d54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00880d50",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00880d54",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00880d78",
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
      "00881cfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00881d00",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00881d24",
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

- 旧版 [`00880d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md#insn-00880d50) · [`00880d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md#insn-00880d54) · [`00880d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md#insn-00880d78)

~~~diff
- 00880d50 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00880d50 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00880d50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00880d50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00880d50 bytes fd7b0ca9
- 00880d54 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:d0:8"]]
- 00880d54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00880d54 bytes f76b00f9
- 00880d78 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00880d78 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00880d78 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00880d78 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe2bdae1f53b5b6f25eb597a74c99871"></a>

### [`008810f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008810f0.md) → [`0088209c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/0088209c.md) FUN_0088209c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0056089c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/0056089c.md) [`00880d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md) [`008861f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008861f8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`008969d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00896/008969d4.md) · 呼出先 9件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00560bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/00560bbc.md) [`00881cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881cf8.md) [`008871a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/008871a4.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 93.38% / 新版 93.38%

CFGの説明率　旧版 72.34% / 新版 77.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088216c",
      "incomplete_value": false,
      "site": "0088216c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008811c0",
      "incomplete_value": false,
      "site": "008811c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008812c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00882274"
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
      "0088216c",
      "DATA",
      [
        "storage",
        "00c80ef8",
        null,
        "undefined *"
      ]
    ],
    [
      "008821ec",
      "READ",
      [
        "storage",
        "00c80f20",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008812c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00882290"
      ]
    ]
  ],
  "added": [
    [
      "0088216c",
      "DATA",
      [
        "storage",
        "00c81ec8",
        null,
        "undefined *"
      ]
    ],
    [
      "008821ec",
      "READ",
      [
        "storage",
        "00c81ef0",
        null,
        "undefined *"
      ]
    ],
    [
      "00882274",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00882290"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00881274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008810f0.md#insn-00881274) · [`008812c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008810f0.md#insn-008812c4) · [`008812c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008810f0.md#insn-008812c8)
- 新版 [`00882270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/0088209c.md#insn-00882270)

~~~diff
- 00881274 ["COPY", "register:0:8", ["register:4040:8"]]
- 00881274 ["INT_ADD", "register:40f0:8", ["const:881274:8", "const:4:8"]]
- 00881274 ["CALLIND", null, ["register:0:8"]]
- 00881274 bytes 00013fd6
- 008812c4 ["INT_ADD", "register:40f0:8", ["const:8812c4:8", "const:4:8"]]
- 008812c4 ["CALL", null, ["callee:00c54d90:8"]]
+ 00882270 ["INT_ADD", "register:40f0:8", ["const:882270:8", "const:4:8"]]
+ 00882270 ["CALL", null, ["callee:00c54d90:8"]]
- 008812c4 bytes b74a0f94
+ 00882270 bytes c84a0f94
- 008812c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008812c8 ["CBRANCH", null, ["local:b32:8", "tmp:0:1"]]
- 008812c8 bytes e00000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da7b031fc62ceac754aaa43d61cb0cf8"></a>

### [`00881408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881408.md) → [`008823b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/008823b4.md) FUN_008823b4

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00484250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484250.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00484570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00484/00484570.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048eb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048eb40.md) [`00492c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492c0c.md) [`00493064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493064.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 16.67% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088140c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088140c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00881410"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088140c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00881410",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00881420",
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
      "008823b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008823bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008823cc",
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

- 旧版 [`0088140c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881408.md#insn-0088140c) · [`00881410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881408.md#insn-00881410) · [`00881420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881408.md#insn-00881420)

~~~diff
- 0088140c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0088140c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0088140c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0088140c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088140c bytes fd7b04a9
- 00881410 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00881410 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00881410 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00881410 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00881410 bytes f44f05a9
- 00881420 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00881420 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00881420 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00881420 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcf68a787f657c1c5ec8b1018de2900b"></a>

### [`008815dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008815dc.md) → [`00882588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/00882588.md) FUN_00882588

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00484250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484250.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00484570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00484/00484570.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048eb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048eb40.md) [`00492c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492c0c.md) [`00493064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493064.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 60.22% / 新版 60.22%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008815e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008815e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008815e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008815e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008815e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00881618",
      "READ",
      [
        "storage",
        "002ba857",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0088258c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00882590",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008825c4",
      "READ",
      [
        "storage",
        "002ba935",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008815e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008815dc.md#insn-008815e0) · [`008815e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008815dc.md#insn-008815e4) · [`0088161c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008815dc.md#insn-0088161c)

~~~diff
- 008815e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008815e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008815e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008815e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008815e0 bytes fd7b04a9
- 008815e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008815e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008815e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 008815e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008815e4 bytes f44f05a9
- 0088161c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0088161c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0088161c ["COPY", "tmp:2:8", ["register:4040:8"]]
- 0088161c ["COPY", "tmp:3:8", ["tmp:2:8"]]
- 0088161c bytes 1f682838
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-300c70fdb6acc50d9aa47b59ef5119dc"></a>

### [`008817b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008817b0.md) → [`0088275c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/0088275c.md) FUN_0088275c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 28件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md) [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`0045444c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/0045444c.md) [`00456364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456364.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0043ecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md) [`0043f798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f798.md) [`0044fc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044fc40.md) [`0045476c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00454/0045476c.md) [`00456684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00456/00456684.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.25% / 新版 85.25%

CFGの説明率　旧版 27.27% / 新版 32.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_value` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008817dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008817ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00881810"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008817dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:008817e0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "unmatched:008817ec",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "00882788",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "0088278c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "00882798",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008817dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008817b0.md#insn-008817dc) · [`008817ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008817b0.md#insn-008817ec) · [`00881810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008817b0.md#insn-00881810)

~~~diff
- 008817dc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008817dc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008817dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008817dc bytes a8831ff8
- 008817ec ["COPY", "tmp:0:4", ["const:0:4"]]
- 008817ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 008817ec ["COPY", "tmp:2:8", ["register:4040:8"]]
- 008817ec ["COPY", "tmp:3:8", ["tmp:2:8"]]
- 008817ec bytes 1f682838
- 00881810 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00881810 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 00881810 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00881810 bytes a8031c38
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b1c0cf7b7c7481e4f7bfdde0eb65b8d"></a>

### [`00881c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881c84.md) → [`00882c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/00882c30.md) FUN_00882c30

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00881c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881c84.md#insn-00881c94) · [`00881ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881c84.md#insn-00881ca0) · [`00881ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881c84.md#insn-00881ca4)
- 新版 [`00882c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/00882c30.md#insn-00882c40) · [`00882c4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/00882c30.md#insn-00882c4c) · [`00882c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/00882c30.md#insn-00882c50)

~~~diff
- 00881c94 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00881c94 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00882c40 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00882c40 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00881c94 bytes b30000b4
+ 00882c40 bytes b30000b4
- 00881ca0 ["INT_ADD", "register:40f0:8", ["const:881ca0:8", "const:4:8"]]
- 00881ca0 ["CALL", null, ["callee:00c54d90:8"]]
+ 00882c4c ["INT_ADD", "register:40f0:8", ["const:882c4c:8", "const:4:8"]]
+ 00882c4c ["CALL", null, ["callee:00c54d90:8"]]
- 00881ca0 bytes 40480f94
+ 00882c4c bytes 51480f94
- 00881ca4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00881ca4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00882c50 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00882c50 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00881ca4 bytes 800000b4
+ 00882c50 bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3b3dff89b2a3975d1fd54561e9072c7"></a>

### [`00881cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881cd4.md) → [`00882c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/00882c80.md) FUN_00882c80

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048eb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048eb40.md) [`00492c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492c0c.md) [`00493064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493064.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 78.72% / 新版 78.72%

CFGの説明率　旧版 50.00% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00882cbc",
      "incomplete_value": true,
      "site": "00882cd0",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00881d10",
      "incomplete_value": true,
      "site": "00881d24",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:507:8"
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00881d78"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00882d24"
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
      "00882ca8",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "00882cac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "00882cbc",
      "READ",
      [
        "storage",
        "002a2507",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00882ca8",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "00882cac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ],
    [
      "00882cbc",
      "READ",
      [
        "storage",
        "002a25d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00881d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881cd4.md#insn-00881d00) · [`00881d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881cd4.md#insn-00881d64) · [`00881d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881cd4.md#insn-00881d68)
- 新版 [`00882cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/00882c80.md#insn-00882cac)

~~~diff
- 00881d00 ["INT_ADD", "register:40f0:8", ["const:881d00:8", "const:4:8"]]
- 00881d00 ["CALL", null, ["ram:48cd38:8"]]
+ 00882cac ["INT_ADD", "register:40f0:8", ["const:882cac:8", "const:4:8"]]
+ 00882cac ["CALL", null, ["ram:48d058:8"]]
- 00881d00 bytes 0e2cf097
+ 00882cac bytes eb28f097
- 00881d64 ["INT_ADD", "register:40f0:8", ["const:881d64:8", "const:4:8"]]
- 00881d64 ["CALL", null, ["ram:48cd38:8"]]
- 00881d64 bytes f52bf097
- 00881d68 ["INT_ADD", "register:40f0:8", ["const:881d68:8", "const:4:8"]]
- 00881d68 ["CALL", null, ["callee:0048eb40:8"]]
- 00881d68 bytes ae32f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c8da700ff52f3b56ecbaabba83d67d9"></a>

### [`00882054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882054.md) → [`00883000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883000.md) FUN_00883000

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00882064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882054.md#insn-00882064) · [`0088207c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882054.md#insn-0088207c)
- 新版 [`00883010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883000.md#insn-00883010) · [`00883028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883000.md#insn-00883028)

~~~diff
- 00882064 ["INT_ADD", "register:40f0:8", ["const:882064:8", "const:4:8"]]
- 00882064 ["CALL", null, ["callee:008524fc:8"]]
+ 00883010 ["INT_ADD", "register:40f0:8", ["const:883010:8", "const:4:8"]]
+ 00883010 ["CALL", null, ["callee:008524fc:8"]]
- 00882064 bytes 3b3dff97
+ 00883010 bytes 3b3dff97
- 0088207c ["INT_ADD", "register:40f0:8", ["const:88207c:8", "const:4:8"]]
- 0088207c ["CALL", null, ["callee:008524fc:8"]]
+ 00883028 ["INT_ADD", "register:40f0:8", ["const:883028:8", "const:4:8"]]
+ 00883028 ["CALL", null, ["callee:008524fc:8"]]
- 0088207c bytes 353dff97
+ 00883028 bytes 353dff97
~~~


<a id="compare-3576e2f8e478c3a1afa55dc7612cec2f"></a>

### [`00882128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882128.md) → [`008830d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/008830d4.md) FUN_008830d4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0076984c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/0076984c.md) [`00769d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769d30.md) [`00769d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769d3c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00769c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769c28.md) [`0076a10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a10c.md) [`0076a118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a118.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 25.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0088216c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00883118"
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
      "unmatched:0088216c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00883118",
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

- 旧版 [`0088216c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882128.md#insn-0088216c) · [`00882138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882128.md#insn-00882138)
- 新版 [`00883118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/008830d4.md#insn-00883118) · [`008830e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/008830d4.md#insn-008830e4)

~~~diff
- 0088216c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088216c ["INT_ADD", "register:40f0:8", ["const:88216c:8", "const:4:8"]]
- 0088216c ["CALLIND", null, ["register:0:8"]]
- 0088216c bytes 00013fd6
+ 00883118 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883118 ["INT_ADD", "register:40f0:8", ["const:883118:8", "const:4:8"]]
+ 00883118 ["CALLIND", null, ["register:0:8"]]
+ 00883118 bytes 00013fd6
- 00882138 ["INT_ADD", "register:40f0:8", ["const:882138:8", "const:4:8"]]
- 00882138 ["CALL", null, ["callee:008524fc:8"]]
+ 008830e4 ["INT_ADD", "register:40f0:8", ["const:8830e4:8", "const:4:8"]]
+ 008830e4 ["CALL", null, ["callee:008524fc:8"]]
- 00882138 bytes 063dff97
+ 008830e4 bytes 063dff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-747fc73a77874f66bb6f14cfce9c0a40"></a>

### [`008821c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008821c8.md) → [`00883174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883174.md) FUN_00883174

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0086d6d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d6d4.md) · 呼出先 5件 [`00764f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0086e680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e680.md) · 呼出先 5件 [`00765314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765314.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00a1b6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b6a4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00882210"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008831bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008831ec",
      "value": [
        "leaf",
        "ram:765314:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00882240",
      "value": [
        "leaf",
        "ram:764f38:8"
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
      "unmatched:00882210",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00883228"
      ]
    ],
    [
      "008831ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764f38"
      ]
    ]
  ],
  "added": [
    [
      "008831bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00883228"
      ]
    ],
    [
      "008831ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00765314"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008821c8.md#insn-00882210) · [`00882240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008821c8.md#insn-00882240)
- 新版 [`008831ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883174.md#insn-008831ec) · [`008831bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883174.md#insn-008831bc)

~~~diff
- 00882210 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00882210 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00882210 bytes 61030054
- 00882240 ["INT_ADD", "register:40f0:8", ["const:882240:8", "const:4:8"]]
- 00882240 ["CALL", null, ["ram:764f38:8"]]
+ 008831ec ["INT_ADD", "register:40f0:8", ["const:8831ec:8", "const:4:8"]]
+ 008831ec ["CALL", null, ["ram:765314:8"]]
- 00882240 bytes 3e8bfb97
+ 008831ec bytes 4a88fb97
+ 008831bc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008831bc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 008831bc bytes 61030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5d050f927c6ebc8da2edf1b4bf7a175"></a>

### [`008822a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008822a0.md) → [`0088324c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/0088324c.md) FUN_0088324c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0086d6d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d6d4.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`0086e680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e680.md) · 呼出先 1件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008822b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008822a0.md#insn-008822b0) · [`008822d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008822a0.md#insn-008822d8)
- 新版 [`0088325c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/0088324c.md#insn-0088325c) · [`00883284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/0088324c.md#insn-00883284)

~~~diff
- 008822b0 ["INT_ADD", "register:40f0:8", ["const:8822b0:8", "const:4:8"]]
- 008822b0 ["CALL", null, ["callee:008524fc:8"]]
+ 0088325c ["INT_ADD", "register:40f0:8", ["const:88325c:8", "const:4:8"]]
+ 0088325c ["CALL", null, ["callee:008524fc:8"]]
- 008822b0 bytes a83cff97
+ 0088325c bytes a83cff97
- 008822d8 ["COPY", "register:0:8", ["register:4008:8"]]
- 008822d8 ["BRANCHIND", null, ["register:0:8"]]
- 008822d8 bytes 20001fd6
+ 00883284 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00883284 ["BRANCHIND", null, ["register:0:8"]]
+ 00883284 bytes 20001fd6
~~~


<a id="compare-c7cb716522964dfbe91f09ffe8be885f"></a>

### [`0088238c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088238c.md) → [`00883338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883338.md) FUN_00883338

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`0043f7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f7cc.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md) [`0043efc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043efc0.md) [`0043faec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043faec.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.27% / 新版 87.27%

CFGの説明率　旧版 18.18% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008823ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00883358"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0088244c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008823ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00883368",
      "DATA",
      [
        "storage",
        "003c77c8",
        "fde_003c77c8",
        "dword"
      ]
    ],
    [
      "008833a8",
      "DATA",
      [
        "storage",
        "003b5248",
        null,
        "byte[83]"
      ]
    ]
  ],
  "added": [
    [
      "00883358",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00883368",
      "DATA",
      [
        "storage",
        "003c77c8",
        null,
        "dword"
      ]
    ],
    [
      "008833a8",
      "DATA",
      [
        "storage",
        "003b5248",
        null,
        "byte[67]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008823ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088238c.md#insn-008823ac) · [`0088244c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088238c.md#insn-0088244c)
- 新版 [`00883358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883338.md#insn-00883358)

~~~diff
- 008823ac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 008823ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008823ac bytes e80f00f9
- 0088244c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0088244c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 0088244c bytes 21020054
+ 00883358 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
+ 00883358 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00883358 bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c40577aa8bb6d3107e2585ad06166342"></a>

### [`00882498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882498.md) → [`00883444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883444.md) FUN_00883444

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00883450",
      "incomplete_value": false,
      "site": "0088345c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008824a4",
      "incomplete_value": false,
      "site": "008824b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
      "0088345c",
      "DATA",
      [
        "storage",
        "00c807e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088345c",
      "DATA",
      [
        "storage",
        "00c817b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008824a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882498.md#insn-008824a0) · [`008824a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882498.md#insn-008824a4)
- 新版 [`0088344c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883444.md#insn-0088344c) · [`00883450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883444.md#insn-00883450)

~~~diff
- 008824a0 ["COPY", "register:4050:8", ["const:c80000:8"]]
+ 0088344c ["COPY", "register:4050:8", ["const:c81000:8"]]
- 008824a0 bytes ea1f00d0
+ 0088344c bytes ea1f00d0
- 008824a4 ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 008824a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008824a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008824a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00883450 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 00883450 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00883450 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00883450 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008824a4 bytes 4aa11f91
+ 00883450 bytes 4ae11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1af44c25da3605daf987ce58215a5a29"></a>

### [`008824dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008824dc.md) → [`00883488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883488.md) FUN_00883488

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008834a0",
      "incomplete_value": false,
      "site": "008834ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008824f4",
      "incomplete_value": false,
      "site": "00882500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
      "008834ac",
      "DATA",
      [
        "storage",
        "00c807e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008834ac",
      "DATA",
      [
        "storage",
        "00c817b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008824f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008824dc.md#insn-008824f0) · [`008824f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008824dc.md#insn-008824f4) · [`00882524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008824dc.md#insn-00882524)
- 新版 [`0088349c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883488.md#insn-0088349c) · [`008834a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883488.md#insn-008834a0) · [`008834d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883488.md#insn-008834d0)

~~~diff
- 008824f0 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0088349c ["COPY", "register:4040:8", ["const:c81000:8"]]
- 008824f0 bytes e81f00d0
+ 0088349c bytes e81f00d0
- 008824f4 ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 008824f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008824f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008824f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008834a0 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 008834a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008834a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008834a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008824f4 bytes 08a11f91
+ 008834a0 bytes 08e11e91
- 00882524 ["COPY", "register:0:8", ["register:4040:8"]]
- 00882524 ["INT_ADD", "register:40f0:8", ["const:882524:8", "const:4:8"]]
- 00882524 ["CALLIND", null, ["register:0:8"]]
+ 008834d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008834d0 ["INT_ADD", "register:40f0:8", ["const:8834d0:8", "const:4:8"]]
+ 008834d0 ["CALLIND", null, ["register:0:8"]]
- 00882524 bytes 00013fd6
+ 008834d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1527171a511b1200fa300573129d552e"></a>

### [`008825c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008825c0.md) → [`0088356c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/0088356c.md) FUN_0088356c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008825dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00883588"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008825e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008825dc",
      "DATA",
      [
        "storage",
        "00c807e8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008825e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008835b4"
      ]
    ],
    [
      "unmatched:008825fc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00883588",
      "DATA",
      [
        "storage",
        "00c817b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0088358c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008835b4"
      ]
    ],
    [
      "008835a8",
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

- 旧版 [`008825dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008825c0.md#insn-008825dc) · [`008825e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008825c0.md#insn-008825e0) · [`008825fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008825c0.md#insn-008825fc)

~~~diff
- 008825dc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008825dc ["COPY", "tmp:1:8", ["register:4008:8"]]
- 008825dc ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 008825dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008825dc bytes 290401f8
- 008825e0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008825e0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 008825e0 bytes 480100b4
- 008825fc ["COPY", "register:0:8", ["register:4048:8"]]
- 008825fc ["INT_ADD", "register:40f0:8", ["const:8825fc:8", "const:4:8"]]
- 008825fc ["CALLIND", null, ["register:0:8"]]
- 008825fc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcfab50c7d669be590155c32e663234c"></a>

### [`0088273c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088273c.md) → [`008836e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/008836e8.md) FUN_008836e8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00442e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442e98.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00493288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493288.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 77.14% / 新版 65.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00882754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088277c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00882780"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00882754",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00882758",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "unmatched:00882774",
      "READ",
      [
        "storage",
        "002b674a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00883700",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00883704",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ],
    [
      "00883720",
      "READ",
      [
        "storage",
        "002b6819",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088273c.md#insn-00882754) · [`00882758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088273c.md#insn-00882758) · [`0088277c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088273c.md#insn-0088277c)

~~~diff
- 00882754 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00882754 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00882754 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00882754 bytes a8831ff8
- 00882758 ["INT_ADD", "register:40f0:8", ["const:882758:8", "const:4:8"]]
- 00882758 ["CALL", null, ["ram:48cd38:8"]]
- 00882758 bytes 7829f097
- 0088277c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 0088277c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0088277c bytes e02300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-034c49619d5abf35984bf202136a91b1"></a>

### [`008829bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829bc.md) → [`00883968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883968.md) FUN_00883968

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0088397c",
      "incomplete_value": false,
      "site": "00883980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008829d0",
      "incomplete_value": false,
      "site": "008829d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "00883980",
      "DATA",
      [
        "storage",
        "00c808e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883980",
      "DATA",
      [
        "storage",
        "00c818b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008829c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829bc.md#insn-008829c8) · [`008829cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829bc.md#insn-008829cc) · [`008829d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829bc.md#insn-008829d0)
- 新版 [`00883974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883968.md#insn-00883974) · [`00883978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883968.md#insn-00883978) · [`0088397c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883968.md#insn-0088397c)

~~~diff
- 008829c8 ["INT_ADD", "register:40f0:8", ["const:8829c8:8", "const:4:8"]]
- 008829c8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00883974 ["INT_ADD", "register:40f0:8", ["const:883974:8", "const:4:8"]]
+ 00883974 ["CALL", null, ["callee:00c58f30:8"]]
- 008829c8 bytes 66550f94
+ 00883974 bytes 6f550f94
- 008829cc ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00883978 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 008829cc bytes e81f00d0
+ 00883978 bytes e81f00d0
- 008829d0 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 008829d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008829d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008829d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088397c ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 0088397c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088397c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088397c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008829d0 bytes 08a12391
+ 0088397c bytes 08e12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be48cae595f4235076fe74130f65ba8f"></a>

### [`008829e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829e0.md) → [`0088398c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/0088398c.md) FUN_0088398c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00883990",
      "incomplete_value": false,
      "site": "00883994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008829e4",
      "incomplete_value": false,
      "site": "008829e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "00883994",
      "DATA",
      [
        "storage",
        "00c808e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883994",
      "DATA",
      [
        "storage",
        "00c818b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008829e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829e0.md#insn-008829e0) · [`008829e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829e0.md#insn-008829e4)
- 新版 [`0088398c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/0088398c.md#insn-0088398c) · [`00883990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/0088398c.md#insn-00883990)

~~~diff
- 008829e0 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0088398c ["COPY", "register:4040:8", ["const:c81000:8"]]
- 008829e0 bytes e81f00d0
+ 0088398c bytes e81f00d0
- 008829e4 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 008829e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008829e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008829e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00883990 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 00883990 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00883990 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00883990 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008829e4 bytes 08a12391
+ 00883990 bytes 08e12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4db272b2c4fc120177ef05f0966572d6"></a>

### [`00882c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882c94.md) → [`00883c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883c40.md) FUN_00883c40

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00883c48",
      "incomplete_value": false,
      "site": "00883c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882c9c",
      "incomplete_value": false,
      "site": "00882ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "00883c4c",
      "DATA",
      [
        "storage",
        "00c80968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883c4c",
      "DATA",
      [
        "storage",
        "00c81938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882c94.md#insn-00882c98) · [`00882c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882c94.md#insn-00882c9c) · [`00882cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882c94.md#insn-00882cc0)
- 新版 [`00883c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883c40.md#insn-00883c44) · [`00883c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883c40.md#insn-00883c48) · [`00883c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883c40.md#insn-00883c6c)

~~~diff
- 00882c98 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00883c44 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00882c98 bytes e91f00d0
+ 00883c44 bytes e91f00d0
- 00882c9c ["COPY", "tmp:0:8", ["const:968:8"]]
- 00882c9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00882c9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00882c9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00883c48 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00883c48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00883c48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00883c48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00882c9c bytes 29a12591
+ 00883c48 bytes 29e12491
- 00882cc0 ["INT_ADD", "register:40f0:8", ["const:882cc0:8", "const:4:8"]]
- 00882cc0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00883c6c ["INT_ADD", "register:40f0:8", ["const:883c6c:8", "const:4:8"]]
+ 00883c6c ["CALL", null, ["callee:00c58f50:8"]]
- 00882cc0 bytes b0540f94
+ 00883c6c bytes b9540f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8bd277b6b3f5cf4bf0552eca87f441b"></a>

### [`00882cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882cd4.md) → [`00883c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883c80.md) FUN_00883c80

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00882d00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00883cac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00882d24",
      "incomplete_value": true,
      "site": "00882d30",
      "value": [
        "live",
        "register:4098:8"
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
      "unmatched:00882d00",
      "DATA",
      [
        "storage",
        "00c80968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883cac",
      "DATA",
      [
        "storage",
        "00c81938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882cd4.md#insn-00882d00) · [`00882ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882cd4.md#insn-00882ce8)
- 新版 [`00883cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883c80.md#insn-00883cac) · [`00883c94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883c80.md#insn-00883c94)

~~~diff
- 00882d00 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00882d00 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00882d00 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00882d00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00882d00 bytes 0a8400f8
+ 00883cac ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00883cac ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00883cac ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
+ 00883cac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00883cac bytes 0a8400f8
- 00882ce8 ["INT_ADD", "register:40f0:8", ["const:882ce8:8", "const:4:8"]]
- 00882ce8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00883c94 ["INT_ADD", "register:40f0:8", ["const:883c94:8", "const:4:8"]]
+ 00883c94 ["CALL", null, ["callee:00c58f30:8"]]
- 00882ce8 bytes 9e540f94
+ 00883c94 bytes a7540f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30de48d0dc1cb15eb2d666bddabf22b7"></a>

### [`00882ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882ea0.md) → [`00883e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883e4c.md) FUN_00883e4c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00883e60",
      "incomplete_value": false,
      "site": "00883e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882eb4",
      "incomplete_value": false,
      "site": "00882eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "00883e64",
      "DATA",
      [
        "storage",
        "00c809e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883e64",
      "DATA",
      [
        "storage",
        "00c819b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882ea0.md#insn-00882eac) · [`00882eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882ea0.md#insn-00882eb0) · [`00882eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882ea0.md#insn-00882eb4)
- 新版 [`00883e58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883e4c.md#insn-00883e58) · [`00883e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883e4c.md#insn-00883e5c) · [`00883e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883e4c.md#insn-00883e60)

~~~diff
- 00882eac ["INT_ADD", "register:40f0:8", ["const:882eac:8", "const:4:8"]]
- 00882eac ["CALL", null, ["callee:00c58f30:8"]]
+ 00883e58 ["INT_ADD", "register:40f0:8", ["const:883e58:8", "const:4:8"]]
+ 00883e58 ["CALL", null, ["callee:00c58f30:8"]]
- 00882eac bytes 2d540f94
+ 00883e58 bytes 36540f94
- 00882eb0 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00883e5c ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00882eb0 bytes e81f00d0
+ 00883e5c bytes e81f00d0
- 00882eb4 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00882eb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00882eb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00882eb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00883e60 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00883e60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00883e60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00883e60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00882eb4 bytes 08a12791
+ 00883e60 bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4db2ae56e28d75e419224328b463c78"></a>

### [`00882ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882ec4.md) → [`00883e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883e70.md) FUN_00883e70

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00883e74",
      "incomplete_value": false,
      "site": "00883e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882ec8",
      "incomplete_value": false,
      "site": "00882ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "00883e78",
      "DATA",
      [
        "storage",
        "00c809e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883e78",
      "DATA",
      [
        "storage",
        "00c819b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882ec4.md#insn-00882ec4) · [`00882ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882ec4.md#insn-00882ec8)
- 新版 [`00883e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883e70.md#insn-00883e70) · [`00883e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883e70.md#insn-00883e74)

~~~diff
- 00882ec4 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00883e70 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00882ec4 bytes e81f00d0
+ 00883e70 bytes e81f00d0
- 00882ec8 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00882ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00882ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00882ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00883e74 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00883e74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00883e74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00883e74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00882ec8 bytes 08a12791
+ 00883e74 bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-564b18aad86160b9a86c7d2cec09b75f"></a>

### [`00882edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882edc.md) → [`00883e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883e88.md) FUN_00883e88

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00442e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442e98.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00493288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493288.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.20% / 新版 93.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00883ec0",
      "incomplete_value": true,
      "site": "00883ed4",
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
                "const:720:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882f14",
      "incomplete_value": true,
      "site": "00882f28",
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
                "const:6d0:8"
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
      "definition_site": "00883ecc",
      "incomplete_value": true,
      "site": "00883ed8",
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
                "const:cca:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882f20",
      "incomplete_value": true,
      "site": "00882f2c",
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
                "const:bec:8"
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
      "definition_site": "00883ecc",
      "incomplete_value": true,
      "site": "00883ed8",
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
      "definition_site": "00882f20",
      "incomplete_value": true,
      "site": "00882f2c",
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
      "00883ea4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "00883ec0",
      "READ",
      [
        "storage",
        "002c26d0",
        null,
        null
      ]
    ],
    [
      "00883ecc",
      "READ",
      [
        "storage",
        "002bcbec",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00883ea4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ],
    [
      "00883ec0",
      "READ",
      [
        "storage",
        "002c2720",
        null,
        null
      ]
    ],
    [
      "00883ecc",
      "READ",
      [
        "storage",
        "002bccca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882edc.md#insn-00882ef8) · [`00882f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882edc.md#insn-00882f04) · [`00882f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882edc.md#insn-00882f14)
- 新版 [`00883ea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883e88.md#insn-00883ea4) · [`00883eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883e88.md#insn-00883eb0) · [`00883ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883e88.md#insn-00883ec0)

~~~diff
- 00882ef8 ["INT_ADD", "register:40f0:8", ["const:882ef8:8", "const:4:8"]]
- 00882ef8 ["CALL", null, ["ram:48cd38:8"]]
+ 00883ea4 ["INT_ADD", "register:40f0:8", ["const:883ea4:8", "const:4:8"]]
+ 00883ea4 ["CALL", null, ["ram:48d058:8"]]
- 00882ef8 bytes 9027f097
+ 00883ea4 bytes 6d24f097
- 00882f04 ["INT_ADD", "register:40f0:8", ["const:882f04:8", "const:4:8"]]
- 00882f04 ["CALL", null, ["callee:00c58f30:8"]]
+ 00883eb0 ["INT_ADD", "register:40f0:8", ["const:883eb0:8", "const:4:8"]]
+ 00883eb0 ["CALL", null, ["callee:00c58f30:8"]]
- 00882f04 bytes 17540f94
+ 00883eb0 bytes 20540f94
- 00882f14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6d0:8"]]
- 00882f14 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00882f14 ["COPY", "register:5010:8", ["const:0:8"]]
- 00882f14 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00883ec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:720:8"]]
+ 00883ec0 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00883ec0 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00883ec0 ["COPY", "register:5018:8", ["const:0:8"]]
- 00882f14 bytes 00b5c13d
+ 00883ec0 bytes 00c9c13d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c74df36f4abc9b3c734ca77fa0e6753"></a>

### [`00883158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883158.md) → [`00884104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884104.md) FUN_00884104

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00884124",
      "incomplete_value": false,
      "site": "00884128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883178",
      "incomplete_value": false,
      "site": "0088317c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "00884128",
      "DATA",
      [
        "storage",
        "00c80a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00884128",
      "DATA",
      [
        "storage",
        "00c81a38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088316c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883158.md#insn-0088316c) · [`00883174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883158.md#insn-00883174) · [`00883178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883158.md#insn-00883178)
- 新版 [`00884118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884104.md#insn-00884118) · [`00884120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884104.md#insn-00884120) · [`00884124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884104.md#insn-00884124)

~~~diff
- 0088316c ["INT_ADD", "register:40f0:8", ["const:88316c:8", "const:4:8"]]
- 0088316c ["CALL", null, ["callee:00c58f30:8"]]
+ 00884118 ["INT_ADD", "register:40f0:8", ["const:884118:8", "const:4:8"]]
+ 00884118 ["CALL", null, ["callee:00c58f30:8"]]
- 0088316c bytes 7d530f94
+ 00884118 bytes 86530f94
- 00883174 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00884120 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00883174 bytes e81f00b0
+ 00884120 bytes e81f00b0
- 00883178 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 00883178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00883178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00883178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00884124 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 00884124 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00884124 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00884124 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00883178 bytes 08a12991
+ 00884124 bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81119dd7f2abf7552fe1951dde1cc5bd"></a>

### [`00883190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883190.md) → [`0088413c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/0088413c.md) FUN_0088413c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00884144",
      "incomplete_value": false,
      "site": "00884148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883198",
      "incomplete_value": false,
      "site": "0088319c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "00884148",
      "DATA",
      [
        "storage",
        "00c80a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00884148",
      "DATA",
      [
        "storage",
        "00c81a38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883190.md#insn-00883194) · [`00883198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883190.md#insn-00883198)
- 新版 [`00884140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/0088413c.md#insn-00884140) · [`00884144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/0088413c.md#insn-00884144)

~~~diff
- 00883194 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00884140 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00883194 bytes e91f00b0
+ 00884140 bytes e91f00b0
- 00883198 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 00883198 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00883198 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00883198 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00884144 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 00884144 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00884144 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00884144 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00883198 bytes 29a12991
+ 00884144 bytes 29e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18c11d83e6d951bcde0247842ab030bb"></a>

### [`008831b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008831b0.md) → [`0088415c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/0088415c.md) FUN_0088415c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0049331c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/0049331c.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00442e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442e98.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0049363c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/0049363c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.16% / 新版 83.16%

CFGの説明率　旧版 50.00% / 新版 46.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008831d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008831e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008831f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008831d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008831e4",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "unmatched:008831f0",
      "WRITE",
      [
        "storage",
        "Stack[-0xa7]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00884184",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00884190",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "0088419c",
      "WRITE",
      [
        "storage",
        "Stack[-0xa7]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008831d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008831b0.md#insn-008831d8) · [`008831e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008831b0.md#insn-008831e4) · [`008831f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008831b0.md#insn-008831f0)

~~~diff
- 008831d8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008831d8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008831d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008831d8 bytes a8831ff8
- 008831e4 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 008831e4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:80:8"]]
- 008831e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008831e4 bytes e9030239
- 008831f0 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008831f0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9:8"]]
- 008831f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 008831f0 bytes a89200b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22188c311174febb2e87b3710fc55319"></a>

### [`00883694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883694.md) → [`00884640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884640.md) FUN_00884640

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00884644",
      "incomplete_value": false,
      "site": "00884648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883698",
      "incomplete_value": false,
      "site": "0088369c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "00884648",
      "DATA",
      [
        "storage",
        "00c80ad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00884648",
      "DATA",
      [
        "storage",
        "00c81aa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883694.md#insn-00883694) · [`00883698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883694.md#insn-00883698)
- 新版 [`00884640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884640.md#insn-00884640) · [`00884644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884640.md#insn-00884644)

~~~diff
- 00883694 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00884640 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00883694 bytes e81f00b0
+ 00884640 bytes e81f00b0
- 00883698 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 00883698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00883698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00883698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00884644 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 00884644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00884644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00884644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00883698 bytes 08612b91
+ 00884644 bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c14df8f20b6404f1dd985fa1322636ee"></a>

### [`008836ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008836ac.md) → [`00884658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884658.md) FUN_00884658

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0048dca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dca0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0048dfc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048dfc0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088469c",
      "incomplete_value": true,
      "site": "0088469c",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:f50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008836f0",
      "incomplete_value": true,
      "site": "008836f0",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:e83:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00884674",
      "value": [
        "leaf",
        "ram:48d058:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008836c8",
      "value": [
        "leaf",
        "ram:48cd38:8"
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
      "00884674",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "00884688",
      "READ",
      [
        "storage",
        "002a9e83",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00884674",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ],
    [
      "00884688",
      "READ",
      [
        "storage",
        "002a9f50",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008836c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008836ac.md#insn-008836c8) · [`008836d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008836ac.md#insn-008836d4) · [`008836fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008836ac.md#insn-008836fc)
- 新版 [`00884674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884658.md#insn-00884674) · [`00884680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884658.md#insn-00884680) · [`008846a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884658.md#insn-008846a8)

~~~diff
- 008836c8 ["INT_ADD", "register:40f0:8", ["const:8836c8:8", "const:4:8"]]
- 008836c8 ["CALL", null, ["ram:48cd38:8"]]
+ 00884674 ["INT_ADD", "register:40f0:8", ["const:884674:8", "const:4:8"]]
+ 00884674 ["CALL", null, ["ram:48d058:8"]]
- 008836c8 bytes 9c25f097
+ 00884674 bytes 7922f097
- 008836d4 ["COPY", "tmp:0:8", ["const:e83:8"]]
- 008836d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008836d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008836d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00884680 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 00884680 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00884680 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00884680 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008836d4 bytes 290d3a91
+ 00884680 bytes 29413d91
- 008836fc ["INT_ADD", "register:40f0:8", ["const:8836fc:8", "const:4:8"]]
- 008836fc ["CALL", null, ["callee:0048d1b4:8"]]
+ 008846a8 ["INT_ADD", "register:40f0:8", ["const:8846a8:8", "const:4:8"]]
+ 008846a8 ["CALL", null, ["callee:0048d1b4:8"]]
- 008836fc bytes e625f097
+ 008846a8 bytes c322f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99f0d9cac38a03355cacf592c45430bb"></a>

### [`008837bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008837bc.md) → [`00884768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884768.md) FUN_00884768

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00884780",
      "incomplete_value": false,
      "site": "0088478c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008837d4",
      "incomplete_value": false,
      "site": "008837e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "0088478c",
      "DATA",
      [
        "storage",
        "00c80b68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088478c",
      "DATA",
      [
        "storage",
        "00c81b38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008837d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008837bc.md#insn-008837d0) · [`008837d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008837bc.md#insn-008837d4) · [`00883804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008837bc.md#insn-00883804)
- 新版 [`0088477c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884768.md#insn-0088477c) · [`00884780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884768.md#insn-00884780) · [`008847b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884768.md#insn-008847b0)

~~~diff
- 008837d0 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0088477c ["COPY", "register:4040:8", ["const:c81000:8"]]
- 008837d0 bytes e81f00b0
+ 0088477c bytes e81f00b0
- 008837d4 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 008837d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008837d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008837d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00884780 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 00884780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00884780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00884780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008837d4 bytes 08a12d91
+ 00884780 bytes 08e12c91
- 00883804 ["COPY", "register:0:8", ["register:4040:8"]]
- 00883804 ["INT_ADD", "register:40f0:8", ["const:883804:8", "const:4:8"]]
- 00883804 ["CALLIND", null, ["register:0:8"]]
+ 008847b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008847b0 ["INT_ADD", "register:40f0:8", ["const:8847b0:8", "const:4:8"]]
+ 008847b0 ["CALLIND", null, ["register:0:8"]]
- 00883804 bytes 00013fd6
+ 008847b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee425f541a4e66283f8228718388cc66"></a>

### [`0088384c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/0088384c.md) → [`008847f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/008847f8.md) FUN_008847f8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00884810",
      "incomplete_value": false,
      "site": "0088481c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883864",
      "incomplete_value": false,
      "site": "00883870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0088486c",
      "incomplete_value": true,
      "site": "00884870",
      "value": [
        "live",
        "register:40a0:8"
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
      "0088481c",
      "DATA",
      [
        "storage",
        "00c80b68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088481c",
      "DATA",
      [
        "storage",
        "00c81b38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008838c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/0088384c.md#insn-008838c4) · [`00883860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/0088384c.md#insn-00883860) · [`00883864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/0088384c.md#insn-00883864)
- 新版 [`00884870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/008847f8.md#insn-00884870) · [`0088480c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/008847f8.md#insn-0088480c) · [`00884810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/008847f8.md#insn-00884810)

~~~diff
- 008838c4 ["INT_ADD", "register:40f0:8", ["const:8838c4:8", "const:4:8"]]
- 008838c4 ["CALL", null, ["callee:00c58f20:8"]]
+ 00884870 ["INT_ADD", "register:40f0:8", ["const:884870:8", "const:4:8"]]
+ 00884870 ["CALL", null, ["callee:00c58f20:8"]]
- 008838c4 bytes a3510f94
+ 00884870 bytes ac510f94
- 00883860 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0088480c ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00883860 bytes e81f00b0
+ 0088480c bytes e81f00b0
- 00883864 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 00883864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00883864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00883864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00884810 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 00884810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00884810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00884810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00883864 bytes 08a12d91
+ 00884810 bytes 08e12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-986dbf6473597697be6595ac2adf8a72"></a>

### [`008838d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008838d8.md) → [`00884884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884884.md) FUN_00884884

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 72.97% / 新版 72.97%

CFGの説明率　旧版 38.46% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008838d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008838d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008838dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008838d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008838dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00883904",
      "DATA",
      [
        "storage",
        "00c80b68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00884884",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00884888",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008848b0",
      "DATA",
      [
        "storage",
        "00c81b38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008838d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008838d8.md#insn-008838d8) · [`008838dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008838d8.md#insn-008838dc) · [`00883904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008838d8.md#insn-00883904)

~~~diff
- 008838d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008838d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008838d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008838d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008838d8 bytes fd7bbea9
- 008838dc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008838dc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008838dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008838dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008838dc bytes f44f01a9
- 00883904 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00883904 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00883904 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1ba2671003a58bc1f73c160b29eef88"></a>

### [`00883988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883988.md) → [`00884934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884934.md) FUN_00884934

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.29% / 新版 74.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008839a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008839b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00884954"
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
      "unmatched:008839b0",
      "DATA",
      [
        "storage",
        "00c80b68",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008839cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00884994"
      ]
    ],
    [
      "unmatched:008839d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088499c"
      ]
    ]
  ],
  "added": [
    [
      "0088495c",
      "DATA",
      [
        "storage",
        "00c81b38",
        null,
        "undefined *"
      ]
    ],
    [
      "00884978",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00884994"
      ]
    ],
    [
      "00884984",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088499c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008839a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883988.md#insn-008839a8) · [`008839b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883988.md#insn-008839b0) · [`008839cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883988.md#insn-008839cc)

~~~diff
- 008839a8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:10:8"]]
- 008839a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008839a8 bytes 2004803d
- 008839b0 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008839b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008839b0 bytes 290000f9
- 008839cc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008839cc ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 008839cc bytes e00000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b79b18a70ac04e50d7d9111290647710"></a>

### [`00883b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883b2c.md) → [`00884ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884ad8.md) FUN_00884ad8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00768848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768848.md) [`00768c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768c40.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00880d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00768c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/00768c24.md) [`0076901c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/0076901c.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00881cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881cf8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 57.92% / 新版 57.92%

CFGの説明率　旧版 22.58% / 新版 22.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_condition` 1件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00883c3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00883c3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00883c40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00883b84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00884c98"
      ]
    ],
    [
      "00884b84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768c40"
      ]
    ],
    [
      "00884b94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768848"
      ]
    ]
  ],
  "added": [
    [
      "00884b30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00884c98"
      ]
    ],
    [
      "00884b84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0076901c"
      ]
    ],
    [
      "00884b94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768c24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883b2c.md#insn-00883b84) · [`00883c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883b2c.md#insn-00883c3c) · [`00883c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883b2c.md#insn-00883c40)

~~~diff
- 00883b84 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00883b84 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
- 00883b84 bytes 400b00b4
- 00883c3c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00883c3c ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00883c3c ["COPY", "tmp:2:8", ["register:8:8"]]
- 00883c3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00883c3c bytes f35300a9
- 00883c40 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00883c40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00883c40 bytes e80b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d5a0bc444405fa300836bd1b85c7a6d"></a>

### [`00884104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884104.md) → [`008850b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008850b0.md) FUN_008850b0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 76.92% / 新版 90.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008850c8",
      "incomplete_value": false,
      "site": "008850d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088411c",
      "incomplete_value": false,
      "site": "00884128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00884180"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0088512c"
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
      "008850d4",
      "DATA",
      [
        "storage",
        "00c80be8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00884180",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "008850d4",
      "DATA",
      [
        "storage",
        "00c81bb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0088512c",
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

- 旧版 [`00884180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884104.md#insn-00884180) · [`00884118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884104.md#insn-00884118)
- 新版 [`0088512c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008850b0.md#insn-0088512c) · [`008850c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008850b0.md#insn-008850c4)

~~~diff
- 00884180 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884180 ["INT_ADD", "register:40f0:8", ["const:884180:8", "const:4:8"]]
- 00884180 ["CALLIND", null, ["register:0:8"]]
- 00884180 bytes 00013fd6
+ 0088512c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088512c ["INT_ADD", "register:40f0:8", ["const:88512c:8", "const:4:8"]]
+ 0088512c ["CALLIND", null, ["register:0:8"]]
+ 0088512c bytes 00013fd6
- 00884118 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 008850c4 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00884118 bytes e81f0090
+ 008850c4 bytes e81f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efeae6a3f5923f2cf642e6de8f2a3049"></a>

### [`00884194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884194.md) → [`00885140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885140.md) FUN_00885140

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885158",
      "incomplete_value": false,
      "site": "00885164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008841ac",
      "incomplete_value": false,
      "site": "008841b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00884204"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "008851b0"
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
      "00885164",
      "DATA",
      [
        "storage",
        "00c80be8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00884204",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00885164",
      "DATA",
      [
        "storage",
        "00c81bb8",
        null,
        "undefined *"
      ]
    ],
    [
      "008851b0",
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

- 旧版 [`00884204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884194.md#insn-00884204) · [`008841a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884194.md#insn-008841a8)
- 新版 [`008851b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885140.md#insn-008851b0) · [`00885154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885140.md#insn-00885154)

~~~diff
- 00884204 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884204 ["INT_ADD", "register:40f0:8", ["const:884204:8", "const:4:8"]]
- 00884204 ["CALLIND", null, ["register:0:8"]]
- 00884204 bytes 00013fd6
+ 008851b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008851b0 ["INT_ADD", "register:40f0:8", ["const:8851b0:8", "const:4:8"]]
+ 008851b0 ["CALLIND", null, ["register:0:8"]]
+ 008851b0 bytes 00013fd6
- 008841a8 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00885154 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 008841a8 bytes e81f0090
+ 00885154 bytes e81f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-548609fd5b23d36be83e0b8016ec0ccb"></a>

### [`00884220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884220.md) → [`008851cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008851cc.md) FUN_008851cc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088424c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008851f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00884278"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088424c",
      "DATA",
      [
        "storage",
        "00c80be8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00884278",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088523c"
      ]
    ]
  ],
  "added": [
    [
      "008851f8",
      "DATA",
      [
        "storage",
        "00c81bb8",
        null,
        "undefined *"
      ]
    ],
    [
      "00885224",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088523c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088424c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884220.md#insn-0088424c) · [`00884264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884220.md#insn-00884264) · [`00884278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884220.md#insn-00884278)
- 新版 [`00885210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008851cc.md#insn-00885210)

~~~diff
- 0088424c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0088424c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0088424c bytes 090000f9
- 00884264 ["INT_ADD", "register:40f0:8", ["const:884264:8", "const:4:8"]]
- 00884264 ["CALL", null, ["callee:00c54d60:8"]]
+ 00885210 ["INT_ADD", "register:40f0:8", ["const:885210:8", "const:4:8"]]
+ 00885210 ["CALL", null, ["callee:00c54d60:8"]]
- 00884264 bytes c33e0f94
+ 00885210 bytes d43e0f94
- 00884278 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00884278 bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-061d9c2ddf07555703ddb6d5095c5bd3"></a>

### [`008842d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008842d0.md) → [`0088527c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088527c.md) FUN_0088527c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

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
      "definition_site": "00885298",
      "incomplete_value": false,
      "site": "008852a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008842ec",
      "incomplete_value": false,
      "site": "008842f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "008852a4",
      "DATA",
      [
        "storage",
        "00c80be8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008852a4",
      "DATA",
      [
        "storage",
        "00c81bb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008842e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008842d0.md#insn-008842e8) · [`008842ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008842d0.md#insn-008842ec) · [`0088430c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008842d0.md#insn-0088430c)
- 新版 [`00885294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088527c.md#insn-00885294) · [`00885298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088527c.md#insn-00885298) · [`008852b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088527c.md#insn-008852b8)

~~~diff
- 008842e8 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00885294 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 008842e8 bytes e91f0090
+ 00885294 bytes e91f0090
- 008842ec ["COPY", "tmp:0:8", ["const:be8:8"]]
- 008842ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008842ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008842ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00885298 ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 00885298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00885298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00885298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008842ec bytes 29a12f91
+ 00885298 bytes 29e12e91
- 0088430c ["INT_ADD", "register:40f0:8", ["const:88430c:8", "const:4:8"]]
- 0088430c ["CALL", null, ["callee:00c54d60:8"]]
+ 008852b8 ["INT_ADD", "register:40f0:8", ["const:8852b8:8", "const:4:8"]]
+ 008852b8 ["CALL", null, ["callee:00c54d60:8"]]
- 0088430c bytes 993e0f94
+ 008852b8 bytes aa3e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5961377b814ba89df322b7d17e9799c"></a>

### [`008844b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008844b0.md) → [`0088545c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088545c.md) FUN_0088545c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885474",
      "incomplete_value": false,
      "site": "00885480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008844c8",
      "incomplete_value": false,
      "site": "008844d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "00885480",
      "DATA",
      [
        "storage",
        "00c80c68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885480",
      "DATA",
      [
        "storage",
        "00c81c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008844c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008844b0.md#insn-008844c4) · [`008844c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008844b0.md#insn-008844c8) · [`008844f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008844b0.md#insn-008844f8)
- 新版 [`00885470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088545c.md#insn-00885470) · [`00885474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088545c.md#insn-00885474) · [`008854a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088545c.md#insn-008854a4)

~~~diff
- 008844c4 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00885470 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 008844c4 bytes e81f0090
+ 00885470 bytes e81f0090
- 008844c8 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 008844c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008844c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008844c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885474 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00885474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008844c8 bytes 08a13191
+ 00885474 bytes 08e13091
- 008844f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008844f8 ["INT_ADD", "register:40f0:8", ["const:8844f8:8", "const:4:8"]]
- 008844f8 ["CALLIND", null, ["register:0:8"]]
+ 008854a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008854a4 ["INT_ADD", "register:40f0:8", ["const:8854a4:8", "const:4:8"]]
+ 008854a4 ["CALLIND", null, ["register:0:8"]]
- 008844f8 bytes 00013fd6
+ 008854a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-141787eb6b8cc5b8fc5ed868c8912637"></a>

### [`00884540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884540.md) → [`008854ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008854ec.md) FUN_008854ec

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00885504",
      "incomplete_value": false,
      "site": "00885510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884558",
      "incomplete_value": false,
      "site": "00884564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "00885510",
      "DATA",
      [
        "storage",
        "00c80c68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885510",
      "DATA",
      [
        "storage",
        "00c81c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884540.md#insn-00884554) · [`00884558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884540.md#insn-00884558) · [`00884588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884540.md#insn-00884588)
- 新版 [`00885500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008854ec.md#insn-00885500) · [`00885504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008854ec.md#insn-00885504) · [`00885534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008854ec.md#insn-00885534)

~~~diff
- 00884554 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00885500 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00884554 bytes e81f0090
+ 00885500 bytes e81f0090
- 00884558 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 00884558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00884558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00884558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885504 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00885504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00884558 bytes 08a13191
+ 00885504 bytes 08e13091
- 00884588 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884588 ["INT_ADD", "register:40f0:8", ["const:884588:8", "const:4:8"]]
- 00884588 ["CALLIND", null, ["register:0:8"]]
+ 00885534 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885534 ["INT_ADD", "register:40f0:8", ["const:885534:8", "const:4:8"]]
+ 00885534 ["CALLIND", null, ["register:0:8"]]
- 00884588 bytes 00013fd6
+ 00885534 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f81921647cb395cd2ba898b57687f5c"></a>

### [`008845cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008845cc.md) → [`00885578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885578.md) FUN_00885578

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 66.67% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008845f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008845fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00884600"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008845f8",
      "DATA",
      [
        "storage",
        "00c80c68",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00884604",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008855c0"
      ]
    ]
  ],
  "added": [
    [
      "008855a4",
      "DATA",
      [
        "storage",
        "00c81c38",
        null,
        "undefined *"
      ]
    ],
    [
      "008855b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008855c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008845e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008845cc.md#insn-008845e0) · [`008845f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008845cc.md#insn-008845f8) · [`008845fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008845cc.md#insn-008845fc)
- 新版 [`0088558c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885578.md#insn-0088558c)

~~~diff
- 008845e0 ["INT_ADD", "register:40f0:8", ["const:8845e0:8", "const:4:8"]]
- 008845e0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0088558c ["INT_ADD", "register:40f0:8", ["const:88558c:8", "const:4:8"]]
+ 0088558c ["CALL", null, ["callee:00c58f30:8"]]
- 008845e0 bytes 604e0f94
+ 0088558c bytes 694e0f94
- 008845f8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008845f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008845f8 bytes 090000f9
- 008845fc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 008845fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008845fc bytes 0004803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36e9ca234bb29108dafc9b8e3d32d4db"></a>

### [`0088467c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/0088467c.md) → [`00885628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885628.md) FUN_00885628

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 58.33% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088469c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008846a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00885648"
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
      "unmatched:008846a4",
      "DATA",
      [
        "storage",
        "00c80c68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885650",
      "DATA",
      [
        "storage",
        "00c81c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088469c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/0088467c.md#insn-0088469c) · [`008846a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/0088467c.md#insn-008846a4) · [`008846b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/0088467c.md#insn-008846b8)
- 新版 [`00885664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885628.md#insn-00885664)

~~~diff
- 0088469c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:10:8"]]
- 0088469c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0088469c bytes 2004803d
- 008846a4 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008846a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008846a4 bytes 290000f9
- 008846b8 ["INT_ADD", "register:40f0:8", ["const:8846b8:8", "const:4:8"]]
- 008846b8 ["CALL", null, ["callee:00c54d60:8"]]
+ 00885664 ["INT_ADD", "register:40f0:8", ["const:885664:8", "const:4:8"]]
+ 00885664 ["CALL", null, ["callee:00c54d60:8"]]
- 008846b8 bytes ae3d0f94
+ 00885664 bytes bf3d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7070ba850ae5c01b84ffacff3c14b80"></a>

### [`0088485c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/0088485c.md) → [`00885808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885808.md) FUN_00885808

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 61.54% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885820",
      "incomplete_value": false,
      "site": "0088582c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884874",
      "incomplete_value": false,
      "site": "00884880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "0088582c",
      "DATA",
      [
        "storage",
        "00c80cf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088582c",
      "DATA",
      [
        "storage",
        "00c81cc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/0088485c.md#insn-00884870) · [`00884874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/0088485c.md#insn-00884874) · [`00884888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/0088485c.md#insn-00884888)
- 新版 [`0088581c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885808.md#insn-0088581c) · [`00885820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885808.md#insn-00885820) · [`00885834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885808.md#insn-00885834)

~~~diff
- 00884870 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0088581c ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00884870 bytes e81f0090
+ 0088581c bytes e81f0090
- 00884874 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 00884874 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00884874 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00884874 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885820 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 00885820 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885820 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885820 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00884874 bytes 08e13391
+ 00885820 bytes 08213391
- 00884888 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00884888 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00885834 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00885834 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00884888 bytes 000100b4
+ 00885834 bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6eebab6b229a12592de13493dec72ad9"></a>

### [`00884978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884978.md) → [`00885924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885924.md) FUN_00885924

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0088594c",
      "incomplete_value": false,
      "site": "00885950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008849a0",
      "incomplete_value": false,
      "site": "008849a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "00885950",
      "DATA",
      [
        "storage",
        "00c80cf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885950",
      "DATA",
      [
        "storage",
        "00c81cc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088498c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884978.md#insn-0088498c) · [`0088499c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884978.md#insn-0088499c) · [`008849a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884978.md#insn-008849a0)
- 新版 [`00885938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885924.md#insn-00885938) · [`00885948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885924.md#insn-00885948) · [`0088594c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885924.md#insn-0088594c)

~~~diff
- 0088498c ["INT_ADD", "register:40f0:8", ["const:88498c:8", "const:4:8"]]
- 0088498c ["CALL", null, ["callee:00c58f30:8"]]
+ 00885938 ["INT_ADD", "register:40f0:8", ["const:885938:8", "const:4:8"]]
+ 00885938 ["CALL", null, ["callee:00c58f30:8"]]
- 0088498c bytes 754d0f94
+ 00885938 bytes 7e4d0f94
- 0088499c ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00885948 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 0088499c bytes e91f0090
+ 00885948 bytes e91f0090
- 008849a0 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 008849a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008849a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008849a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088594c ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 0088594c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088594c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088594c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008849a0 bytes 29e13391
+ 0088594c bytes 29213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f14a960b56d9251377779f735b789111"></a>

### [`00884a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884a28.md) → [`008859d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008859d4.md) FUN_008859d4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

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
      "definition_site": "008859f0",
      "incomplete_value": false,
      "site": "008859fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884a44",
      "incomplete_value": false,
      "site": "00884a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "008859fc",
      "DATA",
      [
        "storage",
        "00c80cf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008859fc",
      "DATA",
      [
        "storage",
        "00c81cc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884a28.md#insn-00884a40) · [`00884a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884a28.md#insn-00884a44) · [`00884a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884a28.md#insn-00884a64)
- 新版 [`008859ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008859d4.md#insn-008859ec) · [`008859f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008859d4.md#insn-008859f0) · [`00885a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008859d4.md#insn-00885a10)

~~~diff
- 00884a40 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 008859ec ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00884a40 bytes e91f0090
+ 008859ec bytes e91f0090
- 00884a44 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 00884a44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00884a44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00884a44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008859f0 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 008859f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008859f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008859f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00884a44 bytes 29e13391
+ 008859f0 bytes 29213391
- 00884a64 ["INT_ADD", "register:40f0:8", ["const:884a64:8", "const:4:8"]]
- 00884a64 ["CALL", null, ["callee:00c54d60:8"]]
+ 00885a10 ["INT_ADD", "register:40f0:8", ["const:885a10:8", "const:4:8"]]
+ 00885a10 ["CALL", null, ["callee:00c54d60:8"]]
- 00884a64 bytes c33c0f94
+ 00885a10 bytes d43c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc4544be50a2627cf01d3aaa935b789a"></a>

### [`00885050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885050.md) → [`00885ffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885ffc.md) FUN_00885ffc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00886014",
      "incomplete_value": false,
      "site": "00886020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885068",
      "incomplete_value": false,
      "site": "00885074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "00886020",
      "DATA",
      [
        "storage",
        "00c80d68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886020",
      "DATA",
      [
        "storage",
        "00c81d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885050.md#insn-00885064) · [`00885068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885050.md#insn-00885068) · [`00885098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885050.md#insn-00885098)
- 新版 [`00886010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885ffc.md#insn-00886010) · [`00886014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885ffc.md#insn-00886014) · [`00886044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885ffc.md#insn-00886044)

~~~diff
- 00885064 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00886010 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00885064 bytes c81f00f0
+ 00886010 bytes c81f00f0
- 00885068 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 00885068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00886014 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00886014 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00886014 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00886014 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885068 bytes 08a13591
+ 00886014 bytes 08e13491
- 00885098 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885098 ["INT_ADD", "register:40f0:8", ["const:885098:8", "const:4:8"]]
- 00885098 ["CALLIND", null, ["register:0:8"]]
+ 00886044 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886044 ["INT_ADD", "register:40f0:8", ["const:886044:8", "const:4:8"]]
+ 00886044 ["CALLIND", null, ["register:0:8"]]
- 00885098 bytes 00013fd6
+ 00886044 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4a95a01b3ba82885eb864a185c668df"></a>

### [`0088516c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088516c.md) → [`00886118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886118.md) FUN_00886118

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00886140",
      "incomplete_value": false,
      "site": "00886144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885194",
      "incomplete_value": false,
      "site": "00885198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "00886144",
      "DATA",
      [
        "storage",
        "00c80d68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886144",
      "DATA",
      [
        "storage",
        "00c81d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088516c.md#insn-00885180) · [`00885190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088516c.md#insn-00885190) · [`00885194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088516c.md#insn-00885194)
- 新版 [`0088612c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886118.md#insn-0088612c) · [`0088613c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886118.md#insn-0088613c) · [`00886140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886118.md#insn-00886140)

~~~diff
- 00885180 ["INT_ADD", "register:40f0:8", ["const:885180:8", "const:4:8"]]
- 00885180 ["CALL", null, ["callee:00c58f30:8"]]
+ 0088612c ["INT_ADD", "register:40f0:8", ["const:88612c:8", "const:4:8"]]
+ 0088612c ["CALL", null, ["callee:00c58f30:8"]]
- 00885180 bytes 784b0f94
+ 0088612c bytes 814b0f94
- 00885190 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 0088613c ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00885190 bytes c91f00f0
+ 0088613c bytes c91f00f0
- 00885194 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 00885194 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00885194 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00885194 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00886140 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00886140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00886140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00886140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00885194 bytes 29a13591
+ 00886140 bytes 29e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f815424c274d76fe8acdee18831c3fd"></a>

### [`0088521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088521c.md) → [`008861c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008861c8.md) FUN_008861c8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

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
      "definition_site": "008861e4",
      "incomplete_value": false,
      "site": "008861f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885238",
      "incomplete_value": false,
      "site": "00885244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "008861f0",
      "DATA",
      [
        "storage",
        "00c80d68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008861f0",
      "DATA",
      [
        "storage",
        "00c81d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088521c.md#insn-00885234) · [`00885238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088521c.md#insn-00885238) · [`00885258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088521c.md#insn-00885258)
- 新版 [`008861e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008861c8.md#insn-008861e0) · [`008861e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008861c8.md#insn-008861e4) · [`00886204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008861c8.md#insn-00886204)

~~~diff
- 00885234 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 008861e0 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00885234 bytes c91f00f0
+ 008861e0 bytes c91f00f0
- 00885238 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 00885238 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00885238 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00885238 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008861e4 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 008861e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008861e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008861e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00885238 bytes 29a13591
+ 008861e4 bytes 29e13491
- 00885258 ["INT_ADD", "register:40f0:8", ["const:885258:8", "const:4:8"]]
- 00885258 ["CALL", null, ["callee:00c54d60:8"]]
+ 00886204 ["INT_ADD", "register:40f0:8", ["const:886204:8", "const:4:8"]]
+ 00886204 ["CALL", null, ["callee:00c54d60:8"]]
- 00885258 bytes c63a0f94
+ 00886204 bytes d73a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8545f43808408562f3bc841c4268d38"></a>

### [`008852bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008852bc.md) → [`00886268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886268.md) FUN_00886268

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 81.82% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008852d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008852bc.md#insn-008852d8) · [`008852dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008852bc.md#insn-008852dc) · [`008852e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008852bc.md#insn-008852e4)
- 新版 [`00886284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886268.md#insn-00886284) · [`00886288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886268.md#insn-00886288) · [`00886290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886268.md#insn-00886290)

~~~diff
- 008852d8 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00886284 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 008852d8 bytes 80000054
+ 00886284 bytes 80000054
- 008852dc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008852dc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00886288 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00886288 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 008852dc bytes 000100b4
+ 00886288 bytes 000100b4
- 008852e4 ["BRANCH", null, ["local:b4:8"]]
+ 00886290 ["BRANCH", null, ["local:b5:8"]]
- 008852e4 bytes 03000014
+ 00886290 bytes 03000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d0622eb9b41191fde54f604a42b36f0"></a>

### [`008853fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008853fc.md) → [`008863a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008863a8.md) FUN_008863a8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008863c4",
      "incomplete_value": false,
      "site": "008863cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885418",
      "incomplete_value": false,
      "site": "00885420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "008863cc",
      "DATA",
      [
        "storage",
        "00c80df8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008863cc",
      "DATA",
      [
        "storage",
        "00c81dc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008853fc.md#insn-00885414) · [`00885418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008853fc.md#insn-00885418) · [`00885430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008853fc.md#insn-00885430)
- 新版 [`008863c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008863a8.md#insn-008863c0) · [`008863c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008863a8.md#insn-008863c4) · [`008863dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008863a8.md#insn-008863dc)

~~~diff
- 00885414 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 008863c0 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00885414 bytes c81f00f0
+ 008863c0 bytes c81f00f0
- 00885418 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 00885418 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885418 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885418 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008863c4 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 008863c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008863c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008863c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885418 bytes 08e13791
+ 008863c4 bytes 08213791
- 00885430 ["INT_ADD", "register:40f0:8", ["const:885430:8", "const:4:8"]]
- 00885430 ["CALL", null, ["callee:00c54d90:8"]]
+ 008863dc ["INT_ADD", "register:40f0:8", ["const:8863dc:8", "const:4:8"]]
+ 008863dc ["CALL", null, ["callee:00c54d90:8"]]
- 00885430 bytes 5c3a0f94
+ 008863dc bytes 6d3a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a24f20c8709367fdc59c2604c214dee"></a>

### [`00885498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885498.md) → [`00886444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886444.md) FUN_00886444

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00886460",
      "incomplete_value": false,
      "site": "00886468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008854b4",
      "incomplete_value": false,
      "site": "008854bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "00886468",
      "DATA",
      [
        "storage",
        "00c80df8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886468",
      "DATA",
      [
        "storage",
        "00c81dc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008854b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885498.md#insn-008854b0) · [`008854b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885498.md#insn-008854b4) · [`008854cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885498.md#insn-008854cc)
- 新版 [`0088645c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886444.md#insn-0088645c) · [`00886460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886444.md#insn-00886460) · [`00886478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886444.md#insn-00886478)

~~~diff
- 008854b0 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0088645c ["COPY", "register:4040:8", ["const:c81000:8"]]
- 008854b0 bytes c81f00f0
+ 0088645c bytes c81f00f0
- 008854b4 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 008854b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008854b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008854b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00886460 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00886460 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00886460 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00886460 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008854b4 bytes 08e13791
+ 00886460 bytes 08213791
- 008854cc ["INT_ADD", "register:40f0:8", ["const:8854cc:8", "const:4:8"]]
- 008854cc ["CALL", null, ["callee:00c54d90:8"]]
+ 00886478 ["INT_ADD", "register:40f0:8", ["const:886478:8", "const:4:8"]]
+ 00886478 ["CALL", null, ["callee:00c54d90:8"]]
- 008854cc bytes 353a0f94
+ 00886478 bytes 463a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4e7bfa7614823e0388fff83ad99882c"></a>

### [`0088552c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088552c.md) → [`008864d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008864d8.md) FUN_008864d8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00886504",
      "incomplete_value": false,
      "site": "00886504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885558",
      "incomplete_value": false,
      "site": "00885558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "00886504",
      "DATA",
      [
        "storage",
        "00c80df8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886504",
      "DATA",
      [
        "storage",
        "00c81dc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088552c.md#insn-00885540) · [`0088554c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088552c.md#insn-0088554c) · [`00885550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088552c.md#insn-00885550)
- 新版 [`008864ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008864d8.md#insn-008864ec) · [`008864f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008864d8.md#insn-008864f8) · [`008864fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008864d8.md#insn-008864fc)

~~~diff
- 00885540 ["INT_ADD", "register:40f0:8", ["const:885540:8", "const:4:8"]]
- 00885540 ["CALL", null, ["callee:00c58f30:8"]]
+ 008864ec ["INT_ADD", "register:40f0:8", ["const:8864ec:8", "const:4:8"]]
+ 008864ec ["CALL", null, ["callee:00c58f30:8"]]
- 00885540 bytes 884a0f94
+ 008864ec bytes 914a0f94
- 0088554c ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 008864f8 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0088554c bytes c81f00f0
+ 008864f8 bytes c81f00f0
- 00885550 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 00885550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008864fc ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 008864fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008864fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008864fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885550 bytes 08e13791
+ 008864fc bytes 08213791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77159b6bb86dd03f717c7bb715a63be9"></a>

### [`008855d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008855d4.md) → [`00886580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886580.md) FUN_00886580

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008865a0",
      "incomplete_value": false,
      "site": "008865a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008855f4",
      "incomplete_value": false,
      "site": "008855f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "008865a0",
      "DATA",
      [
        "storage",
        "00c80df8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008865a0",
      "DATA",
      [
        "storage",
        "00c81dc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008855ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008855d4.md#insn-008855ec) · [`008855f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008855d4.md#insn-008855f0) · [`00885610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008855d4.md#insn-00885610)
- 新版 [`00886598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886580.md#insn-00886598) · [`0088659c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886580.md#insn-0088659c) · [`008865bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886580.md#insn-008865bc)

~~~diff
- 008855ec ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00886598 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 008855ec bytes c81f00f0
+ 00886598 bytes c81f00f0
- 008855f0 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 008855f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008855f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008855f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088659c ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 0088659c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088659c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088659c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008855f0 bytes 08e13791
+ 0088659c bytes 08213791
- 00885610 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885610 ["INT_ADD", "register:40f0:8", ["const:885610:8", "const:4:8"]]
- 00885610 ["CALLIND", null, ["register:0:8"]]
+ 008865bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008865bc ["INT_ADD", "register:40f0:8", ["const:8865bc:8", "const:4:8"]]
+ 008865bc ["CALLIND", null, ["register:0:8"]]
- 00885610 bytes 00013fd6
+ 008865bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-959ef24383795a3c1a7f59083f82f857"></a>

### [`0088577c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088577c.md) → [`00886728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886728.md) FUN_00886728

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00768a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768a80.md) [`00768ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768ee8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00880700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880700.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00768e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/00768e5c.md) [`007692c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/007692c4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008816ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/008816ac.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 78.79% / 新版 72.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885918"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885924"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008868c4"
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
      "00886798",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768a80"
      ]
    ],
    [
      "008867cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00880700"
      ]
    ],
    [
      "008867dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768ee8"
      ]
    ]
  ],
  "added": [
    [
      "00886798",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e5c"
      ]
    ],
    [
      "008867cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008816ac"
      ]
    ],
    [
      "008867dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007692c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008857ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088577c.md#insn-008857ec) · [`00885830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088577c.md#insn-00885830) · [`00885878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088577c.md#insn-00885878)
- 新版 [`00886798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886728.md#insn-00886798) · [`008867dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886728.md#insn-008867dc) · [`00886824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886728.md#insn-00886824)

~~~diff
- 008857ec ["INT_ADD", "register:40f0:8", ["const:8857ec:8", "const:4:8"]]
- 008857ec ["CALL", null, ["ram:768a80:8"]]
+ 00886798 ["INT_ADD", "register:40f0:8", ["const:886798:8", "const:4:8"]]
+ 00886798 ["CALL", null, ["ram:768e5c:8"]]
- 008857ec bytes a58cfb97
+ 00886798 bytes b189fb97
- 00885830 ["INT_ADD", "register:40f0:8", ["const:885830:8", "const:4:8"]]
- 00885830 ["CALL", null, ["ram:768ee8:8"]]
+ 008867dc ["INT_ADD", "register:40f0:8", ["const:8867dc:8", "const:4:8"]]
+ 008867dc ["CALL", null, ["ram:7692c4:8"]]
- 00885830 bytes ae8dfb97
+ 008867dc bytes ba8afb97
- 00885878 ["INT_ADD", "register:40f0:8", ["const:885878:8", "const:4:8"]]
- 00885878 ["CALL", null, ["callee:00c54d60:8"]]
+ 00886824 ["INT_ADD", "register:40f0:8", ["const:886824:8", "const:4:8"]]
+ 00886824 ["CALL", null, ["callee:00c54d60:8"]]
- 00885878 bytes 3e390f94
+ 00886824 bytes 4f390f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcf08ed187499a65c2ebb53ac5e93031"></a>

### [`00885ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885ae8.md) → [`00886a94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886a94.md) FUN_00886a94

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 72.73% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00885b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885ae8.md#insn-00885b04) · [`00885b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885ae8.md#insn-00885b08) · [`00885b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885ae8.md#insn-00885b10)
- 新版 [`00886ab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886a94.md#insn-00886ab0) · [`00886ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886a94.md#insn-00886ab4) · [`00886abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886a94.md#insn-00886abc)

~~~diff
- 00885b04 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00886ab0 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00885b04 bytes 80000054
+ 00886ab0 bytes 80000054
- 00885b08 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00885b08 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00886ab4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00886ab4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00885b08 bytes 000100b4
+ 00886ab4 bytes 000100b4
- 00885b10 ["BRANCH", null, ["local:b4:8"]]
+ 00886abc ["BRANCH", null, ["local:b6:8"]]
- 00885b10 bytes 03000014
+ 00886abc bytes 03000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e58ad84172d76e9dbf6fbf8214f25ab"></a>

### [`00885bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885bfc.md) → [`00886ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886ba8.md) FUN_00886ba8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 68.57% / 新版 68.57%

CFGの説明率　旧版 33.33% / 新版 23.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885bfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885bfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885c00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00885bfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00885c00",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00885c20",
      "DATA",
      [
        "storage",
        "00c80e68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886ba8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00886bac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00886bcc",
      "DATA",
      [
        "storage",
        "00c81e38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885bfc.md#insn-00885bfc) · [`00885c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885bfc.md#insn-00885c00) · [`00885c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885bfc.md#insn-00885c20)

~~~diff
- 00885bfc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00885bfc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00885bfc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00885bfc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00885bfc bytes fd7bbea9
- 00885c00 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00885c00 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00885c00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00885c00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00885c00 bytes f44f01a9
- 00885c20 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00885c20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00885c20 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a31786fe0bcedb6e71adad375f462803"></a>

### [`00885c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885c88.md) → [`00886c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886c34.md) FUN_00886c34

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885cb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885d00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00886c60"
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
      "unmatched:00885cb4",
      "DATA",
      [
        "storage",
        "00c80e68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886c60",
      "DATA",
      [
        "storage",
        "00c81e38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885c88.md#insn-00885cb4) · [`00885d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885c88.md#insn-00885d00) · [`00885d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885c88.md#insn-00885d08)
- 新版 [`00886cb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886c34.md#insn-00886cb4)

~~~diff
- 00885cb4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00885cb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00885cb4 bytes 090000f9
- 00885d00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:50:8"]]
- 00885d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00885d00 bytes 612a00f9
- 00885d08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885d08 ["INT_ADD", "register:40f0:8", ["const:885d08:8", "const:4:8"]]
- 00885d08 ["CALLIND", null, ["register:0:8"]]
+ 00886cb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886cb4 ["INT_ADD", "register:40f0:8", ["const:886cb4:8", "const:4:8"]]
+ 00886cb4 ["CALLIND", null, ["register:0:8"]]
- 00885d08 bytes 00013fd6
+ 00886cb4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c18974a60b64d81e04a7b4e775690c25"></a>

### [`00885d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885d38.md) → [`00886ce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886ce4.md) FUN_00886ce4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 50.00% / 新版 38.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885d58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885d60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00886d04"
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
      "unmatched:00885d60",
      "DATA",
      [
        "storage",
        "00c80e68",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00885d7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00886d44"
      ]
    ]
  ],
  "added": [
    [
      "00886d0c",
      "DATA",
      [
        "storage",
        "00c81e38",
        null,
        "undefined *"
      ]
    ],
    [
      "00886d28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00886d44"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885d38.md#insn-00885d58) · [`00885d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885d38.md#insn-00885d60) · [`00885d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885d38.md#insn-00885d74)
- 新版 [`00886d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886ce4.md#insn-00886d20)

~~~diff
- 00885d58 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:10:8"]]
- 00885d58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00885d58 bytes 2004803d
- 00885d60 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00885d60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00885d60 bytes 290000f9
- 00885d74 ["INT_ADD", "register:40f0:8", ["const:885d74:8", "const:4:8"]]
- 00885d74 ["CALL", null, ["callee:00c54d60:8"]]
+ 00886d20 ["INT_ADD", "register:40f0:8", ["const:886d20:8", "const:4:8"]]
+ 00886d20 ["CALL", null, ["callee:00c54d60:8"]]
- 00885d74 bytes ff370f94
+ 00886d20 bytes 10380f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4195619b5161c56650c3275273882ca4"></a>

### [`00885f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885f18.md) → [`00886ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886ec4.md) FUN_00886ec4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00886edc",
      "incomplete_value": false,
      "site": "00886ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885f30",
      "incomplete_value": false,
      "site": "00885f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "00886ee8",
      "DATA",
      [
        "storage",
        "00c80ef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886ee8",
      "DATA",
      [
        "storage",
        "00c81ec8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885f18.md#insn-00885f2c) · [`00885f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885f18.md#insn-00885f30) · [`00885f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885f18.md#insn-00885f60)
- 新版 [`00886ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886ec4.md#insn-00886ed8) · [`00886edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886ec4.md#insn-00886edc) · [`00886f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886ec4.md#insn-00886f0c)

~~~diff
- 00885f2c ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00886ed8 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00885f2c bytes c81f00f0
+ 00886ed8 bytes c81f00f0
- 00885f30 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 00885f30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885f30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885f30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00886edc ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00886edc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00886edc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00886edc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885f30 bytes 08e13b91
+ 00886edc bytes 08213b91
- 00885f60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885f60 ["INT_ADD", "register:40f0:8", ["const:885f60:8", "const:4:8"]]
- 00885f60 ["CALLIND", null, ["register:0:8"]]
+ 00886f0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886f0c ["INT_ADD", "register:40f0:8", ["const:886f0c:8", "const:4:8"]]
+ 00886f0c ["CALLIND", null, ["register:0:8"]]
- 00885f60 bytes 00013fd6
+ 00886f0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91be3c3e1accdf3caba33b50746a3fa4"></a>

### [`00885f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885f88.md) → [`00886f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886f34.md) FUN_00886f34

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_value, constant, local_def_use, operands_and_dependencies, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00886f4c",
      "incomplete_value": false,
      "site": "00886f58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885fa0",
      "incomplete_value": false,
      "site": "00885fac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00886f54",
      "incomplete_value": true,
      "site": "00886f5c",
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
                "register:4000:8"
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
      "definition_site": "00885fa8",
      "incomplete_value": true,
      "site": "00885fb0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "00886f58",
      "DATA",
      [
        "storage",
        "00c80ef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886f58",
      "DATA",
      [
        "storage",
        "00c81ec8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885f88.md#insn-00885f9c) · [`00885fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885f88.md#insn-00885fa0) · [`00885fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885f88.md#insn-00885fd0)
- 新版 [`00886f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886f34.md#insn-00886f48) · [`00886f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886f34.md#insn-00886f4c) · [`00886f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886f34.md#insn-00886f7c)

~~~diff
- 00885f9c ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00886f48 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00885f9c bytes c81f00f0
+ 00886f48 bytes c81f00f0
- 00885fa0 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 00885fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00886f4c ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00886f4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00886f4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00886f4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885fa0 bytes 08e13b91
+ 00886f4c bytes 08213b91
- 00885fd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885fd0 ["INT_ADD", "register:40f0:8", ["const:885fd0:8", "const:4:8"]]
- 00885fd0 ["CALLIND", null, ["register:0:8"]]
+ 00886f7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886f7c ["INT_ADD", "register:40f0:8", ["const:886f7c:8", "const:4:8"]]
+ 00886f7c ["CALLIND", null, ["register:0:8"]]
- 00885fd0 bytes 00013fd6
+ 00886f7c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-637940c41ede8f0c5284e0ff352ca3ca"></a>

### [`008860cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008860cc.md) → [`00887078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887078.md) FUN_00887078

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.40% / 新版 81.40%

CFGの説明率　旧版 41.67% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008860e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00887094"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00886138"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008860e8",
      "DATA",
      [
        "storage",
        "00c80ef8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00886138",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008870fc"
      ]
    ],
    [
      "unmatched:00886164",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00887094",
      "DATA",
      [
        "storage",
        "00c81ec8",
        null,
        "undefined *"
      ]
    ],
    [
      "008870e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008870fc"
      ]
    ],
    [
      "00887110",
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

- 旧版 [`008860e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008860cc.md#insn-008860e8) · [`00886138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008860cc.md#insn-00886138) · [`00886164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008860cc.md#insn-00886164)

~~~diff
- 008860e8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008860e8 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 008860e8 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:10:8"]]
- 008860e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008860e8 bytes 880601f8
- 00886138 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00886138 bytes c0000054
- 00886164 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886164 ["INT_ADD", "register:40f0:8", ["const:886164:8", "const:4:8"]]
- 00886164 ["CALLIND", null, ["register:0:8"]]
- 00886164 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0623be1032da3b211fff8239d35a9dd"></a>

### [`00886194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886194.md) → [`00887140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887140.md) FUN_00887140

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 88.89% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008861d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886194.md#insn-008861d0) · [`008861d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886194.md#insn-008861d8)
- 新版 [`0088717c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887140.md#insn-0088717c) · [`00887184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887140.md#insn-00887184)

~~~diff
- 008861d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008861d0 ["INT_ADD", "register:40f0:8", ["const:8861d0:8", "const:4:8"]]
- 008861d0 ["CALLIND", null, ["register:0:8"]]
+ 0088717c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088717c ["INT_ADD", "register:40f0:8", ["const:88717c:8", "const:4:8"]]
+ 0088717c ["CALLIND", null, ["register:0:8"]]
- 008861d0 bytes 00013fd6
+ 0088717c bytes 00013fd6
- 008861d8 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 008861d8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 008861d8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 008861d8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00887184 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00887184 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00887184 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00887184 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 008861d8 bytes 88000037
+ 00887184 bytes 88000037
~~~


<a id="compare-5d88d7d8477b4b291aa0318c1ed8b27e"></a>

### [`00886258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886258.md) → [`00887204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887204.md) FUN_00887204

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`0045581c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/0045581c.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00764f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0044fc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044fc40.md) [`00455b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00455/00455b3c.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00765314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765314.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.30% / 新版 84.30%

CFGの説明率　旧版 60.00% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088625c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088625c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886260"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088625c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00886260",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00886264",
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
      "00887208",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0088720c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00887210",
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

- 旧版 [`0088625c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886258.md#insn-0088625c) · [`00886260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886258.md#insn-00886260) · [`00886264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886258.md#insn-00886264)

~~~diff
- 0088625c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0088625c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0088625c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 0088625c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088625c bytes fd7b09a9
- 00886260 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00886260 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00886260 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00886260 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00886260 bytes f6570aa9
- 00886264 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00886264 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00886264 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00886264 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00886264 bytes f44f0ba9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9738228c7977f9d03625ec08fb0d1024"></a>

### [`00886750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886750.md) → [`008876fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/008876fc.md) FUN_008876fc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 43.33% / 新版 48.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00886878"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00887824"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008877c0",
      "incomplete_value": true,
      "site": "008877c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:c:8"
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
      "008877b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0088686c"
      ]
    ],
    [
      "unmatched:00886870",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00886878",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00887890"
      ]
    ]
  ],
  "added": [
    [
      "008877b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00887818"
      ]
    ],
    [
      "0088781c",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00887824",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00887890"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886750.md#insn-00886818) · [`00886830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886750.md#insn-00886830) · [`00886868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886750.md#insn-00886868)
- 新版 [`008877c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/008876fc.md#insn-008877c4) · [`008877dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/008876fc.md#insn-008877dc)

~~~diff
- 00886818 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886818 ["INT_ADD", "register:40f0:8", ["const:886818:8", "const:4:8"]]
- 00886818 ["CALLIND", null, ["register:0:8"]]
+ 008877c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008877c4 ["INT_ADD", "register:40f0:8", ["const:8877c4:8", "const:4:8"]]
+ 008877c4 ["CALLIND", null, ["register:0:8"]]
- 00886818 bytes 00013fd6
+ 008877c4 bytes 00013fd6
- 00886830 ["INT_ADD", "register:40f0:8", ["const:886830:8", "const:4:8"]]
- 00886830 ["CALL", null, ["callee:00c58f50:8"]]
+ 008877dc ["INT_ADD", "register:40f0:8", ["const:8877dc:8", "const:4:8"]]
+ 008877dc ["CALL", null, ["callee:00c58f50:8"]]
- 00886830 bytes d4450f94
+ 008877dc bytes dd450f94
- 00886868 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00886868 ["RETURN", null, ["register:0:8"]]
- 00886868 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fefb9e34ce3491e8468ab881818607b"></a>

### [`0088696c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/0088696c.md) → [`00887918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887918.md) FUN_00887918

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00887930",
      "incomplete_value": false,
      "site": "00887934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886984",
      "incomplete_value": false,
      "site": "00886988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "00887934",
      "DATA",
      [
        "storage",
        "00c81008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00887934",
      "DATA",
      [
        "storage",
        "00c81fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/0088696c.md#insn-00886984) · [`00886998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/0088696c.md#insn-00886998) · [`008869ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/0088696c.md#insn-008869ac)
- 新版 [`00887930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887918.md#insn-00887930) · [`00887944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887918.md#insn-00887944) · [`00887958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887918.md#insn-00887958)

~~~diff
- 00886984 ["COPY", "tmp:0:8", ["const:8:8"]]
- 00886984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00886984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00886984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00887930 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 00887930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00887930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00887930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00886984 bytes 08210091
+ 00887930 bytes 08613f91
- 00886998 ["INT_ADD", "register:40f0:8", ["const:886998:8", "const:4:8"]]
- 00886998 ["CALL", null, ["callee:00c54d90:8"]]
+ 00887944 ["INT_ADD", "register:40f0:8", ["const:887944:8", "const:4:8"]]
+ 00887944 ["CALL", null, ["callee:00c54d90:8"]]
- 00886998 bytes 02350f94
+ 00887944 bytes 13350f94
- 008869ac ["COPY", "register:0:8", ["register:4040:8"]]
- 008869ac ["INT_ADD", "register:40f0:8", ["const:8869ac:8", "const:4:8"]]
- 008869ac ["CALLIND", null, ["register:0:8"]]
+ 00887958 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00887958 ["INT_ADD", "register:40f0:8", ["const:887958:8", "const:4:8"]]
+ 00887958 ["CALLIND", null, ["register:0:8"]]
- 008869ac bytes 00013fd6
+ 00887958 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62ad3d7ddf92657f60a2318b45132c8b"></a>

### [`00886afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886afc.md) → [`00887aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887aa8.md) FUN_00887aa8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00456848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456848.md) [`004647dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/004647dc.md) [`00886f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f68.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0044fc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044fc40.md) [`00456b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00456/00456b68.md) [`00464afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00464/00464afc.md) [`00887f14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887f14.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.14% / 新版 80.14%

CFGの説明率　旧版 45.00% / 新版 62.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886b70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886b78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886b80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00886b70",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ],
    [
      "unmatched:00886b78",
      "WRITE",
      [
        "storage",
        "Stack[-0x108]",
        null,
        null
      ]
    ],
    [
      "unmatched:00886b80",
      "WRITE",
      [
        "storage",
        "Stack[-0xf8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00887b1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ],
    [
      "00887b24",
      "WRITE",
      [
        "storage",
        "Stack[-0x108]",
        null,
        null
      ]
    ],
    [
      "00887b2c",
      "WRITE",
      [
        "storage",
        "Stack[-0xf8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886afc.md#insn-00886b70) · [`00886b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886afc.md#insn-00886b78) · [`00886b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886afc.md#insn-00886b80)

~~~diff
- 00886b70 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:80:8"]]
- 00886b70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00886b70 bytes e84300f9
- 00886b78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 00886b78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00886b78 bytes 0081843c
- 00886b80 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:98:8"]]
- 00886b80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00886b80 bytes e94f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ef8f3881ebca35f7abdc5c8b51a2419"></a>

### [`00886e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e38.md) → [`00887de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887de4.md) FUN_00887de4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00887dec",
      "incomplete_value": false,
      "site": "00887df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886e40",
      "incomplete_value": false,
      "site": "00886e44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "00887df0",
      "DATA",
      [
        "storage",
        "00c81078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00887df0",
      "DATA",
      [
        "storage",
        "00c82048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e38.md#insn-00886e3c) · [`00886e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e38.md#insn-00886e40)
- 新版 [`00887de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887de4.md#insn-00887de8) · [`00887dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887de4.md#insn-00887dec)

~~~diff
- 00886e3c ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 00887de8 ["COPY", "register:4048:8", ["const:c82000:8"]]
- 00886e3c bytes c91f00f0
+ 00887de8 bytes c91f00f0
- 00886e40 ["COPY", "tmp:0:8", ["const:78:8"]]
- 00886e40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00886e40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00886e40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00887dec ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00887dec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00887dec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00887dec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00886e40 bytes 29e10191
+ 00887dec bytes 29210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1350c1d3e5601775af3b8efbcc421a7"></a>

### [`00886e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e58.md) → [`00887e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887e04.md) FUN_00887e04

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00887e0c",
      "incomplete_value": false,
      "site": "00887e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886e60",
      "incomplete_value": false,
      "site": "00886e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "00887e10",
      "DATA",
      [
        "storage",
        "00c81078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00887e10",
      "DATA",
      [
        "storage",
        "00c82048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e58.md#insn-00886e5c) · [`00886e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e58.md#insn-00886e60) · [`00886e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e58.md#insn-00886e84)
- 新版 [`00887e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887e04.md#insn-00887e08) · [`00887e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887e04.md#insn-00887e0c) · [`00887e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887e04.md#insn-00887e30)

~~~diff
- 00886e5c ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 00887e08 ["COPY", "register:4048:8", ["const:c82000:8"]]
- 00886e5c bytes c91f00f0
+ 00887e08 bytes c91f00f0
- 00886e60 ["COPY", "tmp:0:8", ["const:78:8"]]
- 00886e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00886e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00886e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00887e0c ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00887e0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00887e0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00887e0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00886e60 bytes 29e10191
+ 00887e0c bytes 29210191
- 00886e84 ["INT_ADD", "register:40f0:8", ["const:886e84:8", "const:4:8"]]
- 00886e84 ["CALL", null, ["callee:00c58f50:8"]]
+ 00887e30 ["INT_ADD", "register:40f0:8", ["const:887e30:8", "const:4:8"]]
+ 00887e30 ["CALL", null, ["callee:00c58f50:8"]]
- 00886e84 bytes 3f440f94
+ 00887e30 bytes 48440f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0da997e32cc4a8d9e9205af3acc9a505"></a>

### [`00886f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f14.md) → [`00887ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887ec0.md) FUN_00887ec0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

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
      "definition_site": "00887ecc",
      "incomplete_value": false,
      "site": "00887ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886f20",
      "incomplete_value": false,
      "site": "00886f20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "00887ecc",
      "DATA",
      [
        "storage",
        "00c81078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00887ecc",
      "DATA",
      [
        "storage",
        "00c82048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f14.md#insn-00886f18) · [`00886f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f14.md#insn-00886f1c)
- 新版 [`00887ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887ec0.md#insn-00887ec4) · [`00887ec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887ec0.md#insn-00887ec8)

~~~diff
- 00886f18 ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 00887ec4 ["COPY", "register:4048:8", ["const:c82000:8"]]
- 00886f18 bytes c91f00f0
+ 00887ec4 bytes c91f00f0
- 00886f1c ["COPY", "tmp:0:8", ["const:78:8"]]
- 00886f1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00886f1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00886f1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00887ec8 ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00887ec8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00887ec8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00887ec8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00886f1c bytes 29e10191
+ 00887ec8 bytes 29210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e42de846f6531eb618e0f51a046a424"></a>

### [`00886f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f68.md) → [`00887f14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887f14.md) FUN_00887f14

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00886afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886afc.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00887aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887aa8.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00886f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f68.md#insn-00886f6c) · [`00886f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f68.md#insn-00886f88)
- 新版 [`00887f18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887f14.md#insn-00887f18) · [`00887f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887f14.md#insn-00887f34)

~~~diff
- 00886f6c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00886f6c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00886f6c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00886f6c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00887f18 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00887f18 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00887f18 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00887f18 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00886f6c bytes 68010036
+ 00887f18 bytes 68010036
- 00886f88 ["INT_ADD", "register:40f0:8", ["const:886f88:8", "const:4:8"]]
- 00886f88 ["CALL", null, ["callee:00c58f50:8"]]
+ 00887f34 ["INT_ADD", "register:40f0:8", ["const:887f34:8", "const:4:8"]]
+ 00887f34 ["CALL", null, ["callee:00c58f50:8"]]
- 00886f88 bytes fe430f94
+ 00887f34 bytes 07440f94
~~~


<a id="compare-b5361e80bcd3969bbc5256a4689e957a"></a>

### [`00886f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f9c.md) → [`00887f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887f48.md) FUN_00887f48

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00457440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/00457440.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md) [`00764f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md) [`00767dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767dfc.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044fc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044fc40.md) [`00457760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00457/00457760.md) [`007647b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/007647b8.md) [`00765314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765314.md) [`007681d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007681d8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.78% / 新版 83.78%

CFGの説明率　旧版 37.50% / 新版 47.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886fbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00887f68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00887080"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00886fbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00886fd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ],
    [
      "unmatched:00886fdc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ]
  ],
  "added": [
    [
      "00887f68",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00887f84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007647b8"
      ]
    ],
    [
      "00887f88",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f9c.md#insn-00886fbc) · [`00886fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f9c.md#insn-00886fd8) · [`00886fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f9c.md#insn-00886fdc)

~~~diff
- 00886fbc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00886fbc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00886fbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00886fbc bytes a8831ff8
- 00886fd8 ["INT_ADD", "register:40f0:8", ["const:886fd8:8", "const:4:8"]]
- 00886fd8 ["CALL", null, ["ram:7643dc:8"]]
- 00886fd8 bytes 0175fb97
- 00886fdc ["INT_ADD", "register:40f0:8", ["const:886fdc:8", "const:4:8"]]
- 00886fdc ["CALL", null, ["callee:008524fc:8"]]
- 00886fdc bytes 5d29ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4faa817d57c51c4b774e964df7e20c88"></a>

### [`00887140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887140.md) → [`008880ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008880ec.md) _INIT_164

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 52.54% / 新版 52.54%

CFGの説明率　旧版 63.16% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_store_alignment` 39件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00887170"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00887184"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00887188"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00887170",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088717c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00887184",
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
      "0088811c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00888128",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00888130",
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

- 旧版 [`00887170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887140.md#insn-00887170) · [`00887184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887140.md#insn-00887184) · [`00887188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887140.md#insn-00887188)

~~~diff
- 00887170 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00887170 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00887170 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00887170 bytes a9831ff8
- 00887184 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00887184 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00887184 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00887184 bytes ea130278
- 00887188 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00887188 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00887188 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5354943e766e401d7183aa8b2d5166fb"></a>

### [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) → [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) FUN_0088847c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 10件 [`0088a828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a828.md) [`0088adc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088adc0.md) [`0088aee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aee4.md) [`0088b008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b008.md) [`0088b12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b12c.md) · 呼出先 12件 [`00888e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e88.md) [`00888e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e8c.md) [`00888ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888ed4.md) [`00889088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889088.md) [`0088908c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/0088908c.md)
- 新版 呼出元 10件 [`0088b7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b7d4.md) [`0088bd6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088bd6c.md) [`0088be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088be90.md) [`0088bfb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088bfb4.md) [`0088c0d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c0d8.md) · 呼出先 12件 [`00889e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889e34.md) [`00889e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889e38.md) [`00889e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889e80.md) [`0088a034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a034.md) [`0088a038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a038.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.09% / 新版 89.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008884b0",
      "incomplete_value": false,
      "site": "008884b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00887504",
      "incomplete_value": false,
      "site": "00887508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008884ec",
      "incomplete_value": false,
      "site": "008884ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00887540",
      "incomplete_value": false,
      "site": "00887540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088853c",
      "incomplete_value": false,
      "site": "0088853c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00887590",
      "incomplete_value": false,
      "site": "00887590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008884b4",
      "DATA",
      [
        "storage",
        "00c81108",
        null,
        "pointer"
      ]
    ],
    [
      "008884ec",
      "DATA",
      [
        "storage",
        "00c812c0",
        null,
        "undefined *"
      ]
    ],
    [
      "008884f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00888ed4"
      ]
    ]
  ],
  "added": [
    [
      "008884b4",
      "DATA",
      [
        "storage",
        "00c820d8",
        null,
        "pointer"
      ]
    ],
    [
      "008884ec",
      "DATA",
      [
        "storage",
        "00c82290",
        null,
        "undefined *"
      ]
    ],
    [
      "008884f8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00889e80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088754c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md#insn-0088754c) · [`00887500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md#insn-00887500) · [`00887504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md#insn-00887504)
- 新版 [`008884f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md#insn-008884f8) · [`008884ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md#insn-008884ac) · [`008884b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md#insn-008884b0)

~~~diff
- 0088754c ["INT_ADD", "register:40f0:8", ["const:88754c:8", "const:4:8"]]
- 0088754c ["CALL", null, ["ram:888ed4:8"]]
+ 008884f8 ["INT_ADD", "register:40f0:8", ["const:8884f8:8", "const:4:8"]]
+ 008884f8 ["CALL", null, ["callee:00889e80:8"]]
- 0088754c bytes 62060094
+ 008884f8 bytes 62060094
- 00887500 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008884ac ["COPY", "register:4040:8", ["const:c82000:8"]]
- 00887500 bytes c81f00d0
+ 008884ac bytes c81f00d0
- 00887504 ["COPY", "tmp:0:8", ["const:108:8"]]
- 00887504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00887504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00887504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008884b0 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 008884b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008884b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008884b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00887504 bytes 08210491
+ 008884b0 bytes 08610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f14baf20ba4b706670282b1d74ef434"></a>

### [`00887748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887748.md) → [`008886f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008886f4.md) FUN_008886f4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00852508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852508.md) · 呼出先 0件 

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
      "definition_site": "00888708",
      "incomplete_value": false,
      "site": "0088870c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088775c",
      "incomplete_value": false,
      "site": "00887760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:862:8"
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
      "0088870c",
      "DATA",
      [
        "storage",
        "002ba862",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0088870c",
      "DATA",
      [
        "storage",
        "002ba940",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088775c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887748.md#insn-0088775c)
- 新版 [`00888708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008886f4.md#insn-00888708)

~~~diff
- 0088775c ["COPY", "tmp:0:8", ["const:862:8"]]
- 0088775c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088775c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088775c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00888708 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00888708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00888708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00888708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088775c bytes 08892191
+ 00888708 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10459ae272f24521ddfe53a80b3cdc26"></a>

### [`00887838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887838.md) → [`008887e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008887e4.md) FUN_008887e4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00a9ae48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a9a/00a9ae48.md) · 呼出先 4件 [`00889bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bf4.md) [`00889bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bf8.md) [`00b37478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37478.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00a9be3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a9b/00a9be3c.md) · 呼出先 4件 [`0088aba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088aba0.md) [`0088aba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088aba4.md) [`00b3846c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b38/00b3846c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00888818",
      "incomplete_value": false,
      "site": "00888818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088786c",
      "incomplete_value": false,
      "site": "0088786c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
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
      "00888818",
      "DATA",
      [
        "storage",
        "00c814e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00888858",
      "READ",
      [
        "storage",
        "00c81500",
        null,
        "pointer"
      ]
    ],
    [
      "00888858",
      "READ",
      [
        "storage",
        "00c81508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00888818",
      "DATA",
      [
        "storage",
        "00c824b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00888858",
      "READ",
      [
        "storage",
        "00c824d0",
        null,
        "pointer"
      ]
    ],
    [
      "00888858",
      "READ",
      [
        "storage",
        "00c824d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00887860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887838.md#insn-00887860) · [`00887864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887838.md#insn-00887864) · [`00887884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887838.md#insn-00887884)
- 新版 [`0088880c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008887e4.md#insn-0088880c) · [`00888810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008887e4.md#insn-00888810) · [`00888830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008887e4.md#insn-00888830)

~~~diff
- 00887860 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088880c ["COPY", "register:4040:8", ["const:c82000:8"]]
- 00887860 bytes c81f00d0
+ 0088880c bytes c81f00d0
- 00887864 ["COPY", "tmp:0:8", ["const:4e0:8"]]
- 00887864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00887864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00887864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00888810 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 00888810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00888810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00888810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00887864 bytes 08811391
+ 00888810 bytes 08c11291
- 00887884 ["INT_ADD", "register:40f0:8", ["const:887884:8", "const:4:8"]]
- 00887884 ["CALL", null, ["callee:00b3846c:8"]]
+ 00888830 ["INT_ADD", "register:40f0:8", ["const:888830:8", "const:4:8"]]
+ 00888830 ["CALL", null, ["callee:00b3846c:8"]]
- 00887884 bytes fdbe0a94
+ 00888830 bytes 0fbf0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c19d165d2e1c577318be73bca21be692"></a>

### [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) → [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) FUN_008888dc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`006b3864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3864.md) [`0073c990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073c/0073c990.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 24件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0087eb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb18.md) [`00888084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888084.md)
- 新版 呼出元 7件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`00605644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00605/00605644.md) [`006b3c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3c14.md) [`0073cd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073c/0073cd40.md) [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) · 呼出先 24件 [`0043ecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md) [`00597dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597dec.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`0087fac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fac4.md) [`00889030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889030.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.45% / 新版 90.45%

CFGの説明率　旧版 81.40% / 新版 73.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00887c28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00887c2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00887d20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00888a2c",
      "READ",
      [
        "storage",
        "00c9b750",
        null,
        "pointer"
      ]
    ],
    [
      "00888a2c",
      "PARAM",
      [
        "storage",
        "011237a0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00887c28",
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
      "00888a2c",
      "READ",
      [
        "storage",
        "00c9c720",
        null,
        "pointer"
      ]
    ],
    [
      "00888a2c",
      "PARAM",
      [
        "storage",
        "01124760",
        null,
        "undefined1"
      ]
    ],
    [
      "00888bd4",
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

- 旧版 [`00887a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md#insn-00887a88) · [`00887c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md#insn-00887c28) · [`00887c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md#insn-00887c2c)
- 新版 [`00888a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md#insn-00888a34)

~~~diff
- 00887a88 ["INT_ADD", "register:40f0:8", ["const:887a88:8", "const:4:8"]]
- 00887a88 ["CALL", null, ["callee:0087fac4:8"]]
+ 00888a34 ["INT_ADD", "register:40f0:8", ["const:888a34:8", "const:4:8"]]
+ 00888a34 ["CALL", null, ["callee:0087fac4:8"]]
- 00887a88 bytes 24dcff97
+ 00888a34 bytes 24dcff97
- 00887c28 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00887c28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00887c28 bytes e82300b9
- 00887c2c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00887c2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00887c2c bytes e083823c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-735aa897f68519981008e6ee0b02fbb3"></a>

### [`00888174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888174.md) → [`00889120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889120.md) FUN_00889120

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0088818c",
      "incomplete_value": false,
      "site": "00888190",
      "value": [
        "leaf",
        "const:ffffffffffffffff:8"
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
      "definition_site": "00888188",
      "incomplete_value": true,
      "site": "00888190",
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


#### 変更候補の命令位置

- 旧版 [`00888190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888174.md#insn-00888190) · [`00888184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888174.md#insn-00888184) · [`00888194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888174.md#insn-00888194)
- 新版 [`0088913c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889120.md#insn-0088913c) · [`00889130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889120.md#insn-00889130) · [`00889140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889120.md#insn-00889140)

~~~diff
- 00888190 ["INT_ADD", "register:40f0:8", ["const:888190:8", "const:4:8"]]
- 00888190 ["CALL", null, ["callee:00c54d90:8"]]
+ 0088913c ["INT_ADD", "register:40f0:8", ["const:88913c:8", "const:4:8"]]
+ 0088913c ["CALL", null, ["callee:00c54d90:8"]]
- 00888190 bytes 042f0f94
+ 0088913c bytes 152f0f94
- 00888184 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00888184 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00889130 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00889130 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00888184 bytes b30000b4
+ 00889130 bytes b30000b4
- 00888194 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00888194 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00889140 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00889140 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00888194 bytes 800000b4
+ 00889140 bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1c8e2f3dae7b7a5d0fee30f9460bf4d"></a>

### [`00888480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888480.md) → [`0088942c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/0088942c.md) FUN_0088942c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0061675c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/0061675c.md) [`006262ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00626/006262ac.md) [`006ff370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff370.md) [`00741464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/00741464.md) [`007fd3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd3d4.md) · 呼出先 11件 [`0058f474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f474.md) [`0088b990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b990.md) [`0088b994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b994.md) [`0088baa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088baa0.md) [`0088baa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088baa4.md)
- 新版 呼出元 6件 [`00616b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00616/00616b0c.md) [`0062665c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00626/0062665c.md) [`006ff720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff720.md) [`00741814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/00741814.md) [`007fe338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007fe/007fe338.md) · 呼出先 11件 [`0058f794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f794.md) [`0088c93c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c93c.md) [`0088c940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c940.md) [`0088ca4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088ca4c.md) [`0088ca50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088ca50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.43% / 新版 95.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088958c",
      "incomplete_value": false,
      "site": "0088958c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008885e0",
      "incomplete_value": false,
      "site": "008885e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:910:8"
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
      "definition_site": "008895b0",
      "incomplete_value": false,
      "site": "008895b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888604",
      "incomplete_value": false,
      "site": "00888604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008895c8",
      "incomplete_value": false,
      "site": "008895c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088861c",
      "incomplete_value": false,
      "site": "0088861c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "0088958c",
      "DATA",
      [
        "storage",
        "00c81910",
        null,
        "undefined *"
      ]
    ],
    [
      "008895b0",
      "DATA",
      [
        "storage",
        "00c81990",
        null,
        "undefined *"
      ]
    ],
    [
      "008895c8",
      "DATA",
      [
        "storage",
        "00c81a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088958c",
      "DATA",
      [
        "storage",
        "00c828e0",
        null,
        "undefined *"
      ]
    ],
    [
      "008895b0",
      "DATA",
      [
        "storage",
        "00c82960",
        null,
        "undefined *"
      ]
    ],
    [
      "008895c8",
      "DATA",
      [
        "storage",
        "00c829e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888480.md#insn-00888568) · [`00888594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888480.md#insn-00888594) · [`008885a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888480.md#insn-008885a4)
- 新版 [`00889514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/0088942c.md#insn-00889514) · [`00889540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/0088942c.md#insn-00889540) · [`00889550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/0088942c.md#insn-00889550)

~~~diff
- 00888568 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888568 ["INT_ADD", "register:40f0:8", ["const:888568:8", "const:4:8"]]
- 00888568 ["CALLIND", null, ["register:0:8"]]
+ 00889514 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00889514 ["INT_ADD", "register:40f0:8", ["const:889514:8", "const:4:8"]]
+ 00889514 ["CALLIND", null, ["register:0:8"]]
- 00888568 bytes 00013fd6
+ 00889514 bytes 00013fd6
- 00888594 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888594 ["INT_ADD", "register:40f0:8", ["const:888594:8", "const:4:8"]]
- 00888594 ["CALLIND", null, ["register:0:8"]]
+ 00889540 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00889540 ["INT_ADD", "register:40f0:8", ["const:889540:8", "const:4:8"]]
+ 00889540 ["CALLIND", null, ["register:0:8"]]
- 00888594 bytes 00013fd6
+ 00889540 bytes 00013fd6
- 008885a4 ["INT_ADD", "register:40f0:8", ["const:8885a4:8", "const:4:8"]]
- 008885a4 ["CALL", null, ["callee:0058f794:8"]]
+ 00889550 ["INT_ADD", "register:40f0:8", ["const:889550:8", "const:4:8"]]
+ 00889550 ["CALL", null, ["callee:0058f794:8"]]
- 008885a4 bytes b41bf497
+ 00889550 bytes 9118f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e54c2e87602893bcc445bab7bbedbb9"></a>

### [`008888ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008888ac.md) → [`00889858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889858.md) FUN_00889858

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007fd648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd648.md) · 呼出先 4件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md)
- 新版 呼出元 1件 [`007fe5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007fe/007fe5ac.md) · 呼出先 4件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c596b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 71.74% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00888928"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008898d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00889938",
      "incomplete_value": false,
      "site": "00889948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088898c",
      "incomplete_value": false,
      "site": "0088899c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "unmatched:00888928",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088999c"
      ]
    ],
    [
      "00889938",
      "PARAM",
      [
        "storage",
        "00c811f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00889940",
      "PARAM",
      [
        "storage",
        "00c81208",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008898d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088999c"
      ]
    ],
    [
      "00889938",
      "PARAM",
      [
        "storage",
        "00c821c8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00889940",
      "PARAM",
      [
        "storage",
        "00c821d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008888ac.md#insn-00888928) · [`0088899c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008888ac.md#insn-0088899c)
- 新版 [`00889948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889858.md#insn-00889948) · [`008898d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889858.md#insn-008898d4)

~~~diff
- 00888928 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00888928 ["CBRANCH", null, ["local:b30:8", "tmp:0:1"]]
- 00888928 bytes 530600b4
- 0088899c ["INT_ADD", "register:40f0:8", ["const:88899c:8", "const:4:8"]]
- 0088899c ["CALL", null, ["callee:00c596b0:8"]]
+ 00889948 ["INT_ADD", "register:40f0:8", ["const:889948:8", "const:4:8"]]
+ 00889948 ["CALL", null, ["callee:00c596b0:8"]]
- 0088899c bytes 513f0f94
+ 00889948 bytes 5a3f0f94
+ 008898d4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 008898d4 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
+ 008898d4 bytes 530600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9db8964b8461c9923225eaf5730b488"></a>

### [`00888a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888a08.md) → [`008899b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/008899b4.md) FUN_008899b4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006ff698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff698.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 5件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md)
- 新版 呼出元 2件 [`006ffa48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ffa48.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) · 呼出先 5件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c596b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.24% / 新版 72.24%

CFGの説明率　旧版 52.76% / 新版 51.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 6件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00888c94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00888c94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00888d78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00889adc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00888b3c"
      ]
    ],
    [
      "unmatched:00888b38",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00888b4c"
      ]
    ],
    [
      "unmatched:00888b40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00888b4c"
      ]
    ]
  ],
  "added": [
    [
      "00889adc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00889ae8"
      ]
    ],
    [
      "00889ae4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00889af8"
      ]
    ],
    [
      "00889aec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00889af8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888a08.md#insn-00888b40) · [`00888b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888a08.md#insn-00888b44) · [`00888b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888a08.md#insn-00888b50)

~~~diff
- 00888b40 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00888b40 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 00888b40 bytes 63000054
- 00888b44 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00888b44 ["INT_EQUAL", "tmp:1:1", ["register:4040:8", "const:0:8"]]
- 00888b44 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00888b44 ["INT_DIV", "tmp:0:8", ["register:4060:8", "register:4040:8"]]
- 00888b44 bytes 8d09c89a
- 00888b50 ["CBRANCH", null, ["local:b18:8", "register:101:1"]]
- 00888b50 bytes 40feff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1adb57fe2b279f23a56036e878478e48"></a>

### [`00888e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e40.md) → [`00889dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889dec.md) FUN_00889dec

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00889e10",
      "incomplete_value": false,
      "site": "00889e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888e64",
      "incomplete_value": false,
      "site": "00888e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "00889e10",
      "DATA",
      [
        "storage",
        "00c812c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889e10",
      "DATA",
      [
        "storage",
        "00c82290",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e40.md#insn-00888e54) · [`00888e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e40.md#insn-00888e5c) · [`00888e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e40.md#insn-00888e60)
- 新版 [`00889e00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889dec.md#insn-00889e00) · [`00889e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889dec.md#insn-00889e08) · [`00889e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889dec.md#insn-00889e0c)

~~~diff
- 00888e54 ["INT_ADD", "register:40f0:8", ["const:888e54:8", "const:4:8"]]
- 00888e54 ["CALL", null, ["callee:00c58f30:8"]]
+ 00889e00 ["INT_ADD", "register:40f0:8", ["const:889e00:8", "const:4:8"]]
+ 00889e00 ["CALL", null, ["callee:00c58f30:8"]]
- 00888e54 bytes 433c0f94
+ 00889e00 bytes 4c3c0f94
- 00888e5c ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00889e08 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 00888e5c bytes c81f00b0
+ 00889e08 bytes c81f00b0
- 00888e60 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 00888e60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00888e60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00888e60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00889e0c ["COPY", "tmp:0:8", ["const:290:8"]]
+ 00889e0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00889e0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00889e0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00888e60 bytes 08010b91
+ 00889e0c bytes 08410a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

