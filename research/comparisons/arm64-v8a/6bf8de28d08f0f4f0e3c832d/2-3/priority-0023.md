# v16.0.2 → v16.0.3 · 最優先の変更候補 (23)

[一覧の目次](README.md)

<a id="compare-9042d302888e0885d5f34f0f28e15d9a"></a>

### [`005b5b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5b20.md) → [`005b5ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b5/005b5ed0.md) FUN_005b5ed0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`005b2330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2330.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048eb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048eb40.md) [`005b26e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b2/005b26e0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

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
      "site": "005b5eec",
      "value": [
        "leaf",
        "ram:48d058:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b5b3c",
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
      "005b5eec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ],
  "added": [
    [
      "005b5eec",
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

- 旧版 [`005b5b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5b20.md#insn-005b5b3c) · [`005b5b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5b20.md#insn-005b5b40)
- 新版 [`005b5eec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b5/005b5ed0.md#insn-005b5eec) · [`005b5ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b5/005b5ed0.md#insn-005b5ef0)

~~~diff
- 005b5b3c ["INT_ADD", "register:40f0:8", ["const:5b5b3c:8", "const:4:8"]]
- 005b5b3c ["CALL", null, ["ram:48cd38:8"]]
+ 005b5eec ["INT_ADD", "register:40f0:8", ["const:5b5eec:8", "const:4:8"]]
+ 005b5eec ["CALL", null, ["ram:48d058:8"]]
- 005b5b3c bytes 7f5cfb97
+ 005b5eec bytes 5b5cfb97
- 005b5b40 ["INT_ADD", "register:40f0:8", ["const:5b5b40:8", "const:4:8"]]
- 005b5b40 ["CALL", null, ["callee:0048eb40:8"]]
+ 005b5ef0 ["INT_ADD", "register:40f0:8", ["const:5b5ef0:8", "const:4:8"]]
+ 005b5ef0 ["CALL", null, ["callee:0048eb40:8"]]
- 005b5b40 bytes 3863fb97
+ 005b5ef0 bytes 1463fb97
~~~


<a id="compare-90cc70734c501ceb923c7561603729f6"></a>

### [`005b5c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c3c.md) → [`005b5fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b5/005b5fec.md) FUN_005b5fec

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b5c60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b5c60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b6010"
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
      "unmatched:005b5c60",
      "DATA",
      [
        "storage",
        "00c6fc90",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b5c64",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b5c68",
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
      "005b6010",
      "DATA",
      [
        "storage",
        "00c70c60",
        null,
        "undefined *"
      ]
    ],
    [
      "005b6014",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b6018",
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

- 旧版 [`005b5c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c3c.md#insn-005b5c50) · [`005b5c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c3c.md#insn-005b5c60) · [`005b5c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c3c.md#insn-005b5c6c)
- 新版 [`005b6000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b5/005b5fec.md#insn-005b6000)

~~~diff
- 005b5c50 ["INT_ADD", "register:40f0:8", ["const:5b5c50:8", "const:4:8"]]
- 005b5c50 ["CALL", null, ["callee:00c58f30:8"]]
+ 005b6000 ["INT_ADD", "register:40f0:8", ["const:5b6000:8", "const:4:8"]]
+ 005b6000 ["CALL", null, ["callee:00c58f30:8"]]
- 005b5c50 bytes c4881a94
+ 005b6000 bytes cc8b1a94
- 005b5c60 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b5c60 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005b5c60 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005b5c60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b5c60 bytes 082400a9
- 005b5c6c ["COPY", "register:0:8", ["register:40f0:8"]]
- 005b5c6c ["RETURN", null, ["register:0:8"]]
- 005b5c6c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13b0a49c55bc077da307a9d6ef989cb7"></a>

### [`005b5c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c70.md) → [`005b6020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6020.md) FUN_005b6020

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
      "definition_site": "005b602c",
      "incomplete_value": false,
      "site": "005b602c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5c7c",
      "incomplete_value": false,
      "site": "005b5c7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "005b602c",
      "DATA",
      [
        "storage",
        "00c6fc90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b602c",
      "DATA",
      [
        "storage",
        "00c70c60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c70.md#insn-005b5c74) · [`005b5c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c70.md#insn-005b5c78)
- 新版 [`005b6024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6020.md#insn-005b6024) · [`005b6028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6020.md#insn-005b6028)

~~~diff
- 005b5c74 ["COPY", "register:4048:8", ["const:c6f000:8"]]
+ 005b6024 ["COPY", "register:4048:8", ["const:c70000:8"]]
- 005b5c74 bytes c93500d0
+ 005b6024 bytes c93500d0
- 005b5c78 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 005b5c78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5c78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5c78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6028 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 005b6028 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6028 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6028 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5c78 bytes 29413291
+ 005b6028 bytes 29813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfdc94b594fa0ddaf04138c2743fc847"></a>

### [`005b5cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5cd0.md) → [`005b6080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6080.md) FUN_005b6080

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
      "definition_site": "005b60a4",
      "incomplete_value": false,
      "site": "005b60a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5cf4",
      "incomplete_value": false,
      "site": "005b5cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "005b60a4",
      "DATA",
      [
        "storage",
        "00c6fd10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b60a4",
      "DATA",
      [
        "storage",
        "00c70ce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5cd0.md#insn-005b5ce4) · [`005b5cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5cd0.md#insn-005b5cec) · [`005b5cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5cd0.md#insn-005b5cf0)
- 新版 [`005b6094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6080.md#insn-005b6094) · [`005b609c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6080.md#insn-005b609c) · [`005b60a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6080.md#insn-005b60a0)

~~~diff
- 005b5ce4 ["INT_ADD", "register:40f0:8", ["const:5b5ce4:8", "const:4:8"]]
- 005b5ce4 ["CALL", null, ["callee:00c58f30:8"]]
+ 005b6094 ["INT_ADD", "register:40f0:8", ["const:5b6094:8", "const:4:8"]]
+ 005b6094 ["CALL", null, ["callee:00c58f30:8"]]
- 005b5ce4 bytes 9f881a94
+ 005b6094 bytes a78b1a94
- 005b5cec ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b609c ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b5cec bytes c83500d0
+ 005b609c bytes c83500d0
- 005b5cf0 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 005b5cf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5cf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5cf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b60a0 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 005b60a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b60a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b60a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5cf0 bytes 08413491
+ 005b60a0 bytes 08813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-841b17bdd28961d0580b04d5277a3342"></a>

### [`005b5d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5d04.md) → [`005b60b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b60b4.md) FUN_005b60b4

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
      "definition_site": "005b60c0",
      "incomplete_value": false,
      "site": "005b60c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5d10",
      "incomplete_value": false,
      "site": "005b5d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "005b60c0",
      "DATA",
      [
        "storage",
        "00c6fd10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b60c0",
      "DATA",
      [
        "storage",
        "00c70ce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5d04.md#insn-005b5d08) · [`005b5d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5d04.md#insn-005b5d0c)
- 新版 [`005b60b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b60b4.md#insn-005b60b8) · [`005b60bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b60b4.md#insn-005b60bc)

~~~diff
- 005b5d08 ["COPY", "register:4048:8", ["const:c6f000:8"]]
+ 005b60b8 ["COPY", "register:4048:8", ["const:c70000:8"]]
- 005b5d08 bytes c93500d0
+ 005b60b8 bytes c93500d0
- 005b5d0c ["COPY", "tmp:0:8", ["const:d10:8"]]
- 005b5d0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5d0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5d0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b60bc ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 005b60bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b60bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b60bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5d0c bytes 29413491
+ 005b60bc bytes 29813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac90dd99f1903ef1be4092e637e22f21"></a>

### [`005b5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5df8.md) → [`005b61a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b61a8.md) FUN_005b61a8

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
      "definition_site": "005b61cc",
      "incomplete_value": false,
      "site": "005b61cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5e1c",
      "incomplete_value": false,
      "site": "005b5e1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "005b61cc",
      "DATA",
      [
        "storage",
        "00c6fd90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b61cc",
      "DATA",
      [
        "storage",
        "00c70d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5df8.md#insn-005b5e0c) · [`005b5e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5df8.md#insn-005b5e14) · [`005b5e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5df8.md#insn-005b5e18)
- 新版 [`005b61bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b61a8.md#insn-005b61bc) · [`005b61c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b61a8.md#insn-005b61c4) · [`005b61c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b61a8.md#insn-005b61c8)

~~~diff
- 005b5e0c ["INT_ADD", "register:40f0:8", ["const:5b5e0c:8", "const:4:8"]]
- 005b5e0c ["CALL", null, ["callee:00c58f30:8"]]
+ 005b61bc ["INT_ADD", "register:40f0:8", ["const:5b61bc:8", "const:4:8"]]
+ 005b61bc ["CALL", null, ["callee:00c58f30:8"]]
- 005b5e0c bytes 55881a94
+ 005b61bc bytes 5d8b1a94
- 005b5e14 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b61c4 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b5e14 bytes c83500d0
+ 005b61c4 bytes c83500d0
- 005b5e18 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 005b5e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b61c8 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 005b61c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b61c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b61c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5e18 bytes 08413691
+ 005b61c8 bytes 08813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-569ea1f2d0878b5fa4dad62aee9a75f6"></a>

### [`005b5e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5e2c.md) → [`005b61dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b61dc.md) FUN_005b61dc

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
      "definition_site": "005b61e8",
      "incomplete_value": false,
      "site": "005b61e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5e38",
      "incomplete_value": false,
      "site": "005b5e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "005b61e8",
      "DATA",
      [
        "storage",
        "00c6fd90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b61e8",
      "DATA",
      [
        "storage",
        "00c70d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5e2c.md#insn-005b5e30) · [`005b5e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5e2c.md#insn-005b5e34)
- 新版 [`005b61e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b61dc.md#insn-005b61e0) · [`005b61e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b61dc.md#insn-005b61e4)

~~~diff
- 005b5e30 ["COPY", "register:4048:8", ["const:c6f000:8"]]
+ 005b61e0 ["COPY", "register:4048:8", ["const:c70000:8"]]
- 005b5e30 bytes c93500d0
+ 005b61e0 bytes c93500d0
- 005b5e34 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 005b5e34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5e34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5e34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b61e4 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 005b61e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b61e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b61e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5e34 bytes 29413691
+ 005b61e4 bytes 29813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc60395f0bdb169a21b61e5e081cee2d"></a>

### [`005b5ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ee8.md) → [`005b6298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6298.md) FUN_005b6298

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005b3180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3180.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`005b3530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b3/005b3530.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b5f2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b62dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b5f6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b5f2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b5f4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005b3180"
      ]
    ],
    [
      "unmatched:005b5f6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b6360"
      ]
    ]
  ],
  "added": [
    [
      "005b62dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005b62fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005b3530"
      ]
    ],
    [
      "005b631c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b6360"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ee8.md#insn-005b5f2c) · [`005b5f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ee8.md#insn-005b5f3c) · [`005b5f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ee8.md#insn-005b5f4c)
- 新版 [`005b62ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6298.md#insn-005b62ec)

~~~diff
- 005b5f2c ["COPY", "tmp:0:8", ["register:8:8"]]
- 005b5f2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 005b5f2c bytes e003803d
- 005b5f3c ["INT_ADD", "register:40f0:8", ["const:5b5f3c:8", "const:4:8"]]
- 005b5f3c ["CALL", null, ["callee:0043be80:8"]]
+ 005b62ec ["INT_ADD", "register:40f0:8", ["const:5b62ec:8", "const:4:8"]]
+ 005b62ec ["CALL", null, ["callee:0043be80:8"]]
- 005b5f3c bytes 0917fa97
+ 005b62ec bytes e516fa97
- 005b5f4c ["INT_ADD", "register:40f0:8", ["const:5b5f4c:8", "const:4:8"]]
- 005b5f4c ["CALL", null, ["ram:5b3180:8"]]
- 005b5f4c bytes 8df4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fb2ce12e73af2a12d8e705538427a16"></a>

### [`005b614c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b614c.md) → [`005b64fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b64fc.md) FUN_005b64fc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b651c",
      "incomplete_value": false,
      "site": "005b6520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b616c",
      "incomplete_value": false,
      "site": "005b6170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "005b6520",
      "DATA",
      [
        "storage",
        "00c6ff30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6520",
      "DATA",
      [
        "storage",
        "00c70f00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b614c.md#insn-005b6154) · [`005b6160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b614c.md#insn-005b6160) · [`005b6168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b614c.md#insn-005b6168)
- 新版 [`005b6510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b64fc.md#insn-005b6510) · [`005b6518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b64fc.md#insn-005b6518)

~~~diff
- 005b6154 ["COPY", "register:40e8:8", ["register:8:8"]]
- 005b6154 bytes fd030091
- 005b6160 ["INT_ADD", "register:40f0:8", ["const:5b6160:8", "const:4:8"]]
- 005b6160 ["CALL", null, ["callee:00c58f30:8"]]
+ 005b6510 ["INT_ADD", "register:40f0:8", ["const:5b6510:8", "const:4:8"]]
+ 005b6510 ["CALL", null, ["callee:00c58f30:8"]]
- 005b6160 bytes 80871a94
+ 005b6510 bytes 888a1a94
- 005b6168 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b6518 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b6168 bytes c83500b0
+ 005b6518 bytes c83500d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91823c3f20c65d6f702f80259a878303"></a>

### [`005b6184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6184.md) → [`005b6534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6534.md) FUN_005b6534

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
      "definition_site": "005b6538",
      "incomplete_value": false,
      "site": "005b653c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6188",
      "incomplete_value": false,
      "site": "005b618c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "005b653c",
      "DATA",
      [
        "storage",
        "00c6ff30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b653c",
      "DATA",
      [
        "storage",
        "00c70f00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6184.md#insn-005b6184) · [`005b6188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6184.md#insn-005b6188)
- 新版 [`005b6534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6534.md#insn-005b6534) · [`005b6538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6534.md#insn-005b6538)

~~~diff
- 005b6184 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b6534 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b6184 bytes c83500b0
+ 005b6534 bytes c83500d0
- 005b6188 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 005b6188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6538 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 005b6538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6188 bytes 08c13c91
+ 005b6538 bytes 08013c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32f2ff7ef25f11d46e282ae169d12a33"></a>

### [`005b6218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6218.md) → [`005b65c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b65c8.md) FUN_005b65c8

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
      "definition_site": "005b65d4",
      "incomplete_value": false,
      "site": "005b65d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6224",
      "incomplete_value": false,
      "site": "005b6224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      "005b65d4",
      "DATA",
      [
        "storage",
        "00c6ffb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b65d4",
      "DATA",
      [
        "storage",
        "00c70f80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b621c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6218.md#insn-005b621c) · [`005b6220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6218.md#insn-005b6220)
- 新版 [`005b65cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b65c8.md#insn-005b65cc) · [`005b65d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b65c8.md#insn-005b65d0)

~~~diff
- 005b621c ["COPY", "register:4048:8", ["const:c6f000:8"]]
+ 005b65cc ["COPY", "register:4048:8", ["const:c70000:8"]]
- 005b621c bytes c93500b0
+ 005b65cc bytes c93500d0
- 005b6220 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 005b6220 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6220 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6220 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b65d0 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 005b65d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b65d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b65d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6220 bytes 29c13e91
+ 005b65d0 bytes 29013e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68e4c273db6eeb3305796c26032caa20"></a>

### [`005b6234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6234.md) → [`005b65e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b65e4.md) FUN_005b65e4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`005b216c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b216c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005b251c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b2/005b251c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b6604",
      "DATA",
      [
        "storage",
        "002d7368",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005b6604",
      "DATA",
      [
        "storage",
        "002d73a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6234.md#insn-005b6248) · [`005b6250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6234.md#insn-005b6250) · [`005b6258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6234.md#insn-005b6258)
- 新版 [`005b65f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b65e4.md#insn-005b65f8) · [`005b6600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b65e4.md#insn-005b6600) · [`005b6608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b65e4.md#insn-005b6608)

~~~diff
- 005b6248 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005b6248 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 005b6248 ["CBRANCH", null, ["local:b2:8", "tmp:1:1"]]
+ 005b65f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 005b65f8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 005b65f8 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 005b6248 bytes a8000054
+ 005b65f8 bytes a8000054
- 005b6250 ["COPY", "tmp:0:8", ["const:368:8"]]
- 005b6250 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6250 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6250 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6600 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 005b6600 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6600 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6600 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6250 bytes 29a10d91
+ 005b6600 bytes 29a10e91
- 005b6258 ["BRANCH", null, ["local:b3:8"]]
+ 005b6608 ["BRANCH", null, ["local:b4:8"]]
- 005b6258 bytes 02000014
+ 005b6608 bytes 02000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08bd0a72d17913167c46e2eaabcfa50b"></a>

### [`005b62cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b62cc.md) → [`005b667c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b667c.md) FUN_005b667c

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
      "definition_site": "005b6688",
      "incomplete_value": false,
      "site": "005b6688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b62d8",
      "incomplete_value": false,
      "site": "005b62d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:30:8"
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
      "005b6688",
      "DATA",
      [
        "storage",
        "00c70030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6688",
      "DATA",
      [
        "storage",
        "00c71000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b62d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b62cc.md#insn-005b62d0) · [`005b62d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b62cc.md#insn-005b62d4)
- 新版 [`005b6680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b667c.md#insn-005b6680) · [`005b6684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b667c.md#insn-005b6684)

~~~diff
- 005b62d0 ["COPY", "register:4048:8", ["const:c70000:8"]]
+ 005b6680 ["COPY", "register:4048:8", ["const:c71000:8"]]
- 005b62d0 bytes c93500d0
+ 005b6680 bytes c93500f0
- 005b62d4 ["COPY", "tmp:0:8", ["const:30:8"]]
- 005b62d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b62d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b62d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6684 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 005b6684 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6684 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6684 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b62d4 bytes 29c10091
+ 005b6684 bytes 29010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58b19818681c8d2b02e70d7e61248cb7"></a>

### [`005b63c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63c0.md) → [`005b6770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6770.md) FUN_005b6770

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
      "definition_site": "005b6794",
      "incomplete_value": false,
      "site": "005b6794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b63e4",
      "incomplete_value": false,
      "site": "005b63e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "005b6794",
      "DATA",
      [
        "storage",
        "00c700b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6794",
      "DATA",
      [
        "storage",
        "00c71080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b63d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63c0.md#insn-005b63d4) · [`005b63dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63c0.md#insn-005b63dc) · [`005b63e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63c0.md#insn-005b63e0)
- 新版 [`005b6784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6770.md#insn-005b6784) · [`005b678c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6770.md#insn-005b678c) · [`005b6790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6770.md#insn-005b6790)

~~~diff
- 005b63d4 ["INT_ADD", "register:40f0:8", ["const:5b63d4:8", "const:4:8"]]
- 005b63d4 ["CALL", null, ["callee:00c58f30:8"]]
+ 005b6784 ["INT_ADD", "register:40f0:8", ["const:5b6784:8", "const:4:8"]]
+ 005b6784 ["CALL", null, ["callee:00c58f30:8"]]
- 005b63d4 bytes e3861a94
+ 005b6784 bytes eb891a94
- 005b63dc ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b678c ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b63dc bytes c83500d0
+ 005b678c bytes c83500f0
- 005b63e0 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 005b63e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b63e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b63e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6790 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 005b6790 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6790 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6790 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b63e0 bytes 08c10291
+ 005b6790 bytes 08010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fffb36cceec960780f8525a8cdab62c"></a>

### [`005b63f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63f4.md) → [`005b67a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b67a4.md) FUN_005b67a4

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
      "definition_site": "005b67b0",
      "incomplete_value": false,
      "site": "005b67b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6400",
      "incomplete_value": false,
      "site": "005b6400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "005b67b0",
      "DATA",
      [
        "storage",
        "00c700b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b67b0",
      "DATA",
      [
        "storage",
        "00c71080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b63f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63f4.md#insn-005b63f8) · [`005b63fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63f4.md#insn-005b63fc)
- 新版 [`005b67a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b67a4.md#insn-005b67a8) · [`005b67ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b67a4.md#insn-005b67ac)

~~~diff
- 005b63f8 ["COPY", "register:4048:8", ["const:c70000:8"]]
+ 005b67a8 ["COPY", "register:4048:8", ["const:c71000:8"]]
- 005b63f8 bytes c93500d0
+ 005b67a8 bytes c93500f0
- 005b63fc ["COPY", "tmp:0:8", ["const:b0:8"]]
- 005b63fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b63fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b63fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b67ac ["COPY", "tmp:0:8", ["const:80:8"]]
+ 005b67ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b67ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b67ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b63fc bytes 29c10291
+ 005b67ac bytes 29010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d78174ff5aa063905544f08ded07b421"></a>

### [`005b6458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6458.md) → [`005b6808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6808.md) FUN_005b6808

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
      "definition_site": "005b682c",
      "incomplete_value": false,
      "site": "005b682c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b647c",
      "incomplete_value": false,
      "site": "005b647c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:130:8"
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
      "005b682c",
      "DATA",
      [
        "storage",
        "00c70130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b682c",
      "DATA",
      [
        "storage",
        "00c71100",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b646c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6458.md#insn-005b646c) · [`005b6474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6458.md#insn-005b6474) · [`005b6478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6458.md#insn-005b6478)
- 新版 [`005b681c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6808.md#insn-005b681c) · [`005b6824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6808.md#insn-005b6824) · [`005b6828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6808.md#insn-005b6828)

~~~diff
- 005b646c ["INT_ADD", "register:40f0:8", ["const:5b646c:8", "const:4:8"]]
- 005b646c ["CALL", null, ["callee:00c58f30:8"]]
+ 005b681c ["INT_ADD", "register:40f0:8", ["const:5b681c:8", "const:4:8"]]
+ 005b681c ["CALL", null, ["callee:00c58f30:8"]]
- 005b646c bytes bd861a94
+ 005b681c bytes c5891a94
- 005b6474 ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b6824 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b6474 bytes c83500d0
+ 005b6824 bytes c83500f0
- 005b6478 ["COPY", "tmp:0:8", ["const:130:8"]]
- 005b6478 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6478 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6478 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6828 ["COPY", "tmp:0:8", ["const:100:8"]]
+ 005b6828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6478 bytes 08c10491
+ 005b6828 bytes 08010491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-153119773c1149079a4929439be14cde"></a>

### [`005b648c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b648c.md) → [`005b683c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b683c.md) FUN_005b683c

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
      "definition_site": "005b6848",
      "incomplete_value": false,
      "site": "005b6848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6498",
      "incomplete_value": false,
      "site": "005b6498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:130:8"
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
      "005b6848",
      "DATA",
      [
        "storage",
        "00c70130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6848",
      "DATA",
      [
        "storage",
        "00c71100",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b648c.md#insn-005b6490) · [`005b6494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b648c.md#insn-005b6494)
- 新版 [`005b6840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b683c.md#insn-005b6840) · [`005b6844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b683c.md#insn-005b6844)

~~~diff
- 005b6490 ["COPY", "register:4048:8", ["const:c70000:8"]]
+ 005b6840 ["COPY", "register:4048:8", ["const:c71000:8"]]
- 005b6490 bytes c93500d0
+ 005b6840 bytes c93500f0
- 005b6494 ["COPY", "tmp:0:8", ["const:130:8"]]
- 005b6494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6844 ["COPY", "tmp:0:8", ["const:100:8"]]
+ 005b6844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6494 bytes 29c10491
+ 005b6844 bytes 29010491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d82ac0ee374d901ba9cb608fec519fa5"></a>

### [`005b64a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b64a8.md) → [`005b6858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6858.md) FUN_005b6858

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0053f058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f058.md) [`005b66cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b66cc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0053f378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f378.md) [`005b6a7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6a7c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 61.90% / 新版 56.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b68d4",
      "incomplete_value": false,
      "site": "005b68ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6524",
      "incomplete_value": false,
      "site": "005b653c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "site": "005b65bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005b696c"
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
      "005b68ec",
      "DATA",
      [
        "storage",
        "00c701b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005b65a0",
      "READ",
      [
        "storage",
        "00c701c0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b65a4",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "005b6a7c"
      ]
    ]
  ],
  "added": [
    [
      "005b68ec",
      "DATA",
      [
        "storage",
        "00c71180",
        null,
        "pointer"
      ]
    ],
    [
      "005b6950",
      "READ",
      [
        "storage",
        "00c71190",
        null,
        "undefined *"
      ]
    ],
    [
      "005b6954",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "005b6a7c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b65a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b64a8.md#insn-005b65a4) · [`005b65bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b64a8.md#insn-005b65bc)
- 新版 [`005b6954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6858.md#insn-005b6954)

~~~diff
- 005b65a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b65a4 ["INT_ADD", "register:40f0:8", ["const:5b65a4:8", "const:4:8"]]
- 005b65a4 ["CALLIND", null, ["register:0:8"]]
- 005b65a4 bytes 00013fd6
- 005b65bc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005b65bc ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 005b65bc bytes a1020054
+ 005b6954 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b6954 ["INT_ADD", "register:40f0:8", ["const:5b6954:8", "const:4:8"]]
+ 005b6954 ["CALLIND", null, ["register:0:8"]]
+ 005b6954 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c74079087b3d13b581db284813c4609"></a>

### [`005b668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b668c.md) → [`005b6a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6a3c.md) FUN_005b6a3c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6a40",
      "incomplete_value": false,
      "site": "005b6a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6690",
      "incomplete_value": false,
      "site": "005b6694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "005b6a44",
      "DATA",
      [
        "storage",
        "00c701b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b6a44",
      "DATA",
      [
        "storage",
        "00c71180",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b668c.md#insn-005b668c) · [`005b6690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b668c.md#insn-005b6690)
- 新版 [`005b6a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6a3c.md#insn-005b6a3c) · [`005b6a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6a3c.md#insn-005b6a40)

~~~diff
- 005b668c ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b6a3c ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b668c bytes c83500d0
+ 005b6a3c bytes c83500f0
- 005b6690 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 005b6690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6a40 ["COPY", "tmp:0:8", ["const:180:8"]]
+ 005b6a40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6a40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6a40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6690 bytes 08c10691
+ 005b6a40 bytes 08010691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d279dbecb388c9b7590988007b0a68f8"></a>

### [`005b6784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6784.md) → [`005b6b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6b34.md) FUN_005b6b34

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
      "definition_site": "005b6b40",
      "incomplete_value": false,
      "site": "005b6b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6790",
      "incomplete_value": false,
      "site": "005b6790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:210:8"
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
      "005b6b40",
      "DATA",
      [
        "storage",
        "00c70210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6b40",
      "DATA",
      [
        "storage",
        "00c711e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6784.md#insn-005b6788) · [`005b678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6784.md#insn-005b678c)
- 新版 [`005b6b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6b34.md#insn-005b6b38) · [`005b6b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6b34.md#insn-005b6b3c)

~~~diff
- 005b6788 ["COPY", "register:4048:8", ["const:c70000:8"]]
+ 005b6b38 ["COPY", "register:4048:8", ["const:c71000:8"]]
- 005b6788 bytes c93500d0
+ 005b6b38 bytes c93500f0
- 005b678c ["COPY", "tmp:0:8", ["const:210:8"]]
- 005b678c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b678c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b678c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6b3c ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 005b6b3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6b3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6b3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b678c bytes 29410891
+ 005b6b3c bytes 29810791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-164c28b8bab8af4b49e3d248b1476d3c"></a>

### [`005b68a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b68a4.md) → [`005b6c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6c54.md) FUN_005b6c54

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
      "definition_site": "005b6c60",
      "incomplete_value": false,
      "site": "005b6c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b68b0",
      "incomplete_value": false,
      "site": "005b68b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "005b6c60",
      "DATA",
      [
        "storage",
        "00c70320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6c60",
      "DATA",
      [
        "storage",
        "00c712f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b68a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b68a4.md#insn-005b68a8) · [`005b68ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b68a4.md#insn-005b68ac)
- 新版 [`005b6c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6c54.md#insn-005b6c58) · [`005b6c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6c54.md#insn-005b6c5c)

~~~diff
- 005b68a8 ["COPY", "register:4048:8", ["const:c70000:8"]]
+ 005b6c58 ["COPY", "register:4048:8", ["const:c71000:8"]]
- 005b68a8 bytes c93500d0
+ 005b6c58 bytes c93500f0
- 005b68ac ["COPY", "tmp:0:8", ["const:320:8"]]
- 005b68ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b68ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b68ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6c5c ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 005b6c5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6c5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6c5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b68ac bytes 29810c91
+ 005b6c5c bytes 29c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-956af22bbcf8b143d00e2a8f7c662043"></a>

### [`005b6908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6908.md) → [`005b6cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6cb8.md) FUN_005b6cb8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b692c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b692c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b6cdc"
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
      "unmatched:005b692c",
      "DATA",
      [
        "storage",
        "00c703a0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b6930",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b6934",
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
      "005b6cdc",
      "DATA",
      [
        "storage",
        "00c71370",
        null,
        "undefined *"
      ]
    ],
    [
      "005b6ce0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b6ce4",
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

- 旧版 [`005b691c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6908.md#insn-005b691c) · [`005b692c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6908.md#insn-005b692c) · [`005b6938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6908.md#insn-005b6938)
- 新版 [`005b6ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6cb8.md#insn-005b6ccc)

~~~diff
- 005b691c ["INT_ADD", "register:40f0:8", ["const:5b691c:8", "const:4:8"]]
- 005b691c ["CALL", null, ["callee:00c58f30:8"]]
+ 005b6ccc ["INT_ADD", "register:40f0:8", ["const:5b6ccc:8", "const:4:8"]]
+ 005b6ccc ["CALL", null, ["callee:00c58f30:8"]]
- 005b691c bytes 91851a94
+ 005b6ccc bytes 99881a94
- 005b692c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b692c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005b692c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005b692c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b692c bytes 082400a9
- 005b6938 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005b6938 ["RETURN", null, ["register:0:8"]]
- 005b6938 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddb0b0f6002f134061d180d557bf2a1b"></a>

### [`005b693c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b693c.md) → [`005b6cec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6cec.md) FUN_005b6cec

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
      "definition_site": "005b6cf8",
      "incomplete_value": false,
      "site": "005b6cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6948",
      "incomplete_value": false,
      "site": "005b6948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "005b6cf8",
      "DATA",
      [
        "storage",
        "00c703a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6cf8",
      "DATA",
      [
        "storage",
        "00c71370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b693c.md#insn-005b6940) · [`005b6944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b693c.md#insn-005b6944)
- 新版 [`005b6cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6cec.md#insn-005b6cf0) · [`005b6cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6cec.md#insn-005b6cf4)

~~~diff
- 005b6940 ["COPY", "register:4048:8", ["const:c70000:8"]]
+ 005b6cf0 ["COPY", "register:4048:8", ["const:c71000:8"]]
- 005b6940 bytes c93500d0
+ 005b6cf0 bytes c93500f0
- 005b6944 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 005b6944 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6944 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6944 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6cf4 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 005b6cf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6cf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6cf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6944 bytes 29810e91
+ 005b6cf4 bytes 29c10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3ef590f701a2fbfe95578e32d0985b8"></a>

### [`005b6958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6958.md) → [`005b6d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6d08.md) FUN_005b6d08

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`005b0c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0c1c.md) [`005b5254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5254.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`005b0fcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b0/005b0fcc.md) [`005b5604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b5/005b5604.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.88% / 新版 69.88%

CFGの説明率　旧版 45.00% / 新版 45.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b695c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b695c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b6960"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b695c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b6960",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b6964",
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
      "005b6d0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005b6d10",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005b6d14",
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

- 旧版 [`005b695c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6958.md#insn-005b695c) · [`005b6960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6958.md#insn-005b6960) · [`005b6964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6958.md#insn-005b6964)

~~~diff
- 005b695c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005b695c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005b695c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 005b695c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b695c bytes fd7b04a9
- 005b6960 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005b6960 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005b6960 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 005b6960 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b6960 bytes f85f05a9
- 005b6964 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005b6964 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005b6964 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 005b6964 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b6964 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef7c5e16092dadd75e58b6a19587ea41"></a>

### [`005b6b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b5c.md) → [`005b6f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6f0c.md) FUN_005b6f0c

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
      "definition_site": "005b6f18",
      "incomplete_value": false,
      "site": "005b6f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6b68",
      "incomplete_value": false,
      "site": "005b6b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:430:8"
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
      "005b6f18",
      "DATA",
      [
        "storage",
        "00c70430",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6f18",
      "DATA",
      [
        "storage",
        "00c71400",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b5c.md#insn-005b6b60) · [`005b6b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b5c.md#insn-005b6b64)
- 新版 [`005b6f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6f0c.md#insn-005b6f10) · [`005b6f14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6f0c.md#insn-005b6f14)

~~~diff
- 005b6b60 ["COPY", "register:4048:8", ["const:c70000:8"]]
+ 005b6f10 ["COPY", "register:4048:8", ["const:c71000:8"]]
- 005b6b60 bytes c93500d0
+ 005b6f10 bytes c93500f0
- 005b6b64 ["COPY", "tmp:0:8", ["const:430:8"]]
- 005b6b64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6b64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6b64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6f14 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 005b6f14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6f14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6f14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6b64 bytes 29c11091
+ 005b6f14 bytes 29011091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63e3d1e0506e9ac844530b8f489c61fe"></a>

### [`005b6b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b78.md) → [`005b6f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6f28.md) FUN_005b6f28

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`005b6e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6e2c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`005b71dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b71dc.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 30.56% / 新版 28.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b6b9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b6c04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b6c1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b6b9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b6bcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b70bc"
      ]
    ],
    [
      "unmatched:005b6c04",
      "DATA",
      [
        "storage",
        "00c704b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b6f4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "005b6f7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b70bc"
      ]
    ],
    [
      "005b6fb4",
      "DATA",
      [
        "storage",
        "00c71480",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b78.md#insn-005b6b9c) · [`005b6bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b78.md#insn-005b6bcc) · [`005b6bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b78.md#insn-005b6bec)
- 新版 [`005b6f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6f28.md#insn-005b6f9c)

~~~diff
- 005b6b9c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b6b9c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005b6b9c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b6b9c bytes a8831ff8
- 005b6bcc ["CBRANCH", null, ["local:b20:8", "register:101:1"]]
- 005b6bcc bytes 000a0054
- 005b6bec ["INT_ADD", "register:40f0:8", ["const:5b6bec:8", "const:4:8"]]
- 005b6bec ["CALL", null, ["callee:00c58f30:8"]]
+ 005b6f9c ["INT_ADD", "register:40f0:8", ["const:5b6f9c:8", "const:4:8"]]
+ 005b6f9c ["CALL", null, ["callee:00c58f30:8"]]
- 005b6bec bytes dd841a94
+ 005b6f9c bytes e5871a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6986e72731c0ae6d50ff4bcca645886c"></a>

### [`005b6d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6d9c.md) → [`005b714c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b714c.md) FUN_005b714c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 75.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b6db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6d9c.md#insn-005b6db8) · [`005b6dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6d9c.md#insn-005b6dd8)
- 新版 [`005b7168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b714c.md#insn-005b7168) · [`005b7188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b714c.md#insn-005b7188)

~~~diff
- 005b6db8 ["INT_ADD", "register:40f0:8", ["const:5b6db8:8", "const:4:8"]]
- 005b6db8 ["CALL", null, ["callee:00c54d90:8"]]
+ 005b7168 ["INT_ADD", "register:40f0:8", ["const:5b7168:8", "const:4:8"]]
+ 005b7168 ["CALL", null, ["callee:00c54d90:8"]]
- 005b6db8 bytes fa731a94
+ 005b7168 bytes 0a771a94
- 005b6dd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b6dd8 ["INT_ADD", "register:40f0:8", ["const:5b6dd8:8", "const:4:8"]]
- 005b6dd8 ["CALLIND", null, ["register:0:8"]]
+ 005b7188 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7188 ["INT_ADD", "register:40f0:8", ["const:5b7188:8", "const:4:8"]]
+ 005b7188 ["CALLIND", null, ["register:0:8"]]
- 005b6dd8 bytes 00013fd6
+ 005b7188 bytes 00013fd6
~~~


<a id="compare-7ac72df805df4836e6057baf54879ea3"></a>

### [`005b6dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6dec.md) → [`005b719c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b719c.md) FUN_005b719c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b71a0",
      "incomplete_value": false,
      "site": "005b71a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6df0",
      "incomplete_value": false,
      "site": "005b6df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "005b71a4",
      "DATA",
      [
        "storage",
        "00c704b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b71a4",
      "DATA",
      [
        "storage",
        "00c71480",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6dec.md#insn-005b6dec) · [`005b6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6dec.md#insn-005b6df0)
- 新版 [`005b719c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b719c.md#insn-005b719c) · [`005b71a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b719c.md#insn-005b71a0)

~~~diff
- 005b6dec ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b719c ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b6dec bytes c83500d0
+ 005b719c bytes c83500d0
- 005b6df0 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 005b6df0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6df0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6df0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b71a0 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 005b71a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b71a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b71a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6df0 bytes 08c11291
+ 005b71a0 bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1b1c887ee002032092b7e8ccd950077"></a>

### [`005b6dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6dfc.md) → [`005b71ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b71ac.md) FUN_005b71ac

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b71bc",
      "incomplete_value": false,
      "site": "005b71c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6e0c",
      "incomplete_value": false,
      "site": "005b6e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "005b71c4",
      "DATA",
      [
        "storage",
        "00c704b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b71c4",
      "DATA",
      [
        "storage",
        "00c71480",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6dfc.md#insn-005b6e08) · [`005b6e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6dfc.md#insn-005b6e0c) · [`005b6e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6dfc.md#insn-005b6e18)
- 新版 [`005b71b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b71ac.md#insn-005b71b8) · [`005b71bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b71ac.md#insn-005b71bc) · [`005b71c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b71ac.md#insn-005b71c8)

~~~diff
- 005b6e08 ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b71b8 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b6e08 bytes c83500d0
+ 005b71b8 bytes c83500d0
- 005b6e0c ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 005b6e0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6e0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6e0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b71bc ["COPY", "tmp:0:8", ["const:480:8"]]
+ 005b71bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b71bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b71bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6e0c bytes 08c11291
+ 005b71bc bytes 08011291
- 005b6e18 ["INT_ADD", "register:40f0:8", ["const:5b6e18:8", "const:4:8"]]
- 005b6e18 ["CALL", null, ["callee:00c58f40:8"]]
+ 005b71c8 ["INT_ADD", "register:40f0:8", ["const:5b71c8:8", "const:4:8"]]
+ 005b71c8 ["CALL", null, ["callee:00c58f40:8"]]
- 005b6e18 bytes 56841a94
+ 005b71c8 bytes 5e871a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bde73d0a010e9d4edd1829d28ac48933"></a>

### [`005b6e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6e2c.md) → [`005b71dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b71dc.md) FUN_005b71dc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`005b6b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b78.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`005b6f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b6/005b6f28.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 42.86% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005b7218",
      "incomplete_value": true,
      "site": "005b721c",
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
                "const:38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005b6e78",
      "incomplete_value": true,
      "site": "005b6e80",
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
    "ordinal": 2,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`005b6e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6e2c.md#insn-005b6e6c) · [`005b6e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6e2c.md#insn-005b6e80) · [`005b6e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6e2c.md#insn-005b6e50)
- 新版 [`005b721c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b71dc.md#insn-005b721c) · [`005b7230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b71dc.md#insn-005b7230) · [`005b7200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b71dc.md#insn-005b7200)

~~~diff
- 005b6e6c ["INT_ADD", "register:40f0:8", ["const:5b6e6c:8", "const:4:8"]]
- 005b6e6c ["CALL", null, ["callee:00c58f50:8"]]
+ 005b721c ["INT_ADD", "register:40f0:8", ["const:5b721c:8", "const:4:8"]]
+ 005b721c ["CALL", null, ["callee:00c58f50:8"]]
- 005b6e6c bytes 45841a94
+ 005b721c bytes 4d871a94
- 005b6e80 ["INT_ADD", "register:40f0:8", ["const:5b6e80:8", "const:4:8"]]
- 005b6e80 ["CALL", null, ["callee:00c54d90:8"]]
+ 005b7230 ["INT_ADD", "register:40f0:8", ["const:5b7230:8", "const:4:8"]]
+ 005b7230 ["CALL", null, ["callee:00c54d90:8"]]
- 005b6e80 bytes c8731a94
+ 005b7230 bytes d8761a94
- 005b6e50 ["INT_NOTEQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 005b6e50 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 005b7200 ["INT_NOTEQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 005b7200 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 005b6e50 bytes 530100b5
+ 005b7200 bytes 530100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d17d3b074ab14773a17e35242cc549c1"></a>

### [`005b6ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6ef0.md) → [`005b72a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b72a0.md) FUN_005b72a0

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
      "definition_site": "005b72ac",
      "incomplete_value": false,
      "site": "005b72ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6efc",
      "incomplete_value": false,
      "site": "005b6efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:510:8"
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
      "005b72ac",
      "DATA",
      [
        "storage",
        "00c70510",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b72ac",
      "DATA",
      [
        "storage",
        "00c714e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6ef0.md#insn-005b6ef4) · [`005b6ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6ef0.md#insn-005b6ef8)
- 新版 [`005b72a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b72a0.md#insn-005b72a4) · [`005b72a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b72a0.md#insn-005b72a8)

~~~diff
- 005b6ef4 ["COPY", "register:4048:8", ["const:c70000:8"]]
+ 005b72a4 ["COPY", "register:4048:8", ["const:c71000:8"]]
- 005b6ef4 bytes c93500d0
+ 005b72a4 bytes c93500d0
- 005b6ef8 ["COPY", "tmp:0:8", ["const:510:8"]]
- 005b6ef8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6ef8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6ef8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b72a8 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 005b72a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b72a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b72a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6ef8 bytes 29411491
+ 005b72a8 bytes 29811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7002f3472d82da8beafb4bf8c88dfb8"></a>

### [`005b7008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7008.md) → [`005b73b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b73b8.md) FUN_005b73b8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b702c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b702c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b73dc"
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
      "unmatched:005b702c",
      "DATA",
      [
        "storage",
        "00c70590",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b7030",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b7034",
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
      "005b73dc",
      "DATA",
      [
        "storage",
        "00c71560",
        null,
        "undefined *"
      ]
    ],
    [
      "005b73e0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b73e4",
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

- 旧版 [`005b701c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7008.md#insn-005b701c) · [`005b702c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7008.md#insn-005b702c) · [`005b7038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7008.md#insn-005b7038)
- 新版 [`005b73cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b73b8.md#insn-005b73cc)

~~~diff
- 005b701c ["INT_ADD", "register:40f0:8", ["const:5b701c:8", "const:4:8"]]
- 005b701c ["CALL", null, ["callee:00c58f30:8"]]
+ 005b73cc ["INT_ADD", "register:40f0:8", ["const:5b73cc:8", "const:4:8"]]
+ 005b73cc ["CALL", null, ["callee:00c58f30:8"]]
- 005b701c bytes d1831a94
+ 005b73cc bytes d9861a94
- 005b702c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b702c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005b702c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005b702c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b702c bytes 082400a9
- 005b7038 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005b7038 ["RETURN", null, ["register:0:8"]]
- 005b7038 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a7381321f83cb82d2420d8f131300d9"></a>

### [`005b71c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b71c4.md) → [`005b7574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7574.md) FUN_005b7574

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b3bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3bb4.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`005b3f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b3/005b3f64.md) · 呼出先 7件 [`00598230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md) [`005b772c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b772c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 8.11% / 新版 8.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b71f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7204"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b721c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b71f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b71f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f30"
      ]
    ],
    [
      "unmatched:005b7204",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b75a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "005b75a4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f30"
      ]
    ],
    [
      "005b75b4",
      "DATA",
      [
        "storage",
        "00c71660",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b71f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b71c4.md#insn-005b71f0) · [`005b71f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b71c4.md#insn-005b71f4) · [`005b7204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b71c4.md#insn-005b7204)

~~~diff
- 005b71f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 005b71f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005b71f0 bytes e80700f9
- 005b71f4 ["INT_ADD", "register:40f0:8", ["const:5b71f4:8", "const:4:8"]]
- 005b71f4 ["CALL", null, ["callee:00c58f30:8"]]
- 005b71f4 bytes 5b831a94
- 005b7204 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005b7204 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005b7204 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8854763db0090e340af960b28f6f050"></a>

### [`005b73d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b73d0.md) → [`005b7780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7780.md) FUN_005b7780

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b7798",
      "incomplete_value": false,
      "site": "005b77a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b73e8",
      "incomplete_value": false,
      "site": "005b73f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "005b77a4",
      "DATA",
      [
        "storage",
        "00c706e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b77a4",
      "DATA",
      [
        "storage",
        "00c716b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b73e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b73d0.md#insn-005b73e4) · [`005b73e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b73d0.md#insn-005b73e8) · [`005b73fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b73d0.md#insn-005b73fc)
- 新版 [`005b7794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7780.md#insn-005b7794) · [`005b7798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7780.md#insn-005b7798) · [`005b77ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7780.md#insn-005b77ac)

~~~diff
- 005b73e4 ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b7794 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b73e4 bytes c83500b0
+ 005b7794 bytes c83500d0
- 005b73e8 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 005b73e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b73e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b73e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7798 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 005b7798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b73e8 bytes 08811b91
+ 005b7798 bytes 08c11a91
- 005b73fc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 005b73fc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 005b77ac ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 005b77ac ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 005b73fc bytes 000100b4
+ 005b77ac bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3df94bb10a17571a24149eca685b7efd"></a>

### [`005b7774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7774.md) → [`005b7b24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7b24.md) FUN_005b7b24

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b1e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1e64.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`005b2214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b2/005b2214.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b7b64",
      "incomplete_value": false,
      "site": "005b7b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:ab0:8"
              ]
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
      "definition_site": "005b77b4",
      "incomplete_value": false,
      "site": "005b77b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
              ]
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
      "005b7b68",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7b68",
      "DATA",
      [
        "storage",
        "00c6eac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7774.md#insn-005b7794) · [`005b77a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7774.md#insn-005b77a4) · [`005b77a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7774.md#insn-005b77a8)
- 新版 [`005b7b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7b24.md#insn-005b7b44) · [`005b7b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7b24.md#insn-005b7b54) · [`005b7b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7b24.md#insn-005b7b58)

~~~diff
- 005b7794 ["INT_ADD", "register:40f0:8", ["const:5b7794:8", "const:4:8"]]
- 005b7794 ["CALL", null, ["callee:00c58f50:8"]]
+ 005b7b44 ["INT_ADD", "register:40f0:8", ["const:5b7b44:8", "const:4:8"]]
+ 005b7b44 ["CALL", null, ["callee:00c58f50:8"]]
- 005b7794 bytes fb811a94
+ 005b7b44 bytes 03851a94
- 005b77a4 ["INT_ADD", "register:40f0:8", ["const:5b77a4:8", "const:4:8"]]
- 005b77a4 ["CALL", null, ["callee:00c58f50:8"]]
+ 005b7b54 ["INT_ADD", "register:40f0:8", ["const:5b7b54:8", "const:4:8"]]
+ 005b7b54 ["CALL", null, ["callee:00c58f50:8"]]
- 005b77a4 bytes f7811a94
+ 005b7b54 bytes ff841a94
- 005b77a8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 005b7b58 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005b77a8 bytes a83500d0
+ 005b7b58 bytes a83500f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daeb8a2f7bc1689526cefa5f4c85bbb0"></a>

### [`005b77ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b77ec.md) → [`005b7b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7b9c.md) FUN_005b7b9c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b1e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1e64.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`005b2214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b2/005b2214.md) · 呼出先 7件 [`00598230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md) [`005b772c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b772c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b7bd4",
      "incomplete_value": false,
      "site": "005b7bdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7824",
      "incomplete_value": false,
      "site": "005b782c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:690:8"
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
      "005b7bdc",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "005b7c94",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7bdc",
      "DATA",
      [
        "storage",
        "00c71660",
        null,
        "pointer"
      ]
    ],
    [
      "005b7c94",
      "READ",
      [
        "storage",
        "00c71670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b781c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b77ec.md#insn-005b781c) · [`005b7820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b77ec.md#insn-005b7820) · [`005b7824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b77ec.md#insn-005b7824)
- 新版 [`005b7bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7b9c.md#insn-005b7bcc) · [`005b7bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7b9c.md#insn-005b7bd0) · [`005b7bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7b9c.md#insn-005b7bd4)

~~~diff
- 005b781c ["INT_ADD", "register:40f0:8", ["const:5b781c:8", "const:4:8"]]
- 005b781c ["CALL", null, ["callee:00c58f30:8"]]
+ 005b7bcc ["INT_ADD", "register:40f0:8", ["const:5b7bcc:8", "const:4:8"]]
+ 005b7bcc ["CALL", null, ["callee:00c58f30:8"]]
- 005b781c bytes d1811a94
+ 005b7bcc bytes d9841a94
- 005b7820 ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b7bd0 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b7820 bytes c83500b0
+ 005b7bd0 bytes c83500d0
- 005b7824 ["COPY", "tmp:0:8", ["const:690:8"]]
- 005b7824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7bd4 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 005b7bd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7bd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7824 bytes 08411a91
+ 005b7bd4 bytes 08811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f16132e6f0c4f29a777caaa2781a88b2"></a>

### [`005b7964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7964.md) → [`005b7d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7d14.md) FUN_005b7d14

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b7d20",
      "incomplete_value": false,
      "site": "005b7d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7970",
      "incomplete_value": false,
      "site": "005b797c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "005b7d2c",
      "DATA",
      [
        "storage",
        "00c70770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7d2c",
      "DATA",
      [
        "storage",
        "00c71740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7964.md#insn-005b796c) · [`005b7970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7964.md#insn-005b7970)
- 新版 [`005b7d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7d14.md#insn-005b7d1c) · [`005b7d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7d14.md#insn-005b7d20)

~~~diff
- 005b796c ["COPY", "register:4050:8", ["const:c70000:8"]]
+ 005b7d1c ["COPY", "register:4050:8", ["const:c71000:8"]]
- 005b796c bytes ca3500b0
+ 005b7d1c bytes ca3500d0
- 005b7970 ["COPY", "tmp:0:8", ["const:770:8"]]
- 005b7970 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b7970 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b7970 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b7d20 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 005b7d20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b7d20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b7d20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b7970 bytes 4ac11d91
+ 005b7d20 bytes 4a011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8ac12c5703a85d9e974b22e68c18c2f"></a>

### [`005b79a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b79a8.md) → [`005b7d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7d58.md) FUN_005b7d58

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b7d70",
      "incomplete_value": false,
      "site": "005b7d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b79c0",
      "incomplete_value": false,
      "site": "005b79cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "005b7d7c",
      "DATA",
      [
        "storage",
        "00c70770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7d7c",
      "DATA",
      [
        "storage",
        "00c71740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b79bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b79a8.md#insn-005b79bc) · [`005b79c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b79a8.md#insn-005b79c0) · [`005b79f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b79a8.md#insn-005b79f0)
- 新版 [`005b7d6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7d58.md#insn-005b7d6c) · [`005b7d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7d58.md#insn-005b7d70) · [`005b7da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7d58.md#insn-005b7da0)

~~~diff
- 005b79bc ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b7d6c ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b79bc bytes c83500b0
+ 005b7d6c bytes c83500d0
- 005b79c0 ["COPY", "tmp:0:8", ["const:770:8"]]
- 005b79c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b79c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b79c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7d70 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 005b7d70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7d70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7d70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b79c0 bytes 08c11d91
+ 005b7d70 bytes 08011d91
- 005b79f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b79f0 ["INT_ADD", "register:40f0:8", ["const:5b79f0:8", "const:4:8"]]
- 005b79f0 ["CALLIND", null, ["register:0:8"]]
+ 005b7da0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7da0 ["INT_ADD", "register:40f0:8", ["const:5b7da0:8", "const:4:8"]]
+ 005b7da0 ["CALLIND", null, ["register:0:8"]]
- 005b79f0 bytes 00013fd6
+ 005b7da0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f3f0e523c70883d696e0277ceae5f39"></a>

### [`005b7a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7a04.md) → [`005b7db4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7db4.md) FUN_005b7db4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7a30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b7de0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7a34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b7a30",
      "DATA",
      [
        "storage",
        "00c70770",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b7a34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b7e00"
      ]
    ]
  ],
  "added": [
    [
      "005b7de0",
      "DATA",
      [
        "storage",
        "00c71740",
        null,
        "undefined *"
      ]
    ],
    [
      "005b7de4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b7e00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7a04.md#insn-005b7a30) · [`005b7a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7a04.md#insn-005b7a34)
- 新版 [`005b7de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7db4.md#insn-005b7de0)

~~~diff
- 005b7a30 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b7a30 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 005b7a30 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 005b7a30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b7a30 bytes 280401f8
- 005b7a34 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 005b7a34 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 005b7a34 bytes e00000b4
+ 005b7de0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005b7de0 ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 005b7de0 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
+ 005b7de0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 005b7de0 bytes 280401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ba4504716b6c126700f84e2978c8863"></a>

### [`005b7a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7a8c.md) → [`005b7e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7e3c.md) FUN_005b7e3c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 79.31% / 新版 79.31%

CFGの説明率　旧版 12.50% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b7e58",
      "incomplete_value": false,
      "site": "005b7e58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7aa8",
      "incomplete_value": false,
      "site": "005b7aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7ab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005b7e68"
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
      "005b7e58",
      "DATA",
      [
        "storage",
        "00c70770",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b7ab8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b7e94"
      ]
    ]
  ],
  "added": [
    [
      "005b7e58",
      "DATA",
      [
        "storage",
        "00c71740",
        null,
        "undefined *"
      ]
    ],
    [
      "005b7e68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b7e94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7a8c.md#insn-005b7ab8) · [`005b7ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7a8c.md#insn-005b7ae0)
- 新版 [`005b7e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7e3c.md#insn-005b7e68)

~~~diff
- 005b7ab8 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 005b7ab8 bytes 60010054
- 005b7ae0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005b7ae0 ["RETURN", null, ["register:0:8"]]
- 005b7ae0 bytes c0035fd6
+ 005b7e68 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 005b7e68 bytes 60010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcb91e9e69db21d5348bf324e7c182fe"></a>

### [`005b7b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7b88.md) → [`005b7f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7f38.md) FUN_005b7f38

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.02% / 新版 73.02%

CFGの説明率　旧版 37.04% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7b8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7b8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7b90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b7b8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b7b90",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b7b94",
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
      "005b7f3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005b7f40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b7f44",
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

- 旧版 [`005b7b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7b88.md#insn-005b7b8c) · [`005b7b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7b88.md#insn-005b7b90) · [`005b7b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7b88.md#insn-005b7b94)

~~~diff
- 005b7b8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005b7b8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005b7b8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 005b7b8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b7b8c bytes fd7b03a9
- 005b7b90 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005b7b90 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005b7b90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 005b7b90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b7b90 bytes f65704a9
- 005b7b94 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005b7b94 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005b7b94 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 005b7b94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b7b94 bytes f44f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d8feda09dcc77cdf44e7f2a9ac407f9"></a>

### [`005b7d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7d38.md) → [`005b80e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b80e8.md) FUN_005b80e8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b3638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3638.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`005b39e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b3/005b39e8.md) · 呼出先 7件 [`00598230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md) [`005b772c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b772c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 94.81% / 新版 94.81%

CFGの説明率　旧版 85.71% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b8120",
      "incomplete_value": false,
      "site": "005b8128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7d70",
      "incomplete_value": false,
      "site": "005b7d78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7e34"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "005b81e4"
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
      "005b8128",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "005b81e0",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b7e34",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "005b772c"
      ]
    ]
  ],
  "added": [
    [
      "005b8128",
      "DATA",
      [
        "storage",
        "00c71660",
        null,
        "pointer"
      ]
    ],
    [
      "005b81e0",
      "READ",
      [
        "storage",
        "00c71670",
        null,
        "undefined *"
      ]
    ],
    [
      "005b81e4",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "005b772c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7d38.md#insn-005b7e34) · [`005b7d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7d38.md#insn-005b7d68)
- 新版 [`005b81e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b80e8.md#insn-005b81e4) · [`005b8118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b80e8.md#insn-005b8118)

~~~diff
- 005b7e34 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7e34 ["INT_ADD", "register:40f0:8", ["const:5b7e34:8", "const:4:8"]]
- 005b7e34 ["CALLIND", null, ["register:0:8"]]
- 005b7e34 bytes 00013fd6
+ 005b81e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b81e4 ["INT_ADD", "register:40f0:8", ["const:5b81e4:8", "const:4:8"]]
+ 005b81e4 ["CALLIND", null, ["register:0:8"]]
+ 005b81e4 bytes 00013fd6
- 005b7d68 ["INT_ADD", "register:40f0:8", ["const:5b7d68:8", "const:4:8"]]
- 005b7d68 ["CALL", null, ["callee:00c58f30:8"]]
+ 005b8118 ["INT_ADD", "register:40f0:8", ["const:5b8118:8", "const:4:8"]]
+ 005b8118 ["CALL", null, ["callee:00c58f30:8"]]
- 005b7d68 bytes 7e801a94
+ 005b8118 bytes 86831a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e8f54dc32806741ce0d7decaa26b69e"></a>

### [`005b7f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7f50.md) → [`005b8300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8300.md) FUN_005b8300

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.52% / 新版 65.52%

CFGの説明率　旧版 20.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7f7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b832c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7f80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b7f7c",
      "DATA",
      [
        "storage",
        "00c707f0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b7f80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b834c"
      ]
    ],
    [
      "unmatched:005b7f8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8354"
      ]
    ]
  ],
  "added": [
    [
      "005b832c",
      "DATA",
      [
        "storage",
        "00c717c0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b8330",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b834c"
      ]
    ],
    [
      "005b833c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8354"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7f50.md#insn-005b7f7c) · [`005b7f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7f50.md#insn-005b7f80) · [`005b7f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7f50.md#insn-005b7f8c)

~~~diff
- 005b7f7c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b7f7c ["COPY", "tmp:1:8", ["register:4008:8"]]
- 005b7f7c ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 005b7f7c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b7f7c bytes 280401f8
- 005b7f80 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 005b7f80 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 005b7f80 bytes e00000b4
- 005b7f8c ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 005b7f8c bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38d296f47b290e141e2b7b6de5f334cf"></a>

### [`005b811c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b811c.md) → [`005b84cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b84cc.md) FUN_005b84cc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b279c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b279c.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`005b2b4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b2/005b2b4c.md) · 呼出先 7件 [`00598230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md) [`005b772c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b772c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.22% / 新版 79.22%

CFGの説明率　旧版 11.11% / 新版 10.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b815c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8174"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8178"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b815c",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005b8178",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b8184",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00598230"
      ]
    ]
  ],
  "added": [
    [
      "005b850c",
      "DATA",
      [
        "storage",
        "00c71660",
        null,
        "pointer"
      ]
    ],
    [
      "005b8528",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005b8534",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00598230"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b815c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b811c.md#insn-005b815c) · [`005b8174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b811c.md#insn-005b8174) · [`005b8178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b811c.md#insn-005b8178)

~~~diff
- 005b815c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005b815c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005b815c bytes 080000f9
- 005b8174 ["COPY", "tmp:0:8", ["const:0:8"]]
- 005b8174 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 005b8174 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
- 005b8174 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:1:8"]]
- 005b8174 bytes 9f8e00f8
- 005b8178 ["COPY", "tmp:0:8", ["register:8:8"]]
- 005b8178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005b8178 bytes e80300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eabac95c6748b8390455816806ada5f7"></a>

### [`005b8334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8334.md) → [`005b86e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b86e4.md) FUN_005b86e4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.52% / 新版 65.52%

CFGの説明率　旧版 22.22% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8360"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b8710"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8364"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b8360",
      "DATA",
      [
        "storage",
        "00c70870",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b8364",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8730"
      ]
    ],
    [
      "unmatched:005b8370",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8738"
      ]
    ]
  ],
  "added": [
    [
      "005b8710",
      "DATA",
      [
        "storage",
        "00c71840",
        null,
        "undefined *"
      ]
    ],
    [
      "005b8714",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8730"
      ]
    ],
    [
      "005b8720",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8334.md#insn-005b8360) · [`005b8364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8334.md#insn-005b8364) · [`005b8370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8334.md#insn-005b8370)

~~~diff
- 005b8360 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b8360 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 005b8360 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 005b8360 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b8360 bytes 280401f8
- 005b8364 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 005b8364 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 005b8364 bytes e00000b4
- 005b8370 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 005b8370 bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b70eaa53b6e11beae6dba7278319a533"></a>

### [`005b83bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b83bc.md) → [`005b876c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b876c.md) FUN_005b876c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 62.07% / 新版 62.07%

CFGの説明率　旧版 25.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b83d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b8788"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b83dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b83d8",
      "DATA",
      [
        "storage",
        "00c70870",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b83dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b87b4"
      ]
    ],
    [
      "unmatched:005b83e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b87c4"
      ]
    ]
  ],
  "added": [
    [
      "005b8788",
      "DATA",
      [
        "storage",
        "00c71840",
        null,
        "undefined *"
      ]
    ],
    [
      "005b878c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b87b4"
      ]
    ],
    [
      "005b8798",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b87c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b83d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b83bc.md#insn-005b83d8) · [`005b83dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b83bc.md#insn-005b83dc) · [`005b83e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b83bc.md#insn-005b83e8)

~~~diff
- 005b83d8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005b83d8 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 005b83d8 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 005b83d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b83d8 bytes 290401f8
- 005b83dc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005b83dc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 005b83dc bytes 480100b4
- 005b83e8 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 005b83e8 bytes 60010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5d167e8705fd989e8265c9315e10127"></a>

### [`005b84b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b84b8.md) → [`005b8868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8868.md) FUN_005b8868

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b84bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005b886c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005b84d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b84bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b887c"
      ]
    ],
    [
      "unmatched:005b84d4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0045a0d4"
      ]
    ]
  ],
  "added": [
    [
      "005b886c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b887c"
      ]
    ],
    [
      "005b8884",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0045a0d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b84bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b84b8.md#insn-005b84bc) · [`005b84d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b84b8.md#insn-005b84d4)
- 新版 [`005b886c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8868.md#insn-005b886c)

~~~diff
- 005b84bc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 005b84bc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 005b84bc bytes 800000b4
- 005b84d4 ["INT_ADD", "register:40f0:8", ["const:5b84d4:8", "const:4:8"]]
- 005b84d4 ["CALL", null, ["callee:0045a0d4:8"]]
- 005b84d4 bytes 3886fa97
+ 005b886c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 005b886c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 005b886c bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb2ebf28e87ff7859128ac8d020094a0"></a>

### [`005b8500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8500.md) → [`005b88b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b88b0.md) FUN_005b88b0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b4060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b4060.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`005b4410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b4/005b4410.md) · 呼出先 7件 [`00598230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md) [`005b772c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b772c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 7.69% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8504"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8504"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8508"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b8504",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b8508",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b850c",
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
      "005b88b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005b88b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005b88bc",
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

- 旧版 [`005b8504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8500.md#insn-005b8504) · [`005b8508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8500.md#insn-005b8508) · [`005b850c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8500.md#insn-005b850c)

~~~diff
- 005b8504 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005b8504 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005b8504 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005b8504 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b8504 bytes fd7b01a9
- 005b8508 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005b8508 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005b8508 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005b8508 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b8508 bytes f85f02a9
- 005b850c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005b850c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005b850c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 005b850c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b850c bytes f65703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72fb4182b19f7d2543a7e8b58beec2e5"></a>

### [`005b8718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8718.md) → [`005b8ac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8ac8.md) FUN_005b8ac8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.97% / 新版 68.97%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8744"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b8af4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8748"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b8744",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b8748",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8b14"
      ]
    ],
    [
      "unmatched:005b8754",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8b1c"
      ]
    ]
  ],
  "added": [
    [
      "005b8af4",
      "DATA",
      [
        "storage",
        "00c718c0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b8af8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8b14"
      ]
    ],
    [
      "005b8b04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8b1c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8718.md#insn-005b8744) · [`005b8748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8718.md#insn-005b8748) · [`005b8754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8718.md#insn-005b8754)

~~~diff
- 005b8744 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b8744 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 005b8744 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 005b8744 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b8744 bytes 280401f8
- 005b8748 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 005b8748 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 005b8748 bytes e00000b4
- 005b8754 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 005b8754 bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6357e22aad76fd92fb31fbf6150181a0"></a>

### [`005b87a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b87a0.md) → [`005b8b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8b50.md) FUN_005b8b50

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 75.86% / 新版 75.86%

CFGの説明率　旧版 83.33% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b8b6c",
      "incomplete_value": false,
      "site": "005b8b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b87bc",
      "incomplete_value": false,
      "site": "005b87bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "005b8b6c",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b8808",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b880c",
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
      "005b8b6c",
      "DATA",
      [
        "storage",
        "00c718c0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b8bb8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b8bbc",
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

- 旧版 [`005b87b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b87a0.md#insn-005b87b4) · [`005b87b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b87a0.md#insn-005b87b8) · [`005b87dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b87a0.md#insn-005b87dc)
- 新版 [`005b8b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8b50.md#insn-005b8b64) · [`005b8b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8b50.md#insn-005b8b68) · [`005b8b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8b50.md#insn-005b8b8c)

~~~diff
- 005b87b4 ["COPY", "register:4048:8", ["const:c70000:8"]]
+ 005b8b64 ["COPY", "register:4048:8", ["const:c71000:8"]]
- 005b87b4 bytes c9350090
+ 005b8b64 bytes c93500b0
- 005b87b8 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 005b87b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b87b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b87b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b8b68 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 005b8b68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b8b68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b8b68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b87b8 bytes 29c12391
+ 005b8b68 bytes 29012391
- 005b87dc ["COPY", "register:0:8", ["register:4048:8"]]
- 005b87dc ["INT_ADD", "register:40f0:8", ["const:5b87dc:8", "const:4:8"]]
- 005b87dc ["CALLIND", null, ["register:0:8"]]
+ 005b8b8c ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b8b8c ["INT_ADD", "register:40f0:8", ["const:5b8b8c:8", "const:4:8"]]
+ 005b8b8c ["CALLIND", null, ["register:0:8"]]
- 005b87dc bytes 20013fd6
+ 005b8b8c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a029d70e184b075be5f51214b5479b9"></a>

### [`005b889c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b889c.md) → [`005b8c4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8c4c.md) FUN_005b8c4c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.94% / 新版 94.94%

CFGの説明率　旧版 50.00% / 新版 53.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b88bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b88c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b88c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b88bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b88c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b894c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "005b8c6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "005b8c74",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "005b8cfc",
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

- 旧版 [`005b88bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b889c.md#insn-005b88bc) · [`005b88c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b889c.md#insn-005b88c4) · [`005b88d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b889c.md#insn-005b88d4)
- 新版 [`005b8c84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8c4c.md#insn-005b8c84)

~~~diff
- 005b88bc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b88bc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005b88bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b88bc bytes a8831ff8
- 005b88c4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005b88c4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005b88c4 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 005b88c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b88c4 bytes b6cf3ea9
- 005b88d4 ["INT_ADD", "register:40f0:8", ["const:5b88d4:8", "const:4:8"]]
- 005b88d4 ["CALL", null, ["callee:00c54d60:8"]]
+ 005b8c84 ["INT_ADD", "register:40f0:8", ["const:5b8c84:8", "const:4:8"]]
+ 005b8c84 ["CALL", null, ["callee:00c54d60:8"]]
- 005b88d4 bytes 276d1a94
+ 005b8c84 bytes 37701a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26a224314506c04757ab9fdf576db598"></a>

### [`005b8aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8aa4.md) → [`005b8e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8e54.md) FUN_005b8e54

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b45d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b45d0.md) · 呼出先 7件 [`005aca50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005aca50.md) [`005b8c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c5c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`005b4980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b4/005b4980.md) · 呼出先 7件 [`005ace00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ac/005ace00.md) [`005b900c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b900c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.21% / 新版 92.21%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8ae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8afc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8b00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b8ae4",
      "DATA",
      [
        "storage",
        "00c70970",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005b8b00",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b8b18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8ed8"
      ]
    ]
  ],
  "added": [
    [
      "005b8e94",
      "DATA",
      [
        "storage",
        "00c71940",
        null,
        "pointer"
      ]
    ],
    [
      "005b8eb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005b8ec8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8ed8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8aa4.md#insn-005b8ae4) · [`005b8afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8aa4.md#insn-005b8afc) · [`005b8b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8aa4.md#insn-005b8b00)

~~~diff
- 005b8ae4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005b8ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005b8ae4 bytes 080000f9
- 005b8afc ["COPY", "tmp:0:8", ["const:0:8"]]
- 005b8afc ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 005b8afc ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
- 005b8afc ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:1:8"]]
- 005b8afc bytes 9f8e00f8
- 005b8b00 ["COPY", "tmp:0:8", ["register:8:8"]]
- 005b8b00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005b8b00 bytes e80300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66c87e0082944376eb5cf9306438ead2"></a>

### [`005b8c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c1c.md) → [`005b8fcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8fcc.md) FUN_005b8fcc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b8fd0",
      "incomplete_value": false,
      "site": "005b8fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8c20",
      "incomplete_value": false,
      "site": "005b8c24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "005b8fd4",
      "DATA",
      [
        "storage",
        "00c70970",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b8fd4",
      "DATA",
      [
        "storage",
        "00c71940",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c1c.md#insn-005b8c1c) · [`005b8c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c1c.md#insn-005b8c20)
- 新版 [`005b8fcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8fcc.md#insn-005b8fcc) · [`005b8fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8fcc.md#insn-005b8fd0)

~~~diff
- 005b8c1c ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b8fcc ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b8c1c bytes c8350090
+ 005b8fcc bytes c83500b0
- 005b8c20 ["COPY", "tmp:0:8", ["const:970:8"]]
- 005b8c20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8c20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8c20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8fd0 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 005b8fd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8fd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8fd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8c20 bytes 08c12591
+ 005b8fd0 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7282aaaeff84deca241c8a792cb0a96"></a>

### [`005b8c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c2c.md) → [`005b8fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8fdc.md) FUN_005b8fdc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b8fec",
      "incomplete_value": false,
      "site": "005b8ff4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8c3c",
      "incomplete_value": false,
      "site": "005b8c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "005b8ff4",
      "DATA",
      [
        "storage",
        "00c70970",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b8ff4",
      "DATA",
      [
        "storage",
        "00c71940",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c2c.md#insn-005b8c38) · [`005b8c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c2c.md#insn-005b8c3c) · [`005b8c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c2c.md#insn-005b8c48)
- 新版 [`005b8fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8fdc.md#insn-005b8fe8) · [`005b8fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8fdc.md#insn-005b8fec) · [`005b8ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8fdc.md#insn-005b8ff8)

~~~diff
- 005b8c38 ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b8fe8 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b8c38 bytes c8350090
+ 005b8fe8 bytes c83500b0
- 005b8c3c ["COPY", "tmp:0:8", ["const:970:8"]]
- 005b8c3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8c3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8c3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8fec ["COPY", "tmp:0:8", ["const:940:8"]]
+ 005b8fec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8fec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8fec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8c3c bytes 08c12591
+ 005b8fec bytes 08012591
- 005b8c48 ["INT_ADD", "register:40f0:8", ["const:5b8c48:8", "const:4:8"]]
- 005b8c48 ["CALL", null, ["callee:00c58f40:8"]]
+ 005b8ff8 ["INT_ADD", "register:40f0:8", ["const:5b8ff8:8", "const:4:8"]]
+ 005b8ff8 ["CALL", null, ["callee:00c58f40:8"]]
- 005b8c48 bytes ca7c1a94
+ 005b8ff8 bytes d27f1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c82fea727cf87859cfc827553f2395a5"></a>

### [`005b8c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c6c.md) → [`005b901c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b901c.md) FUN_005b901c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b9028",
      "incomplete_value": false,
      "site": "005b9034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8c78",
      "incomplete_value": false,
      "site": "005b8c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "005b9034",
      "DATA",
      [
        "storage",
        "00c709c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b9034",
      "DATA",
      [
        "storage",
        "00c71990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c6c.md#insn-005b8c74) · [`005b8c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c6c.md#insn-005b8c78)
- 新版 [`005b9024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b901c.md#insn-005b9024) · [`005b9028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b901c.md#insn-005b9028)

~~~diff
- 005b8c74 ["COPY", "register:4050:8", ["const:c70000:8"]]
+ 005b9024 ["COPY", "register:4050:8", ["const:c71000:8"]]
- 005b8c74 bytes ca350090
+ 005b9024 bytes ca350090
- 005b8c78 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 005b8c78 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b8c78 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b8c78 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b9028 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 005b9028 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9028 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9028 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b8c78 bytes 4a012791
+ 005b9028 bytes 4a412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-471afe6ff83b9c5eff8420ce70c5becf"></a>

### [`005b8cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8cb0.md) → [`005b9060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9060.md) FUN_005b9060

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b9078",
      "incomplete_value": false,
      "site": "005b9084",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8cc8",
      "incomplete_value": false,
      "site": "005b8cd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "005b9084",
      "DATA",
      [
        "storage",
        "00c709c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b9084",
      "DATA",
      [
        "storage",
        "00c71990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8cb0.md#insn-005b8cc4) · [`005b8cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8cb0.md#insn-005b8cc8) · [`005b8cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8cb0.md#insn-005b8cf8)
- 新版 [`005b9074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9060.md#insn-005b9074) · [`005b9078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9060.md#insn-005b9078) · [`005b90a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9060.md#insn-005b90a8)

~~~diff
- 005b8cc4 ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b9074 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b8cc4 bytes c8350090
+ 005b9074 bytes c8350090
- 005b8cc8 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 005b8cc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8cc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8cc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b9078 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 005b9078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b9078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b9078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8cc8 bytes 08012791
+ 005b9078 bytes 08412691
- 005b8cf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8cf8 ["INT_ADD", "register:40f0:8", ["const:5b8cf8:8", "const:4:8"]]
- 005b8cf8 ["CALLIND", null, ["register:0:8"]]
+ 005b90a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b90a8 ["INT_ADD", "register:40f0:8", ["const:5b90a8:8", "const:4:8"]]
+ 005b90a8 ["CALLIND", null, ["register:0:8"]]
- 005b8cf8 bytes 00013fd6
+ 005b90a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b400522dc4f74d25014e86337d4e7409"></a>

### [`005b8d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d0c.md) → [`005b90bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b90bc.md) FUN_005b90bc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b90e8",
      "incomplete_value": false,
      "site": "005b90e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8d38",
      "incomplete_value": false,
      "site": "005b8d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "005b90e8",
      "DATA",
      [
        "storage",
        "00c709c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b90e8",
      "DATA",
      [
        "storage",
        "00c71990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d0c.md#insn-005b8d20) · [`005b8d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d0c.md#insn-005b8d2c) · [`005b8d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d0c.md#insn-005b8d30)
- 新版 [`005b90d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b90bc.md#insn-005b90d0) · [`005b90dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b90bc.md#insn-005b90dc) · [`005b90e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b90bc.md#insn-005b90e0)

~~~diff
- 005b8d20 ["INT_ADD", "register:40f0:8", ["const:5b8d20:8", "const:4:8"]]
- 005b8d20 ["CALL", null, ["callee:00c58f30:8"]]
+ 005b90d0 ["INT_ADD", "register:40f0:8", ["const:5b90d0:8", "const:4:8"]]
+ 005b90d0 ["CALL", null, ["callee:00c58f30:8"]]
- 005b8d20 bytes 907c1a94
+ 005b90d0 bytes 987f1a94
- 005b8d2c ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b90dc ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b8d2c bytes c8350090
+ 005b90dc bytes c8350090
- 005b8d30 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 005b8d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b90e0 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 005b90e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b90e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b90e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8d30 bytes 08012791
+ 005b90e0 bytes 08412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfed0c60624ef66e13284bbd9818d505"></a>

### [`005b8d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d94.md) → [`005b9144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9144.md) FUN_005b9144

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b9160",
      "incomplete_value": false,
      "site": "005b9160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8db0",
      "incomplete_value": false,
      "site": "005b8db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "005b9160",
      "DATA",
      [
        "storage",
        "00c709c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b9160",
      "DATA",
      [
        "storage",
        "00c71990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d94.md#insn-005b8da8) · [`005b8dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d94.md#insn-005b8dac) · [`005b8dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d94.md#insn-005b8dd0)
- 新版 [`005b9158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9144.md#insn-005b9158) · [`005b915c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9144.md#insn-005b915c) · [`005b9180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9144.md#insn-005b9180)

~~~diff
- 005b8da8 ["COPY", "register:4048:8", ["const:c70000:8"]]
+ 005b9158 ["COPY", "register:4048:8", ["const:c71000:8"]]
- 005b8da8 bytes c9350090
+ 005b9158 bytes c9350090
- 005b8dac ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 005b8dac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b8dac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b8dac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b915c ["COPY", "tmp:0:8", ["const:990:8"]]
+ 005b915c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b915c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b915c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b8dac bytes 29012791
+ 005b915c bytes 29412691
- 005b8dd0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b8dd0 ["INT_ADD", "register:40f0:8", ["const:5b8dd0:8", "const:4:8"]]
- 005b8dd0 ["CALLIND", null, ["register:0:8"]]
+ 005b9180 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b9180 ["INT_ADD", "register:40f0:8", ["const:5b9180:8", "const:4:8"]]
+ 005b9180 ["CALLIND", null, ["register:0:8"]]
- 005b8dd0 bytes 20013fd6
+ 005b9180 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a4968bd6f0b4db7b711e9208a4a8e3e"></a>

### [`005b8ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8ff4.md) → [`005b93a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b93a4.md) FUN_005b93a4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b4ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b4ad8.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`005b4e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b4/005b4e88.md) · 呼出先 7件 [`00598230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md) [`005b772c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b772c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b93dc",
      "incomplete_value": false,
      "site": "005b93e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b902c",
      "incomplete_value": false,
      "site": "005b9034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:690:8"
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
      "005b93e4",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "005b949c",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b93e4",
      "DATA",
      [
        "storage",
        "00c71660",
        null,
        "pointer"
      ]
    ],
    [
      "005b949c",
      "READ",
      [
        "storage",
        "00c71670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b9024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8ff4.md#insn-005b9024) · [`005b9028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8ff4.md#insn-005b9028) · [`005b902c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8ff4.md#insn-005b902c)
- 新版 [`005b93d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b93a4.md#insn-005b93d4) · [`005b93d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b93a4.md#insn-005b93d8) · [`005b93dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b93a4.md#insn-005b93dc)

~~~diff
- 005b9024 ["INT_ADD", "register:40f0:8", ["const:5b9024:8", "const:4:8"]]
- 005b9024 ["CALL", null, ["callee:00c58f30:8"]]
+ 005b93d4 ["INT_ADD", "register:40f0:8", ["const:5b93d4:8", "const:4:8"]]
+ 005b93d4 ["CALL", null, ["callee:00c58f30:8"]]
- 005b9024 bytes cf7b1a94
+ 005b93d4 bytes d77e1a94
- 005b9028 ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b93d8 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b9028 bytes a83500f0
+ 005b93d8 bytes c8350090
- 005b902c ["COPY", "tmp:0:8", ["const:690:8"]]
- 005b902c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b902c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b902c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b93dc ["COPY", "tmp:0:8", ["const:660:8"]]
+ 005b93dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b93dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b93dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b902c bytes 08411a91
+ 005b93dc bytes 08811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffadb1b4147b33d659d13d4a95493529"></a>

### [`005b916c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b916c.md) → [`005b951c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b951c.md) FUN_005b951c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b9528",
      "incomplete_value": false,
      "site": "005b9534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b9178",
      "incomplete_value": false,
      "site": "005b9184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      "005b9534",
      "DATA",
      [
        "storage",
        "00c70a40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b9534",
      "DATA",
      [
        "storage",
        "00c71a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b9174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b916c.md#insn-005b9174) · [`005b9178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b916c.md#insn-005b9178)
- 新版 [`005b9524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b951c.md#insn-005b9524) · [`005b9528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b951c.md#insn-005b9528)

~~~diff
- 005b9174 ["COPY", "register:4050:8", ["const:c70000:8"]]
+ 005b9524 ["COPY", "register:4050:8", ["const:c71000:8"]]
- 005b9174 bytes aa3500f0
+ 005b9524 bytes ca350090
- 005b9178 ["COPY", "tmp:0:8", ["const:a40:8"]]
- 005b9178 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b9178 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b9178 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b9528 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005b9528 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9528 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9528 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b9178 bytes 4a012991
+ 005b9528 bytes 4a412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9805ac0f2bb92c164ba8cce176731746"></a>

### [`005b91b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b91b0.md) → [`005b9560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9560.md) FUN_005b9560

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b9578",
      "incomplete_value": false,
      "site": "005b9584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b91c8",
      "incomplete_value": false,
      "site": "005b91d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      "005b9584",
      "DATA",
      [
        "storage",
        "00c70a40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b9584",
      "DATA",
      [
        "storage",
        "00c71a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b91c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b91b0.md#insn-005b91c4) · [`005b91c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b91b0.md#insn-005b91c8) · [`005b91f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b91b0.md#insn-005b91f8)
- 新版 [`005b9574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9560.md#insn-005b9574) · [`005b9578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9560.md#insn-005b9578) · [`005b95a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9560.md#insn-005b95a8)

~~~diff
- 005b91c4 ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005b9574 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b91c4 bytes a83500f0
+ 005b9574 bytes c8350090
- 005b91c8 ["COPY", "tmp:0:8", ["const:a40:8"]]
- 005b91c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b91c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b91c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b9578 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005b9578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b9578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b9578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b91c8 bytes 08012991
+ 005b9578 bytes 08412891
- 005b91f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b91f8 ["INT_ADD", "register:40f0:8", ["const:5b91f8:8", "const:4:8"]]
- 005b91f8 ["CALLIND", null, ["register:0:8"]]
+ 005b95a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b95a8 ["INT_ADD", "register:40f0:8", ["const:5b95a8:8", "const:4:8"]]
+ 005b95a8 ["CALLIND", null, ["register:0:8"]]
- 005b91f8 bytes 00013fd6
+ 005b95a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-138ca8e6783350d6ad323313011c9bb6"></a>

### [`005b920c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b920c.md) → [`005b95bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b95bc.md) FUN_005b95bc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b95e8",
      "incomplete_value": false,
      "site": "005b95e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b9238",
      "incomplete_value": false,
      "site": "005b9238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      "site": "005b9254"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "005b9604"
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
      "005b95e8",
      "DATA",
      [
        "storage",
        "00c70a40",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b9254",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "005b95e8",
      "DATA",
      [
        "storage",
        "00c71a10",
        null,
        "undefined *"
      ]
    ],
    [
      "005b9604",
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

- 旧版 [`005b9254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b920c.md#insn-005b9254) · [`005b9220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b920c.md#insn-005b9220)
- 新版 [`005b9604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b95bc.md#insn-005b9604) · [`005b95d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b95bc.md#insn-005b95d0)

~~~diff
- 005b9254 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b9254 ["INT_ADD", "register:40f0:8", ["const:5b9254:8", "const:4:8"]]
- 005b9254 ["CALLIND", null, ["register:0:8"]]
- 005b9254 bytes 00013fd6
+ 005b9604 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b9604 ["INT_ADD", "register:40f0:8", ["const:5b9604:8", "const:4:8"]]
+ 005b9604 ["CALLIND", null, ["register:0:8"]]
+ 005b9604 bytes 00013fd6
- 005b9220 ["INT_ADD", "register:40f0:8", ["const:5b9220:8", "const:4:8"]]
- 005b9220 ["CALL", null, ["callee:00c58f30:8"]]
+ 005b95d0 ["INT_ADD", "register:40f0:8", ["const:5b95d0:8", "const:4:8"]]
+ 005b95d0 ["CALL", null, ["callee:00c58f30:8"]]
- 005b9220 bytes 507b1a94
+ 005b95d0 bytes 587e1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c3eafa0746b4e37cd5bfe6e97df18ad"></a>

### [`005b9294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9294.md) → [`005b9644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9644.md) FUN_005b9644

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b9660",
      "incomplete_value": false,
      "site": "005b9660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b92b0",
      "incomplete_value": false,
      "site": "005b92b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      "005b9660",
      "DATA",
      [
        "storage",
        "00c70a40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b9660",
      "DATA",
      [
        "storage",
        "00c71a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b92a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9294.md#insn-005b92a8) · [`005b92ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9294.md#insn-005b92ac) · [`005b92c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9294.md#insn-005b92c0)
- 新版 [`005b9658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9644.md#insn-005b9658) · [`005b965c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9644.md#insn-005b965c) · [`005b9670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9644.md#insn-005b9670)

~~~diff
- 005b92a8 ["COPY", "register:4048:8", ["const:c70000:8"]]
+ 005b9658 ["COPY", "register:4048:8", ["const:c71000:8"]]
- 005b92a8 bytes a93500f0
+ 005b9658 bytes c9350090
- 005b92ac ["COPY", "tmp:0:8", ["const:a40:8"]]
- 005b92ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b92ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b92ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b965c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005b965c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b965c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b965c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b92ac bytes 29012991
+ 005b965c bytes 29412891
- 005b92c0 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 005b9670 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 005b92c0 bytes 60010054
+ 005b9670 bytes 60010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-054606b4b8b050940e41d710ec888230"></a>

### [`005b9540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9540.md) → [`00889e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889e80.md) FUN_00889e80

採用 · 移動量 `+0x2d0940` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`005b2f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2f28.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.76% / 新版 88.76%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b9560"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b95f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00889ea0"
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
      "unmatched:005b9560",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00889ea4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005b967c"
      ]
    ],
    [
      "unmatched:005b9584",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00889f0c"
      ]
    ]
  ],
  "added": [
    [
      "00889ea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00889ea4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00889fbc"
      ]
    ],
    [
      "00889ec4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00889f0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b9560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9540.md#insn-005b9560) · [`005b9584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9540.md#insn-005b9584) · [`005b95f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9540.md#insn-005b95f4)

~~~diff
- 005b9560 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b9560 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005b9560 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b9560 bytes a8831ff8
- 005b9584 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 005b9584 bytes 40020054
- 005b95f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:20:8"]]
- 005b95f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005b95f4 bytes 681200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2d3db2534a6acbbbb0c9a5df2bbe015"></a>

### [`005b96a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b96a8.md) → [`005b9a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9a58.md) _INIT_61

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 59.89% / 新版 59.89%

CFGの説明率　旧版 52.50% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `unresolved_store_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b96d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b96ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b96f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b96d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b96e4",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005b96ec",
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
      "005b9a88",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "005b9a94",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "005b9a9c",
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

- 旧版 [`005b96d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b96a8.md#insn-005b96d8) · [`005b96ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b96a8.md#insn-005b96ec) · [`005b96f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b96a8.md#insn-005b96f0)

~~~diff
- 005b96d8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005b96d8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005b96d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b96d8 bytes a9831ff8
- 005b96ec ["COPY", "tmp:0:4", ["register:4050:4"]]
- 005b96ec ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 005b96ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 005b96ec bytes ea130278
- 005b96f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 005b96f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 005b96f0 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b91a501795a1b38a8847d8a9f98ae4d1"></a>

### [`005b9ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9ad8.md) → [`005b9e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9e88.md) FUN_005b9e88

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) · 呼出先 2件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md)
- 新版 呼出元 1件 [`00852a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852a10.md) · 呼出先 2件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "site": "005b9ea4",
      "value": [
        "leaf",
        "ram:48d058:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b9af4",
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
      "005b9ea4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ],
  "added": [
    [
      "005b9ea4",
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

- 旧版 [`005b9af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9ad8.md#insn-005b9af4) · [`005b9af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9ad8.md#insn-005b9af8)
- 新版 [`005b9ea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9e88.md#insn-005b9ea4) · [`005b9ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9e88.md#insn-005b9ea8)

~~~diff
- 005b9af4 ["INT_ADD", "register:40f0:8", ["const:5b9af4:8", "const:4:8"]]
- 005b9af4 ["CALL", null, ["ram:48cd38:8"]]
+ 005b9ea4 ["INT_ADD", "register:40f0:8", ["const:5b9ea4:8", "const:4:8"]]
+ 005b9ea4 ["CALL", null, ["ram:48d058:8"]]
- 005b9af4 bytes 914cfb97
+ 005b9ea4 bytes 6d4cfb97
- 005b9af8 ["INT_ADD", "register:40f0:8", ["const:5b9af8:8", "const:4:8"]]
- 005b9af8 ["CALL", null, ["callee:0048d1e4:8"]]
+ 005b9ea8 ["INT_ADD", "register:40f0:8", ["const:5b9ea8:8", "const:4:8"]]
+ 005b9ea8 ["CALL", null, ["callee:0048d1e4:8"]]
- 005b9af8 bytes f34cfb97
+ 005b9ea8 bytes cf4cfb97
~~~


<a id="compare-54331677af5213219d9448e7d2ccddd4"></a>

### [`005b9b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b20.md) → [`005b9ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9ed0.md) FUN_005b9ed0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 3件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`005b9b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b94.md)
- 新版 呼出元 1件 [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) · 呼出先 3件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`005b9f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9f44.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

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
      "site": "005b9ef0",
      "value": [
        "leaf",
        "ram:48d058:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b9b40",
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
      "005b9ef0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ],
  "added": [
    [
      "005b9ef0",
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

- 旧版 [`005b9b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b20.md#insn-005b9b40) · [`005b9b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b20.md#insn-005b9b44) · [`005b9b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b20.md#insn-005b9b6c)
- 新版 [`005b9ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9ed0.md#insn-005b9ef0) · [`005b9ef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9ed0.md#insn-005b9ef4) · [`005b9f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9ed0.md#insn-005b9f1c)

~~~diff
- 005b9b40 ["INT_ADD", "register:40f0:8", ["const:5b9b40:8", "const:4:8"]]
- 005b9b40 ["CALL", null, ["ram:48cd38:8"]]
+ 005b9ef0 ["INT_ADD", "register:40f0:8", ["const:5b9ef0:8", "const:4:8"]]
+ 005b9ef0 ["CALL", null, ["ram:48d058:8"]]
- 005b9b40 bytes 7e4cfb97
+ 005b9ef0 bytes 5a4cfb97
- 005b9b44 ["INT_ADD", "register:40f0:8", ["const:5b9b44:8", "const:4:8"]]
- 005b9b44 ["CALL", null, ["callee:0048d1e4:8"]]
+ 005b9ef4 ["INT_ADD", "register:40f0:8", ["const:5b9ef4:8", "const:4:8"]]
+ 005b9ef4 ["CALL", null, ["callee:0048d1e4:8"]]
- 005b9b44 bytes e04cfb97
+ 005b9ef4 bytes bc4cfb97
- 005b9b6c ["INT_ADD", "register:40f0:8", ["const:5b9b6c:8", "const:4:8"]]
- 005b9b6c ["CALL", null, ["callee:005b9f44:8"]]
+ 005b9f1c ["INT_ADD", "register:40f0:8", ["const:5b9f1c:8", "const:4:8"]]
+ 005b9f1c ["CALL", null, ["callee:005b9f44:8"]]
- 005b9b6c bytes 0a000094
+ 005b9f1c bytes 0a000094
~~~


<a id="compare-9d7b04e789f1d4ea9e7978b326dc2379"></a>

### [`005b9b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b94.md) → [`005b9f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9f44.md) FUN_005b9f44

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b9b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b20.md) · 呼出先 18件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)
- 新版 呼出元 1件 [`005b9ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9ed0.md) · 呼出先 18件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00487c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c8c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487dc4.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.36% / 新版 88.36%

CFGの説明率　旧版 78.95% / 新版 76.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b9f94",
      "incomplete_value": false,
      "site": "005b9f9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b9be4",
      "incomplete_value": false,
      "site": "005b9bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "site": "005b9dd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b9ddc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b9f9c",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "005b9fc4",
      "PARAM",
      [
        "storage",
        "00ca6970",
        null,
        null
      ]
    ],
    [
      "unmatched:005b9d7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ba110"
      ]
    ]
  ],
  "added": [
    [
      "005b9f9c",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "005b9fc4",
      "PARAM",
      [
        "storage",
        "00ca7930",
        null,
        null
      ]
    ],
    [
      "005ba12c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ba110"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b9c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b94.md#insn-005b9c20) · [`005b9d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b94.md#insn-005b9d74) · [`005b9d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b94.md#insn-005b9d7c)
- 新版 [`005b9fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9f44.md#insn-005b9fd0)

~~~diff
- 005b9c20 ["INT_ADD", "register:40f0:8", ["const:5b9c20:8", "const:4:8"]]
- 005b9c20 ["CALL", null, ["callee:00493168:8"]]
+ 005b9fd0 ["INT_ADD", "register:40f0:8", ["const:5b9fd0:8", "const:4:8"]]
+ 005b9fd0 ["CALL", null, ["callee:00493168:8"]]
- 005b9c20 bytes 8a64fb97
+ 005b9fd0 bytes 6664fb97
- 005b9d74 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005b9d74 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 005b9d74 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 005b9d74 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005b9d74 bytes 08b1899a
- 005b9d7c ["INT_NOTEQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 005b9d7c ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 005b9d7c bytes 2bffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85b38ba0aaea312b15454c30eb5c17bb"></a>

### [`005b9f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9f24.md) → [`005ba2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005ba2d4.md) FUN_005ba2d4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 16件 [`005b9b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b94.md) [`005b9f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9f24.md) [`005c6340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c6340.md) [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 2件 [`005b9f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9f24.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 16件 [`005b9f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9f44.md) [`005ba2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005ba2d4.md) [`005c66f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c66f0.md) [`0081b818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081b/0081b818.md) [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 2件 [`005ba2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005ba2d4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b9f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9f24.md#insn-005b9f24) · [`005b9f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9f24.md#insn-005b9f40) · [`005b9f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9f24.md#insn-005b9f4c)
- 新版 [`005ba2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005ba2d4.md#insn-005ba2d4) · [`005ba2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005ba2d4.md#insn-005ba2f0) · [`005ba2fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005ba2d4.md#insn-005ba2fc)

~~~diff
- 005b9f24 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 005b9f24 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 005ba2d4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 005ba2d4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 005b9f24 bytes 610200b4
+ 005ba2d4 bytes 610200b4
- 005b9f40 ["INT_ADD", "register:40f0:8", ["const:5b9f40:8", "const:4:8"]]
- 005b9f40 ["CALL", null, ["local:b0:8"]]
+ 005ba2f0 ["INT_ADD", "register:40f0:8", ["const:5ba2f0:8", "const:4:8"]]
+ 005ba2f0 ["CALL", null, ["local:b0:8"]]
- 005b9f40 bytes f9ffff97
+ 005ba2f0 bytes f9ffff97
- 005b9f4c ["INT_ADD", "register:40f0:8", ["const:5b9f4c:8", "const:4:8"]]
- 005b9f4c ["CALL", null, ["local:b0:8"]]
+ 005ba2fc ["INT_ADD", "register:40f0:8", ["const:5ba2fc:8", "const:4:8"]]
+ 005ba2fc ["CALL", null, ["local:b0:8"]]
- 005b9f4c bytes f6ffff97
+ 005ba2fc bytes f6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e492b417b9380a336af3379b87d70a3d"></a>

### [`005b9f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9f74.md) → [`005ba324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005ba324.md) _INIT_62

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00bc5880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5880.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.41% / 新版 70.41%

CFGの説明率　旧版 51.43% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 21件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b9f78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b9f78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b9f7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b9f78",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b9f7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b9f80",
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
      "005ba328",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005ba32c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005ba330",
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

- 旧版 [`005b9f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9f74.md#insn-005b9f78) · [`005b9f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9f74.md#insn-005b9f7c) · [`005b9f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9f74.md#insn-005b9f80)

~~~diff
- 005b9f78 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005b9f78 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005b9f78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 005b9f78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b9f78 bytes fd7b0fa9
- 005b9f7c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 005b9f7c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005b9f7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 005b9f7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b9f7c bytes fc5710a9
- 005b9f80 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005b9f80 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005b9f80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 005b9f80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b9f80 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c2d430bb1d081ca8da1234ef92db7d0"></a>

### [`005ba350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba350.md) → [`005ba700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005ba700.md) FUN_005ba700

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) · 呼出先 12件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00597f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f08.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00852a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852a10.md) · 呼出先 12件 [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`00598228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598228.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.56% / 新版 71.56%

CFGの説明率　旧版 65.45% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba354"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba354"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba358"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ba354",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ba358",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ba35c",
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
      "005ba704",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005ba708",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005ba70c",
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

- 旧版 [`005ba354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba350.md#insn-005ba354) · [`005ba358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba350.md#insn-005ba358) · [`005ba35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba350.md#insn-005ba35c)

~~~diff
- 005ba354 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005ba354 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005ba354 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 005ba354 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ba354 bytes fd7b05a9
- 005ba358 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 005ba358 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 005ba358 bytes f93300f9
- 005ba35c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005ba35c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005ba35c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 005ba35c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ba35c bytes f85f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-529139678b8f714e1cf16effe40415fb"></a>

### [`005ba7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba7d8.md) → [`005bab88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005bab88.md) FUN_005bab88

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005bae34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005bae34.md) · 呼出先 14件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047b800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b800.md) [`0047b808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b808.md) [`0047b88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b88c.md) [`0047cf48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cf48.md)
- 新版 呼出元 1件 [`005bb1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb1e4.md) · 呼出先 14件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047bb20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047bb20.md) [`0047bb28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047bb28.md) [`0047bbac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047bbac.md) [`0047d268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d268.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.04% / 新版 83.04%

CFGの説明率　旧版 33.33% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba968"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba96c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005bad18"
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
      "005baba0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0084e5f4"
      ]
    ],
    [
      "005babb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b11cb8"
      ]
    ],
    [
      "005babdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b1f4c4"
      ]
    ]
  ],
  "added": [
    [
      "005baba0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0084f5a0"
      ]
    ],
    [
      "005babb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b12cac"
      ]
    ],
    [
      "005babdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b204b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ba7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba7d8.md#insn-005ba7f0) · [`005ba804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba7d8.md#insn-005ba804) · [`005ba82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba7d8.md#insn-005ba82c)
- 新版 [`005baba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005bab88.md#insn-005baba0) · [`005babb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005bab88.md#insn-005babb4) · [`005babdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005bab88.md#insn-005babdc)

~~~diff
- 005ba7f0 ["INT_ADD", "register:40f0:8", ["const:5ba7f0:8", "const:4:8"]]
- 005ba7f0 ["CALL", null, ["ram:84e5f4:8"]]
+ 005baba0 ["INT_ADD", "register:40f0:8", ["const:5baba0:8", "const:4:8"]]
+ 005baba0 ["CALL", null, ["ram:84f5a0:8"]]
- 005ba7f0 bytes 814f0a94
+ 005baba0 bytes 80520a94
- 005ba804 ["INT_ADD", "register:40f0:8", ["const:5ba804:8", "const:4:8"]]
- 005ba804 ["CALL", null, ["ram:b11cb8:8"]]
+ 005babb4 ["INT_ADD", "register:40f0:8", ["const:5babb4:8", "const:4:8"]]
+ 005babb4 ["CALL", null, ["ram:b12cac:8"]]
- 005ba804 bytes 2d5d1594
+ 005babb4 bytes 3e601594
- 005ba82c ["INT_ADD", "register:40f0:8", ["const:5ba82c:8", "const:4:8"]]
- 005ba82c ["CALL", null, ["ram:b1f4c4:8"]]
+ 005babdc ["INT_ADD", "register:40f0:8", ["const:5babdc:8", "const:4:8"]]
+ 005babdc ["CALL", null, ["ram:b204b8:8"]]
- 005ba82c bytes 26931594
+ 005babdc bytes 37961594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6b766d116167db3c24c8fb216b717fa"></a>

### [`005ba998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba998.md) → [`005bad48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005bad48.md) FUN_005bad48

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`005bae0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005bae0c.md) [`005baedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005baedc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`005bb1bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb1bc.md) [`005bb28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb28c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.36% / 新版 87.36%

CFGの説明率　旧版 20.00% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba9bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005baa2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005baa30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ba9bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "005bad90",
      "DATA",
      [
        "storage",
        "00c70b20",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005baa28",
      "READ",
      [
        "storage",
        "002c2d90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005bad6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "005bad90",
      "DATA",
      [
        "storage",
        "00c71af0",
        null,
        "pointer"
      ]
    ],
    [
      "005badd8",
      "READ",
      [
        "storage",
        "002c2de0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ba9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba998.md#insn-005ba9bc) · [`005baa2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba998.md#insn-005baa2c) · [`005baa30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba998.md#insn-005baa30)

~~~diff
- 005ba9bc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005ba9bc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005ba9bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005ba9bc bytes a8831ff8
- 005baa2c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005baa2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 005baa2c bytes 160000f9
- 005baa30 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:18:8"]]
- 005baa30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005baa30 bytes 130c00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f8ec3440315b744fae781bf99fd4b60"></a>

### [`005baba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005baba4.md) → [`005baf54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005baf54.md) FUN_005baf54

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c585b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59580.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 31.58% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005baba4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005baba4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005baba8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005baba4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005baba8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005babc0",
      "DATA",
      [
        "storage",
        "00c70ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005baf54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005baf58",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005baf70",
      "DATA",
      [
        "storage",
        "00c71a90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005baba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005baba4.md#insn-005baba4) · [`005baba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005baba4.md#insn-005baba8) · [`005babc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005baba4.md#insn-005babc0)

~~~diff
- 005baba4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005baba4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005baba4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005baba4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005baba4 bytes fd7bbea9
- 005baba8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005baba8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005baba8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005baba8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005baba8 bytes f44f01a9
- 005babc0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005babc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005babc0 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eec097fe1627103c75d8202f8ee3cd2"></a>

### [`005bac58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005bac58.md) → [`005bb008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb008.md) FUN_005bb008

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c585b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59580.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 48.78% / 新版 48.78%

CFGの説明率　旧版 5.56% / 新版 6.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bac58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bac58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bac5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bac58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bac5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bac74",
      "DATA",
      [
        "storage",
        "00c70ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005bb008",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005bb00c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005bb024",
      "DATA",
      [
        "storage",
        "00c71a90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bac58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005bac58.md#insn-005bac58) · [`005bac5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005bac58.md#insn-005bac5c) · [`005bac74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005bac58.md#insn-005bac74)

~~~diff
- 005bac58 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005bac58 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005bac58 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005bac58 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005bac58 bytes fd7bbea9
- 005bac5c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005bac5c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005bac5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005bac5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bac5c bytes f44f01a9
- 005bac74 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005bac74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005bac74 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-017348485f37d49877d889f212e857d9"></a>

### [`005badb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005badb8.md) → [`005bb168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb168.md) FUN_005bb168

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005baddc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005bb18c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005bade4",
      "incomplete_value": true,
      "site": "005bade8",
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
            "const:18:8"
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
      "unmatched:005badd0",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005baddc",
      "DATA",
      [
        "storage",
        "00c92da8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005bb180",
      "READ",
      [
        "storage",
        "00c9bcf0",
        null,
        "pointer"
      ]
    ],
    [
      "005bb18c",
      "DATA",
      [
        "storage",
        "00c93d78",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005baddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005badb8.md#insn-005baddc) · [`005bade8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005badb8.md#insn-005bade8)
- 新版 [`005bb198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb168.md#insn-005bb198) · [`005bb18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb168.md#insn-005bb18c)

~~~diff
- 005baddc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005baddc ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 005baddc ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:10:8"]]
- 005baddc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005baddc bytes 880601f8
- 005bade8 ["INT_ADD", "register:40f0:8", ["const:5bade8:8", "const:4:8"]]
- 005bade8 ["CALL", null, ["callee:00c58f00:8"]]
+ 005bb198 ["INT_ADD", "register:40f0:8", ["const:5bb198:8", "const:4:8"]]
+ 005bb198 ["CALL", null, ["callee:00c58f00:8"]]
- 005bade8 bytes 52741a94
+ 005bb198 bytes 5a771a94
+ 005bb18c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005bb18c ["COPY", "tmp:1:8", ["register:40a0:8"]]
+ 005bb18c ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:10:8"]]
+ 005bb18c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 005bb18c bytes 880601f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0010af965fdec3d600df44fb5a5d3675"></a>

### [`005baedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005baedc.md) → [`005bb28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb28c.md) FUN_005bb28c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005ba998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba998.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58200.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)
- 新版 呼出元 1件 [`005bad48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005bad48.md) · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c591d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591d0.md) [`00c591e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591e0.md) [`00c591f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 27.27% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005baf48",
      "incomplete_value": true,
      "site": "005baf4c",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005bb310",
      "incomplete_value": true,
      "site": "005bb314",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "005baf7c"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`005baf4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005baedc.md#insn-005baf4c) · [`005baf64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005baedc.md#insn-005baf64) · [`005baf7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005baedc.md#insn-005baf7c)
- 新版 [`005bb2fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb28c.md#insn-005bb2fc) · [`005bb314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb28c.md#insn-005bb314)

~~~diff
- 005baf4c ["INT_ADD", "register:40f0:8", ["const:5baf4c:8", "const:4:8"]]
- 005baf4c ["CALL", null, ["callee:00c58f50:8"]]
+ 005bb2fc ["INT_ADD", "register:40f0:8", ["const:5bb2fc:8", "const:4:8"]]
+ 005bb2fc ["CALL", null, ["callee:00c58f50:8"]]
- 005baf4c bytes 0d741a94
+ 005bb2fc bytes 15771a94
- 005baf64 ["INT_ADD", "register:40f0:8", ["const:5baf64:8", "const:4:8"]]
- 005baf64 ["CALL", null, ["callee:00c58f50:8"]]
+ 005bb314 ["INT_ADD", "register:40f0:8", ["const:5bb314:8", "const:4:8"]]
+ 005bb314 ["CALL", null, ["callee:00c58f50:8"]]
- 005baf64 bytes 07741a94
+ 005bb314 bytes 0f771a94
- 005baf7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 005baf7c ["RETURN", null, ["register:0:8"]]
- 005baf7c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d19eb281bdf60cf435a9983cc3d8816"></a>

### [`005bafa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005bafa8.md) → [`005bb358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb358.md) FUN_005bb358

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c591f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 16.67% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005bafc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005bb378"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005bb37c",
      "incomplete_value": true,
      "site": "005bb380",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bafc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005bb38c"
      ]
    ]
  ],
  "added": [
    [
      "005bb378",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005bb38c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bafc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005bafa8.md#insn-005bafc8) · [`005bafd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005bafa8.md#insn-005bafd0)
- 新版 [`005bb380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb358.md#insn-005bb380) · [`005bb378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb358.md#insn-005bb378)

~~~diff
- 005bafc8 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 005bafc8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 005bafc8 bytes b40000b4
- 005bafd0 ["INT_ADD", "register:40f0:8", ["const:5bafd0:8", "const:4:8"]]
- 005bafd0 ["CALL", null, ["callee:00c591f0:8"]]
+ 005bb380 ["INT_ADD", "register:40f0:8", ["const:5bb380:8", "const:4:8"]]
+ 005bb380 ["CALL", null, ["callee:00c591f0:8"]]
- 005bafd0 bytes 94741a94
+ 005bb380 bytes 9c771a94
+ 005bb378 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 005bb378 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 005bb378 bytes b40000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfbc59147e3b8e0ec172e44218ffee5c"></a>

### [`005baff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005baff8.md) → [`005bb3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb3a8.md) _INIT_63

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 75.68% / 新版 90.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb028"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb03c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb040"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bb028",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bb034",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005bb03c",
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
      "005bb3d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "005bb3e4",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "005bb3ec",
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

- 旧版 [`005bb028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005baff8.md#insn-005bb028) · [`005bb03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005baff8.md#insn-005bb03c) · [`005bb040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005baff8.md#insn-005bb040)

~~~diff
- 005bb028 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005bb028 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005bb028 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005bb028 bytes a9831ff8
- 005bb03c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 005bb03c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 005bb03c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 005bb03c bytes ea130278
- 005bb040 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 005bb040 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 005bb040 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccfb01cfd71c714b500dc46980689624"></a>

### [`005bb388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb388.md) → [`005bb738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb738.md) FUN_005bb738

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 5件 [`005bb3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb3c4.md) [`005bb738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb738.md) [`005bbf54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bbf54.md) [`005bc278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc278.md) [`005bc558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc558.md)
- 新版 呼出元 1件 [`00b29fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b29/00b29fe4.md) · 呼出先 5件 [`005bb774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb774.md) [`005bbae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bbae8.md) [`005bc304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bc304.md) [`005bc628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bc628.md) [`005bc908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bc908.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005bb754",
      "incomplete_value": true,
      "site": "005bb758",
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


#### 変更候補の命令位置

- 旧版 [`005bb3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb388.md#insn-005bb3a8) · [`005bb398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb388.md#insn-005bb398) · [`005bb3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb388.md#insn-005bb3a0)
- 新版 [`005bb758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb738.md#insn-005bb758) · [`005bb748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb738.md#insn-005bb748) · [`005bb750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb738.md#insn-005bb750)

~~~diff
- 005bb3a8 ["INT_ADD", "register:40f0:8", ["const:5bb3a8:8", "const:4:8"]]
- 005bb3a8 ["CALL", null, ["callee:005bc304:8"]]
+ 005bb758 ["INT_ADD", "register:40f0:8", ["const:5bb758:8", "const:4:8"]]
+ 005bb758 ["CALL", null, ["callee:005bc304:8"]]
- 005bb3a8 bytes eb020094
+ 005bb758 bytes eb020094
- 005bb398 ["INT_ADD", "register:40f0:8", ["const:5bb398:8", "const:4:8"]]
- 005bb398 ["CALL", null, ["callee:005bb774:8"]]
+ 005bb748 ["INT_ADD", "register:40f0:8", ["const:5bb748:8", "const:4:8"]]
+ 005bb748 ["CALL", null, ["callee:005bb774:8"]]
- 005bb398 bytes 0b000094
+ 005bb748 bytes 0b000094
- 005bb3a0 ["INT_ADD", "register:40f0:8", ["const:5bb3a0:8", "const:4:8"]]
- 005bb3a0 ["CALL", null, ["callee:005bbae8:8"]]
+ 005bb750 ["INT_ADD", "register:40f0:8", ["const:5bb750:8", "const:4:8"]]
+ 005bb750 ["CALL", null, ["callee:005bbae8:8"]]
- 005bb3a0 bytes e6000094
+ 005bb750 bytes e6000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d004848c45da83e936213691ef1a4601"></a>

### [`005bb3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb3c4.md) → [`005bb774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb774.md) FUN_005bb774

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005bb388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb388.md) · 呼出先 14件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487bc0.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)
- 新版 呼出元 1件 [`005bb738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb738.md) · 呼出先 14件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487ee0.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.59% / 新版 82.59%

CFGの説明率　旧版 65.57% / 新版 64.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件, `store_value` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb3d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb3d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb3d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bb3d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bb3d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bb3dc",
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
      "005bb784",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005bb788",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005bb78c",
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

- 旧版 [`005bb3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb3c4.md#insn-005bb3d4) · [`005bb3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb3c4.md#insn-005bb3d8) · [`005bb3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb3c4.md#insn-005bb3dc)

~~~diff
- 005bb3d4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005bb3d4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005bb3d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1b0:8"]]
- 005bb3d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bb3d4 bytes f85f1ba9
- 005bb3d8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005bb3d8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005bb3d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1c0:8"]]
- 005bb3d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bb3d8 bytes f6571ca9
- 005bb3dc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005bb3dc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005bb3dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1d0:8"]]
- 005bb3dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bb3dc bytes f44f1da9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7da38cde3dc0992521975e689528bbe"></a>

### [`005bb738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb738.md) → [`005bbae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bbae8.md) FUN_005bbae8

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005bb388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb388.md) · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)
- 新版 呼出元 1件 [`005bb738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb738.md) · 呼出先 13件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 54.03% / 新版 54.03%

CFGの説明率　旧版 23.56% / 新版 23.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 7件, `unresolved_branch_alignment` 33件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 66件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005bbb28",
      "incomplete_value": false,
      "site": "005bbb2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bb778",
      "incomplete_value": false,
      "site": "005bb77c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005bbb44",
      "incomplete_value": true,
      "site": "005bbb54",
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
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:9af:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bb794",
      "incomplete_value": true,
      "site": "005bb7a4",
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
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:8e2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005bbb48",
      "incomplete_value": true,
      "site": "005bbb58",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bb798",
      "incomplete_value": true,
      "site": "005bb7a8",
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
                "const:10:8"
              ]
            ]
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
      "005bbb2c",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "005bbb44",
      "READ",
      [
        "storage",
        "002ad8e2",
        null,
        "string"
      ]
    ],
    [
      "005bbb48",
      "READ",
      [
        "storage",
        "002ad8f2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005bbb2c",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "005bbb44",
      "READ",
      [
        "storage",
        "002ad9af",
        null,
        "string"
      ]
    ],
    [
      "005bbb48",
      "READ",
      [
        "storage",
        "002ad9bf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bb79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb738.md#insn-005bb79c) · [`005bb9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb738.md#insn-005bb9d8) · [`005bb9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb738.md#insn-005bb9e0)
- 新版 [`005bbb4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bbae8.md#insn-005bbb4c)

~~~diff
- 005bb79c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2e0:8"]]
- 005bb79c ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 005bb79c ["COPY", "register:5030:8", ["const:0:8"]]
- 005bb79c ["COPY", "register:5038:8", ["const:0:8"]]
+ 005bbb4c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:330:8"]]
+ 005bbb4c ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 005bbb4c ["COPY", "register:5030:8", ["const:0:8"]]
+ 005bbb4c ["COPY", "register:5038:8", ["const:0:8"]]
- 005bb79c bytes 21b9c03d
+ 005bbb4c bytes 21cdc03d
- 005bb9d8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:1c:8"]]
- 005bb9d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 005bb9d8 bytes 141c00b9
- 005bb9e0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:90:8"]]
- 005bb9e0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 005bb9e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 005bb9e0 bytes 1f4800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dfcbd83af3a6c6862a827eb20fd69a1"></a>

### [`005bbf54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bbf54.md) → [`005bc304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bc304.md) FUN_005bc304

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005bb388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb388.md) · 呼出先 15件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487bc0.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)
- 新版 呼出元 1件 [`005bb738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb738.md) · 呼出先 15件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487ee0.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.16% / 新版 85.16%

CFGの説明率　旧版 33.33% / 新版 32.20%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bbf9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bbfc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bbfc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bbf9c",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005bbf9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bbfb8",
      "READ",
      [
        "storage",
        "002a214a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005bc34c",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "005bc34c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "005bc368",
      "READ",
      [
        "storage",
        "002a2215",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bbf9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bbf54.md#insn-005bbf9c) · [`005bbfc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bbf54.md#insn-005bbfc4) · [`005bbfc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bbf54.md#insn-005bbfc8)

~~~diff
- 005bbf9c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 005bbf9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005bbf9c bytes e90f00f9
- 005bbfc4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005bbfc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 005bbfc4 bytes e00b00f9
- 005bbfc8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005bbfc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 005bbfc8 bytes 0000803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaad41784a083ad93fbc587a53dcabdf"></a>

### [`005bc278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc278.md) → [`005bc628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bc628.md) FUN_005bc628

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005bb388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb388.md) · 呼出先 15件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487bc0.md)
- 新版 呼出元 1件 [`005bb738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb738.md) · 呼出先 15件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.85% / 新版 65.85%

CFGの説明率　旧版 25.45% / 新版 25.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 2件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 23件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bc27c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bc27c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bc280"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bc27c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bc280",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bc284",
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
      "005bc62c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "005bc630",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005bc634",
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

- 旧版 [`005bc27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc278.md#insn-005bc27c) · [`005bc280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc278.md#insn-005bc280) · [`005bc284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc278.md#insn-005bc284)

~~~diff
- 005bc27c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005bc27c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005bc27c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:190:8"]]
- 005bc27c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bc27c bytes fd7b19a9
- 005bc280 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 005bc280 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 005bc280 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 005bc280 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bc280 bytes fc6f1aa9
- 005bc284 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005bc284 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005bc284 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1b0:8"]]
- 005bc284 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bc284 bytes fa671ba9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7545e7c737d3181a91fadd67b55dc6cc"></a>

### [`005bc558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc558.md) → [`005bc908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bc908.md) FUN_005bc908

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005bb388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb388.md) · 呼出先 14件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487bc0.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)
- 新版 呼出元 1件 [`005bb738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb738.md) · 呼出先 14件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487ee0.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.94% / 新版 81.94%

CFGの説明率　旧版 26.53% / 新版 26.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bc56c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bc56c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bc570"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bc56c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bc570",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bc5a8",
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
      "005bc91c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005bc920",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005bc958",
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

- 旧版 [`005bc56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc558.md#insn-005bc56c) · [`005bc570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc558.md#insn-005bc570) · [`005bc5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc558.md#insn-005bc5a8)

~~~diff
- 005bc56c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005bc56c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005bc56c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1c0:8"]]
- 005bc56c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bc56c bytes f6571ca9
- 005bc570 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005bc570 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005bc570 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1d0:8"]]
- 005bc570 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bc570 bytes f44f1da9
- 005bc5a8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 005bc5a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005bc5a8 bytes e81300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07f04dfa93d9a96f432cea9b17551dd8"></a>

### [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) → [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) FUN_005bcbbc

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00af01a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af01a4.md) [`00af075c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af075c.md) · 呼出先 59件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0046dafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046dafc.md) [`0046db14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db14.md)
- 新版 呼出元 2件 [`00af1198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1198.md) [`00af1750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1750.md) · 呼出先 59件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0046de1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de1c.md) [`0046de34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de34.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.36% / 新版 80.36%

CFGの説明率　旧版 39.55% / 新版 39.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 42件, `call_target` 1件, `store_condition` 14件, `store_value` 2件, `unresolved_branch_alignment` 131件, `unresolved_call_alignment` 41件, `unresolved_store_alignment` 159件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bc80c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bc810"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bc810"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bc80c",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bc810",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bc814",
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
      "005bcbbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "005bcbc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "005bcbc4",
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

- 旧版 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md#insn-005bc80c) · [`005bc810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md#insn-005bc810) · [`005bc814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md#insn-005bc814)

~~~diff
- 005bc80c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffff80:8"]]
- 005bc80c ["STORE", null, ["const:1b1:8", "register:8:8", "register:5140:8"]]
- 005bc80c bytes ea0f18fc
- 005bc810 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005bc810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5120:8"]]
- 005bc810 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:8:8"]]
- 005bc810 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5100:8"]]
- 005bc810 bytes e923016d
- 005bc814 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005bc814 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005bc814 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005bc814 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bc814 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9a2cee9fbf417ee25b5de9b95e1f567"></a>

### [`005c0530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0530.md) → [`005c08e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c0/005c08e0.md) FUN_005c08e0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`008c5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c5df8.md) [`008c7b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c7/008c7b94.md) [`00ad6af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6af8.md) [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)
- 新版 呼出元 10件 [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`008c6da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c6/008c6da4.md) [`008c8b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c8/008c8b40.md) [`00ad7aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7aec.md) [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) · 呼出先 3件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c594f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 17.81% / 新版 18.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c0628"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005c09d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005c0554"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c0558",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c093c"
      ]
    ],
    [
      "unmatched:005c0578",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c0918"
      ]
    ],
    [
      "unmatched:005c05b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c09e0"
      ]
    ]
  ],
  "added": [
    [
      "005c0908",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c093c"
      ]
    ],
    [
      "005c0928",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c0918"
      ]
    ],
    [
      "005c0968",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c09e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c0554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0530.md#insn-005c0554) · [`005c0558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0530.md#insn-005c0558) · [`005c0578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0530.md#insn-005c0578)

~~~diff
- 005c0554 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005c0554 ["COPY", "tmp:1:4", ["const:0:4"]]
- 005c0554 ["COPY", "tmp:2:4", ["register:4008:4"]]
- 005c0554 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 005c0554 bytes 36109f5a
- 005c0558 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005c0558 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 005c0558 bytes a80100b4
- 005c0578 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005c0578 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 005c0578 bytes 8bffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07e68d8b87791cf836d073f7872881b0"></a>

### [`005c07b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c07b0.md) → [`005c0b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c0/005c0b60.md) FUN_005c0b60

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) · 呼出先 3件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.91% / 新版 92.91%

CFGの説明率　旧版 50.00% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c07b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c07b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c07b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c07b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c07b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c07b8",
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
      "005c0b60",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "005c0b64",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005c0b68",
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

- 旧版 [`005c07b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c07b0.md#insn-005c07b0) · [`005c07b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c07b0.md#insn-005c07b4) · [`005c07b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c07b0.md#insn-005c07b8)

~~~diff
- 005c07b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c07b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c07b0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 005c07b0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005c07b0 bytes fd7bbaa9
- 005c07b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005c07b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 005c07b4 bytes fb0b00f9
- 005c07b8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005c07b8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005c07b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005c07b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c07b8 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a2fabc84bb54b1405660f574cfde88b"></a>

### [`005c09ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c09ac.md) → [`005c0d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c0/005c0d5c.md) FUN_005c0d5c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) · 呼出先 3件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.30% / 新版 87.30%

CFGの説明率　旧版 15.00% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c0a7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005c0eec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005c09f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005c0d98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005c09fc"
      ]
    ],
    [
      "unmatched:005c09f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c0dcc"
      ]
    ],
    [
      "unmatched:005c0a08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c0da0"
      ]
    ]
  ],
  "added": [
    [
      "005c0d98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c0dac"
      ]
    ],
    [
      "005c0da8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c0dcc"
      ]
    ],
    [
      "005c0db8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c0da0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c09f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c09ac.md#insn-005c09f8) · [`005c0a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c09ac.md#insn-005c0a08) · [`005c0a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c09ac.md#insn-005c0a70)

~~~diff
- 005c09f8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005c09f8 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 005c09f8 bytes 280100b4
- 005c0a08 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005c0a08 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 005c0a08 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 005c0a08 ["CBRANCH", null, ["local:b3:8", "tmp:2:1"]]
- 005c0a08 bytes 4cffff54
- 005c0a70 ["INT_ADD", "register:40f0:8", ["const:5c0a70:8", "const:4:8"]]
- 005c0a70 ["CALL", null, ["callee:0043bf04:8"]]
- 005c0a70 bytes 5decf997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b5a5392ca9d4000e35325007d5a07a1"></a>

### [`005c0ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0ba4.md) → [`005c0f54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c0/005c0f54.md) FUN_005c0f54

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 1件 [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md)
- 新版 呼出元 1件 [`0084f5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084f/0084f5a0.md) · 呼出先 1件 [`005c426c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c426c.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c0bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0ba4.md#insn-005c0bbc)
- 新版 [`005c0f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c0/005c0f54.md#insn-005c0f6c)

~~~diff
- 005c0bbc ["INT_ADD", "register:40f0:8", ["const:5c0bbc:8", "const:4:8"]]
- 005c0bbc ["CALL", null, ["callee:005c426c:8"]]
+ 005c0f6c ["INT_ADD", "register:40f0:8", ["const:5c0f6c:8", "const:4:8"]]
+ 005c0f6c ["CALL", null, ["callee:005c426c:8"]]
- 005c0bbc bytes c00c0094
+ 005c0f6c bytes c00c0094
~~~


<a id="compare-d2867342d192c8a8a7746046acfc1360"></a>

### [`005c0ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0ecc.md) → [`005c127c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c127c.md) FUN_005c127c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ad09c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad09c8.md) · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`005c1390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1390.md) [`00743de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743de8.md)
- 新版 呼出元 1件 [`00ad19bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad19bc.md) · 呼出先 13件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`005c1740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1740.md) [`00744198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744198.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 95.04% / 新版 95.04%

CFGの説明率　旧版 50.45% / 新版 50.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_branch_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c1054"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c1224"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005c1404"
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
      "unmatched:005c1088",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c144c"
      ]
    ],
    [
      "unmatched:005c12a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c173c"
      ]
    ],
    [
      "unmatched:005c1308",
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
      "005c1438",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c144c"
      ]
    ],
    [
      "005c1654",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c173c"
      ]
    ],
    [
      "005c16b8",
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

- 旧版 [`005c0f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0ecc.md#insn-005c0f14) · [`005c1054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0ecc.md#insn-005c1054) · [`005c1058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0ecc.md#insn-005c1058)
- 新版 [`005c12c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c127c.md#insn-005c12c4) · [`005c1408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c127c.md#insn-005c1408)

~~~diff
- 005c0f14 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005c0f14 ["CBRANCH", null, ["local:b64:8", "tmp:0:1"]]
+ 005c12c4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 005c12c4 ["CBRANCH", null, ["local:b68:8", "tmp:0:1"]]
- 005c0f14 bytes 281c00b4
+ 005c12c4 bytes 281c00b4
- 005c1054 ["COPY", "tmp:0:4", ["register:40c0:4"]]
- 005c1054 ["COPY", "tmp:1:8", ["register:40e0:8"]]
- 005c1054 ["INT_ADD", "register:40e0:8", ["register:40e0:8", "const:4:8"]]
- 005c1054 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 005c1054 bytes 984700b8
- 005c1058 ["INT_ADD", "register:40f0:8", ["const:5c1058:8", "const:4:8"]]
- 005c1058 ["CALL", null, ["callee:00c590a0:8"]]
+ 005c1408 ["INT_ADD", "register:40f0:8", ["const:5c1408:8", "const:4:8"]]
+ 005c1408 ["CALL", null, ["callee:00c590a0:8"]]
- 005c1058 bytes 1e5c1a94
+ 005c1408 bytes 265f1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f7fc6c4749de8de212bc2a76c732613"></a>

### [`005c1390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1390.md) → [`005c1740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1740.md) FUN_005c1740

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005c0ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0ecc.md) [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) [`00aec9fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec9fc.md) · 呼出先 8件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`005c127c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c127c.md) [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) [`00aed9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed9f0.md) · 呼出先 8件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.45% / 新版 77.45%

CFGの説明率　旧版 43.80% / 新版 41.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 2件, `store_destination` 1件, `store_value` 1件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c145c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c14b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c14b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c13d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c17bc"
      ]
    ],
    [
      "unmatched:005c13fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c1810"
      ]
    ],
    [
      "005c1820",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005c14a4"
      ]
    ]
  ],
  "added": [
    [
      "005c1780",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c17bc"
      ]
    ],
    [
      "005c17ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c1810"
      ]
    ],
    [
      "005c1820",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "005c1854"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c13e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1390.md#insn-005c13e4) · [`005c145c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1390.md#insn-005c145c) · [`005c14b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1390.md#insn-005c14b0)
- 新版 [`005c1794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1740.md#insn-005c1794)

~~~diff
- 005c13e4 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 005c13e4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 005c1794 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 005c1794 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 005c13e4 bytes 490100b4
+ 005c1794 bytes 490100b4
- 005c145c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 005c145c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005c145c bytes 690a00f9
- 005c14b0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 005c14b0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 005c14b0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 005c14b0 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 005c14b0 bytes 1f7c03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f1b1ad25599500fab078a7cf9f7aa16"></a>

### [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) → [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) FUN_005c1b8c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 155件 [`005bb738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb738.md) [`005bc558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc558.md) [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`005c1820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1820.md) · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 155件 [`005bbae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bbae8.md) [`005bc908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bc908.md) [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`005c1bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1bd0.md) · 呼出先 2件 [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005c1800",
      "incomplete_value": true,
      "site": "005c1808",
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
                "register:40a0:8"
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
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`005c1808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md#insn-005c1808) · [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md#insn-005c17dc) · [`005c17fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md#insn-005c17fc)
- 新版 [`005c1bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md#insn-005c1bb8) · [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md#insn-005c1b8c) · [`005c1bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md#insn-005c1bac)

~~~diff
- 005c1808 ["INT_ADD", "register:40f0:8", ["const:5c1808:8", "const:4:8"]]
- 005c1808 ["CALL", null, ["local:b0:8"]]
+ 005c1bb8 ["INT_ADD", "register:40f0:8", ["const:5c1bb8:8", "const:4:8"]]
+ 005c1bb8 ["CALL", null, ["local:b0:8"]]
- 005c1808 bytes f5ffff97
+ 005c1bb8 bytes f5ffff97
- 005c17dc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 005c17dc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 005c1b8c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 005c1b8c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 005c17dc bytes 010200b4
+ 005c1b8c bytes 010200b4
- 005c17fc ["INT_ADD", "register:40f0:8", ["const:5c17fc:8", "const:4:8"]]
- 005c17fc ["CALL", null, ["local:b0:8"]]
+ 005c1bac ["INT_ADD", "register:40f0:8", ["const:5c1bac:8", "const:4:8"]]
+ 005c1bac ["CALL", null, ["local:b0:8"]]
- 005c17fc bytes f8ffff97
+ 005c1bac bytes f8ffff97
~~~


<a id="compare-ecc1d28709e4edaf84d3a9dc019b93f7"></a>

### [`005c1870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1870.md) → [`005c1c20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1c20.md) FUN_005c1c20

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005bbf54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bbf54.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`005bc304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bc304.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005c1c2c",
      "incomplete_value": false,
      "site": "005c1c30",
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
      "definition_site": "005c187c",
      "incomplete_value": false,
      "site": "005c1880",
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
      "005c1c2c",
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
      "005c1c2c",
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

- 旧版 [`005c1880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1870.md#insn-005c1880) · [`005c1878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1870.md#insn-005c1878) · [`005c187c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1870.md#insn-005c187c)
- 新版 [`005c1c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1c20.md#insn-005c1c30) · [`005c1c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1c20.md#insn-005c1c28) · [`005c1c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1c20.md#insn-005c1c2c)

~~~diff
- 005c1880 ["INT_ADD", "register:40f0:8", ["const:5c1880:8", "const:4:8"]]
- 005c1880 ["CALL", null, ["callee:0043bad8:8"]]
+ 005c1c30 ["INT_ADD", "register:40f0:8", ["const:5c1c30:8", "const:4:8"]]
+ 005c1c30 ["CALL", null, ["callee:0043bad8:8"]]
- 005c1880 bytes cee7f997
+ 005c1c30 bytes aae7f997
- 005c1878 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005c1c28 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 005c1878 bytes a0e7ffd0
+ 005c1c28 bytes a0e7fff0
- 005c187c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 005c187c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005c187c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005c187c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005c1c2c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005c1c2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005c1c2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005c1c2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005c187c bytes 00303e91
+ 005c1c2c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba3895806def426df27e4cd55004bb09"></a>

### [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md) → [`005c1fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1fe0.md) FUN_005c1fe0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 19件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md) [`00675b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00675/00675b88.md) [`00675bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00675/00675bd4.md) [`007342f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00734/007342f8.md) · 呼出先 2件 [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 19件 [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`005c1fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1fe0.md) [`00675f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00675/00675f38.md) [`00675f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00675/00675f84.md) [`007346a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00734/007346a8.md) · 呼出先 2件 [`005c1fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1fe0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md#insn-005c1c30) · [`005c1c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md#insn-005c1c50) · [`005c1c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md#insn-005c1c5c)
- 新版 [`005c1fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1fe0.md#insn-005c1fe0) · [`005c2000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1fe0.md#insn-005c2000) · [`005c200c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1fe0.md#insn-005c200c)

~~~diff
- 005c1c30 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 005c1c30 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 005c1fe0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 005c1fe0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 005c1c30 bytes 010200b4
+ 005c1fe0 bytes 010200b4
- 005c1c50 ["INT_ADD", "register:40f0:8", ["const:5c1c50:8", "const:4:8"]]
- 005c1c50 ["CALL", null, ["local:b0:8"]]
+ 005c2000 ["INT_ADD", "register:40f0:8", ["const:5c2000:8", "const:4:8"]]
+ 005c2000 ["CALL", null, ["local:b0:8"]]
- 005c1c50 bytes f8ffff97
+ 005c2000 bytes f8ffff97
- 005c1c5c ["INT_ADD", "register:40f0:8", ["const:5c1c5c:8", "const:4:8"]]
- 005c1c5c ["CALL", null, ["local:b0:8"]]
+ 005c200c ["INT_ADD", "register:40f0:8", ["const:5c200c:8", "const:4:8"]]
+ 005c200c ["CALL", null, ["local:b0:8"]]
- 005c1c5c bytes f5ffff97
+ 005c200c bytes f5ffff97
~~~


<a id="compare-5a89fb01619232c836fe4435eb8ca3ea"></a>

### [`005c1d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1d1c.md) → [`005c20cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c20cc.md) FUN_005c20cc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`0069a55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md) [`0069f154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069f/0069f154.md) [`006a2ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2ae8.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 8件 [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`0069a90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0069a/0069a90c.md) [`0069f504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0069f/0069f504.md) [`006a2e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a2/006a2e98.md) [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005c20d8",
      "incomplete_value": false,
      "site": "005c20dc",
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
      "definition_site": "005c1d28",
      "incomplete_value": false,
      "site": "005c1d2c",
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
      "005c20d8",
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
      "005c20d8",
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

- 旧版 [`005c1d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1d1c.md#insn-005c1d2c) · [`005c1d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1d1c.md#insn-005c1d24) · [`005c1d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1d1c.md#insn-005c1d28)
- 新版 [`005c20dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c20cc.md#insn-005c20dc) · [`005c20d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c20cc.md#insn-005c20d4) · [`005c20d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c20cc.md#insn-005c20d8)

~~~diff
- 005c1d2c ["INT_ADD", "register:40f0:8", ["const:5c1d2c:8", "const:4:8"]]
- 005c1d2c ["CALL", null, ["callee:0043bad8:8"]]
+ 005c20dc ["INT_ADD", "register:40f0:8", ["const:5c20dc:8", "const:4:8"]]
+ 005c20dc ["CALL", null, ["callee:0043bad8:8"]]
- 005c1d2c bytes a3e6f997
+ 005c20dc bytes 7fe6f997
- 005c1d24 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005c20d4 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 005c1d24 bytes a0e7ffd0
+ 005c20d4 bytes a0e7ffd0
- 005c1d28 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 005c1d28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005c1d28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005c1d28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005c20d8 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005c20d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005c20d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005c20d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005c1d28 bytes 00303e91
+ 005c20d8 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5757c4a548b541d415141ed8935f3d94"></a>

### [`005c1d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1d30.md) → [`005c20e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c20e0.md) FUN_005c20e0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`005c1d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1d30.md) · 呼出先 5件 [`005c1d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1d30.md) [`005c25d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c25d0.md) [`005c26f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c26f4.md) [`005c294c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c294c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`005c20e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c20e0.md) · 呼出先 5件 [`005c20e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c20e0.md) [`005c2980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2980.md) [`005c2aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2aa4.md) [`005c2cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2cfc.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.96% / 新版 84.96%

CFGの説明率　旧版 37.84% / 新版 39.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 9件, `unresolved_branch_alignment` 17件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c1d5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c1d74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c1e58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c1d5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c1d74",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c1da0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c2164"
      ]
    ]
  ],
  "added": [
    [
      "005c210c",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "005c2124",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "005c2150",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c2164"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c1d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1d30.md#insn-005c1d5c) · [`005c1d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1d30.md#insn-005c1d74) · [`005c1da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1d30.md#insn-005c1da0)

~~~diff
- 005c1d5c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 005c1d5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005c1d5c bytes e80700f9
- 005c1d74 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005c1d74 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005c1d74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005c1d74 bytes a8831ff8
- 005c1da0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005c1da0 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 005c1da0 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 005c1da0 ["CBRANCH", null, ["local:b10:8", "tmp:2:1"]]
- 005c1da0 bytes ac000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c10d3dfe78b6a88499366ddf2ad2090b"></a>

### [`005c26f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c26f4.md) → [`005c2aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2aa4.md) FUN_005c2aa4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005c1d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1d30.md) · 呼出先 2件 [`005c25d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c25d0.md) [`005c294c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c294c.md)
- 新版 呼出元 1件 [`005c20e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c20e0.md) · 呼出先 2件 [`005c2980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2980.md) [`005c2cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2cfc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.67% / 新版 90.67%

CFGの説明率　旧版 36.36% / 新版 37.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 7件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c26f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c26f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c26f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c26f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c26f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c26fc",
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
      "005c2aa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005c2aa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005c2aac",
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

- 旧版 [`005c26f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c26f4.md#insn-005c26f4) · [`005c26f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c26f4.md#insn-005c26f8) · [`005c26fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c26f4.md#insn-005c26fc)

~~~diff
- 005c26f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c26f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c26f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 005c26f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005c26f4 bytes fd7bbda9
- 005c26f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005c26f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 005c26f8 bytes f50b00f9
- 005c26fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005c26fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005c26fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005c26fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c26fc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4d455e4f80ae30a1612c86185e2533a"></a>

### [`005c294c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c294c.md) → [`005c2cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2cfc.md) FUN_005c2cfc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`005c1d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1d30.md) [`005c26f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c26f4.md) · 呼出先 1件 [`005c25d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c25d0.md)
- 新版 呼出元 2件 [`005c20e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c20e0.md) [`005c2aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2aa4.md) · 呼出先 1件 [`005c2980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2980.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 20.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c296c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c294c.md#insn-005c296c) · [`005c297c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c294c.md#insn-005c297c) · [`005c29bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c294c.md#insn-005c29bc)
- 新版 [`005c2d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2cfc.md#insn-005c2d1c) · [`005c2d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2cfc.md#insn-005c2d2c) · [`005c2d6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2cfc.md#insn-005c2d6c)

~~~diff
- 005c296c ["INT_ADD", "register:40f0:8", ["const:5c296c:8", "const:4:8"]]
- 005c296c ["CALL", null, ["callee:005c2980:8"]]
+ 005c2d1c ["INT_ADD", "register:40f0:8", ["const:5c2d1c:8", "const:4:8"]]
+ 005c2d1c ["CALL", null, ["callee:005c2980:8"]]
- 005c296c bytes 19ffff97
+ 005c2d1c bytes 19ffff97
- 005c297c ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005c297c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 005c2d2c ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 005c2d2c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 005c297c bytes aa050054
+ 005c2d2c bytes aa050054
- 005c29bc ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005c29bc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 005c2d6c ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 005c2d6c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 005c29bc bytes aa030054
+ 005c2d6c bytes aa030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2e19414a4f9a4a3afbdb5837577c0eb"></a>

### [`005c2a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2a40.md) → [`005c2df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2df0.md) FUN_005c2df0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`005c2a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2a40.md) · 呼出先 2件 [`005c2a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2a40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`005c2df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2df0.md) · 呼出先 2件 [`005c2df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2df0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 20.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c2a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2a40.md#insn-005c2a40) · [`005c2a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2a40.md#insn-005c2a5c) · [`005c2a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2a40.md#insn-005c2a68)
- 新版 [`005c2df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2df0.md#insn-005c2df0) · [`005c2e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2df0.md#insn-005c2e0c) · [`005c2e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2df0.md#insn-005c2e18)

~~~diff
- 005c2a40 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 005c2a40 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 005c2df0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 005c2df0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 005c2a40 bytes 610200b4
+ 005c2df0 bytes 610200b4
- 005c2a5c ["INT_ADD", "register:40f0:8", ["const:5c2a5c:8", "const:4:8"]]
- 005c2a5c ["CALL", null, ["local:b0:8"]]
+ 005c2e0c ["INT_ADD", "register:40f0:8", ["const:5c2e0c:8", "const:4:8"]]
+ 005c2e0c ["CALL", null, ["local:b0:8"]]
- 005c2a5c bytes f9ffff97
+ 005c2e0c bytes f9ffff97
- 005c2a68 ["INT_ADD", "register:40f0:8", ["const:5c2a68:8", "const:4:8"]]
- 005c2a68 ["CALL", null, ["local:b0:8"]]
+ 005c2e18 ["INT_ADD", "register:40f0:8", ["const:5c2e18:8", "const:4:8"]]
+ 005c2e18 ["CALL", null, ["local:b0:8"]]
- 005c2a68 bytes f6ffff97
+ 005c2e18 bytes f6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

