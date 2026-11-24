# v16.0.1 → v16.0.2 · 命令位置の検査未完了 (6)

[一覧の目次](README.md)

<a id="compare-8be75a26b73c6be0deaad89af06de419"></a>

### [`00af5324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5324.md) → [`00af53c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af53c0.md) FUN_00af53c0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5324"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5324"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5328"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5324",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5328",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af532c",
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
      "00af53c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af53c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af53c8",
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

- 旧版 [`00af5324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5324.md#insn-00af5324) · [`00af5328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5324.md#insn-00af5328) · [`00af532c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5324.md#insn-00af532c)

~~~diff
- 00af5324 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af5324 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af5324 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af5324 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5324 bytes fd7bbda9
- 00af5328 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af5328 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af5328 bytes f50b00f9
- 00af532c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af532c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af532c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af532c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af532c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c157f7f3733bac132bd3b9cfc64459b"></a>

### [`00af5378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5378.md) → [`00af5414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af5414.md) FUN_00af5414

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

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
      "site": "00af5378"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5378"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af537c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5378",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af537c",
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
      "00af5414",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af5418",
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

- 旧版 [`00af5378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5378.md#insn-00af5378) · [`00af537c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5378.md#insn-00af537c)
- 新版 [`00af5414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af5414.md#insn-00af5414)

~~~diff
- 00af5378 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af5378 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af5378 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af5378 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5378 bytes fd7bbea9
- 00af537c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af537c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af537c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af537c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af537c bytes f44f01a9
+ 00af5414 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00af5414 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00af5414 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00af5414 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00af5414 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ab242836eb45dfc013d49a672e78fba"></a>

### [`00af58a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af58a4.md) → [`00af5940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af5940.md) FUN_00af5940

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00a52034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a52/00a52034.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af58dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af5978"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af58dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af58a4.md#insn-00af58dc) · [`00af58c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af58a4.md#insn-00af58c0)
- 新版 [`00af5978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af5940.md#insn-00af5978) · [`00af595c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af5940.md#insn-00af595c)

~~~diff
- 00af58dc ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00af58dc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af58dc ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af58dc ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af58dc bytes 136929b8
+ 00af5978 ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00af5978 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af5978 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af5978 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af5978 bytes 136929b8
- 00af58c0 ["INT_ADD", "register:40f0:8", ["const:af58c0:8", "const:4:8"]]
- 00af58c0 ["CALL", null, ["callee:00851550:8"]]
+ 00af595c ["INT_ADD", "register:40f0:8", ["const:af595c:8", "const:4:8"]]
+ 00af595c ["CALL", null, ["callee:00851550:8"]]
- 00af58c0 bytes 0e6ff597
+ 00af595c bytes fd6ef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad58b3177343d1249ba0ca6eb80a464f"></a>

### [`00af58f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af58f0.md) → [`00af598c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af598c.md) FUN_00af598c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00713358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) [`0071425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`007133b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/007133b0.md) [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) [`007142b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/007142b4.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 76.00% / 新版 76.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5928",
      "DATA",
      [
        "storage",
        "0030a380",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af59c4",
      "DATA",
      [
        "storage",
        "0030a3c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af590c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af58f0.md#insn-00af590c) · [`00af5924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af58f0.md#insn-00af5924) · [`00af5928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af58f0.md#insn-00af5928)
- 新版 [`00af59a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af598c.md#insn-00af59a8)

~~~diff
- 00af590c ["INT_ADD", "register:40f0:8", ["const:af590c:8", "const:4:8"]]
- 00af590c ["CALL", null, ["callee:00851550:8"]]
+ 00af59a8 ["INT_ADD", "register:40f0:8", ["const:af59a8:8", "const:4:8"]]
+ 00af59a8 ["CALL", null, ["callee:00851550:8"]]
- 00af590c bytes fb6ef597
+ 00af59a8 bytes ea6ef597
- 00af5924 ["COPY", "tmp:0:8", ["const:380:8"]]
- 00af5924 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00af5924 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00af5924 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00af5924 bytes 29010e91
- 00af5928 ["INT_SEXT", "tmp:0:8", ["register:4098:4"]]
- 00af5928 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00af5928 ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:2:8"]]
- 00af5928 ["INT_ADD", "tmp:2:8", ["register:4048:8", "tmp:1:8"]]
- 00af5928 bytes 29d9b3b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eef1447e3704bb1c16173d0f6163abe2"></a>

### [`00af59b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af59b4.md) → [`00af5a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af5a50.md) FUN_00af5a50

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af59b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af59b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af59b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af59b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af59b8",
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
      "00af5a50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af5a54",
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

- 旧版 [`00af59b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af59b4.md#insn-00af59b4) · [`00af59b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af59b4.md#insn-00af59b8)
- 新版 [`00af5a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af5a50.md#insn-00af5a50)

~~~diff
- 00af59b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af59b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af59b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af59b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af59b4 bytes fd7bbea9
- 00af59b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af59b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af59b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af59b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af59b8 bytes f44f01a9
+ 00af5a50 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00af5a50 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00af5a50 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00af5a50 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00af5a50 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dc792e1b91e3b42e4d62630d0c8cd5a"></a>

### [`00af5a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a40.md) → [`00af5adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af5adc.md) FUN_00af5adc

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5a80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af5b1c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af5a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a40.md#insn-00af5a80) · [`00af5a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a40.md#insn-00af5a5c)
- 新版 [`00af5b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af5adc.md#insn-00af5b1c) · [`00af5af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af5adc.md#insn-00af5af8)

~~~diff
- 00af5a80 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00af5a80 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af5a80 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af5a80 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af5a80 bytes 0a6929b8
+ 00af5b1c ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 00af5b1c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af5b1c ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af5b1c ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af5b1c bytes 0a6929b8
- 00af5a5c ["INT_ADD", "register:40f0:8", ["const:af5a5c:8", "const:4:8"]]
- 00af5a5c ["CALL", null, ["callee:00851550:8"]]
+ 00af5af8 ["INT_ADD", "register:40f0:8", ["const:af5af8:8", "const:4:8"]]
+ 00af5af8 ["CALL", null, ["callee:00851550:8"]]
- 00af5a5c bytes a76ef597
+ 00af5af8 bytes 966ef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2fb62073f91931e401e91ea91f98162"></a>

### [`00af6420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6420.md) → [`00af64bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af64bc.md) FUN_00af64bc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007100d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 4件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00710128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710128.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af6434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6420.md#insn-00af6434) · [`00af6448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6420.md#insn-00af6448) · [`00af644c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6420.md#insn-00af644c)
- 新版 [`00af64d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af64bc.md#insn-00af64d0) · [`00af64e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af64bc.md#insn-00af64e4) · [`00af64e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af64bc.md#insn-00af64e8)

~~~diff
- 00af6434 ["INT_ADD", "register:40f0:8", ["const:af6434:8", "const:4:8"]]
- 00af6434 ["CALL", null, ["callee:00851550:8"]]
+ 00af64d0 ["INT_ADD", "register:40f0:8", ["const:af64d0:8", "const:4:8"]]
+ 00af64d0 ["CALL", null, ["callee:00851550:8"]]
- 00af6434 bytes 316cf597
+ 00af64d0 bytes 206cf597
- 00af6448 ["INT_ADD", "register:40f0:8", ["const:af6448:8", "const:4:8"]]
- 00af6448 ["CALL", null, ["callee:005e7460:8"]]
+ 00af64e4 ["INT_ADD", "register:40f0:8", ["const:af64e4:8", "const:4:8"]]
+ 00af64e4 ["CALL", null, ["callee:005e7460:8"]]
- 00af6448 bytes f6c3eb97
+ 00af64e4 bytes dfc3eb97
- 00af644c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00af644c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00af644c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00af644c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00af64e8 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00af64e8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00af64e8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00af64e8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00af644c bytes a0010037
+ 00af64e8 bytes a0010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c953fd67f7d96d383d65af4a86a3afc"></a>

### [`00af6490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6490.md) → [`00af652c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af652c.md) FUN_00af652c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007100d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00710128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710128.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af64a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6490.md#insn-00af64a4) · [`00af64b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6490.md#insn-00af64b8) · [`00af64bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6490.md#insn-00af64bc)
- 新版 [`00af6540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af652c.md#insn-00af6540) · [`00af6554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af652c.md#insn-00af6554) · [`00af6558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af652c.md#insn-00af6558)

~~~diff
- 00af64a4 ["INT_ADD", "register:40f0:8", ["const:af64a4:8", "const:4:8"]]
- 00af64a4 ["CALL", null, ["callee:00851550:8"]]
+ 00af6540 ["INT_ADD", "register:40f0:8", ["const:af6540:8", "const:4:8"]]
+ 00af6540 ["CALL", null, ["callee:00851550:8"]]
- 00af64a4 bytes 156cf597
+ 00af6540 bytes 046cf597
- 00af64b8 ["INT_ADD", "register:40f0:8", ["const:af64b8:8", "const:4:8"]]
- 00af64b8 ["CALL", null, ["callee:005e7460:8"]]
+ 00af6554 ["INT_ADD", "register:40f0:8", ["const:af6554:8", "const:4:8"]]
+ 00af6554 ["CALL", null, ["callee:005e7460:8"]]
- 00af64b8 bytes dac3eb97
+ 00af6554 bytes c3c3eb97
- 00af64bc ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00af64bc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00af64bc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00af64bc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00af6558 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00af6558 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00af6558 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00af6558 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00af64bc bytes 60000037
+ 00af6558 bytes 60000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dfc0866c1859e4e4b9281a07ba878bd"></a>

### [`00af65e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af65e0.md) → [`00af667c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af667c.md) FUN_00af667c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007100d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 4件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00710128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710128.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af65e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af65e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af65e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af65e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af65e4",
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
      "00af667c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af6680",
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

- 旧版 [`00af65e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af65e0.md#insn-00af65e0) · [`00af65e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af65e0.md#insn-00af65e4)
- 新版 [`00af667c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af667c.md#insn-00af667c)

~~~diff
- 00af65e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af65e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af65e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af65e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af65e0 bytes fd7bbea9
- 00af65e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af65e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af65e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af65e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af65e4 bytes f44f01a9
+ 00af667c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00af667c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00af667c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00af667c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00af667c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b63393179e12ae5bc72ea34e507a6332"></a>

### [`00af6650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6650.md) → [`00af66ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af66ec.md) FUN_00af66ec

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007100d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00710128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710128.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af6664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6650.md#insn-00af6664) · [`00af6678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6650.md#insn-00af6678) · [`00af667c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6650.md#insn-00af667c)
- 新版 [`00af6700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af66ec.md#insn-00af6700) · [`00af6714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af66ec.md#insn-00af6714) · [`00af6718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af66ec.md#insn-00af6718)

~~~diff
- 00af6664 ["INT_ADD", "register:40f0:8", ["const:af6664:8", "const:4:8"]]
- 00af6664 ["CALL", null, ["callee:00851550:8"]]
+ 00af6700 ["INT_ADD", "register:40f0:8", ["const:af6700:8", "const:4:8"]]
+ 00af6700 ["CALL", null, ["callee:00851550:8"]]
- 00af6664 bytes a56bf597
+ 00af6700 bytes 946bf597
- 00af6678 ["INT_ADD", "register:40f0:8", ["const:af6678:8", "const:4:8"]]
- 00af6678 ["CALL", null, ["callee:005e7460:8"]]
+ 00af6714 ["INT_ADD", "register:40f0:8", ["const:af6714:8", "const:4:8"]]
+ 00af6714 ["CALL", null, ["callee:005e7460:8"]]
- 00af6678 bytes 6ac3eb97
+ 00af6714 bytes 53c3eb97
- 00af667c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00af667c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00af667c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00af667c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00af6718 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00af6718 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00af6718 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00af6718 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00af667c bytes 60000037
+ 00af6718 bytes 60000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1246be891528151b0075ae6d64f2a6ac"></a>

### [`00af6820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6820.md) → [`00af68bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af68bc.md) FUN_00af68bc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007100d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 4件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00710128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710128.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 6.67% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af6834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6820.md#insn-00af6834) · [`00af6848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6820.md#insn-00af6848) · [`00af684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6820.md#insn-00af684c)
- 新版 [`00af68d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af68bc.md#insn-00af68d0) · [`00af68e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af68bc.md#insn-00af68e4) · [`00af68e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af68bc.md#insn-00af68e8)

~~~diff
- 00af6834 ["INT_ADD", "register:40f0:8", ["const:af6834:8", "const:4:8"]]
- 00af6834 ["CALL", null, ["callee:00851550:8"]]
+ 00af68d0 ["INT_ADD", "register:40f0:8", ["const:af68d0:8", "const:4:8"]]
+ 00af68d0 ["CALL", null, ["callee:00851550:8"]]
- 00af6834 bytes 316bf597
+ 00af68d0 bytes 206bf597
- 00af6848 ["INT_ADD", "register:40f0:8", ["const:af6848:8", "const:4:8"]]
- 00af6848 ["CALL", null, ["callee:005e7460:8"]]
+ 00af68e4 ["INT_ADD", "register:40f0:8", ["const:af68e4:8", "const:4:8"]]
+ 00af68e4 ["CALL", null, ["callee:005e7460:8"]]
- 00af6848 bytes f6c2eb97
+ 00af68e4 bytes dfc2eb97
- 00af684c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00af684c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00af684c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00af684c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00af68e8 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00af68e8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00af68e8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00af68e8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00af684c bytes a0010037
+ 00af68e8 bytes a0010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa04cac73e2b0c7b98fc74518d5fc106"></a>

### [`00af6c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6c10.md) → [`00af6cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af6cac.md) FUN_00af6cac

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6c10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6c10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6c14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af6c10",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6c14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6c18",
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
      "00af6cac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af6cb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af6cb4",
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

- 旧版 [`00af6c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6c10.md#insn-00af6c10) · [`00af6c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6c10.md#insn-00af6c14) · [`00af6c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6c10.md#insn-00af6c18)

~~~diff
- 00af6c10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af6c10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af6c10 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af6c10 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af6c10 bytes fd7bbda9
- 00af6c14 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af6c14 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af6c14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af6c14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af6c14 bytes f65701a9
- 00af6c18 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af6c18 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af6c18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af6c18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af6c18 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6123f24b0c7ccac1a5221b1ad9f305d3"></a>

### [`00af6cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6cdc.md) → [`00af6d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af6d78.md) FUN_00af6d78

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6d14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af6db0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af6d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6cdc.md#insn-00af6d14) · [`00af6cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6cdc.md#insn-00af6cf8)
- 新版 [`00af6db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af6d78.md#insn-00af6db0) · [`00af6d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af6d78.md#insn-00af6d94)

~~~diff
- 00af6d14 ["COPY", "tmp:0:4", ["register:40a8:4"]]
- 00af6d14 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af6d14 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af6d14 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af6d14 bytes 156929b8
+ 00af6db0 ["COPY", "tmp:0:4", ["register:40a8:4"]]
+ 00af6db0 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af6db0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af6db0 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af6db0 bytes 156929b8
- 00af6cf8 ["INT_ADD", "register:40f0:8", ["const:af6cf8:8", "const:4:8"]]
- 00af6cf8 ["CALL", null, ["callee:00851550:8"]]
+ 00af6d94 ["INT_ADD", "register:40f0:8", ["const:af6d94:8", "const:4:8"]]
+ 00af6d94 ["CALL", null, ["callee:00851550:8"]]
- 00af6cf8 bytes 006af597
+ 00af6d94 bytes ef69f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb4241704ff567a9df17caeda6a0620c"></a>

### [`00af6d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6d28.md) → [`00af6dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af6dc4.md) FUN_00af6dc4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6d60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af6dfc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af6d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6d28.md#insn-00af6d60) · [`00af6d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6d28.md#insn-00af6d44)
- 新版 [`00af6dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af6dc4.md#insn-00af6dfc) · [`00af6de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af6dc4.md#insn-00af6de0)

~~~diff
- 00af6d60 ["COPY", "tmp:0:4", ["register:40a8:4"]]
- 00af6d60 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af6d60 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af6d60 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af6d60 bytes 156929b8
+ 00af6dfc ["COPY", "tmp:0:4", ["register:40a8:4"]]
+ 00af6dfc ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af6dfc ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af6dfc ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af6dfc bytes 156929b8
- 00af6d44 ["INT_ADD", "register:40f0:8", ["const:af6d44:8", "const:4:8"]]
- 00af6d44 ["CALL", null, ["callee:00851550:8"]]
+ 00af6de0 ["INT_ADD", "register:40f0:8", ["const:af6de0:8", "const:4:8"]]
+ 00af6de0 ["CALL", null, ["callee:00851550:8"]]
- 00af6d44 bytes ed69f597
+ 00af6de0 bytes dc69f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f2824823be4b7496991bf7274aae613"></a>

### [`00af6df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6df4.md) → [`00af6e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af6e90.md) FUN_00af6e90

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6e2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af6ec8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af6e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6df4.md#insn-00af6e2c) · [`00af6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6df4.md#insn-00af6e10)
- 新版 [`00af6ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af6e90.md#insn-00af6ec8) · [`00af6eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af6e90.md#insn-00af6eac)

~~~diff
- 00af6e2c ["COPY", "tmp:0:4", ["register:40a8:4"]]
- 00af6e2c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af6e2c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af6e2c ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af6e2c bytes 156929b8
+ 00af6ec8 ["COPY", "tmp:0:4", ["register:40a8:4"]]
+ 00af6ec8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af6ec8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af6ec8 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af6ec8 bytes 156929b8
- 00af6e10 ["INT_ADD", "register:40f0:8", ["const:af6e10:8", "const:4:8"]]
- 00af6e10 ["CALL", null, ["callee:00851550:8"]]
+ 00af6eac ["INT_ADD", "register:40f0:8", ["const:af6eac:8", "const:4:8"]]
+ 00af6eac ["CALL", null, ["callee:00851550:8"]]
- 00af6e10 bytes ba69f597
+ 00af6eac bytes a969f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f853efe559be24606ab49a8857b3d83a"></a>

### [`00af6ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6ed8.md) → [`00af6f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af6f74.md) FUN_00af6f74

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6ed8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6ed8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6edc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af6ed8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6edc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6ee0",
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
      "00af6f74",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af6f78",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af6f7c",
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

- 旧版 [`00af6ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6ed8.md#insn-00af6ed8) · [`00af6edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6ed8.md#insn-00af6edc) · [`00af6ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6ed8.md#insn-00af6ee0)

~~~diff
- 00af6ed8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af6ed8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af6ed8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af6ed8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af6ed8 bytes fd7bbda9
- 00af6edc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af6edc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af6edc bytes f50b00f9
- 00af6ee0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af6ee0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af6ee0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af6ee0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af6ee0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8a9f9053a6a6dab13300d3eba6033b8"></a>

### [`00af6fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6fbc.md) → [`00af7058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7058.md) FUN_00af7058

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6fbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6fbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6fc0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af6fbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6fc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6fc4",
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
      "00af7058",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af705c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af7060",
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

- 旧版 [`00af6fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6fbc.md#insn-00af6fbc) · [`00af6fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6fbc.md#insn-00af6fc0) · [`00af6fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6fbc.md#insn-00af6fc4)

~~~diff
- 00af6fbc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af6fbc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af6fbc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af6fbc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af6fbc bytes fd7bbda9
- 00af6fc0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af6fc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af6fc0 bytes f50b00f9
- 00af6fc4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af6fc4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af6fc4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af6fc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af6fc4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65b2573a5d34747f443ca737e6bf0ba0"></a>

### [`00af7008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7008.md) → [`00af70a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af70a4.md) FUN_00af70a4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af700c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7008",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af700c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7010",
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
      "00af70a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af70a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af70ac",
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

- 旧版 [`00af7008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7008.md#insn-00af7008) · [`00af700c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7008.md#insn-00af700c) · [`00af7010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7008.md#insn-00af7010)

~~~diff
- 00af7008 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af7008 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af7008 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af7008 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af7008 bytes fd7bbda9
- 00af700c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af700c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af700c bytes f50b00f9
- 00af7010 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af7010 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af7010 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af7010 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af7010 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-012375d9b638d9e8c5ffaa27cc6852a4"></a>

### [`00af7054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7054.md) → [`00af70f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af70f0.md) FUN_00af70f0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_destination` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7058"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af705c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af705c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7058",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af705c",
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
      "00af70f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af70f8",
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

- 旧版 [`00af7058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7054.md#insn-00af7058) · [`00af705c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7054.md#insn-00af705c)
- 新版 [`00af70f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af70f0.md#insn-00af70f4)

~~~diff
- 00af7058 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af7058 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af7058 bytes f50b00f9
- 00af705c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af705c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af705c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af705c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af705c bytes f44f02a9
+ 00af70f4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 00af70f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 00af70f4 bytes f50b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3883d936ceecc7760e3df2c0dd95325a"></a>

### [`00af7110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7110.md) → [`00af71ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af71ac.md) FUN_00af71ac

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7158"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af71f4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af7158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7110.md#insn-00af7158) · [`00af712c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7110.md#insn-00af712c)
- 新版 [`00af71f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af71ac.md#insn-00af71f4) · [`00af71c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af71ac.md#insn-00af71c8)

~~~diff
- 00af7158 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af7158 ["RETURN", null, ["register:0:8"]]
- 00af7158 bytes c0035fd6
+ 00af71f4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af71f4 ["RETURN", null, ["register:0:8"]]
+ 00af71f4 bytes c0035fd6
- 00af712c ["INT_ADD", "register:40f0:8", ["const:af712c:8", "const:4:8"]]
- 00af712c ["CALL", null, ["callee:00851550:8"]]
+ 00af71c8 ["INT_ADD", "register:40f0:8", ["const:af71c8:8", "const:4:8"]]
+ 00af71c8 ["CALL", null, ["callee:00851550:8"]]
- 00af712c bytes f368f597
+ 00af71c8 bytes e268f597
~~~


<a id="compare-1c7c78c0775d458c4a5941b0062ba8f3"></a>

### [`00af72d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af72d4.md) → [`00af7370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7370.md) FUN_00af7370

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af72d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af72d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af72d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af72d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af72d8",
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
      "00af7370",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af7374",
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

- 旧版 [`00af72d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af72d4.md#insn-00af72d4) · [`00af72d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af72d4.md#insn-00af72d8)
- 新版 [`00af7370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7370.md#insn-00af7370)

~~~diff
- 00af72d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af72d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af72d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af72d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af72d4 bytes fd7bbea9
- 00af72d8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af72d8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af72d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af72d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af72d8 bytes f44f01a9
+ 00af7370 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00af7370 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00af7370 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00af7370 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00af7370 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50d45d7972054711ab532fea6b7e8ad5"></a>

### [`00af731c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af731c.md) → [`00af73b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af73b8.md) FUN_00af73b8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af731c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af731c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7320"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af731c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7320",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7324",
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
      "00af73b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af73bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af73c0",
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

- 旧版 [`00af731c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af731c.md#insn-00af731c) · [`00af7320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af731c.md#insn-00af7320) · [`00af7324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af731c.md#insn-00af7324)

~~~diff
- 00af731c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af731c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af731c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af731c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af731c bytes fd7bbda9
- 00af7320 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af7320 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af7320 bytes f50b00f9
- 00af7324 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af7324 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af7324 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af7324 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af7324 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c448f4d1410322845a14248f24cb7f6"></a>

### [`00af73b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af73b0.md) → [`00af744c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af744c.md) FUN_00af744c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 57.89% / 新版 57.89%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af73b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af73b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af73b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af73b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af73b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af73b8",
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
      "00af744c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af7450",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af7454",
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

- 旧版 [`00af73b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af73b0.md#insn-00af73b0) · [`00af73b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af73b0.md#insn-00af73b4) · [`00af73b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af73b0.md#insn-00af73b8)

~~~diff
- 00af73b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af73b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af73b0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af73b0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af73b0 bytes fd7bbda9
- 00af73b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af73b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af73b4 bytes f50b00f9
- 00af73b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af73b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af73b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af73b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af73b8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b76aa7c45df6e843bedd2c8312dfe926"></a>

### [`00af73fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af73fc.md) → [`00af7498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7498.md) FUN_00af7498

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00713358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`0071425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`007133b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/007133b0.md) [`007142b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/007142b4.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 43.75% / 新版 43.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af73fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af73fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7400"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af73fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7400",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7430",
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
      "00af7498",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af749c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af74cc",
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

- 旧版 [`00af73fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af73fc.md#insn-00af73fc) · [`00af7400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af73fc.md#insn-00af7400) · [`00af7438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af73fc.md#insn-00af7438)

~~~diff
- 00af73fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af73fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af73fc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af73fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af73fc bytes fd7bbea9
- 00af7400 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af7400 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af7400 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af7400 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af7400 bytes f44f01a9
- 00af7438 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af7438 ["RETURN", null, ["register:0:8"]]
- 00af7438 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e65e61f047aec7b0454269dd86fcc5d"></a>

### [`00af7754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7754.md) → [`00af77f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af77f0.md) FUN_00af77f0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af77c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af785c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af77c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7754.md#insn-00af77c0) · [`00af7768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7754.md#insn-00af7768)
- 新版 [`00af785c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af77f0.md#insn-00af785c) · [`00af7804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af77f0.md#insn-00af7804)

~~~diff
- 00af77c0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af77c0 ["RETURN", null, ["register:0:8"]]
- 00af77c0 bytes c0035fd6
+ 00af785c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af785c ["RETURN", null, ["register:0:8"]]
+ 00af785c bytes c0035fd6
- 00af7768 ["INT_ADD", "register:40f0:8", ["const:af7768:8", "const:4:8"]]
- 00af7768 ["CALL", null, ["callee:00851550:8"]]
+ 00af7804 ["INT_ADD", "register:40f0:8", ["const:af7804:8", "const:4:8"]]
+ 00af7804 ["CALL", null, ["callee:00851550:8"]]
- 00af7768 bytes 6467f597
+ 00af7804 bytes 5367f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55da2942cf69e6781a99086ee4414490"></a>

### [`00af789c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af789c.md) → [`00af7938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7938.md) FUN_00af7938

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

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
      "site": "00af78f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af7990"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7904"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af796c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00af78f8"
      ]
    ],
    [
      "unmatched:00af78f8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af78fc",
      "READ",
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
      "00af796c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af7994"
      ]
    ],
    [
      "00af7994",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af7998",
      "READ",
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

- 旧版 [`00af78f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af789c.md#insn-00af78f4) · [`00af7904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af789c.md#insn-00af7904)
- 新版 [`00af7990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7938.md#insn-00af7990)

~~~diff
- 00af78f4 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00af78f4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af78f4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af78f4 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af78f4 bytes 136929b8
- 00af7904 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af7904 ["RETURN", null, ["register:0:8"]]
- 00af7904 bytes c0035fd6
+ 00af7990 ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00af7990 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af7990 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af7990 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af7990 bytes 136929b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5944279635cda6bc763feb3af09068a1"></a>

### [`00af7908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7908.md) → [`00af79a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af79a4.md) FUN_00af79a4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7940"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af79dc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af7940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7908.md#insn-00af7940) · [`00af7924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7908.md#insn-00af7924)
- 新版 [`00af79dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af79a4.md#insn-00af79dc) · [`00af79c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af79a4.md#insn-00af79c0)

~~~diff
- 00af7940 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00af7940 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af7940 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af7940 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af7940 bytes 136929b8
+ 00af79dc ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00af79dc ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af79dc ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af79dc ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af79dc bytes 136929b8
- 00af7924 ["INT_ADD", "register:40f0:8", ["const:af7924:8", "const:4:8"]]
- 00af7924 ["CALL", null, ["callee:00851550:8"]]
+ 00af79c0 ["INT_ADD", "register:40f0:8", ["const:af79c0:8", "const:4:8"]]
+ 00af79c0 ["CALL", null, ["callee:00851550:8"]]
- 00af7924 bytes f566f597
+ 00af79c0 bytes e466f597
~~~


<a id="compare-044956c6a5b9ed087161479e36bc1d4e"></a>

### [`00af7954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7954.md) → [`00af79f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af79f0.md) FUN_00af79f0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0070792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/0070792c.md) [`00713358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`0071425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`00707984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707984.md) [`007133b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/007133b0.md) [`007142b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/007142b4.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.44% / 新版 75.44%

CFGの説明率　旧版 10.00% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7998",
      "DATA",
      [
        "storage",
        "0030a38c",
        null,
        null
      ]
    ],
    [
      "unmatched:00af79d0",
      "DATA",
      [
        "storage",
        "0030a398",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00af7a34",
      "DATA",
      [
        "storage",
        "0030a3cc",
        null,
        null
      ]
    ],
    [
      "00af7a6c",
      "DATA",
      [
        "storage",
        "0030a3d8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af7970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7954.md#insn-00af7970) · [`00af7978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7954.md#insn-00af7978) · [`00af7994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7954.md#insn-00af7994)
- 新版 [`00af7a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af79f0.md#insn-00af7a0c) · [`00af7a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af79f0.md#insn-00af7a14)

~~~diff
- 00af7970 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00af7970 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00af7970 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 00af7a0c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00af7a0c ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
+ 00af7a0c ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00af7970 bytes 0d040054
+ 00af7a0c bytes 0d040054
- 00af7978 ["INT_ADD", "register:40f0:8", ["const:af7978:8", "const:4:8"]]
- 00af7978 ["CALL", null, ["callee:00851550:8"]]
+ 00af7a14 ["INT_ADD", "register:40f0:8", ["const:af7a14:8", "const:4:8"]]
+ 00af7a14 ["CALL", null, ["callee:00851550:8"]]
- 00af7978 bytes e066f597
+ 00af7a14 bytes cf66f597
- 00af7994 ["COPY", "tmp:0:8", ["const:38c:8"]]
- 00af7994 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00af7994 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00af7994 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00af7994 bytes 29310e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19f03bc0b37b56398c97d117906b8917"></a>

### [`00af7a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7a38.md) → [`00af7ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7ad4.md) FUN_00af7ad4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 57.69% / 新版 57.69%

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
      "site": "00af7a8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af7b28"
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
      "unmatched:00af7a7c",
      "DATA",
      [
        "storage",
        "002c3f0c",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af7b18",
      "DATA",
      [
        "storage",
        "002c3f4c",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af7a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7a38.md#insn-00af7a8c) · [`00af7a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7a38.md#insn-00af7a48)
- 新版 [`00af7b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7ad4.md#insn-00af7b28)

~~~diff
- 00af7a8c ["COPY", "tmp:0:4", ["register:40b0:4"]]
- 00af7a8c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af7a8c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af7a8c ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af7a8c bytes 166929b8
+ 00af7b28 ["COPY", "tmp:0:4", ["register:40b0:4"]]
+ 00af7b28 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af7b28 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af7b28 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af7b28 bytes 166929b8
- 00af7a48 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00af7a48 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c9f20fa1a60b0fcaed809b2496ba88e"></a>

### [`00af7aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7aa0.md) → [`00af7b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7b3c.md) FUN_00af7b3c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0070792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/0070792c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00707984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707984.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.06% / 新版 88.06%

CFGの説明率　旧版 25.00% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7aec",
      "DATA",
      [
        "storage",
        "0030a38c",
        null,
        null
      ]
    ],
    [
      "00af7bb8",
      "DATA",
      [
        "storage",
        "0030a398",
        null,
        "undefined4"
      ]
    ],
    [
      "00af7c24",
      "READ",
      [
        "storage",
        "0030a398",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00af7b88",
      "DATA",
      [
        "storage",
        "0030a3cc",
        null,
        null
      ]
    ],
    [
      "00af7bb8",
      "DATA",
      [
        "storage",
        "0030a3d8",
        null,
        "undefined4"
      ]
    ],
    [
      "00af7c24",
      "READ",
      [
        "storage",
        "0030a3d8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af7ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7aa0.md#insn-00af7ac0) · [`00af7ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7aa0.md#insn-00af7ac4) · [`00af7acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7aa0.md#insn-00af7acc)
- 新版 [`00af7b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7b3c.md#insn-00af7b5c) · [`00af7b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7b3c.md#insn-00af7b60) · [`00af7b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7b3c.md#insn-00af7b68)

~~~diff
- 00af7ac0 ["COPY", "tmp:0:8", ["const:398:8"]]
- 00af7ac0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00af7ac0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00af7ac0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00af7b5c ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 00af7b5c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00af7b5c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00af7b5c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00af7ac0 bytes d6620e91
+ 00af7b5c bytes d6620f91
- 00af7ac4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00af7ac4 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00af7ac4 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
+ 00af7b60 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00af7b60 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
+ 00af7b60 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00af7ac4 bytes cd030054
+ 00af7b60 bytes cd030054
- 00af7acc ["INT_ADD", "register:40f0:8", ["const:af7acc:8", "const:4:8"]]
- 00af7acc ["CALL", null, ["callee:00851550:8"]]
+ 00af7b68 ["INT_ADD", "register:40f0:8", ["const:af7b68:8", "const:4:8"]]
+ 00af7b68 ["CALL", null, ["callee:00851550:8"]]
- 00af7acc bytes 8b66f597
+ 00af7b68 bytes 7a66f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-438765f943cd5cdaebdf566a1a16e674"></a>

### [`00af7e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7e54.md) → [`00af7ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7ef0.md) FUN_00af7ef0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7e90"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af7f2c"
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
      "unmatched:00af7e88",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7e8c",
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
      "00af7f24",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af7f28",
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

- 旧版 [`00af7e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7e54.md#insn-00af7e90) · [`00af7e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7e54.md#insn-00af7e68)
- 新版 [`00af7f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7ef0.md#insn-00af7f2c) · [`00af7f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7ef0.md#insn-00af7f04)

~~~diff
- 00af7e90 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af7e90 ["RETURN", null, ["register:0:8"]]
- 00af7e90 bytes c0035fd6
+ 00af7f2c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af7f2c ["RETURN", null, ["register:0:8"]]
+ 00af7f2c bytes c0035fd6
- 00af7e68 ["INT_ADD", "register:40f0:8", ["const:af7e68:8", "const:4:8"]]
- 00af7e68 ["CALL", null, ["callee:00851550:8"]]
+ 00af7f04 ["INT_ADD", "register:40f0:8", ["const:af7f04:8", "const:4:8"]]
+ 00af7f04 ["CALL", null, ["callee:00851550:8"]]
- 00af7e68 bytes a465f597
+ 00af7f04 bytes 9365f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13704353d16bf06300009cb45355e58f"></a>

### [`00af7e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7e94.md) → [`00af7f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7f30.md) FUN_00af7f30

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7e94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7e94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7e98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7e94",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7e98",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7e9c",
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
      "00af7f30",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af7f34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af7f38",
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

- 旧版 [`00af7e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7e94.md#insn-00af7e94) · [`00af7e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7e94.md#insn-00af7e98) · [`00af7e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7e94.md#insn-00af7e9c)

~~~diff
- 00af7e94 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af7e94 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af7e94 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af7e94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af7e94 bytes fd7bbda9
- 00af7e98 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af7e98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af7e98 bytes f50b00f9
- 00af7e9c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af7e9c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af7e9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af7e9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af7e9c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-257296ab3fbd091b40ed851120c4c582"></a>

### [`00af7ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7ee0.md) → [`00af7f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7f7c.md) FUN_00af7f7c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7ee0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7ee0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7ee4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7ee0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7ee4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7f14",
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
      "00af7f7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af7f80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af7fb0",
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

- 旧版 [`00af7ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7ee0.md#insn-00af7ee0) · [`00af7ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7ee0.md#insn-00af7ee4) · [`00af7f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7ee0.md#insn-00af7f1c)

~~~diff
- 00af7ee0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af7ee0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af7ee0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af7ee0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af7ee0 bytes fd7bbea9
- 00af7ee4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af7ee4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af7ee4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af7ee4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af7ee4 bytes f44f01a9
- 00af7f1c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af7f1c ["RETURN", null, ["register:0:8"]]
- 00af7f1c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d03d2602685e6e94749246556707056e"></a>

### [`00af7f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7f6c.md) → [`00af8008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8008.md) FUN_00af8008

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

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
      "site": "00af7fa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af8044"
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
      "unmatched:00af7fa0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7fa4",
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
      "00af803c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af8040",
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

- 旧版 [`00af7fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7f6c.md#insn-00af7fa8) · [`00af7f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7f6c.md#insn-00af7f80)
- 新版 [`00af8044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8008.md#insn-00af8044) · [`00af801c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8008.md#insn-00af801c)

~~~diff
- 00af7fa8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af7fa8 ["RETURN", null, ["register:0:8"]]
- 00af7fa8 bytes c0035fd6
+ 00af8044 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af8044 ["RETURN", null, ["register:0:8"]]
+ 00af8044 bytes c0035fd6
- 00af7f80 ["INT_ADD", "register:40f0:8", ["const:af7f80:8", "const:4:8"]]
- 00af7f80 ["CALL", null, ["callee:00851550:8"]]
+ 00af801c ["INT_ADD", "register:40f0:8", ["const:af801c:8", "const:4:8"]]
+ 00af801c ["CALL", null, ["callee:00851550:8"]]
- 00af7f80 bytes 5e65f597
+ 00af801c bytes 4d65f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-272a7c72308b306c96aa0540627c97a9"></a>

### [`00af7fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7fac.md) → [`00af8048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8048.md) FUN_00af8048

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7fe4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af8080"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7ff4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7fec",
      "READ",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7ff0",
      "DATA",
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
      "00af8088",
      "READ",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af808c",
      "DATA",
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

- 旧版 [`00af7fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7fac.md#insn-00af7fe4) · [`00af7ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7fac.md#insn-00af7ff4)
- 新版 [`00af8080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8048.md#insn-00af8080)

~~~diff
- 00af7fe4 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00af7fe4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af7fe4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af7fe4 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af7fe4 bytes 136929b8
- 00af7ff4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af7ff4 ["RETURN", null, ["register:0:8"]]
- 00af7ff4 bytes c0035fd6
+ 00af8080 ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00af8080 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af8080 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af8080 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af8080 bytes 136929b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6f7b2fe6914dc1d3058c85c61ccb9ac"></a>

### [`00af7ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7ff8.md) → [`00af8094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8094.md) FUN_00af8094

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af803c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af80d8"
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
      "unmatched:00af8034",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8038",
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
      "00af80d0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af80d4",
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

- 旧版 [`00af803c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7ff8.md#insn-00af803c) · [`00af800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7ff8.md#insn-00af800c)
- 新版 [`00af80d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8094.md#insn-00af80d8) · [`00af80a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8094.md#insn-00af80a8)

~~~diff
- 00af803c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af803c ["RETURN", null, ["register:0:8"]]
- 00af803c bytes c0035fd6
+ 00af80d8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af80d8 ["RETURN", null, ["register:0:8"]]
+ 00af80d8 bytes c0035fd6
- 00af800c ["INT_ADD", "register:40f0:8", ["const:af800c:8", "const:4:8"]]
- 00af800c ["CALL", null, ["callee:00851550:8"]]
+ 00af80a8 ["INT_ADD", "register:40f0:8", ["const:af80a8:8", "const:4:8"]]
+ 00af80a8 ["CALL", null, ["callee:00851550:8"]]
- 00af800c bytes 3b65f597
+ 00af80a8 bytes 2a65f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-862403255b4a3af2def268e9ad5bd7b7"></a>

### [`00af8040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8040.md) → [`00af80dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af80dc.md) FUN_00af80dc

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af807c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af8118"
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
      "unmatched:00af8074",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8078",
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
      "00af8110",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af8114",
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

- 旧版 [`00af807c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8040.md#insn-00af807c) · [`00af8054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8040.md#insn-00af8054)
- 新版 [`00af8118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af80dc.md#insn-00af8118) · [`00af80f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af80dc.md#insn-00af80f0)

~~~diff
- 00af807c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af807c ["RETURN", null, ["register:0:8"]]
- 00af807c bytes c0035fd6
+ 00af8118 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af8118 ["RETURN", null, ["register:0:8"]]
+ 00af8118 bytes c0035fd6
- 00af8054 ["INT_ADD", "register:40f0:8", ["const:af8054:8", "const:4:8"]]
- 00af8054 ["CALL", null, ["callee:00851550:8"]]
+ 00af80f0 ["INT_ADD", "register:40f0:8", ["const:af80f0:8", "const:4:8"]]
+ 00af80f0 ["CALL", null, ["callee:00851550:8"]]
- 00af8054 bytes 2965f597
+ 00af80f0 bytes 1865f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd265d32bcad2589281ef75aadedb312"></a>

### [`00af8154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8154.md) → [`00af81f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af81f0.md) FUN_00af81f0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00af8190"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af822c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af8190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8154.md#insn-00af8190) · [`00af8168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8154.md#insn-00af8168)
- 新版 [`00af822c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af81f0.md#insn-00af822c) · [`00af8204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af81f0.md#insn-00af8204)

~~~diff
- 00af8190 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af8190 ["RETURN", null, ["register:0:8"]]
- 00af8190 bytes c0035fd6
+ 00af822c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af822c ["RETURN", null, ["register:0:8"]]
+ 00af822c bytes c0035fd6
- 00af8168 ["INT_ADD", "register:40f0:8", ["const:af8168:8", "const:4:8"]]
- 00af8168 ["CALL", null, ["callee:00851550:8"]]
+ 00af8204 ["INT_ADD", "register:40f0:8", ["const:af8204:8", "const:4:8"]]
+ 00af8204 ["CALL", null, ["callee:00851550:8"]]
- 00af8168 bytes e464f597
+ 00af8204 bytes d364f597
~~~


<a id="compare-53c3e0abf0f61a496a6965edcf331b15"></a>

### [`00af8260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8260.md) → [`00af82fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af82fc.md) FUN_00af82fc

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af82a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af8344"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af82a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8260.md#insn-00af82a8) · [`00af827c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8260.md#insn-00af827c)
- 新版 [`00af8344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af82fc.md#insn-00af8344) · [`00af8318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af82fc.md#insn-00af8318)

~~~diff
- 00af82a8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af82a8 ["RETURN", null, ["register:0:8"]]
- 00af82a8 bytes c0035fd6
+ 00af8344 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af8344 ["RETURN", null, ["register:0:8"]]
+ 00af8344 bytes c0035fd6
- 00af827c ["INT_ADD", "register:40f0:8", ["const:af827c:8", "const:4:8"]]
- 00af827c ["CALL", null, ["callee:00851550:8"]]
+ 00af8318 ["INT_ADD", "register:40f0:8", ["const:af8318:8", "const:4:8"]]
+ 00af8318 ["CALL", null, ["callee:00851550:8"]]
- 00af827c bytes 9f64f597
+ 00af8318 bytes 8e64f597
~~~


<a id="compare-bee6f926c7d2f0b4ce3fec67a5548a6b"></a>

### [`00af82ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af82ec.md) → [`00af8388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8388.md) FUN_00af8388

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 57.89% / 新版 57.89%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af82ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af82ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af82f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af82ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af82f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af82f4",
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
      "00af8388",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af838c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af8390",
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

- 旧版 [`00af82ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af82ec.md#insn-00af82ec) · [`00af82f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af82ec.md#insn-00af82f0) · [`00af82f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af82ec.md#insn-00af82f4)

~~~diff
- 00af82ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af82ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af82ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af82ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af82ec bytes fd7bbda9
- 00af82f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af82f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af82f0 bytes f50b00f9
- 00af82f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af82f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af82f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af82f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af82f4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0686c267dc323e9c6ab855409c40613a"></a>

### [`00af8378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8378.md) → [`00af8414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8414.md) FUN_00af8414

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

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
      "site": "00af83c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af845c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af83c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8378.md#insn-00af83c0) · [`00af8394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8378.md#insn-00af8394)
- 新版 [`00af845c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8414.md#insn-00af845c) · [`00af8430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8414.md#insn-00af8430)

~~~diff
- 00af83c0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af83c0 ["RETURN", null, ["register:0:8"]]
- 00af83c0 bytes c0035fd6
+ 00af845c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af845c ["RETURN", null, ["register:0:8"]]
+ 00af845c bytes c0035fd6
- 00af8394 ["INT_ADD", "register:40f0:8", ["const:af8394:8", "const:4:8"]]
- 00af8394 ["CALL", null, ["callee:00851550:8"]]
+ 00af8430 ["INT_ADD", "register:40f0:8", ["const:af8430:8", "const:4:8"]]
+ 00af8430 ["CALL", null, ["callee:00851550:8"]]
- 00af8394 bytes 5964f597
+ 00af8430 bytes 4864f597
~~~


<a id="compare-d3a050af5f927e4c49c0395d3c7931eb"></a>

### [`00af8450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8450.md) → [`00af84ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af84ec.md) FUN_00af84ec

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af8524"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af8488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8450.md#insn-00af8488) · [`00af846c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8450.md#insn-00af846c)
- 新版 [`00af8524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af84ec.md#insn-00af8524) · [`00af8508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af84ec.md#insn-00af8508)

~~~diff
- 00af8488 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00af8488 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af8488 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af8488 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af8488 bytes 136929b8
+ 00af8524 ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00af8524 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af8524 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af8524 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af8524 bytes 136929b8
- 00af846c ["INT_ADD", "register:40f0:8", ["const:af846c:8", "const:4:8"]]
- 00af846c ["CALL", null, ["callee:00851550:8"]]
+ 00af8508 ["INT_ADD", "register:40f0:8", ["const:af8508:8", "const:4:8"]]
+ 00af8508 ["CALL", null, ["callee:00851550:8"]]
- 00af846c bytes 2364f597
+ 00af8508 bytes 1264f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5168a8204bdc9ed2ff4dc40f9ae5f125"></a>

### [`00af849c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af849c.md) → [`00af8538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8538.md) FUN_00af8538

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af849c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af849c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af84a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af849c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af84a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af84a4",
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
      "00af8538",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af853c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af8540",
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

- 旧版 [`00af849c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af849c.md#insn-00af849c) · [`00af84a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af849c.md#insn-00af84a0) · [`00af84a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af849c.md#insn-00af84a4)

~~~diff
- 00af849c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af849c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af849c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af849c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af849c bytes fd7bbda9
- 00af84a0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af84a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af84a0 bytes f50b00f9
- 00af84a4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af84a4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af84a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af84a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af84a4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46c6bb355b6979e99ff1652c0c0a86ec"></a>

### [`00af84e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af84e8.md) → [`00af8584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8584.md) FUN_00af8584

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00714f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) [`00715500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`00714fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714fe4.md) [`00715558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00715/00715558.md) [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 43.75% / 新版 43.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af84e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af84e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af84ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af84e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af84ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af851c",
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
      "00af8584",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af8588",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af85b8",
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

- 旧版 [`00af84e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af84e8.md#insn-00af84e8) · [`00af84ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af84e8.md#insn-00af84ec) · [`00af8524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af84e8.md#insn-00af8524)

~~~diff
- 00af84e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af84e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af84e8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af84e8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af84e8 bytes fd7bbea9
- 00af84ec ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af84ec ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af84ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af84ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af84ec bytes f44f01a9
- 00af8524 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af8524 ["RETURN", null, ["register:0:8"]]
- 00af8524 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70d7026ab1d77e0a24a849263f57ba73"></a>

### [`00af8528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8528.md) → [`00af85c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af85c4.md) FUN_00af85c4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 57.89% / 新版 57.89%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af852c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af8528",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af852c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8530",
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
      "00af85c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af85c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af85cc",
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

- 旧版 [`00af8528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8528.md#insn-00af8528) · [`00af852c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8528.md#insn-00af852c) · [`00af8530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8528.md#insn-00af8530)

~~~diff
- 00af8528 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af8528 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af8528 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af8528 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af8528 bytes fd7bbda9
- 00af852c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af852c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af852c bytes f50b00f9
- 00af8530 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af8530 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af8530 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af8530 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af8530 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd1ee129fa6b63576477d7084915132c"></a>

### [`00af8600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8600.md) → [`00af869c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af869c.md) FUN_00af869c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00714f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) [`00715500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`00714fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714fe4.md) [`00715558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00715/00715558.md) [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00af863c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af86d8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af863c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8600.md#insn-00af863c) · [`00af8614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8600.md#insn-00af8614)
- 新版 [`00af86d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af869c.md#insn-00af86d8) · [`00af86b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af869c.md#insn-00af86b0)

~~~diff
- 00af863c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af863c ["RETURN", null, ["register:0:8"]]
- 00af863c bytes c0035fd6
+ 00af86d8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af86d8 ["RETURN", null, ["register:0:8"]]
+ 00af86d8 bytes c0035fd6
- 00af8614 ["INT_ADD", "register:40f0:8", ["const:af8614:8", "const:4:8"]]
- 00af8614 ["CALL", null, ["callee:00851550:8"]]
+ 00af86b0 ["INT_ADD", "register:40f0:8", ["const:af86b0:8", "const:4:8"]]
+ 00af86b0 ["CALL", null, ["callee:00851550:8"]]
- 00af8614 bytes b963f597
+ 00af86b0 bytes a863f597
~~~


<a id="compare-7f2b8852e2ff2ce2e2e5e56416515b44"></a>

### [`00af86cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af86cc.md) → [`00af8768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8768.md) FUN_00af8768

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

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
      "site": "00af8714"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af87b0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af8714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af86cc.md#insn-00af8714) · [`00af86e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af86cc.md#insn-00af86e8)
- 新版 [`00af87b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8768.md#insn-00af87b0) · [`00af8784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8768.md#insn-00af8784)

~~~diff
- 00af8714 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af8714 ["RETURN", null, ["register:0:8"]]
- 00af8714 bytes c0035fd6
+ 00af87b0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af87b0 ["RETURN", null, ["register:0:8"]]
+ 00af87b0 bytes c0035fd6
- 00af86e8 ["INT_ADD", "register:40f0:8", ["const:af86e8:8", "const:4:8"]]
- 00af86e8 ["CALL", null, ["callee:00851550:8"]]
+ 00af8784 ["INT_ADD", "register:40f0:8", ["const:af8784:8", "const:4:8"]]
+ 00af8784 ["CALL", null, ["callee:00851550:8"]]
- 00af86e8 bytes 8463f597
+ 00af8784 bytes 7363f597
~~~


<a id="compare-7ae1de8ff462891c6c69e924003ade90"></a>

### [`00af8758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8758.md) → [`00af87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af87f4.md) FUN_00af87f4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8758"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8758"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af875c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af8758",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af875c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8760",
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
      "00af87f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af87f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af87fc",
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

- 旧版 [`00af8758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8758.md#insn-00af8758) · [`00af875c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8758.md#insn-00af875c) · [`00af8760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8758.md#insn-00af8760)

~~~diff
- 00af8758 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af8758 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af8758 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af8758 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af8758 bytes fd7bbda9
- 00af875c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af875c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af875c bytes f50b00f9
- 00af8760 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af8760 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af8760 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af8760 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af8760 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f60672f04b8e4ad1dc244e10bfe0fcd"></a>

### [`00af87ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af87ec.md) → [`00af8888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8888.md) FUN_00af8888

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00714f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00714fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714fe4.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af87ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af87ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af87f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af87ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af87f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af87f4",
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
      "00af8888",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af888c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af8890",
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

- 旧版 [`00af87ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af87ec.md#insn-00af87ec) · [`00af87f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af87ec.md#insn-00af87f0) · [`00af87f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af87ec.md#insn-00af87f4)

~~~diff
- 00af87ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af87ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af87ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af87ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af87ec bytes fd7bbda9
- 00af87f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af87f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af87f0 bytes f50b00f9
- 00af87f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af87f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af87f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af87f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af87f4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eb754b863752be56f359ba7e16f9fc7"></a>

### [`00af8838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8838.md) → [`00af88d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af88d4.md) FUN_00af88d4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00714f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00714fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714fe4.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8838"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8838"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af883c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af8838",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af883c",
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
      "00af88d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af88d8",
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

- 旧版 [`00af8838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8838.md#insn-00af8838) · [`00af883c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8838.md#insn-00af883c)
- 新版 [`00af88d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af88d4.md#insn-00af88d4)

~~~diff
- 00af8838 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af8838 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af8838 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af8838 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af8838 bytes fd7bbea9
- 00af883c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af883c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af883c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af883c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af883c bytes f44f01a9
+ 00af88d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00af88d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00af88d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00af88d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00af88d4 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e12e3fc394d35f139a6123dde7d56ae"></a>

### [`00af8878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8878.md) → [`00af8914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8914.md) FUN_00af8914

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8878"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8878"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af887c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af8878",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af887c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8880",
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
      "00af8914",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af8918",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af891c",
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

- 旧版 [`00af8878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8878.md#insn-00af8878) · [`00af887c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8878.md#insn-00af887c) · [`00af8880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8878.md#insn-00af8880)

~~~diff
- 00af8878 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af8878 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af8878 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af8878 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af8878 bytes fd7bbda9
- 00af887c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af887c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af887c bytes f50b00f9
- 00af8880 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af8880 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af8880 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af8880 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af8880 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e072e9c0de074a6274b68abaa9d48cd"></a>

### [`00af890c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af890c.md) → [`00af89a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af89a8.md) FUN_00af89a8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00714f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00714fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714fe4.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af890c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af890c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8910"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af890c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8910",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8914",
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
      "00af89a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af89ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af89b0",
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

- 旧版 [`00af890c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af890c.md#insn-00af890c) · [`00af8910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af890c.md#insn-00af8910) · [`00af8914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af890c.md#insn-00af8914)

~~~diff
- 00af890c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af890c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af890c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af890c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af890c bytes fd7bbda9
- 00af8910 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af8910 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af8910 bytes f50b00f9
- 00af8914 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af8914 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af8914 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af8914 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af8914 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72b771a909baa41cc2fdce4108a5ed6c"></a>

### [`00af89e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af89e4.md) → [`00af8a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8a80.md) FUN_00af8a80

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00713358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`0071425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`007133b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/007133b0.md) [`007142b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/007142b4.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

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
      "site": "00af8a20"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af8abc"
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
      "unmatched:00af8a18",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8a1c",
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
      "00af8ab4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af8ab8",
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

- 旧版 [`00af8a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af89e4.md#insn-00af8a20) · [`00af89f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af89e4.md#insn-00af89f8)
- 新版 [`00af8abc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8a80.md#insn-00af8abc) · [`00af8a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8a80.md#insn-00af8a94)

~~~diff
- 00af8a20 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af8a20 ["RETURN", null, ["register:0:8"]]
- 00af8a20 bytes c0035fd6
+ 00af8abc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af8abc ["RETURN", null, ["register:0:8"]]
+ 00af8abc bytes c0035fd6
- 00af89f8 ["INT_ADD", "register:40f0:8", ["const:af89f8:8", "const:4:8"]]
- 00af89f8 ["CALL", null, ["callee:00851550:8"]]
+ 00af8a94 ["INT_ADD", "register:40f0:8", ["const:af8a94:8", "const:4:8"]]
+ 00af8a94 ["CALL", null, ["callee:00851550:8"]]
- 00af89f8 bytes c062f597
+ 00af8a94 bytes af62f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a194cef9c57e92f640df3080cd4370aa"></a>

### [`00af8a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8a24.md) → [`00af8ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8ac0.md) FUN_00af8ac0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8a5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af8af8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af8a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8a24.md#insn-00af8a5c) · [`00af8a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8a24.md#insn-00af8a40)
- 新版 [`00af8af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8ac0.md#insn-00af8af8) · [`00af8adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8ac0.md#insn-00af8adc)

~~~diff
- 00af8a5c ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00af8a5c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af8a5c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af8a5c ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af8a5c bytes 136929b8
+ 00af8af8 ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00af8af8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af8af8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af8af8 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af8af8 bytes 136929b8
- 00af8a40 ["INT_ADD", "register:40f0:8", ["const:af8a40:8", "const:4:8"]]
- 00af8a40 ["CALL", null, ["callee:00851550:8"]]
+ 00af8adc ["INT_ADD", "register:40f0:8", ["const:af8adc:8", "const:4:8"]]
+ 00af8adc ["CALL", null, ["callee:00851550:8"]]
- 00af8a40 bytes ae62f597
+ 00af8adc bytes 9d62f597
~~~


<a id="compare-be3b445555fc806c54256fc7b49a6e65"></a>

### [`00af8afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8afc.md) → [`00af8b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8b98.md) FUN_00af8b98

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00715500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00715558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00715/00715558.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8b38"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af8bd4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af8b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8afc.md#insn-00af8b38) · [`00af8b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8afc.md#insn-00af8b10)
- 新版 [`00af8bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8b98.md#insn-00af8bd4) · [`00af8bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8b98.md#insn-00af8bac)

~~~diff
- 00af8b38 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af8b38 ["RETURN", null, ["register:0:8"]]
- 00af8b38 bytes c0035fd6
+ 00af8bd4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af8bd4 ["RETURN", null, ["register:0:8"]]
+ 00af8bd4 bytes c0035fd6
- 00af8b10 ["INT_ADD", "register:40f0:8", ["const:af8b10:8", "const:4:8"]]
- 00af8b10 ["CALL", null, ["callee:00851550:8"]]
+ 00af8bac ["INT_ADD", "register:40f0:8", ["const:af8bac:8", "const:4:8"]]
+ 00af8bac ["CALL", null, ["callee:00851550:8"]]
- 00af8b10 bytes 7a62f597
+ 00af8bac bytes 6962f597
~~~


<a id="compare-93986c4e9e5ebfabca63c58e36d25295"></a>

### [`00af8b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8b3c.md) → [`00af8bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8bd8.md) FUN_00af8bd8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

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
      "site": "00af8b84"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af8c20"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af8b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8b3c.md#insn-00af8b84) · [`00af8b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8b3c.md#insn-00af8b58)
- 新版 [`00af8c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8bd8.md#insn-00af8c20) · [`00af8bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8bd8.md#insn-00af8bf4)

~~~diff
- 00af8b84 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af8b84 ["RETURN", null, ["register:0:8"]]
- 00af8b84 bytes c0035fd6
+ 00af8c20 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af8c20 ["RETURN", null, ["register:0:8"]]
+ 00af8c20 bytes c0035fd6
- 00af8b58 ["INT_ADD", "register:40f0:8", ["const:af8b58:8", "const:4:8"]]
- 00af8b58 ["CALL", null, ["callee:00851550:8"]]
+ 00af8bf4 ["INT_ADD", "register:40f0:8", ["const:af8bf4:8", "const:4:8"]]
+ 00af8bf4 ["CALL", null, ["callee:00851550:8"]]
- 00af8b58 bytes 6862f597
+ 00af8bf4 bytes 5762f597
~~~


<a id="compare-08c1c701879681377b5e6a8fe9ddc72e"></a>

### [`00af8b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8b88.md) → [`00af8c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8c24.md) FUN_00af8c24

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00a52034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a52/00a52034.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

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
      "site": "00af8bc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af8c5c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af8bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8b88.md#insn-00af8bc0) · [`00af8ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8b88.md#insn-00af8ba4)
- 新版 [`00af8c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8c24.md#insn-00af8c5c) · [`00af8c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8c24.md#insn-00af8c40)

~~~diff
- 00af8bc0 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00af8bc0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af8bc0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af8bc0 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af8bc0 bytes 136929b8
+ 00af8c5c ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00af8c5c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af8c5c ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af8c5c ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af8c5c bytes 136929b8
- 00af8ba4 ["INT_ADD", "register:40f0:8", ["const:af8ba4:8", "const:4:8"]]
- 00af8ba4 ["CALL", null, ["callee:00851550:8"]]
+ 00af8c40 ["INT_ADD", "register:40f0:8", ["const:af8c40:8", "const:4:8"]]
+ 00af8c40 ["CALL", null, ["callee:00851550:8"]]
- 00af8ba4 bytes 5562f597
+ 00af8c40 bytes 4462f597
~~~


<a id="compare-bb41172f1c77f5ddb6e1b096e078aeae"></a>

### [`00af8bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8bd4.md) → [`00af8c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8c70.md) FUN_00af8c70

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8bd4.md#insn-00af8be8) · [`00af8c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8bd4.md#insn-00af8c04)
- 新版 [`00af8c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8c70.md#insn-00af8c84) · [`00af8ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8c70.md#insn-00af8ca0)

~~~diff
- 00af8be8 ["INT_ADD", "register:40f0:8", ["const:af8be8:8", "const:4:8"]]
- 00af8be8 ["CALL", null, ["callee:00851550:8"]]
+ 00af8c84 ["INT_ADD", "register:40f0:8", ["const:af8c84:8", "const:4:8"]]
+ 00af8c84 ["CALL", null, ["callee:00851550:8"]]
- 00af8be8 bytes 4462f597
+ 00af8c84 bytes 3362f597
- 00af8c04 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00af8c04 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00af8c04 ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:0:8"]]
- 00af8c04 ["INT_ADD", "tmp:2:8", ["register:4040:8", "tmp:1:8"]]
- 00af8c04 bytes 086969b8
+ 00af8ca0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00af8ca0 ["COPY", "tmp:1:8", ["tmp:0:8"]]
+ 00af8ca0 ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:0:8"]]
+ 00af8ca0 ["INT_ADD", "tmp:2:8", ["register:4040:8", "tmp:1:8"]]
+ 00af8ca0 bytes 086969b8
~~~


<a id="compare-692e5c616803c86c236ecd96eeb01eca"></a>

### [`00af8c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8c5c.md) → [`00af8cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8cf8.md) FUN_00af8cf8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8c5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8c5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8c60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af8c5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8c60",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8c64",
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
      "00af8cf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af8cfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af8d00",
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

- 旧版 [`00af8c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8c5c.md#insn-00af8c5c) · [`00af8c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8c5c.md#insn-00af8c60) · [`00af8c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8c5c.md#insn-00af8c64)

~~~diff
- 00af8c5c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af8c5c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af8c5c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af8c5c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af8c5c bytes fd7bbda9
- 00af8c60 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af8c60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af8c60 bytes f50b00f9
- 00af8c64 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af8c64 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af8c64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af8c64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af8c64 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5213d63c1d5568e07342606684a980fb"></a>

### [`00af8ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8ca8.md) → [`00af8d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8d44.md) FUN_00af8d44

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) [`00af34ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af34ec.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) [`00af3588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af3588.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

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
      "site": "00af8ca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8ca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8cac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af8ca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8cac",
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
      "00af8d44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af8d48",
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

- 旧版 [`00af8ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8ca8.md#insn-00af8ca8) · [`00af8cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8ca8.md#insn-00af8cac)
- 新版 [`00af8d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8d44.md#insn-00af8d44)

~~~diff
- 00af8ca8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af8ca8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af8ca8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af8ca8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af8ca8 bytes fd7bbea9
- 00af8cac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af8cac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af8cac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af8cac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af8cac bytes f44f01a9
+ 00af8d44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00af8d44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00af8d44 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00af8d44 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00af8d44 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5abd9a86ebf422a0af8fa9265da71cda"></a>

### [`00af8cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8cf0.md) → [`00af8d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8d8c.md) FUN_00af8d8c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8cf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8cf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8cf4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af8cf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8cf4",
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
      "00af8d8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af8d90",
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

- 旧版 [`00af8cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8cf0.md#insn-00af8cf0) · [`00af8cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8cf0.md#insn-00af8cf4)
- 新版 [`00af8d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8d8c.md#insn-00af8d8c)

~~~diff
- 00af8cf0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af8cf0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af8cf0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af8cf0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af8cf0 bytes fd7bbea9
- 00af8cf4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af8cf4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af8cf4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af8cf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af8cf4 bytes f44f01a9
+ 00af8d8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00af8d8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00af8d8c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00af8d8c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00af8d8c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-480eca74efcbeb19bb0d3d41f63b4426"></a>

### [`00af8d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8d30.md) → [`00af8dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8dcc.md) FUN_00af8dcc

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af34f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af34f4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00af3590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af3590.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

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
      "site": "00af8d68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af8e04"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af8d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8d30.md#insn-00af8d68) · [`00af8d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8d30.md#insn-00af8d3c)
- 新版 [`00af8e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8dcc.md#insn-00af8e04)

~~~diff
- 00af8d68 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00af8d68 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af8d68 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af8d68 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af8d68 bytes 136929b8
+ 00af8e04 ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00af8e04 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af8e04 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af8e04 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af8e04 bytes 136929b8
- 00af8d3c ["COPY", "register:40e8:8", ["register:8:8"]]
- 00af8d3c bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39803df6d8c58b4231833e2b6eaf6490"></a>

### [`00af8d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8d7c.md) → [`00af8e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8e18.md) FUN_00af8e18

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8db8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af8e54"
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
      "unmatched:00af8db0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8db4",
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
      "00af8e4c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af8e50",
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

- 旧版 [`00af8db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8d7c.md#insn-00af8db8) · [`00af8d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8d7c.md#insn-00af8d90)
- 新版 [`00af8e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8e18.md#insn-00af8e54) · [`00af8e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8e18.md#insn-00af8e2c)

~~~diff
- 00af8db8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af8db8 ["RETURN", null, ["register:0:8"]]
- 00af8db8 bytes c0035fd6
+ 00af8e54 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af8e54 ["RETURN", null, ["register:0:8"]]
+ 00af8e54 bytes c0035fd6
- 00af8d90 ["INT_ADD", "register:40f0:8", ["const:af8d90:8", "const:4:8"]]
- 00af8d90 ["CALL", null, ["callee:00851550:8"]]
+ 00af8e2c ["INT_ADD", "register:40f0:8", ["const:af8e2c:8", "const:4:8"]]
+ 00af8e2c ["CALL", null, ["callee:00851550:8"]]
- 00af8d90 bytes da61f597
+ 00af8e2c bytes c961f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0211865d98a05833f5ed968b3d0f9079"></a>

### [`00af8dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8dbc.md) → [`00af8e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8e58.md) FUN_00af8e58

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af3500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3500.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00af359c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af359c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8df4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af8e90"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af8df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8dbc.md#insn-00af8df4) · [`00af8dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8dbc.md#insn-00af8dd8)
- 新版 [`00af8e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8e58.md#insn-00af8e90) · [`00af8e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8e58.md#insn-00af8e74)

~~~diff
- 00af8df4 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00af8df4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af8df4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af8df4 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af8df4 bytes 136929b8
+ 00af8e90 ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00af8e90 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af8e90 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af8e90 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af8e90 bytes 136929b8
- 00af8dd8 ["INT_ADD", "register:40f0:8", ["const:af8dd8:8", "const:4:8"]]
- 00af8dd8 ["CALL", null, ["callee:00851550:8"]]
+ 00af8e74 ["INT_ADD", "register:40f0:8", ["const:af8e74:8", "const:4:8"]]
+ 00af8e74 ["CALL", null, ["callee:00851550:8"]]
- 00af8dd8 bytes c861f597
+ 00af8e74 bytes b761f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99e4d4dd3e7be08bb2568496e7565ca2"></a>

### [`00af8e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8e08.md) → [`00af8ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8ea4.md) FUN_00af8ea4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) [`00af350c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af350c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) [`00af35a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af35a8.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8e08.md#insn-00af8e1c) · [`00af8e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8e08.md#insn-00af8e38)
- 新版 [`00af8eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8ea4.md#insn-00af8eb8) · [`00af8ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8ea4.md#insn-00af8ed4)

~~~diff
- 00af8e1c ["INT_ADD", "register:40f0:8", ["const:af8e1c:8", "const:4:8"]]
- 00af8e1c ["CALL", null, ["callee:00851550:8"]]
+ 00af8eb8 ["INT_ADD", "register:40f0:8", ["const:af8eb8:8", "const:4:8"]]
+ 00af8eb8 ["CALL", null, ["callee:00851550:8"]]
- 00af8e1c bytes b761f597
+ 00af8eb8 bytes a661f597
- 00af8e38 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00af8e38 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00af8e38 ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:0:8"]]
- 00af8e38 ["INT_ADD", "tmp:2:8", ["register:4040:8", "tmp:1:8"]]
- 00af8e38 bytes 086969b8
+ 00af8ed4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00af8ed4 ["COPY", "tmp:1:8", ["tmp:0:8"]]
+ 00af8ed4 ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:0:8"]]
+ 00af8ed4 ["INT_ADD", "tmp:2:8", ["register:4040:8", "tmp:1:8"]]
+ 00af8ed4 bytes 086969b8
~~~


<a id="compare-6b86f6b275ce4299d6a6a4ce9b48dfdd"></a>

### [`00af8e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8e90.md) → [`00af8f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8f2c.md) FUN_00af8f2c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af3514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3514.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00af35b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af35b0.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8ec8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af8f64"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af8ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8e90.md#insn-00af8ec8) · [`00af8eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8e90.md#insn-00af8eac)
- 新版 [`00af8f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8f2c.md#insn-00af8f64) · [`00af8f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8f2c.md#insn-00af8f48)

~~~diff
- 00af8ec8 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00af8ec8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af8ec8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af8ec8 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af8ec8 bytes 136929b8
+ 00af8f64 ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00af8f64 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af8f64 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af8f64 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af8f64 bytes 136929b8
- 00af8eac ["INT_ADD", "register:40f0:8", ["const:af8eac:8", "const:4:8"]]
- 00af8eac ["CALL", null, ["callee:00851550:8"]]
+ 00af8f48 ["INT_ADD", "register:40f0:8", ["const:af8f48:8", "const:4:8"]]
+ 00af8f48 ["CALL", null, ["callee:00851550:8"]]
- 00af8eac bytes 9361f597
+ 00af8f48 bytes 8261f597
~~~


<a id="compare-9ae9a16221c2292e6b4560aac416e623"></a>

### [`00af8f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8f1c.md) → [`00af8fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8fb8.md) FUN_00af8fb8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af3520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3520.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00af35bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af35bc.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8f54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af8ff0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af8f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8f1c.md#insn-00af8f54) · [`00af8f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8f1c.md#insn-00af8f38)
- 新版 [`00af8ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8fb8.md#insn-00af8ff0) · [`00af8fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8fb8.md#insn-00af8fd4)

~~~diff
- 00af8f54 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00af8f54 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af8f54 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af8f54 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af8f54 bytes 136929b8
+ 00af8ff0 ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00af8ff0 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af8ff0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af8ff0 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af8ff0 bytes 136929b8
- 00af8f38 ["INT_ADD", "register:40f0:8", ["const:af8f38:8", "const:4:8"]]
- 00af8f38 ["CALL", null, ["callee:00851550:8"]]
+ 00af8fd4 ["INT_ADD", "register:40f0:8", ["const:af8fd4:8", "const:4:8"]]
+ 00af8fd4 ["CALL", null, ["callee:00851550:8"]]
- 00af8f38 bytes 7061f597
+ 00af8fd4 bytes 5f61f597
~~~


<a id="compare-25ac2df45dd17cf41d616344c92f108c"></a>

### [`00af8f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8f68.md) → [`00af9004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9004.md) FUN_00af9004

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8f68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8f68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8f6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af8f68",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8f6c",
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
      "00af9004",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af9008",
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

- 旧版 [`00af8f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8f68.md#insn-00af8f68) · [`00af8f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8f68.md#insn-00af8f6c)
- 新版 [`00af9004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9004.md#insn-00af9004)

~~~diff
- 00af8f68 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af8f68 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af8f68 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af8f68 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af8f68 bytes fd7bbea9
- 00af8f6c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af8f6c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af8f6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af8f6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af8f6c bytes f44f01a9
+ 00af9004 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00af9004 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00af9004 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00af9004 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00af9004 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd108ea5c3191f34b4c446d1fc22530c"></a>

### [`00af8fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8fb0.md) → [`00af904c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af904c.md) FUN_00af904c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00af8fe0",
      "incomplete_value": true,
      "site": "00af8fec",
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
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af8fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8fb0.md#insn-00af8fb8) · [`00af8fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8fb0.md#insn-00af8fc4)
- 新版 [`00af9060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af904c.md#insn-00af9060) · [`00af9054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af904c.md#insn-00af9054)

~~~diff
- 00af8fb8 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00af8fb8 bytes fd030091
- 00af8fc4 ["INT_ADD", "register:40f0:8", ["const:af8fc4:8", "const:4:8"]]
- 00af8fc4 ["CALL", null, ["callee:00851550:8"]]
+ 00af9060 ["INT_ADD", "register:40f0:8", ["const:af9060:8", "const:4:8"]]
+ 00af9060 ["CALL", null, ["callee:00851550:8"]]
- 00af8fc4 bytes 4d61f597
+ 00af9060 bytes 3c61f597
+ 00af9054 ["COPY", "register:40e8:8", ["register:8:8"]]
+ 00af9054 bytes fd030091
~~~


<a id="compare-2996e1bae89c303406a68b30ba267279"></a>

### [`00af9108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9108.md) → [`00af91a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af91a4.md) FUN_00af91a4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9140"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af91dc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af9140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9108.md#insn-00af9140) · [`00af9124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9108.md#insn-00af9124)
- 新版 [`00af91dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af91a4.md#insn-00af91dc) · [`00af91c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af91a4.md#insn-00af91c0)

~~~diff
- 00af9140 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00af9140 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af9140 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af9140 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af9140 bytes 136929b8
+ 00af91dc ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00af91dc ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af91dc ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00af91dc ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00af91dc bytes 136929b8
- 00af9124 ["INT_ADD", "register:40f0:8", ["const:af9124:8", "const:4:8"]]
- 00af9124 ["CALL", null, ["callee:00851550:8"]]
+ 00af91c0 ["INT_ADD", "register:40f0:8", ["const:af91c0:8", "const:4:8"]]
+ 00af91c0 ["CALL", null, ["callee:00851550:8"]]
- 00af9124 bytes f560f597
+ 00af91c0 bytes e460f597
~~~


<a id="compare-852a5743abb04907caa2406e82585799"></a>

### [`00af9154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9154.md) → [`00af91f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af91f0.md) FUN_00af91f0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) [`00af352c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af352c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) [`00af35c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af35c8.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9154"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9154"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9158"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af9154",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9158",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9190",
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
      "00af91f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af91f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af922c",
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

- 旧版 [`00af9154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9154.md#insn-00af9154) · [`00af9158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9154.md#insn-00af9158) · [`00af9198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9154.md#insn-00af9198)

~~~diff
- 00af9154 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af9154 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af9154 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af9154 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af9154 bytes fd7bbea9
- 00af9158 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af9158 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af9158 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af9158 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af9158 bytes f44f01a9
- 00af9198 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af9198 ["RETURN", null, ["register:0:8"]]
- 00af9198 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b230d8b721fb76ca982ad4a96aecb451"></a>

### [`00af919c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af919c.md) → [`00af9238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9238.md) FUN_00af9238

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 43.75% / 新版 43.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af919c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af919c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af91a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af919c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af91a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af91d0",
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
      "00af9238",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af923c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af926c",
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

- 旧版 [`00af919c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af919c.md#insn-00af919c) · [`00af91a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af919c.md#insn-00af91a0) · [`00af91d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af919c.md#insn-00af91d8)

~~~diff
- 00af919c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af919c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af919c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af919c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af919c bytes fd7bbea9
- 00af91a0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af91a0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af91a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af91a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af91a0 bytes f44f01a9
- 00af91d8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af91d8 ["RETURN", null, ["register:0:8"]]
- 00af91d8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df02fe8d4ac04dc0bc54518dbd3d54fc"></a>

### [`00af91dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af91dc.md) → [`00af9278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9278.md) FUN_00af9278

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af3534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3534.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00af35d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af35d0.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af91dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af91dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af91e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af91dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af91e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af91e4",
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
      "00af9278",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af927c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af9280",
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

- 旧版 [`00af91dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af91dc.md#insn-00af91dc) · [`00af91e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af91dc.md#insn-00af91e0) · [`00af91e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af91dc.md#insn-00af91e4)

~~~diff
- 00af91dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af91dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af91dc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af91dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af91dc bytes fd7bbda9
- 00af91e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af91e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af91e0 bytes f50b00f9
- 00af91e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af91e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af91e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af91e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af91e4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-537707bc64c1d1f46e56eae99854f5d2"></a>

### [`00af92b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af92b4.md) → [`00af9350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9350.md) FUN_00af9350

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af92b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af92b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af92b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af92b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af92b8",
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
      "00af9350",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af9354",
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

- 旧版 [`00af92b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af92b4.md#insn-00af92b4) · [`00af92b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af92b4.md#insn-00af92b8)
- 新版 [`00af9350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9350.md#insn-00af9350)

~~~diff
- 00af92b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af92b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af92b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af92b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af92b4 bytes fd7bbea9
- 00af92b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af92b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af92b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af92b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af92b8 bytes f44f01a9
+ 00af9350 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00af9350 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00af9350 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00af9350 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00af9350 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03cc18c8c9f46a63995e1309e2c9719f"></a>

### [`00af92f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af92f4.md) → [`00af9390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9390.md) FUN_00af9390

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af93c8",
      "incomplete_value": true,
      "site": "00af93c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4040:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af932c",
      "incomplete_value": true,
      "site": "00af932c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af9300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af92f4.md#insn-00af9300) · [`00af9310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af92f4.md#insn-00af9310) · [`00af9320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af92f4.md#insn-00af9320)
- 新版 [`00af93ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9390.md#insn-00af93ac)

~~~diff
- 00af9300 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00af9300 bytes fd030091
- 00af9310 ["INT_ADD", "register:40f0:8", ["const:af9310:8", "const:4:8"]]
- 00af9310 ["CALL", null, ["callee:00851550:8"]]
+ 00af93ac ["INT_ADD", "register:40f0:8", ["const:af93ac:8", "const:4:8"]]
+ 00af93ac ["CALL", null, ["callee:00851550:8"]]
- 00af9310 bytes 7a60f597
+ 00af93ac bytes 6960f597
- 00af9320 ["INT_SEXT", "tmp:0:8", ["register:40a0:4"]]
- 00af9320 ["INT_SEXT", "tmp:1:8", ["register:4048:4"]]
- 00af9320 ["INT_MULT", "tmp:2:8", ["tmp:0:8", "tmp:1:8"]]
- 00af9320 ["INT_ADD", "register:4040:8", ["register:4040:8", "tmp:2:8"]]
- 00af9320 bytes 8822299b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3944d4d2064f7cf0c8908e0c4e54328"></a>

### [`00af9340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9340.md) → [`00af93dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af93dc.md) FUN_00af93dc

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af937c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af9418"
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
      "unmatched:00af9374",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9378",
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
      "00af9410",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af9414",
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

- 旧版 [`00af937c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9340.md#insn-00af937c) · [`00af9354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9340.md#insn-00af9354)
- 新版 [`00af9418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af93dc.md#insn-00af9418) · [`00af93f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af93dc.md#insn-00af93f0)

~~~diff
- 00af937c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af937c ["RETURN", null, ["register:0:8"]]
- 00af937c bytes c0035fd6
+ 00af9418 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af9418 ["RETURN", null, ["register:0:8"]]
+ 00af9418 bytes c0035fd6
- 00af9354 ["INT_ADD", "register:40f0:8", ["const:af9354:8", "const:4:8"]]
- 00af9354 ["CALL", null, ["callee:00851550:8"]]
+ 00af93f0 ["INT_ADD", "register:40f0:8", ["const:af93f0:8", "const:4:8"]]
+ 00af93f0 ["CALL", null, ["callee:00851550:8"]]
- 00af9354 bytes 6960f597
+ 00af93f0 bytes 5860f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0e7d55cdbeeb02387f6ff735ffa97dc"></a>

### [`00af9714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9714.md) → [`00af97b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af97b0.md) FUN_00af97b0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 28.57% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af9728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9714.md#insn-00af9728) · [`00af973c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9714.md#insn-00af973c) · [`00af9748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9714.md#insn-00af9748)
- 新版 [`00af97c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af97b0.md#insn-00af97c4) · [`00af97d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af97b0.md#insn-00af97d8) · [`00af97e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af97b0.md#insn-00af97e4)

~~~diff
- 00af9728 ["INT_ADD", "register:40f0:8", ["const:af9728:8", "const:4:8"]]
- 00af9728 ["CALL", null, ["callee:00851550:8"]]
+ 00af97c4 ["INT_ADD", "register:40f0:8", ["const:af97c4:8", "const:4:8"]]
+ 00af97c4 ["CALL", null, ["callee:00851550:8"]]
- 00af9728 bytes 745ff597
+ 00af97c4 bytes 635ff597
- 00af973c ["INT_ADD", "register:40f0:8", ["const:af973c:8", "const:4:8"]]
- 00af973c ["CALL", null, ["callee:005e7460:8"]]
+ 00af97d8 ["INT_ADD", "register:40f0:8", ["const:af97d8:8", "const:4:8"]]
+ 00af97d8 ["CALL", null, ["callee:005e7460:8"]]
- 00af973c bytes 39b7eb97
+ 00af97d8 bytes 22b7eb97
- 00af9748 ["BRANCH", null, ["local:b12:8"]]
+ 00af97e4 ["BRANCH", null, ["local:b11:8"]]
- 00af9748 bytes 0c000014
+ 00af97e4 bytes 0c000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d4a3c6add40573f20ab67a1c8298bae"></a>

### [`00af9864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9864.md) → [`00af9900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9900.md) FUN_00af9900

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9864"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9864"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9868"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af9864",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9868",
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
      "00af9900",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af9904",
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

- 旧版 [`00af9864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9864.md#insn-00af9864) · [`00af9868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9864.md#insn-00af9868) · [`00af98c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9864.md#insn-00af98c0)

~~~diff
- 00af9864 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af9864 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af9864 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af9864 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af9864 bytes fd7bbda9
- 00af9868 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af9868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af9868 bytes f50b00f9
- 00af98c0 ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 00af98c0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af98c0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af98c0 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00af98c0 bytes 146929b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ab9e4a0b22f7aed8078b6909bf0a4b6"></a>

### [`00af9944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9944.md) → [`00af99e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af99e0.md) FUN_00af99e0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.43% / 新版 96.43%

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
      "site": "00af99b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af9a4c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af99b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9944.md#insn-00af99b0) · [`00af9960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9944.md#insn-00af9960)
- 新版 [`00af9a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af99e0.md#insn-00af9a4c) · [`00af99fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af99e0.md#insn-00af99fc)

~~~diff
- 00af99b0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af99b0 ["RETURN", null, ["register:0:8"]]
- 00af99b0 bytes c0035fd6
+ 00af9a4c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af9a4c ["RETURN", null, ["register:0:8"]]
+ 00af9a4c bytes c0035fd6
- 00af9960 ["INT_ADD", "register:40f0:8", ["const:af9960:8", "const:4:8"]]
- 00af9960 ["CALL", null, ["callee:00851550:8"]]
+ 00af99fc ["INT_ADD", "register:40f0:8", ["const:af99fc:8", "const:4:8"]]
+ 00af99fc ["CALL", null, ["callee:00851550:8"]]
- 00af9960 bytes e65ef597
+ 00af99fc bytes d55ef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09de3ab3656889aef94dab963174b17f"></a>

### [`00af9b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9b1c.md) → [`00af9bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9bb8.md) FUN_00af9bb8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9b64"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af9c00"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af9b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9b1c.md#insn-00af9b64) · [`00af9b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9b1c.md#insn-00af9b38)
- 新版 [`00af9c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9bb8.md#insn-00af9c00) · [`00af9bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9bb8.md#insn-00af9bd4)

~~~diff
- 00af9b64 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af9b64 ["RETURN", null, ["register:0:8"]]
- 00af9b64 bytes c0035fd6
+ 00af9c00 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af9c00 ["RETURN", null, ["register:0:8"]]
+ 00af9c00 bytes c0035fd6
- 00af9b38 ["INT_ADD", "register:40f0:8", ["const:af9b38:8", "const:4:8"]]
- 00af9b38 ["CALL", null, ["callee:00851550:8"]]
+ 00af9bd4 ["INT_ADD", "register:40f0:8", ["const:af9bd4:8", "const:4:8"]]
+ 00af9bd4 ["CALL", null, ["callee:00851550:8"]]
- 00af9b38 bytes 705ef597
+ 00af9bd4 bytes 5f5ef597
~~~


<a id="compare-c8de43b35229264c10043370f5f600b6"></a>

### [`00af9e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9e2c.md) → [`00af9ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9ec8.md) FUN_00af9ec8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.43% / 新版 96.43%

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
      "site": "00af9e98"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af9f34"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af9e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9e2c.md#insn-00af9e98) · [`00af9e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9e2c.md#insn-00af9e48)
- 新版 [`00af9f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9ec8.md#insn-00af9f34) · [`00af9ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9ec8.md#insn-00af9ee4)

~~~diff
- 00af9e98 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af9e98 ["RETURN", null, ["register:0:8"]]
- 00af9e98 bytes c0035fd6
+ 00af9f34 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af9f34 ["RETURN", null, ["register:0:8"]]
+ 00af9f34 bytes c0035fd6
- 00af9e48 ["INT_ADD", "register:40f0:8", ["const:af9e48:8", "const:4:8"]]
- 00af9e48 ["CALL", null, ["callee:00851550:8"]]
+ 00af9ee4 ["INT_ADD", "register:40f0:8", ["const:af9ee4:8", "const:4:8"]]
+ 00af9ee4 ["CALL", null, ["callee:00851550:8"]]
- 00af9e48 bytes ac5df597
+ 00af9ee4 bytes 9b5df597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9dd321c8ef23402249189d5252ac444"></a>

### [`00afa05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa05c.md) → [`00afa0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa0f8.md) FUN_00afa0f8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa05c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa05c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa060"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa05c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa060",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa064",
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
      "00afa0f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00afa0fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afa100",
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

- 旧版 [`00afa05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa05c.md#insn-00afa05c) · [`00afa060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa05c.md#insn-00afa060) · [`00afa064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa05c.md#insn-00afa064)

~~~diff
- 00afa05c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afa05c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afa05c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00afa05c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afa05c bytes fd7bbca9
- 00afa060 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00afa060 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00afa060 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afa060 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa060 bytes f85f01a9
- 00afa064 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00afa064 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afa064 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afa064 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa064 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-908bf634bf6c96b13923f8b143474418"></a>

### [`00afa1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa1cc.md) → [`00afa268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa268.md) FUN_00afa268

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afa1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa1cc.md#insn-00afa1e0) · [`00afa1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa1cc.md#insn-00afa1fc)
- 新版 [`00afa27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa268.md#insn-00afa27c) · [`00afa298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa268.md#insn-00afa298)

~~~diff
- 00afa1e0 ["INT_ADD", "register:40f0:8", ["const:afa1e0:8", "const:4:8"]]
- 00afa1e0 ["CALL", null, ["callee:00851550:8"]]
+ 00afa27c ["INT_ADD", "register:40f0:8", ["const:afa27c:8", "const:4:8"]]
+ 00afa27c ["CALL", null, ["callee:00851550:8"]]
- 00afa1e0 bytes c65cf597
+ 00afa27c bytes b55cf597
- 00afa1fc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00afa1fc ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00afa1fc ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:0:8"]]
- 00afa1fc ["INT_ADD", "tmp:2:8", ["register:4040:8", "tmp:1:8"]]
- 00afa1fc bytes 086969b8
+ 00afa298 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00afa298 ["COPY", "tmp:1:8", ["tmp:0:8"]]
+ 00afa298 ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:0:8"]]
+ 00afa298 ["INT_ADD", "tmp:2:8", ["register:4040:8", "tmp:1:8"]]
+ 00afa298 bytes 086969b8
~~~


<a id="compare-bde8683ff29be25c81771fc88f3da471"></a>

### [`00afa214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa214.md) → [`00afa2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa2b0.md) FUN_00afa2b0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa250"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00afa2ec"
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
      "unmatched:00afa248",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa24c",
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
      "00afa2e4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afa2e8",
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

- 旧版 [`00afa250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa214.md#insn-00afa250) · [`00afa228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa214.md#insn-00afa228)
- 新版 [`00afa2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa2b0.md#insn-00afa2ec) · [`00afa2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa2b0.md#insn-00afa2c4)

~~~diff
- 00afa250 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afa250 ["RETURN", null, ["register:0:8"]]
- 00afa250 bytes c0035fd6
+ 00afa2ec ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00afa2ec ["RETURN", null, ["register:0:8"]]
+ 00afa2ec bytes c0035fd6
- 00afa228 ["INT_ADD", "register:40f0:8", ["const:afa228:8", "const:4:8"]]
- 00afa228 ["CALL", null, ["callee:00851550:8"]]
+ 00afa2c4 ["INT_ADD", "register:40f0:8", ["const:afa2c4:8", "const:4:8"]]
+ 00afa2c4 ["CALL", null, ["callee:00851550:8"]]
- 00afa228 bytes b45cf597
+ 00afa2c4 bytes a35cf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2afa9de8f9f25a246c95401b874d1e58"></a>

### [`00afa2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa2a0.md) → [`00afa33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa33c.md) FUN_00afa33c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa2a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa2a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afa340"
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
      "unmatched:00afa2a4",
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
      "00afa340",
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

- 旧版 [`00afa2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa2a0.md#insn-00afa2a4) · [`00afa2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa2a0.md#insn-00afa2a8)
- 新版 [`00afa340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa33c.md#insn-00afa340)

~~~diff
- 00afa2a4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afa2a4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afa2a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afa2a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa2a4 bytes f44f01a9
+ 00afa340 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00afa340 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00afa340 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 00afa340 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00afa340 bytes f44f01a9
- 00afa2a8 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00afa2a8 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-539914e62a2643460e2963e0a3ffa0d6"></a>

### [`00afa2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa2e8.md) → [`00afa384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa384.md) FUN_00afa384

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00713d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/00713d7c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

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
      "site": "00afa2ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa2ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afa388"
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
      "unmatched:00afa2ec",
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
      "00afa388",
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

- 旧版 [`00afa2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa2e8.md#insn-00afa2ec) · [`00afa2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa2e8.md#insn-00afa2f0)
- 新版 [`00afa388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa384.md#insn-00afa388)

~~~diff
- 00afa2ec ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afa2ec ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afa2ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afa2ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa2ec bytes f44f01a9
+ 00afa388 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00afa388 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00afa388 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 00afa388 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00afa388 bytes f44f01a9
- 00afa2f0 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00afa2f0 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c71216b4404a0e1620d1a3038c6e08c"></a>

### [`00afa328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa328.md) → [`00afa3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa3c4.md) FUN_00afa3c4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa328"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa328"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa32c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa328",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa32c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa330",
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
      "00afa3c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afa3c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afa3cc",
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

- 旧版 [`00afa328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa328.md#insn-00afa328) · [`00afa32c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa328.md#insn-00afa32c) · [`00afa330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa328.md#insn-00afa330)

~~~diff
- 00afa328 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afa328 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afa328 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afa328 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afa328 bytes fd7bbda9
- 00afa32c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00afa32c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00afa32c bytes f50b00f9
- 00afa330 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afa330 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afa330 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afa330 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa330 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6fa500cdc05696dabe1c8249d7f90f1"></a>

### [`00afa374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa374.md) → [`00afa410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa410.md) FUN_00afa410

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 36.84% / 新版 36.84%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa374"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa374"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa378"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa374",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa378",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa37c",
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
      "00afa410",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afa414",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afa418",
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

- 旧版 [`00afa374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa374.md#insn-00afa374) · [`00afa378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa374.md#insn-00afa378) · [`00afa37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa374.md#insn-00afa37c)

~~~diff
- 00afa374 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afa374 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afa374 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afa374 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afa374 bytes fd7bbda9
- 00afa378 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00afa378 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00afa378 bytes f50b00f9
- 00afa37c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afa37c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afa37c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afa37c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa37c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6de974e3f2e2deb485e7711a91ff0e0b"></a>

### [`00afa3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa3c0.md) → [`00afa45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa45c.md) FUN_00afa45c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa3c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa3c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa3c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa3c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa3c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa3f4",
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
      "00afa45c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afa460",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afa490",
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

- 旧版 [`00afa3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa3c0.md#insn-00afa3c0) · [`00afa3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa3c0.md#insn-00afa3c4) · [`00afa3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa3c0.md#insn-00afa3fc)

~~~diff
- 00afa3c0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afa3c0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afa3c0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00afa3c0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afa3c0 bytes fd7bbea9
- 00afa3c4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afa3c4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afa3c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afa3c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa3c4 bytes f44f01a9
- 00afa3fc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afa3fc ["RETURN", null, ["register:0:8"]]
- 00afa3fc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaeb3b4ad3af09891fc3099cf5996a22"></a>

### [`00afa400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa400.md) → [`00afa49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa49c.md) FUN_00afa49c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa400"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa400"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa404"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa400",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa404",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa408",
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
      "00afa49c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afa4a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afa4a4",
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

- 旧版 [`00afa400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa400.md#insn-00afa400) · [`00afa404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa400.md#insn-00afa404) · [`00afa408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa400.md#insn-00afa408)

~~~diff
- 00afa400 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afa400 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afa400 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afa400 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afa400 bytes fd7bbda9
- 00afa404 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00afa404 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00afa404 bytes f50b00f9
- 00afa408 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afa408 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afa408 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afa408 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa408 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c6f3e75ec6d52148a8c5d7787a2870f"></a>

### [`00afa44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa44c.md) → [`00afa4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa4e8.md) FUN_00afa4e8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af3554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3554.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00af35f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af35f0.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

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
      "site": "00afa494"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00afa530"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00afa494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa44c.md#insn-00afa494) · [`00afa468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa44c.md#insn-00afa468)
- 新版 [`00afa530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa4e8.md#insn-00afa530) · [`00afa504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa4e8.md#insn-00afa504)

~~~diff
- 00afa494 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afa494 ["RETURN", null, ["register:0:8"]]
- 00afa494 bytes c0035fd6
+ 00afa530 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00afa530 ["RETURN", null, ["register:0:8"]]
+ 00afa530 bytes c0035fd6
- 00afa468 ["INT_ADD", "register:40f0:8", ["const:afa468:8", "const:4:8"]]
- 00afa468 ["CALL", null, ["callee:00851550:8"]]
+ 00afa504 ["INT_ADD", "register:40f0:8", ["const:afa504:8", "const:4:8"]]
+ 00afa504 ["CALL", null, ["callee:00851550:8"]]
- 00afa468 bytes 245cf597
+ 00afa504 bytes 135cf597
~~~


<a id="compare-1ba7a50f9ec306af5239a651a8abed32"></a>

### [`00afa578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa578.md) → [`00afa614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa614.md) FUN_00afa614

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.08% / 新版 73.08%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa578"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa578"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa57c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa578",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa57c",
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
      "00afa614",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afa618",
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

- 旧版 [`00afa578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa578.md#insn-00afa578) · [`00afa57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa578.md#insn-00afa57c)
- 新版 [`00afa614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa614.md#insn-00afa614)

~~~diff
- 00afa578 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afa578 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afa578 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00afa578 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afa578 bytes fd7bbea9
- 00afa57c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afa57c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afa57c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afa57c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa57c bytes f44f01a9
+ 00afa614 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00afa614 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00afa614 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00afa614 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00afa614 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a9b5a73a4ca713f419cdb2b69aefa14"></a>

### [`00afa720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa720.md) → [`00afa7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa7bc.md) FUN_00afa7bc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 25.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa78c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00afa828"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00afa78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa720.md#insn-00afa78c) · [`00afa734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa720.md#insn-00afa734)
- 新版 [`00afa828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa7bc.md#insn-00afa828) · [`00afa7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa7bc.md#insn-00afa7d0)

~~~diff
- 00afa78c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afa78c ["RETURN", null, ["register:0:8"]]
- 00afa78c bytes c0035fd6
+ 00afa828 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00afa828 ["RETURN", null, ["register:0:8"]]
+ 00afa828 bytes c0035fd6
- 00afa734 ["INT_ADD", "register:40f0:8", ["const:afa734:8", "const:4:8"]]
- 00afa734 ["CALL", null, ["callee:00851550:8"]]
+ 00afa7d0 ["INT_ADD", "register:40f0:8", ["const:afa7d0:8", "const:4:8"]]
+ 00afa7d0 ["CALL", null, ["callee:00851550:8"]]
- 00afa734 bytes 715bf597
+ 00afa7d0 bytes 605bf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98a0262dc9c203c6832a00423b268699"></a>

### [`00afa95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa95c.md) → [`00afa9f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa9f8.md) FUN_00afa9f8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa994"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afaa30"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00afa994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa95c.md#insn-00afa994) · [`00afa978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa95c.md#insn-00afa978)
- 新版 [`00afaa30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa9f8.md#insn-00afaa30) · [`00afaa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa9f8.md#insn-00afaa14)

~~~diff
- 00afa994 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00afa994 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00afa994 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00afa994 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00afa994 bytes 136929b8
+ 00afaa30 ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00afaa30 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00afaa30 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00afaa30 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00afaa30 bytes 136929b8
- 00afa978 ["INT_ADD", "register:40f0:8", ["const:afa978:8", "const:4:8"]]
- 00afa978 ["CALL", null, ["callee:00851550:8"]]
+ 00afaa14 ["INT_ADD", "register:40f0:8", ["const:afaa14:8", "const:4:8"]]
+ 00afaa14 ["CALL", null, ["callee:00851550:8"]]
- 00afa978 bytes e05af597
+ 00afaa14 bytes cf5af597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-615cafc46cb5759003a1ed801db2bcf2"></a>

### [`00afa9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa9a8.md) → [`00afaa44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afaa44.md) FUN_00afaa44

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa9a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa9a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa9ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa9a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa9ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa9dc",
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
      "00afaa44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afaa48",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afaa78",
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

- 旧版 [`00afa9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa9a8.md#insn-00afa9a8) · [`00afa9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa9a8.md#insn-00afa9ac) · [`00afa9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa9a8.md#insn-00afa9e4)

~~~diff
- 00afa9a8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afa9a8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afa9a8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00afa9a8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afa9a8 bytes fd7bbea9
- 00afa9ac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afa9ac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afa9ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afa9ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa9ac bytes f44f01a9
- 00afa9e4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afa9e4 ["RETURN", null, ["register:0:8"]]
- 00afa9e4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff00eae1f3836d71efe4a476d4437417"></a>

### [`00afa9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa9e8.md) → [`00afaa84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afaa84.md) FUN_00afaa84

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 52.63% / 新版 52.63%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa9e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa9e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa9ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa9e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa9ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa9f0",
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
      "00afaa84",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afaa88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afaa8c",
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

- 旧版 [`00afa9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa9e8.md#insn-00afa9e8) · [`00afa9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa9e8.md#insn-00afa9ec) · [`00afa9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa9e8.md#insn-00afa9f0)

~~~diff
- 00afa9e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afa9e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afa9e8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afa9e8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afa9e8 bytes fd7bbda9
- 00afa9ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00afa9ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00afa9ec bytes f50b00f9
- 00afa9f0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afa9f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afa9f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afa9f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa9f0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d92bede4a72fd6a950e6a4c9ae3ca28"></a>

### [`00afaa34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaa34.md) → [`00afaad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afaad0.md) FUN_00afaad0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005fb93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb93c.md) [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`005fb97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fb/005fb97c.md) [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 72.22% / 新版 72.22%

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
      "site": "00afaa78"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00afab14"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00afaa78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaa34.md#insn-00afaa78) · [`00afaa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaa34.md#insn-00afaa48)
- 新版 [`00afab14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afaad0.md#insn-00afab14) · [`00afaae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afaad0.md#insn-00afaae4)

~~~diff
- 00afaa78 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afaa78 ["RETURN", null, ["register:0:8"]]
- 00afaa78 bytes c0035fd6
+ 00afab14 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00afab14 ["RETURN", null, ["register:0:8"]]
+ 00afab14 bytes c0035fd6
- 00afaa48 ["INT_ADD", "register:40f0:8", ["const:afaa48:8", "const:4:8"]]
- 00afaa48 ["CALL", null, ["callee:00851550:8"]]
+ 00afaae4 ["INT_ADD", "register:40f0:8", ["const:afaae4:8", "const:4:8"]]
+ 00afaae4 ["CALL", null, ["callee:00851550:8"]]
- 00afaa48 bytes ac5af597
+ 00afaae4 bytes 9b5af597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aec521e8fd90cd17e07e32bbc972715"></a>

### [`00afaa7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaa7c.md) → [`00afab18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afab18.md) FUN_00afab18

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 52.63% / 新版 52.63%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaa7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaa7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaa80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afaa7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afaa80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afaa84",
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
      "00afab18",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afab1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afab20",
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

- 旧版 [`00afaa7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaa7c.md#insn-00afaa7c) · [`00afaa80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaa7c.md#insn-00afaa80) · [`00afaa84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaa7c.md#insn-00afaa84)

~~~diff
- 00afaa7c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afaa7c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afaa7c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afaa7c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afaa7c bytes fd7bbda9
- 00afaa80 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00afaa80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00afaa80 bytes f50b00f9
- 00afaa84 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afaa84 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afaa84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afaa84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afaa84 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78e7575c2c58fda1fd38e01e39366595"></a>

### [`00afaac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaac8.md) → [`00afab64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afab64.md) FUN_00afab64

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005f7940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f7/005f7940.md) [`005fb93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb93c.md) [`00714be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714be8.md) [`00714db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714db8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 4件 [`005f7980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f7/005f7980.md) [`005fb97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fb/005fb97c.md) [`00714c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714c40.md) [`00714e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714e10.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaac8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaac8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaacc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afaac8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afaacc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afab04",
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
      "00afab64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afab68",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afaba0",
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

- 旧版 [`00afaac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaac8.md#insn-00afaac8) · [`00afaacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaac8.md#insn-00afaacc)
- 新版 [`00afab64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afab64.md#insn-00afab64)

~~~diff
- 00afaac8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afaac8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afaac8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00afaac8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afaac8 bytes fd7bbea9
- 00afaacc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afaacc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afaacc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afaacc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afaacc bytes f44f01a9
+ 00afab64 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00afab64 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00afab64 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00afab64 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00afab64 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbaf6c512f918d5921c3a8701d21b481"></a>

### [`00afab5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afab5c.md) → [`00afabf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afabf8.md) FUN_00afabf8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afab70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afab5c.md#insn-00afab70) · [`00afab8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afab5c.md#insn-00afab8c)
- 新版 [`00afac0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afabf8.md#insn-00afac0c) · [`00afac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afabf8.md#insn-00afac28)

~~~diff
- 00afab70 ["INT_ADD", "register:40f0:8", ["const:afab70:8", "const:4:8"]]
- 00afab70 ["CALL", null, ["callee:00851550:8"]]
+ 00afac0c ["INT_ADD", "register:40f0:8", ["const:afac0c:8", "const:4:8"]]
+ 00afac0c ["CALL", null, ["callee:00851550:8"]]
- 00afab70 bytes 625af597
+ 00afac0c bytes 515af597
- 00afab8c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00afab8c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00afab8c ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:0:8"]]
- 00afab8c ["INT_ADD", "tmp:2:8", ["register:4040:8", "tmp:1:8"]]
- 00afab8c bytes 086969b8
+ 00afac28 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00afac28 ["COPY", "tmp:1:8", ["tmp:0:8"]]
+ 00afac28 ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:0:8"]]
+ 00afac28 ["INT_ADD", "tmp:2:8", ["register:4040:8", "tmp:1:8"]]
+ 00afac28 bytes 086969b8
~~~


