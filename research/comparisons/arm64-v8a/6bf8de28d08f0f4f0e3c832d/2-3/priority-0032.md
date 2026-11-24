# v16.0.2 → v16.0.3 · 最優先の変更候補 (32)

[一覧の目次](README.md)

<a id="compare-2c37b76209d23b77053260462338d63a"></a>

### [`0068f630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md) → [`0068f9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068f/0068f9e0.md) FUN_0068f9e0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0069649c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/0069649c.md) [`006987e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006987e0.md) · 呼出先 43件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 2件 [`0069684c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/0069684c.md) [`00698b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698b90.md) · 呼出先 43件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0046de54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de54.md) [`0048a2ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2ac.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.91% / 新版 56.91%

CFGの説明率　旧版 42.99% / 新版 42.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_value` 8件, `unresolved_branch_alignment` 36件, `unresolved_call_alignment` 63件, `unresolved_store_alignment` 49件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0068fa68",
      "incomplete_value": false,
      "site": "0068fa68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068f78c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0068f790"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0068fa68",
      "DATA",
      [
        "storage",
        "00c75350",
        null,
        "undefined *"
      ]
    ],
    [
      "0068fad0",
      "READ",
      [
        "storage",
        "00c75370",
        null,
        "pointer"
      ]
    ],
    [
      "0068fad0",
      "READ",
      [
        "storage",
        "00c75378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0068fa68",
      "DATA",
      [
        "storage",
        "00c76320",
        null,
        "undefined *"
      ]
    ],
    [
      "0068fad0",
      "READ",
      [
        "storage",
        "00c76340",
        null,
        "pointer"
      ]
    ],
    [
      "0068fad0",
      "READ",
      [
        "storage",
        "00c76348",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068f78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md#insn-0068f78c) · [`0068f790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md#insn-0068f790) · [`0068f794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md#insn-0068f794)

~~~diff
- 0068f78c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0068f78c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:b0:8"]]
- 0068f78c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0068f78c bytes e8c30239
- 0068f790 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0068f790 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0068f790 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c6:8"]]
- 0068f790 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0068f790 bytes ff1b0339
- 0068f794 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:1:8"]]
- 0068f794 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0068f794 bytes 0013803c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec9ae75fbe28933939d4199d2e90ec49"></a>

### [`00690740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690740.md) → [`00690af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00690/00690af0.md) FUN_00690af0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00696e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e7c.md) · 呼出先 35件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 1件 [`0069722c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/0069722c.md) · 呼出先 35件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0046de54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de54.md) [`0048a2ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2ac.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 93.30% / 新版 93.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_value` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006907dc"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00690c28",
      "incomplete_value": false,
      "site": "00690c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00690878",
      "incomplete_value": false,
      "site": "00690878",
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
            "const:5d0:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00690ec4",
      "incomplete_value": false,
      "site": "00690ec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00690b14",
      "incomplete_value": false,
      "site": "00690b14",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006907c4",
      "READ",
      [
        "storage",
        "002bb674",
        null,
        "string"
      ]
    ],
    [
      "unmatched:006907dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x1b7]",
        null,
        null
      ]
    ],
    [
      "00690c28",
      "DATA",
      [
        "storage",
        "00c755d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00690b74",
      "READ",
      [
        "storage",
        "002bb752",
        null,
        "string"
      ]
    ],
    [
      "00690b8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1b7]",
        null,
        null
      ]
    ],
    [
      "00690c28",
      "DATA",
      [
        "storage",
        "00c765a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006907dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690740.md#insn-006907dc) · [`00690858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690740.md#insn-00690858) · [`00690868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690740.md#insn-00690868)
- 新版 [`00690c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00690/00690af0.md#insn-00690c08) · [`00690c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00690/00690af0.md#insn-00690c18)

~~~diff
- 006907dc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:49:8"]]
- 006907dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006907dc bytes e093843c
- 00690858 ["INT_ADD", "register:40f0:8", ["const:690858:8", "const:4:8"]]
- 00690858 ["CALL", null, ["callee:0052e060:8"]]
+ 00690c08 ["INT_ADD", "register:40f0:8", ["const:690c08:8", "const:4:8"]]
+ 00690c08 ["CALL", null, ["callee:0052e060:8"]]
- 00690858 bytes 3a75fa97
+ 00690c08 bytes 1675fa97
- 00690868 ["INT_ADD", "register:40f0:8", ["const:690868:8", "const:4:8"]]
- 00690868 ["CALL", null, ["callee:005cd4e0:8"]]
+ 00690c18 ["INT_ADD", "register:40f0:8", ["const:690c18:8", "const:4:8"]]
+ 00690c18 ["CALL", null, ["callee:005cd4e0:8"]]
- 00690868 bytes 32f2fc97
+ 00690c18 bytes 32f2fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-598bea018ab2d9a896228312bc85b7ae"></a>

### [`00690ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690ef8.md) → [`006912a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00691/006912a8.md) FUN_006912a8

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0069649c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/0069649c.md) · 呼出先 37件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md) [`005cd130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md)
- 新版 呼出元 1件 [`0069684c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/0069684c.md) · 呼出先 37件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0046de54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de54.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0052e060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md) [`005cd4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cd4e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.97% / 新版 57.97%

CFGの説明率　旧版 25.81% / 新版 25.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件, `store_condition` 1件, `store_value` 1件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 36件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 35件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00690f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00690f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00690f24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00690f0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00690f24",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00690f4c",
      "READ",
      [
        "storage",
        "002b0e9c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006912bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006912d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "006912fc",
      "READ",
      [
        "storage",
        "002b0f73",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00690f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690ef8.md#insn-00690f0c) · [`00690f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690ef8.md#insn-00690f24) · [`00690f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690ef8.md#insn-00690f58)

~~~diff
- 00690f0c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00690f0c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00690f0c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00690f0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00690f0c bytes f44f05a9
- 00690f24 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00690f24 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00690f24 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00690f24 bytes a8831ef8
- 00690f58 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00690f58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00690f58 bytes e03300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3b4ca75f0ea7e522a970620241667d8"></a>

### [`00691c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691c70.md) → [`00692020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692020.md) FUN_00692020

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00691b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691b24.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00691ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00691/00691ed4.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0069202c",
      "incomplete_value": false,
      "site": "00692030",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
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
      "0069202c",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0069202c",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691c70.md#insn-00691c80) · [`00691c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691c70.md#insn-00691c78) · [`00691c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691c70.md#insn-00691c7c)
- 新版 [`00692030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692020.md#insn-00692030) · [`00692028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692020.md#insn-00692028) · [`0069202c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692020.md#insn-0069202c)

~~~diff
- 00691c80 ["INT_ADD", "register:40f0:8", ["const:691c80:8", "const:4:8"]]
- 00691c80 ["CALL", null, ["callee:0043bad8:8"]]
+ 00692030 ["INT_ADD", "register:40f0:8", ["const:692030:8", "const:4:8"]]
+ 00692030 ["CALL", null, ["callee:0043bad8:8"]]
- 00691c80 bytes cea6f697
+ 00692030 bytes aaa6f697
- 00691c78 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00692028 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00691c78 bytes 20e1ffd0
+ 00692028 bytes 20e1ffd0
- 00691c7c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00691c7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00691c7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00691c7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0069202c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0069202c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0069202c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0069202c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00691c7c bytes 00303e91
+ 0069202c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb732c7895c5d098124e3277f84d0bbb"></a>

### [`00691e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e70.md) → [`00692220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692220.md) FUN_00692220

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00685b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/00685b24.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00685ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/00685ed4.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0069222c",
      "incomplete_value": false,
      "site": "00692230",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
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
      "0069222c",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0069222c",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e70.md#insn-00691e80) · [`00691e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e70.md#insn-00691e78) · [`00691e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e70.md#insn-00691e7c)
- 新版 [`00692230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692220.md#insn-00692230) · [`00692228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692220.md#insn-00692228) · [`0069222c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692220.md#insn-0069222c)

~~~diff
- 00691e80 ["INT_ADD", "register:40f0:8", ["const:691e80:8", "const:4:8"]]
- 00691e80 ["CALL", null, ["callee:0043bad8:8"]]
+ 00692230 ["INT_ADD", "register:40f0:8", ["const:692230:8", "const:4:8"]]
+ 00692230 ["CALL", null, ["callee:0043bad8:8"]]
- 00691e80 bytes 4ea6f697
+ 00692230 bytes 2aa6f697
- 00691e78 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00692228 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00691e78 bytes 20e1ffd0
+ 00692228 bytes 20e1ffd0
- 00691e7c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00691e7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00691e7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00691e7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0069222c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0069222c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0069222c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0069222c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00691e7c bytes 00303e91
+ 0069222c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7dc46129d05f227babbdf7efbaf08c3"></a>

### [`00691e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md) → [`00692234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692234.md) FUN_00692234

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 17件 [`00684f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684f4c.md) [`00685b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/00685b24.md) [`00687668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687668.md) [`00687690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687690.md) [`00687b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687b8c.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 17件 [`006852fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/006852fc.md) [`00685ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/00685ed4.md) [`00687a18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00687/00687a18.md) [`00687a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00687/00687a40.md) [`00687f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00687/00687f3c.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "00692240",
      "incomplete_value": false,
      "site": "00692244",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00692240",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00692240",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md#insn-00691e94) · [`00691e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md#insn-00691e8c) · [`00691e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e84.md#insn-00691e90)
- 新版 [`00692244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692234.md#insn-00692244) · [`0069223c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692234.md#insn-0069223c) · [`00692240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692234.md#insn-00692240)

~~~diff
- 00691e94 ["INT_ADD", "register:40f0:8", ["const:691e94:8", "const:4:8"]]
- 00691e94 ["CALL", null, ["callee:00442c90:8"]]
+ 00692244 ["INT_ADD", "register:40f0:8", ["const:692244:8", "const:4:8"]]
+ 00692244 ["CALL", null, ["callee:00442c90:8"]]
- 00691e94 bytes b7c2f697
+ 00692244 bytes 93c2f697
- 00691e8c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0069223c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00691e8c bytes 20e1ffd0
+ 0069223c bytes 20e1ffd0
- 00691e90 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00691e90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00691e90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00691e90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00692240 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00692240 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00692240 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00692240 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00691e90 bytes 00303e91
+ 00692240 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b9350fa36650e023c8a1b2eb531bc61"></a>

### [`00691e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e98.md) → [`00692248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692248.md) FUN_00692248

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00686030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00686/00686030.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`006863e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00686/006863e0.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00692254",
      "incomplete_value": false,
      "site": "00692258",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00692254",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00692254",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e98.md#insn-00691ea8) · [`00691ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e98.md#insn-00691ea0) · [`00691ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691e98.md#insn-00691ea4)
- 新版 [`00692258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692248.md#insn-00692258) · [`00692250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692248.md#insn-00692250) · [`00692254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692248.md#insn-00692254)

~~~diff
- 00691ea8 ["INT_ADD", "register:40f0:8", ["const:691ea8:8", "const:4:8"]]
- 00691ea8 ["CALL", null, ["callee:0043bad8:8"]]
+ 00692258 ["INT_ADD", "register:40f0:8", ["const:692258:8", "const:4:8"]]
+ 00692258 ["CALL", null, ["callee:0043bad8:8"]]
- 00691ea8 bytes 44a6f697
+ 00692258 bytes 20a6f697
- 00691ea0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00692250 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00691ea0 bytes 20e1ffd0
+ 00692250 bytes 20e1ffd0
- 00691ea4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00691ea4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00691ea4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00691ea4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00692254 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00692254 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00692254 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00692254 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00691ea4 bytes 00303e91
+ 00692254 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f09b2212f327cb5d00b9bf332d421f6"></a>

### [`00691eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691eac.md) → [`0069225c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/0069225c.md) FUN_0069225c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`00684e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684e7c.md) [`00684ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684ec4.md) [`00684f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684f18.md) [`00684ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684ff0.md) [`00686030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00686/00686030.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 7件 [`0068522c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/0068522c.md) [`00685274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/00685274.md) [`006852c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/006852c8.md) [`006853a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/006853a0.md) [`006863e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00686/006863e0.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "00692268",
      "incomplete_value": false,
      "site": "0069226c",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00692268",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00692268",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691eac.md#insn-00691ebc) · [`00691eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691eac.md#insn-00691eb4) · [`00691eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691eac.md#insn-00691eb8)
- 新版 [`0069226c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/0069225c.md#insn-0069226c) · [`00692264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/0069225c.md#insn-00692264) · [`00692268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/0069225c.md#insn-00692268)

~~~diff
- 00691ebc ["INT_ADD", "register:40f0:8", ["const:691ebc:8", "const:4:8"]]
- 00691ebc ["CALL", null, ["callee:00442c90:8"]]
+ 0069226c ["INT_ADD", "register:40f0:8", ["const:69226c:8", "const:4:8"]]
+ 0069226c ["CALL", null, ["callee:00442c90:8"]]
- 00691ebc bytes adc2f697
+ 0069226c bytes 89c2f697
- 00691eb4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00692264 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00691eb4 bytes 20e1ffd0
+ 00692264 bytes 20e1ffd0
- 00691eb8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00691eb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00691eb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00691eb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00692268 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00692268 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00692268 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00692268 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00691eb8 bytes 00303e91
+ 00692268 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4aa9e113d95d114dbeeba64abdce532c"></a>

### [`00692060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692060.md) → [`00692410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692410.md) FUN_00692410

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00691ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691ec0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00692270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692270.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0069241c",
      "incomplete_value": false,
      "site": "00692420",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
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
      "0069241c",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0069241c",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00692070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692060.md#insn-00692070) · [`00692068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692060.md#insn-00692068) · [`0069206c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692060.md#insn-0069206c)
- 新版 [`00692420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692410.md#insn-00692420) · [`00692418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692410.md#insn-00692418) · [`0069241c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692410.md#insn-0069241c)

~~~diff
- 00692070 ["INT_ADD", "register:40f0:8", ["const:692070:8", "const:4:8"]]
- 00692070 ["CALL", null, ["callee:0043bad8:8"]]
+ 00692420 ["INT_ADD", "register:40f0:8", ["const:692420:8", "const:4:8"]]
+ 00692420 ["CALL", null, ["callee:0043bad8:8"]]
- 00692070 bytes d2a5f697
+ 00692420 bytes aea5f697
- 00692068 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00692418 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00692068 bytes 20e1ffb0
+ 00692418 bytes 20e1ffd0
- 0069206c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0069206c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0069206c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0069206c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0069241c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0069241c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0069241c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0069241c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0069206c bytes 00303e91
+ 0069241c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3e4dca4c242c8898665880c2b2e03b4"></a>

### [`00692074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692074.md) → [`00692424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692424.md) FUN_00692424

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00686ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00686/00686ab8.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0069229c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069229c.md) [`00692474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692474.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00686e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00686/00686e68.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0069264c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/0069264c.md) [`00692824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692824.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.47% / 新版 91.47%

CFGの説明率　旧版 66.67% / 新版 63.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00692548"
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
      "unmatched:00692198",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00692228",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692648"
      ]
    ]
  ],
  "added": [
    [
      "00692548",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "006925d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692648"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069210c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692074.md#insn-0069210c) · [`00692114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692074.md#insn-00692114) · [`00692198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692074.md#insn-00692198)

~~~diff
- 0069210c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0069210c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0069210c ["COPY", "tmp:2:8", ["register:4058:8"]]
- 0069210c ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 0069210c bytes 6981899a
- 00692114 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00692114 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00692114 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00692114 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00692114 bytes 3631889a
- 00692198 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00692198 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00692198 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00692198 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00692198 bytes e92301a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43449670f73689a5db20a37dd0e2021d"></a>

### [`0069229c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069229c.md) → [`0069264c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/0069264c.md) FUN_0069264c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00692074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692074.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00692424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692424.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 45.83% / 新版 45.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692314"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692398"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006922cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692738"
      ]
    ]
  ],
  "added": [
    [
      "0069267c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006922cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069229c.md#insn-006922cc) · [`00692310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069229c.md#insn-00692310) · [`00692314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069229c.md#insn-00692314)

~~~diff
- 006922cc ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 006922cc bytes e0050054
- 00692310 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:40:8"]]
- 00692310 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00692310 bytes 2a2100f9
- 00692314 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 00692314 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00692314 bytes 200d803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f1044e2c4a7f17ae79b598a877c9b1a"></a>

### [`006923d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/006923d4.md) → [`00692784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692784.md) FUN_00692784

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 75.00% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006927d0",
      "incomplete_value": true,
      "site": "006927d4",
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
    "old": null,
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00692424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/006923d4.md#insn-00692424) · [`006923f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/006923d4.md#insn-006923f8) · [`00692410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/006923d4.md#insn-00692410)
- 新版 [`006927d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692784.md#insn-006927d4) · [`006927a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692784.md#insn-006927a8) · [`006927c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692784.md#insn-006927c0)

~~~diff
- 00692424 ["INT_ADD", "register:40f0:8", ["const:692424:8", "const:4:8"]]
- 00692424 ["CALL", null, ["callee:00c58f50:8"]]
+ 006927d4 ["INT_ADD", "register:40f0:8", ["const:6927d4:8", "const:4:8"]]
+ 006927d4 ["CALL", null, ["callee:00c58f50:8"]]
- 00692424 bytes d7161794
+ 006927d4 bytes df191794
- 006923f8 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
+ 006927a8 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 006923f8 bytes a0020054
+ 006927a8 bytes a0020054
- 00692410 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00692410 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00692410 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00692410 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 006927c0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 006927c0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 006927c0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 006927c0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00692410 bytes 08010037
+ 006927c0 bytes 08010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9036adf161d4a7454d74c9d3212b38be"></a>

### [`00692474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692474.md) → [`00692824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692824.md) FUN_00692824

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00692074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692074.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00692424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692424.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00692830",
      "incomplete_value": false,
      "site": "00692834",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00692830",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00692830",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00692484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692474.md#insn-00692484) · [`0069247c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692474.md#insn-0069247c) · [`00692480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692474.md#insn-00692480)
- 新版 [`00692834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692824.md#insn-00692834) · [`0069282c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692824.md#insn-0069282c) · [`00692830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692824.md#insn-00692830)

~~~diff
- 00692484 ["INT_ADD", "register:40f0:8", ["const:692484:8", "const:4:8"]]
- 00692484 ["CALL", null, ["callee:0043bad8:8"]]
+ 00692834 ["INT_ADD", "register:40f0:8", ["const:692834:8", "const:4:8"]]
+ 00692834 ["CALL", null, ["callee:0043bad8:8"]]
- 00692484 bytes cda4f697
+ 00692834 bytes a9a4f697
- 0069247c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0069282c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0069247c bytes 20e1ffb0
+ 0069282c bytes 20e1ffd0
- 00692480 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00692480 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00692480 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00692480 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00692830 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00692830 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00692830 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00692830 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00692480 bytes 00303e91
+ 00692830 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-011b875d7db9a0fc07de7ba3fa8261a9"></a>

### [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) → [`006928cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928cc.md) FUN_006928cc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 11件 [`00687944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687944.md) [`0068e7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068e7ac.md) [`0068f630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md) [`00694d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d80.md) [`00694e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694e38.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 11件 [`00687cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00687/00687cf4.md) [`0068eb5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068e/0068eb5c.md) [`0068f9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068f/0068f9e0.md) [`00695130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695130.md) [`006951e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/006951e8.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "006928d8",
      "incomplete_value": false,
      "site": "006928dc",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
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
      "006928d8",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006928d8",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md#insn-0069252c) · [`00692524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md#insn-00692524) · [`00692528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md#insn-00692528)
- 新版 [`006928dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928cc.md#insn-006928dc) · [`006928d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928cc.md#insn-006928d4) · [`006928d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928cc.md#insn-006928d8)

~~~diff
- 0069252c ["INT_ADD", "register:40f0:8", ["const:69252c:8", "const:4:8"]]
- 0069252c ["CALL", null, ["callee:0043bad8:8"]]
+ 006928dc ["INT_ADD", "register:40f0:8", ["const:6928dc:8", "const:4:8"]]
+ 006928dc ["CALL", null, ["callee:0043bad8:8"]]
- 0069252c bytes a3a4f697
+ 006928dc bytes 7fa4f697
- 00692524 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 006928d4 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00692524 bytes 20e1ffb0
+ 006928d4 bytes 20e1ffd0
- 00692528 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00692528 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00692528 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00692528 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006928d8 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 006928d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006928d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006928d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00692528 bytes 00303e91
+ 006928d8 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0ceb38d9d30ad4a765f3b84de8f2502"></a>

### [`00692530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692530.md) → [`006928e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928e0.md) FUN_006928e0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00684ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684ff0.md) [`00685288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/00685288.md) [`006853b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/006853b4.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 3件 [`006853a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/006853a0.md) [`00685638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/00685638.md) [`00685764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/00685764.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "006928ec",
      "incomplete_value": false,
      "site": "006928f0",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
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
      "006928ec",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006928ec",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00692540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692530.md#insn-00692540) · [`00692538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692530.md#insn-00692538) · [`0069253c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692530.md#insn-0069253c)
- 新版 [`006928f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928e0.md#insn-006928f0) · [`006928e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928e0.md#insn-006928e8) · [`006928ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928e0.md#insn-006928ec)

~~~diff
- 00692540 ["INT_ADD", "register:40f0:8", ["const:692540:8", "const:4:8"]]
- 00692540 ["CALL", null, ["callee:00442c90:8"]]
+ 006928f0 ["INT_ADD", "register:40f0:8", ["const:6928f0:8", "const:4:8"]]
+ 006928f0 ["CALL", null, ["callee:00442c90:8"]]
- 00692540 bytes 0cc1f697
+ 006928f0 bytes e8c0f697
- 00692538 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 006928e8 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00692538 bytes 20e1ffb0
+ 006928e8 bytes 20e1ffd0
- 0069253c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0069253c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0069253c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0069253c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006928ec ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 006928ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006928ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006928ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0069253c bytes 00303e91
+ 006928ec bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04a25a822cc02c1b72f41fe728b65038"></a>

### [`00692544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692544.md) → [`006928f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928f4.md) FUN_006928f4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00684ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684ff0.md) [`00685320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/00685320.md) [`006853b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/006853b4.md) [`0068a71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a71c.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 4件 [`006853a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/006853a0.md) [`006856d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/006856d0.md) [`00685764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/00685764.md) [`0068aacc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068a/0068aacc.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "00692900",
      "incomplete_value": false,
      "site": "00692904",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00692900",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00692900",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00692554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692544.md#insn-00692554) · [`0069254c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692544.md#insn-0069254c) · [`00692550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692544.md#insn-00692550)
- 新版 [`00692904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928f4.md#insn-00692904) · [`006928fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928f4.md#insn-006928fc) · [`00692900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928f4.md#insn-00692900)

~~~diff
- 00692554 ["INT_ADD", "register:40f0:8", ["const:692554:8", "const:4:8"]]
- 00692554 ["CALL", null, ["callee:00442c90:8"]]
+ 00692904 ["INT_ADD", "register:40f0:8", ["const:692904:8", "const:4:8"]]
+ 00692904 ["CALL", null, ["callee:00442c90:8"]]
- 00692554 bytes 07c1f697
+ 00692904 bytes e3c0f697
- 0069254c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 006928fc ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0069254c bytes 20e1ffb0
+ 006928fc bytes 20e1ffd0
- 00692550 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00692550 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00692550 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00692550 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00692900 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00692900 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00692900 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00692900 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00692550 bytes 00303e91
+ 00692900 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57ae904778a538cd76eb93e90c838ba1"></a>

### [`00692558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692558.md) → [`00692908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692908.md) FUN_00692908

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0068a310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a310.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0068a6c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068a/0068a6c0.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00692914",
      "incomplete_value": false,
      "site": "00692918",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00692914",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00692914",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00692568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692558.md#insn-00692568) · [`00692560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692558.md#insn-00692560) · [`00692564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692558.md#insn-00692564)
- 新版 [`00692918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692908.md#insn-00692918) · [`00692910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692908.md#insn-00692910) · [`00692914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692908.md#insn-00692914)

~~~diff
- 00692568 ["INT_ADD", "register:40f0:8", ["const:692568:8", "const:4:8"]]
- 00692568 ["CALL", null, ["callee:0043bad8:8"]]
+ 00692918 ["INT_ADD", "register:40f0:8", ["const:692918:8", "const:4:8"]]
+ 00692918 ["CALL", null, ["callee:0043bad8:8"]]
- 00692568 bytes 94a4f697
+ 00692918 bytes 70a4f697
- 00692560 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00692910 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00692560 bytes 20e1ffb0
+ 00692910 bytes 20e1ffd0
- 00692564 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00692564 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00692564 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00692564 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00692914 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00692914 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00692914 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00692914 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00692564 bytes 00303e91
+ 00692914 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ef74d26abeed1fbcc306ee929c3d663"></a>

### [`0069256c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069256c.md) → [`0069291c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/0069291c.md) FUN_0069291c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0068a310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a310.md) [`0069256c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069256c.md) [`0069290c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069290c.md) · 呼出先 4件 [`0069256c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069256c.md) [`0069290c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069290c.md) [`00692c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692c30.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 3件 [`0068a6c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068a/0068a6c0.md) [`0069291c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/0069291c.md) [`00692cbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692cbc.md) · 呼出先 4件 [`0069291c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/0069291c.md) [`00692cbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692cbc.md) [`00692fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692fe0.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.78% / 新版 85.78%

CFGの説明率　旧版 53.23% / 新版 52.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 4件, `unresolved_branch_alignment` 9件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069262c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692630"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692674"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00692608",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692950"
      ]
    ],
    [
      "unmatched:006928c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692c54"
      ]
    ],
    [
      "unmatched:00692900",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692c8c"
      ]
    ]
  ],
  "added": [
    [
      "006929b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692950"
      ]
    ],
    [
      "00692c78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692c54"
      ]
    ],
    [
      "00692cb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692c8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006925f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069256c.md#insn-006925f4) · [`006925f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069256c.md#insn-006925f8) · [`00692608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069256c.md#insn-00692608)

~~~diff
- 006925f4 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 006925f4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 006925f4 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 006925f4 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 006925f4 bytes a8018b9a
- 006925f8 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 006925f8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 006925f8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 006925f8 ["COPY", "register:4048:8", ["tmp:0:8"]]
- 006925f8 bytes 89018a9a
- 00692608 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00692608 ["CBRANCH", null, ["local:b1:8", "tmp:0:1"]]
- 00692608 bytes cafcff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da347f9e2fd19efe25ecc7ae0ca8074e"></a>

### [`00692c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692c30.md) → [`00692fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692fe0.md) FUN_00692fe0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0069256c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069256c.md) [`00692c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692c30.md) · 呼出先 4件 [`00692c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692c30.md) [`0069314c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/0069314c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 2件 [`0069291c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/0069291c.md) [`00692fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692fe0.md) · 呼出先 4件 [`00692fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692fe0.md) [`006934fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/006934fc.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.77% / 新版 87.77%

CFGの説明率　旧版 59.49% / 新版 56.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 10件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692f44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692f48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00692f48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00692e1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069318c"
      ]
    ],
    [
      "unmatched:00692f4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006932d8"
      ]
    ],
    [
      "unmatched:00693028",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006934b8"
      ]
    ]
  ],
  "added": [
    [
      "006931cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069318c"
      ]
    ],
    [
      "006932fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006932d8"
      ]
    ],
    [
      "006933d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006934b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00692df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692c30.md#insn-00692df8) · [`00692dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692c30.md#insn-00692dfc) · [`00692e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692c30.md#insn-00692e14)

~~~diff
- 00692df8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00692df8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00692df8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00692df8 ["COPY", "register:4070:8", ["tmp:0:8"]]
- 00692df8 bytes 6e018a9a
- 00692dfc ["COPY", "tmp:0:8", ["register:4080:8"]]
- 00692dfc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00692dfc ["COPY", "tmp:0:8", ["register:4078:8"]]
- 00692dfc ["COPY", "register:4078:8", ["tmp:0:8"]]
- 00692dfc bytes 0f028f9a
- 00692e14 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00692e14 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00692e14 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00692e14 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00692e14 bytes 29b18c9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e654765545d46d17c4abb46585196f4"></a>

### [`0069314c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/0069314c.md) → [`006934fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/006934fc.md) FUN_006934fc

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00692c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692c30.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00692fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/00692fe0.md) · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 29.27% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006931e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006931f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006931f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00693188",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006935d8"
      ]
    ],
    [
      "unmatched:006931c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00693674"
      ]
    ],
    [
      "unmatched:00693204",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006935c8"
      ]
    ]
  ],
  "added": [
    [
      "00693538",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006935d8"
      ]
    ],
    [
      "00693574",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00693674"
      ]
    ],
    [
      "006935b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006935c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006931e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/0069314c.md#insn-006931e8) · [`006931f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/0069314c.md#insn-006931f0) · [`006931f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/0069314c.md#insn-006931f4)

~~~diff
- 006931e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ffffffffffffffdc:8"]]
- 006931e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006931e8 bytes 00c19d3c
- 006931f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ffffffffffffffec:8"]]
- 006931f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 006931f0 bytes 01c19e3c
- 006931f4 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 006931f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:fffffffffffffffc:8"]]
- 006931f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 006931f4 bytes 0ac11fb8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86fdb6b79e1823e4ea6f8226d8c0160a"></a>

### [`006933e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006933e0.md) → [`00693790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693790.md) FUN_00693790

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068bb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068bb28.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0068bed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068b/0068bed8.md)

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
      "site": "006937b0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00693400",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "006937bc",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0069340c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "006937b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006937bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006937b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006937bc",
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

- 旧版 [`00693400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006933e0.md#insn-00693400) · [`0069340c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006933e0.md#insn-0069340c)
- 新版 [`006937b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693790.md#insn-006937b0) · [`006937bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693790.md#insn-006937bc)

~~~diff
- 00693400 ["INT_ADD", "register:40f0:8", ["const:693400:8", "const:4:8"]]
- 00693400 ["CALL", null, ["ram:47ad34:8"]]
+ 006937b0 ["INT_ADD", "register:40f0:8", ["const:6937b0:8", "const:4:8"]]
+ 006937b0 ["CALL", null, ["ram:47b054:8"]]
- 00693400 bytes 4d9ef797
+ 006937b0 bytes 299ef797
- 0069340c ["INT_ADD", "register:40f0:8", ["const:69340c:8", "const:4:8"]]
- 0069340c ["CALL", null, ["ram:47ad34:8"]]
+ 006937bc ["INT_ADD", "register:40f0:8", ["const:6937bc:8", "const:4:8"]]
+ 006937bc ["CALL", null, ["ram:47b054:8"]]
- 0069340c bytes 4a9ef797
+ 006937bc bytes 269ef797
~~~


<a id="compare-004ab7cceb24fd062d8c5767bda52fee"></a>

### [`00693460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693460.md) → [`00693810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693810.md) FUN_00693810

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00693834",
      "incomplete_value": false,
      "site": "00693834",
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
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00693484",
      "incomplete_value": false,
      "site": "00693484",
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
      "00693834",
      "DATA",
      [
        "storage",
        "00c749a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00693834",
      "DATA",
      [
        "storage",
        "00c75970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00693468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693460.md#insn-00693468) · [`00693474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693460.md#insn-00693474) · [`0069347c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693460.md#insn-0069347c)
- 新版 [`00693824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693810.md#insn-00693824) · [`0069382c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693810.md#insn-0069382c)

~~~diff
- 00693468 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00693468 bytes fd030091
- 00693474 ["INT_ADD", "register:40f0:8", ["const:693474:8", "const:4:8"]]
- 00693474 ["CALL", null, ["callee:00c58f30:8"]]
+ 00693824 ["INT_ADD", "register:40f0:8", ["const:693824:8", "const:4:8"]]
+ 00693824 ["CALL", null, ["callee:00c58f30:8"]]
- 00693474 bytes bb121794
+ 00693824 bytes c3151794
- 0069347c ["COPY", "register:4040:8", ["const:c74000:8"]]
+ 0069382c ["COPY", "register:4040:8", ["const:c75000:8"]]
- 0069347c bytes 082f00b0
+ 0069382c bytes 082f00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa80c5959325ecf6d878e6b32e0eb3e5"></a>

### [`006934b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006934b0.md) → [`00693860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693860.md) FUN_00693860

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 15件 [`004709d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004709d4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0068bb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068bb28.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00470cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470cf4.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0068bed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068b/0068bed8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.66% / 新版 74.66%

CFGの説明率　旧版 30.56% / 新版 26.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006934cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069361c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00693620"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006934cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00693890",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00693504"
      ]
    ],
    [
      "unmatched:006934e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "0069387c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00693890",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006938b4"
      ]
    ],
    [
      "00693898",
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

- 旧版 [`006934cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006934b0.md#insn-006934cc) · [`006934e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006934b0.md#insn-006934e8) · [`006934f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006934b0.md#insn-006934f8)

~~~diff
- 006934cc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006934cc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 006934cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 006934cc bytes a8831ff8
- 006934e8 ["INT_ADD", "register:40f0:8", ["const:6934e8:8", "const:4:8"]]
- 006934e8 ["CALL", null, ["ram:47ad34:8"]]
- 006934e8 bytes 139ef797
- 006934f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006934f8 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 006934f8 bytes e1120054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-977a13fda37fa29a6e23f790c6ef32ce"></a>

### [`006937b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006937b4.md) → [`00693b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693b64.md) FUN_00693b64

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00693b88",
      "incomplete_value": false,
      "site": "00693b88",
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
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00693b88",
      "DATA",
      [
        "storage",
        "00c74a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00693b88",
      "DATA",
      [
        "storage",
        "00c759e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006937c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006937b4.md#insn-006937c8) · [`006937d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006937b4.md#insn-006937d0) · [`006937d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006937b4.md#insn-006937d4)
- 新版 [`00693b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693b64.md#insn-00693b78) · [`00693b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693b64.md#insn-00693b80) · [`00693b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693b64.md#insn-00693b84)

~~~diff
- 006937c8 ["INT_ADD", "register:40f0:8", ["const:6937c8:8", "const:4:8"]]
- 006937c8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00693b78 ["INT_ADD", "register:40f0:8", ["const:693b78:8", "const:4:8"]]
+ 00693b78 ["CALL", null, ["callee:00c58f30:8"]]
- 006937c8 bytes e6111794
+ 00693b78 bytes ee141794
- 006937d0 ["COPY", "register:4040:8", ["const:c74000:8"]]
+ 00693b80 ["COPY", "register:4040:8", ["const:c75000:8"]]
- 006937d0 bytes 082f00b0
+ 00693b80 bytes 082f00d0
- 006937d4 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 006937d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006937d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006937d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00693b84 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00693b84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00693b84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00693b84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006937d4 bytes 08412891
+ 00693b84 bytes 08812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9404f60fe68de08ee95a0c633b63b045"></a>

### [`00693804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693804.md) → [`00693bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693bb4.md) FUN_00693bb4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

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
      "site": "00693bd0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00693820",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "00693bd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00693bd0",
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

- 旧版 [`00693820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693804.md#insn-00693820) · [`0069382c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693804.md#insn-0069382c)
- 新版 [`00693bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693bb4.md#insn-00693bd0) · [`00693bdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693bb4.md#insn-00693bdc)

~~~diff
- 00693820 ["INT_ADD", "register:40f0:8", ["const:693820:8", "const:4:8"]]
- 00693820 ["CALL", null, ["ram:47ad34:8"]]
+ 00693bd0 ["INT_ADD", "register:40f0:8", ["const:693bd0:8", "const:4:8"]]
+ 00693bd0 ["CALL", null, ["ram:47b054:8"]]
- 00693820 bytes 459df797
+ 00693bd0 bytes 219df797
- 0069382c ["INT_ADD", "register:40f0:8", ["const:69382c:8", "const:4:8"]]
- 0069382c ["CALL", null, ["callee:0047d134:8"]]
+ 00693bdc ["INT_ADD", "register:40f0:8", ["const:693bdc:8", "const:4:8"]]
+ 00693bdc ["CALL", null, ["callee:0047d134:8"]]
- 0069382c bytes 7aa5f797
+ 00693bdc bytes 56a5f797
~~~


<a id="compare-dab6cfa8acc6be07ad093e4e66dae46d"></a>

### [`00693870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693870.md) → [`00693c20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693c20.md) FUN_00693c20

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00693c44",
      "incomplete_value": false,
      "site": "00693c44",
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
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00693c44",
      "DATA",
      [
        "storage",
        "00c74aa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00693c44",
      "DATA",
      [
        "storage",
        "00c75a70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00693884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693870.md#insn-00693884) · [`0069388c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693870.md#insn-0069388c) · [`00693890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693870.md#insn-00693890)
- 新版 [`00693c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693c20.md#insn-00693c34) · [`00693c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693c20.md#insn-00693c3c) · [`00693c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693c20.md#insn-00693c40)

~~~diff
- 00693884 ["INT_ADD", "register:40f0:8", ["const:693884:8", "const:4:8"]]
- 00693884 ["CALL", null, ["callee:00c58f30:8"]]
+ 00693c34 ["INT_ADD", "register:40f0:8", ["const:693c34:8", "const:4:8"]]
+ 00693c34 ["CALL", null, ["callee:00c58f30:8"]]
- 00693884 bytes b7111794
+ 00693c34 bytes bf141794
- 0069388c ["COPY", "register:4040:8", ["const:c74000:8"]]
+ 00693c3c ["COPY", "register:4040:8", ["const:c75000:8"]]
- 0069388c bytes 082f00b0
+ 00693c3c bytes 082f00d0
- 00693890 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00693890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00693890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00693890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00693c40 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 00693c40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00693c40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00693c40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00693890 bytes 08812a91
+ 00693c40 bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba4489b15ad8e42a4fefe1b736b2790d"></a>

### [`006938c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006938c0.md) → [`00693c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693c70.md) FUN_00693c70

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068aa04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068aa04.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0068adb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068a/0068adb4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md)

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
      "site": "00693c98",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006938e8",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "00693ca8",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006938f8",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "00693c98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00693ca8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00693c98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00693ca8",
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

- 旧版 [`006938e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006938c0.md#insn-006938e8) · [`006938f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006938c0.md#insn-006938f8) · [`00693918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006938c0.md#insn-00693918)
- 新版 [`00693c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693c70.md#insn-00693c98) · [`00693ca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693c70.md#insn-00693ca8) · [`00693cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693c70.md#insn-00693cc8)

~~~diff
- 006938e8 ["INT_ADD", "register:40f0:8", ["const:6938e8:8", "const:4:8"]]
- 006938e8 ["CALL", null, ["ram:47ad34:8"]]
+ 00693c98 ["INT_ADD", "register:40f0:8", ["const:693c98:8", "const:4:8"]]
+ 00693c98 ["CALL", null, ["ram:47b054:8"]]
- 006938e8 bytes 139df797
+ 00693c98 bytes ef9cf797
- 006938f8 ["INT_ADD", "register:40f0:8", ["const:6938f8:8", "const:4:8"]]
- 006938f8 ["CALL", null, ["ram:47ad34:8"]]
+ 00693ca8 ["INT_ADD", "register:40f0:8", ["const:693ca8:8", "const:4:8"]]
+ 00693ca8 ["CALL", null, ["ram:47b054:8"]]
- 006938f8 bytes 0f9df797
+ 00693ca8 bytes eb9cf797
- 00693918 ["INT_ADD", "register:40f0:8", ["const:693918:8", "const:4:8"]]
- 00693918 ["CALL", null, ["callee:0068adb4:8"]]
+ 00693cc8 ["INT_ADD", "register:40f0:8", ["const:693cc8:8", "const:4:8"]]
+ 00693cc8 ["CALL", null, ["callee:0068adb4:8"]]
- 00693918 bytes 3bdcff97
+ 00693cc8 bytes 3bdcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bb5e5f2bfcf89f96a2b9a680ee7842a"></a>

### [`006939a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006939a4.md) → [`00693d54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693d54.md) FUN_00693d54

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00693d78",
      "incomplete_value": false,
      "site": "00693d80",
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
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00693d80",
      "DATA",
      [
        "storage",
        "00c74b20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00693d80",
      "DATA",
      [
        "storage",
        "00c75af0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006939b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006939a4.md#insn-006939b8) · [`006939c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006939a4.md#insn-006939c4) · [`006939c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006939a4.md#insn-006939c8)
- 新版 [`00693d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693d54.md#insn-00693d68) · [`00693d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693d54.md#insn-00693d74) · [`00693d78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693d54.md#insn-00693d78)

~~~diff
- 006939b8 ["INT_ADD", "register:40f0:8", ["const:6939b8:8", "const:4:8"]]
- 006939b8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00693d68 ["INT_ADD", "register:40f0:8", ["const:693d68:8", "const:4:8"]]
+ 00693d68 ["CALL", null, ["callee:00c58f30:8"]]
- 006939b8 bytes 6a111794
+ 00693d68 bytes 72141794
- 006939c4 ["COPY", "register:4040:8", ["const:c74000:8"]]
+ 00693d74 ["COPY", "register:4040:8", ["const:c75000:8"]]
- 006939c4 bytes 082f00b0
+ 00693d74 bytes 082f00d0
- 006939c8 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 006939c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006939c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006939c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00693d78 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00693d78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00693d78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00693d78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006939c8 bytes 08812c91
+ 00693d78 bytes 08c12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5a303e66a0cbd673a47501179c39938"></a>

### [`00693a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693a1c.md) → [`00693dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693dcc.md) FUN_00693dcc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 97.50% / 新版 95.12%

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
      "site": "00693e78",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00693ac8",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "00693ea0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00693af0",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "00693e78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00693ea0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00693e78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00693ea0",
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

- 旧版 [`00693ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693a1c.md#insn-00693ac8) · [`00693af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693a1c.md#insn-00693af0) · [`00693a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693a1c.md#insn-00693a58)
- 新版 [`00693e78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693dcc.md#insn-00693e78) · [`00693ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693dcc.md#insn-00693ea0) · [`00693e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00693/00693dcc.md#insn-00693e08)

~~~diff
- 00693ac8 ["INT_ADD", "register:40f0:8", ["const:693ac8:8", "const:4:8"]]
- 00693ac8 ["CALL", null, ["ram:47ad34:8"]]
+ 00693e78 ["INT_ADD", "register:40f0:8", ["const:693e78:8", "const:4:8"]]
+ 00693e78 ["CALL", null, ["ram:47b054:8"]]
- 00693ac8 bytes 9b9cf797
+ 00693e78 bytes 779cf797
- 00693af0 ["INT_ADD", "register:40f0:8", ["const:693af0:8", "const:4:8"]]
- 00693af0 ["CALL", null, ["ram:47ad34:8"]]
+ 00693ea0 ["INT_ADD", "register:40f0:8", ["const:693ea0:8", "const:4:8"]]
+ 00693ea0 ["CALL", null, ["ram:47b054:8"]]
- 00693af0 bytes 919cf797
+ 00693ea0 bytes 6d9cf797
- 00693a58 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00693a58 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
+ 00693e08 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00693e08 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 00693a58 bytes a1100054
+ 00693e08 bytes a1100054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51f1c80fd7c3c0ad85b05497748c9fd4"></a>

### [`00693d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693d10.md) → [`006940c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/006940c0.md) FUN_006940c0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068bb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068bb28.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0068bed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068b/0068bed8.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 30.00% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00693d28"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006940d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006940e0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00693d30",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "unmatched:00693d28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00693d3c"
      ]
    ],
    [
      "006940e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:00693d3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006940d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006940ec"
      ]
    ],
    [
      "006940e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006940ec",
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

- 旧版 [`00693d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693d10.md#insn-00693d28) · [`00693d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693d10.md#insn-00693d30) · [`00693d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693d10.md#insn-00693d3c)
- 新版 [`006940e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/006940c0.md#insn-006940e0)

~~~diff
- 00693d28 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00693d28 bytes a0000054
- 00693d30 ["INT_ADD", "register:40f0:8", ["const:693d30:8", "const:4:8"]]
- 00693d30 ["CALL", null, ["ram:47ad34:8"]]
+ 006940e0 ["INT_ADD", "register:40f0:8", ["const:6940e0:8", "const:4:8"]]
+ 006940e0 ["CALL", null, ["ram:47b054:8"]]
- 00693d30 bytes 019cf797
+ 006940e0 bytes dd9bf797
- 00693d3c ["INT_ADD", "register:40f0:8", ["const:693d3c:8", "const:4:8"]]
- 00693d3c ["CALL", null, ["ram:47ad34:8"]]
- 00693d3c bytes fe9bf797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24eb67d190adf45241d4051e4652611d"></a>

### [`006943f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006943f4.md) → [`006947a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/006947a4.md) FUN_006947a4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068aa04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068aa04.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0068adb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068a/0068adb4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 66.67% / 新版 76.92%

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
      "site": "006947cc",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0069441c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "006947dc",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0069442c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006947f4",
      "incomplete_value": true,
      "site": "006947fc",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
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
      "006947cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006947dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006947cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006947dc",
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

- 旧版 [`0069441c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006943f4.md#insn-0069441c) · [`0069442c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006943f4.md#insn-0069442c) · [`0069444c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006943f4.md#insn-0069444c)
- 新版 [`006947cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/006947a4.md#insn-006947cc) · [`006947dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/006947a4.md#insn-006947dc) · [`006947fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/006947a4.md#insn-006947fc)

~~~diff
- 0069441c ["INT_ADD", "register:40f0:8", ["const:69441c:8", "const:4:8"]]
- 0069441c ["CALL", null, ["ram:47ad34:8"]]
+ 006947cc ["INT_ADD", "register:40f0:8", ["const:6947cc:8", "const:4:8"]]
+ 006947cc ["CALL", null, ["ram:47b054:8"]]
- 0069441c bytes 469af797
+ 006947cc bytes 229af797
- 0069442c ["INT_ADD", "register:40f0:8", ["const:69442c:8", "const:4:8"]]
- 0069442c ["CALL", null, ["ram:47ad34:8"]]
+ 006947dc ["INT_ADD", "register:40f0:8", ["const:6947dc:8", "const:4:8"]]
+ 006947dc ["CALL", null, ["ram:47b054:8"]]
- 0069442c bytes 429af797
+ 006947dc bytes 1e9af797
- 0069444c ["INT_ADD", "register:40f0:8", ["const:69444c:8", "const:4:8"]]
- 0069444c ["CALL", null, ["callee:0068adb4:8"]]
+ 006947fc ["INT_ADD", "register:40f0:8", ["const:6947fc:8", "const:4:8"]]
+ 006947fc ["CALL", null, ["callee:0068adb4:8"]]
- 0069444c bytes 6ed9ff97
+ 006947fc bytes 6ed9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b8cc5e03ad3bb480dc3f7a39422f967"></a>

### [`006944d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006944d8.md) → [`00694888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694888.md) FUN_00694888

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006948ac",
      "incomplete_value": false,
      "site": "006948ac",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006944fc",
      "incomplete_value": false,
      "site": "006944fc",
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
      "006948ac",
      "DATA",
      [
        "storage",
        "00c74da0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006948ac",
      "DATA",
      [
        "storage",
        "00c75d70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006944ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006944d8.md#insn-006944ec) · [`006944f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006944d8.md#insn-006944f4) · [`006944f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006944d8.md#insn-006944f8)
- 新版 [`0069489c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694888.md#insn-0069489c) · [`006948a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694888.md#insn-006948a4) · [`006948a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694888.md#insn-006948a8)

~~~diff
- 006944ec ["INT_ADD", "register:40f0:8", ["const:6944ec:8", "const:4:8"]]
- 006944ec ["CALL", null, ["callee:00c58f30:8"]]
+ 0069489c ["INT_ADD", "register:40f0:8", ["const:69489c:8", "const:4:8"]]
+ 0069489c ["CALL", null, ["callee:00c58f30:8"]]
- 006944ec bytes 9d0e1794
+ 0069489c bytes a5111794
- 006944f4 ["COPY", "register:4040:8", ["const:c74000:8"]]
+ 006948a4 ["COPY", "register:4040:8", ["const:c75000:8"]]
- 006944f4 bytes 082f0090
+ 006948a4 bytes 082f00b0
- 006944f8 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 006944f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006944f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006944f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006948a8 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 006948a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006948a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006948a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006944f8 bytes 08813691
+ 006948a8 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94c7b070ec5d2f56cbf424381885aaf3"></a>

### [`006945c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006945c4.md) → [`00694974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694974.md) FUN_00694974

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00694998",
      "incomplete_value": false,
      "site": "00694998",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00694998",
      "DATA",
      [
        "storage",
        "00c74e20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694998",
      "DATA",
      [
        "storage",
        "00c75df0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006945d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006945c4.md#insn-006945d8) · [`006945e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006945c4.md#insn-006945e0) · [`006945e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006945c4.md#insn-006945e4)
- 新版 [`00694988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694974.md#insn-00694988) · [`00694990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694974.md#insn-00694990) · [`00694994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694974.md#insn-00694994)

~~~diff
- 006945d8 ["INT_ADD", "register:40f0:8", ["const:6945d8:8", "const:4:8"]]
- 006945d8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00694988 ["INT_ADD", "register:40f0:8", ["const:694988:8", "const:4:8"]]
+ 00694988 ["CALL", null, ["callee:00c58f30:8"]]
- 006945d8 bytes 620e1794
+ 00694988 bytes 6a111794
- 006945e0 ["COPY", "register:4040:8", ["const:c74000:8"]]
+ 00694990 ["COPY", "register:4040:8", ["const:c75000:8"]]
- 006945e0 bytes 082f0090
+ 00694990 bytes 082f00b0
- 006945e4 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 006945e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006945e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006945e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00694994 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 00694994 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00694994 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00694994 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006945e4 bytes 08813891
+ 00694994 bytes 08c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9910ddf3e4d1ab318688fcbed92385bf"></a>

### [`0069472c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/0069472c.md) → [`00694adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694adc.md) FUN_00694adc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00694b00",
      "incomplete_value": false,
      "site": "00694b08",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00694b08",
      "DATA",
      [
        "storage",
        "00c74ea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694b08",
      "DATA",
      [
        "storage",
        "00c75e70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/0069472c.md#insn-00694740) · [`0069474c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/0069472c.md#insn-0069474c) · [`00694750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/0069472c.md#insn-00694750)
- 新版 [`00694af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694adc.md#insn-00694af0) · [`00694afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694adc.md#insn-00694afc) · [`00694b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694adc.md#insn-00694b00)

~~~diff
- 00694740 ["INT_ADD", "register:40f0:8", ["const:694740:8", "const:4:8"]]
- 00694740 ["CALL", null, ["callee:00c58f30:8"]]
+ 00694af0 ["INT_ADD", "register:40f0:8", ["const:694af0:8", "const:4:8"]]
+ 00694af0 ["CALL", null, ["callee:00c58f30:8"]]
- 00694740 bytes 080e1794
+ 00694af0 bytes 10111794
- 0069474c ["COPY", "register:4040:8", ["const:c74000:8"]]
+ 00694afc ["COPY", "register:4040:8", ["const:c75000:8"]]
- 0069474c bytes 082f0090
+ 00694afc bytes 082f00b0
- 00694750 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 00694750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00694750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00694750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00694b00 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00694b00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00694b00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00694b00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00694750 bytes 08813a91
+ 00694b00 bytes 08c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ab84d8eb9424b0a0098e4a77034d570"></a>

### [`006947a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006947a4.md) → [`00694b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694b54.md) FUN_00694b54

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.67% / 新版 93.67%

CFGの説明率　旧版 65.91% / 新版 64.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006948e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006948ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00694978"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00694c00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00694c28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00694c00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00694c28",
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

- 旧版 [`00694850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006947a4.md#insn-00694850) · [`00694878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006947a4.md#insn-00694878) · [`006948e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006947a4.md#insn-006948e0)
- 新版 [`00694c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694b54.md#insn-00694c00) · [`00694c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694b54.md#insn-00694c28)

~~~diff
- 00694850 ["INT_ADD", "register:40f0:8", ["const:694850:8", "const:4:8"]]
- 00694850 ["CALL", null, ["ram:47ad34:8"]]
+ 00694c00 ["INT_ADD", "register:40f0:8", ["const:694c00:8", "const:4:8"]]
+ 00694c00 ["CALL", null, ["ram:47b054:8"]]
- 00694850 bytes 3999f797
+ 00694c00 bytes 1599f797
- 00694878 ["INT_ADD", "register:40f0:8", ["const:694878:8", "const:4:8"]]
- 00694878 ["CALL", null, ["ram:47ad34:8"]]
+ 00694c28 ["INT_ADD", "register:40f0:8", ["const:694c28:8", "const:4:8"]]
+ 00694c28 ["CALL", null, ["ram:47b054:8"]]
- 00694878 bytes 2f99f797
+ 00694c28 bytes 0b99f797
- 006948e0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006948e0 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 006948e0 ["COPY", "tmp:2:8", ["register:4050:8"]]
- 006948e0 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 006948e0 bytes 4881889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5a01ab889e30d2dba844e45a431d540"></a>

### [`00694a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a48.md) → [`00694df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694df8.md) FUN_00694df8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00694e1c",
      "incomplete_value": false,
      "site": "00694e1c",
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
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00694e1c",
      "DATA",
      [
        "storage",
        "00c74f20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694e1c",
      "DATA",
      [
        "storage",
        "00c75ef0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a48.md#insn-00694a5c) · [`00694a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a48.md#insn-00694a64) · [`00694a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a48.md#insn-00694a68)
- 新版 [`00694e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694df8.md#insn-00694e0c) · [`00694e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694df8.md#insn-00694e14) · [`00694e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694df8.md#insn-00694e18)

~~~diff
- 00694a5c ["INT_ADD", "register:40f0:8", ["const:694a5c:8", "const:4:8"]]
- 00694a5c ["CALL", null, ["callee:00c58f30:8"]]
+ 00694e0c ["INT_ADD", "register:40f0:8", ["const:694e0c:8", "const:4:8"]]
+ 00694e0c ["CALL", null, ["callee:00c58f30:8"]]
- 00694a5c bytes 410d1794
+ 00694e0c bytes 49101794
- 00694a64 ["COPY", "register:4040:8", ["const:c74000:8"]]
+ 00694e14 ["COPY", "register:4040:8", ["const:c75000:8"]]
- 00694a64 bytes 082f0090
+ 00694e14 bytes 082f00b0
- 00694a68 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00694a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00694a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00694a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00694e18 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 00694e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00694e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00694e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00694a68 bytes 08813c91
+ 00694e18 bytes 08c13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4116104c91710a7b845d6167aff25c5d"></a>

### [`00694a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a98.md) → [`00694e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694e48.md) FUN_00694e48

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00694aa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00694e50"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00694ab4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00694aa0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00694e84"
      ]
    ],
    [
      "unmatched:00694ab4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00694e50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00694e84"
      ]
    ],
    [
      "00694e64",
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

- 旧版 [`00694aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a98.md#insn-00694aa0) · [`00694ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a98.md#insn-00694ab4) · [`00694ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a98.md#insn-00694ac0)
- 新版 [`00694e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694e48.md#insn-00694e70)

~~~diff
- 00694aa0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00694aa0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00694aa0 bytes a1010054
- 00694ab4 ["INT_ADD", "register:40f0:8", ["const:694ab4:8", "const:4:8"]]
- 00694ab4 ["CALL", null, ["ram:47ad34:8"]]
- 00694ab4 bytes a098f797
- 00694ac0 ["INT_ADD", "register:40f0:8", ["const:694ac0:8", "const:4:8"]]
- 00694ac0 ["CALL", null, ["callee:0047d134:8"]]
+ 00694e70 ["INT_ADD", "register:40f0:8", ["const:694e70:8", "const:4:8"]]
+ 00694e70 ["CALL", null, ["callee:0047d134:8"]]
- 00694ac0 bytes d5a0f797
+ 00694e70 bytes b1a0f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7aa995c6724497e849aaa0505c5455ba"></a>

### [`00694b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694b6c.md) → [`00694f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00694/00694f1c.md) FUN_00694f1c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068483c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/0068483c.md) [`0068edd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068edd8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`00684bec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00684/00684bec.md) [`0068f188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068f/0068f188.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.73% / 新版 86.73%

CFGの説明率　旧版 59.26% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694b70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694b70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694b74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00694b70",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00694b74",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00694b78",
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
      "00694f20",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00694f24",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00694f28",
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

- 旧版 [`00694b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694b6c.md#insn-00694b70) · [`00694b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694b6c.md#insn-00694b74) · [`00694b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694b6c.md#insn-00694b78)

~~~diff
- 00694b70 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00694b70 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00694b70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00694b70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00694b70 bytes fd7b02a9
- 00694b74 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00694b74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00694b74 bytes f91b00f9
- 00694b78 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00694b78 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00694b78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00694b78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00694b78 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c3dc881899013bd94dd15a5d2062c77"></a>

### [`00694d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d1c.md) → [`006950cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/006950cc.md) FUN_006950cc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "006950d8",
      "incomplete_value": false,
      "site": "006950dc",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "006950dc",
      "DATA",
      [
        "storage",
        "00c75020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006950dc",
      "DATA",
      [
        "storage",
        "00c75ff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d1c.md#insn-00694d28)
- 新版 [`006950d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/006950cc.md#insn-006950d8)

~~~diff
- 00694d28 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00694d28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00694d28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00694d28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006950d8 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 006950d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006950d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006950d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00694d28 bytes 29810091
+ 006950d8 bytes 29c13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d77aa7ef1d7a589c130b79c711d405b"></a>

### [`00694d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d80.md) → [`00695130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695130.md) FUN_00695130

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`006928cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928cc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

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
      "definition_site": "00695150",
      "incomplete_value": false,
      "site": "00695158",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00695158",
      "DATA",
      [
        "storage",
        "00c75020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00695158",
      "DATA",
      [
        "storage",
        "00c75ff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d80.md#insn-00694d98) · [`00694da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d80.md#insn-00694da0) · [`00694dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694d80.md#insn-00694dd4)
- 新版 [`00695148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695130.md#insn-00695148) · [`00695150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695130.md#insn-00695150) · [`00695184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695130.md#insn-00695184)

~~~diff
- 00694d98 ["INT_ADD", "register:40f0:8", ["const:694d98:8", "const:4:8"]]
- 00694d98 ["CALL", null, ["callee:00c58f30:8"]]
+ 00695148 ["INT_ADD", "register:40f0:8", ["const:695148:8", "const:4:8"]]
+ 00695148 ["CALL", null, ["callee:00c58f30:8"]]
- 00694d98 bytes 720c1794
+ 00695148 bytes 7a0f1794
- 00694da0 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00694da0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00694da0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00694da0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00695150 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00695150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00695150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00695150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00694da0 bytes 08810091
+ 00695150 bytes 08c13f91
- 00694dd4 ["INT_ADD", "register:40f0:8", ["const:694dd4:8", "const:4:8"]]
- 00694dd4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00695184 ["INT_ADD", "register:40f0:8", ["const:695184:8", "const:4:8"]]
+ 00695184 ["CALL", null, ["callee:00c58f30:8"]]
- 00694dd4 bytes 630c1794
+ 00695184 bytes 6b0f1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e049e5b781668cc069665578cc2d717b"></a>

### [`00694e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694e38.md) → [`006951e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/006951e8.md) FUN_006951e8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`006928cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928cc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 30.00% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694e38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694e38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694e3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00694e38",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00694e3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00694e40",
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
      "006951e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "006951ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006951f0",
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

- 旧版 [`00694e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694e38.md#insn-00694e38) · [`00694e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694e38.md#insn-00694e3c) · [`00694e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694e38.md#insn-00694e40)

~~~diff
- 00694e38 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00694e38 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00694e38 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00694e38 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00694e38 bytes fd7bbda9
- 00694e3c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00694e3c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00694e3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00694e3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00694e3c bytes f65701a9
- 00694e40 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00694e40 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00694e40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00694e40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00694e40 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5cf432c7e64cbecd5539ba0be4f58e6"></a>

### [`00694ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694ed8.md) → [`00695288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695288.md) FUN_00695288

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "site": "00694ee0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00695290"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00694ee0"
      ],
      [
        "FALL_THROUGH",
        "00695290"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00695290",
      "incomplete_value": true,
      "site": "00695294",
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
      "unmatched:00694ee0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069529c"
      ]
    ]
  ],
  "added": [
    [
      "00695290",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069529c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694ed8.md#insn-00694ee0) · [`00694ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694ed8.md#insn-00694ed8)
- 新版 [`00695290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695288.md#insn-00695290)

~~~diff
- 00694ee0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00694ee0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00694ee0 bytes 600000b4
+ 00695290 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00695290 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00695290 bytes 600000b4
- 00694ed8 ["COPY", "register:4040:8", ["register:4000:8"]]
- 00694ed8 bytes e80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14d6a1f9d572353567760a2628c54179"></a>

### [`00694ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694ef0.md) → [`006952a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/006952a0.md) FUN_006952a0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0068e7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068e7ac.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0068eb5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068e/0068eb5c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00694ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694ef0.md#insn-00694ef4) · [`00694f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694ef0.md#insn-00694f10)
- 新版 [`006952a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/006952a0.md#insn-006952a4) · [`006952c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/006952a0.md#insn-006952c0)

~~~diff
- 00694ef4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00694ef4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 006952a4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 006952a4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00694ef4 bytes 680100b4
+ 006952a4 bytes 680100b4
- 00694f10 ["INT_ADD", "register:40f0:8", ["const:694f10:8", "const:4:8"]]
- 00694f10 ["CALL", null, ["callee:00c58f50:8"]]
+ 006952c0 ["INT_ADD", "register:40f0:8", ["const:6952c0:8", "const:4:8"]]
+ 006952c0 ["CALL", null, ["callee:00c58f50:8"]]
- 00694f10 bytes 1c0c1794
+ 006952c0 bytes 240f1794
~~~


<a id="compare-5127fac9573d6433f6bd613437d1fcd9"></a>

### [`0069534c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/0069534c.md) → [`006956fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/006956fc.md) FUN_006956fc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00695708",
      "incomplete_value": false,
      "site": "0069570c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "0069570c",
      "DATA",
      [
        "storage",
        "00c750d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069570c",
      "DATA",
      [
        "storage",
        "00c760a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00695354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/0069534c.md#insn-00695354) · [`00695358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/0069534c.md#insn-00695358)
- 新版 [`00695704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/006956fc.md#insn-00695704) · [`00695708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/006956fc.md#insn-00695708)

~~~diff
- 00695354 ["COPY", "register:4048:8", ["const:c75000:8"]]
+ 00695704 ["COPY", "register:4048:8", ["const:c76000:8"]]
- 00695354 bytes 092f0090
+ 00695704 bytes 092f00b0
- 00695358 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 00695358 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00695358 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00695358 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00695708 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 00695708 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00695708 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00695708 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00695358 bytes 29410391
+ 00695708 bytes 29810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-878f5e01ee4e3aff36a11232b13663b8"></a>

### [`00695370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695370.md) → [`00695720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695720.md) FUN_00695720

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00695728",
      "incomplete_value": false,
      "site": "0069572c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "0069572c",
      "DATA",
      [
        "storage",
        "00c750d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069572c",
      "DATA",
      [
        "storage",
        "00c760a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00695374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695370.md#insn-00695374) · [`00695378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695370.md#insn-00695378) · [`0069539c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695370.md#insn-0069539c)
- 新版 [`00695724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695720.md#insn-00695724) · [`00695728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695720.md#insn-00695728) · [`0069574c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695720.md#insn-0069574c)

~~~diff
- 00695374 ["COPY", "register:4048:8", ["const:c75000:8"]]
+ 00695724 ["COPY", "register:4048:8", ["const:c76000:8"]]
- 00695374 bytes 092f0090
+ 00695724 bytes 092f00b0
- 00695378 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 00695378 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00695378 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00695378 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00695728 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 00695728 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00695728 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00695728 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00695378 bytes 29410391
+ 00695728 bytes 29810291
- 0069539c ["INT_ADD", "register:40f0:8", ["const:69539c:8", "const:4:8"]]
- 0069539c ["CALL", null, ["callee:00c58f50:8"]]
+ 0069574c ["INT_ADD", "register:40f0:8", ["const:69574c:8", "const:4:8"]]
+ 0069574c ["CALL", null, ["callee:00c58f50:8"]]
- 0069539c bytes f90a1794
+ 0069574c bytes 010e1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9eab016d8b46a3dd8e645a70e4a24358"></a>

### [`006953b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/006953b0.md) → [`00695760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695760.md) FUN_00695760

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`006928cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928cc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

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
      "definition_site": "00695780",
      "incomplete_value": false,
      "site": "00695788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00695788",
      "DATA",
      [
        "storage",
        "00c750d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00695788",
      "DATA",
      [
        "storage",
        "00c760a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006953c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/006953b0.md#insn-006953c8) · [`006953cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/006953b0.md#insn-006953cc) · [`006953d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/006953b0.md#insn-006953d0)
- 新版 [`00695778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695760.md#insn-00695778) · [`0069577c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695760.md#insn-0069577c) · [`00695780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695760.md#insn-00695780)

~~~diff
- 006953c8 ["INT_ADD", "register:40f0:8", ["const:6953c8:8", "const:4:8"]]
- 006953c8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00695778 ["INT_ADD", "register:40f0:8", ["const:695778:8", "const:4:8"]]
+ 00695778 ["CALL", null, ["callee:00c58f30:8"]]
- 006953c8 bytes e60a1794
+ 00695778 bytes ee0d1794
- 006953cc ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 0069577c ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006953cc bytes 082f0090
+ 0069577c bytes 082f00b0
- 006953d0 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 006953d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006953d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006953d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00695780 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 00695780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00695780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00695780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006953d0 bytes 08410391
+ 00695780 bytes 08810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24cdf50c8b0c4ca221b4bafc5a9addbf"></a>

### [`00695470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695470.md) → [`00695820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695820.md) FUN_00695820

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`006928cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928cc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

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
      "definition_site": "00695834",
      "incomplete_value": false,
      "site": "0069583c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "0069583c",
      "DATA",
      [
        "storage",
        "00c750d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069583c",
      "DATA",
      [
        "storage",
        "00c760a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00695480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695470.md#insn-00695480) · [`00695484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695470.md#insn-00695484) · [`006954c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695470.md#insn-006954c0)
- 新版 [`00695830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695820.md#insn-00695830) · [`00695834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695820.md#insn-00695834) · [`00695870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695820.md#insn-00695870)

~~~diff
- 00695480 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 00695830 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 00695480 bytes 082f0090
+ 00695830 bytes 082f00b0
- 00695484 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 00695484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00695484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00695484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00695834 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 00695834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00695834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00695834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00695484 bytes 08410391
+ 00695834 bytes 08810291
- 006954c0 ["INT_ADD", "register:40f0:8", ["const:6954c0:8", "const:4:8"]]
- 006954c0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00695870 ["INT_ADD", "register:40f0:8", ["const:695870:8", "const:4:8"]]
+ 00695870 ["CALL", null, ["callee:00c58f30:8"]]
- 006954c0 bytes a80a1794
+ 00695870 bytes b00d1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6e0d60372837cdb51c690bc4800d1e1"></a>

### [`00695564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695564.md) → [`00695914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695914.md) FUN_00695914

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 24件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`004682b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004682b4.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.81% / 新版 91.81%

CFGの説明率　旧版 64.29% / 新版 64.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695590"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695608"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00695940"
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
      "unmatched:00695590",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:006955d4",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:006955d8",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00695940",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00695984",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00695988",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00695590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695564.md#insn-00695590) · [`006955ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695564.md#insn-006955ec) · [`00695608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695564.md#insn-00695608)

~~~diff
- 00695590 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00695590 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00695590 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00695590 bytes a8831ff8
- 006955ec ["INT_ADD", "register:40f0:8", ["const:6955ec:8", "const:4:8"]]
- 006955ec ["CALL", null, ["callee:00c596b0:8"]]
- 006955ec bytes 3d0c1794
- 00695608 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00695608 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00695608 bytes e11300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b6a2fbfc7a5f38ccbd6e2cf271ea115"></a>

### [`00695a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695a48.md) → [`00695df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695df8.md) FUN_00695df8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00695564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695564.md) [`00696768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696768.md) [`0069802c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/0069802c.md) [`006992d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006992d4.md) · 呼出先 3件 [`005d8aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8aac.md) [`00695fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695fa8.md) [`00c5a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8f0.md)
- 新版 呼出元 4件 [`00695914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695914.md) [`00696b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696b18.md) [`006983dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006983dc.md) [`00699684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/00699684.md) · 呼出先 3件 [`005d8e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8e5c.md) [`00696358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696358.md) [`00c5b8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.86% / 新版 89.86%

CFGの説明率　旧版 33.33% / 新版 32.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00695a94"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00695ad0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00695b1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00695a94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695e64"
      ]
    ],
    [
      "unmatched:00695ad0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695ebc"
      ]
    ],
    [
      "unmatched:00695b1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695edc"
      ]
    ]
  ],
  "added": [
    [
      "00695e44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695e64"
      ]
    ],
    [
      "00695e80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695ebc"
      ]
    ],
    [
      "00695ecc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695edc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00695a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695a48.md#insn-00695a94) · [`00695ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695a48.md#insn-00695ad0) · [`00695b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695a48.md#insn-00695b1c)

~~~diff
- 00695a94 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00695a94 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00695a94 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00695a94 bytes 09010054
- 00695ad0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00695ad0 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00695ad0 bytes e3010054
- 00695b1c ["CBRANCH", null, ["local:b15:8", "register:102:1"]]
- 00695b1c bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-673989cdc35580494e78f98a46837896"></a>

### [`00695c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695c04.md) → [`00695fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695fb4.md) FUN_00695fb4

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 20件 [`00695564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695564.md) [`0069802c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/0069802c.md) [`00698ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698ad0.md) [`0090b95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090b/0090b95c.md) [`0091abcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0091a/0091abcc.md) · 呼出先 4件 [`005d8aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8aac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8f0.md)
- 新版 呼出元 20件 [`00695914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695914.md) [`006983dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006983dc.md) [`00698e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698e80.md) [`0090c908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0090c/0090c908.md) [`0091bb78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0091b/0091bb78.md) · 呼出先 4件 [`005d8e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8e5c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8c0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.72% / 新版 78.72%

CFGの説明率　旧版 21.05% / 新版 21.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 4件, `unresolved_branch_alignment` 14件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695d08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695d08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695ebc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00696010",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "006961fc"
      ]
    ],
    [
      "unmatched:00695c70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006961fc"
      ]
    ],
    [
      "00696204",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00696090"
      ]
    ]
  ],
  "added": [
    [
      "00696010",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0069602c"
      ]
    ],
    [
      "00696020",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069602c"
      ]
    ],
    [
      "00696034",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00696090"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00695c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695c04.md#insn-00695c70) · [`00695c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695c04.md#insn-00695c8c) · [`00695ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695c04.md#insn-00695ca0)

~~~diff
- 00695c70 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00695c70 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00695c70 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 00695c70 bytes 68000054
- 00695c8c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00695c8c ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00695c8c bytes b40200b4
- 00695ca0 ["CBRANCH", null, ["local:b46:8", "register:101:1"]]
- 00695ca0 bytes 000b0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36337038e44638164ccb1d0943aa3682"></a>

### [`00695f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695f18.md) → [`006962c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/006962c8.md) FUN_006962c8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.11% / 新版 86.11%

CFGの説明率　旧版 6.67% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695f18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695f18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695f1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00695f18",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00695f1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00695f20",
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
      "006962c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "006962cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006962d0",
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

- 旧版 [`00695f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695f18.md#insn-00695f18) · [`00695f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695f18.md#insn-00695f1c) · [`00695f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695f18.md#insn-00695f20)

~~~diff
- 00695f18 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00695f18 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00695f18 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00695f18 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00695f18 bytes fd7bbda9
- 00695f1c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00695f1c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00695f1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00695f1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00695f1c bytes f65701a9
- 00695f20 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00695f20 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00695f20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00695f20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00695f20 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1df57feae19614829bc252103bf55e01"></a>

### [`00695fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695fa8.md) → [`00696358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696358.md) FUN_00696358

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00695a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695a48.md) · 呼出先 5件 [`005d8aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8aac.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8f0.md)
- 新版 呼出元 1件 [`00695df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695df8.md) · 呼出先 5件 [`005d8e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8e5c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 57.61% / 新版 60.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695fac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695fac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00695fb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00695fac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00695fb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00695fb4",
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
      "0069635c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00696360",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00696364",
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

- 旧版 [`00695fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695fa8.md#insn-00695fac) · [`00695fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695fa8.md#insn-00695fb0) · [`00695fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695fa8.md#insn-00695fb4)

~~~diff
- 00695fac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00695fac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00695fac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00695fac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00695fac bytes fd7b02a9
- 00695fb0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00695fb0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00695fb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00695fb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00695fb0 bytes fa6703a9
- 00695fb4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00695fb4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00695fb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00695fb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00695fb4 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c0c66f050ca873b02a1d4263bd88063"></a>

### [`006962d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006962d0.md) → [`00696680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696680.md) FUN_00696680

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006966a0",
      "incomplete_value": false,
      "site": "006966a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
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
      "006966a4",
      "DATA",
      [
        "storage",
        "00c75150",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006966a4",
      "DATA",
      [
        "storage",
        "00c76120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006962e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006962d0.md#insn-006962e4) · [`006962ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006962d0.md#insn-006962ec) · [`006962f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006962d0.md#insn-006962f0)
- 新版 [`00696694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696680.md#insn-00696694) · [`0069669c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696680.md#insn-0069669c) · [`006966a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696680.md#insn-006966a0)

~~~diff
- 006962e4 ["INT_ADD", "register:40f0:8", ["const:6962e4:8", "const:4:8"]]
- 006962e4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00696694 ["INT_ADD", "register:40f0:8", ["const:696694:8", "const:4:8"]]
+ 00696694 ["CALL", null, ["callee:00c58f30:8"]]
- 006962e4 bytes 1f071794
+ 00696694 bytes 270a1794
- 006962ec ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 0069669c ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006962ec bytes e82e00f0
+ 0069669c bytes 082f0090
- 006962f0 ["COPY", "tmp:0:8", ["const:150:8"]]
- 006962f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006962f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006962f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006966a0 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 006966a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006966a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006966a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006962f0 bytes 08410591
+ 006966a0 bytes 08810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1865fb4bb59f906bb009fe1cf77f1b57"></a>

### [`00696308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696308.md) → [`006966b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/006966b8.md) FUN_006966b8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006966bc",
      "incomplete_value": false,
      "site": "006966c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
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
      "006966c0",
      "DATA",
      [
        "storage",
        "00c75150",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006966c0",
      "DATA",
      [
        "storage",
        "00c76120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00696308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696308.md#insn-00696308) · [`0069630c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696308.md#insn-0069630c)
- 新版 [`006966b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/006966b8.md#insn-006966b8) · [`006966bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/006966b8.md#insn-006966bc)

~~~diff
- 00696308 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006966b8 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 00696308 bytes e82e00f0
+ 006966b8 bytes 082f0090
- 0069630c ["COPY", "tmp:0:8", ["const:150:8"]]
- 0069630c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0069630c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0069630c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006966bc ["COPY", "tmp:0:8", ["const:120:8"]]
+ 006966bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006966bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006966bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0069630c bytes 08410591
+ 006966bc bytes 08810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87d61aba5bca40d53162c25c653823b7"></a>

### [`00696328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696328.md) → [`006966d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/006966d8.md) FUN_006966d8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`006882d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00688/006882d4.md) [`0068978c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/0068978c.md) [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`00688684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00688/00688684.md) [`00689b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00689/00689b3c.md) [`0071c2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c2e0.md)

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
      "site": "0069670c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0069635c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "00696790",
      "value": [
        "leaf",
        "ram:71c2e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006963e0",
      "value": [
        "leaf",
        "ram:71bf30:8"
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
      "site": "006967a0",
      "value": [
        "leaf",
        "ram:71d604:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006963f0",
      "value": [
        "leaf",
        "ram:71d254:8"
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
      "0069670c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00696790",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "006967a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d254"
      ]
    ]
  ],
  "added": [
    [
      "0069670c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00696790",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c2e0"
      ]
    ],
    [
      "006967a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d604"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069635c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696328.md#insn-0069635c) · [`006963e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696328.md#insn-006963e0) · [`006963f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696328.md#insn-006963f0)
- 新版 [`0069670c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/006966d8.md#insn-0069670c) · [`00696790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/006966d8.md#insn-00696790) · [`006967a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/006966d8.md#insn-006967a0)

~~~diff
- 0069635c ["INT_ADD", "register:40f0:8", ["const:69635c:8", "const:4:8"]]
- 0069635c ["CALL", null, ["ram:47ad34:8"]]
+ 0069670c ["INT_ADD", "register:40f0:8", ["const:69670c:8", "const:4:8"]]
+ 0069670c ["CALL", null, ["ram:47b054:8"]]
- 0069635c bytes 7692f797
+ 0069670c bytes 5292f797
- 006963e0 ["INT_ADD", "register:40f0:8", ["const:6963e0:8", "const:4:8"]]
- 006963e0 ["CALL", null, ["ram:71bf30:8"]]
+ 00696790 ["INT_ADD", "register:40f0:8", ["const:696790:8", "const:4:8"]]
+ 00696790 ["CALL", null, ["ram:71c2e0:8"]]
- 006963e0 bytes d4160294
+ 00696790 bytes d4160294
- 006963f0 ["INT_ADD", "register:40f0:8", ["const:6963f0:8", "const:4:8"]]
- 006963f0 ["CALL", null, ["ram:71d254:8"]]
+ 006967a0 ["INT_ADD", "register:40f0:8", ["const:6967a0:8", "const:4:8"]]
+ 006967a0 ["CALL", null, ["ram:71d604:8"]]
- 006963f0 bytes 991b0294
+ 006967a0 bytes 991b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-328addfd7284cc05daac1dbc4ace3e62"></a>

### [`00696480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696480.md) → [`00696830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696830.md) FUN_00696830

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0069683c",
      "incomplete_value": false,
      "site": "0069683c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "0069683c",
      "DATA",
      [
        "storage",
        "00c751d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069683c",
      "DATA",
      [
        "storage",
        "00c761a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00696484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696480.md#insn-00696484) · [`00696488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696480.md#insn-00696488)
- 新版 [`00696834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696830.md#insn-00696834) · [`00696838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696830.md#insn-00696838)

~~~diff
- 00696484 ["COPY", "register:4048:8", ["const:c75000:8"]]
+ 00696834 ["COPY", "register:4048:8", ["const:c76000:8"]]
- 00696484 bytes e92e00f0
+ 00696834 bytes 092f0090
- 00696488 ["COPY", "tmp:0:8", ["const:1d0:8"]]
- 00696488 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00696488 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00696488 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00696838 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 00696838 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00696838 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00696838 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00696488 bytes 29410791
+ 00696838 bytes 29810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba578cfdae472e0c673757a2c92210c1"></a>

### [`00696588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696588.md) → [`00696938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696938.md) FUN_00696938

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0069695c",
      "incomplete_value": false,
      "site": "0069695c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
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
      "0069695c",
      "DATA",
      [
        "storage",
        "00c75250",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069695c",
      "DATA",
      [
        "storage",
        "00c76220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069659c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696588.md#insn-0069659c) · [`006965a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696588.md#insn-006965a4) · [`006965a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696588.md#insn-006965a8)
- 新版 [`0069694c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696938.md#insn-0069694c) · [`00696954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696938.md#insn-00696954) · [`00696958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696938.md#insn-00696958)

~~~diff
- 0069659c ["INT_ADD", "register:40f0:8", ["const:69659c:8", "const:4:8"]]
- 0069659c ["CALL", null, ["callee:00c58f30:8"]]
+ 0069694c ["INT_ADD", "register:40f0:8", ["const:69694c:8", "const:4:8"]]
+ 0069694c ["CALL", null, ["callee:00c58f30:8"]]
- 0069659c bytes 71061794
+ 0069694c bytes 79091794
- 006965a4 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 00696954 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006965a4 bytes e82e00f0
+ 00696954 bytes 082f0090
- 006965a8 ["COPY", "tmp:0:8", ["const:250:8"]]
- 006965a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006965a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006965a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00696958 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 00696958 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00696958 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00696958 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006965a8 bytes 08410991
+ 00696958 bytes 08810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78005799c85abb845f6efab7b7293c20"></a>

### [`006965bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006965bc.md) → [`0069696c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/0069696c.md) FUN_0069696c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00696978",
      "incomplete_value": false,
      "site": "00696978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00696978",
      "DATA",
      [
        "storage",
        "00c75250",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00696978",
      "DATA",
      [
        "storage",
        "00c76220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006965c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006965bc.md#insn-006965c0) · [`006965c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006965bc.md#insn-006965c4)
- 新版 [`00696970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/0069696c.md#insn-00696970) · [`00696974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/0069696c.md#insn-00696974)

~~~diff
- 006965c0 ["COPY", "register:4048:8", ["const:c75000:8"]]
+ 00696970 ["COPY", "register:4048:8", ["const:c76000:8"]]
- 006965c0 bytes e92e00f0
+ 00696970 bytes 092f0090
- 006965c4 ["COPY", "tmp:0:8", ["const:250:8"]]
- 006965c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006965c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006965c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00696974 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 00696974 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00696974 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00696974 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006965c4 bytes 29410991
+ 00696974 bytes 29810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cab3dc4c472cbdd3cdbc194549584061"></a>

### [`006965d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006965d8.md) → [`00696988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696988.md) FUN_00696988

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0085b338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b338.md) [`008b92f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92f0.md) [`008b9558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b9558.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0046de54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de54.md) [`0085c2e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c2e4.md) [`008ba29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba29c.md) [`008ba504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba504.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 60.00% / 新版 70.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00696a08",
      "incomplete_value": true,
      "site": "00696a0c",
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
                "const:170:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00696a5c",
      "incomplete_value": true,
      "site": "00696a64",
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
    "old": null,
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00696a5c",
      "incomplete_value": true,
      "site": "00696a64",
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
    "old": null,
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
      "unmatched:00696610",
      "DATA",
      [
        "storage",
        "00338758",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "00696a08",
      "READ",
      [
        "storage",
        "002c4120",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006969c0",
      "DATA",
      [
        "storage",
        "00338758",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "00696a08",
      "READ",
      [
        "storage",
        "002c4170",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006966b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006965d8.md#insn-006966b4) · [`0069660c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006965d8.md#insn-0069660c) · [`00696610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/006965d8.md#insn-00696610)
- 新版 [`00696a64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696988.md#insn-00696a64)

~~~diff
- 006966b4 ["INT_ADD", "register:40f0:8", ["const:6966b4:8", "const:4:8"]]
- 006966b4 ["CALL", null, ["callee:008ba504:8"]]
+ 00696a64 ["INT_ADD", "register:40f0:8", ["const:696a64:8", "const:4:8"]]
+ 00696a64 ["CALL", null, ["callee:008ba504:8"]]
- 006966b4 bytes a98b0894
+ 00696a64 bytes a88e0894
- 0069660c ["INT_LEFT", "tmp:0:8", ["const:338:8", "const:c:4"]]
- 0069660c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 0069660c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:1:8"]]
- 0069660c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:1:8"]]
- 0069660c bytes 96e24c91
- 00696610 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:758:8"]]
- 00696610 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00696610 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 00696610 bytes c85a47b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d93d3b54f31200a26538a5a5c805576"></a>

### [`00696710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696710.md) → [`00696ac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696ac0.md) FUN_00696ac0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00696734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00696738"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00696ae4"
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
      "unmatched:00696734",
      "DATA",
      [
        "storage",
        "00c752d0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0069673c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00696740",
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
      "00696ae4",
      "DATA",
      [
        "storage",
        "00c762a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00696aec",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00696af0",
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

- 旧版 [`00696724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696710.md#insn-00696724) · [`00696734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696710.md#insn-00696734) · [`00696738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696710.md#insn-00696738)
- 新版 [`00696ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696ac0.md#insn-00696ad4)

~~~diff
- 00696724 ["INT_ADD", "register:40f0:8", ["const:696724:8", "const:4:8"]]
- 00696724 ["CALL", null, ["callee:00c58f30:8"]]
+ 00696ad4 ["INT_ADD", "register:40f0:8", ["const:696ad4:8", "const:4:8"]]
+ 00696ad4 ["CALL", null, ["callee:00c58f30:8"]]
- 00696724 bytes 0f061794
+ 00696ad4 bytes 17091794
- 00696734 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00696734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00696734 bytes 080000f9
- 00696738 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00696738 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00696738 bytes 0080803c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a638e5bd5dbcec8d471dc326eff4e6b3"></a>

### [`00696748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696748.md) → [`00696af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696af8.md) FUN_00696af8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00696afc",
      "incomplete_value": false,
      "site": "00696b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00696b00",
      "DATA",
      [
        "storage",
        "00c752d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00696b00",
      "DATA",
      [
        "storage",
        "00c762a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00696748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696748.md#insn-00696748) · [`0069674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696748.md#insn-0069674c)
- 新版 [`00696af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696af8.md#insn-00696af8) · [`00696afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696af8.md#insn-00696afc)

~~~diff
- 00696748 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 00696af8 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 00696748 bytes e82e00f0
+ 00696af8 bytes 082f0090
- 0069674c ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 0069674c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0069674c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0069674c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00696afc ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 00696afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00696afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00696afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0069674c bytes 08410b91
+ 00696afc bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15b4ef466f7c9556135cf555b464b68e"></a>

### [`00696768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696768.md) → [`00696b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696b18.md) FUN_00696b18

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 21件 [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md)
- 新版 呼出元 0件  · 呼出先 21件 [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`004682b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004682b4.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046cde4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cde4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.75% / 新版 87.75%

CFGの説明率　旧版 5.48% / 新版 5.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00696798"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00696b48"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006967b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00696798",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:006967b0",
      "DATA",
      [
        "storage",
        "00338754",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "unmatched:006967b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00696d2c"
      ]
    ]
  ],
  "added": [
    [
      "00696b48",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00696b60",
      "DATA",
      [
        "storage",
        "00338754",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "00696b68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00696d2c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00696798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696768.md#insn-00696798) · [`006967b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696768.md#insn-006967b8) · [`00696854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696768.md#insn-00696854)
- 新版 [`00696c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696b18.md#insn-00696c04)

~~~diff
- 00696798 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00696798 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00696798 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00696798 bytes a8831ff8
- 006967b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 006967b8 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 006967b8 bytes 2b0e0054
- 00696854 ["INT_ADD", "register:40f0:8", ["const:696854:8", "const:4:8"]]
- 00696854 ["CALL", null, ["callee:00c596b0:8"]]
+ 00696c04 ["INT_ADD", "register:40f0:8", ["const:696c04:8", "const:4:8"]]
+ 00696c04 ["CALL", null, ["callee:00c596b0:8"]]
- 00696854 bytes a3071794
+ 00696c04 bytes ab0a1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-883dd1330bdb454f0bacbdad7080eba5"></a>

### [`00696e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e5c.md) → [`0069720c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/0069720c.md) FUN_0069720c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00697210",
      "incomplete_value": false,
      "site": "00697214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00697214",
      "DATA",
      [
        "storage",
        "00c75350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697214",
      "DATA",
      [
        "storage",
        "00c76320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00696e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e5c.md#insn-00696e5c) · [`00696e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e5c.md#insn-00696e60)
- 新版 [`0069720c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/0069720c.md#insn-0069720c) · [`00697210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/0069720c.md#insn-00697210)

~~~diff
- 00696e5c ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 0069720c ["COPY", "register:4040:8", ["const:c76000:8"]]
- 00696e5c bytes e82e00f0
+ 0069720c bytes e82e00f0
- 00696e60 ["COPY", "tmp:0:8", ["const:350:8"]]
- 00696e60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00696e60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00696e60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00697210 ["COPY", "tmp:0:8", ["const:320:8"]]
+ 00697210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00697210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00697210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00696e60 bytes 08410d91
+ 00697210 bytes 08810c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0736a421ab7e3758b329510e6c2a9fc"></a>

### [`00696e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e7c.md) → [`0069722c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/0069722c.md) FUN_0069722c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 16件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068edd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068edd8.md) [`00690740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00690/00690740.md) [`006971c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006971c0.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0068f188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068f/0068f188.md) [`00690af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00690/00690af0.md) [`00697570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697570.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 71.43% / 新版 80.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_value` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00696e9c"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006973bc",
      "incomplete_value": false,
      "site": "006973c4",
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
            "const:ef3:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006973e4",
      "incomplete_value": false,
      "site": "006973f0",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
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
      "unmatched:00696e9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "0069728c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00697330",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "0069724c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "0069728c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00697330",
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

- 旧版 [`00696e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e7c.md#insn-00696e9c) · [`00696edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e7c.md#insn-00696edc) · [`00696f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e7c.md#insn-00696f38)
- 新版 [`0069728c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/0069722c.md#insn-0069728c) · [`006972e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/0069722c.md#insn-006972e8)

~~~diff
- 00696e9c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00696e9c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00696e9c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00696e9c bytes a8831ff8
- 00696edc ["INT_ADD", "register:40f0:8", ["const:696edc:8", "const:4:8"]]
- 00696edc ["CALL", null, ["ram:47ad34:8"]]
+ 0069728c ["INT_ADD", "register:40f0:8", ["const:69728c:8", "const:4:8"]]
+ 0069728c ["CALL", null, ["ram:47b054:8"]]
- 00696edc bytes 968ff797
+ 0069728c bytes 728ff797
- 00696f38 ["INT_ADD", "register:40f0:8", ["const:696f38:8", "const:4:8"]]
- 00696f38 ["CALL", null, ["callee:008b894c:8"]]
+ 006972e8 ["INT_ADD", "register:40f0:8", ["const:6972e8:8", "const:4:8"]]
+ 006972e8 ["CALL", null, ["callee:008b894c:8"]]
- 00696f38 bytes 9a820894
+ 006972e8 bytes 99850894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a95c0298fccb6d9b5067315f1ea987a"></a>

### [`006971c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006971c0.md) → [`00697570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697570.md) FUN_00697570

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 5件 [`00696e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e7c.md) [`0071d254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d254.md) [`007200e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00720/007200e8.md) [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) · 呼出先 5件 [`006972e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006972e8.md) [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md) [`00b3bfbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bfbc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 5件 [`0069722c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/0069722c.md) [`0071d604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d604.md) [`00720498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00720/00720498.md) [`0090ecfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0090e/0090ecfc.md) [`0094826c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00948/0094826c.md) · 呼出先 5件 [`00697698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697698.md) [`00b3cf24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf24.md) [`00b3cfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cfb0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 85.71% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006971e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006971c0.md#insn-006971e0) · [`006971f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006971c0.md#insn-006971f4) · [`006971fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006971c0.md#insn-006971fc)
- 新版 [`00697590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697570.md#insn-00697590) · [`006975a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697570.md#insn-006975a4) · [`006975ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697570.md#insn-006975ac)

~~~diff
- 006971e0 ["INT_RIGHT", "tmp:0:4", ["register:4008:4", "const:1f:4"]]
- 006971e0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 006971e0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 006971e0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00697590 ["INT_RIGHT", "tmp:0:4", ["register:4008:4", "const:1f:4"]]
+ 00697590 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00697590 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00697590 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 006971e0 bytes 0101f837
+ 00697590 bytes 0101f837
- 006971f4 ["INT_ADD", "register:40f0:8", ["const:6971f4:8", "const:4:8"]]
- 006971f4 ["CALL", null, ["callee:00b3cf24:8"]]
+ 006975a4 ["INT_ADD", "register:40f0:8", ["const:6975a4:8", "const:4:8"]]
+ 006975a4 ["CALL", null, ["callee:00b3cf24:8"]]
- 006971f4 bytes 4f931294
+ 006975a4 bytes 60961294
- 006971fc ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 006971fc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 006975ac ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 006975ac ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 006971fc bytes 6a000054
+ 006975ac bytes 6a000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c040dc21d4375ba7a3e3376ef72cdfd"></a>

### [`00697444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697444.md) → [`006977f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006977f4.md) FUN_006977f4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006977f8",
      "incomplete_value": false,
      "site": "006977fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00697448",
      "incomplete_value": false,
      "site": "0069744c",
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
            "const:3d0:8"
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
      "006977fc",
      "DATA",
      [
        "storage",
        "00c753d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006977fc",
      "DATA",
      [
        "storage",
        "00c763a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697444.md#insn-00697444) · [`00697448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697444.md#insn-00697448)
- 新版 [`006977f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006977f4.md#insn-006977f4) · [`006977f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006977f4.md#insn-006977f8)

~~~diff
- 00697444 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006977f4 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 00697444 bytes e82e00d0
+ 006977f4 bytes e82e00f0
- 00697448 ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 00697448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00697448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00697448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006977f8 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 006977f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006977f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006977f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00697448 bytes 08410f91
+ 006977f8 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d65b014369385cf8f7233397a9dfbbb"></a>

### [`00697464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697464.md) → [`00697814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697814.md) FUN_00697814

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa0.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f4c.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 72.73% / 新版 80.00%

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
      "site": "0069784c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0069749c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "00697864",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006974b4",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "0069784c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00697864",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "0069784c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00697864",
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

- 旧版 [`0069749c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697464.md#insn-0069749c) · [`006974b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697464.md#insn-006974b4) · [`00697480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697464.md#insn-00697480)
- 新版 [`0069784c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697814.md#insn-0069784c) · [`00697864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697814.md#insn-00697864) · [`00697830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697814.md#insn-00697830)

~~~diff
- 0069749c ["INT_ADD", "register:40f0:8", ["const:69749c:8", "const:4:8"]]
- 0069749c ["CALL", null, ["ram:47ad34:8"]]
+ 0069784c ["INT_ADD", "register:40f0:8", ["const:69784c:8", "const:4:8"]]
+ 0069784c ["CALL", null, ["ram:47b054:8"]]
- 0069749c bytes 268ef797
+ 0069784c bytes 028ef797
- 006974b4 ["INT_ADD", "register:40f0:8", ["const:6974b4:8", "const:4:8"]]
- 006974b4 ["CALL", null, ["ram:47ad34:8"]]
+ 00697864 ["INT_ADD", "register:40f0:8", ["const:697864:8", "const:4:8"]]
+ 00697864 ["CALL", null, ["ram:47b054:8"]]
- 006974b4 bytes 208ef797
+ 00697864 bytes fc8df797
- 00697480 ["INT_ADD", "register:40f0:8", ["const:697480:8", "const:4:8"]]
- 00697480 ["CALL", null, ["callee:008b7f4c:8"]]
+ 00697830 ["INT_ADD", "register:40f0:8", ["const:697830:8", "const:4:8"]]
+ 00697830 ["CALL", null, ["callee:008b7f4c:8"]]
- 00697480 bytes c87e0894
+ 00697830 bytes c7810894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24fc970197b94ade83229f206f4abdb9"></a>

### [`00697508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697508.md) → [`006978b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006978b8.md) FUN_006978b8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006978d8",
      "incomplete_value": false,
      "site": "006978dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
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
      "006978dc",
      "DATA",
      [
        "storage",
        "00c75450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006978dc",
      "DATA",
      [
        "storage",
        "00c76420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069751c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697508.md#insn-0069751c) · [`00697524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697508.md#insn-00697524) · [`00697528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697508.md#insn-00697528)
- 新版 [`006978cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006978b8.md#insn-006978cc) · [`006978d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006978b8.md#insn-006978d4) · [`006978d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006978b8.md#insn-006978d8)

~~~diff
- 0069751c ["INT_ADD", "register:40f0:8", ["const:69751c:8", "const:4:8"]]
- 0069751c ["CALL", null, ["callee:00c58f30:8"]]
+ 006978cc ["INT_ADD", "register:40f0:8", ["const:6978cc:8", "const:4:8"]]
+ 006978cc ["CALL", null, ["callee:00c58f30:8"]]
- 0069751c bytes 91021794
+ 006978cc bytes 99051794
- 00697524 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006978d4 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 00697524 bytes e82e00d0
+ 006978d4 bytes e82e00f0
- 00697528 ["COPY", "tmp:0:8", ["const:450:8"]]
- 00697528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00697528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00697528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006978d8 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 006978d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006978d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006978d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00697528 bytes 08411191
+ 006978d8 bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35a9589c4e39d081ccd9e3e086ad79ff"></a>

### [`00697540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697540.md) → [`006978f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006978f0.md) FUN_006978f0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006978f4",
      "incomplete_value": false,
      "site": "006978f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
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
      "006978f8",
      "DATA",
      [
        "storage",
        "00c75450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006978f8",
      "DATA",
      [
        "storage",
        "00c76420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697540.md#insn-00697540) · [`00697544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697540.md#insn-00697544)
- 新版 [`006978f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006978f0.md#insn-006978f0) · [`006978f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006978f0.md#insn-006978f4)

~~~diff
- 00697540 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006978f0 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 00697540 bytes e82e00d0
+ 006978f0 bytes e82e00f0
- 00697544 ["COPY", "tmp:0:8", ["const:450:8"]]
- 00697544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00697544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00697544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006978f4 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 006978f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006978f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006978f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00697544 bytes 08411191
+ 006978f4 bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3f48e71acff7f1ed801b76faba55562"></a>

### [`00697560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697560.md) → [`00697910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697910.md) FUN_00697910

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f4c.md)

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
      "site": "00697948",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00697598",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "00697954",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006975a4",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "00697948",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00697954",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00697948",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00697954",
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

- 旧版 [`00697598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697560.md#insn-00697598) · [`006975a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697560.md#insn-006975a4) · [`0069757c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697560.md#insn-0069757c)
- 新版 [`00697948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697910.md#insn-00697948) · [`00697954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697910.md#insn-00697954) · [`0069792c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697910.md#insn-0069792c)

~~~diff
- 00697598 ["INT_ADD", "register:40f0:8", ["const:697598:8", "const:4:8"]]
- 00697598 ["CALL", null, ["ram:47ad34:8"]]
+ 00697948 ["INT_ADD", "register:40f0:8", ["const:697948:8", "const:4:8"]]
+ 00697948 ["CALL", null, ["ram:47b054:8"]]
- 00697598 bytes e78df797
+ 00697948 bytes c38df797
- 006975a4 ["INT_ADD", "register:40f0:8", ["const:6975a4:8", "const:4:8"]]
- 006975a4 ["CALL", null, ["ram:47ad34:8"]]
+ 00697954 ["INT_ADD", "register:40f0:8", ["const:697954:8", "const:4:8"]]
+ 00697954 ["CALL", null, ["ram:47b054:8"]]
- 006975a4 bytes e48df797
+ 00697954 bytes c08df797
- 0069757c ["INT_ADD", "register:40f0:8", ["const:69757c:8", "const:4:8"]]
- 0069757c ["CALL", null, ["callee:008b7f4c:8"]]
+ 0069792c ["INT_ADD", "register:40f0:8", ["const:69792c:8", "const:4:8"]]
+ 0069792c ["CALL", null, ["callee:008b7f4c:8"]]
- 0069757c bytes 897e0894
+ 0069792c bytes 88810894
~~~


<a id="compare-33f8717f1db12ab308d49a71af36ae87"></a>

### [`00697600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697600.md) → [`006979b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006979b0.md) FUN_006979b0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "006979bc",
      "incomplete_value": false,
      "site": "006979c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "006979c0",
      "DATA",
      [
        "storage",
        "00c754d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006979c0",
      "DATA",
      [
        "storage",
        "00c764a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697600.md#insn-00697608) · [`0069760c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697600.md#insn-0069760c)
- 新版 [`006979b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006979b0.md#insn-006979b8) · [`006979bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006979b0.md#insn-006979bc)

~~~diff
- 00697608 ["COPY", "register:4048:8", ["const:c75000:8"]]
+ 006979b8 ["COPY", "register:4048:8", ["const:c76000:8"]]
- 00697608 bytes e92e00d0
+ 006979b8 bytes e92e00f0
- 0069760c ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 0069760c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0069760c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0069760c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006979bc ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 006979bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006979bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006979bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0069760c bytes 29411391
+ 006979bc bytes 29811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-544dc19d6bbcb91193f86ce3dd70a050"></a>

### [`00697624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697624.md) → [`006979d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006979d4.md) FUN_006979d4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006979dc",
      "incomplete_value": false,
      "site": "006979e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "006979e0",
      "DATA",
      [
        "storage",
        "00c754d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006979e0",
      "DATA",
      [
        "storage",
        "00c764a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697624.md#insn-00697628) · [`0069762c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697624.md#insn-0069762c) · [`00697650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697624.md#insn-00697650)
- 新版 [`006979d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006979d4.md#insn-006979d8) · [`006979dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006979d4.md#insn-006979dc) · [`00697a00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/006979d4.md#insn-00697a00)

~~~diff
- 00697628 ["COPY", "register:4048:8", ["const:c75000:8"]]
+ 006979d8 ["COPY", "register:4048:8", ["const:c76000:8"]]
- 00697628 bytes e92e00d0
+ 006979d8 bytes e92e00f0
- 0069762c ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 0069762c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0069762c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0069762c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006979dc ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 006979dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006979dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006979dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0069762c bytes 29411391
+ 006979dc bytes 29811291
- 00697650 ["INT_ADD", "register:40f0:8", ["const:697650:8", "const:4:8"]]
- 00697650 ["CALL", null, ["callee:00c58f50:8"]]
+ 00697a00 ["INT_ADD", "register:40f0:8", ["const:697a00:8", "const:4:8"]]
+ 00697a00 ["CALL", null, ["callee:00c58f50:8"]]
- 00697650 bytes 4c021794
+ 00697a00 bytes 54051794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44cd4046c9c198a3d85eb40a926a64ba"></a>

### [`00697664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697664.md) → [`00697a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697a14.md) FUN_00697a14

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`006928cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928cc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

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
      "definition_site": "00697a34",
      "incomplete_value": false,
      "site": "00697a3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00697a3c",
      "DATA",
      [
        "storage",
        "00c754d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697a3c",
      "DATA",
      [
        "storage",
        "00c764a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069767c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697664.md#insn-0069767c) · [`00697680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697664.md#insn-00697680) · [`00697684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697664.md#insn-00697684)
- 新版 [`00697a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697a14.md#insn-00697a2c) · [`00697a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697a14.md#insn-00697a30) · [`00697a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697a14.md#insn-00697a34)

~~~diff
- 0069767c ["INT_ADD", "register:40f0:8", ["const:69767c:8", "const:4:8"]]
- 0069767c ["CALL", null, ["callee:00c58f30:8"]]
+ 00697a2c ["INT_ADD", "register:40f0:8", ["const:697a2c:8", "const:4:8"]]
+ 00697a2c ["CALL", null, ["callee:00c58f30:8"]]
- 0069767c bytes 39021794
+ 00697a2c bytes 41051794
- 00697680 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 00697a30 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 00697680 bytes e82e00d0
+ 00697a30 bytes e82e00f0
- 00697684 ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 00697684 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00697684 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00697684 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00697a34 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 00697a34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00697a34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00697a34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00697684 bytes 08411391
+ 00697a34 bytes 08811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7efaa58fcfd07e427e47de7822abe99f"></a>

### [`0069771c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/0069771c.md) → [`00697acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697acc.md) FUN_00697acc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`006928cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928cc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 75.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00697ae0",
      "incomplete_value": false,
      "site": "00697ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00697778"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00697b28"
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
      "00697ae8",
      "DATA",
      [
        "storage",
        "00c754d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697ae8",
      "DATA",
      [
        "storage",
        "00c764a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/0069771c.md#insn-00697778) · [`0069772c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/0069771c.md#insn-0069772c)
- 新版 [`00697b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697acc.md#insn-00697b28) · [`00697adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697acc.md#insn-00697adc)

~~~diff
- 00697778 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
- 00697778 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00697778 bytes 741600f9
+ 00697b28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
+ 00697b28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00697b28 bytes 741600f9
- 0069772c ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 00697adc ["COPY", "register:4040:8", ["const:c76000:8"]]
- 0069772c bytes e82e00d0
+ 00697adc bytes e82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38fd5a0fba89d9bc118dbb0bdc522ff5"></a>

### [`006977bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006977bc.md) → [`00697b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697b6c.md) FUN_00697b6c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006977c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006977bc.md#insn-006977c4)
- 新版 [`00697b74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697b6c.md#insn-00697b74)

~~~diff
- 006977c4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 006977c4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00697b74 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00697b74 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 006977c4 bytes 600000b4
+ 00697b74 bytes 600000b4
~~~


<a id="compare-c1363bbadbd5d6bfc15cce8fde50e4a0"></a>

### [`006977d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006977d4.md) → [`00697b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697b84.md) FUN_00697b84

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0068f630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0068f9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068f/0068f9e0.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_condition` 4件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006977d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00697b88"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "006977d8"
      ],
      [
        "FALL_THROUGH",
        "00697b88"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00697b88",
      "incomplete_value": true,
      "site": "00697b8c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006977d8",
      "incomplete_value": true,
      "site": "006977dc",
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
      "unmatched:006977d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00697bb4"
      ]
    ]
  ],
  "added": [
    [
      "00697b88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00697bb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006977d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006977d4.md#insn-006977d8) · [`006977d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006977d4.md#insn-006977d4)
- 新版 [`00697b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697b84.md#insn-00697b88)

~~~diff
- 006977d8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 006977d8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 006977d8 bytes 680100b4
+ 00697b88 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00697b88 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00697b88 bytes 680100b4
- 006977d4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:18:8"]]
- 006977d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006977d4 bytes 080c40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-612edb717fe979ab15e99d938039873e"></a>

### [`00697e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e14.md) → [`006981c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006981c4.md) FUN_006981c4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00697e24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006981d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00697e28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00697e24",
      "DATA",
      [
        "storage",
        "00c75550",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00697e28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006981e4"
      ]
    ]
  ],
  "added": [
    [
      "006981d4",
      "DATA",
      [
        "storage",
        "00c76520",
        null,
        "undefined *"
      ]
    ],
    [
      "006981d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006981e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e14.md#insn-00697e24) · [`00697e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e14.md#insn-00697e28)
- 新版 [`006981d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006981c4.md#insn-006981d4)

~~~diff
- 00697e24 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00697e24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00697e24 bytes 090100f9
- 00697e28 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00697e28 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00697e28 bytes 600000b4
+ 006981d4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 006981d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 006981d4 bytes 090100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d37114d2643dc01bf048792b1092a44"></a>

### [`00697e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e38.md) → [`006981e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006981e8.md) FUN_006981e8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00697e44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006981f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00697e48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00697e44",
      "DATA",
      [
        "storage",
        "00c75550",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00697e48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00698224"
      ]
    ]
  ],
  "added": [
    [
      "006981f4",
      "DATA",
      [
        "storage",
        "00c76520",
        null,
        "undefined *"
      ]
    ],
    [
      "006981f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00698224"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e38.md#insn-00697e44) · [`00697e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e38.md#insn-00697e48)
- 新版 [`006981f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006981e8.md#insn-006981f4)

~~~diff
- 00697e44 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00697e44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00697e44 bytes 090000f9
- 00697e48 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00697e48 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00697e48 bytes 680100b4
+ 006981f4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 006981f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 006981f4 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2c34ac3357a6b154c5f242bb9787997"></a>

### [`00697e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e78.md) → [`00698228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698228.md) FUN_00698228

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`006928cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928cc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 25.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00697ea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00697eb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00697ebc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00697ea0",
      "DATA",
      [
        "storage",
        "00c75550",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00697ec8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006982a4"
      ]
    ]
  ],
  "added": [
    [
      "00698250",
      "DATA",
      [
        "storage",
        "00c76520",
        null,
        "undefined *"
      ]
    ],
    [
      "00698278",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006982a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e78.md#insn-00697ea0) · [`00697eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e78.md#insn-00697eb4) · [`00697ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e78.md#insn-00697ebc)

~~~diff
- 00697ea0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00697ea0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00697ea0 bytes 080000f9
- 00697eb4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00697eb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00697eb4 bytes 0080803c
- 00697ebc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:18:8"]]
- 00697ebc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00697ebc bytes 091800b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3f8b26e22cfba7887898ceeef6ff7f6"></a>

### [`00697f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697f38.md) → [`006982e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006982e8.md) FUN_006982e8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0069251c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069251c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`006928cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00692/006928cc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 45.45% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006982fc",
      "incomplete_value": false,
      "site": "00698304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00697f4c",
      "incomplete_value": false,
      "site": "00697f54",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00697f9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0069834c"
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
      "00698304",
      "DATA",
      [
        "storage",
        "00c75550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00698304",
      "DATA",
      [
        "storage",
        "00c76520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697f38.md#insn-00697f9c) · [`00697fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697f38.md#insn-00697fa0) · [`00697fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697f38.md#insn-00697fd4)
- 新版 [`00698350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006982e8.md#insn-00698350) · [`00698384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006982e8.md#insn-00698384)

~~~diff
- 00697f9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
- 00697f9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00697f9c bytes 741a00f9
- 00697fa0 ["INT_ADD", "register:40f0:8", ["const:697fa0:8", "const:4:8"]]
- 00697fa0 ["CALL", null, ["callee:00c590a0:8"]]
+ 00698350 ["INT_ADD", "register:40f0:8", ["const:698350:8", "const:4:8"]]
+ 00698350 ["CALL", null, ["callee:00c590a0:8"]]
- 00697fa0 bytes 4c001794
+ 00698350 bytes 54031794
- 00697fd4 ["INT_ADD", "register:40f0:8", ["const:697fd4:8", "const:4:8"]]
- 00697fd4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00698384 ["INT_ADD", "register:40f0:8", ["const:698384:8", "const:4:8"]]
+ 00698384 ["CALL", null, ["callee:00c58f50:8"]]
- 00697fd4 bytes ebff1694
+ 00698384 bytes f3021794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e722639b23489a89992ca9a97b4b2c82"></a>

### [`00697ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697ff8.md) → [`006983a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006983a8.md) FUN_006983a8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0068f630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0068f9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068f/0068f9e0.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00698014",
      "incomplete_value": true,
      "site": "00698018",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00698018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697ff8.md#insn-00698018) · [`00697ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697ff8.md#insn-00697ffc)
- 新版 [`006983c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006983a8.md#insn-006983c8) · [`006983ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006983a8.md#insn-006983ac)

~~~diff
- 00698018 ["INT_ADD", "register:40f0:8", ["const:698018:8", "const:4:8"]]
- 00698018 ["CALL", null, ["callee:00c58f50:8"]]
+ 006983c8 ["INT_ADD", "register:40f0:8", ["const:6983c8:8", "const:4:8"]]
+ 006983c8 ["CALL", null, ["callee:00c58f50:8"]]
- 00698018 bytes daff1694
+ 006983c8 bytes e2021794
- 00697ffc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00697ffc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 006983ac ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 006983ac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00697ffc bytes 680100b4
+ 006983ac bytes 680100b4
~~~


<a id="compare-4f2436eadedb4e0c9e16c36b56392c4d"></a>

### [`0069802c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/0069802c.md) → [`006983dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006983dc.md) FUN_006983dc

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 28件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md)
- 新版 呼出元 0件  · 呼出先 28件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`004682b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004682b4.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 13.85% / 新版 13.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 36件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00698184"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006981c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00698438"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006980a0",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:006980a4",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:006980ac",
      "PARAM",
      [
        "storage",
        "00c750a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00698450",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00698454",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "0069845c",
      "PARAM",
      [
        "storage",
        "00c76078",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00698070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/0069802c.md#insn-00698070) · [`00698084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/0069802c.md#insn-00698084) · [`006980b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/0069802c.md#insn-006980b8)
- 新版 [`00698420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006983dc.md#insn-00698420) · [`00698434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006983dc.md#insn-00698434) · [`00698468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006983dc.md#insn-00698468)

~~~diff
- 00698070 ["INT_ADD", "register:40f0:8", ["const:698070:8", "const:4:8"]]
- 00698070 ["CALL", null, ["callee:008ba294:8"]]
+ 00698420 ["INT_ADD", "register:40f0:8", ["const:698420:8", "const:4:8"]]
+ 00698420 ["CALL", null, ["callee:008ba294:8"]]
- 00698070 bytes 9e840894
+ 00698420 bytes 9d870894
- 00698084 ["INT_ADD", "register:40f0:8", ["const:698084:8", "const:4:8"]]
- 00698084 ["CALL", null, ["callee:008ba29c:8"]]
+ 00698434 ["INT_ADD", "register:40f0:8", ["const:698434:8", "const:4:8"]]
+ 00698434 ["CALL", null, ["callee:008ba29c:8"]]
- 00698084 bytes 9b840894
+ 00698434 bytes 9a870894
- 006980b8 ["INT_ADD", "register:40f0:8", ["const:6980b8:8", "const:4:8"]]
- 006980b8 ["CALL", null, ["callee:00c596b0:8"]]
+ 00698468 ["INT_ADD", "register:40f0:8", ["const:698468:8", "const:4:8"]]
+ 00698468 ["CALL", null, ["callee:00c596b0:8"]]
- 006980b8 bytes 8a011794
+ 00698468 bytes 92041794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc814db1c2209ea71be458f4eeae3306"></a>

### [`00698788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698788.md) → [`00698b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698b38.md) FUN_00698b38

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00698b58",
      "incomplete_value": false,
      "site": "00698b5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006987a8",
      "incomplete_value": false,
      "site": "006987ac",
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
            "const:5d0:8"
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
      "00698b5c",
      "DATA",
      [
        "storage",
        "00c755d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00698b5c",
      "DATA",
      [
        "storage",
        "00c765a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069879c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698788.md#insn-0069879c) · [`006987a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698788.md#insn-006987a4) · [`006987a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698788.md#insn-006987a8)
- 新版 [`00698b4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698b38.md#insn-00698b4c) · [`00698b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698b38.md#insn-00698b54) · [`00698b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698b38.md#insn-00698b58)

~~~diff
- 0069879c ["INT_ADD", "register:40f0:8", ["const:69879c:8", "const:4:8"]]
- 0069879c ["CALL", null, ["callee:00c58f30:8"]]
+ 00698b4c ["INT_ADD", "register:40f0:8", ["const:698b4c:8", "const:4:8"]]
+ 00698b4c ["CALL", null, ["callee:00c58f30:8"]]
- 0069879c bytes f1fd1694
+ 00698b4c bytes f9001794
- 006987a4 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 00698b54 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006987a4 bytes e82e00b0
+ 00698b54 bytes e82e00d0
- 006987a8 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 006987a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006987a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006987a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00698b58 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 00698b58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00698b58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00698b58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006987a8 bytes 08411791
+ 00698b58 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d1a6a73e7ddace5f902113ef096348b"></a>

### [`006987c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006987c0.md) → [`00698b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698b70.md) FUN_00698b70

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00698b74",
      "incomplete_value": false,
      "site": "00698b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006987c4",
      "incomplete_value": false,
      "site": "006987c8",
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
            "const:5d0:8"
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
      "00698b78",
      "DATA",
      [
        "storage",
        "00c755d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00698b78",
      "DATA",
      [
        "storage",
        "00c765a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006987c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006987c0.md#insn-006987c0) · [`006987c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006987c0.md#insn-006987c4)
- 新版 [`00698b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698b70.md#insn-00698b70) · [`00698b74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698b70.md#insn-00698b74)

~~~diff
- 006987c0 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 00698b70 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006987c0 bytes e82e00b0
+ 00698b70 bytes e82e00d0
- 006987c4 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 006987c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006987c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006987c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00698b74 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 00698b74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00698b74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00698b74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006987c4 bytes 08411791
+ 00698b74 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-341aad796c2da25efb11ced81d4327a3"></a>

### [`006987e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006987e0.md) → [`00698b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698b90.md) FUN_00698b90

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0068f630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b79a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b79a0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0068f9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068f/0068f9e0.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b894c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b894c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.58% / 新版 81.58%

CFGの説明率　旧版 11.11% / 新版 6.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698858"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00698c08"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0069882c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00698810",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:0069882c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00698c1c"
      ]
    ],
    [
      "unmatched:00698830",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ]
  ],
  "added": [
    [
      "00698bc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00698bdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00698c1c"
      ]
    ],
    [
      "00698be0",
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

- 旧版 [`00698810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006987e0.md#insn-00698810) · [`0069882c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006987e0.md#insn-0069882c) · [`00698830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006987e0.md#insn-00698830)

~~~diff
- 00698810 ["INT_ADD", "register:40f0:8", ["const:698810:8", "const:4:8"]]
- 00698810 ["CALL", null, ["ram:47ad34:8"]]
- 00698810 bytes 4989f797
- 0069882c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0069882c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 0069882c bytes 01020054
- 00698830 ["INT_ADD", "register:40f0:8", ["const:698830:8", "const:4:8"]]
- 00698830 ["CALL", null, ["callee:008524fc:8"]]
- 00698830 bytes 48e30694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-839d727b33807cd81307d4b29ddbf9bc"></a>

### [`006988fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006988fc.md) → [`00698cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698cac.md) FUN_00698cac

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa0.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f4c.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 21.43% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00698cc4",
      "incomplete_value": true,
      "site": "00698cc8",
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
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00698934"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00698cfc",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0069894c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "unmatched:00698934",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00698cfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00698ce4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00698cfc",
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

- 旧版 [`00698918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006988fc.md#insn-00698918) · [`00698934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006988fc.md#insn-00698934) · [`00698948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006988fc.md#insn-00698948)
- 新版 [`00698cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698cac.md#insn-00698cc8)

~~~diff
- 00698918 ["INT_ADD", "register:40f0:8", ["const:698918:8", "const:4:8"]]
- 00698918 ["CALL", null, ["callee:008b7f4c:8"]]
+ 00698cc8 ["INT_ADD", "register:40f0:8", ["const:698cc8:8", "const:4:8"]]
+ 00698cc8 ["CALL", null, ["callee:008b7f4c:8"]]
- 00698918 bytes a2790894
+ 00698cc8 bytes a17c0894
- 00698934 ["INT_ADD", "register:40f0:8", ["const:698934:8", "const:4:8"]]
- 00698934 ["CALL", null, ["ram:47ad34:8"]]
- 00698934 bytes 0089f797
- 00698948 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00698948 ["RETURN", null, ["register:0:8"]]
- 00698948 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba7c745d020ce1b7bf7b1f2fda62cdc7"></a>

### [`006989a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006989a0.md) → [`00698d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698d50.md) FUN_00698d50

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

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
      "site": "006989a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006989a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006989a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006989a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006989a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006989c4",
      "DATA",
      [
        "storage",
        "00c756d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00698d50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00698d54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00698d74",
      "DATA",
      [
        "storage",
        "00c766a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006989a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006989a0.md#insn-006989a0) · [`006989a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006989a0.md#insn-006989a4) · [`006989b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006989a0.md#insn-006989b4)
- 新版 [`00698d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698d50.md#insn-00698d64)

~~~diff
- 006989a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006989a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006989a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 006989a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 006989a0 bytes fd7bbea9
- 006989a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 006989a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 006989a4 bytes f30b00f9
- 006989b4 ["INT_ADD", "register:40f0:8", ["const:6989b4:8", "const:4:8"]]
- 006989b4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00698d64 ["INT_ADD", "register:40f0:8", ["const:698d64:8", "const:4:8"]]
+ 00698d64 ["CALL", null, ["callee:00c58f30:8"]]
- 006989b4 bytes 6bfd1694
+ 00698d64 bytes 73001794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b4416b8cde0e61e0f20873255909ccd"></a>

### [`006989f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006989f0.md) → [`00698da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698da0.md) FUN_00698da0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`008b6ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6ab4.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md) [`008b92e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92e8.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008b7a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7a60.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md) [`008ba294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba294.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 20.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006989f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006989f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006989f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006989f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006989f4",
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
      "00698da0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00698da4",
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

- 旧版 [`006989f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006989f0.md#insn-006989f0) · [`006989f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006989f0.md#insn-006989f4) · [`00698a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006989f0.md#insn-00698a08)
- 新版 [`00698db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698da0.md#insn-00698db8)

~~~diff
- 006989f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006989f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006989f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 006989f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 006989f0 bytes fd7bbea9
- 006989f4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 006989f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 006989f4 bytes f30b00f9
- 00698a08 ["INT_ADD", "register:40f0:8", ["const:698a08:8", "const:4:8"]]
- 00698a08 ["CALL", null, ["callee:008ba294:8"]]
+ 00698db8 ["INT_ADD", "register:40f0:8", ["const:698db8:8", "const:4:8"]]
+ 00698db8 ["CALL", null, ["callee:008ba294:8"]]
- 00698a08 bytes 38820894
+ 00698db8 bytes 37850894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-358440ba0e570f73ae6e9d9fb8665c59"></a>

### [`00698ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698ad0.md) → [`00698e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698e80.md) FUN_00698e80

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 16件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046a928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a928.md) [`0046af4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af4c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046ac48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046a/0046ac48.md) [`0046b26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046b/0046b26c.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.81% / 新版 86.81%

CFGの説明率　旧版 26.67% / 新版 26.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 15件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698aec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698aec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698b00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00698aec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00698b00",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00698ee0",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00698e9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00698eb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00698ee0",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00698aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698ad0.md#insn-00698aec) · [`00698b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698ad0.md#insn-00698b00) · [`00698b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698ad0.md#insn-00698b34)
- 新版 [`00698ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/00698e80.md#insn-00698ee4)

~~~diff
- 00698aec ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00698aec ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00698aec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00698aec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00698aec bytes f44f08a9
- 00698b00 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00698b00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00698b00 bytes e80f00f9
- 00698b34 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00698b34 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00698ee4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00698ee4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00698b34 bytes 200100b4
+ 00698ee4 bytes 200100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2b81b4fae9a53de78dc590e81f61a21"></a>

### [`00698e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698e0c.md) → [`006991bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/006991bc.md) FUN_006991bc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006991c0",
      "incomplete_value": false,
      "site": "006991c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00698e10",
      "incomplete_value": false,
      "site": "00698e14",
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
            "const:7d0:8"
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
      "006991c4",
      "DATA",
      [
        "storage",
        "00c757d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006991c4",
      "DATA",
      [
        "storage",
        "00c767a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00698e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698e0c.md#insn-00698e0c) · [`00698e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698e0c.md#insn-00698e10)
- 新版 [`006991bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/006991bc.md#insn-006991bc) · [`006991c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/006991bc.md#insn-006991c0)

~~~diff
- 00698e0c ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006991bc ["COPY", "register:4040:8", ["const:c76000:8"]]
- 00698e0c bytes e82e00b0
+ 006991bc bytes e82e00b0
- 00698e10 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 00698e10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00698e10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00698e10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006991c0 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 006991c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006991c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006991c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00698e10 bytes 08411f91
+ 006991c0 bytes 08811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bcef4a89d8fac35e17302c22ce65765"></a>

### [`00698e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698e2c.md) → [`006991dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/006991dc.md) FUN_006991dc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`006882d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00688/006882d4.md) [`0068978c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/0068978c.md) [`0068edd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068edd8.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`00688684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00688/00688684.md) [`00689b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00689/00689b3c.md) [`0068f188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068f/0068f188.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00698e60"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00698eec"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00698efc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00698e60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:00698eec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "unmatched:00698efc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d254"
      ]
    ]
  ],
  "added": [
    [
      "00699210",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "0069929c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c2e0"
      ]
    ],
    [
      "006992ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d604"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00698e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698e2c.md#insn-00698e60) · [`00698eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698e2c.md#insn-00698eec) · [`00698efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698e2c.md#insn-00698efc)

~~~diff
- 00698e60 ["INT_ADD", "register:40f0:8", ["const:698e60:8", "const:4:8"]]
- 00698e60 ["CALL", null, ["ram:47ad34:8"]]
- 00698e60 bytes b587f797
- 00698eec ["INT_ADD", "register:40f0:8", ["const:698eec:8", "const:4:8"]]
- 00698eec ["CALL", null, ["ram:71bf30:8"]]
- 00698eec bytes 110c0294
- 00698efc ["INT_ADD", "register:40f0:8", ["const:698efc:8", "const:4:8"]]
- 00698efc ["CALL", null, ["ram:71d254:8"]]
- 00698efc bytes d6100294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0318c044e133eda66164c5bb8c677d7"></a>

### [`00698f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698f90.md) → [`00699340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/00699340.md) FUN_00699340

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00699344",
      "incomplete_value": false,
      "site": "00699348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00698f94",
      "incomplete_value": false,
      "site": "00698f98",
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
            "const:850:8"
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
      "00699348",
      "DATA",
      [
        "storage",
        "00c75850",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00699348",
      "DATA",
      [
        "storage",
        "00c76820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00698f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698f90.md#insn-00698f90) · [`00698f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698f90.md#insn-00698f94)
- 新版 [`00699340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/00699340.md#insn-00699340) · [`00699344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/00699340.md#insn-00699344)

~~~diff
- 00698f90 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 00699340 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 00698f90 bytes e82e00b0
+ 00699340 bytes e82e00b0
- 00698f94 ["COPY", "tmp:0:8", ["const:850:8"]]
- 00698f94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00698f94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00698f94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00699344 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 00699344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00699344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00699344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00698f94 bytes 08412191
+ 00699344 bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c38b45fc8eb076b80a2e4bd8c1247c0e"></a>

### [`00698fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698fb0.md) → [`00699360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/00699360.md) FUN_00699360

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa0.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f4c.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 23.08% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00698fc8",
      "incomplete_value": true,
      "site": "00698fcc",
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
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00698fe8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00699000"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00699390",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00699000"
      ]
    ],
    [
      "unmatched:00698fe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:00699000",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00699390",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006993b0"
      ]
    ],
    [
      "00699398",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006993b0",
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

- 旧版 [`00698fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698fb0.md#insn-00698fcc) · [`00698fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698fb0.md#insn-00698fe8) · [`00699000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698fb0.md#insn-00699000)
- 新版 [`0069937c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/00699360.md#insn-0069937c)

~~~diff
- 00698fcc ["INT_ADD", "register:40f0:8", ["const:698fcc:8", "const:4:8"]]
- 00698fcc ["CALL", null, ["callee:008b7f4c:8"]]
+ 0069937c ["INT_ADD", "register:40f0:8", ["const:69937c:8", "const:4:8"]]
+ 0069937c ["CALL", null, ["callee:008b7f4c:8"]]
- 00698fcc bytes f5770894
+ 0069937c bytes f47a0894
- 00698fe8 ["INT_ADD", "register:40f0:8", ["const:698fe8:8", "const:4:8"]]
- 00698fe8 ["CALL", null, ["ram:47ad34:8"]]
- 00698fe8 bytes 5387f797
- 00699000 ["INT_ADD", "register:40f0:8", ["const:699000:8", "const:4:8"]]
- 00699000 ["CALL", null, ["ram:47ad34:8"]]
- 00699000 bytes 4d87f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5106b340daa6433a960f3583825c9d9"></a>

### [`006990a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006990a4.md) → [`00699454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/00699454.md) FUN_00699454

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085b2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b2fc.md) [`0085b304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b304.md) [`008b6ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6ab4.md) [`008b6eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6eb0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`0085c2a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c2a8.md) [`0085c2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c2b0.md) [`008b7a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7a60.md) [`008b7e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7e5c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 82.57% / 新版 82.57%

CFGの説明率　旧版 4.76% / 新版 5.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0069915c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0069950c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "006990d8",
      "incomplete_value": true,
      "site": "006990e4",
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
            "const:2f38:8"
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
      "unmatched:0069915c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006995b4"
      ]
    ],
    [
      "unmatched:00699160",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "unmatched:00699164",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0085c2b0"
      ]
    ]
  ],
  "added": [
    [
      "0069950c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006995b4"
      ]
    ],
    [
      "00699510",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "00699514",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0085c2b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006990e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006990a4.md#insn-006990e4) · [`0069915c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006990a4.md#insn-0069915c) · [`00699160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006990a4.md#insn-00699160)
- 新版 [`00699494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/00699454.md#insn-00699494)

~~~diff
- 006990e4 ["INT_ADD", "register:40f0:8", ["const:6990e4:8", "const:4:8"]]
- 006990e4 ["CALL", null, ["callee:008b89cc:8"]]
+ 00699494 ["INT_ADD", "register:40f0:8", ["const:699494:8", "const:4:8"]]
+ 00699494 ["CALL", null, ["callee:008b89cc:8"]]
- 006990e4 bytes 4f7a0894
+ 00699494 bytes 4e7d0894
- 0069915c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 0069915c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 0069915c bytes 4b050054
- 00699160 ["INT_ADD", "register:40f0:8", ["const:699160:8", "const:4:8"]]
- 00699160 ["CALL", null, ["callee:008524fc:8"]]
- 00699160 bytes fce00694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef683fa31c16f319f0a400702a5a47a5"></a>

### [`006992d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006992d4.md) → [`00699684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/00699684.md) FUN_00699684

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 16件 [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`00687b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687b8c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046cde4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cde4.md) [`0048a2ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2ac.md) [`00687f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00687/00687f3c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.23% / 新版 80.23%

CFGの説明率　旧版 7.41% / 新版 6.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006992fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006996ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00699370"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006992fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00699320",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:00699324",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006996ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "006996d0",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006996d4",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006992fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006992d4.md#insn-006992fc) · [`00699334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006992d4.md#insn-00699334) · [`00699370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006992d4.md#insn-00699370)
- 新版 [`006996e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/00699684.md#insn-006996e4)

~~~diff
- 006992fc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006992fc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 006992fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 006992fc bytes a8831ff8
- 00699334 ["INT_ADD", "register:40f0:8", ["const:699334:8", "const:4:8"]]
- 00699334 ["CALL", null, ["callee:00c596b0:8"]]
+ 006996e4 ["INT_ADD", "register:40f0:8", ["const:6996e4:8", "const:4:8"]]
+ 006996e4 ["CALL", null, ["callee:00c596b0:8"]]
- 00699334 bytes ebfc1694
+ 006996e4 bytes f3ff1694
- 00699370 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00699370 ["COPY", "tmp:1:4", ["register:40b8:4"]]
- 00699370 ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 00699370 ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 00699370 bytes e8a6971a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1471df39225010b531e7945346d2f80b"></a>

### [`006995d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006995d0.md) → [`00699980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/00699980.md) _INIT_101

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.84% / 新版 63.84%

CFGの説明率　旧版 31.58% / 新版 35.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006995d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006995d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006995d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006995d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:006995d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006995dc",
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
      "00699984",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00699988",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0069998c",
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

- 旧版 [`006995d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006995d0.md#insn-006995d4) · [`006995d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006995d0.md#insn-006995d8) · [`006995dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006995d0.md#insn-006995dc)

~~~diff
- 006995d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006995d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006995d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 006995d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006995d4 bytes fd7b0fa9
- 006995d8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 006995d8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 006995d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 006995d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006995d8 bytes fc5710a9
- 006995dc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 006995dc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 006995dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 006995dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006995dc bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1a5ff613eff3317ddd668b6d0c1dfe6"></a>

### [`00699960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/00699960.md) → [`00699d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/00699d10.md) FUN_00699d10

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0069a55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md) · 呼出先 28件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md)
- 新版 呼出元 1件 [`0069a90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0069a/0069a90c.md) · 呼出先 28件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.73% / 新版 80.73%

CFGの説明率　旧版 49.58% / 新版 48.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_value` 4件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 24件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00699990"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006999ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00699e10",
      "incomplete_value": true,
      "site": "00699e20",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:db6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00699a60",
      "incomplete_value": true,
      "site": "00699a70",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:cdf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00699990",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00699994",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00488180"
      ]
    ],
    [
      "unmatched:006999ac",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00699d40",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00699d44",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00488180"
      ]
    ],
    [
      "00699d5c",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00699990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/00699960.md#insn-00699990) · [`006999ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/00699960.md#insn-006999ac) · [`00699ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/00699960.md#insn-00699ab8)

~~~diff
- 00699990 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00699990 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00699990 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00699990 bytes a8031ff8
- 006999ac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:98:8"]]
- 006999ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006999ac bytes e84f00f9
- 00699ab8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:68:8"]]
- 00699ab8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00699ab8 bytes 683600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a55d2c44d8410614288e45ea385207d"></a>

### [`0069a4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a4b0.md) → [`0069a860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0069a/0069a860.md) FUN_0069a860

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 2件 [`0089b2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089b2e4.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 3件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)
- 新版 呼出元 2件 [`0089c290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089c290.md) [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 3件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 85.71% / 新版 90.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0069a8cc",
      "incomplete_value": false,
      "site": "0069a8d0",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0069a51c",
      "incomplete_value": false,
      "site": "0069a520",
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
      "0069a8cc",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0069a8cc",
      "PARAM",
      [
        "storage",
        "002a01b0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069a520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a4b0.md#insn-0069a520) · [`0069a4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a4b0.md#insn-0069a4c4) · [`0069a4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a4b0.md#insn-0069a4cc)
- 新版 [`0069a8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0069a/0069a860.md#insn-0069a8d0) · [`0069a874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0069a/0069a860.md#insn-0069a874) · [`0069a87c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0069a/0069a860.md#insn-0069a87c)

~~~diff
- 0069a520 ["INT_ADD", "register:40f0:8", ["const:69a520:8", "const:4:8"]]
- 0069a520 ["CALL", null, ["callee:00442c90:8"]]
+ 0069a8d0 ["INT_ADD", "register:40f0:8", ["const:69a8d0:8", "const:4:8"]]
+ 0069a8d0 ["CALL", null, ["callee:00442c90:8"]]
- 0069a520 bytes 14a1f697
+ 0069a8d0 bytes f0a0f697
- 0069a4c4 ["INT_ADD", "register:40f0:8", ["const:69a4c4:8", "const:4:8"]]
- 0069a4c4 ["CALL", null, ["callee:00c59180:8"]]
+ 0069a874 ["INT_ADD", "register:40f0:8", ["const:69a874:8", "const:4:8"]]
+ 0069a874 ["CALL", null, ["callee:00c59180:8"]]
- 0069a4c4 bytes 3bf71694
+ 0069a874 bytes 43fa1694
- 0069a4cc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0069a4cc ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 0069a87c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 0069a87c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 0069a4cc bytes c80200b4
+ 0069a87c bytes c80200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-add72fb0cebc537d84f2e918e2a60018"></a>

### [`0069a55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md) → [`0069a90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0069a/0069a90c.md) FUN_0069a90c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005ba7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba7d8.md) [`0089b2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089b2e4.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) [`00a89b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a89/00a89b40.md) · 呼出先 62件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0059769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059769c.md) [`00597728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597728.md)
- 新版 呼出元 4件 [`005bab88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005bab88.md) [`0089c290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089c290.md) [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) [`00a8ab34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a8a/00a8ab34.md) · 呼出先 62件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`005979bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979bc.md) [`00597a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597a48.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 67.41% / 新版 67.41%

CFGの説明率　旧版 35.11% / 新版 35.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 47件, `call_target` 2件, `store_condition` 5件, `unresolved_branch_alignment` 229件, `unresolved_call_alignment` 176件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 166件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069a574"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069a574"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069a580"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0069a574",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0069a580",
      "WRITE",
      [
        "storage",
        "Stack[-0x304]",
        null,
        null
      ]
    ],
    [
      "unmatched:0069a58c",
      "WRITE",
      [
        "storage",
        "Stack[-0x348]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0069a924",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0069a930",
      "WRITE",
      [
        "storage",
        "Stack[-0x304]",
        null,
        null
      ]
    ],
    [
      "0069a93c",
      "WRITE",
      [
        "storage",
        "Stack[-0x348]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069a574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md#insn-0069a574) · [`0069a580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md#insn-0069a580) · [`0069a58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md#insn-0069a58c)

~~~diff
- 0069a574 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0069a574 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0069a574 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 0069a574 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0069a574 bytes f44f06a9
- 0069a580 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:6c:8"]]
- 0069a580 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
- 0069a580 bytes e16f00b9
- 0069a58c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 0069a58c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0069a58c bytes e81700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6cf5db8bb02cf122ee0a663ab0299b1"></a>

### [`0069e968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069e968.md) → [`0069ed18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0069e/0069ed18.md) FUN_0069ed18

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 10件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0063499c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00634/0063499c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0089cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089cc90.md) [`00a07d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a07/00a07d9c.md) · 呼出先 10件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00634d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00634/00634d4c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.66% / 新版 88.66%

CFGの説明率　旧版 41.18% / 新版 35.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069ea9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0069ee4c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0069e9d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0069e9d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069ee6c"
      ]
    ],
    [
      "unmatched:0069ea44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069ee90"
      ]
    ]
  ],
  "added": [
    [
      "0069ed88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069ee6c"
      ]
    ],
    [
      "0069edf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069ee90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069e9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069e968.md#insn-0069e9d8) · [`0069ea44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069e968.md#insn-0069ea44) · [`0069ea58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069e968.md#insn-0069ea58)

~~~diff
- 0069e9d8 ["CBRANCH", null, ["local:b23:8", "register:101:1"]]
- 0069e9d8 bytes 20070054
- 0069ea44 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 0069ea44 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 0069ea44 bytes ea0400b5
- 0069ea58 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0069ea58 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0069ea58 ["COPY", "tmp:2:8", ["register:4050:8"]]
- 0069ea58 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 0069ea58 bytes 4881889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

