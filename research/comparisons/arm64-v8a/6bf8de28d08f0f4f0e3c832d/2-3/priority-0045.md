# v16.0.2 → v16.0.3 · 最優先の変更候補 (45)

[一覧の目次](README.md)

<a id="compare-117c6a016b1451a12dac98de927ca2ba"></a>

### [`008302e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302e0.md) → [`0083128c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083128c.md) FUN_0083128c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 3件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) [`008302e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302e0.md) [`008478b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008478b8.md) · 呼出先 4件 [`008302e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302e0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0081b818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081b/0081b818.md) [`0083128c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083128c.md) [`00848864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848864.md) · 呼出先 4件 [`0083128c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083128c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 22.22% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008312a0",
      "incomplete_value": true,
      "site": "008312a8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008312c4",
      "incomplete_value": false,
      "site": "008312c8",
      "value": [
        "leaf",
        "const:ffffffffffffffff:8"
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008312c0",
      "incomplete_value": true,
      "site": "008312c8",
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
            "const:8:8"
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


#### 変更候補の命令位置

- 旧版 [`008302fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302e0.md#insn-008302fc) · [`0083031c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302e0.md#insn-0083031c) · [`008302e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302e0.md#insn-008302e0)
- 新版 [`008312a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083128c.md#insn-008312a8) · [`008312c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083128c.md#insn-008312c8) · [`0083128c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083128c.md#insn-0083128c)

~~~diff
- 008302fc ["INT_ADD", "register:40f0:8", ["const:8302fc:8", "const:4:8"]]
- 008302fc ["CALL", null, ["local:b0:8"]]
+ 008312a8 ["INT_ADD", "register:40f0:8", ["const:8312a8:8", "const:4:8"]]
+ 008312a8 ["CALL", null, ["local:b0:8"]]
- 008302fc bytes f9ffff97
+ 008312a8 bytes f9ffff97
- 0083031c ["INT_ADD", "register:40f0:8", ["const:83031c:8", "const:4:8"]]
- 0083031c ["CALL", null, ["callee:00c54d90:8"]]
+ 008312c8 ["INT_ADD", "register:40f0:8", ["const:8312c8:8", "const:4:8"]]
+ 008312c8 ["CALL", null, ["callee:00c54d90:8"]]
- 0083031c bytes a18e1094
+ 008312c8 bytes b28e1094
- 008302e0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 008302e0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 0083128c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 0083128c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 008302e0 bytes 610300b4
+ 0083128c bytes 610300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99a5d97e0e956466870e339428e0caaf"></a>

### [`00830458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830458.md) → [`00831404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831404.md) FUN_00831404

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
      "definition_site": "00831408",
      "incomplete_value": false,
      "site": "0083140c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083045c",
      "incomplete_value": false,
      "site": "00830460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "0083140c",
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
      "0083140c",
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

- 旧版 [`00830458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830458.md#insn-00830458) · [`0083045c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830458.md#insn-0083045c)
- 新版 [`00831404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831404.md#insn-00831404) · [`00831408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831404.md#insn-00831408)

~~~diff
- 00830458 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00831404 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00830458 bytes 682200d0
+ 00831404 bytes 682200d0
- 0083045c ["COPY", "tmp:0:8", ["const:550:8"]]
- 0083045c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083045c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083045c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00831408 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 00831408 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00831408 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00831408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083045c bytes 08411591
+ 00831408 bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c857dda4fec25c753f5fea5fa19bfe38"></a>

### [`00830568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830568.md) → [`00831514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831514.md) FUN_00831514

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) [`00830568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830568.md) [`008478b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008478b8.md) · 呼出先 2件 [`00830568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830568.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0081b818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081b/0081b818.md) [`00831514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831514.md) [`00848864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848864.md) · 呼出先 2件 [`00831514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831514.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830568.md#insn-00830568) · [`00830588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830568.md#insn-00830588) · [`00830594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830568.md#insn-00830594)
- 新版 [`00831514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831514.md#insn-00831514) · [`00831534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831514.md#insn-00831534) · [`00831540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831514.md#insn-00831540)

~~~diff
- 00830568 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00830568 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00831514 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00831514 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00830568 bytes 010200b4
+ 00831514 bytes 010200b4
- 00830588 ["INT_ADD", "register:40f0:8", ["const:830588:8", "const:4:8"]]
- 00830588 ["CALL", null, ["local:b0:8"]]
+ 00831534 ["INT_ADD", "register:40f0:8", ["const:831534:8", "const:4:8"]]
+ 00831534 ["CALL", null, ["local:b0:8"]]
- 00830588 bytes f8ffff97
+ 00831534 bytes f8ffff97
- 00830594 ["INT_ADD", "register:40f0:8", ["const:830594:8", "const:4:8"]]
- 00830594 ["CALL", null, ["local:b0:8"]]
+ 00831540 ["INT_ADD", "register:40f0:8", ["const:831540:8", "const:4:8"]]
+ 00831540 ["CALL", null, ["local:b0:8"]]
- 00830594 bytes f5ffff97
+ 00831540 bytes f5ffff97
~~~


<a id="compare-4270bf6487095e534cac6343146f925f"></a>

### [`0083061c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083061c.md) → [`008315c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008315c8.md) FUN_008315c8

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
      "definition_site": "008315cc",
      "incomplete_value": false,
      "site": "008315d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830620",
      "incomplete_value": false,
      "site": "00830624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "008315d0",
      "DATA",
      [
        "storage",
        "00c7e5a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008315d0",
      "DATA",
      [
        "storage",
        "00c7f570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083061c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083061c.md#insn-0083061c) · [`00830620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083061c.md#insn-00830620)
- 新版 [`008315c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008315c8.md#insn-008315c8) · [`008315cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008315c8.md#insn-008315cc)

~~~diff
- 0083061c ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 008315c8 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0083061c bytes 682200d0
+ 008315c8 bytes 682200d0
- 00830620 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 00830620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00830620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00830620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008315cc ["COPY", "tmp:0:8", ["const:570:8"]]
+ 008315cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008315cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008315cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00830620 bytes 08811691
+ 008315cc bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4ee86cb9b4f6ef259362f01252ab0bf"></a>

### [`0083062c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083062c.md) → [`008315d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008315d8.md) FUN_008315d8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008315e8",
      "incomplete_value": false,
      "site": "008315f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083063c",
      "incomplete_value": false,
      "site": "00830644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "008315f0",
      "DATA",
      [
        "storage",
        "00c7e5a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008315f0",
      "DATA",
      [
        "storage",
        "00c7f570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083062c.md#insn-00830638) · [`0083063c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083062c.md#insn-0083063c) · [`00830648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083062c.md#insn-00830648)
- 新版 [`008315e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008315d8.md#insn-008315e4) · [`008315e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008315d8.md#insn-008315e8) · [`008315f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008315d8.md#insn-008315f4)

~~~diff
- 00830638 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 008315e4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00830638 bytes 682200d0
+ 008315e4 bytes 682200d0
- 0083063c ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 0083063c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083063c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083063c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008315e8 ["COPY", "tmp:0:8", ["const:570:8"]]
+ 008315e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008315e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008315e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083063c bytes 08811691
+ 008315e8 bytes 08c11591
- 00830648 ["INT_ADD", "register:40f0:8", ["const:830648:8", "const:4:8"]]
- 00830648 ["CALL", null, ["callee:00c58f40:8"]]
+ 008315f4 ["INT_ADD", "register:40f0:8", ["const:8315f4:8", "const:4:8"]]
+ 008315f4 ["CALL", null, ["callee:00c58f40:8"]]
- 00830648 bytes 4a9e1094
+ 008315f4 bytes 539e1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-375ac403836c9cde5c703eb5157d0ab1"></a>

### [`008306b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008306b0.md) → [`0083165c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083165c.md) FUN_0083165c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0081c34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c34c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0081d2f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081d/0081d2f8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008306c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008306b0.md#insn-008306c4) · [`008306cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008306b0.md#insn-008306cc) · [`008306d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008306b0.md#insn-008306d4)
- 新版 [`00831670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083165c.md#insn-00831670) · [`00831678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083165c.md#insn-00831678) · [`00831680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083165c.md#insn-00831680)

~~~diff
- 008306c4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 008306c4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00831670 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00831670 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 008306c4 bytes 330100b4
+ 00831670 bytes 330100b4
- 008306cc ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 008306cc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00831678 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00831678 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 008306cc bytes 68000034
+ 00831678 bytes 68000034
- 008306d4 ["INT_ADD", "register:40f0:8", ["const:8306d4:8", "const:4:8"]]
- 008306d4 ["CALL", null, ["callee:0081d2f8:8"]]
+ 00831680 ["INT_ADD", "register:40f0:8", ["const:831680:8", "const:4:8"]]
+ 00831680 ["CALL", null, ["callee:0081d2f8:8"]]
- 008306d4 bytes 1eafff97
+ 00831680 bytes 1eafff97
~~~


<a id="compare-c6520c8f2257c0db62a1691b9c167fd5"></a>

### [`00830850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830850.md) → [`008317fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008317fc.md) FUN_008317fc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 8件 [`0081c95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c95c.md) [`00823068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/00823068.md) [`008238b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/008238b8.md) [`008293ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008293ec.md) [`0082c3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c3dc.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`008300b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008300b8.md) [`00830960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830960.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 8件 [`0081d908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081d/0081d908.md) [`00824014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00824/00824014.md) [`00824864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00824/00824864.md) [`0082a398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082a/0082a398.md) [`0082d388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082d/0082d388.md) · 呼出先 5件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00831064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831064.md) [`0083190c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083190c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830850.md#insn-00830888) · [`00830890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830850.md#insn-00830890) · [`00830898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830850.md#insn-00830898)
- 新版 [`00831834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008317fc.md#insn-00831834) · [`0083183c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008317fc.md#insn-0083183c) · [`00831844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008317fc.md#insn-00831844)

~~~diff
- 00830888 ["INT_ADD", "register:40f0:8", ["const:830888:8", "const:4:8"]]
- 00830888 ["CALL", null, ["callee:0083190c:8"]]
+ 00831834 ["INT_ADD", "register:40f0:8", ["const:831834:8", "const:4:8"]]
+ 00831834 ["CALL", null, ["callee:0083190c:8"]]
- 00830888 bytes 36000094
+ 00831834 bytes 36000094
- 00830890 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00830890 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0083183c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 0083183c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00830890 bytes 740000b4
+ 0083183c bytes 740000b4
- 00830898 ["BRANCH", null, ["local:b6:8"]]
+ 00831844 ["BRANCH", null, ["local:b5:8"]]
- 00830898 bytes 1d000014
+ 00831844 bytes 1d000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebb610424aa0bd6c80be43d0d9ed492e"></a>

### [`00830960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830960.md) → [`0083190c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083190c.md) FUN_0083190c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00830850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830850.md) · 呼出先 0件 
- 新版 呼出元 1件 [`008317fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/008317fc.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 93.33% / 新版 94.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830960.md#insn-00830a90) · [`00830a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830960.md#insn-00830a9c) · [`00830aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830960.md#insn-00830aa0)
- 新版 [`00831a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083190c.md#insn-00831a3c) · [`00831a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083190c.md#insn-00831a48) · [`00831a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/0083190c.md#insn-00831a4c)

~~~diff
- 00830a90 ["CBRANCH", null, ["local:b32:8", "register:101:1"]]
+ 00831a3c ["CBRANCH", null, ["local:b31:8", "register:101:1"]]
- 00830a90 bytes 80000054
+ 00831a3c bytes 80000054
- 00830a9c ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00830a9c ["CBRANCH", null, ["local:b34:8", "tmp:0:1"]]
+ 00831a48 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00831a48 ["CBRANCH", null, ["local:b33:8", "tmp:0:1"]]
- 00830a9c bytes aa000054
+ 00831a48 bytes aa000054
- 00830aa0 ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 00830aa0 ["CBRANCH", null, ["local:b41:8", "tmp:0:1"]]
+ 00831a4c ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
+ 00831a4c ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
- 00830aa0 bytes eb0200b4
+ 00831a4c bytes eb0200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce99e1ecc6e237719aa9d2547d8506ca"></a>

### [`00830b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b08.md) → [`00831ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831ab4.md) FUN_00831ab4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008246d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/008246d4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00825680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00825/00825680.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00831ac0",
      "incomplete_value": false,
      "site": "00831ac4",
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
      "definition_site": "00830b14",
      "incomplete_value": false,
      "site": "00830b18",
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
      "00831ac0",
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
      "00831ac0",
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

- 旧版 [`00830b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b08.md#insn-00830b18) · [`00830b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b08.md#insn-00830b10) · [`00830b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b08.md#insn-00830b14)
- 新版 [`00831ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831ab4.md#insn-00831ac4) · [`00831abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831ab4.md#insn-00831abc) · [`00831ac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831ab4.md#insn-00831ac0)

~~~diff
- 00830b18 ["INT_ADD", "register:40f0:8", ["const:830b18:8", "const:4:8"]]
- 00830b18 ["CALL", null, ["callee:0043bad8:8"]]
+ 00831ac4 ["INT_ADD", "register:40f0:8", ["const:831ac4:8", "const:4:8"]]
+ 00831ac4 ["CALL", null, ["callee:0043bad8:8"]]
- 00830b18 bytes 282bf097
+ 00831ac4 bytes 0528f097
- 00830b10 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00831abc ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00830b10 bytes 20d4fff0
+ 00831abc bytes 20d4fff0
- 00830b14 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00830b14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00830b14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00830b14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00831ac0 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00831ac0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00831ac0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00831ac0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00830b14 bytes 00303e91
+ 00831ac0 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9103ae5030d4a26d6f4f80607c1eeff"></a>

### [`00830bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830bf4.md) → [`00831ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831ba0.md) FUN_00831ba0

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
      "definition_site": "00831bc4",
      "incomplete_value": false,
      "site": "00831bc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830c18",
      "incomplete_value": false,
      "site": "00830c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:688:8"
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
      "00831bc4",
      "DATA",
      [
        "storage",
        "00c7e688",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00831bc4",
      "DATA",
      [
        "storage",
        "00c7f658",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830bf4.md#insn-00830c08) · [`00830c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830bf4.md#insn-00830c10) · [`00830c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830bf4.md#insn-00830c14)
- 新版 [`00831bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831ba0.md#insn-00831bb4) · [`00831bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831ba0.md#insn-00831bbc) · [`00831bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831ba0.md#insn-00831bc0)

~~~diff
- 00830c08 ["INT_ADD", "register:40f0:8", ["const:830c08:8", "const:4:8"]]
- 00830c08 ["CALL", null, ["callee:00c58f30:8"]]
+ 00831bb4 ["INT_ADD", "register:40f0:8", ["const:831bb4:8", "const:4:8"]]
+ 00831bb4 ["CALL", null, ["callee:00c58f30:8"]]
- 00830c08 bytes d69c1094
+ 00831bb4 bytes df9c1094
- 00830c10 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00831bbc ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00830c10 bytes 682200d0
+ 00831bbc bytes 682200d0
- 00830c14 ["COPY", "tmp:0:8", ["const:688:8"]]
- 00830c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00830c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00830c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00831bc0 ["COPY", "tmp:0:8", ["const:658:8"]]
+ 00831bc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00831bc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00831bc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00830c14 bytes 08211a91
+ 00831bc0 bytes 08611991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8408e8e4ac729a9277a880aee97d8b87"></a>

### [`00830cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830cd0.md) → [`00831c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831c7c.md) FUN_00831c7c

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
      "definition_site": "00831c88",
      "incomplete_value": false,
      "site": "00831c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830cdc",
      "incomplete_value": false,
      "site": "00830ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:708:8"
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
      "00831c94",
      "DATA",
      [
        "storage",
        "00c7e708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00831c94",
      "DATA",
      [
        "storage",
        "00c7f6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830cd0.md#insn-00830cd8) · [`00830cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830cd0.md#insn-00830cdc)
- 新版 [`00831c84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831c7c.md#insn-00831c84) · [`00831c88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831c7c.md#insn-00831c88)

~~~diff
- 00830cd8 ["COPY", "register:4050:8", ["const:c7e000:8"]]
+ 00831c84 ["COPY", "register:4050:8", ["const:c7f000:8"]]
- 00830cd8 bytes 6a2200d0
+ 00831c84 bytes 6a2200d0
- 00830cdc ["COPY", "tmp:0:8", ["const:708:8"]]
- 00830cdc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00830cdc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00830cdc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00831c88 ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 00831c88 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00831c88 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00831c88 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00830cdc bytes 4a211c91
+ 00831c88 bytes 4a611b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67b79fe728b66161ee776acc8da5ab60"></a>

### [`00830d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830d14.md) → [`00831cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831cc0.md) FUN_00831cc0

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
      "definition_site": "00831cd8",
      "incomplete_value": false,
      "site": "00831ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830d2c",
      "incomplete_value": false,
      "site": "00830d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:708:8"
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
      "00831ce4",
      "DATA",
      [
        "storage",
        "00c7e708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00831ce4",
      "DATA",
      [
        "storage",
        "00c7f6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830d14.md#insn-00830d28) · [`00830d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830d14.md#insn-00830d2c) · [`00830d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830d14.md#insn-00830d5c)
- 新版 [`00831cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831cc0.md#insn-00831cd4) · [`00831cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831cc0.md#insn-00831cd8) · [`00831d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831cc0.md#insn-00831d08)

~~~diff
- 00830d28 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00831cd4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00830d28 bytes 682200d0
+ 00831cd4 bytes 682200d0
- 00830d2c ["COPY", "tmp:0:8", ["const:708:8"]]
- 00830d2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00830d2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00830d2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00831cd8 ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 00831cd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00831cd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00831cd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00830d2c bytes 08211c91
+ 00831cd8 bytes 08611b91
- 00830d5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00830d5c ["INT_ADD", "register:40f0:8", ["const:830d5c:8", "const:4:8"]]
- 00830d5c ["CALLIND", null, ["register:0:8"]]
+ 00831d08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00831d08 ["INT_ADD", "register:40f0:8", ["const:831d08:8", "const:4:8"]]
+ 00831d08 ["CALLIND", null, ["register:0:8"]]
- 00830d5c bytes 00013fd6
+ 00831d08 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8165472a6cadb39c09c07e5d554cda08"></a>

### [`00830d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830d70.md) → [`00831d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831d1c.md) FUN_00831d1c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00831d48",
      "incomplete_value": false,
      "site": "00831d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830d9c",
      "incomplete_value": false,
      "site": "00830d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:708:8"
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
      "00831d48",
      "DATA",
      [
        "storage",
        "00c7e708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00831d48",
      "DATA",
      [
        "storage",
        "00c7f6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830d70.md#insn-00830d84) · [`00830d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830d70.md#insn-00830d90) · [`00830d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830d70.md#insn-00830d94)
- 新版 [`00831d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831d1c.md#insn-00831d30) · [`00831d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831d1c.md#insn-00831d3c) · [`00831d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831d1c.md#insn-00831d40)

~~~diff
- 00830d84 ["INT_ADD", "register:40f0:8", ["const:830d84:8", "const:4:8"]]
- 00830d84 ["CALL", null, ["callee:00c58f30:8"]]
+ 00831d30 ["INT_ADD", "register:40f0:8", ["const:831d30:8", "const:4:8"]]
+ 00831d30 ["CALL", null, ["callee:00c58f30:8"]]
- 00830d84 bytes 779c1094
+ 00831d30 bytes 809c1094
- 00830d90 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00831d3c ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00830d90 bytes 682200d0
+ 00831d3c bytes 682200d0
- 00830d94 ["COPY", "tmp:0:8", ["const:708:8"]]
- 00830d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00830d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00830d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00831d40 ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 00831d40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00831d40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00831d40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00830d94 bytes 08211c91
+ 00831d40 bytes 08611b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20be997212f71e482c8b107fc53374c7"></a>

### [`00830df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830df8.md) → [`00831da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831da4.md) FUN_00831da4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00831dc0",
      "incomplete_value": false,
      "site": "00831dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830e14",
      "incomplete_value": false,
      "site": "00830e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:708:8"
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
      "00831dc0",
      "DATA",
      [
        "storage",
        "00c7e708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00831dc0",
      "DATA",
      [
        "storage",
        "00c7f6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830df8.md#insn-00830e0c) · [`00830e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830df8.md#insn-00830e10) · [`00830e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830df8.md#insn-00830e34)
- 新版 [`00831db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831da4.md#insn-00831db8) · [`00831dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831da4.md#insn-00831dbc) · [`00831de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831da4.md#insn-00831de0)

~~~diff
- 00830e0c ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 00831db8 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00830e0c bytes 692200d0
+ 00831db8 bytes 692200d0
- 00830e10 ["COPY", "tmp:0:8", ["const:708:8"]]
- 00830e10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00830e10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00830e10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00831dbc ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 00831dbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00831dbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00831dbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00830e10 bytes 29211c91
+ 00831dbc bytes 29611b91
- 00830e34 ["COPY", "register:0:8", ["register:4048:8"]]
- 00830e34 ["INT_ADD", "register:40f0:8", ["const:830e34:8", "const:4:8"]]
- 00830e34 ["CALLIND", null, ["register:0:8"]]
+ 00831de0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00831de0 ["INT_ADD", "register:40f0:8", ["const:831de0:8", "const:4:8"]]
+ 00831de0 ["CALLIND", null, ["register:0:8"]]
- 00830e34 bytes 20013fd6
+ 00831de0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1749ab376cffca5c2f6d91384bf7404e"></a>

### [`00830ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830ef4.md) → [`00831ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831ea0.md) FUN_00831ea0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00acad38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acad38.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`00acbd2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acb/00acbd2c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

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
      "site": "00831ec8",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00830f1c",
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
      "00831ec8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00831ec8",
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

- 旧版 [`00830f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830ef4.md#insn-00830f1c) · [`00830f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830ef4.md#insn-00830f28) · [`00830f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830ef4.md#insn-00830f4c)
- 新版 [`00831ec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831ea0.md#insn-00831ec8) · [`00831ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831ea0.md#insn-00831ed4) · [`00831ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831ea0.md#insn-00831ef8)

~~~diff
- 00830f1c ["INT_ADD", "register:40f0:8", ["const:830f1c:8", "const:4:8"]]
- 00830f1c ["CALL", null, ["ram:47ad34:8"]]
+ 00831ec8 ["INT_ADD", "register:40f0:8", ["const:831ec8:8", "const:4:8"]]
+ 00831ec8 ["CALL", null, ["ram:47b054:8"]]
- 00830f1c bytes 8627f197
+ 00831ec8 bytes 6324f197
- 00830f28 ["INT_ADD", "register:40f0:8", ["const:830f28:8", "const:4:8"]]
- 00830f28 ["CALL", null, ["callee:0047d134:8"]]
+ 00831ed4 ["INT_ADD", "register:40f0:8", ["const:831ed4:8", "const:4:8"]]
+ 00831ed4 ["CALL", null, ["callee:0047d134:8"]]
- 00830f28 bytes bb2ff197
+ 00831ed4 bytes 982cf197
- 00830f4c ["INT_ADD", "register:40f0:8", ["const:830f4c:8", "const:4:8"]]
- 00830f4c ["CALL", null, ["callee:008524fc:8"]]
+ 00831ef8 ["INT_ADD", "register:40f0:8", ["const:831ef8:8", "const:4:8"]]
+ 00831ef8 ["CALL", null, ["callee:008524fc:8"]]
- 00830f4c bytes 81810094
+ 00831ef8 bytes 81810094
~~~


<a id="compare-c83e299e70dbebc74191c9da2edbbcf1"></a>

### [`00830f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830f9c.md) → [`00831f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831f48.md) FUN_00831f48

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
      "definition_site": "00831f54",
      "incomplete_value": false,
      "site": "00831f60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830fa8",
      "incomplete_value": false,
      "site": "00830fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "00831f60",
      "DATA",
      [
        "storage",
        "00c7e788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00831f60",
      "DATA",
      [
        "storage",
        "00c7f758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830f9c.md#insn-00830fa4) · [`00830fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830f9c.md#insn-00830fa8)
- 新版 [`00831f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831f48.md#insn-00831f50) · [`00831f54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831f48.md#insn-00831f54)

~~~diff
- 00830fa4 ["COPY", "register:4050:8", ["const:c7e000:8"]]
+ 00831f50 ["COPY", "register:4050:8", ["const:c7f000:8"]]
- 00830fa4 bytes 6a2200d0
+ 00831f50 bytes 6a2200d0
- 00830fa8 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00830fa8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00830fa8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00830fa8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00831f54 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00831f54 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00831f54 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00831f54 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00830fa8 bytes 4a211e91
+ 00831f54 bytes 4a611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-871248aa481f5a198cb56c04b5f70aa5"></a>

### [`00830fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830fe0.md) → [`00831f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831f8c.md) FUN_00831f8c

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
      "definition_site": "00831fa4",
      "incomplete_value": false,
      "site": "00831fb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830ff8",
      "incomplete_value": false,
      "site": "00831004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "00831fb0",
      "DATA",
      [
        "storage",
        "00c7e788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00831fb0",
      "DATA",
      [
        "storage",
        "00c7f758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830fe0.md#insn-00830ff4) · [`00830ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830fe0.md#insn-00830ff8) · [`00831028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830fe0.md#insn-00831028)
- 新版 [`00831fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831f8c.md#insn-00831fa0) · [`00831fa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831f8c.md#insn-00831fa4) · [`00831fd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831f8c.md#insn-00831fd4)

~~~diff
- 00830ff4 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00831fa0 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00830ff4 bytes 682200d0
+ 00831fa0 bytes 682200d0
- 00830ff8 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00830ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00830ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00830ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00831fa4 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00831fa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00831fa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00831fa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00830ff8 bytes 08211e91
+ 00831fa4 bytes 08611d91
- 00831028 ["COPY", "register:0:8", ["register:4040:8"]]
- 00831028 ["INT_ADD", "register:40f0:8", ["const:831028:8", "const:4:8"]]
- 00831028 ["CALLIND", null, ["register:0:8"]]
+ 00831fd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00831fd4 ["INT_ADD", "register:40f0:8", ["const:831fd4:8", "const:4:8"]]
+ 00831fd4 ["CALLIND", null, ["register:0:8"]]
- 00831028 bytes 00013fd6
+ 00831fd4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66ff1ba05d1d7cdd1c39baf41bbf57c1"></a>

### [`0083103c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083103c.md) → [`00831fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831fe8.md) FUN_00831fe8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00832014",
      "incomplete_value": false,
      "site": "00832014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831068",
      "incomplete_value": false,
      "site": "00831068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "00832014",
      "DATA",
      [
        "storage",
        "00c7e788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00832014",
      "DATA",
      [
        "storage",
        "00c7f758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00831050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083103c.md#insn-00831050) · [`0083105c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083103c.md#insn-0083105c) · [`00831060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083103c.md#insn-00831060)
- 新版 [`00831ffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831fe8.md#insn-00831ffc) · [`00832008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831fe8.md#insn-00832008) · [`0083200c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831fe8.md#insn-0083200c)

~~~diff
- 00831050 ["INT_ADD", "register:40f0:8", ["const:831050:8", "const:4:8"]]
- 00831050 ["CALL", null, ["callee:00c58f30:8"]]
+ 00831ffc ["INT_ADD", "register:40f0:8", ["const:831ffc:8", "const:4:8"]]
+ 00831ffc ["CALL", null, ["callee:00c58f30:8"]]
- 00831050 bytes c49b1094
+ 00831ffc bytes cd9b1094
- 0083105c ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00832008 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0083105c bytes 682200b0
+ 00832008 bytes 682200b0
- 00831060 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00831060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00831060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00831060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083200c ["COPY", "tmp:0:8", ["const:758:8"]]
+ 0083200c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083200c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083200c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00831060 bytes 08211e91
+ 0083200c bytes 08611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-244065f68172aa10fe12c06c06826236"></a>

### [`008310c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008310c4.md) → [`00832070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832070.md) FUN_00832070

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008310e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0083208c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008310e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008310e0",
      "DATA",
      [
        "storage",
        "00c7e788",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008310e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008320b8"
      ]
    ]
  ],
  "added": [
    [
      "0083208c",
      "DATA",
      [
        "storage",
        "00c7f758",
        null,
        "undefined *"
      ]
    ],
    [
      "00832090",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008320b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008310e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008310c4.md#insn-008310e0) · [`008310e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008310c4.md#insn-008310e4)
- 新版 [`0083208c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832070.md#insn-0083208c)

~~~diff
- 008310e0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008310e0 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 008310e0 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 008310e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008310e0 bytes 290401f8
- 008310e4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008310e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008310e4 bytes 480100b4
+ 0083208c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0083208c ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 0083208c ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
+ 0083208c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 0083208c bytes 290401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c8d82fdc670971fa7cfd4cf63ea2c38"></a>

### [`008311c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008311c0.md) → [`0083216c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/0083216c.md) FUN_0083216c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

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
      "site": "00832194",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008311e8",
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
      "00832194",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00832194",
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

- 旧版 [`008311e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008311c0.md#insn-008311e8) · [`008311f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008311c0.md#insn-008311f4)
- 新版 [`00832194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/0083216c.md#insn-00832194) · [`008321a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/0083216c.md#insn-008321a0)

~~~diff
- 008311e8 ["INT_ADD", "register:40f0:8", ["const:8311e8:8", "const:4:8"]]
- 008311e8 ["CALL", null, ["ram:47ad34:8"]]
+ 00832194 ["INT_ADD", "register:40f0:8", ["const:832194:8", "const:4:8"]]
+ 00832194 ["CALL", null, ["ram:47b054:8"]]
- 008311e8 bytes d326f197
+ 00832194 bytes b023f197
- 008311f4 ["INT_ADD", "register:40f0:8", ["const:8311f4:8", "const:4:8"]]
- 008311f4 ["CALL", null, ["callee:0047d134:8"]]
+ 008321a0 ["INT_ADD", "register:40f0:8", ["const:8321a0:8", "const:4:8"]]
+ 008321a0 ["CALL", null, ["callee:0047d134:8"]]
- 008311f4 bytes 082ff197
+ 008321a0 bytes e52bf197
~~~


<a id="compare-57c4f0b0fb5ce6112620707dfeed7ef3"></a>

### [`0083126c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083126c.md) → [`00832218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832218.md) FUN_00832218

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00832224",
      "incomplete_value": false,
      "site": "00832224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831278",
      "incomplete_value": false,
      "site": "00831278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:808:8"
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
      "00832224",
      "DATA",
      [
        "storage",
        "00c7e808",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00832224",
      "DATA",
      [
        "storage",
        "00c7f7d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00831270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083126c.md#insn-00831270) · [`00831274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083126c.md#insn-00831274)
- 新版 [`0083221c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832218.md#insn-0083221c) · [`00832220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832218.md#insn-00832220)

~~~diff
- 00831270 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 0083221c ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00831270 bytes 692200b0
+ 0083221c bytes 692200b0
- 00831274 ["COPY", "tmp:0:8", ["const:808:8"]]
- 00831274 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00831274 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00831274 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00832220 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00832220 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00832220 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00832220 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00831274 bytes 29212091
+ 00832220 bytes 29611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66b0c46cfff8ff130f8b44daea6ec439"></a>

### [`0083134c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083134c.md) → [`008322f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008322f8.md) FUN_008322f8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 20件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0081fe20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081f/0081fe20.md) [`008290d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008290d4.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00820dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00820/00820dcc.md) [`0082a080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082a/0082a080.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.02% / 新版 89.02%

CFGの説明率　旧版 82.93% / 新版 77.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008323d0",
      "incomplete_value": true,
      "site": "008323e0",
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
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:17c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831424",
      "incomplete_value": true,
      "site": "00831434",
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
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:9e:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "008323e4",
      "incomplete_value": true,
      "site": "008323e4",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831438",
      "incomplete_value": true,
      "site": "00831438",
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
                "const:f:8"
              ]
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
    "kind": "store_value",
    "new": {
      "definition_site": "008323d8",
      "incomplete_value": true,
      "site": "008323e8",
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083142c",
      "incomplete_value": true,
      "site": "0083143c",
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00831390",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:00831398",
      "READ",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008313a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008326a0"
      ]
    ]
  ],
  "added": [
    [
      "0083233c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00832344",
      "READ",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0083234c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008326a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00831390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083134c.md#insn-00831390) · [`008313a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083134c.md#insn-008313a0) · [`008314d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083134c.md#insn-008314d8)
- 新版 [`00832484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008322f8.md#insn-00832484)

~~~diff
- 00831390 ["INT_ADD", "register:40f0:8", ["const:831390:8", "const:4:8"]]
- 00831390 ["CALL", null, ["ram:47ad34:8"]]
- 00831390 bytes 6926f197
- 008313a0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008313a0 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 008313a0 bytes a11a0054
- 008314d8 ["INT_ADD", "register:40f0:8", ["const:8314d8:8", "const:4:8"]]
- 008314d8 ["CALL", null, ["ram:47ad34:8"]]
+ 00832484 ["INT_ADD", "register:40f0:8", ["const:832484:8", "const:4:8"]]
+ 00832484 ["CALL", null, ["ram:47b054:8"]]
- 008314d8 bytes 1726f197
+ 00832484 bytes f422f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d5d27b68b62ce3209343c9d00f26cc5"></a>

### [`00831724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831724.md) → [`008326d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008326d0.md) FUN_008326d0

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
      "definition_site": "008326f4",
      "incomplete_value": false,
      "site": "008326f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831748",
      "incomplete_value": false,
      "site": "00831748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "008326f4",
      "DATA",
      [
        "storage",
        "00c7e8f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008326f4",
      "DATA",
      [
        "storage",
        "00c7f8c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00831738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831724.md#insn-00831738) · [`00831740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831724.md#insn-00831740) · [`00831744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831724.md#insn-00831744)
- 新版 [`008326e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008326d0.md#insn-008326e4) · [`008326ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008326d0.md#insn-008326ec) · [`008326f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008326d0.md#insn-008326f0)

~~~diff
- 00831738 ["INT_ADD", "register:40f0:8", ["const:831738:8", "const:4:8"]]
- 00831738 ["CALL", null, ["callee:00c58f30:8"]]
+ 008326e4 ["INT_ADD", "register:40f0:8", ["const:8326e4:8", "const:4:8"]]
+ 008326e4 ["CALL", null, ["callee:00c58f30:8"]]
- 00831738 bytes 0a9a1094
+ 008326e4 bytes 139a1094
- 00831740 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 008326ec ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00831740 bytes 682200b0
+ 008326ec bytes 682200b0
- 00831744 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00831744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00831744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00831744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008326f0 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 008326f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008326f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008326f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00831744 bytes 08e12391
+ 008326f0 bytes 08212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28492376bd786579c13d6f477d03cfcf"></a>

### [`00831758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831758.md) → [`00832704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832704.md) FUN_00832704

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00832710",
      "incomplete_value": false,
      "site": "00832710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831764",
      "incomplete_value": false,
      "site": "00831764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
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
      "00832710",
      "DATA",
      [
        "storage",
        "00c7e8f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00832710",
      "DATA",
      [
        "storage",
        "00c7f8c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083175c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831758.md#insn-0083175c) · [`00831760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831758.md#insn-00831760)
- 新版 [`00832708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832704.md#insn-00832708) · [`0083270c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832704.md#insn-0083270c)

~~~diff
- 0083175c ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 00832708 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0083175c bytes 692200b0
+ 00832708 bytes 692200b0
- 00831760 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00831760 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00831760 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00831760 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083270c ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 0083270c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083270c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083270c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00831760 bytes 29e12391
+ 0083270c bytes 29212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cffff1e1380b4af924cf4dfe74cbd77d"></a>

### [`00831774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831774.md) → [`00832720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832720.md) FUN_00832720

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

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
      "site": "00832744",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00831798",
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
      "00832744",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00832744",
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

- 旧版 [`00831798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831774.md#insn-00831798) · [`008317a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831774.md#insn-008317a4)
- 新版 [`00832744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832720.md#insn-00832744) · [`00832750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832720.md#insn-00832750)

~~~diff
- 00831798 ["INT_ADD", "register:40f0:8", ["const:831798:8", "const:4:8"]]
- 00831798 ["CALL", null, ["ram:47ad34:8"]]
+ 00832744 ["INT_ADD", "register:40f0:8", ["const:832744:8", "const:4:8"]]
+ 00832744 ["CALL", null, ["ram:47b054:8"]]
- 00831798 bytes 6725f197
+ 00832744 bytes 4422f197
- 008317a4 ["INT_ADD", "register:40f0:8", ["const:8317a4:8", "const:4:8"]]
- 008317a4 ["CALL", null, ["callee:0047d134:8"]]
+ 00832750 ["INT_ADD", "register:40f0:8", ["const:832750:8", "const:4:8"]]
+ 00832750 ["CALL", null, ["callee:0047d134:8"]]
- 008317a4 bytes 9c2df197
+ 00832750 bytes 792af197
~~~


<a id="compare-bee52ae021441aaccf1b8b4c49d13ff1"></a>

### [`008317e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317e4.md) → [`00832790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832790.md) FUN_00832790

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008295cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008295cc.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 1件 [`0082a578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082a/0082a578.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "0083279c",
      "incomplete_value": false,
      "site": "008327a0",
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
      "definition_site": "008317f0",
      "incomplete_value": false,
      "site": "008317f4",
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
      "0083279c",
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
      "0083279c",
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

- 旧版 [`008317f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317e4.md#insn-008317f4) · [`008317ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317e4.md#insn-008317ec) · [`008317f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317e4.md#insn-008317f0)
- 新版 [`008327a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832790.md#insn-008327a0) · [`00832798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832790.md#insn-00832798) · [`0083279c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832790.md#insn-0083279c)

~~~diff
- 008317f4 ["INT_ADD", "register:40f0:8", ["const:8317f4:8", "const:4:8"]]
- 008317f4 ["CALL", null, ["callee:00442c90:8"]]
+ 008327a0 ["INT_ADD", "register:40f0:8", ["const:8327a0:8", "const:4:8"]]
+ 008327a0 ["CALL", null, ["callee:00442c90:8"]]
- 008317f4 bytes 5f44f097
+ 008327a0 bytes 3c41f097
- 008317ec ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00832798 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 008317ec bytes 20d4ffd0
+ 00832798 bytes 20d4ffd0
- 008317f0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 008317f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008317f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008317f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0083279c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0083279c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0083279c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0083279c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008317f0 bytes 00303e91
+ 0083279c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54c9412b09568f25c066f37ff2b24831"></a>

### [`008317fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317fc.md) → [`008327a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008327a8.md) FUN_008327a8

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
      "definition_site": "008327cc",
      "incomplete_value": false,
      "site": "008327cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831820",
      "incomplete_value": false,
      "site": "00831820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:988:8"
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
      "008327cc",
      "DATA",
      [
        "storage",
        "00c7e988",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008327cc",
      "DATA",
      [
        "storage",
        "00c7f958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00831810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317fc.md#insn-00831810) · [`00831818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317fc.md#insn-00831818) · [`0083181c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317fc.md#insn-0083181c)
- 新版 [`008327bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008327a8.md#insn-008327bc) · [`008327c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008327a8.md#insn-008327c4) · [`008327c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008327a8.md#insn-008327c8)

~~~diff
- 00831810 ["INT_ADD", "register:40f0:8", ["const:831810:8", "const:4:8"]]
- 00831810 ["CALL", null, ["callee:00c58f30:8"]]
+ 008327bc ["INT_ADD", "register:40f0:8", ["const:8327bc:8", "const:4:8"]]
+ 008327bc ["CALL", null, ["callee:00c58f30:8"]]
- 00831810 bytes d4991094
+ 008327bc bytes dd991094
- 00831818 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 008327c4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00831818 bytes 682200b0
+ 008327c4 bytes 682200b0
- 0083181c ["COPY", "tmp:0:8", ["const:988:8"]]
- 0083181c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083181c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083181c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008327c8 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 008327c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008327c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008327c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083181c bytes 08212691
+ 008327c8 bytes 08612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-751ad93b8df61f9115203a7b8fcd5dae"></a>

### [`00831830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831830.md) → [`008327dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008327dc.md) FUN_008327dc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008327e8",
      "incomplete_value": false,
      "site": "008327e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083183c",
      "incomplete_value": false,
      "site": "0083183c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:988:8"
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
      "008327e8",
      "DATA",
      [
        "storage",
        "00c7e988",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008327e8",
      "DATA",
      [
        "storage",
        "00c7f958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00831834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831830.md#insn-00831834) · [`00831838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831830.md#insn-00831838)
- 新版 [`008327e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008327dc.md#insn-008327e0) · [`008327e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008327dc.md#insn-008327e4)

~~~diff
- 00831834 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 008327e0 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00831834 bytes 692200b0
+ 008327e0 bytes 692200b0
- 00831838 ["COPY", "tmp:0:8", ["const:988:8"]]
- 00831838 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00831838 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00831838 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008327e4 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 008327e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008327e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008327e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00831838 bytes 29212691
+ 008327e4 bytes 29612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fd3c85fc4ae54e78b363ea217c8d3b6"></a>

### [`0083184c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083184c.md) → [`008327f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008327f8.md) FUN_008327f8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00826e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00826/00826e14.md) [`00827718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00827/00827718.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`00827dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00827/00827dc0.md) [`008286c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00828/008286c4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 93.42% / 新版 91.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00831aa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00832a50"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00832830",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00831884",
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
      "00832830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00832984",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00827970"
      ]
    ],
    [
      "008329dc",
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
      "00832830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00832984",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0082891c"
      ]
    ],
    [
      "008329dc",
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

- 旧版 [`00831884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083184c.md#insn-00831884) · [`00831a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083184c.md#insn-00831a34) · [`00831aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083184c.md#insn-00831aa4)
- 新版 [`00832830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008327f8.md#insn-00832830) · [`008329e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008327f8.md#insn-008329e0)

~~~diff
- 00831884 ["INT_ADD", "register:40f0:8", ["const:831884:8", "const:4:8"]]
- 00831884 ["CALL", null, ["ram:47ad34:8"]]
+ 00832830 ["INT_ADD", "register:40f0:8", ["const:832830:8", "const:4:8"]]
+ 00832830 ["CALL", null, ["ram:47b054:8"]]
- 00831884 bytes 2c25f197
+ 00832830 bytes 0922f197
- 00831a34 ["INT_ADD", "register:40f0:8", ["const:831a34:8", "const:4:8"]]
- 00831a34 ["CALL", null, ["callee:00442c90:8"]]
+ 008329e0 ["INT_ADD", "register:40f0:8", ["const:8329e0:8", "const:4:8"]]
+ 008329e0 ["CALL", null, ["callee:00442c90:8"]]
- 00831a34 bytes cf43f097
+ 008329e0 bytes ac40f097
- 00831aa4 ["CBRANCH", null, ["local:b44:8", "register:101:1"]]
- 00831aa4 bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e81c545266647556110bfab2edc8c578"></a>

### [`00831d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d78.md) → [`00832d24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832d24.md) FUN_00832d24

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
      "definition_site": "00832d28",
      "incomplete_value": false,
      "site": "00832d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831d7c",
      "incomplete_value": false,
      "site": "00831d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
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
      "00832d2c",
      "DATA",
      [
        "storage",
        "00c7ea08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00832d2c",
      "DATA",
      [
        "storage",
        "00c7f9d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00831d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d78.md#insn-00831d78) · [`00831d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d78.md#insn-00831d7c)
- 新版 [`00832d24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832d24.md#insn-00832d24) · [`00832d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832d24.md#insn-00832d28)

~~~diff
- 00831d78 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00832d24 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00831d78 bytes 682200b0
+ 00832d24 bytes 682200b0
- 00831d7c ["COPY", "tmp:0:8", ["const:a08:8"]]
- 00831d7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00831d7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00831d7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00832d28 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 00832d28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00832d28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00832d28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00831d7c bytes 08212891
+ 00832d28 bytes 08612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f3d04e706cd149560da722d804cc82b"></a>

### [`00831d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d98.md) → [`00832d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832d44.md) FUN_00832d44

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0082c8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c8bc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0082d868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082d/0082d868.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 77.78% / 新版 87.50%

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
      "site": "00832d6c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00831dc0",
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
      "site": "00832d78",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00831dcc",
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
      "00832d6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00832d78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00832d6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00832d78",
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

- 旧版 [`00831dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d98.md#insn-00831dc0) · [`00831dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d98.md#insn-00831dcc) · [`00831dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d98.md#insn-00831dbc)
- 新版 [`00832d6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832d44.md#insn-00832d6c) · [`00832d78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832d44.md#insn-00832d78) · [`00832d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832d44.md#insn-00832d68)

~~~diff
- 00831dc0 ["INT_ADD", "register:40f0:8", ["const:831dc0:8", "const:4:8"]]
- 00831dc0 ["CALL", null, ["ram:47ad34:8"]]
+ 00832d6c ["INT_ADD", "register:40f0:8", ["const:832d6c:8", "const:4:8"]]
+ 00832d6c ["CALL", null, ["ram:47b054:8"]]
- 00831dc0 bytes dd23f197
+ 00832d6c bytes ba20f197
- 00831dcc ["INT_ADD", "register:40f0:8", ["const:831dcc:8", "const:4:8"]]
- 00831dcc ["CALL", null, ["ram:47ad34:8"]]
+ 00832d78 ["INT_ADD", "register:40f0:8", ["const:832d78:8", "const:4:8"]]
+ 00832d78 ["CALL", null, ["ram:47b054:8"]]
- 00831dcc bytes da23f197
+ 00832d78 bytes b720f197
- 00831dbc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00831dbc ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00832d68 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00832d68 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00831dbc bytes a8070035
+ 00832d68 bytes a8070035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9ba5f09915e87a53184f0a2770cc2cd"></a>

### [`00831f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f20.md) → [`00832ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832ecc.md) FUN_00832ecc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00832ed8",
      "incomplete_value": false,
      "site": "00832ed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831f2c",
      "incomplete_value": false,
      "site": "00831f2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
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
      "00832ed8",
      "DATA",
      [
        "storage",
        "00c7ea88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00832ed8",
      "DATA",
      [
        "storage",
        "00c7fa58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00831f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f20.md#insn-00831f24) · [`00831f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f20.md#insn-00831f28)
- 新版 [`00832ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832ecc.md#insn-00832ed0) · [`00832ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832ecc.md#insn-00832ed4)

~~~diff
- 00831f24 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 00832ed0 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00831f24 bytes 692200b0
+ 00832ed0 bytes 692200b0
- 00831f28 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00831f28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00831f28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00831f28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00832ed4 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 00832ed4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00832ed4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00832ed4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00831f28 bytes 29212a91
+ 00832ed4 bytes 29612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beb7f57ebd632ad6cd19c4fdf69d6f86"></a>

### [`00831f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f3c.md) → [`00832ee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832ee8.md) FUN_00832ee8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0082c8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c8bc.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`00a4692c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a4692c.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0082d868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082d/0082d868.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md) [`00a47920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47920.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 70.00% / 新版 87.50%

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
      "site": "00832f0c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00831f60",
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
      "site": "00832f18",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00831f6c",
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
      "definition_site": "00832f34",
      "incomplete_value": true,
      "site": "00832f44",
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
      "00832f0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00832f18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00832f0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00832f18",
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

- 旧版 [`00831f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f3c.md#insn-00831f60) · [`00831f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f3c.md#insn-00831f6c) · [`00831f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f3c.md#insn-00831f98)
- 新版 [`00832f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832ee8.md#insn-00832f0c) · [`00832f18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832ee8.md#insn-00832f18) · [`00832f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832ee8.md#insn-00832f44)

~~~diff
- 00831f60 ["INT_ADD", "register:40f0:8", ["const:831f60:8", "const:4:8"]]
- 00831f60 ["CALL", null, ["ram:47ad34:8"]]
+ 00832f0c ["INT_ADD", "register:40f0:8", ["const:832f0c:8", "const:4:8"]]
+ 00832f0c ["CALL", null, ["ram:47b054:8"]]
- 00831f60 bytes 7523f197
+ 00832f0c bytes 5220f197
- 00831f6c ["INT_ADD", "register:40f0:8", ["const:831f6c:8", "const:4:8"]]
- 00831f6c ["CALL", null, ["ram:47ad34:8"]]
+ 00832f18 ["INT_ADD", "register:40f0:8", ["const:832f18:8", "const:4:8"]]
+ 00832f18 ["CALL", null, ["ram:47b054:8"]]
- 00831f6c bytes 7223f197
+ 00832f18 bytes 4f20f197
- 00831f98 ["INT_ADD", "register:40f0:8", ["const:831f98:8", "const:4:8"]]
- 00831f98 ["CALL", null, ["callee:008b7ea8:8"]]
+ 00832f44 ["INT_ADD", "register:40f0:8", ["const:832f44:8", "const:4:8"]]
+ 00832f44 ["CALL", null, ["callee:008b7ea8:8"]]
- 00831f98 bytes d9130294
+ 00832f44 bytes d9130294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e05d6da38ef16799edffe00472e3b899"></a>

### [`00831ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831ffc.md) → [`00832fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832fa8.md) FUN_00832fa8

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
      "definition_site": "00832fcc",
      "incomplete_value": false,
      "site": "00832fcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00832020",
      "incomplete_value": false,
      "site": "00832020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "00832fcc",
      "DATA",
      [
        "storage",
        "00c7eb08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00832fcc",
      "DATA",
      [
        "storage",
        "00c7fad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00832010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831ffc.md#insn-00832010) · [`00832018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831ffc.md#insn-00832018) · [`0083201c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831ffc.md#insn-0083201c)
- 新版 [`00832fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832fa8.md#insn-00832fbc) · [`00832fc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832fa8.md#insn-00832fc4) · [`00832fc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832fa8.md#insn-00832fc8)

~~~diff
- 00832010 ["INT_ADD", "register:40f0:8", ["const:832010:8", "const:4:8"]]
- 00832010 ["CALL", null, ["callee:00c58f30:8"]]
+ 00832fbc ["INT_ADD", "register:40f0:8", ["const:832fbc:8", "const:4:8"]]
+ 00832fbc ["CALL", null, ["callee:00c58f30:8"]]
- 00832010 bytes d4971094
+ 00832fbc bytes dd971094
- 00832018 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00832fc4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00832018 bytes 68220090
+ 00832fc4 bytes 682200b0
- 0083201c ["COPY", "tmp:0:8", ["const:b08:8"]]
- 0083201c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083201c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083201c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00832fc8 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 00832fc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00832fc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00832fc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083201c bytes 08212c91
+ 00832fc8 bytes 08612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e276bec1c887d2f02f4896a2b34e798"></a>

### [`00832030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/00832030.md) → [`00832fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832fdc.md) FUN_00832fdc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00832fe8",
      "incomplete_value": false,
      "site": "00832fe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083203c",
      "incomplete_value": false,
      "site": "0083203c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "00832fe8",
      "DATA",
      [
        "storage",
        "00c7eb08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00832fe8",
      "DATA",
      [
        "storage",
        "00c7fad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00832034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/00832030.md#insn-00832034) · [`00832038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/00832030.md#insn-00832038)
- 新版 [`00832fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832fdc.md#insn-00832fe0) · [`00832fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832fdc.md#insn-00832fe4)

~~~diff
- 00832034 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 00832fe0 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00832034 bytes 69220090
+ 00832fe0 bytes 692200b0
- 00832038 ["COPY", "tmp:0:8", ["const:b08:8"]]
- 00832038 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00832038 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00832038 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00832fe4 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 00832fe4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00832fe4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00832fe4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00832038 bytes 29212c91
+ 00832fe4 bytes 29612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3b6acaadfb85ac3ab576008759e915d"></a>

### [`0083204c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083204c.md) → [`00832ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832ff8.md) FUN_00832ff8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0082d2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d2e8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0082e294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082e/0082e294.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

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
      "site": "00833018",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0083206c",
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
      "site": "00833024",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00832078",
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
      "00833018",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00833024",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00833048",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "00833018",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00833024",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00833048",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083206c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083204c.md#insn-0083206c) · [`00832078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083204c.md#insn-00832078) · [`0083208c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083204c.md#insn-0083208c)
- 新版 [`00833018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832ff8.md#insn-00833018) · [`00833024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832ff8.md#insn-00833024) · [`00833038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832ff8.md#insn-00833038)

~~~diff
- 0083206c ["INT_ADD", "register:40f0:8", ["const:83206c:8", "const:4:8"]]
- 0083206c ["CALL", null, ["ram:47ad34:8"]]
+ 00833018 ["INT_ADD", "register:40f0:8", ["const:833018:8", "const:4:8"]]
+ 00833018 ["CALL", null, ["ram:47b054:8"]]
- 0083206c bytes 3223f197
+ 00833018 bytes 0f20f197
- 00832078 ["INT_ADD", "register:40f0:8", ["const:832078:8", "const:4:8"]]
- 00832078 ["CALL", null, ["ram:47ad34:8"]]
+ 00833024 ["INT_ADD", "register:40f0:8", ["const:833024:8", "const:4:8"]]
+ 00833024 ["CALL", null, ["ram:47b054:8"]]
- 00832078 bytes 2f23f197
+ 00833024 bytes 0c20f197
- 0083208c ["INT_ADD", "register:40f0:8", ["const:83208c:8", "const:4:8"]]
- 0083208c ["CALL", null, ["callee:008524fc:8"]]
+ 00833038 ["INT_ADD", "register:40f0:8", ["const:833038:8", "const:4:8"]]
+ 00833038 ["CALL", null, ["callee:008524fc:8"]]
- 0083208c bytes 317d0094
+ 00833038 bytes 317d0094
~~~


<a id="compare-fbeef373520c5f48cebc0ae0e4fb4a0a"></a>

### [`008320dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/008320dc.md) → [`00833088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/00833088.md) FUN_00833088

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
      "definition_site": "008330ac",
      "incomplete_value": false,
      "site": "008330ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00832100",
      "incomplete_value": false,
      "site": "00832100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "008330ac",
      "DATA",
      [
        "storage",
        "00c7eb88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008330ac",
      "DATA",
      [
        "storage",
        "00c7fb58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008320f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/008320dc.md#insn-008320f0) · [`008320f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/008320dc.md#insn-008320f8) · [`008320fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/008320dc.md#insn-008320fc)
- 新版 [`0083309c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/00833088.md#insn-0083309c) · [`008330a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/00833088.md#insn-008330a4) · [`008330a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/00833088.md#insn-008330a8)

~~~diff
- 008320f0 ["INT_ADD", "register:40f0:8", ["const:8320f0:8", "const:4:8"]]
- 008320f0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0083309c ["INT_ADD", "register:40f0:8", ["const:83309c:8", "const:4:8"]]
+ 0083309c ["CALL", null, ["callee:00c58f30:8"]]
- 008320f0 bytes 9c971094
+ 0083309c bytes a5971094
- 008320f8 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 008330a4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 008320f8 bytes 68220090
+ 008330a4 bytes 68220090
- 008320fc ["COPY", "tmp:0:8", ["const:b88:8"]]
- 008320fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008320fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008320fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008330a8 ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 008330a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008330a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008330a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008320fc bytes 08212e91
+ 008330a8 bytes 08612d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e93e2fb9f4b21839a9019d26551ce493"></a>

### [`0083212c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083212c.md) → [`008330d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/008330d8.md) FUN_008330d8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 41件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md)
- 新版 呼出元 0件  · 呼出先 41件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0046de54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de54.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.49% / 新版 88.49%

CFGの説明率　旧版 72.44% / 新版 66.99%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 4件, `store_value` 2件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 31件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083212c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083212c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00832130"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083212c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00832130",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00832134",
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
      "008330d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008330dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008330e0",
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

- 旧版 [`0083212c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083212c.md#insn-0083212c) · [`00832130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083212c.md#insn-00832130) · [`00832134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083212c.md#insn-00832134)

~~~diff
- 0083212c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0083212c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0083212c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 0083212c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0083212c bytes fd7bbaa9
- 00832130 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00832130 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00832130 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00832130 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00832130 bytes fc6f01a9
- 00832134 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00832134 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00832134 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00832134 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00832134 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8f0b72d335a06d735569b65eb5eeae0"></a>

### [`0083336c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083336c.md) → [`00834318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/00834318.md) FUN_00834318

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0083212c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083212c.md) [`0083336c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083336c.md) [`0083371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083371c.md) · 呼出先 5件 [`0081d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081d560.md) [`0083336c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083336c.md) [`0083371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083371c.md) [`00833a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/00833a94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 3件 [`008330d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/008330d8.md) [`00834318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/00834318.md) [`008346c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/008346c8.md) · 呼出先 5件 [`0081e50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081e/0081e50c.md) [`00834318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/00834318.md) [`008346c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/008346c8.md) [`00834a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/00834a40.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.59% / 新版 85.59%

CFGの説明率　旧版 28.40% / 新版 30.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00833708"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00833708"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008346b4"
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
      "unmatched:008333d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081d560"
      ]
    ],
    [
      "unmatched:008333e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081d560"
      ]
    ],
    [
      "unmatched:0083346c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081d560"
      ]
    ]
  ],
  "added": [
    [
      "00834380",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081e50c"
      ]
    ],
    [
      "00834394",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081e50c"
      ]
    ],
    [
      "00834418",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081e50c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008333d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083336c.md#insn-008333d4) · [`008333e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083336c.md#insn-008333e8) · [`0083346c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083336c.md#insn-0083346c)

~~~diff
- 008333d4 ["INT_ADD", "register:40f0:8", ["const:8333d4:8", "const:4:8"]]
- 008333d4 ["CALL", null, ["ram:81d560:8"]]
- 008333d4 bytes 63a8ff97
- 008333e8 ["INT_ADD", "register:40f0:8", ["const:8333e8:8", "const:4:8"]]
- 008333e8 ["CALL", null, ["ram:81d560:8"]]
- 008333e8 bytes 5ea8ff97
- 0083346c ["INT_ADD", "register:40f0:8", ["const:83346c:8", "const:4:8"]]
- 0083346c ["CALL", null, ["ram:81d560:8"]]
- 0083346c bytes 3da8ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-398d23014e60717f684ca42a918672b0"></a>

### [`0083371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083371c.md) → [`008346c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/008346c8.md) FUN_008346c8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083336c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083336c.md) · 呼出先 3件 [`0081d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081d560.md) [`0083336c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083336c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`00834318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/00834318.md) · 呼出先 3件 [`0081e50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081e/0081e50c.md) [`00834318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/00834318.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.34% / 新版 92.34%

CFGの説明率　旧版 79.69% / 新版 73.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00833970"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0083491c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00833974"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00834724",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081d560"
      ]
    ],
    [
      "00834738",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081d560"
      ]
    ],
    [
      "unmatched:00833830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081d560"
      ]
    ]
  ],
  "added": [
    [
      "00834724",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081e50c"
      ]
    ],
    [
      "00834738",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081e50c"
      ]
    ],
    [
      "008347dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081e50c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00833778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083371c.md#insn-00833778) · [`0083378c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083371c.md#insn-0083378c) · [`00833830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083371c.md#insn-00833830)
- 新版 [`00834724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/008346c8.md#insn-00834724) · [`00834738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/008346c8.md#insn-00834738)

~~~diff
- 00833778 ["INT_ADD", "register:40f0:8", ["const:833778:8", "const:4:8"]]
- 00833778 ["CALL", null, ["ram:81d560:8"]]
+ 00834724 ["INT_ADD", "register:40f0:8", ["const:834724:8", "const:4:8"]]
+ 00834724 ["CALL", null, ["ram:81e50c:8"]]
- 00833778 bytes 7aa7ff97
+ 00834724 bytes 7aa7ff97
- 0083378c ["INT_ADD", "register:40f0:8", ["const:83378c:8", "const:4:8"]]
- 0083378c ["CALL", null, ["ram:81d560:8"]]
+ 00834738 ["INT_ADD", "register:40f0:8", ["const:834738:8", "const:4:8"]]
+ 00834738 ["CALL", null, ["ram:81e50c:8"]]
- 0083378c bytes 75a7ff97
+ 00834738 bytes 75a7ff97
- 00833830 ["INT_ADD", "register:40f0:8", ["const:833830:8", "const:4:8"]]
- 00833830 ["CALL", null, ["ram:81d560:8"]]
- 00833830 bytes 4ca7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a704e30803c11cd869fd98704ae4b567"></a>

### [`00833a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/00833a94.md) → [`00834a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/00834a40.md) FUN_00834a40

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0083336c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083336c.md) [`00833a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/00833a94.md) · 呼出先 4件 [`0081d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081d560.md) [`00833a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/00833a94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 2件 [`00834318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/00834318.md) [`00834a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/00834a40.md) · 呼出先 4件 [`0081e50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081e/0081e50c.md) [`00834a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/00834a40.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.77% / 新版 86.77%

CFGの説明率　旧版 46.67% / 新版 52.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 4件, `store_condition` 2件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00833aa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00833aa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00833aa8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00833aa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00833aa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00833aac",
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
      "00834a50",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00834a54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00834a58",
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

- 旧版 [`00833aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/00833a94.md#insn-00833aa4) · [`00833aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/00833a94.md#insn-00833aa8) · [`00833aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/00833a94.md#insn-00833aac)

~~~diff
- 00833aa4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00833aa4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00833aa4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00833aa4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00833aa4 bytes f85f07a9
- 00833aa8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00833aa8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00833aa8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00833aa8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00833aa8 bytes f65708a9
- 00833aac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00833aac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00833aac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00833aac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00833aac bytes f44f09a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-effa14238c9163ecb609af131472f733"></a>

### [`008341a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/008341a0.md) → [`0083514c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/0083514c.md) FUN_0083514c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0083212c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083212c.md) [`008341a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/008341a0.md) [`00834668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834668.md) · 呼出先 3件 [`008341a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/008341a0.md) [`00834668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834668.md) [`00834990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834990.md)
- 新版 呼出元 3件 [`008330d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/008330d8.md) [`0083514c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/0083514c.md) [`00835614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/00835614.md) · 呼出先 3件 [`0083514c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/0083514c.md) [`00835614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/00835614.md) [`0083593c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/0083593c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.07% / 新版 80.07%

CFGの説明率　旧版 44.76% / 新版 41.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 9件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008345e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008345e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008345ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00834228",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00835360"
      ]
    ],
    [
      "unmatched:00834284",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00834288",
      "READ",
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
      "008351d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00835360"
      ]
    ],
    [
      "00835230",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00835234",
      "READ",
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

- 旧版 [`00834228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/008341a0.md#insn-00834228) · [`00834490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/008341a0.md#insn-00834490) · [`008344d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/008341a0.md#insn-008344d4)

~~~diff
- 00834228 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00834228 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00834228 ["CBRANCH", null, ["local:b37:8", "tmp:1:1"]]
- 00834228 bytes 6d0c0054
- 00834490 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00834490 ["CBRANCH", null, ["local:b65:8", "tmp:0:1"]]
- 00834490 bytes 230d0054
- 008344d4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 008344d4 ["COPY", "tmp:1:1", ["tmp:0:1"]]
- 008344d4 ["COPY", "tmp:2:1", ["const:2:1"]]
- 008344d4 ["INT_AND", "tmp:3:1", ["tmp:2:1", "const:8:1"]]
- 008344d4 bytes 42314cfa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1879555916de497413343184b5ccc2ec"></a>

### [`0083515c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083515c.md) → [`00836108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836108.md) FUN_00836108

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00836114",
      "incomplete_value": false,
      "site": "00836118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835168",
      "incomplete_value": false,
      "site": "0083516c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
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
      "00836118",
      "DATA",
      [
        "storage",
        "00c7ebf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00836118",
      "DATA",
      [
        "storage",
        "00c7fbc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00835164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083515c.md#insn-00835164) · [`00835168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083515c.md#insn-00835168)
- 新版 [`00836110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836108.md#insn-00836110) · [`00836114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836108.md#insn-00836114)

~~~diff
- 00835164 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 00836110 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00835164 bytes 492200b0
+ 00836110 bytes 492200b0
- 00835168 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00835168 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00835168 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00835168 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00836114 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 00836114 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00836114 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00836114 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00835168 bytes 29e12f91
+ 00836114 bytes 29212f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d523a94bd658f4e22785acc92001dcb9"></a>

### [`00835180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835180.md) → [`0083612c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/0083612c.md) FUN_0083612c

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
      "definition_site": "00836134",
      "incomplete_value": false,
      "site": "00836138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835188",
      "incomplete_value": false,
      "site": "0083518c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
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
      "00836138",
      "DATA",
      [
        "storage",
        "00c7ebf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00836138",
      "DATA",
      [
        "storage",
        "00c7fbc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00835184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835180.md#insn-00835184) · [`00835188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835180.md#insn-00835188) · [`008351ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835180.md#insn-008351ac)
- 新版 [`00836130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/0083612c.md#insn-00836130) · [`00836134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/0083612c.md#insn-00836134) · [`00836158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/0083612c.md#insn-00836158)

~~~diff
- 00835184 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 00836130 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00835184 bytes 492200b0
+ 00836130 bytes 492200b0
- 00835188 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00835188 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00835188 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00835188 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00836134 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 00836134 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00836134 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00836134 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00835188 bytes 29e12f91
+ 00836134 bytes 29212f91
- 008351ac ["INT_ADD", "register:40f0:8", ["const:8351ac:8", "const:4:8"]]
- 008351ac ["CALL", null, ["callee:00c58f50:8"]]
+ 00836158 ["INT_ADD", "register:40f0:8", ["const:836158:8", "const:4:8"]]
+ 00836158 ["CALL", null, ["callee:00c58f50:8"]]
- 008351ac bytes 758b1094
+ 00836158 bytes 7e8b1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8721d9df2ecace845a013e9ef9d5738c"></a>

### [`008351c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008351c0.md) → [`0083616c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/0083616c.md) FUN_0083616c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00835138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/00835138.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008351f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008351f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008351f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008351f4",
      "DATA",
      [
        "storage",
        "00c7ebf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008361a0",
      "DATA",
      [
        "storage",
        "00c7fbc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008351dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008351c0.md#insn-008351dc) · [`008351f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008351c0.md#insn-008351f0) · [`008351f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008351c0.md#insn-008351f4)
- 新版 [`00836188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/0083616c.md#insn-00836188)

~~~diff
- 008351dc ["INT_ADD", "register:40f0:8", ["const:8351dc:8", "const:4:8"]]
- 008351dc ["CALL", null, ["callee:00c58f30:8"]]
+ 00836188 ["INT_ADD", "register:40f0:8", ["const:836188:8", "const:4:8"]]
+ 00836188 ["CALL", null, ["callee:00c58f30:8"]]
- 008351dc bytes 618b1094
+ 00836188 bytes 6a8b1094
- 008351f0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 008351f0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 008351f0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 008351f0 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 008351f0 bytes 1ffc01a9
- 008351f4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008351f4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008351f4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008351f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008351f4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68b65ea3de392a629b338d5cc8aa3c27"></a>

### [`008353c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008353c8.md) → [`00836374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836374.md) FUN_00836374

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083212c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083212c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008330d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/008330d8.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 4件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008353cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00836378"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "008353cc"
      ],
      [
        "FALL_THROUGH",
        "00836378"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00836378",
      "incomplete_value": true,
      "site": "0083637c",
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
      "definition_site": "008353cc",
      "incomplete_value": true,
      "site": "008353d0",
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
      "unmatched:008353cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008363a4"
      ]
    ]
  ],
  "added": [
    [
      "00836378",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008363a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008353cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008353c8.md#insn-008353cc) · [`008353c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008353c8.md#insn-008353c8)
- 新版 [`00836378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836374.md#insn-00836378)

~~~diff
- 008353cc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008353cc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 008353cc bytes 680100b4
+ 00836378 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00836378 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00836378 bytes 680100b4
- 008353c8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 008353c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008353c8 bytes 080840f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c73310ad748fea09df24f6e70787ed3f"></a>

### [`008353fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008353fc.md) → [`008363a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/008363a8.md) FUN_008363a8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a832d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a83/00a832d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`00a842c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a84/00a842c4.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 75.00% / 新版 81.82%

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
      "site": "008363dc",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00835430",
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
      "008363dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "008363dc",
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

- 旧版 [`00835430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008353fc.md#insn-00835430) · [`00835418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008353fc.md#insn-00835418) · [`00835424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008353fc.md#insn-00835424)
- 新版 [`008363dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/008363a8.md#insn-008363dc) · [`008363c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/008363a8.md#insn-008363c4) · [`008363d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/008363a8.md#insn-008363d0)

~~~diff
- 00835430 ["INT_ADD", "register:40f0:8", ["const:835430:8", "const:4:8"]]
- 00835430 ["CALL", null, ["ram:47ad34:8"]]
+ 008363dc ["INT_ADD", "register:40f0:8", ["const:8363dc:8", "const:4:8"]]
+ 008363dc ["CALL", null, ["ram:47b054:8"]]
- 00835430 bytes 4116f197
+ 008363dc bytes 1e13f197
- 00835418 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00835418 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 008363c4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008363c4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00835418 bytes a1010054
+ 008363c4 bytes a1010054
- 00835424 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 008363d0 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00835424 bytes 40010054
+ 008363d0 bytes 40010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25e7e9b9bf25513e7341732b7f2e238e"></a>

### [`008354f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008354f4.md) → [`008364a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/008364a0.md) FUN_008364a0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008364ac",
      "incomplete_value": false,
      "site": "008364b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835500",
      "incomplete_value": false,
      "site": "00835504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "008364b0",
      "DATA",
      [
        "storage",
        "00c7ec78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008364b0",
      "DATA",
      [
        "storage",
        "00c7fc48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008354fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008354f4.md#insn-008354fc) · [`00835500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008354f4.md#insn-00835500)
- 新版 [`008364a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/008364a0.md#insn-008364a8) · [`008364ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/008364a0.md#insn-008364ac)

~~~diff
- 008354fc ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 008364a8 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 008354fc bytes 492200b0
+ 008364a8 bytes 492200b0
- 00835500 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00835500 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00835500 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00835500 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008364ac ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 008364ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008364ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008364ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00835500 bytes 29e13191
+ 008364ac bytes 29213191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-221c8699f4f4b6fd7fab0af4111abcc4"></a>

### [`00835518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835518.md) → [`008364c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/008364c4.md) FUN_008364c4

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
      "definition_site": "008364cc",
      "incomplete_value": false,
      "site": "008364d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835520",
      "incomplete_value": false,
      "site": "00835524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "008364d0",
      "DATA",
      [
        "storage",
        "00c7ec78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008364d0",
      "DATA",
      [
        "storage",
        "00c7fc48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083551c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835518.md#insn-0083551c) · [`00835520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835518.md#insn-00835520) · [`00835544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835518.md#insn-00835544)
- 新版 [`008364c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/008364c4.md#insn-008364c8) · [`008364cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/008364c4.md#insn-008364cc) · [`008364f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/008364c4.md#insn-008364f0)

~~~diff
- 0083551c ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 008364c8 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0083551c bytes 492200b0
+ 008364c8 bytes 492200b0
- 00835520 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00835520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00835520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00835520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008364cc ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 008364cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008364cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008364cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00835520 bytes 29e13191
+ 008364cc bytes 29213191
- 00835544 ["INT_ADD", "register:40f0:8", ["const:835544:8", "const:4:8"]]
- 00835544 ["CALL", null, ["callee:00c58f50:8"]]
+ 008364f0 ["INT_ADD", "register:40f0:8", ["const:8364f0:8", "const:4:8"]]
+ 008364f0 ["CALL", null, ["callee:00c58f50:8"]]
- 00835544 bytes 8f8a1094
+ 008364f0 bytes 988a1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a413f05692c4659c4b2b3460ba168a68"></a>

### [`0083565c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083565c.md) → [`00836608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836608.md) FUN_00836608

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00835138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/00835138.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 61.02% / 新版 61.02%

CFGの説明率　旧版 15.00% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083567c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083568c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083568c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083568c",
      "DATA",
      [
        "storage",
        "00c7ec78",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008356bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008366cc"
      ]
    ]
  ],
  "added": [
    [
      "00836638",
      "DATA",
      [
        "storage",
        "00c7fc48",
        null,
        "undefined *"
      ]
    ],
    [
      "00836668",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008366cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083567c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083565c.md#insn-0083567c) · [`0083568c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083565c.md#insn-0083568c) · [`008356bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083565c.md#insn-008356bc)

~~~diff
- 0083567c ["COPY", "tmp:0:8", ["const:0:8"]]
- 0083567c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 0083567c ["INT_ADD", "register:40a8:8", ["register:40a8:8", "const:10:8"]]
- 0083567c ["STORE", null, ["const:1b1:8", "register:40a8:8", "tmp:1:8"]]
- 0083567c bytes bf0e01f8
- 0083568c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 0083568c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0083568c ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0083568c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083568c bytes 2a2000a9
- 008356bc ["CBRANCH", null, ["local:b16:8", "register:102:1"]]
- 008356bc bytes 22030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0b0f6d538f4d472e10a6bb5d7d7e628"></a>

### [`00835794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835794.md) → [`00836740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836740.md) FUN_00836740

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085b304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b304.md) [`0085b324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b324.md) [`0085b32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b32c.md) [`0085b338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b338.md)
- 新版 呼出元 0件  · 呼出先 11件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`0085c2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c2b0.md) [`0085c2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c2d0.md) [`0085c2d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c2d8.md) [`0085c2e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c2e4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 94.50% / 新版 94.50%

CFGの説明率　旧版 68.00% / 新版 77.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00835794"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00835798"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00835798"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00835794",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00835798",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083579c",
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
      "00836740",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00836744",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00836748",
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

- 旧版 [`00835794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835794.md#insn-00835794) · [`00835798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835794.md#insn-00835798) · [`0083579c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835794.md#insn-0083579c)

~~~diff
- 00835794 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00835794 ["STORE", null, ["const:1b1:8", "register:8:8", "register:5100:8"]]
- 00835794 bytes e80f1cfc
- 00835798 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00835798 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00835798 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:8:8"]]
- 00835798 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00835798 bytes fdfb00a9
- 0083579c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 0083579c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 0083579c bytes f70f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa560a4205c880b5215bd32202ffa92d"></a>

### [`00835970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835970.md) → [`0083691c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/0083691c.md) FUN_0083691c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00836928",
      "incomplete_value": false,
      "site": "0083692c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083597c",
      "incomplete_value": false,
      "site": "00835980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "0083692c",
      "DATA",
      [
        "storage",
        "00c7ecf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083692c",
      "DATA",
      [
        "storage",
        "00c7fcc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00835978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835970.md#insn-00835978) · [`0083597c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835970.md#insn-0083597c)
- 新版 [`00836924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/0083691c.md#insn-00836924) · [`00836928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/0083691c.md#insn-00836928)

~~~diff
- 00835978 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 00836924 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00835978 bytes 492200b0
+ 00836924 bytes 492200b0
- 0083597c ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 0083597c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083597c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083597c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00836928 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 00836928 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00836928 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00836928 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083597c bytes 29e13391
+ 00836928 bytes 29213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd7d180f2aee90a731477a9b17d01d7f"></a>

### [`00835994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835994.md) → [`00836940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836940.md) FUN_00836940

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 20.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008359a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0083694c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008359a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008359a0",
      "DATA",
      [
        "storage",
        "00c7ecf8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008359a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083697c"
      ]
    ]
  ],
  "added": [
    [
      "0083694c",
      "DATA",
      [
        "storage",
        "00c7fcc8",
        null,
        "undefined *"
      ]
    ],
    [
      "00836950",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083697c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008359a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835994.md#insn-008359a0) · [`008359a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835994.md#insn-008359a4)
- 新版 [`0083694c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836940.md#insn-0083694c)

~~~diff
- 008359a0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008359a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008359a0 bytes 090000f9
- 008359a4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008359a4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 008359a4 bytes 680100b4
+ 0083694c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0083694c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0083694c bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2fc210f62c576004f5ca21d92fe8ce5"></a>

### [`008359d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008359d4.md) → [`00836980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836980.md) FUN_00836980

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00835138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/00835138.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008369b4",
      "incomplete_value": false,
      "site": "008369b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835a08",
      "incomplete_value": false,
      "site": "00835a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "008369b4",
      "DATA",
      [
        "storage",
        "00c7ecf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008369b4",
      "DATA",
      [
        "storage",
        "00c7fcc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008359f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008359d4.md#insn-008359f0) · [`008359f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008359d4.md#insn-008359f8) · [`008359fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008359d4.md#insn-008359fc)
- 新版 [`0083699c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836980.md#insn-0083699c) · [`008369a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836980.md#insn-008369a4) · [`008369a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836980.md#insn-008369a8)

~~~diff
- 008359f0 ["INT_ADD", "register:40f0:8", ["const:8359f0:8", "const:4:8"]]
- 008359f0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0083699c ["INT_ADD", "register:40f0:8", ["const:83699c:8", "const:4:8"]]
+ 0083699c ["CALL", null, ["callee:00c58f30:8"]]
- 008359f0 bytes 5c891094
+ 0083699c bytes 65891094
- 008359f8 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 008369a4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 008359f8 bytes 482200b0
+ 008369a4 bytes 482200b0
- 008359fc ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 008359fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008359fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008359fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008369a8 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 008369a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008369a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008369a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008359fc bytes 08e13391
+ 008369a8 bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1c6719a04b42c4e6a01e14ad269f7c5"></a>

### [`00835ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835ad8.md) → [`00836a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836a84.md) FUN_00836a84

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00835138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/00835138.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00836ab4",
      "incomplete_value": false,
      "site": "00836ab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835b08",
      "incomplete_value": false,
      "site": "00835b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00836ab4",
      "DATA",
      [
        "storage",
        "00c7ecf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00836ab4",
      "DATA",
      [
        "storage",
        "00c7fcc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00835afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835ad8.md#insn-00835afc) · [`00835b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835ad8.md#insn-00835b00) · [`00835b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835ad8.md#insn-00835b40)
- 新版 [`00836aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836a84.md#insn-00836aa8) · [`00836aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836a84.md#insn-00836aac) · [`00836aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836a84.md#insn-00836aec)

~~~diff
- 00835afc ["COPY", "register:4050:8", ["const:c7e000:8"]]
+ 00836aa8 ["COPY", "register:4050:8", ["const:c7f000:8"]]
- 00835afc bytes 4a2200b0
+ 00836aa8 bytes 4a2200b0
- 00835b00 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 00835b00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00835b00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00835b00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00836aac ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 00836aac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00836aac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00836aac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00835b00 bytes 4ae13391
+ 00836aac bytes 4a213391
- 00835b40 ["INT_ADD", "register:40f0:8", ["const:835b40:8", "const:4:8"]]
- 00835b40 ["CALL", null, ["callee:00c58f30:8"]]
+ 00836aec ["INT_ADD", "register:40f0:8", ["const:836aec:8", "const:4:8"]]
+ 00836aec ["CALL", null, ["callee:00c58f30:8"]]
- 00835b40 bytes 08891094
+ 00836aec bytes 11891094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c05da48dae6573b6e421bb7b86ad8d5"></a>

### [`00835c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835c10.md) → [`00836bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836bbc.md) FUN_00836bbc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467df4.md) [`0055a624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a624.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00862900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00862/00862900.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00468114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468114.md) [`0055a944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055a/0055a944.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008638ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00863/008638ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00836c54",
      "incomplete_value": true,
      "site": "00836c58",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:a38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835ca8",
      "incomplete_value": true,
      "site": "00835cac",
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
                "const:ca4000:8"
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00836c40",
      "incomplete_value": false,
      "site": "00836c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835c94",
      "incomplete_value": false,
      "site": "00835cac",
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
            "const:f28:8"
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
    "new": {
      "definition_site": "00836c4c",
      "incomplete_value": false,
      "site": "00836c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835ca0",
      "incomplete_value": false,
      "site": "00835cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "00836c40",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00836c44",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00836c4c",
      "PARAM",
      [
        "storage",
        "00c7e5e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00836c40",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00836c44",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "00836c4c",
      "PARAM",
      [
        "storage",
        "00c7f5b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00835cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835c10.md#insn-00835cac) · [`00835c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835c10.md#insn-00835c38) · [`00835c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835c10.md#insn-00835c44)
- 新版 [`00836c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836bbc.md#insn-00836c58) · [`00836be4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836bbc.md#insn-00836be4) · [`00836bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836bbc.md#insn-00836bf0)

~~~diff
- 00835cac ["INT_ADD", "register:40f0:8", ["const:835cac:8", "const:4:8"]]
- 00835cac ["CALL", null, ["callee:00c596b0:8"]]
+ 00836c58 ["INT_ADD", "register:40f0:8", ["const:836c58:8", "const:4:8"]]
+ 00836c58 ["CALL", null, ["callee:00c596b0:8"]]
- 00835cac bytes 8d8a1094
+ 00836c58 bytes 968a1094
- 00835c38 ["INT_ADD", "register:40f0:8", ["const:835c38:8", "const:4:8"]]
- 00835c38 ["CALL", null, ["callee:008ba294:8"]]
+ 00836be4 ["INT_ADD", "register:40f0:8", ["const:836be4:8", "const:4:8"]]
+ 00836be4 ["CALL", null, ["callee:008ba294:8"]]
- 00835c38 bytes ac0d0294
+ 00836be4 bytes ac0d0294
- 00835c44 ["INT_ADD", "register:40f0:8", ["const:835c44:8", "const:4:8"]]
- 00835c44 ["CALL", null, ["callee:008ba29c:8"]]
+ 00836bf0 ["INT_ADD", "register:40f0:8", ["const:836bf0:8", "const:4:8"]]
+ 00836bf0 ["CALL", null, ["callee:008ba29c:8"]]
- 00835c44 bytes ab0d0294
+ 00836bf0 bytes ab0d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-103d8f1e57e75d6d7db88fbce18e620b"></a>

### [`00835dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835dc4.md) → [`00836d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836d70.md) FUN_00836d70

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
      "definition_site": "00836d84",
      "incomplete_value": false,
      "site": "00836d88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835dd8",
      "incomplete_value": false,
      "site": "00835ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "00836d88",
      "DATA",
      [
        "storage",
        "00c7ed78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00836d88",
      "DATA",
      [
        "storage",
        "00c7fd48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00835dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835dc4.md#insn-00835dd0) · [`00835dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835dc4.md#insn-00835dd4) · [`00835dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835dc4.md#insn-00835dd8)
- 新版 [`00836d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836d70.md#insn-00836d7c) · [`00836d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836d70.md#insn-00836d80) · [`00836d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836d70.md#insn-00836d84)

~~~diff
- 00835dd0 ["INT_ADD", "register:40f0:8", ["const:835dd0:8", "const:4:8"]]
- 00835dd0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00836d7c ["INT_ADD", "register:40f0:8", ["const:836d7c:8", "const:4:8"]]
+ 00836d7c ["CALL", null, ["callee:00c58f30:8"]]
- 00835dd0 bytes 64881094
+ 00836d7c bytes 6d881094
- 00835dd4 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00836d80 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00835dd4 bytes 482200b0
+ 00836d80 bytes 482200b0
- 00835dd8 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00835dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00835dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00835dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00836d84 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 00836d84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00836d84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00836d84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00835dd8 bytes 08e13591
+ 00836d84 bytes 08213591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e9822af5e9fad1c1eb8bcbfaa8d3837"></a>

### [`00835de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835de8.md) → [`00836d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836d94.md) FUN_00836d94

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
      "definition_site": "00836d98",
      "incomplete_value": false,
      "site": "00836d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835dec",
      "incomplete_value": false,
      "site": "00835df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "00836d9c",
      "DATA",
      [
        "storage",
        "00c7ed78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00836d9c",
      "DATA",
      [
        "storage",
        "00c7fd48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00835de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835de8.md#insn-00835de8) · [`00835dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835de8.md#insn-00835dec)
- 新版 [`00836d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836d94.md#insn-00836d94) · [`00836d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836d94.md#insn-00836d98)

~~~diff
- 00835de8 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00836d94 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00835de8 bytes 482200b0
+ 00836d94 bytes 482200b0
- 00835dec ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00835dec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00835dec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00835dec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00836d98 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 00836d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00836d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00836d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00835dec bytes 08e13591
+ 00836d98 bytes 08213591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb6ed742089f91e82db258f234ea270b"></a>

### [`00835e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835e00.md) → [`00836dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836dac.md) FUN_00836dac

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

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
      "site": "00836dd0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00835e24",
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
      "00836dd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00836dd0",
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

- 旧版 [`00835e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835e00.md#insn-00835e24) · [`00835e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835e00.md#insn-00835e30)
- 新版 [`00836dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836dac.md#insn-00836dd0) · [`00836ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836dac.md#insn-00836ddc)

~~~diff
- 00835e24 ["INT_ADD", "register:40f0:8", ["const:835e24:8", "const:4:8"]]
- 00835e24 ["CALL", null, ["ram:47ad34:8"]]
+ 00836dd0 ["INT_ADD", "register:40f0:8", ["const:836dd0:8", "const:4:8"]]
+ 00836dd0 ["CALL", null, ["ram:47b054:8"]]
- 00835e24 bytes c413f197
+ 00836dd0 bytes a110f197
- 00835e30 ["INT_ADD", "register:40f0:8", ["const:835e30:8", "const:4:8"]]
- 00835e30 ["CALL", null, ["callee:0047d134:8"]]
+ 00836ddc ["INT_ADD", "register:40f0:8", ["const:836ddc:8", "const:4:8"]]
+ 00836ddc ["CALL", null, ["callee:0047d134:8"]]
- 00835e30 bytes f91bf197
+ 00836ddc bytes d618f197
~~~


<a id="compare-9c733346054b967a59e9a499770a8c62"></a>

### [`00836024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836024.md) → [`00836fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836fd0.md) FUN_00836fd0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00835e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835e70.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00836e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836e1c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00836fdc",
      "incomplete_value": false,
      "site": "00836fe0",
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
      "definition_site": "00836030",
      "incomplete_value": false,
      "site": "00836034",
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
      "00836fdc",
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
      "00836fdc",
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

- 旧版 [`00836034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836024.md#insn-00836034) · [`0083602c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836024.md#insn-0083602c) · [`00836030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836024.md#insn-00836030)
- 新版 [`00836fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836fd0.md#insn-00836fe0) · [`00836fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836fd0.md#insn-00836fd8) · [`00836fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836fd0.md#insn-00836fdc)

~~~diff
- 00836034 ["INT_ADD", "register:40f0:8", ["const:836034:8", "const:4:8"]]
- 00836034 ["CALL", null, ["callee:0043bad8:8"]]
+ 00836fe0 ["INT_ADD", "register:40f0:8", ["const:836fe0:8", "const:4:8"]]
+ 00836fe0 ["CALL", null, ["callee:0043bad8:8"]]
- 00836034 bytes e115f097
+ 00836fe0 bytes be12f097
- 0083602c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00836fd8 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0083602c bytes 00d4ffb0
+ 00836fd8 bytes 00d4ffd0
- 00836030 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00836030 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00836030 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00836030 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00836fdc ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00836fdc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00836fdc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00836fdc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00836030 bytes 00303e91
+ 00836fdc bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9838d890145056d741b5995bfa43c5a"></a>

### [`00836dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836dc8.md) → [`00837d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/00837d74.md) FUN_00837d74

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00836038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836038.md) [`00836dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836dc8.md) · 呼出先 6件 [`0083669c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/0083669c.md) [`00836dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836dc8.md) [`008375e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/008375e0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 2件 [`00836fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836fe4.md) [`00837d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/00837d74.md) · 呼出先 6件 [`00837648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/00837648.md) [`00837d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00837/00837d74.md) [`0083858c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00838/0083858c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.04% / 新版 85.04%

CFGの説明率　旧版 47.52% / 新版 41.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00836f94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00837194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00837448"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00836e54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00837de4"
      ]
    ],
    [
      "unmatched:00836f94",
      "WRITE",
      [
        "storage",
        "Stack[-0xe0]",
        null,
        null
      ]
    ],
    [
      "unmatched:008370d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008384c0"
      ]
    ]
  ],
  "added": [
    [
      "00837e00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00837de4"
      ]
    ],
    [
      "00837f40",
      "WRITE",
      [
        "storage",
        "Stack[-0xe0]",
        null,
        null
      ]
    ],
    [
      "0083807c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008384c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00836e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836dc8.md#insn-00836e54) · [`00836f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836dc8.md#insn-00836f5c) · [`00836f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836dc8.md#insn-00836f94)

~~~diff
- 00836e54 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00836e54 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00836e54 bytes 23ffff54
- 00836f5c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00836f5c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00836f5c ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 00836f5c ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 00836f5c bytes 08a5889a
- 00836f94 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00836f94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00836f94 bytes f30b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a90c42caeb0e1b4115841ecfcafcea43"></a>

### [`00837930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/00837930.md) → [`008388dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00838/008388dc.md) FUN_008388dc

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0082ee78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082ee78.md) · 呼出先 12件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0067e1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e1dc.md) [`00862ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00862/00862ca8.md) [`00864590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864590.md)
- 新版 呼出元 1件 [`0082fe24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082f/0082fe24.md) · 呼出先 12件 [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0067e58c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0067e/0067e58c.md) [`00863c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00863/00863c54.md) [`0086553c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00865/0086553c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 23.09% / 新版 23.09%

CFGの説明率　旧版 2.05% / 新版 2.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 88件, `unresolved_call_alignment` 95件, `unresolved_store_alignment` 147件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00837974"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00837980"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00837980"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00837974",
      "DATA",
      [
        "storage",
        "00c7ee08",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00837984",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00837988",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008394b4"
      ]
    ]
  ],
  "added": [
    [
      "00838920",
      "DATA",
      [
        "storage",
        "00c7fdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00838930",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "00838934",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008394b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00837974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/00837930.md#insn-00837974) · [`00837980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/00837930.md#insn-00837980) · [`00837994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/00837930.md#insn-00837994)

~~~diff
- 00837974 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00837974 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00837974 bytes 680200f9
- 00837980 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2e0:8"]]
- 00837980 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00837980 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00837980 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00837980 bytes 600217ad
- 00837994 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00837994 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00837994 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:2b:8"]]
- 00837994 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00837994 bytes ffaf0039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f88e6a97c0b4dc9aa5b80c88e9ea80ae"></a>

### [`008389a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/008389a8.md) → [`00839954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839954.md) FUN_00839954

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00682364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00682714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00682/00682714.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008389c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00838a30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00839970"
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
      "unmatched:008389c4",
      "DATA",
      [
        "storage",
        "00c7ee08",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:008389d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008399a0"
      ]
    ],
    [
      "unmatched:00838a08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008399d0"
      ]
    ]
  ],
  "added": [
    [
      "00839970",
      "DATA",
      [
        "storage",
        "00c7fdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00839984",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008399a0"
      ]
    ],
    [
      "008399b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008399d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008389c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/008389a8.md#insn-008389c4) · [`008389d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/008389a8.md#insn-008389d8) · [`00838a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/008389a8.md#insn-00838a08)

~~~diff
- 008389c4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008389c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008389c4 bytes 080000f9
- 008389d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008389d8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008389d8 bytes e00000b5
- 00838a08 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00838a08 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00838a08 bytes e00000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4432f0d6e860208e3e793c85c1cb7bd4"></a>

### [`00838a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838a7c.md) → [`00839a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839a28.md) FUN_00839a28

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
      "definition_site": "00839a4c",
      "incomplete_value": false,
      "site": "00839a4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838aa0",
      "incomplete_value": false,
      "site": "00838aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "00839a4c",
      "DATA",
      [
        "storage",
        "00c7ee28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00839a4c",
      "DATA",
      [
        "storage",
        "00c7fdf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838a7c.md#insn-00838a90) · [`00838a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838a7c.md#insn-00838a98) · [`00838a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838a7c.md#insn-00838a9c)
- 新版 [`00839a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839a28.md#insn-00839a3c) · [`00839a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839a28.md#insn-00839a44) · [`00839a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839a28.md#insn-00839a48)

~~~diff
- 00838a90 ["INT_ADD", "register:40f0:8", ["const:838a90:8", "const:4:8"]]
- 00838a90 ["CALL", null, ["callee:00c58f30:8"]]
+ 00839a3c ["INT_ADD", "register:40f0:8", ["const:839a3c:8", "const:4:8"]]
+ 00839a3c ["CALL", null, ["callee:00c58f30:8"]]
- 00838a90 bytes 347d1094
+ 00839a3c bytes 3d7d1094
- 00838a98 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00839a44 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00838a98 bytes 282200d0
+ 00839a44 bytes 282200d0
- 00838a9c ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00838a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00838a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00838a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00839a48 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 00839a48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00839a48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00839a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00838a9c bytes 08a13891
+ 00839a48 bytes 08e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c6eab20ce9523744cd315b3a5c14d14"></a>

### [`00838ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838ab0.md) → [`00839a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839a5c.md) FUN_00839a5c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00839a68",
      "incomplete_value": false,
      "site": "00839a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838abc",
      "incomplete_value": false,
      "site": "00838abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "00839a68",
      "DATA",
      [
        "storage",
        "00c7ee28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00839a68",
      "DATA",
      [
        "storage",
        "00c7fdf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838ab0.md#insn-00838ab4) · [`00838ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838ab0.md#insn-00838ab8)
- 新版 [`00839a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839a5c.md#insn-00839a60) · [`00839a64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839a5c.md#insn-00839a64)

~~~diff
- 00838ab4 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 00839a60 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00838ab4 bytes 292200d0
+ 00839a60 bytes 292200d0
- 00838ab8 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00838ab8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838ab8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838ab8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00839a64 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 00839a64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00839a64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00839a64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838ab8 bytes 29a13891
+ 00839a64 bytes 29e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1829931f1a98bf97baa62a1ee0e245fc"></a>

### [`00838b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b4c.md) → [`00839af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839af8.md) FUN_00839af8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00839b04",
      "incomplete_value": false,
      "site": "00839b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838b58",
      "incomplete_value": false,
      "site": "00838b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
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
      "00839b04",
      "DATA",
      [
        "storage",
        "00c7eea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00839b04",
      "DATA",
      [
        "storage",
        "00c7fe78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b4c.md#insn-00838b50) · [`00838b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b4c.md#insn-00838b54)
- 新版 [`00839afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839af8.md#insn-00839afc) · [`00839b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839af8.md#insn-00839b00)

~~~diff
- 00838b50 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 00839afc ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00838b50 bytes 292200d0
+ 00839afc bytes 292200d0
- 00838b54 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 00838b54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838b54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838b54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00839b00 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 00839b00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00839b00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00839b00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838b54 bytes 29a13a91
+ 00839b00 bytes 29e13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e513f5c4fc399d604c4537dfd23b605"></a>

### [`00838bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838bdc.md) → [`00839b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839b88.md) FUN_00839b88

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00839b94",
      "incomplete_value": false,
      "site": "00839b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838be8",
      "incomplete_value": false,
      "site": "00838be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "00839b94",
      "DATA",
      [
        "storage",
        "00c7ef28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00839b94",
      "DATA",
      [
        "storage",
        "00c7fef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838bdc.md#insn-00838be0) · [`00838be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838bdc.md#insn-00838be4)
- 新版 [`00839b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839b88.md#insn-00839b8c) · [`00839b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839b88.md#insn-00839b90)

~~~diff
- 00838be0 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 00839b8c ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00838be0 bytes 292200d0
+ 00839b8c bytes 292200d0
- 00838be4 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 00838be4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838be4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838be4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00839b90 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 00839b90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00839b90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00839b90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838be4 bytes 29a13c91
+ 00839b90 bytes 29e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3a7aaeb823658510c7dec81881a9a2a"></a>

### [`00838bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838bf8.md) → [`00839ba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839ba4.md) FUN_00839ba4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0082d2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d2e8.md) [`00838d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d58.md) [`00838d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d5c.md) [`00acac44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acac44.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0082e294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082e/0082e294.md) [`00839d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839d04.md) [`00839d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839d08.md) [`00acbc38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acb/00acbc38.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

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
      "definition_site": "00839bd8",
      "incomplete_value": false,
      "site": "00839bd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838c2c",
      "incomplete_value": false,
      "site": "00838c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "00839bd8",
      "DATA",
      [
        "storage",
        "00c7ef98",
        null,
        "undefined *"
      ]
    ],
    [
      "00839c14",
      "READ",
      [
        "storage",
        "00c7efb8",
        null,
        "pointer"
      ]
    ],
    [
      "00839c14",
      "READ",
      [
        "storage",
        "00c7efc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00839bd8",
      "DATA",
      [
        "storage",
        "00c7ff68",
        null,
        "undefined *"
      ]
    ],
    [
      "00839c14",
      "READ",
      [
        "storage",
        "00c7ff88",
        null,
        "pointer"
      ]
    ],
    [
      "00839c14",
      "READ",
      [
        "storage",
        "00c7ff90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838bf8.md#insn-00838c1c) · [`00838c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838bf8.md#insn-00838c20) · [`00838c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838bf8.md#insn-00838c24)
- 新版 [`00839bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839ba4.md#insn-00839bc8) · [`00839bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839ba4.md#insn-00839bcc) · [`00839bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839ba4.md#insn-00839bd0)

~~~diff
- 00838c1c ["INT_ADD", "register:40f0:8", ["const:838c1c:8", "const:4:8"]]
- 00838c1c ["CALL", null, ["callee:0082e294:8"]]
+ 00839bc8 ["INT_ADD", "register:40f0:8", ["const:839bc8:8", "const:4:8"]]
+ 00839bc8 ["CALL", null, ["callee:0082e294:8"]]
- 00838c1c bytes b3d1ff97
+ 00839bc8 bytes b3d1ff97
- 00838c20 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00839bcc ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00838c20 bytes 282200d0
+ 00839bcc bytes 282200d0
- 00838c24 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00838c24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00838c24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00838c24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00839bd0 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00839bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00839bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00839bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00838c24 bytes 08613e91
+ 00839bd0 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c67c9ec96dcc4456096d6d58e798d470"></a>

### [`00838d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d10.md) → [`00839cbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839cbc.md) FUN_00839cbc

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
      "definition_site": "00839ce0",
      "incomplete_value": false,
      "site": "00839ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838d34",
      "incomplete_value": false,
      "site": "00838d34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "00839ce0",
      "DATA",
      [
        "storage",
        "00c7ef98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00839ce0",
      "DATA",
      [
        "storage",
        "00c7ff68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d10.md#insn-00838d24) · [`00838d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d10.md#insn-00838d2c) · [`00838d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d10.md#insn-00838d30)
- 新版 [`00839cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839cbc.md#insn-00839cd0) · [`00839cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839cbc.md#insn-00839cd8) · [`00839cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839cbc.md#insn-00839cdc)

~~~diff
- 00838d24 ["INT_ADD", "register:40f0:8", ["const:838d24:8", "const:4:8"]]
- 00838d24 ["CALL", null, ["callee:00c58f30:8"]]
+ 00839cd0 ["INT_ADD", "register:40f0:8", ["const:839cd0:8", "const:4:8"]]
+ 00839cd0 ["CALL", null, ["callee:00c58f30:8"]]
- 00838d24 bytes 8f7c1094
+ 00839cd0 bytes 987c1094
- 00838d2c ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 00839cd8 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00838d2c bytes 282200d0
+ 00839cd8 bytes 282200d0
- 00838d30 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00838d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00838d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00838d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00839cdc ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00839cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00839cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00839cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00838d30 bytes 08613e91
+ 00839cdc bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0169fb5a3de6c36f5d8224158e23ecb"></a>

### [`00838d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d44.md) → [`00839cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839cf0.md) FUN_00839cf0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00839cfc",
      "incomplete_value": false,
      "site": "00839cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838d50",
      "incomplete_value": false,
      "site": "00838d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "00839cfc",
      "DATA",
      [
        "storage",
        "00c7ef98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00839cfc",
      "DATA",
      [
        "storage",
        "00c7ff68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d44.md#insn-00838d48) · [`00838d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d44.md#insn-00838d4c)
- 新版 [`00839cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839cf0.md#insn-00839cf4) · [`00839cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839cf0.md#insn-00839cf8)

~~~diff
- 00838d48 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 00839cf4 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00838d48 bytes 292200d0
+ 00839cf4 bytes 292200d0
- 00838d4c ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00838d4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838d4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838d4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00839cf8 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00839cf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00839cf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00839cf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838d4c bytes 29613e91
+ 00839cf8 bytes 29a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a70f58835094a72ebcec4975b627c82"></a>

### [`00838d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d60.md) → [`00839d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839d0c.md) FUN_00839d0c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`007562fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00756/007562fc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085bbc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085bbc8.md) [`00ac86ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac86ac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 5件 [`007566ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00756/007566ac.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`0085cb74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085cb74.md) [`00ac96a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac96a0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.00% / 新版 74.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00838da4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00838da8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00838dd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00838d98",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00838d9c",
      "READ",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00838da4",
      "WRITE",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00839d44",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "00839d48",
      "READ",
      [
        "storage",
        "00ca5a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00839d50",
      "WRITE",
      [
        "storage",
        "00ca5a28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d60.md#insn-00838d84) · [`00838da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d60.md#insn-00838da4) · [`00838da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d60.md#insn-00838da8)
- 新版 [`00839d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839d0c.md#insn-00839d30)

~~~diff
- 00838d84 ["INT_ADD", "register:40f0:8", ["const:838d84:8", "const:4:8"]]
- 00838d84 ["CALL", null, ["callee:00ac96a0:8"]]
+ 00839d30 ["INT_ADD", "register:40f0:8", ["const:839d30:8", "const:4:8"]]
+ 00839d30 ["CALL", null, ["callee:00ac96a0:8"]]
- 00838d84 bytes 4a3e0a94
+ 00839d30 bytes 5c3e0a94
- 00838da4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 00838da4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00838da4 bytes 093505f9
- 00838da8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 00838da8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00838da8 bytes ca3e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71ccc417a566dae0441b7d953bf545f5"></a>

### [`00838e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838e64.md) → [`00839e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839e10.md) _INIT_153

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 66.10% / 新版 66.10%

CFGの説明率　旧版 37.14% / 新版 37.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00838e94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00838ea8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00838eac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00838e94",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00838ea0",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00838ea8",
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
      "00839e40",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00839e4c",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00839e54",
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

- 旧版 [`00838e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838e64.md#insn-00838e94) · [`00838ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838e64.md#insn-00838ea8) · [`00838eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838e64.md#insn-00838eac)

~~~diff
- 00838e94 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00838e94 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00838e94 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00838e94 bytes a9831ff8
- 00838ea8 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00838ea8 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00838ea8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00838ea8 bytes ea130278
- 00838eac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00838eac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00838eac bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fde7344f10094d5cd32381f9926cb96"></a>

### [`008391f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/008391f4.md) → [`0083a1a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083a1a0.md) _INIT_154

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.79% / 新版 80.79%

CFGの説明率　旧版 47.50% / 新版 35.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008391f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008391f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008391fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008391f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008391fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00839200",
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
      "0083a1a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0083a1a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0083a1ac",
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

- 旧版 [`008391f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/008391f4.md#insn-008391f8) · [`008391fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/008391f4.md#insn-008391fc) · [`00839200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/008391f4.md#insn-00839200)

~~~diff
- 008391f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008391f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008391f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 008391f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008391f8 bytes fd7b0fa9
- 008391fc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008391fc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 008391fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 008391fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008391fc bytes fc5710a9
- 00839200 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00839200 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00839200 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00839200 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00839200 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3f27eeb681a8609c1b11450c9d14fa1"></a>

### [`00839844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839844.md) → [`0083a7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083a7f0.md) FUN_0083a7f0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a14de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14de0.md) · 呼出先 2件 [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`00480f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480f78.md)
- 新版 呼出元 1件 [`00a15d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a15/00a15d8c.md) · 呼出先 2件 [`004810a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/004810a8.md) [`00481298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/00481298.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 37.04% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008398f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0083a8a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00839918",
      "incomplete_value": true,
      "site": "0083991c",
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
      "unmatched:008398f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083a890"
      ]
    ]
  ],
  "added": [
    [
      "0083a8a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0083a890"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008398a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839844.md#insn-008398a4) · [`008398f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839844.md#insn-008398f4) · [`0083991c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839844.md#insn-0083991c)
- 新版 [`0083a8c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083a7f0.md#insn-0083a8c8)

~~~diff
- 008398a4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008398a4 ["RETURN", null, ["register:0:8"]]
- 008398a4 bytes c0035fd6
- 008398f4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008398f4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 008398f4 bytes 81ffff54
- 0083991c ["INT_ADD", "register:40f0:8", ["const:83991c:8", "const:4:8"]]
- 0083991c ["CALL", null, ["callee:004810a8:8"]]
+ 0083a8c8 ["INT_ADD", "register:40f0:8", ["const:83a8c8:8", "const:4:8"]]
+ 0083a8c8 ["CALL", null, ["callee:004810a8:8"]]
- 0083991c bytes 1b1df197
+ 0083a8c8 bytes f819f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e26ae2f93c03e4c26b80a485eb9ec331"></a>

### [`00839950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839950.md) → [`0083a8fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083a8fc.md) FUN_0083a8fc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0062c100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062c/0062c100.md) [`0075d7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d7b4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`0062c4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062c/0062c4b0.md) [`0075db64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075db64.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 61.11% / 新版 68.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083a95c",
      "incomplete_value": false,
      "site": "0083a964",
      "value": [
        "leaf",
        "const:28:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008399b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839950.md#insn-008399b8) · [`008399a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839950.md#insn-008399a0) · [`008399e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839950.md#insn-008399e0)
- 新版 [`0083a964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083a8fc.md#insn-0083a964) · [`0083a94c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083a8fc.md#insn-0083a94c) · [`0083a98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083a8fc.md#insn-0083a98c)

~~~diff
- 008399b8 ["INT_ADD", "register:40f0:8", ["const:8399b8:8", "const:4:8"]]
- 008399b8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0083a964 ["INT_ADD", "register:40f0:8", ["const:83a964:8", "const:4:8"]]
+ 0083a964 ["CALL", null, ["callee:00c58f30:8"]]
- 008399b8 bytes 6a791094
+ 0083a964 bytes 73791094
- 008399a0 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008399a0 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 0083a94c ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 0083a94c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 008399a0 bytes 0a030054
+ 0083a94c bytes 0a030054
- 008399e0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008399e0 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 0083a98c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 0083a98c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 008399e0 bytes 680000b4
+ 0083a98c bytes 680000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b31aa94cfaca25e0600b7454bf1a731"></a>

### [`00839b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839b28.md) → [`0083aad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083aad4.md) FUN_0083aad4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0075d7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d7b4.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0075db64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075db64.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839b28.md#insn-00839b2c) · [`00839b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839b28.md#insn-00839b50) · [`00839b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839b28.md#insn-00839b5c)
- 新版 [`0083aad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083aad4.md#insn-0083aad8) · [`0083aafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083aad4.md#insn-0083aafc) · [`0083ab08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083aad4.md#insn-0083ab08)

~~~diff
- 00839b2c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00839b2c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0083aad8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 0083aad8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00839b2c bytes a90100b4
+ 0083aad8 bytes a90100b4
- 00839b50 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 0083aafc ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00839b50 bytes 80000054
+ 0083aafc bytes 80000054
- 00839b5c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00839b5c ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00839b5c ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
+ 0083ab08 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 0083ab08 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
+ 0083ab08 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00839b5c bytes 6d000054
+ 0083ab08 bytes 6d000054
~~~


<a id="compare-86fd3fc249391b94088795330d159e82"></a>

### [`00839b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839b70.md) → [`0083ab1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083ab1c.md) FUN_0083ab1c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a89b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a89/00a89b40.md) · 呼出先 7件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00a35bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a35/00a35bec.md) [`00a378c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a37/00a378c8.md) [`00a37f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a37/00a37f30.md) [`00a38c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a38c10.md)
- 新版 呼出元 1件 [`00a8ab34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a8a/00a8ab34.md) · 呼出先 7件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00a36be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a36/00a36be0.md) [`00a388bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a38/00a388bc.md) [`00a38f24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a38/00a38f24.md) [`00a39c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a39/00a39c04.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 50.00% / 新版 45.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00839b70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00839b70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00839b74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00839b70",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00839b74",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00839b78",
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
      "0083ab1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0083ab20",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0083ab24",
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

- 旧版 [`00839b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839b70.md#insn-00839b70) · [`00839b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839b70.md#insn-00839b74) · [`00839b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839b70.md#insn-00839b78)

~~~diff
- 00839b70 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00839b70 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00839b70 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00839b70 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00839b70 bytes fd7bbba9
- 00839b74 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00839b74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00839b74 bytes f90b00f9
- 00839b78 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00839b78 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00839b78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00839b78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00839b78 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-348b86d22b7a8db144e27886bc891ecb"></a>

### [`00839da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839da4.md) → [`0083ad50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083ad50.md) _INIT_155

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00839584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839584.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`0083a530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083a530.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.90% / 新版 79.90%

CFGの説明率　旧版 14.81% / 新版 17.39%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00839dd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00839dfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00839e20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00839dd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00839de0",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00839dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0083ad80",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0083ad8c",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0083ada8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839da4.md#insn-00839dd4) · [`00839dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839da4.md#insn-00839dfc) · [`00839e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839da4.md#insn-00839e20)

~~~diff
- 00839dd4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00839dd4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00839dd4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00839dd4 bytes a9831ff8
- 00839dfc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00839dfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00839dfc bytes e013813c
- 00839e20 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00839e20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00839e20 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c4d43db47917b2d06616c3893c6f73b"></a>

### [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) → [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) FUN_0083b124

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084a098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084a/0084a098.md) · 呼出先 150件 [`0044ab50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ab50.md) [`0044ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ab78.md) [`0044d730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d730.md) [`0044d848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d848.md) [`0044e108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e108.md)
- 新版 呼出元 1件 [`0084b044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084b/0084b044.md) · 呼出先 148件 [`0044d820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044d/0044d820.md) [`0044dc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044d/0044dc80.md) [`0044e1f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044e/0044e1f8.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0046ec04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ec04.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.60% / 新版 88.60%

CFGの説明率　旧版 67.84% / 新版 68.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 44件, `store_condition` 5件, `unresolved_branch_alignment` 154件, `unresolved_call_alignment` 45件, `unresolved_store_alignment` 48件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083a17c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083a17c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083a180"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083a17c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083a180",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083a184",
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
      "0083b128",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0083b12c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0083b130",
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

- 旧版 [`0083a17c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md#insn-0083a17c) · [`0083a180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md#insn-0083a180) · [`0083a184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md#insn-0083a184)

~~~diff
- 0083a17c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0083a17c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0083a17c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 0083a17c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083a17c bytes fd7b16a9
- 0083a180 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0083a180 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0083a180 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 0083a180 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083a180 bytes fc6f17a9
- 0083a184 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0083a184 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0083a184 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 0083a184 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083a184 bytes fa6718a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4224e17caea515dbd50c2cc791fd7a98"></a>

### [`0083f2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f2dc.md) → [`00840288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/00840288.md) FUN_00840288

採用 · 移動量 `+0xfac` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 2件 [`008939b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008939b4.md) [`00a52e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a52/00a52e94.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00894960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894960.md) [`00a53e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a53/00a53e88.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-398adfcd0fea15dddf68696377957b34"></a>

### [`0083f2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f2e8.md) → [`00840294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/00840294.md) FUN_00840294

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0085b190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b190.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0085c13c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c13c.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 90.91% / 新版 93.02%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083f2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f2e8.md#insn-0083f2f8) · [`0083f318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f2e8.md#insn-0083f318) · [`0083f324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f2e8.md#insn-0083f324)
- 新版 [`008402a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/00840294.md#insn-008402a4) · [`008402c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/00840294.md#insn-008402c4) · [`008402d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/00840294.md#insn-008402d0)

~~~diff
- 0083f2f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0083f2f8 ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
+ 008402a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008402a4 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 0083f2f8 bytes c1070054
+ 008402a4 bytes c1070054
- 0083f318 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 0083f318 ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
+ 008402c4 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 008402c4 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 0083f318 bytes c8060034
+ 008402c4 bytes c8060034
- 0083f324 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0083f324 ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
+ 008402d0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008402d0 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 0083f324 bytes 61060054
+ 008402d0 bytes 61060054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fd01958066766c3027c7f9635a45445"></a>

### [`0083f4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f4c0.md) → [`0084046c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/0084046c.md) FUN_0084046c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00814c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00814/00814c50.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 8件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00491410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00491/00491410.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`00815bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00815/00815bb4.md) [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) · 呼出先 8件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004738a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/004738a0.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`00491730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00491/00491730.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call, call_argument_candidate, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.86% / 新版 85.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008404f0",
      "incomplete_value": true,
      "site": "008404fc",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:4b6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083f544",
      "incomplete_value": true,
      "site": "0083f550",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:3e7:8"
              ]
            ]
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
      "definition_site": "00840544",
      "incomplete_value": true,
      "site": "00840554",
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
      "definition_site": "0083f598",
      "incomplete_value": true,
      "site": "0083f5a8",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00840540",
      "incomplete_value": true,
      "site": "0084055c",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:7f1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083f594",
      "incomplete_value": true,
      "site": "0083f5b0",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:726:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00840498",
      "READ",
      [
        "storage",
        "00c9ad78",
        null,
        "pointer"
      ]
    ],
    [
      "008404a4",
      "READ",
      [
        "storage",
        "00ca5250",
        null,
        "undefined1"
      ]
    ],
    [
      "008404ac",
      "READ",
      [
        "storage",
        "00ca5250",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00840498",
      "READ",
      [
        "storage",
        "00c9bd48",
        null,
        "pointer"
      ]
    ],
    [
      "008404a4",
      "READ",
      [
        "storage",
        "00ca6210",
        null,
        "undefined1"
      ]
    ],
    [
      "008404ac",
      "READ",
      [
        "storage",
        "00ca6210",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083f728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f4c0.md#insn-0083f728) · [`0083f72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f4c0.md#insn-0083f72c) · [`0083f4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f4c0.md#insn-0083f4e0)
- 新版 [`008406d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/0084046c.md#insn-008406d4) · [`008406d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/0084046c.md#insn-008406d8) · [`0084048c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/0084046c.md#insn-0084048c)

~~~diff
- 0083f728 ["INT_ADD", "register:40f0:8", ["const:83f728:8", "const:4:8"]]
- 0083f728 ["CALL", null, ["callee:00c594d0:8"]]
+ 008406d4 ["INT_ADD", "register:40f0:8", ["const:8406d4:8", "const:4:8"]]
+ 008406d4 ["CALL", null, ["callee:00c594d0:8"]]
- 0083f728 bytes 76631094
+ 008406d4 bytes 7f631094
- 0083f72c ["INT_ADD", "register:40f0:8", ["const:83f72c:8", "const:4:8"]]
- 0083f72c ["CALL", null, ["ram:48cd38:8"]]
+ 008406d8 ["INT_ADD", "register:40f0:8", ["const:8406d8:8", "const:4:8"]]
+ 008406d8 ["CALL", null, ["ram:48d058:8"]]
- 0083f72c bytes 8335f197
+ 008406d8 bytes 6032f197
- 0083f4e0 ["COPY", "register:40b8:8", ["const:c9a000:8"]]
+ 0084048c ["COPY", "register:40b8:8", ["const:c9b000:8"]]
- 0083f4e0 bytes d72200f0
+ 0084048c bytes d72200f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0aa8468156d7590df20c5c95b593114"></a>

### [`0083f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) → [`00840888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/00840888.md) FUN_00840888

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084a098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084a/0084a098.md) · 呼出先 39件 [`0044e108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e108.md) [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md) [`00472a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472a40.md) [`0048cd08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd08.md)
- 新版 呼出元 1件 [`0084b044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084b/0084b044.md) · 呼出先 38件 [`0046eb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eb24.md) [`0046f258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f258.md) [`00472d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00472/00472d60.md) [`0048d028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d028.md) [`005979bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979bc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.20% / 新版 81.20%

CFGの説明率　旧版 8.60% / 新版 6.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 61件, `store_condition` 47件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 560件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083f9d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083fcbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083fcbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083f9d8",
      "DATA",
      [
        "storage",
        "00c7f028",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0083fdf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083fdf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x1e8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00840984",
      "DATA",
      [
        "storage",
        "00c7fff8",
        null,
        "undefined *"
      ]
    ],
    [
      "00840d9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "00840da4",
      "WRITE",
      [
        "storage",
        "Stack[-0x1e8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083f9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md#insn-0083f9d8) · [`0083fcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md#insn-0083fcbc) · [`0083fcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md#insn-0083fcc0)

~~~diff
- 0083f9d8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0083f9d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0083f9d8 bytes 090000f9
- 0083fcbc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:300:8"]]
- 0083fcbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0083fcbc ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 0083fcbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 0083fcbc bytes e00218ad
- 0083fcc0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:350:8"]]
- 0083fcc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0083fcc0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 0083fcc0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 0083fcc0 bytes e0821aad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81719b5ca680228fb588a5162e97f9b8"></a>

### [`00846520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846520.md) → [`008474cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/008474cc.md) FUN_008474cc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c426c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c426c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00846540"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008474ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00846534",
      "incomplete_value": true,
      "site": "00846538",
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
            "const:1d8:8"
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
      "unmatched:00846540",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00847500"
      ]
    ]
  ],
  "added": [
    [
      "008474ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00847500"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00846538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846520.md#insn-00846538) · [`00846540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846520.md#insn-00846540)
- 新版 [`008474e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/008474cc.md#insn-008474e4) · [`008474ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/008474cc.md#insn-008474ec)

~~~diff
- 00846538 ["INT_ADD", "register:40f0:8", ["const:846538:8", "const:4:8"]]
- 00846538 ["CALL", null, ["callee:005c426c:8"]]
+ 008474e4 ["INT_ADD", "register:40f0:8", ["const:8474e4:8", "const:4:8"]]
+ 008474e4 ["CALL", null, ["callee:005c426c:8"]]
- 00846538 bytes 61f6f597
+ 008474e4 bytes 62f3f597
- 00846540 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00846540 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00846540 bytes a00000b4
+ 008474ec ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 008474ec ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 008474ec bytes a00000b4
~~~


<a id="compare-d1f711678101a0fd20a4c6d610b3dd0c"></a>

### [`00846560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846560.md) → [`0084750c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/0084750c.md) FUN_0084750c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0083f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) · 呼出先 1件 [`00b3bf04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf04.md)
- 新版 呼出元 1件 [`00840888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/00840888.md) · 呼出先 1件 [`00b3cef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cef8.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0084658c",
      "incomplete_value": true,
      "site": "00846590",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "008465f4",
      "incomplete_value": true,
      "site": "008465f8",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00847610",
      "incomplete_value": true,
      "site": "00847614",
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
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 31,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00846590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846560.md#insn-00846590) · [`008465f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846560.md#insn-008465f8) · [`00846668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846560.md#insn-00846668)
- 新版 [`0084753c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/0084750c.md#insn-0084753c) · [`008475a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/0084750c.md#insn-008475a4) · [`00847614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/0084750c.md#insn-00847614)

~~~diff
- 00846590 ["INT_ADD", "register:40f0:8", ["const:846590:8", "const:4:8"]]
- 00846590 ["CALL", null, ["callee:00b3cef8:8"]]
+ 0084753c ["INT_ADD", "register:40f0:8", ["const:84753c:8", "const:4:8"]]
+ 0084753c ["CALL", null, ["callee:00b3cef8:8"]]
- 00846590 bytes 5dd60b94
+ 0084753c bytes 6fd60b94
- 008465f8 ["INT_ADD", "register:40f0:8", ["const:8465f8:8", "const:4:8"]]
- 008465f8 ["CALL", null, ["callee:00b3cef8:8"]]
+ 008475a4 ["INT_ADD", "register:40f0:8", ["const:8475a4:8", "const:4:8"]]
+ 008475a4 ["CALL", null, ["callee:00b3cef8:8"]]
- 008465f8 bytes 43d60b94
+ 008475a4 bytes 55d60b94
- 00846668 ["INT_ADD", "register:40f0:8", ["const:846668:8", "const:4:8"]]
- 00846668 ["CALL", null, ["callee:00b3cef8:8"]]
+ 00847614 ["INT_ADD", "register:40f0:8", ["const:847614:8", "const:4:8"]]
+ 00847614 ["CALL", null, ["callee:00b3cef8:8"]]
- 00846668 bytes 27d60b94
+ 00847614 bytes 39d60b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5ed63c029a6f3f56b0476294ebdfc27"></a>

### [`008466c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/008466c4.md) → [`00847670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/00847670.md) FUN_00847670

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) · 呼出先 2件 [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md)
- 新版 呼出元 1件 [`00840888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/00840888.md) · 呼出先 2件 [`0046eb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eb24.md) [`0046f258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f258.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 69.81% / 新版 69.81%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846718"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084671c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084671c"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00846718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/008466c4.md#insn-00846718) · [`0084671c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/008466c4.md#insn-0084671c) · [`00846720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/008466c4.md#insn-00846720)

~~~diff
- 00846718 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00846718 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00846718 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:a0:8"]]
- 00846718 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 00846718 bytes 1f0d0af8
- 0084671c ["COPY", "tmp:0:8", ["const:0:8"]]
- 0084671c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 0084671c ["COPY", "tmp:2:8", ["register:4040:8"]]
- 0084671c ["INT_ADD", "tmp:3:8", ["register:4000:8", "const:90:8"]]
- 0084671c bytes 1f2009a9
- 00846720 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00846720 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00846720 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00846720 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00846720 bytes 1ffc0aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-275ad361b228996645e5c08d613c7ddd"></a>

### [`00846924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846924.md) → [`008478d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/008478d0.md) FUN_008478d0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008472f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008472f4.md) · 呼出先 5件 [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`0078dd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dd04.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`008482a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008482a0.md) · 呼出先 5件 [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`0078e0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e0e0.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 75.00% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00847968",
      "incomplete_value": true,
      "site": "0084796c",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00847964",
      "incomplete_value": true,
      "site": "0084796c",
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
                "const:70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 7,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008469c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846924.md#insn-008469c0) · [`00846960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846924.md#insn-00846960) · [`00846970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846924.md#insn-00846970)
- 新版 [`0084796c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/008478d0.md#insn-0084796c) · [`0084790c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/008478d0.md#insn-0084790c) · [`0084791c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/008478d0.md#insn-0084791c)

~~~diff
- 008469c0 ["INT_ADD", "register:40f0:8", ["const:8469c0:8", "const:4:8"]]
- 008469c0 ["CALL", null, ["callee:00676e50:8"]]
+ 0084796c ["INT_ADD", "register:40f0:8", ["const:84796c:8", "const:4:8"]]
+ 0084796c ["CALL", null, ["callee:00676e50:8"]]
- 008469c0 bytes 38c0f897
+ 0084796c bytes 39bdf897
- 00846960 ["COPY", "register:0:8", ["register:4040:8"]]
- 00846960 ["INT_ADD", "register:40f0:8", ["const:846960:8", "const:4:8"]]
- 00846960 ["CALLIND", null, ["register:0:8"]]
+ 0084790c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0084790c ["INT_ADD", "register:40f0:8", ["const:84790c:8", "const:4:8"]]
+ 0084790c ["CALLIND", null, ["register:0:8"]]
- 00846960 bytes 00013fd6
+ 0084790c bytes 00013fd6
- 00846970 ["INT_ADD", "register:40f0:8", ["const:846970:8", "const:4:8"]]
- 00846970 ["CALL", null, ["callee:00c58f50:8"]]
+ 0084791c ["INT_ADD", "register:40f0:8", ["const:84791c:8", "const:4:8"]]
+ 0084791c ["CALL", null, ["callee:00c58f50:8"]]
- 00846970 bytes 84451094
+ 0084791c bytes 8d451094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20216fb9723c9a44f8d488545790971a"></a>

### [`008469fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/008469fc.md) → [`008479a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/008479a8.md) FUN_008479a8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 6件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`008689b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/008689b8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 6件 [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00869964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869964.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 93.83% / 新版 96.20%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008479c0",
      "incomplete_value": true,
      "site": "008479c4",
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
            "const:3e8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008479b8",
      "incomplete_value": true,
      "site": "008479c4",
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:3f0:8"
              ]
            ]
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


#### 変更候補の命令位置

- 旧版 [`00846a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/008469fc.md#insn-00846a18) · [`00846a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/008469fc.md#insn-00846a20) · [`00846a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/008469fc.md#insn-00846a2c)
- 新版 [`008479c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/008479a8.md#insn-008479c4) · [`008479cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/008479a8.md#insn-008479cc) · [`008479d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/008479a8.md#insn-008479d8)

~~~diff
- 00846a18 ["INT_ADD", "register:40f0:8", ["const:846a18:8", "const:4:8"]]
- 00846a18 ["CALL", null, ["callee:005c1b8c:8"]]
+ 008479c4 ["INT_ADD", "register:40f0:8", ["const:8479c4:8", "const:4:8"]]
+ 008479c4 ["CALL", null, ["callee:005c1b8c:8"]]
- 00846a18 bytes 71ebf597
+ 008479c4 bytes 72e8f597
- 00846a20 ["BRANCH", null, ["local:b3:8"]]
+ 008479cc ["BRANCH", null, ["local:b2:8"]]
- 00846a20 bytes 04000014
+ 008479cc bytes 04000014
- 00846a2c ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 008479d8 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00846a2c bytes 20020054
+ 008479d8 bytes 20020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86d64959fdead8d7d0f5ee9d1aaaf0c5"></a>

### [`00846ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ca8.md) → [`00847c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/00847c54.md) FUN_00847c54

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 5件 [`006a2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2bd0.md) [`00866da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866da0.md) [`008670c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/008670c0.md) [`00868a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868a50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 5件 [`006a2f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a2/006a2f80.md) [`00867d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00867/00867d4c.md) [`0086806c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00868/0086806c.md) [`008699fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/008699fc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 60.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00846d18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00847cc4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00847cec",
      "incomplete_value": true,
      "site": "00847cf0",
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
            "const:7360:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00846d18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00847cdc"
      ]
    ]
  ],
  "added": [
    [
      "00847cc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00847cdc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00846d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ca8.md#insn-00846d18) · [`00846d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ca8.md#insn-00846d44)
- 新版 [`00847cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/00847c54.md#insn-00847cf0) · [`00847cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/00847c54.md#insn-00847cc4)

~~~diff
- 00846d18 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00846d18 bytes c0000054
- 00846d44 ["INT_ADD", "register:40f0:8", ["const:846d44:8", "const:4:8"]]
- 00846d44 ["CALL", null, ["callee:008699fc:8"]]
+ 00847cf0 ["INT_ADD", "register:40f0:8", ["const:847cf0:8", "const:4:8"]]
+ 00847cf0 ["CALL", null, ["callee:008699fc:8"]]
- 00846d44 bytes 43870094
+ 00847cf0 bytes 43870094
+ 00847cc4 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
+ 00847cc4 bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba7c3b3823693e6939c2a142a85773fa"></a>

### [`00846d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846d68.md) → [`00847d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/00847d14.md) FUN_00847d14

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 7件 [`005b9f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9f24.md) [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md) [`005d8ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8ca4.md) [`00847734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847734.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 7件 [`005ba2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005ba2d4.md) [`005c426c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c426c.md) [`005d9054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d9/005d9054.md) [`008486e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008486e0.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 38.71% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846d68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846d68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846d6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00846d68",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00846d6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00846d70",
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
      "00847d14",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00847d18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00847d1c",
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

- 旧版 [`00846d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846d68.md#insn-00846d68) · [`00846d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846d68.md#insn-00846d6c) · [`00846d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846d68.md#insn-00846d70)

~~~diff
- 00846d68 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00846d68 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00846d68 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00846d68 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00846d68 bytes fd7bbda9
- 00846d6c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00846d6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00846d6c bytes f50b00f9
- 00846d70 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00846d70 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00846d70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00846d70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00846d70 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70612b401d4d47b33052814b3beaee3f"></a>

### [`00846ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ebc.md) → [`00847e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/00847e68.md) FUN_00847e68

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 5件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`00672788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00672/00672788.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 5件 [`0046ec04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ec04.md) [`0046f33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f33c.md) [`00672b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00672/00672b38.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 11.54% / 新版 13.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00846f10"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00846f60"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00846f98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00846f10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00847ed8"
      ]
    ],
    [
      "unmatched:00846f60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00847f28"
      ]
    ],
    [
      "unmatched:00846f98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00847f58"
      ]
    ]
  ],
  "added": [
    [
      "00847ebc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00847ed8"
      ]
    ],
    [
      "00847f0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00847f28"
      ]
    ],
    [
      "00847f44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00847f58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00846f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ebc.md#insn-00846f0c) · [`00846f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ebc.md#insn-00846f10) · [`00846f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ebc.md#insn-00846f60)
- 新版 [`00847eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/00847e68.md#insn-00847eb8)

~~~diff
- 00846f0c ["INT_ADD", "register:40f0:8", ["const:846f0c:8", "const:4:8"]]
- 00846f0c ["CALL", null, ["callee:00c54d90:8"]]
+ 00847eb8 ["INT_ADD", "register:40f0:8", ["const:847eb8:8", "const:4:8"]]
+ 00847eb8 ["CALL", null, ["callee:00c54d90:8"]]
- 00846f0c bytes a5331094
+ 00847eb8 bytes b6331094
- 00846f10 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00846f10 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00846f10 bytes e00000b5
- 00846f60 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00846f60 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00846f60 bytes e00000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6132e01b5d73d59104c9632be523ca22"></a>

### [`00846ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ffc.md) → [`00847fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/00847fa8.md) FUN_00847fa8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 3件 [`0078dd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dd04.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 3件 [`0078e0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e0e0.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.93% / 新版 70.93%

CFGの説明率　旧版 40.54% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846ffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846ffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00847000"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00846ffc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00847000",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00847020",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00847fe8"
      ]
    ]
  ],
  "added": [
    [
      "00847fa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00847fac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00847fcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00847fe8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00846ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ffc.md#insn-00846ffc) · [`00847000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ffc.md#insn-00847000) · [`00847020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ffc.md#insn-00847020)

~~~diff
- 00846ffc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00846ffc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00846ffc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00846ffc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00846ffc bytes fd7bbea9
- 00847000 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00847000 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00847000 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00847000 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00847000 bytes f44f01a9
- 00847020 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00847020 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00847020 bytes e00000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-882556c25347a10745dd92e399a3b72a"></a>

### [`008471a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008471a4.md) → [`00848150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848150.md) FUN_00848150

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c426c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c426c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 68.97% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00847270"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0084821c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0084819c",
      "incomplete_value": true,
      "site": "008481a0",
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
            "const:68:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00848214",
      "DATA",
      [
        "storage",
        "00c8a550",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00847270",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008481dc"
      ]
    ]
  ],
  "added": [
    [
      "00848214",
      "DATA",
      [
        "storage",
        "00c8b520",
        null,
        "undefined *"
      ]
    ],
    [
      "0084821c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008481dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008471f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008471a4.md#insn-008471f4) · [`00847270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008471a4.md#insn-00847270)
- 新版 [`008481a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848150.md#insn-008481a0) · [`0084821c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848150.md#insn-0084821c)

~~~diff
- 008471f4 ["INT_ADD", "register:40f0:8", ["const:8471f4:8", "const:4:8"]]
- 008471f4 ["CALL", null, ["callee:005c426c:8"]]
+ 008481a0 ["INT_ADD", "register:40f0:8", ["const:8481a0:8", "const:4:8"]]
+ 008481a0 ["CALL", null, ["callee:005c426c:8"]]
- 008471f4 bytes 32f3f597
+ 008481a0 bytes 33f0f597
- 00847270 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00847270 bytes 00feff54
+ 0084821c ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 0084821c bytes 00feff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bca7e959ac8e5de2b77f2245b3c0f0cb"></a>

### [`008472f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008472f4.md) → [`008482a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008482a0.md) FUN_008482a0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 6件 [`0067e628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e628.md) [`00846924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846924.md) [`00868cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868cbc.md) [`00868da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868da4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 6件 [`0067e9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0067e/0067e9d8.md) [`008478d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/008478d0.md) [`00869c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869c68.md) [`00869d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869d50.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 79.03% / 新版 79.03%

CFGの説明率　旧版 33.33% / 新版 40.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00847350"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00847380"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008473b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00847350",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848318"
      ]
    ],
    [
      "unmatched:00847380",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848348"
      ]
    ],
    [
      "unmatched:008473b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848374"
      ]
    ]
  ],
  "added": [
    [
      "008482fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848318"
      ]
    ],
    [
      "0084832c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848348"
      ]
    ],
    [
      "00848364",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00848374"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084734c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008472f4.md#insn-0084734c) · [`00847350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008472f4.md#insn-00847350) · [`00847380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008472f4.md#insn-00847380)
- 新版 [`008482f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008482a0.md#insn-008482f8)

~~~diff
- 0084734c ["INT_ADD", "register:40f0:8", ["const:84734c:8", "const:4:8"]]
- 0084734c ["CALL", null, ["callee:00c54d90:8"]]
+ 008482f8 ["INT_ADD", "register:40f0:8", ["const:8482f8:8", "const:4:8"]]
+ 008482f8 ["CALL", null, ["callee:00c54d90:8"]]
- 0084734c bytes 95321094
+ 008482f8 bytes a6321094
- 00847350 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00847350 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00847350 bytes e00000b5
- 00847380 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00847380 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00847380 bytes e00000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08abb1647ace821c81eed6a3de789430"></a>

### [`00847538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847538.md) → [`008484e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008484e4.md) FUN_008484e4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005fe2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe2d8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005fe688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fe688.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 81.82% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084754c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847538.md#insn-0084754c) · [`00847560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847538.md#insn-00847560) · [`00847564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847538.md#insn-00847564)
- 新版 [`008484f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008484e4.md#insn-008484f8) · [`0084850c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008484e4.md#insn-0084850c) · [`00848510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008484e4.md#insn-00848510)

~~~diff
- 0084754c ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 0084754c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 008484f8 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 008484f8 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 0084754c bytes 150300b4
+ 008484f8 bytes 150300b4
- 00847560 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00847560 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0084850c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0084850c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00847560 bytes 81000054
+ 0084850c bytes 81000054
- 00847564 ["BRANCH", null, ["local:b7:8"]]
+ 00848510 ["BRANCH", null, ["local:b8:8"]]
- 00847564 bytes 0d000014
+ 00848510 bytes 0d000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26f3cb530bbc0b59c9ebdba5ffd0dd4d"></a>

### [`00847704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847704.md) → [`008486b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008486b0.md) FUN_008486b0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0086950c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/0086950c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0086a4b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a4b8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084771c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847704.md#insn-0084771c)
- 新版 [`008486c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/008486b0.md#insn-008486c8)

~~~diff
- 0084771c ["INT_ADD", "register:40f0:8", ["const:84771c:8", "const:4:8"]]
- 0084771c ["CALL", null, ["callee:0086a4b8:8"]]
+ 008486c8 ["INT_ADD", "register:40f0:8", ["const:8486c8:8", "const:4:8"]]
+ 008486c8 ["CALL", null, ["callee:0086a4b8:8"]]
- 0084771c bytes 7c870094
+ 008486c8 bytes 7c870094
~~~


<a id="compare-b323a5a9deaa9eb3b6c670a05143eb05"></a>

### [`008478b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008478b8.md) → [`00848864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848864.md) FUN_00848864

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 11件 [`005b9f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9f24.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`0083027c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083027c.md)
- 新版 呼出元 1件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 11件 [`005ba2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ba/005ba2d4.md) [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`005c426c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c426c.md) [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`00831228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831228.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00847988",
      "incomplete_value": true,
      "site": "00847990",
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00847990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008478b8.md#insn-00847990) · [`008478d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008478b8.md#insn-008478d0) · [`008478dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008478b8.md#insn-008478dc)
- 新版 [`0084893c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848864.md#insn-0084893c) · [`0084887c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848864.md#insn-0084887c) · [`00848888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848864.md#insn-00848888)

~~~diff
- 00847990 ["INT_ADD", "register:40f0:8", ["const:847990:8", "const:4:8"]]
- 00847990 ["CALL", null, ["callee:00831610:8"]]
+ 0084893c ["INT_ADD", "register:40f0:8", ["const:84893c:8", "const:4:8"]]
+ 0084893c ["CALL", null, ["callee:00831610:8"]]
- 00847990 bytes 35a3ff97
+ 0084893c bytes 35a3ff97
- 008478d0 ["INT_ADD", "register:40f0:8", ["const:8478d0:8", "const:4:8"]]
- 008478d0 ["CALL", null, ["callee:00831558:8"]]
+ 0084887c ["INT_ADD", "register:40f0:8", ["const:84887c:8", "const:4:8"]]
+ 0084887c ["CALL", null, ["callee:00831558:8"]]
- 008478d0 bytes 37a3ff97
+ 0084887c bytes 37a3ff97
- 008478dc ["INT_ADD", "register:40f0:8", ["const:8478dc:8", "const:4:8"]]
- 008478dc ["CALL", null, ["callee:005c426c:8"]]
+ 00848888 ["INT_ADD", "register:40f0:8", ["const:848888:8", "const:4:8"]]
+ 00848888 ["CALL", null, ["callee:005c426c:8"]]
- 008478dc bytes 78f1f597
+ 00848888 bytes 79eef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21beda7be9e9231b30aaf3b2ebf959cd"></a>

### [`008479c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008479c0.md) → [`0084896c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/0084896c.md) FUN_0084896c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 21.43% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008479e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008479f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00848994"
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
      "unmatched:008479e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008489a8"
      ]
    ],
    [
      "unmatched:008479f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008489dc"
      ]
    ],
    [
      "008489ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008479f0"
      ]
    ]
  ],
  "added": [
    [
      "00848994",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008489a8"
      ]
    ],
    [
      "008489a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008489dc"
      ]
    ],
    [
      "008489ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0084899c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008479e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008479c0.md#insn-008479e8) · [`008479f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008479c0.md#insn-008479f8) · [`00847a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008479c0.md#insn-00847a0c)
- 新版 [`008489b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/0084896c.md#insn-008489b8)

~~~diff
- 008479e8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008479e8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 008479e8 bytes a1000054
- 008479f8 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 008479f8 bytes c0010054
- 00847a0c ["INT_ADD", "register:40f0:8", ["const:847a0c:8", "const:4:8"]]
- 00847a0c ["CALL", null, ["callee:00c54d90:8"]]
+ 008489b8 ["INT_ADD", "register:40f0:8", ["const:8489b8:8", "const:4:8"]]
+ 008489b8 ["CALL", null, ["callee:00c54d90:8"]]
- 00847a0c bytes e5301094
+ 008489b8 bytes f6301094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b578c6d95f7e6d88bb3bcfb2c4c00dd7"></a>

### [`00847b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847b50.md) → [`00848afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848afc.md) FUN_00848afc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0062a4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062a/0062a4a0.md) [`00865d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865d00.md) [`008695a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008695a0.md) [`008697dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008697dc.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0062a850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062a/0062a850.md) [`00866cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866cac.md) [`0086a54c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a54c.md) [`0086a788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a788.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847b50.md#insn-00847b68) · [`00847b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847b50.md#insn-00847b74) · [`00847b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847b50.md#insn-00847b7c)
- 新版 [`00848b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848afc.md#insn-00848b14) · [`00848b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848afc.md#insn-00848b20) · [`00848b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848afc.md#insn-00848b28)

~~~diff
- 00847b68 ["INT_ADD", "register:40f0:8", ["const:847b68:8", "const:4:8"]]
- 00847b68 ["CALL", null, ["callee:0062a850:8"]]
+ 00848b14 ["INT_ADD", "register:40f0:8", ["const:848b14:8", "const:4:8"]]
+ 00848b14 ["CALL", null, ["callee:0062a850:8"]]
- 00847b68 bytes 4e8af797
+ 00848b14 bytes 4f87f797
- 00847b74 ["INT_ADD", "register:40f0:8", ["const:847b74:8", "const:4:8"]]
- 00847b74 ["CALL", null, ["callee:0086a788:8"]]
+ 00848b20 ["INT_ADD", "register:40f0:8", ["const:848b20:8", "const:4:8"]]
+ 00848b20 ["CALL", null, ["callee:0086a788:8"]]
- 00847b74 bytes 1a870094
+ 00848b20 bytes 1a870094
- 00847b7c ["INT_ADD", "register:40f0:8", ["const:847b7c:8", "const:4:8"]]
- 00847b7c ["CALL", null, ["callee:0086a54c:8"]]
+ 00848b28 ["INT_ADD", "register:40f0:8", ["const:848b28:8", "const:4:8"]]
+ 00848b28 ["CALL", null, ["callee:0086a54c:8"]]
- 00847b7c bytes 89860094
+ 00848b28 bytes 89860094
~~~


<a id="compare-26e70a17019c9d791f023d3d7510dc66"></a>

### [`00847b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847b90.md) → [`00848b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848b3c.md) FUN_00848b3c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00869820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869820.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0086a7cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a7cc.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 72.00% / 新版 78.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00848bac",
      "incomplete_value": true,
      "site": "00848bb0",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00847c00",
      "incomplete_value": true,
      "site": "00847c04",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00847c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847b90.md#insn-00847c04) · [`00847bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847b90.md#insn-00847bb4) · [`00847bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847b90.md#insn-00847bb8)
- 新版 [`00848bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848b3c.md#insn-00848bb0) · [`00848b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848b3c.md#insn-00848b60) · [`00848b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848b3c.md#insn-00848b64)

~~~diff
- 00847c04 ["INT_ADD", "register:40f0:8", ["const:847c04:8", "const:4:8"]]
- 00847c04 ["CALL", null, ["callee:0086a7cc:8"]]
+ 00848bb0 ["INT_ADD", "register:40f0:8", ["const:848bb0:8", "const:4:8"]]
+ 00848bb0 ["CALL", null, ["callee:0086a7cc:8"]]
- 00847c04 bytes 07870094
+ 00848bb0 bytes 07870094
- 00847bb4 ["INT_ADD", "register:40f0:8", ["const:847bb4:8", "const:4:8"]]
- 00847bb4 ["CALL", null, ["callee:00c54d90:8"]]
+ 00848b60 ["INT_ADD", "register:40f0:8", ["const:848b60:8", "const:4:8"]]
+ 00848b60 ["CALL", null, ["callee:00c54d90:8"]]
- 00847bb4 bytes 7b301094
+ 00848b60 bytes 8c301094
- 00847bb8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00847bb8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00848b64 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00848b64 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00847bb8 bytes 800300b4
+ 00848b64 bytes 800300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

